# CMD: list methods [filter] / list tools

**Trigger**: `list`

**Parse second word**:
- `methods` → list discovery methods (with filter or G11 guidance)
- `tools` → list context tools
- other/missing → apply G11: show both options and ask

**Output mode** — check config `output_mode`. Append `full` to any list command to force standard columns regardless of config (e.g., `list methods value full`).

**Compact mode columns** (config `output_mode: compact`): M## | Name | Stage
**Standard mode columns** (default): M## | Name | Primary Risk | Stage | Category | Tier | Time | Evidence

---

**list methods (no filter)**:

Read `templates/list-template.md`. Apply G11 — do not dump 80 methods. Display Variant 1 (Filter Guidance) from that template.

---

**list methods all**:

Read `data/methods-index.md` and `templates/list-template.md`. Display Variant 3 from that template — all 80 active methods. Columns follow output mode.

Footer: "Use `/discovery-karaoke describe M##` for the full entry on any method."

---

**list methods [filter]**:

Read `data/methods-index.md` and `templates/list-template.md`. Apply filter(s) using AND logic. Display Variant 2 from that template. Show match count. Columns follow output mode.

Footer: "Use `/discovery-karaoke describe M##` for the full entry."

---

**list tools**:

Read `data/methods-index.md` (filter by Type: `"Synthesis Tool"`, `"Framework"`, or `"Operating Practice"` — these are the exact values written by `local/generate_index.py`) and `templates/list-template.md`. Display Variant 4. For the Primary Pairing column: read those 11 entries from `data/discovery-methods-full.md` only if pairing detail is needed; otherwise show Type column in its place.

Footer: "Context tools structure thinking — pair them with discovery methods, not as standalone discovery activities."
