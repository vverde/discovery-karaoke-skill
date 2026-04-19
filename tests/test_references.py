"""
test_references.py — M-code cross-reference integrity for the Discovery Karaoke skill.

Validates that all M-codes referenced across command files, templates, and SKILL.md
actually exist in data/methods-index.md. Catches broken references introduced by
renaming, removing, or adding methods.

No Claude API calls. Run from the skill root:

    pytest tests/ -v

"""
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

SKILL_ROOT = Path(__file__).parent.parent


def skill_path(*parts) -> Path:
    return SKILL_ROOT.joinpath(*parts)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract_m_codes(text: str) -> set[str]:
    """Extract all M## references (e.g. M1, M23, M89) from a text string."""
    return set(re.findall(r'\bM\d+\b', text))


def get_active_m_codes_from_index() -> set[str]:
    """Parse data/methods-index.md and return the set of active M-codes."""
    content = read(skill_path("data/methods-index.md"))
    # Each data row starts with "| M## |" — extract those IDs
    return set(re.findall(r'^\|\s*(M\d+)\s*\|', content, re.MULTILINE))


def get_superseded_m_codes() -> set[str]:
    """Return known superseded M-codes from data/constants.md."""
    content = read(skill_path("data/constants.md"))
    # Match the line listing actual codes (e.g. "Superseded: M25, M30, M46")
    # Skips the count line ("Superseded: 3") by requiring the line to start with M
    match = re.search(r'Superseded:\s*(M\d+.*)', content)
    if not match:
        return set()
    return set(re.findall(r'M\d+', match.group(1)))


def get_known_gap_m_codes() -> set[str]:
    """Return known gap M-codes (intentional gaps in the ID range) from data/constants.md."""
    content = read(skill_path("data/constants.md"))
    match = re.search(r'Known gaps:\s*([^\n]+)', content)
    if not match:
        return set()
    # Expand ranges like M50–M52 into individual codes
    raw = match.group(1)
    codes = set()
    for part in re.split(r'[,\s]+', raw):
        range_match = re.match(r'M(\d+)[–-]M?(\d+)', part)
        if range_match:
            for n in range(int(range_match.group(1)), int(range_match.group(2)) + 1):
                codes.add(f"M{n}")
        elif re.match(r'M\d+', part):
            codes.add(re.match(r'M\d+', part).group())
    return codes


def strip_html_comments(text: str) -> str:
    """Remove HTML comment blocks (<!-- ... -->) from text before M-code extraction."""
    return re.sub(r'<!--.*?-->', '', text, flags=re.DOTALL)


# ---------------------------------------------------------------------------
# 1. Index count matches constants.md
# ---------------------------------------------------------------------------

def test_index_active_count_matches_constants():
    """Total active entry count in methods-index.md must match 'Total active entries' in constants.md."""
    constants = read(skill_path("data/constants.md"))
    match = re.search(r'Total active entries:\s*(\d+)', constants)
    assert match, "Could not find 'Total active entries:' in data/constants.md"
    expected_count = int(match.group(1))

    index_codes = get_active_m_codes_from_index()
    assert len(index_codes) == expected_count, (
        f"methods-index.md has {len(index_codes)} active entries, "
        f"but constants.md says {expected_count}. "
        f"Run python3 local/generate_index.py to regenerate."
    )


def test_index_has_no_superseded_codes():
    """Superseded M-codes must not appear as active rows in methods-index.md."""
    superseded = get_superseded_m_codes()
    active = get_active_m_codes_from_index()
    overlap = superseded & active
    assert not overlap, (
        f"Superseded M-codes appear as active in methods-index.md: {sorted(overlap)}"
    )


# ---------------------------------------------------------------------------
# 2. SKILL.md M-code references exist in the index
# ---------------------------------------------------------------------------

def test_skill_md_m_code_references_exist():
    """All M## codes in SKILL.md guardrails must exist in the active index or be known gaps/superseded."""
    content = read(skill_path("SKILL.md"))
    active = get_active_m_codes_from_index()
    superseded = get_superseded_m_codes()
    gaps = get_known_gap_m_codes()

    refs = extract_m_codes(content)
    broken = refs - active - superseded - gaps
    assert not broken, (
        f"SKILL.md references M-codes not in the active index: {sorted(broken)}"
    )


# ---------------------------------------------------------------------------
# 3. G4 M-code references in SKILL.md
# ---------------------------------------------------------------------------

def test_skill_md_g4_m_codes_exist():
    """G4 references M75, M76, M89, M91 — all must be active."""
    active = get_active_m_codes_from_index()
    required = {"M75", "M76", "M89", "M91"}
    missing = required - active
    assert not missing, (
        f"G4-referenced M-codes not found in active index: {sorted(missing)}"
    )


# ---------------------------------------------------------------------------
# 4. assess.md signal pre-fill table M-code references
# ---------------------------------------------------------------------------

def test_assess_signal_table_m_codes_exist():
    """All M## codes referenced in the assess.md signal pre-fill table must be active."""
    content = read(skill_path("commands/assess.md"))
    active = get_active_m_codes_from_index()
    superseded = get_superseded_m_codes()

    refs = extract_m_codes(content)
    broken = refs - active - superseded
    assert not broken, (
        f"assess.md references M-codes not in the active index: {sorted(broken)}"
    )


# ---------------------------------------------------------------------------
# 5. risk-method-matrix.md M-code references
# ---------------------------------------------------------------------------

def test_risk_matrix_m_codes_exist():
    """All M## codes in risk-method-matrix.md must exist in the active index (HTML comments excluded)."""
    raw = read(skill_path("data/risk-method-matrix.md"))
    content = strip_html_comments(raw)
    active = get_active_m_codes_from_index()
    superseded = get_superseded_m_codes()
    gaps = get_known_gap_m_codes()

    refs = extract_m_codes(content)
    broken = refs - active - superseded - gaps
    assert not broken, (
        f"risk-method-matrix.md references M-codes not in the active index: {sorted(broken)}"
    )


# ---------------------------------------------------------------------------
# 6. All command files — M-code references
# ---------------------------------------------------------------------------

def test_command_files_m_codes_exist():
    """All M## codes in command files must exist in the active index or be superseded."""
    active = get_active_m_codes_from_index()
    superseded = get_superseded_m_codes()
    violations = {}

    for f in skill_path("commands").glob("*.md"):
        refs = extract_m_codes(f.read_text(encoding="utf-8"))
        broken = refs - active - superseded
        if broken:
            violations[f.name] = sorted(broken)

    assert not violations, (
        f"Command files reference M-codes not in the active index: {violations}"
    )


# ---------------------------------------------------------------------------
# 7. recommendation-template.md guardrail references
# ---------------------------------------------------------------------------

def test_recommendation_template_guardrail_refs_exist():
    """G-code references in recommendation-template.md must match defined guardrails."""
    content = read(skill_path("templates/recommendation-template.md"))
    skill_content = read(skill_path("SKILL.md"))

    g_refs = set(re.findall(r'\bG\d+\b', content))
    defined_guardrails = set(re.findall(r'### (G\d+):', skill_content))
    broken = g_refs - defined_guardrails
    assert not broken, (
        f"recommendation-template.md references undefined guardrails: {sorted(broken)}"
    )


# ---------------------------------------------------------------------------
# 8. anti-patterns.md — count matches constants.md
# ---------------------------------------------------------------------------

def test_anti_pattern_count_matches_constants():
    """Number of anti-patterns in data/anti-patterns.md must match constants.md."""
    constants = read(skill_path("data/constants.md"))
    match = re.search(r'Anti-patterns:\s*(\d+)', constants)
    assert match, "Could not find 'Anti-patterns:' in data/constants.md"
    expected = int(match.group(1))

    content = read(skill_path("data/anti-patterns.md"))
    # Anti-patterns use "### N. Name" headers (three hashes)
    found = len(re.findall(r'^###\s+\d+\.\s', content, re.MULTILINE))
    assert found == expected, (
        f"data/anti-patterns.md has {found} patterns, constants.md says {expected}."
    )


# ---------------------------------------------------------------------------
# 9. constants.md tier counts match methods-index.md
# ---------------------------------------------------------------------------

def test_tier_counts_match_constants():
    """Core/Extended/Specialist counts in methods-index.md must match constants.md."""
    constants = read(skill_path("data/constants.md"))
    index_content = read(skill_path("data/methods-index.md"))

    for tier in ("Core", "Extended", "Specialist"):
        match = re.search(rf'{tier}:\s*(\d+)', constants)
        if not match:
            continue
        expected = int(match.group(1))
        actual = len(re.findall(rf'\|\s*{tier}\s*\|', index_content))
        assert actual == expected, (
            f"Tier '{tier}': methods-index.md has {actual}, constants.md says {expected}."
        )


# ---------------------------------------------------------------------------
# 10. data/methods-index.md is not stale vs discovery-methods-full.md
# ---------------------------------------------------------------------------

def test_index_is_not_older_than_source():
    """methods-index.md should not be older than discovery-methods-full.md."""
    index = skill_path("data/methods-index.md")
    source = skill_path("data/discovery-methods-full.md")

    index_mtime = index.stat().st_mtime
    source_mtime = source.stat().st_mtime

    assert index_mtime >= source_mtime, (
        "data/methods-index.md is older than data/discovery-methods-full.md. "
        "Run: python3 local/generate_index.py"
    )


# ---------------------------------------------------------------------------
# 11. context tool count matches constants.md
# ---------------------------------------------------------------------------

CONTEXT_TOOL_TYPES = {"Synthesis Tool", "Framework", "Operating Practice"}


def get_context_tool_count_from_index() -> int:
    """Count rows in methods-index.md whose Type column is a context tool type."""
    content = read(skill_path("data/methods-index.md"))
    count = 0
    for row in re.findall(r'^\|.*\|$', content, re.MULTILINE):
        cols = [c.strip() for c in row.split('|')]
        # Type is column index 6 (after empty, ID, Name, PrimaryRisk, Stage, Category, Type, ...)
        if len(cols) > 7 and cols[6] in CONTEXT_TOOL_TYPES:
            count += 1
    return count


def test_context_tool_count_matches_constants():
    """Context tool count in methods-index.md must match 'Context tools:' in constants.md."""
    constants = read(skill_path("data/constants.md"))
    match = re.search(r'Context tools:\s*(\d+)', constants)
    assert match, "Could not find 'Context tools:' in data/constants.md"
    expected = int(match.group(1))

    actual = get_context_tool_count_from_index()
    assert actual == expected, (
        f"methods-index.md has {actual} context tool rows, "
        f"but constants.md says {expected}. "
        f"Run python3 local/generate_index.py to regenerate."
    )


def test_active_method_count_matches_constants():
    """Active method count (non-context-tools) in methods-index.md must match 'Active methods:' in constants.md."""
    constants = read(skill_path("data/constants.md"))
    match = re.search(r'Active methods:\s*(\d+)', constants)
    assert match, "Could not find 'Active methods:' in data/constants.md"
    expected = int(match.group(1))

    total_active = len(get_active_m_codes_from_index())
    ct_count = get_context_tool_count_from_index()
    actual = total_active - ct_count
    assert actual == expected, (
        f"methods-index.md has {actual} active methods (total {total_active} minus {ct_count} context tools), "
        f"but constants.md says {expected}."
    )


# ---------------------------------------------------------------------------
# 12. guardrail count in constants.md matches SKILL.md
# ---------------------------------------------------------------------------

def test_guardrail_count_matches_constants():
    """Number of G#: headers in SKILL.md must match 'Guardrails:' in constants.md."""
    constants = read(skill_path("data/constants.md"))
    match = re.search(r'Guardrails:\s*(\d+)', constants)
    assert match, "Could not find 'Guardrails:' in data/constants.md"
    expected = int(match.group(1))

    skill_content = read(skill_path("SKILL.md"))
    actual = len(re.findall(r'^### G\d+:', skill_content, re.MULTILINE))
    assert actual == expected, (
        f"SKILL.md defines {actual} guardrails, but constants.md says {expected}."
    )


# ---------------------------------------------------------------------------
# 13. M-code numeric range stays within M1–M96
# ---------------------------------------------------------------------------

def test_m_codes_within_declared_range():
    """All active M-codes in methods-index.md must be within the M1–M96 range declared in constants.md."""
    active = get_active_m_codes_from_index()
    out_of_range = {code for code in active if int(code[1:]) > 96 or int(code[1:]) < 1}
    assert not out_of_range, (
        f"Active M-codes outside declared M1–M96 range: {sorted(out_of_range)}. "
        f"Update the ID range in data/constants.md if the DB has grown."
    )
