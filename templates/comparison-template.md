# Comparison Template

Use this template for the `compare` command. Check `output_mode` before rendering:
- **Compact mode** (default): use the Compact Template below
- **Standard mode** (config `output_mode: standard` or `full` suffix): use the Full Template below

---

## Compact Template

```
# [ID1: Name] vs [ID2: Name]

| Dimension | [ID1] | [ID2] |
|-----------|-------|-------|
| **Risk** | [codes] | [codes] |
| **Stage** | [stage] | [stage] |
| **Time** | [range] | [range] |
| **Cost** | [level] | [level] |
| **Evidence** | [strength] | [strength] |
| **User Access** | [level] | [level] |

**Choose [ID1]**: [condition 1] · [condition 2]
**Choose [ID2]**: [condition 1] · [condition 2]
**Use both**: [when they sequence well — 1 line]

⚠️ [ID1] karaoke risk: [1 sentence]
⚠️ [ID2] karaoke risk: [1 sentence]

*The right method depends on your risk and constraints.*
```

**Compact rules:**
- Side-by-side table: always shown
- Choose X: 2 conditions max (not 3), inline (not bullets)
- Use both: 1 line
- Karaoke risk: 1 sentence each

---

## Full Template

```
# Compare: [ID1: Name] vs [ID2: Name]

## Side-by-Side

| Dimension | [ID1: Name] | [ID2: Name] |
|-----------|-------------|-------------|
| **Risk** | [Risk codes] | [Risk codes] |
| **Stage** | [Stage] | [Stage] |
| **Time** | [Duration] | [Duration] |
| **Cost** | [Level] | [Level] |
| **Effort** | [Level] | [Level] |
| **Evidence** | [Strength] | [Strength] |
| **User Access** | [Required level] | [Required level] |
| **Best for** | [1-line context] | [1-line context] |

---

## When to Choose Each

**Choose [ID1: Name] when:**
- [Condition 1]
- [Condition 2]
- [Condition 3]

**Choose [ID2: Name] when:**
- [Condition 1]
- [Condition 2]
- [Condition 3]

**Use both (in sequence) when:**
- [Condition where they complement each other]

---

## Karaoke Check

- [ID1] karaoke risk: [When this method becomes a default rather than a deliberate choice]
- [ID2] karaoke risk: [When this method becomes a default rather than a deliberate choice]

---

*The right method depends on your risk and constraints. Neither is universally better.*
*Framework: The Thinking Lens — "Stop Doing Discovery Karaoke" | the-thinking-lens.com*
```

---

## Formatting Rules

1. Never declare a "winner" — always frame as "depends on context"
2. Always include when to use BOTH in sequence
3. Always show karaoke risk for each method
4. Include attribution
