#!/usr/bin/env python3
"""
generate_index.py — Generate data/methods-index.md from data/discovery-methods-full.md

Generated file : data/methods-index.md
Source         : data/discovery-methods-full.md
Run            : python3 tests/generate_index.py  (from skill root)

Do not edit methods-index.md manually — regenerate from source when the DB changes.
"""

import re
from pathlib import Path
from collections import Counter
from datetime import date

SOURCE = Path("data/discovery-methods-full.md")
OUTPUT = Path("data/methods-index.md")

# Type values that identify context tools (vs. discovery methods).
# list.md uses these exact strings to filter the index for `list tools`.
# Update here if Type values change in the source DB — never hardcode elsewhere.
CONTEXT_TOOL_TYPES = {"Synthesis Tool", "Framework", "Operating Practice"}


# ---------------------------------------------------------------------------
# Field extraction helpers
# ---------------------------------------------------------------------------

def get_field(content: str, field_name: str) -> str:
    """Return the value of a **FieldName**: line, stripped of trailing whitespace."""
    pattern = rf'\*\*{re.escape(field_name)}\*\*:\s*(.+?)(?:\n|$)'
    match = re.search(pattern, content)
    return match.group(1).strip() if match else ""


def extract_primary_risk(risk_str: str) -> str:
    """
    Parse 'primary: Value/Desirability, ...' or bare 'Value/Desirability' and
    return only the first (primary) risk value.
    """
    if not risk_str:
        return ""
    # Strip optional 'primary: ' prefix
    risk = re.sub(r'^primary:\s*', '', risk_str, flags=re.IGNORECASE)
    # Drop any '; secondary: ...' block
    risk = risk.split(';')[0]
    # Take only the first comma-separated value
    return risk.split(',')[0].strip()


# ---------------------------------------------------------------------------
# Entry parser
# ---------------------------------------------------------------------------

def parse_entry(method_num: str, raw_name: str, content: str) -> dict | None:
    """
    Parse a single ## METHOD N: Name block.
    Returns None for Superseded entries (excluded from the index).
    """
    status = get_field(content, "Status")
    if status.lower() == "superseded":
        return None

    # Strip parenthetical subtitle from the name, e.g. "(Problem Discovery)"
    name = re.sub(r'\s*\([^)]*\)\s*$', '', raw_name).strip()

    primary_risk  = extract_primary_risk(get_field(content, "Risk Addressed"))
    stage         = get_field(content, "Discovery Stage")
    category      = get_field(content, "Category")
    type_val      = get_field(content, "Type")
    tier          = get_field(content, "Practitioner Tier")
    time_val      = get_field(content, "Time to Execute")
    effort        = get_field(content, "Effort")
    cost          = get_field(content, "Cost Range")
    evidence      = get_field(content, "Evidence Strength")
    needs_users   = get_field(content, "Needs Existing Users")
    needs_traffic = get_field(content, "Needs Live Traffic")
    needs_legal   = get_field(content, "Needs Legal Review")

    return {
        "id":            f"M{method_num}",
        "name":          name,
        "primary_risk":  primary_risk,
        "stage":         stage,
        "category":      category,
        "type":          type_val,
        "tier":          tier,
        "time":          time_val,
        "effort":        effort,
        "cost":          cost,
        "evidence":      evidence,
        "needs_users":   needs_users,
        "needs_traffic": needs_traffic,
        "needs_legal":   needs_legal,
    }


# ---------------------------------------------------------------------------
# Main parser — splits on ## METHOD N: headers
# ---------------------------------------------------------------------------

def parse_methods(text: str) -> list[dict]:
    """
    Split source text on '## METHOD N: Name' headers and parse each block.
    Returns only Active entries (Superseded filtered out).
    """
    # Pattern captures: (method_number, method_name, block_content)
    sections = re.split(r'\n## METHOD (\d+): ([^\n]+)', text)
    # sections[0] = preamble text before first method
    # then triples: [number, name, content] at indices 1,2,3 / 4,5,6 / ...

    entries = []
    i = 1
    while i + 2 <= len(sections) - 1:
        method_num = sections[i]
        raw_name   = sections[i + 1].strip()
        content    = sections[i + 2]
        i += 3

        entry = parse_entry(method_num, raw_name, content)
        if entry:
            entries.append(entry)

    return entries


# ---------------------------------------------------------------------------
# Markdown renderer
# ---------------------------------------------------------------------------

HEADER_ROW = (
    "| ID | Name | Primary Risk | Stage | Category | Type | Tier | "
    "Time | Effort | Cost | Evidence | Needs Users | Needs Traffic | Needs Legal |"
)
SEPARATOR_ROW = (
    "|----|------|--------------|-------|----------|------|------|"
    "-----|--------|------|----------|-------------|---------------|-------------|"
)


def render_row(e: dict) -> str:
    return (
        f"| {e['id']} | {e['name']} | {e['primary_risk']} | {e['stage']} | "
        f"{e['category']} | {e['type']} | {e['tier']} | {e['time']} | "
        f"{e['effort']} | {e['cost']} | {e['evidence']} | "
        f"{e['needs_users']} | {e['needs_traffic']} | {e['needs_legal']} |"
    )


def render_index(entries: list[dict]) -> str:
    today = date.today().isoformat()
    count = len(entries)

    preamble = f"""\
# Discovery Karaoke — Methods Index

> **Generated file — do not edit manually.**
> Source: `data/discovery-methods-full.md`
> Regenerate: `python3 tests/generate_index.py` (run from skill root)
> Last generated: {today}
>
> {count} active entries. Superseded methods excluded.
> Use this file for navigation commands (list, quick, compare, assess shortlisting, answer list-queries).
> Load the full DB only for deep-dive prose content (describe, ai, final assess entries).

---

"""
    rows = [HEADER_ROW, SEPARATOR_ROW] + [render_row(e) for e in entries]
    return preamble + "\n".join(rows) + "\n"


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if not SOURCE.exists():
        print(f"Error: {SOURCE} not found.")
        print("Run this script from the skill root directory:")
        print("  cd ~/Projects/discovery-karaoke-skill && python3 tests/generate_index.py")
        return

    text    = SOURCE.read_text(encoding="utf-8")
    entries = parse_methods(text)

    OUTPUT.write_text(render_index(entries), encoding="utf-8")

    tiers = Counter(e["tier"] for e in entries if e["tier"])
    print(f"Generated {OUTPUT}")
    print(f"  Total active entries : {len(entries)}")
    for tier in ("Core", "Extended", "Specialist"):
        print(f"  {tier:12s}: {tiers.get(tier, 0)}")
    untiered = [e["id"] for e in entries if not e["tier"]]
    if untiered:
        print(f"  No tier       : {', '.join(untiered)}")


if __name__ == "__main__":
    main()
