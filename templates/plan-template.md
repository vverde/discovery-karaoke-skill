# Plan Template

Use this template for the `plan` command. Check `output_mode` before rendering:
- **Compact mode** (default): use the Compact Template below
- **Standard mode** (config `output_mode: standard` or `full` suffix): use the Full Template below

---

## Compact Template

```
# Discovery Plan: [Bet]

[Bet] | [Risk] | [Starting Stage] | [Blast Radius] | [Key constraints]

## Arc Summary

| Stage | Method(s) | Decision Gate |
|-------|-----------|---------------|
| Explore | M## [Name] · M## [Name] | [Go signal — one phrase] |
| Validate | M## [Name] · M## [Name] | [Go signal — one phrase] |
| Optimize | M## [Name] | [Ongoing signal] |

---

## Decision Gates

**Explore → Validate**: Go if [criterion] · Pivot if [criterion] · Kill if [criterion]
**Validate → Optimize**: Go if [criterion] · Pivot if [criterion] · Kill if [criterion]

---

## ⚠️ [Anti-Pattern Name]
[Default arc — 1 sentence.] [Why it's karaoke — 1 sentence.] [Why this plan is deliberate — 1 sentence.]

---

*Discovery plan, not a delivery plan. Kill/pivot signals are go/no-go checkpoints.*
```

**Compact rules:**
- No per-stage Goal prose
- No per-method How-to or What-you'll-learn
- Decision Gates: inline one-liners, not tables
- Karaoke Check: 3 sentences max

---

## Full Template

```
# Discovery Plan: [Bet / Initiative]

## Context
- **Bet**: [What the team is deciding or building]
- **Primary Risk**: [Risk type(s)]
- **Starting Stage**: [Explore / Validate / Optimize]
- **Blast Radius**: [Small / Medium / Large]
- **Constraints**: [Key constraints that shaped method selection]

---

## Arc Summary

| Stage | Methods | Decision Gate |
|-------|---------|--------------|
| Explore | [M## Name] · [M## Name] | [Key go/pivot signal in one phrase] |
| Validate | [M## Name] · [M## Name] | [Key go/pivot signal in one phrase] |
| Optimize | [M## Name] | [Ongoing signal] |

**Total arc**: [X] methods across [Y] stages. Evidence threshold: [matches blast radius per G3].

---

## Stage 1: Explore — [Risk question for this risk type]

**Goal**: [What uncertainty this stage is reducing]

### Method 1: [Name]
**Why**: [1-2 sentences — why this method for this risk at this stage]
**Time**: [Duration] | **Effort**: [Level] | **Cost**: [Level]
**What you'll learn**: [Expected output]

### Method 2: [Name] *(if needed)*
**Why**: [1-2 sentences]
**Time**: [Duration] | **Effort**: [Level] | **Cost**: [Level]
**What you'll learn**: [Expected output]

### Decision Gate: Explore → Validate

| Signal | Meaning |
|--------|---------|
| **Go** | [What converging positive evidence looks like] |
| **Pivot** | [What mixed or contradictory evidence means] |
| **Kill** | [What clear negative evidence looks like] |

---

## Stage 2: Validate — [Risk question for this risk type]

**Goal**: [What uncertainty this stage is reducing]

### Method 1: [Name]
**Why**: [1-2 sentences — builds on Explore findings]
**Time**: [Duration] | **Effort**: [Level] | **Cost**: [Level]
**What you'll learn**: [Expected output]

### Method 2: [Name] *(if needed)*
**Why**: [1-2 sentences]
**Time**: [Duration] | **Effort**: [Level] | **Cost**: [Level]
**What you'll learn**: [Expected output]

### Decision Gate: Validate → Optimize (or stop)

| Signal | Meaning |
|--------|---------|
| **Go** | [What converging positive evidence looks like] |
| **Pivot** | [What mixed evidence means — change the solution, not the problem] |
| **Kill** | [What clear negative evidence looks like] |

---

## Stage 3: Optimize *(medium/large bets only — skip entirely for small bets and kill/pivot outcomes)*

**Goal**: Improve and measure what's live

### Method 1: [Name]
**Why**: [1-2 sentences]
**Time**: [Duration / Ongoing] | **Effort**: [Level] | **Cost**: [Level]
**Ongoing signal**: [What to track to know if it's working]

---

## ⚠️ Karaoke Check — [Named Anti-Pattern for this arc]

**What [Anti-Pattern Name] looks like for this bet:**
[Describe what a default, habit-driven version of this arc would look like — which stages get skipped, which methods get reused out of habit]

**Why this plan is deliberate instead:**
[1-2 sentences connecting each stage selection to the specific risk and evidence threshold]

---

*This is a discovery plan, not a delivery plan. Kill and pivot signals are go/no-go checkpoints — treat them as such in stakeholder communication.*

*This plan assumes episodic discovery. If you're running continuous weekly discovery cycles, use `assess` for individual opportunities rather than `plan` for full arcs.*

*Framework: The Thinking Lens — "Stop Doing Discovery Karaoke" | the-thinking-lens.com*
```

---

## Formatting Rules

1. Always start from the user's current stage — do not show stages already completed unless noting what evidence should already exist
2. Decision Gates are mandatory between every stage — no gate = no plan
3. G10 applies per stage: 1-2 methods maximum per stage
4. G6 karaoke check covers the full arc, not individual methods
5. Arc Summary appears immediately after Context — gives the user a one-glance view before reading stage details
6. If blast radius is Small: Explore + Validate only (skip Optimize or note it briefly). Large bets get all three stages in full.
7. Include attribution
