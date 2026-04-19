# CMD: diagnose

**Trigger**: `diagnose`

**Data files**:
- `data/anti-patterns.md` — diagnostic instrument, scoring bands, recovery actions
- `templates/diagnostic-template.md` — output card format

**Step 0: Optional context** *(ask before the 12 questions — skippable)*:
> "One optional question to personalise the results: what type of product team are you?
> (a) B2B SaaS (b) B2C (c) Internal tooling (d) Pre-product / no product yet (e) Skip"

If a product type is provided, use it to frame the score interpretation and anti-pattern recovery actions with product-type-specific context (e.g. B2B teams often face Stakeholder Karaoke; pre-product teams often face Survey-First Karaoke). If skipped, proceed with generic framing.

**Step 1**: Read `data/anti-patterns.md`. Locate the `## Diagnostic: Are You Doing Discovery Karaoke?` section. Present those exact questions to the user via AskUserQuestion (single batch, scoring scale 0–3 as defined in that section).

Frame the instrument as it is labelled in the file: *"a reflective heuristic, not a validated instrument — use results to surface patterns worth examining, not as a definitive score."*

**Step 2**: Calculate the total score. Apply the interpretation bands as defined in `data/anti-patterns.md` — read the bands from that file, do not use hardcoded values here.

**Step 3**: Map the highest-scoring questions to their corresponding **named anti-patterns** from `data/anti-patterns.md`. Each question corresponds to a specific pattern — identify them by name.

**Step 4**: Read `templates/diagnostic-template.md`. Deliver output using that card structure exactly:
- Score and interpretation band
- Top anti-patterns triggered — named, with their specific recovery actions from the file
- The 30-minute exercise from the `## Recovery` section
- Next commands to run

**Tone**: Non-judgmental, recovery-oriented. Never blame. Frame as "here's where defaults may have crept in."
