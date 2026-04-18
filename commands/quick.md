# CMD: quick [situation]

**Trigger**: `quick`

**No situation provided**: Apply G11:
> "Describe your situation for a fast recommendation.
> Example: `quick Should we add dark mode to the dashboard?`
> For the full assessment: `assess [situation]`"

**Data files**:
- `data/risk-method-matrix.md`
- `data/methods-index.md` — method names and metadata for selected methods
- `data/anti-patterns.md` — for G6 named anti-pattern check
- `templates/quick-template.md`

**Step 1**: Check saved config (same as assess — look for `.discovery-karaoke-config.yml`).

**Step 2**: Ask 4 questions only (single batch via AskUserQuestion):
1. What are you trying to decide? (free text)
2. Primary risk (pick 1): Value / Usability / Feasibility / Viability / Compliance
3. Discovery stage: Explore / Validate / Optimize
4. Blast radius: Small / Medium / Large

If config exists, use saved constraints. If no config, apply reasonable defaults from the situation description.

**Step 3**:
1. Read `data/risk-method-matrix.md` → find the risk × stage cell
2. Select 1–2 primary methods (G10). Show 1 alternative only if time/access constraints justify it
3. Pick 1 companion context tool
4. G6 karaoke check: read `data/anti-patterns.md` → identify the most relevant **named pattern** → surface it by name with its key warning sign

**Step 4**: Read `templates/quick-template.md`. Deliver output using that card structure exactly.

**Step 5**: Offer upgrade:
> "Want the full context-matched assessment? `/discovery-karaoke assess [same situation]`"
