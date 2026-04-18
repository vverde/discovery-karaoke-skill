# Diagnostic Template

Use this template for the `diagnose` command. Interactive karaoke diagnostic scorecard.

---

## Template

```
# Discovery Karaoke Diagnostic

## Your Scores

| # | Question | Score |
|---|----------|-------|
| 1 | We use the same 2-3 discovery methods for most initiatives | [0-3] |
| 2 | Our discovery process is the same regardless of the risk type | [0-3] |
| 3 | We can't explain WHY we chose a particular method (vs. alternatives) | [0-3] |
| 4 | We default to interviews when we're unsure what to do | [0-3] |
| 5 | Our discovery findings rarely surprise us | [0-3] |
| 6 | We treat compliance/ethics as a checkbox, not a first-class risk | [0-3] |
| 7 | We don't adjust evidence thresholds based on bet size | [0-3] |
| 8 | Our "discovery" is mainly about building confidence, not reducing uncertainty | [0-3] |
| 9 | We skip or delay discovery when timelines are tight | [0-3] |
| 10 | We use the same discovery process we used 2+ years ago | [0-3] |

**Total: [X] / 30**

---

## Interpretation

### [Band name based on score]

- **0-8: Deliberate Discovery** — You're matching methods to risks. Keep it up. Watch for creeping defaults.
- **9-15: Mild Karaoke** — Some defaults creeping in. Review your method selection for the top 2-3 questions you scored highest on.
- **16-21: Significant Karaoke** — Time to rebuild your risk-to-method mapping. Your process has become the default.
- **22-30: Full Karaoke** — Your discovery process needs a fundamental rethink. Start with the 30-minute recovery exercise below.

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
