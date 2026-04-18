# CMD: config save|show|clear

**Trigger**: `config`

**No subcommand**: Apply G11:
> "Available: `config save` | `config show` | `config clear`"

---

**config save**:

Ask via AskUserQuestion:
1. Company size: Startup / Scaleup / Enterprise
2. Business model: B2B / B2C / B2B2C / Internal
3. User access: Easy / Moderate / Limited
4. Team size: Solo / Small (2–5) / Cross-functional (5+)
5. Customer base: None / Small / Medium / Large
6. Regulated industry: Yes / No
7. Output mode: Standard (full output by default) / Compact (short summaries by default — use `full` suffix to expand)

Warn if overwriting an existing config (G7).

Write to `.discovery-karaoke-config.yml` in the working directory:

```yaml
# Discovery Karaoke — Team Config
# Saved by /discovery-karaoke config save
# Constraints only. Risk and stage are NOT saved — they change per decision.
team:
  company_size: [value]
  business_model: [value]
  user_access: [value]
  team_size: [value]
  customer_base: [value]
  regulated: [true/false]
  output_mode: [standard|compact]
created: [YYYY-MM-DD]
```

---

**config show**: Read `.discovery-karaoke-config.yml` and display in readable format. If none exists: "No config saved. Run `config save` to set your team context."

---

**config clear**: Confirm before deleting. On confirm: delete `.discovery-karaoke-config.yml`.
