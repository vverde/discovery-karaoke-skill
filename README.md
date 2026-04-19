# Discovery Karaoke Prevention Engine — Claude Code Skill

> **Discovery Karaoke** = defaulting to the same familiar research methods out of habit instead of matching them to your actual risk and context.
> Default ≠ Deliberate. Familiar ≠ Fit-for-purpose.

A Claude Code skill that helps product teams pick the right discovery method for their situation — matched to risk, stage, and constraints. Built around the framework: **Risk → Stage → Method → Evidence**.

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

## Usage Examples

**You have a situation and want a recommendation:**
```
/discovery-karaoke assess We're pre-launch B2B SaaS, 3 design partners, want to test
whether our onboarding flow makes sense before we build it
```

**You're building an AI feature and need the right sequence:**
```
/discovery-karaoke ai We want to add an AI-generated summary to our dashboard.
We have 6 months of user data but haven't defined what "good" looks like yet
```

**Something feels off about your team's research practice:**
```
/discovery-karaoke diagnose
```

**You have a discovery plan and want a second opinion:**
```
/discovery-karaoke review We're planning 10 user interviews followed by a usability
test and then an A/B test — all before we write a line of code
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
| `review [plan]` | Critique an existing discovery plan against karaoke symptoms |
| `config save` | Save team constraints to `.discovery-karaoke-config.yml` |
| `about` | Framework overview and credits |
| `help` | Usage guide and all commands |

---

## The Toolkit

**80 active entries** (M1–M96): 67 discovery methods + 13 context tools (frameworks, synthesis tools, operating practices). Five risk types: Value/Desirability · Usability · Feasibility · Viability · Compliance & Ethics. Three stages: Explore · Validate · Optimize.

---

## Tests

```bash
# Structural + reference integrity (no API calls)
pytest tests/ -v

# Behavioral golden eval (requires ANTHROPIC_API_KEY)
python3 tests/golden_eval.py
```

After editing `data/discovery-methods-full.md`, regenerate the lite index:

```bash
python3 tests/generate_index.py
```

---

## Credits

**Framework**: Amodiovalerio Verde — ["Stop Doing Discovery Karaoke"](https://www.the-thinking-lens.com/stop-doing-discovery-karaoke/), The Thinking Lens (June 2025)

**Methods** sourced from established product discovery literature: Teresa Torres, Marty Cagan, Jake Knapp, Jeff Gothelf, Erika Hall, Carolyn Snyder, Eric Ries, and others.

## License

[CC BY-NC 4.0](LICENSE) — free to use, share, and adapt with attribution to Amodiovalerio Verde / The Thinking Lens. Commercial use prohibited.
