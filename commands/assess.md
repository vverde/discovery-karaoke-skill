# CMD: assess [situation]

**Trigger**: `assess` or smart fallback — classified as a situation description.

**No situation provided**: Apply G11:
> "Describe your situation and I'll recommend the right discovery methods.
> Example: `assess We're considering a self-serve tier for SMBs`
> For a faster result: `quick [situation]` — 4 questions, top methods in under 2 minutes."

**Data files**:
- `data/risk-method-matrix.md` — Risk × Stage navigation and constraint quick picks
- `data/discovery-methods-full.md` — Full method entries for shortlisted candidates
- `data/anti-patterns.md` — Named anti-patterns for G6 karaoke check
- `data/ai-guardrails.md` — AI acceleration and guardrails (G5)
- `templates/recommendation-template.md` — Output card format

**Step 1: Check for saved config**

Look for `.discovery-karaoke-config.yml` in the working directory. If found:
- Pre-fill constraint fields (company size, business model, user access, team size, customer base, regulated)
- If older than 6 months, warn: "Your saved config is from [date]. Team context may have changed. Want to update it?"
- Show pre-filled values and ask the user to confirm or adjust

**Step 2: Gather context** (AskUserQuestion, max 3–4 questions per batch)

*Batch 1 — Situation* (always ask):
1. What are you trying to decide? (free text)
2. Product stage: Pre-launch / MVP / Growth / Mature
3. Primary risk (multi-select 1–2): Value/Desirability / Usability / Feasibility / Viability / Compliance & Ethics

*Batch 2 — Constraints* (skip fields already in config):
4. Company context: Startup / Scaleup / Enterprise
5. Business model: B2B / B2C / B2B2C / Internal
6. User access: Easy / Moderate / Limited
7. Time available: Urgent (<1 week) / Short (1–4 weeks) / Standard (1–3 months) / Flexible

*Batch 3 — Depth* (medium/large bets only — skip entirely for small bets):
8. Budget: Minimal / Moderate / Significant
9. Team capacity: Solo / Small (2–5) / Cross-functional (5+)
10. Regulated industry? Yes → auto-elevate Compliance (G4)
11. Customer base: None / Small (<100) / Medium (100–10K) / Large (10K+)
12. Blast radius: Small (feature tweak) / Medium (new feature) / Large (new product/pivot)

**Step 3: Generate recommendations**

1. Read `data/risk-method-matrix.md` → identify candidate methods for the risk × stage combination and applicable constraint quick picks
2. Narrow candidates by constraints (business model, user access, time, cost level, company size)
3. Read the shortlisted method entries from `data/discovery-methods-full.md`
4. Select 1–2 primary methods (G10); sequence with explicit decision points — what each method's output unlocks for the next step
5. Suggest 1 companion context tool
6. G6 karaoke check: read `data/anti-patterns.md` → identify the 1–2 anti-patterns **by name** most relevant to the situation → surface the specific pattern name, its warning signs, and its recovery action
7. G4 compliance check: if regulated or AI/data-sensitive, surface M75/M76 or M89/M91 as early as Explore
8. G5 AI opportunities: read `data/ai-guardrails.md` for relevant acceleration notes

**Step 4**: Read `templates/recommendation-template.md`. Deliver output using that card structure exactly.

**Step 5: Offer follow-up**:
- `/discovery-karaoke describe M##` — deep-dive on any recommended method
- `/discovery-karaoke compare M## vs M##` — compare with the alternative not recommended
- `/discovery-karaoke review [plan]` — critique an existing plan
- Offer to help design the specific research instrument (interview guide, survey, test plan)
