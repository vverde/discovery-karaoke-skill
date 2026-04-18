# CMD: describe [M##]

**Trigger**: `describe`

**Data file**: `data/discovery-methods-full.md`

**No ID provided**: Apply G11:
> "Specify an M-code (e.g., `describe M23`).
> Browse all methods: `/discovery-karaoke list methods`
> Browse by risk: `/discovery-karaoke list methods value`"

**Parse the ID** (remaining argument):
- Starts with `M` (case-insensitive) → look up the full entry in `data/discovery-methods-full.md`
- Not recognized as M-code → same G11 response as above

**Display the full entry**: Read `data/discovery-methods-full.md` to get the method entry, then read `templates/describe-template.md`. Deliver output using that card structure.

**Output mode** — check config `output_mode`, or look for `full` suffix after the M-code (e.g., `describe M23 full`):

- **Compact mode** (config `output_mode: compact` AND no `full` suffix):
  Use the Compact section of `templates/describe-template.md`:
  - Box-drawn card (~66 chars wide): title bar, 1–2 line description, 5-cell metadata row, karaoke trap row
  - Footer outside the box: `describe M## full · compare M## vs M##`

- **Standard mode** (config `output_mode: standard`, or no config, or `full` suffix used):
  Use the Full section of `templates/describe-template.md` — all sections including:
  - How to Apply (numbered steps)
  - When to Use / When NOT to Use
  - AI Augmentation with "cannot replace" column
  - Prerequisites
