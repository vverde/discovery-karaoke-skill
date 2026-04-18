# CMD: compare [M##] vs [M##]

**Trigger**: `compare`

**Data files**:
- `data/discovery-methods-full.md`
- `templates/comparison-template.md`

**Parse**: Extract two M-codes from the remaining argument. Accept: `M1 vs M23`, `M1 M23`, `M1 and M23`.

**Fewer than 2 IDs**: Apply G11:
> "Specify two M-codes. Example: `/discovery-karaoke compare M1 vs M23`
> Not sure which methods to compare? `/discovery-karaoke list methods [filter]`"

**Step 1**: Read both full method entries from `data/discovery-methods-full.md`.

**Step 2**: Read `templates/comparison-template.md`. Deliver output using that card structure exactly.

**Rules (always apply)**:
- Never declare a winner without context — always frame as "depends on your risk and constraints" (G2)
- Always show when to use each AND when to use both in sequence
- Always surface the named karaoke risk for each method (G6)
