# Describe Template

Use this template for the `describe` command. Two modes based on `output_mode` config.

---

## Compact Mode (config: output_mode = compact, no `full` suffix)

Render as a box-drawn card using Unicode box characters. Keep total width ~66 chars.

```
┌─ [M##]: [Method Name] ──────────────────────────────────────┐
│ [One-sentence description — what it produces and when.]     │
│ [Continue on second line only if needed. Max 2 lines.]      │
├──────────────┬───────────┬──────────────┬────────┬──────────┤
│ [Tier]       │ [Risk]    │ [Stage]      │ [Time] │ [Evid.]  │
├──────────────┴───────────┴──────────────┴────────┴──────────┤
│ ⚠  [1 sentence — when this becomes a default, not a choice] │
└──────────────────────────────────────────────────────────────┘
  describe [M##] full · compare [M##] vs [M##]
```

**Rules for the card:**
- Title bar: `┌─ M##: Name ──...─┐` — pad dashes to reach ~66 chars total
- Description: 1–2 lines max, wrapped at ~60 chars inside `│ ... │`
- Metadata row: 5 cells — Tier / Risk code(s) / Stage(s) / Time range / Evidence strength
- Trap row: starts with `⚠ ` (single char, space), 1 sentence, no bold markup inside the box
- Footer: plain text below the box, no `│` — just the two commands separated by ` · `
- Pad all cell content with a trailing space before `│` for readability
- No markdown headers (`#`) in compact mode — the box IS the header

---

## Full Mode (config: output_mode = standard, or `full` suffix used)

```
# 🔍 [M##: Method Name]

**[One-line description of what this method is and what it produces]**

| | |
|---|---|
| **Tier** | [Core / Extended / Specialist] |
| **Category** | [Generative / Evaluative / Experimentation / Analytics / Compliance] |
| **Risk** | [V / U / F / Vi / C — spell out primary] |
| **Stage** | [Explore / Validate / Optimize] |
| **Time** | [Duration range] |
| **Cost** | [Time-only / Low / Medium / High] |
| **Effort** | [Low / Medium / High] |
| **Evidence** | [Weak / Moderate / Strong] |
| **User Access** | [None / Low / Moderate / High] |

---

## How to Apply

1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]
5. [Step 5 if needed]

---

## ✅ When to Use

- [Condition 1]
- [Condition 2]
- [Condition 3]

## ❌ When NOT to Use

- [Condition 1 — wrong risk, wrong stage, or wrong context]
- [Condition 2]

---

## ⚠️ Karaoke Check

**Default trap**: [When this method becomes a reflex rather than a deliberate choice]
**Deliberate signal**: [What good looks like — how you know it's the right method for the situation]

---

## 🤖 AI Augmentation

| Task | AI Can Help | AI Cannot Replace |
|------|------------|-------------------|
| [Task 1] | [How] | [What still needs humans] |
| [Task 2] | [How] | [What still needs humans] |

---

**Prerequisites**: [M## Name if any, or "None"]

---

`/discovery-karaoke compare [M##] vs [M##]` — compare with [alternative name]
```

---

## Formatting Rules

1. Compact mode: box-drawn card (~66 chars wide). No markdown headers. 5-cell metadata row. Karaoke trap inside box. Footer outside box.
2. Compact mode footer ALWAYS offers the `full` upgrade path and a compare offer
3. Full mode: vertical key-value metadata table, all sections
4. Always include Karaoke Check in both modes — it's the core value (G6)
5. Full mode: AI Augmentation always includes "cannot replace" column (G5)
6. End with compare offer if alternatives exist
