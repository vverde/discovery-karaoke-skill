# List Template

Use this template for the `list` command. Four variants × two output modes.

---

## Variant 1: Filter Guidance (list methods — no filter)
*(Same in both output modes — always compact)*

```
# Browse Discovery Methods

Filter options (AND logic — combine freely):

| Dimension | Options |
|-----------|---------|
| **Risk** | `value` · `usability` · `feasibility` · `viability` · `compliance` |
| **Stage** | `explore` · `validate` · `optimize` |
| **Category** | `generative` · `evaluative` · `experimentation` · `analytics` · `compliance` |
| **Constraint** | `B2B` · `B2C` · `startup` · `enterprise` · `solo` · `urgent` · `no-users` |

**Examples:**
- `list methods value` — all Value/Desirability methods
- `list methods B2B explore` — B2B-relevant Explore methods
- `list methods compliance validate` — Compliance methods for Validate stage

To show all 67 active methods: `list methods all`
```

---

## Variant 2: Filtered Results — Compact (config: output_mode = compact)

```
# [Filter Applied] — [X] methods

| M## | Name | Stage |
|-----|------|-------|
| [M##] | [Name] | [Stage] |

---

`/discovery-karaoke describe [M##]` — summary card
`/discovery-karaoke describe [M##] full` — full entry
`list methods [filter] full` — show all columns
```

---

## Variant 2: Filtered Results — Standard (default)

```
# Discovery Methods: [Filter Applied]

Showing [X] of 67 active methods.

| M## | Name | Risk | Stage | Category | Tier | Time | Evidence |
|-----|------|------|-------|----------|------|------|----------|
| [M##] | [Name] | [Risk] | [Stage] | [Category] | [Tier] | [Time] | [Evidence] |

---

`/discovery-karaoke describe [M##]` — full entry for any method
`/discovery-karaoke compare [M##] vs [M##]` — side-by-side comparison
```

---

## Variant 3: All Methods — Compact (config: output_mode = compact)

```
# All Methods (67 Active)

| M## | Name | Stage |
|-----|------|-------|
[All 67 active methods — 3 columns only]

---

> Tiers: Core (31) · Extended (41) · Specialist (8)
> `list methods all full` — show all columns
> `list tools` — context tools
```

---

## Variant 3: All Methods — Standard (default)

```
# All Discovery Methods (67 Active)

| M## | Name | Risk | Stage | Category | Tier | Time | Evidence |
|-----|------|------|-------|----------|------|------|----------|
[All 67 active methods]

---

> 67 active methods shown. 3 superseded methods excluded.
> Tiers: Core (31) · Extended (41) · Specialist (8)
> Context tools listed separately: `/discovery-karaoke list tools`

`/discovery-karaoke describe [M##]` — full entry for any method
```

---

## Variant 4: Context Tools
*(Same in both output modes — only 13 tools, always show all columns)*

```
# Context Tools (13)

Context tools structure discovery thinking. Use them alongside evidence-generating methods — not as standalone discovery activities.

| M## | Tool | Type | Primary Pairing |
|-----|------|------|----------------|
| [M##] | [Name] | [Type] | [Risk codes — paired methods] |

---

> These tools do not generate independent user evidence.
> Start with a discovery method, use a context tool to structure or synthesize.

`/discovery-karaoke describe [M##]` — full entry for any context tool
```

---

## Formatting Rules

1. Variant 1 (filter guidance): always compact — it's navigation, not data
2. Variants 2/3 compact: 3 columns only (M##, Name, Stage). Always include `full` upgrade offer
3. Variants 2/3 standard: 8 columns. Always include describe offer
4. Variant 4 (tools): always 4 columns — only 11 rows, full columns always worth showing
5. Show match count ("Showing X of 67") in Variants 2/3 — helps user see if filter is too narrow
6. Never include superseded methods in any variant
