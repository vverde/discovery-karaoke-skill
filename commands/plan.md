# CMD: plan [situation]

**Trigger**: `plan`

**Purpose**: Generate a full discovery arc across all three stages (Explore → Validate → Optimize) for a given bet. Unlike `assess` (which recommends what to do right now), `plan` shows the complete staged sequence with decision gates between each stage.

**No situation provided**: Apply G11:
> "Describe your bet or initiative and I'll map the full discovery arc (Explore → Validate → Optimize).
> Example: `plan We're considering adding an AI writing assistant to our B2B product`
> For a point-in-time recommendation at your current stage only: `assess [situation]`"

**Data files**:
- `data/risk-method-matrix.md` — Risk × Stage navigation for all three stages
- `data/methods-index.md` — method metadata for shortlisting per stage
- `data/discovery-methods-full.md` — full prose entries for selected methods only
- `data/anti-patterns.md` — Named anti-patterns for G6 karaoke check on the full arc
- `templates/plan-template.md` — Output card format

---

**Step 1: Check for saved config**

Look for `.discovery-karaoke-config.yml`. If found, pre-fill constraint fields and confirm with user.

---

**Step 2: Gather context** (single batch via AskUserQuestion)

1. What is the bet or initiative? (free text — feature, product, pivot)
2. Primary risk (pick 1–2): Value/Desirability / Usability / Feasibility / Viability / Compliance & Ethics
3. Where are you today? Explore / Validate / Optimize
   *(The plan will cover your current stage and all remaining stages.)*
4. Blast radius: Small (feature tweak) / Medium (new feature) / Large (new product/pivot)

If config exists, skip constraint questions already answered. Apply G4 auto-elevation if regulated/AI/data context is detectable from the situation description.

---

**Step 3: Build the staged plan**

For each remaining stage (starting from the user's current stage):

1. Read `data/risk-method-matrix.md` → identify candidate method IDs for risk × stage
2. Read `data/methods-index.md` → filter candidates by constraints (Needs Existing Users, Needs Live Traffic, Effort, Cost)
3. Shortlist 2-3 candidates per stage. Read those entries from `data/discovery-methods-full.md`
4. Select 1–2 methods per stage (G10 applies per stage, not across the full arc)
5. Define the Decision Gate for that stage: what specific evidence must exist before moving to the next stage?

**Decision Gate logic**:
- **Go**: what converging positive evidence looks like
- **Pivot**: what mixed or contradictory evidence means
- **Kill**: what clear negative evidence looks like (for Explore/Validate stages only)

**Stage sequencing rule**: Never recommend Validate methods before Explore is complete. If user is already in Validate, acknowledge what Explore evidence should already exist and note it as an assumption.

---

**Step 4: G6 Karaoke check on the full arc**

Read `data/anti-patterns.md`. Evaluate the entire proposed sequence:
- Does the arc reflect deliberate stage progression or a default sequence?
- Which named anti-pattern does a karaoke version of this arc most resemble?
- Name it explicitly and contrast it with the recommended arc.

---

**Step 5**: Read `templates/plan-template.md`. Arc Summary is rendered immediately after Context (before stage details), giving the user a one-glance view of the full arc. Then render stage details and Karaoke Check.

---

**Step 6: Offer follow-up**:
- `/discovery-karaoke assess [situation]` — point-in-time recommendation for your current stage only (no arc)
- `/discovery-karaoke describe M##` — deep-dive on any method in the plan
- `/discovery-karaoke review [plan]` — critique an existing plan for karaoke symptoms
