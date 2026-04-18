# Matrix Template

Use this template for the `matrix` command. Four modes — use the matching section.

---

## Mode 1: Compact Overview (no args)

```
# 📊 Discovery Method Matrix

> Top methods per cell. Pick your risk, find your stage, start there.

| Risk | Explore | Validate | Optimize |
|------|---------|----------|----------|
| **Value / Desirability** *Will they want this?* | [M## Name] · [M## Name] | [M## Name] · [M## Name] | [M## Name] · [M## Name] |
| **Usability** *Can they use it?* | [M## Name] · [M## Name] | [M## Name] · [M## Name] | [M## Name] · [M## Name] |
| **Feasibility** *Can we build it?* | [M## Name] · [M## Name] | [M## Name] · [M## Name] | [M## Name] · [M## Name] |
| **Viability** *Does it work for the business?* | [M## Name] · [M## Name] | [M## Name] · [M## Name] | [M## Name] · [M## Name] |
| **Compliance & Ethics** *First-class risk* | [M## Name] · [M## Name] | [M## Name] · [M## Name] | [M## Name] · [M## Name] |

---

Need more detail?

| Command | What it shows |
|---------|--------------|
| `matrix full` | All methods per cell |
| `matrix [risk]` | Full row — all stages + constraint picks |
| `matrix [risk] [stage]` | Single cell — all methods + constraint picks |

Risks: `value` | `usability` | `feasibility` | `viability` | `compliance`

---

*Starting point only. For a context-matched recommendation: `/discovery-karaoke assess [situation]`*
*Evidence thresholds — Small bet: 1 method. Medium: 2 converging. Large: 3+ converging.*
```

---

## Mode 2: Full Matrix (matrix full)

```
# 📊 Discovery Method Matrix — Full

---

### Value / Desirability — *Will they want this?*

| Stage | Methods | Evidence |
|-------|---------|----------|
| **Explore** | [M## Name] · [M## Name] · [M## Name] | [Range] |
| **Validate** | [M## Name] · [M## Name] · [M## Name] | [Range] |
| **Optimize** | [M## Name] · [M## Name] · [M## Name] | [Range] |

---

### Usability — *Can they use it?*

| Stage | Methods | Evidence |
|-------|---------|----------|
| **Explore** | [M## Name] · [M## Name] | [Range] |
| **Validate** | [M## Name] · [M## Name] · [M## Name] | [Range] |
| **Optimize** | [M## Name] · [M## Name] · [M## Name] | [Range] |

---

### Feasibility — *Can we build it?*

| Stage | Methods | Evidence |
|-------|---------|----------|
| **Explore** | [M## Name] · [M## Name] · [M## Name] | [Range] |
| **Validate** | [M## Name] · [M## Name] · [M## Name] | [Range] |
| **Optimize** | [M## Name] · [M## Name] | [Range] |

> [Include AI addendum if applicable: M89 → M91 → M90 sequence note]

---

### Viability — *Does it work for the business?*

| Stage | Methods | Evidence |
|-------|---------|----------|
| **Explore** | [M## Name] · [M## Name] · [M## Name] | [Range] |
| **Validate** | [M## Name] · [M## Name] · [M## Name] | [Range] |
| **Optimize** | [M## Name] · [M## Name] · [M## Name] | [Range] |

---

### Compliance & Ethics — *First-class risk*

| Stage | Methods | Evidence |
|-------|---------|----------|
| **Explore** | [M## Name] · [M## Name] · [M## Name] | [Range] |
| **Validate** | [M## Name] · [M## Name] · [M## Name] | [Range] |
| **Optimize** | [M## Name] · [M## Name] · [M## Name] | [Range] |

---

*Starting point only. For a context-matched recommendation: `/discovery-karaoke assess [situation]`*
*Evidence thresholds — Small bet: 1 method. Medium: 2 converging. Large: 3+ converging.*
```

---

## Mode 3: Full Row (matrix [risk])

```
# 📊 [Risk Name] — All Stages

*[Risk question]*

| Stage | Methods | Evidence |
|-------|---------|----------|
| **Explore** | [M## Name] · [M## Name] · [M## Name] | [Range] |
| **Validate** | [M## Name] · [M## Name] · [M## Name] | [Range] |
| **Optimize** | [M## Name] · [M## Name] · [M## Name] | [Range] |

---

## Quick Picks by Constraint

**⚡ Urgent + Low budget** (days, minimal spend):
- Explore: [M## Name] · [M## Name]
- Validate: [M## Name] · [M## Name]
- Optimize: [M## Name] · [M## Name]

**🚫 No user access** (without talking to users):
- Explore: [M## Name] · [M## Name]
- Validate: [M## Name] · [M## Name]
- Optimize: [M## Name] · [M## Name]

**🏢 B2B specific**:
- Explore: [M## Name] · [M## Name]
- Validate: [M## Name] · [M## Name]
- Optimize: [M## Name] · [M## Name]

**🚀 Pre-launch** (no existing product/users):
- Explore: [M## Name] · [M## Name]
- Validate: [M## Name] · [M## Name]

---

Drill into a cell: `matrix [risk] explore` | `matrix [risk] validate` | `matrix [risk] optimize`

*Starting point only. For a context-matched recommendation: `/discovery-karaoke assess [situation]`*
*Evidence thresholds — Small bet: 1 method. Medium: 2 converging. Large: 3+ converging.*
```

---

## Mode 4: Single Cell (matrix [risk] [stage])

```
# 📊 [Risk Name] × [Stage] — All Methods

*[Risk question] at [Stage] stage.*

| M## | Method | Time | Evidence | User Access |
|-----|--------|------|----------|-------------|
| [M##] | [Name] | [Time] | [Evidence] | [Access] |
| [M##] | [Name] | [Time] | [Evidence] | [Access] |

---

## Quick Picks by Constraint

**⚡ Urgent + Low budget**: [M## Name] · [M## Name]
**🚫 No user access**: [M## Name] · [M## Name]
**🏢 B2B**: [M## Name] · [M## Name]
**🚀 Pre-launch**: [M## Name] · [M## Name]

---

## ⚠️ Karaoke Watch

[1-2 sentence warning about the habitual default for this risk × stage cell — which method teams tend to reach for automatically and why it may not be the best fit.]

---

*Starting point only. For a context-matched recommendation: `/discovery-karaoke assess [situation]`*
*Evidence thresholds — Small bet: 1 method. Medium: 2 converging. Large: 3+ converging.*
```

---

## Formatting Rules

1. Always use the risk question as a subtitle — not just the risk name
2. Mode 1 and 2: show ALL five risks with clear separators
3. Mode 3: always include all 4 constraint scenarios from the data file
4. Mode 4: always include the karaoke watch warning
5. Footer on every mode — both the assess offer AND the evidence threshold reminder
6. Constraint icons (⚡🚫🏢🚀) make the quick picks section scannable
