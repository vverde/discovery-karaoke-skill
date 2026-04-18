# CMD: matrix

**Trigger**: `matrix`

**Data files**:
- `data/risk-method-matrix.md`
- `templates/matrix-template.md`

**Four modes** — parse remaining arguments (case-insensitive). Read `data/risk-method-matrix.md` first (needed for all modes), then read `templates/matrix-template.md` and use the matching mode section:

---

**Mode 1 — No args: compact 5×3 overview**

Display compact matrix using Mode 1 from `templates/matrix-template.md` — top 2 methods per cell, M-codes shown, evidence range per row. Apply G11 options block after the table.

---

**Mode 2 — `full`: full 5×3, all methods per cell**

Display full matrix using Mode 2 from `templates/matrix-template.md` — all methods per cell with evidence range per row, separated by risk section.

---

**Mode 3 — `[risk]` only: full row**

Display using Mode 3 from `templates/matrix-template.md`:
- Full row table: all 3 stages × all methods for that risk, with evidence range
- Quick picks by constraint section (urgent/low-budget, no-user-access, B2B, pre-launch) with constraint icons

Apply G11 footer: "Drill into a cell: `matrix [risk] explore` | `matrix [risk] validate` | `matrix [risk] optimize`"

---

**Mode 4 — `[risk] [stage]`: single cell**

Display using Mode 4 from `templates/matrix-template.md`:
- All methods for that risk × stage cell as a table
- Quick picks by constraint (all four constraint scenarios)
- Karaoke warning specific to that cell

---

**Unrecognized argument** (not a risk, stage, or `full`): Apply G11:
> "I don't recognize '[arg]' as a risk, stage, or format.
> Risks: value | usability | feasibility | viability | compliance
> Stages: explore | validate | optimize
> Formats: (no args for overview) | full | [risk] | [risk] [stage]"

---

**Footer on all matrix outputs**:
```
Starting point only. For context-matched recommendations: /discovery-karaoke assess [situation]
Evidence thresholds — Small bet: 1 method. Medium: 2 converging. Large: 3+ converging.
```
