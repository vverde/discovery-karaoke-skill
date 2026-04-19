# Discovery Karaoke — Constants

> Canonical reference for all counts and taxonomy values.
> When any number here changes, update this file first — all other files reference this as source of truth.
> Commands and templates are instructed to read these values from this file, not from hardcoded strings.

---

## Counts (update when DB changes)

- Active methods: 67
- Context tools: 13
- Total active entries: 80
- Superseded: 3
- Anti-patterns: 12
- Guardrails: 11

## Tier Counts (active methods only)

- Core: 31
- Extended: 41
- Specialist: 8

## Risks

| Code | Name | Core Question |
|------|------|--------------|
| V | Value / Desirability | Will customers buy/use this? |
| U | Usability | Can users figure it out? |
| F | Feasibility | Can we build it? |
| Vi | Viability | Does it work for the business? |
| C | Compliance & Ethics | Is it legal, ethical, and responsible? |

## Stages

| Stage | Purpose |
|-------|---------|
| Explore | Understand the problem, discover opportunities (Problem Space) |
| Validate | Test solutions, reduce uncertainty (Solution Space) |
| Optimize | Improve and measure what's live |

## Evidence Thresholds

| Bet Size | Methods Needed | Evidence Bar |
|----------|---------------|--------------|
| Small (feature tweak) | 1 method | Moderate |
| Medium (new feature) | 2 methods | Converging |
| Large (new product/pivot) | 3 methods (maximum) | Strong convergence across multiple risk types |

## Method ID Notes

- ID range: M1–M96 (non-contiguous — gaps are intentional, IDs are stable identifiers not sequence numbers)
- Known gaps: M34, M40, M41, M43, M50–M52, M61–M63, M85–M87
- Superseded: M25, M30, M46
- Source file: `data/discovery-methods-full.md`
