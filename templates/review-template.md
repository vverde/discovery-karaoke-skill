# Review Template

Use this template for the `review` command. Check `output_mode` before rendering:
- **Compact mode** (default): use the Compact Template below
- **Standard mode** (config `output_mode: standard` or `full` suffix): use the Full Template below

---

## Compact Template

```
# Plan Review: [Plan summary — one line]

## Symptom Check

| # | Symptom | Status |
|---|---------|--------|
| 1 | Methods matched to specific risks? | [Pass/Flag] |
| 2 | Evidence threshold matches blast radius? | [Pass/Flag] |
| 3 | Generative AND evaluative methods used? | [Pass/Flag] |
| 4 | Compliance & Ethics as first-class risk? | [Pass/Flag] |
| 5 | Decision criteria defined before research starts? | [Pass/Flag] |
| 6 | AI used as accelerator, not replacement? | [Pass/Flag] |

**Overall**: [Deliberate / Mild karaoke / Significant karaoke / Full karaoke] — [1 sentence]

## Top Adjustments

1. [Swap X for Y — 1 sentence reason]
2. [Second adjustment if needed]

`/discovery-karaoke assess [situation]` · `plan [situation]`
```

**Compact rules:**
- No "What's Working Well" section
- No "Specific Observations" detailed prose
- Symptom checklist: status only (no Notes column)
- Overall Health: band + 1 sentence
- Adjustments: max 2 bullets, 1 sentence each

---

## Full Template

```
# Discovery Plan Review

## Your Plan (as understood)

[Summarize the user's described plan — methods, sequence, timeline]

---

## What's Working Well

- [Positive observation 1 — specific, connected to a principle]
- [Positive observation 2]

---

## Karaoke Symptom Check

| # | Symptom | Status | Notes |
|---|---------|--------|-------|
| 1 | Methods matched to specific risks? | [Pass/Flag] | [Explanation] |
| 2 | Evidence threshold matches blast radius? | [Pass/Flag] | [Explanation] |
| 3 | Using evaluative AND generative methods (not just one)? | [Pass/Flag] | [Explanation] |
| 4 | Compliance & Ethics addressed as first-class risk? | [Pass/Flag] | [Explanation] |
| 5 | Decision criteria defined before research starts? | [Pass/Flag] | [Explanation] |
| 6 | AI used as accelerator, not replacement? | [Pass/Flag] | [Explanation] |

---

## Specific Observations

### [Observation 1: e.g., "Interview Reflex detected"]
**What you're doing**: [Describe the pattern in their plan]
**Why it might be karaoke**: [Connect to anti-pattern]
**Deliberate alternative**: [Suggest a better-matched method, with rationale]

### [Observation 2]
[Same format]

---

## Suggested Adjustments

1. [Concrete change — swap method X for Y because Z]
2. [Concrete change]
3. [Concrete change]

---

## Overall Health

**[Deliberate / Mild karaoke / Significant karaoke / Full karaoke]**
[1-2 sentence summary of the plan's strengths and the main adjustment needed]

---

*Framework: The Thinking Lens — "Stop Doing Discovery Karaoke" | the-thinking-lens.com*
```

---

## Formatting Rules

1. ALWAYS lead with what's working well — acknowledge strengths before flagging issues
2. Never say "you're doing it wrong" — frame as "this might be a default rather than a deliberate choice"
3. Every flagged symptom must include a concrete alternative
4. Use the 6-symptom checklist consistently
5. Overall health uses the same 4-band scale as the diagnostic
6. Include attribution
