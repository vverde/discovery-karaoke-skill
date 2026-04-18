# CMD: assess [situation]

**Trigger**: `assess` or smart fallback — classified as a situation description.

**No situation provided**: Apply G11:
> "Describe your situation and I'll recommend the right discovery methods.
> Example: `assess We're considering a self-serve tier for SMBs`
> For a faster result: `quick [situation]` — 4 questions, top methods in under 2 minutes."

**Data files**:
- `data/risk-method-matrix.md` — Risk × Stage navigation and constraint quick picks
- `data/methods-index.md` — method metadata for shortlisting and constraint filtering
- `data/discovery-methods-full.md` — full prose entries for the 2-3 shortlisted methods only
- `data/anti-patterns.md` — Named anti-patterns for G6 karaoke check
- `data/ai-guardrails.md` — AI acceleration and guardrails (G5)
- `templates/recommendation-template.md` — Output card format

**Step 1: Check for saved config**

Look for `.discovery-karaoke-config.yml` in the working directory. If found:
- Pre-fill constraint fields (company size, business model, user access, team size, customer base, regulated)
- If older than 6 months, warn: "Your saved config is from [date]. Team context may have changed. Want to update it?"
- Show pre-filled values and ask the user to confirm or adjust

**Step 1b: Signal-based pre-fill** *(apply before asking Batch 2 — skip questions already answered by signals)*

Scan the situation description for recognizable signals and pre-fill the corresponding constraint fields:

| Signal in description | Pre-fill |
|----------------------|----------|
| "B2B", "enterprise", "sales", "account", "procurement" | Business model → B2B |
| "B2C", "consumer", "app store", "freemium" | Business model → B2C |
| "startup", "pre-launch", "founding", "seed" | Company context → Startup; Product stage → Pre-launch |
| "MVP", "early stage", "first version" | Product stage → MVP |
| "regulated", "GDPR", "HIPAA", "FDA", "EU AI Act", "financial services", "healthcare", "legal" | Regulated → Yes → auto-elevate G4 (skip regulated question in Batch 3) |
| "no users yet", "pre-launch", "no customers" | User access → Limited |
| "large user base", "10K+", "millions" | Customer base → Large |
| "urgent", "this week", "deadline", "by Friday" | Time → Urgent |

Show pre-filled values at the start of Batch 2 and let the user correct any that are wrong. Do not silently apply signals without surfacing them.

**Step 2: Gather context** (AskUserQuestion, max 3–4 questions per batch)

*Batch 1 — Situation* (always ask):
1. What are you trying to decide? (free text)
2. Product stage: Pre-launch / MVP / Growth / Mature
3. Primary risk (multi-select 1–2): Value/Desirability / Usability / Feasibility / Viability / Compliance & Ethics

*Batch 2 — Constraints* (skip fields already in config or pre-filled by signals):
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

1. Read `data/risk-method-matrix.md` → identify candidate method IDs for the risk × stage combination and applicable constraint quick picks
2. Read `data/methods-index.md` → narrow candidates by constraints (Needs Existing Users, Needs Live Traffic, Needs Legal Review, Effort, Cost, Tier, Stage match)
3. Shortlist 3-5 candidates from the index. Then read only those entries from `data/discovery-methods-full.md` for full prose content
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
