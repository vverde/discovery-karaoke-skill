"""
test_structure.py — Static structure validation for the Discovery Karaoke skill.

Tests file presence, required sections, and template integrity.
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


# ---------------------------------------------------------------------------
# 1. File presence — all files referenced in the Command Router must exist
# ---------------------------------------------------------------------------

COMMAND_FILES = [
    "commands/help.md",
    "commands/about.md",
    "commands/assess.md",
    "commands/quick.md",
    "commands/list.md",
    "commands/describe.md",
    "commands/compare.md",
    "commands/matrix.md",
    "commands/diagnose.md",
    "commands/review.md",
    "commands/ai.md",
    "commands/config.md",
    "commands/plan.md",
    "commands/answer.md",   # smart fallback handler — not user-facing but required
]

TEMPLATE_FILES = [
    "templates/recommendation-template.md",
    "templates/quick-template.md",
    "templates/plan-template.md",
    "templates/review-template.md",
    "templates/comparison-template.md",
    "templates/describe-template.md",
    "templates/list-template.md",
    "templates/matrix-template.md",
    "templates/diagnostic-template.md",
    "templates/answer-template.md",
]

DATA_FILES = [
    "data/discovery-methods-full.md",
    "data/methods-index.md",
    "data/risk-method-matrix.md",
    "data/anti-patterns.md",
    "data/ai-guardrails.md",
    "data/constants.md",
    "data/about.md",
]

ROOT_FILES = [
    "SKILL.md",
]


def test_command_files_exist():
    missing = [f for f in COMMAND_FILES if not skill_path(f).exists()]
    assert not missing, f"Missing command files: {missing}"


def test_template_files_exist():
    missing = [f for f in TEMPLATE_FILES if not skill_path(f).exists()]
    assert not missing, f"Missing template files: {missing}"


def test_data_files_exist():
    missing = [f for f in DATA_FILES if not skill_path(f).exists()]
    assert not missing, f"Missing data files: {missing}"


def test_root_files_exist():
    missing = [f for f in ROOT_FILES if not skill_path(f).exists()]
    assert not missing, f"Missing root files: {missing}"


# ---------------------------------------------------------------------------
# 2. SKILL.md — guardrail and command router integrity
# ---------------------------------------------------------------------------

def test_skill_md_has_all_guardrails():
    """G1 through G11 must all be defined in SKILL.md."""
    content = read(skill_path("SKILL.md"))
    missing = [f"G{i}" for i in range(1, 12) if f"### G{i}:" not in content]
    assert not missing, f"Missing guardrail definitions in SKILL.md: {missing}"


def test_skill_md_command_router_has_all_commands():
    """All 13 user-facing commands must appear in the Command Router table."""
    content = read(skill_path("SKILL.md"))
    commands = [
        "help", "about", "assess", "quick", "list",
        "describe", "compare", "matrix", "diagnose",
        "review", "ai", "config", "plan",
    ]
    missing = [cmd for cmd in commands if f"`{cmd}`" not in content]
    assert not missing, f"Commands missing from SKILL.md router: {missing}"


def test_skill_md_no_t_codes():
    """No deprecated T## codes anywhere in SKILL.md."""
    content = read(skill_path("SKILL.md"))
    t_codes = re.findall(r'\bT\d+\b', content)
    assert not t_codes, f"Deprecated T-codes found in SKILL.md: {t_codes}"


# ---------------------------------------------------------------------------
# 3. Template integrity — RENDER GATEs and required sections
# ---------------------------------------------------------------------------

def test_quick_template_has_render_gate():
    """quick-template.md must contain a RENDER GATE (Issue 1 fix)."""
    content = read(skill_path("templates/quick-template.md"))
    assert "RENDER GATE" in content, (
        "quick-template.md is missing the RENDER GATE block. "
        "Small bets will incorrectly show 3 methods."
    )


def test_recommendation_template_has_render_gate():
    """recommendation-template.md must contain a RENDER GATE."""
    content = read(skill_path("templates/recommendation-template.md"))
    assert "RENDER GATE" in content, (
        "recommendation-template.md is missing the RENDER GATE block."
    )


def test_quick_template_header_is_not_top_3():
    """quick-template.md must not have 'Top 3 Methods' as a section header (Issue 1 fix)."""
    content = read(skill_path("templates/quick-template.md"))
    assert "## Top 3 Methods" not in content, (
        "'## Top 3 Methods' header found — should be '## Top Methods' after Issue 1 fix."
    )


def test_recommendation_template_has_karaoke_check():
    content = read(skill_path("templates/recommendation-template.md"))
    assert "Karaoke Check" in content, (
        "recommendation-template.md missing Karaoke Check section."
    )


def test_recommendation_template_has_evidence_convergence():
    content = read(skill_path("templates/recommendation-template.md"))
    assert "Evidence Convergence" in content, (
        "recommendation-template.md missing Evidence Convergence Map section."
    )


def test_plan_template_has_decision_gates():
    content = read(skill_path("templates/plan-template.md"))
    assert "Decision Gate" in content, (
        "plan-template.md missing Decision Gate section."
    )


def test_plan_template_stage3_has_blast_radius_guard():
    """Stage 3 must explicitly restrict itself to medium/large bets (Issue 7 fix)."""
    content = read(skill_path("templates/plan-template.md"))
    assert "medium/large bets only" in content or "skip entirely for small bets" in content, (
        "plan-template.md Stage 3 is missing blast-radius restriction note."
    )


def test_review_template_has_6_symptom_checklist():
    content = read(skill_path("templates/review-template.md"))
    # The checklist uses numbered rows — check at least 6 are present
    rows = re.findall(r'\|\s*\d+\s*\|', content)
    assert len(rows) >= 6, (
        f"review-template.md symptom checklist has {len(rows)} rows, expected at least 6."
    )


# ---------------------------------------------------------------------------
# 4. assess.md — new signals and guardrail wiring (Issues 5, 6, 8, 9, 12)
# ---------------------------------------------------------------------------

def test_assess_has_extended_compliance_signals():
    """Issue 5 fix: new regulatory keyword rows must be present."""
    content = read(skill_path("commands/assess.md"))
    required_signals = ["CCPA", "PSD2", "COPPA", "employment", "automated decision"]
    missing = [s for s in required_signals if s not in content]
    assert not missing, f"assess.md missing compliance signal rows: {missing}"


def test_assess_has_org_readiness_signals():
    """Issue 9 fix: org-readiness flag rows must be present."""
    content = read(skill_path("commands/assess.md"))
    required = ["already decided", "leadership wants", "roadmap committed", "need to justify"]
    missing = [s for s in required if s not in content]
    assert not missing, f"assess.md missing org-readiness signal rows: {missing}"


def test_assess_has_ai_probe_question():
    """Issue 6 fix: optional AI research question must be in Batch 1."""
    content = read(skill_path("commands/assess.md"))
    assert "AI tools to generate user insights" in content, (
        "assess.md missing optional AI research probe question in Batch 1."
    )


def test_assess_has_framing_check():
    """Issue 8 fix: solution-framed vs problem-framed check must be in Step 3.4."""
    content = read(skill_path("commands/assess.md"))
    assert "Framing check" in content, (
        "assess.md missing framing check in Step 3.4."
    )
    assert "solution-framed" in content.lower(), (
        "assess.md framing check missing 'solution-framed' detection."
    )


def test_assess_config_check_has_no_age_warning():
    """Issue 12 fix: 6-month age warning must be removed from Step 1."""
    content = read(skill_path("commands/assess.md"))
    assert "6 months" not in content, (
        "assess.md still contains the 6-month age warning — should be removed (Issue 12 fix)."
    )


def test_assess_batch3_regulated_question_is_expanded():
    """Issue 5 fix: Batch 3 regulated question must enumerate regulated categories."""
    content = read(skill_path("commands/assess.md"))
    assert "employment decisions" in content, (
        "assess.md Batch 3 regulated question missing enumerated categories (Issue 5 fix)."
    )


# ---------------------------------------------------------------------------
# 5. SKILL.md G7 — no age-based warning (Issue 12 fix)
# ---------------------------------------------------------------------------

def test_skill_md_g7_no_age_warning():
    """Issue 12 fix: G7 must not contain a 6-month age warning."""
    content = read(skill_path("SKILL.md"))
    assert "6 months" not in content, (
        "SKILL.md G7 still contains the 6-month age warning — should be removed (Issue 12 fix)."
    )


# ---------------------------------------------------------------------------
# 6. risk-method-matrix.md — M42 disambiguation note (Issue 3 fix)
# ---------------------------------------------------------------------------

def test_risk_matrix_has_m42_disambiguation():
    """Issue 3 fix: M42 classification note must be present."""
    content = read(skill_path("data/risk-method-matrix.md"))
    assert "M42 classification note" in content, (
        "risk-method-matrix.md missing M42 disambiguation note (Issue 3 fix)."
    )


# ---------------------------------------------------------------------------
# 7. No T-codes anywhere in command or template files
# ---------------------------------------------------------------------------

def test_no_t_codes_in_commands():
    t_code_pattern = re.compile(r'\bT\d+\b')
    violations = {}
    for f in skill_path("commands").glob("*.md"):
        hits = t_code_pattern.findall(f.read_text(encoding="utf-8"))
        if hits:
            violations[f.name] = hits
    assert not violations, f"Deprecated T-codes found in command files: {violations}"


def test_no_t_codes_in_templates():
    t_code_pattern = re.compile(r'\bT\d+\b')
    violations = {}
    for f in skill_path("templates").glob("*.md"):
        hits = t_code_pattern.findall(f.read_text(encoding="utf-8"))
        if hits:
            violations[f.name] = hits
    assert not violations, f"Deprecated T-codes found in template files: {violations}"


# ---------------------------------------------------------------------------
# 8. ai.md — G5 Simulation Trap wiring
# ---------------------------------------------------------------------------

def test_ai_command_has_simulation_trap_warning():
    """ai.md must surface the Simulation Trap warning (G5 critical path)."""
    content = read(skill_path("commands/ai.md"))
    assert "Simulation Trap" in content, (
        "commands/ai.md is missing the Simulation Trap warning. "
        "AI-simulation inputs must be caught and redirected (G5)."
    )


def test_ai_command_references_ai_guardrails():
    """ai.md must load data/ai-guardrails.md (its primary data source)."""
    content = read(skill_path("commands/ai.md"))
    assert "ai-guardrails.md" in content, (
        "commands/ai.md does not reference data/ai-guardrails.md."
    )


# ---------------------------------------------------------------------------
# 9. diagnose.md — anti-patterns data dependency
# ---------------------------------------------------------------------------

def test_diagnose_references_anti_patterns_data():
    """diagnose.md must reference data/anti-patterns.md (diagnostic questions sourced from there)."""
    content = read(skill_path("commands/diagnose.md"))
    assert "anti-patterns.md" in content, (
        "commands/diagnose.md does not reference data/anti-patterns.md. "
        "Diagnostic questions must be read from the data file, not hardcoded."
    )
