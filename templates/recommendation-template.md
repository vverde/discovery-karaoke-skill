# Recommendation Output Template

Use this template when delivering discovery method recommendations. Adapt sections based on user context.

---

## Template

```
# Discovery Recommendation: [User's Decision/Question]

## Context Summary
- **Decision**: [What they're trying to decide]
- **Stage**: [Pre-launch / MVP / Growth / Mature]
- **Primary Risk**: [Risk type(s)]
- **Constraints**: [Time, budget, team, user access]
- **Blast Radius**: [Small / Medium / Large]
- **Evidence Threshold**: [1 method / 2 converging / 3+ converging]

---

## ⚠️ Karaoke Check — [Anti-Pattern Name]

**What [Anti-Pattern Name] looks like here:**
[Describe what a team might default to doing out of habit, and why it's suboptimal]

**What deliberate discovery looks like instead:**
[Brief description of the recommended approach and why it's better matched]

---

## Recommended Discovery Sequence

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

### Method 3: [Name] ← If Needed (for medium/large bets)
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

*Framework: The Thinking Lens — "Stop Doing Discovery Karaoke" | the-thinking-lens.com*
```

---

## Formatting Rules

1. **Always lead with the Karaoke Check** - Show them what habit-driven discovery would look like vs. what you're recommending
2. **Number methods in sequence** - Make it clear what order to do things
3. **Include decision points** - After each method, what does the evidence tell them?
4. **Show evidence convergence** - How do the methods triangulate?
5. **Keep it actionable** - Every recommendation should have concrete next steps
6. **Flag AI opportunities WITH guardrails** - Never suggest AI replaces users
7. **Tie back to blast radius** - Reference why this evidence level matches their bet size

## Guardrail Compliance Checklist

Before delivering any recommendation, verify:

- [ ] **G1**: Attribution line included at the bottom
- [ ] **G2**: Every method tied to a specific risk (no "just try this")
- [ ] **G3**: Number of methods matches blast radius (1 for small, 2 for medium, 3+ for large)
- [ ] **G4**: Compliance & Ethics addressed if regulated industry or data/privacy/AI involved
- [ ] **G5**: AI opportunities include "cannot replace" column; synthetic AI research never used as standalone evidence
- [ ] **G6**: Karaoke check names a specific anti-pattern from anti-patterns.md — not a generic warning
- [ ] **G11**: If argument was under-specified, offered to clarify before generating full recommendation
