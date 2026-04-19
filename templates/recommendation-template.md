# Recommendation Output Template

Use this template when delivering discovery method recommendations. Check `output_mode` (config or `full` suffix) before rendering:
- **Compact mode** (default): use the Compact Template below
- **Standard mode** (config `output_mode: standard` or `full` suffix): use the Full Template below

---

## Compact Template

```
# [Decision — short label]

[Decision] | [Stage] | [Risk] | [Blast Radius] | [Key constraints, one line]
**Assumption**: [Primary assumption being tested]

---

## ⚠️ [Anti-Pattern Name]
[Default move — 1 sentence.] [Why it fails — 1 sentence.] [Deliberate alternative — 1 sentence.]

---

## M## [Name] ← Start Here

**Why**: [Fit — 1 sentence. What it unlocks — 1 sentence.]
**Evidence**: [strength] | **Time**: [range] | **Cost**: [level]

**Decision point**:
- Go: [criterion]
- Pivot: [criterion]
- Kill: [criterion]

**Companion tool**: M## [Name] — [one line]

---

`/discovery-karaoke describe M##` · `compare M## vs M##` · `plan [same situation]`
```

**Compact rules:**
- No How-to-apply steps
- No Evidence Convergence Map
- No AI Acceleration table
- No Anti-Patterns checklist
- No Next Steps block
- Karaoke Check: 3 sentences max (default move / why it fails / deliberate alternative)
- Why-this-method: 2 sentences (fit + what it unlocks)
- Decision point: 3 bullets (Go / Pivot / Kill), no prose

---

## Full Template

```
# Discovery Recommendation: [User's Decision/Question]

## Context Summary
- **Decision**: [What they're trying to decide]
- **Stage**: [Pre-launch / MVP / Growth / Mature]
- **Primary Risk**: [Risk type(s)]
- **Primary Assumption Being Tested**: [Inferred from risk × stage — e.g. "Customers have this problem at sufficient intensity to prioritise a solution"]
- **Constraints**: [Time, budget, team, user access]
- **Blast Radius**: [Small / Medium / Large]
- **Evidence Threshold**: [1 method / 2 converging / 3 converging (large bets only)]

---

## ⚠️ Karaoke Check — [Anti-Pattern Name]

**What [Anti-Pattern Name] looks like here:**
[Describe what a team might default to doing out of habit, and why it's suboptimal]

**What deliberate discovery looks like instead:**
[Brief description of the recommended approach and why it's better matched]

---

## Recommended Discovery Sequence

> **RENDER GATE** — Before rendering method slots, check blast radius:
> - Small bet → render Method 1 only. Remove Methods 2 and 3, including any "conditional" or "follow-up" method sections. Do not add conditional methods as a workaround.
> - Medium bet → render Methods 1–2. Remove Method 3.
> - Large bet → render Methods 1–3 only if two distinct risk types are both active (G10). Otherwise render Methods 1–2.

**Start here: [M##: Name]** — [One sentence: why this method over alternatives for this specific risk and context.]

### Method 1: [Name] ← Start Here
**Why this method**: [1-2 sentences connecting to their specific risk and context]
**Evidence strength**: [Weak / Moderate / Strong]
**Time**: [Duration] | **Effort**: [Low/Med/High] | **Cost**: [Range]

**How to apply:**
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]
5. [Step 5 if needed]

**What you'll learn**: [Expected output/deliverable]
**Decision point**: [What result means go vs. no-go vs. pivot]

---

### Method 2: [Name] ← Then This
**Why this method**: [1-2 sentences - should build on Method 1 findings]
**Evidence strength**: [Weak / Moderate / Strong]
**Time**: [Duration] | **Effort**: [Low/Med/High] | **Cost**: [Range]

**How to apply:**
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]

**What you'll learn**: [Expected output/deliverable]
**Decision point**: [What result means go vs. no-go vs. pivot]

---

### Method 3: [Name] ← Large bets only (two active risk types required)
[Same format as above]

---

## Evidence Convergence Map

| Signal | Method 1 | Method 2 | Method 3 |
|--------|----------|----------|----------|
| [Key question 1] | [What it tells you] | [What it tells you] | [What it tells you] |
| [Key question 2] | [What it tells you] | [What it tells you] | [What it tells you] |

**Go signal**: [Describe what converging positive evidence looks like]
**Pivot signal**: [Describe what mixed or negative evidence means]
**Kill signal**: [Describe what clear negative evidence looks like]

---

## AI Acceleration Opportunities

| Task | AI Can Help | AI Cannot Replace |
|------|------------|-------------------|
| [Task 1] | [How AI helps] | [What still needs humans] |
| [Task 2] | [How AI helps] | [What still needs humans] |

**Guardrail**: AI-simulated feedback compresses time to signal. It NEVER replaces real user signal.

---

## 🚫 Anti-Patterns to Watch For

- [ ] [Anti-pattern 1 specific to their situation]
- [ ] [Anti-pattern 2 specific to their situation]
- [ ] [Anti-pattern 3 specific to their situation]

---

## Next Steps

1. **Immediately**: [First action item]
2. **This week**: [Second action item]
3. **Before deciding**: [Final checkpoint]

**Need help with?**
- `/discovery-karaoke describe [M##]` — deep-dive on any recommended method
- `/discovery-karaoke compare [M## vs M##]` — compare alternative methods
- Designing the discussion guide / survey / test plan
- `/discovery-karaoke review` — review your existing plan for karaoke symptoms

---

```

---

## Formatting Rules

1. **Always lead with the Karaoke Check** - Show them what habit-driven discovery would look like vs. what you're recommending
2. **Method 1 must visually dominate** - The bold callout line before Method 1 is mandatory. Methods 2-3 have no equivalent line.
3. **Number methods in sequence** - Make it clear what order to do things
3. **Include decision points** - After each method, what does the evidence tell them?
4. **Show evidence convergence** - How do the methods triangulate?
5. **Keep it actionable** - Every recommendation should have concrete next steps
6. **Flag AI opportunities WITH guardrails** - Never suggest AI replaces users
7. **Tie back to blast radius** - Reference why this evidence level matches their bet size

## Guardrail Compliance Checklist

Before delivering any recommendation, verify:

- [ ] **G1**: No attribution line in output (attribution in `about` only)
- [ ] **G2**: Every method tied to a specific risk (no "just try this")
- [ ] **G3**: Number of method slots rendered matches blast radius (1 for small, 2 for medium, 3 for large with two active risk types only). Did you render Method 3? If blast radius is not Large with two active risk types, remove it.
- [ ] **G4**: Compliance & Ethics addressed if regulated industry or data/privacy/AI involved
- [ ] **G5**: AI opportunities include "cannot replace" column; synthetic AI research never used as standalone evidence
- [ ] **G6**: Karaoke check names a specific anti-pattern from anti-patterns.md — not a generic warning
- [ ] **G11**: If argument was under-specified, offered to clarify before generating full recommendation
