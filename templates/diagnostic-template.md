# Diagnostic Template

Use this template for the `diagnose` command. Interactive karaoke diagnostic scorecard.

---

## Template

```
# Discovery Karaoke Diagnostic

## Your Scores

| # | Question | Score |
|---|----------|-------|
| 1-12 | [Read the 12 diagnostic questions from `data/anti-patterns.md` — section "Diagnostic: Are You Doing Discovery Karaoke?". Use the exact question text from that file, not from this template. This prevents drift when questions are updated.] | [0-3 each] |

**Total: [X] / 36**

---

## Interpretation

### [Band name based on score]

[Read the score interpretation bands from `data/anti-patterns.md` — section "Diagnostic: Are You Doing Discovery Karaoke?", subsection "Score interpretation". Use the exact band labels, score ranges, and descriptions from that file. This prevents drift when bands are updated.]

---

## Your Top Anti-Patterns

Based on your highest-scoring questions:

### [Anti-pattern name] (scored [X])
[Description of the pattern]
**Recovery action**: [Specific, actionable step]

### [Anti-pattern name] (scored [X])
[Description]
**Recovery action**: [Specific step]

---

## 30-Minute Recovery Exercise

1. List your current bets (features, products, initiatives in flight)
2. For each bet, name the primary risk (Value? Usability? Feasibility? Viability? Compliance?)
3. For each bet, name the stage (Explore? Validate? Optimize?)
4. For each bet, name the method you're using (or plan to use)
5. Check: Does the method match the risk and stage? Or is it your default?
6. If default: Use `/discovery-karaoke matrix [risk] [stage]` to find alternatives

---

## Next Steps

- Run `/discovery-karaoke review [your current plan]` to check a specific initiative
- Run `/discovery-karaoke assess [situation]` to get deliberate recommendations for your next bet
- Repeat this diagnostic quarterly to track improvement

---

*Framework: The Thinking Lens — "Stop Doing Discovery Karaoke" | the-thinking-lens.com*
```

---

## Formatting Rules

1. Non-judgmental framing throughout — recovery-oriented, not blame-oriented
2. Always map highest-scoring questions to specific anti-patterns
3. Always include the 30-minute recovery exercise
4. Always suggest next commands to run
5. Include attribution
