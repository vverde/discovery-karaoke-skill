#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "anthropic>=0.90",
#   "pyyaml>=6.0",
# ]
# ///
"""
golden_eval.py — Runtime golden set evaluation for Discovery Karaoke skill.

Calls the Claude API with the skill's system prompt and asserts on output
characteristics. NOT run on every commit — run manually before releases or
when SKILL.md, a command file, or a template changes.

Usage:
    uv run local/golden_eval.py                       # run all cases (recommended)
    uv run local/golden_eval.py --case TC-16          # run single case
    uv run local/golden_eval.py --dry-run             # show prompts, no API call
    uv run local/golden_eval.py --verbose             # show full model responses
    uv run local/golden_eval.py --priority critical   # critical cases only (~$0.05)

Cost estimate (claude-haiku-4-5): ~$0.002–0.005 per case. Full suite: ~$0.03.
"""

import argparse
import sys
import textwrap
import time
from pathlib import Path

import anthropic
import yaml

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

SKILL_ROOT = Path(__file__).parent.parent
CASES_FILE = SKILL_ROOT / "local/golden-cases.yaml"
MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 1500

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def load_cases() -> list[dict]:
    return yaml.safe_load(CASES_FILE.read_text(encoding="utf-8"))


def build_system_prompt(file_list: list[str]) -> str:
    parts = []
    for rel_path in file_list:
        path = SKILL_ROOT / rel_path
        if not path.exists():
            raise FileNotFoundError(f"System file not found: {rel_path}")
        parts.append(f"--- {rel_path} ---\n\n{path.read_text(encoding='utf-8')}")
    return "\n\n".join(parts)


def check_assertions(response: str, case: dict) -> list[str]:
    failures = []
    for s in case.get("expect_present", []):
        if s.lower() not in response.lower():
            failures.append(f"MISSING   : {s!r}")
    for s in case.get("expect_absent", []):
        if s.lower() in response.lower():
            failures.append(f"PRESENT   : {s!r}  (should be absent)")
    return failures


def truncate(text: str, width: int = 80) -> str:
    return textwrap.shorten(text.strip().replace("\n", " "), width=width)


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


def run_case(client: anthropic.Anthropic, case: dict, verbose: bool = False) -> dict:
    system = build_system_prompt(case.get("system_files", ["SKILL.md"]))
    user_input = case["input"].strip()

    start = time.monotonic()
    message = client.messages.create(
        model=MODEL,
        max_tokens=case.get("max_tokens", MAX_TOKENS),
        system=system,
        messages=[{"role": "user", "content": user_input}],
    )
    elapsed = time.monotonic() - start

    response = message.content[0].text
    failures = check_assertions(response, case)

    return {
        "case": case,
        "response": response,
        "failures": failures,
        "status": "PASS" if not failures else "FAIL",
        "elapsed": elapsed,
        "input_tokens": message.usage.input_tokens,
        "output_tokens": message.usage.output_tokens,
    }


def dry_run_case(case: dict) -> None:
    print(f"\n{'='*70}")
    print(f"  {case['id']} — {case['name']}")
    print(f"{'='*70}")
    print(f"  System files : {', '.join(case.get('system_files', ['SKILL.md']))}")
    print(f"  Input        : {truncate(case['input'], 100)}")
    print(f"  Must have    : {case.get('expect_present', [])}")
    print(f"  Must lack    : {case.get('expect_absent', [])}")
    print(f"  Notes        : {truncate(str(case.get('notes', '')), 80)}")


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def print_result(result: dict, verbose: bool = False) -> None:
    case = result["case"]
    status = result["status"]
    marker = "✓" if status == "PASS" else "✗"
    color = "\033[32m" if status == "PASS" else "\033[31m"
    reset = "\033[0m"

    print(
        f"  {color}{marker}{reset} {case['id']:<8} [{case.get('priority','?'):8}]  "
        f"{case['name']:<55}  {result['elapsed']:.1f}s"
    )

    if result["failures"]:
        for f in result["failures"]:
            print(f"             → {f}")

    if verbose:
        print(f"\n--- Response ({result['output_tokens']} tokens) ---")
        print(result["response"])
        print("---\n")


def print_summary(results: list[dict]) -> None:
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = sum(1 for r in results if r["status"] == "FAIL")
    total = len(results)
    total_input = sum(r["input_tokens"] for r in results)
    total_output = sum(r["output_tokens"] for r in results)
    # Haiku pricing (approximate): $0.80/M input, $4.00/M output
    est_cost = (total_input / 1_000_000) * 0.80 + (total_output / 1_000_000) * 4.00

    print(f"\n{'─'*70}")
    print(f"  Results  : {passed}/{total} passed", end="")
    if failed:
        print(f"  ({failed} FAILED)", end="")
    print()
    print(f"  Tokens   : {total_input:,} in / {total_output:,} out")
    print(f"  Est. cost: ${est_cost:.4f}")
    print(f"{'─'*70}")

    if failed:
        print("\n  FAILED CASES:")
        for r in results:
            if r["status"] == "FAIL":
                print(f"    {r['case']['id']} — {r['case']['name']}")
                for f in r["failures"]:
                    print(f"      {f}")
        sys.exit(1)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run golden set evaluation against the live Claude API."
    )
    parser.add_argument("--case", help="Run a single case by ID (e.g. TC-16)")
    parser.add_argument("--dry-run", action="store_true", help="Print prompts without calling the API")
    parser.add_argument("--verbose", action="store_true", help="Print full model responses")
    parser.add_argument("--priority", choices=["critical", "high", "medium"], help="Filter by priority")
    args = parser.parse_args()

    cases = load_cases()

    if args.case:
        cases = [c for c in cases if c["id"] == args.case]
        if not cases:
            print(f"Error: case {args.case!r} not found in {CASES_FILE.name}")
            sys.exit(1)

    if args.priority:
        cases = [c for c in cases if c.get("priority") == args.priority]

    if args.dry_run:
        print(f"\nDRY RUN — {len(cases)} case(s) — no API calls\n")
        for case in cases:
            dry_run_case(case)
        return

    print(f"\nDiscovery Karaoke — Golden Eval  ({len(cases)} cases, model: {MODEL})\n")

    client = anthropic.Anthropic()
    results = []

    for case in cases:
        result = run_case(client, case, verbose=args.verbose)
        print_result(result, verbose=args.verbose)
        results.append(result)

    print_summary(results)


if __name__ == "__main__":
    main()
