# Discovery Karaoke Prevention Engine — Claude Code Skill

> **Discovery Karaoke** = defaulting to the same familiar research methods out of habit instead of matching them to your actual risk and context.
> Default ≠ Deliberate. Familiar ≠ Fit-for-purpose.

A Claude Code skill that helps product teams stop doing Discovery Karaoke — matching the right discovery method to the right risk, stage, and context. Built around the framework: **Risk → Stage → Method → Evidence**.

**Live web app:** [discovery.the-thinking-lens.com](https://discovery.the-thinking-lens.com)

---

## Install

```bash
npx @anthropic-ai/claude-code skills add [username]/discovery-karaoke-skill
```

Or install manually: copy the repo contents into `~/.claude/skills/discovery-karaoke/`.

Invoke with:

```
/discovery-karaoke [command] [args]
```

---

## Commands

| Command | What it does |
|---------|-------------|
| `assess [situation]` | Full context-matched recommendation — risk, stage, constraints, karaoke check |
| `quick [situation]` | 4-question fast path — top methods in under 2 minutes |
| `plan [situation]` | Full discovery arc across Explore → Validate → Optimize with decision gates |
| `ai [situation]` | AI product specialist path — M89 → M91 → M90 sequence, EU AI Act, simulation trap |
| `list methods [filter]` | Browse 67 active methods by risk, stage, category, or constraint |
| `list tools` | Browse 13 context tools (frameworks, synthesis tools, operating practices) |
| `describe M##` | Deep-dive on a specific method or context tool |
| `compare M## vs M##` | Side-by-side comparison of two methods |
| `matrix [risk] [stage]` | Risk × Stage navigation — top methods per cell |
| `diagnose` | 36-point interactive diagnostic — identify karaoke patterns in your practice |
| `review [plan]` | Critique an existing discovery plan against 6 karaoke symptoms |
| `config save` | Save team constraints to `.discovery-karaoke-config.yml` |
| `about` | Framework overview and credits |
| `help` | Usage guide and all commands |

---

## The Framework

**Five discovery risks** — every method maps to one or more:

| Risk | Core Question |
|------|--------------|
| Value / Desirability | Will customers buy or use this? |
| Usability | Can users figure it out? |
| Feasibility | Can we build it? |
| Viability | Does it work for the business? |
| Compliance & Ethics | Is it legal, ethical, and responsible? |

**Three discovery stages:** Explore (problem space) · Validate (solution space) · Optimize (live product)

**Evidence threshold = bet size:** Small bet → 1 method. Medium → 2. Large → 3 (maximum).

---

## The Toolkit

**80 active entries** (M1–M96, non-contiguous):

- **67 discovery methods** across three tiers — Core (31), Extended (41), Specialist (8)
- **13 context tools** — Frameworks, Synthesis Tools, and Operating Practices that structure thinking; not standalone discovery activities

Categories: Generative · Evaluative · Experimentation · Analytics · Compliance & Ethics · AI Feasibility

Each method entry includes: risk tags, stage, time/effort/cost, evidence strength, when to use, when NOT to use, karaoke check, and AI augmentation note.

---

## Architecture

```
discovery-karaoke-skill/
├── SKILL.md                          # Command router + 11 guardrails + framework reference
│                                     # Always loaded; ~160 lines / ~1,400 tokens
├── commands/  (14 files)
│   ├── assess.md                     # Full recommendation flow (signal pre-fill, 3 batches)
│   ├── quick.md                      # 4-question fast path
│   ├── plan.md                       # Full arc: Explore → Validate → Optimize
│   ├── ai.md                         # AI product specialist path
│   ├── list.md                       # Browse/filter methods
│   ├── describe.md                   # Method deep-dive
│   ├── compare.md                    # Side-by-side comparison
│   ├── matrix.md                     # Risk × Stage navigation
│   ├── diagnose.md                   # 36-point karaoke diagnostic
│   ├── review.md                     # Plan critique
│   ├── config.md                     # Team config management
│   ├── about.md                      # Framework attribution
│   ├── help.md                       # Usage guide
│   └── answer.md                     # Smart fallback for framework Q&A
├── templates/  (10 files)
│   └── [command]-template.md         # Compact + full output formats per command
├── data/  (7 files)
│   ├── discovery-methods-full.md     # Source DB: 80 active entries (~5,100 lines)
│   ├── methods-index.md              # Generated lite index — metadata only (95 lines)
│   ├── risk-method-matrix.md         # Risk × Stage → method IDs + constraint quick picks
│   ├── anti-patterns.md              # 12 named anti-patterns + 36-point diagnostic
│   ├── ai-guardrails.md              # AI-in-discovery guardrails and Simulation Trap
│   ├── constants.md                  # Single source of truth for all counts
│   └── about.md                      # Framework overview text (used by about command)
├── tests/
│   ├── test_structure.py             # 30 structural/reference integrity tests
│   └── test_references.py            # 13 M-code cross-reference consistency tests
└── local/  (gitignored)
    ├── generate_index.py             # Regenerates methods-index.md from source DB
    ├── golden_eval.py                # Behavioral tests against Claude API
    └── golden-cases.yaml             # 11 golden test cases
```

Command files and data files are loaded on demand — only when the routed command needs them. `SKILL.md` is the only file always in context.

---

## Output Modes

Two modes controlled by config or per-command `full` suffix:

- **`compact`** (default) — short-form output: tighter tables, fewer sections, karaoke check in 3 sentences
- **`standard`** — full output: all sections, prose explanations, Evidence Convergence Map

Override per command:
```
/discovery-karaoke assess full [situation]   # standard output for this invocation only
```

Set globally:
```
/discovery-karaoke config save               # set output_mode: standard in config
```

---

## Config

Save team constraints to avoid repeating them on every `assess` invocation:

```
/discovery-karaoke config save
```

Creates `.discovery-karaoke-config.yml` in the current working directory:

```yaml
team:
  company_size: [Startup|Scaleup|Enterprise]
  business_model: [B2B|B2C|B2B2C|Internal]
  user_access: [Easy|Moderate|Limited]
  team_size: [Solo|Small|Cross-functional]
  customer_base: [None|Small|Medium|Large]
  regulated: [true|false]
  output_mode: [compact|standard]
created: YYYY-MM-DD
```

Config stores constraint fields only. Risk, stage, and past recommendations are never saved.

---

## Tests

```bash
# Structural + reference integrity (no API calls)
pytest tests/ -v

# Behavioral golden eval (requires ANTHROPIC_API_KEY)
python3 local/golden_eval.py
```

After editing `data/discovery-methods-full.md`, regenerate the lite index:

```bash
python3 local/generate_index.py
```

---

## Guardrails

11 always-active rules applied to every output:

| # | Guardrail | Rule |
|---|-----------|------|
| G1 | Source Integrity | Attribution in `about` only — not on every output |
| G2 | Risk-Method Integrity | Methods recommended only with a named risk |
| G3 | Evidence = Blast Radius | Method count matched to bet size; over-researching is also karaoke |
| G4 | Compliance First-Class | Auto-elevated for regulated industries, AI products, sensitive data |
| G5 | AI ≠ Real Users | AI outputs are hypotheses; always paired with real-user validation |
| G6 | Anti-Pattern Check | Named anti-pattern surfaced on every recommendation |
| G7 | Config Safety | Stores only constraints — risk/stage never saved |
| G8 | Data Integrity | Skill never modifies its own data, template, or command files |
| G9 | Graceful Degradation | Unknown commands and missing data handled gracefully |
| G10 | Minimum Sufficient Methods | 1–2 primary methods; never 3+ simultaneously |
| G11 | Guided Disclosure | No-arg commands surface options, never dump everything |

---

## Credits

**Framework**: Amodiovalerio Verde — ["Stop Doing Discovery Karaoke"](https://www.the-thinking-lens.com/stop-doing-discovery-karaoke/), The Thinking Lens (June 2025)

**Methods** sourced from established product discovery literature: Teresa Torres, Marty Cagan, Jake Knapp, Jeff Gothelf, Erika Hall, Carolyn Snyder, Eric Ries, and others.

## License

[CC BY 4.0](LICENSE) — free to use, share, and adapt with attribution to Amodiovalerio Verde / The Thinking Lens.
