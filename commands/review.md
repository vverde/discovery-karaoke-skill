# CMD: review [plan]

**Trigger**: `review`

**No plan provided**: Ask:
> "Describe your current discovery plan — what methods are you planning or currently running, and what decision are you trying to make?"

**Data files**:
- `data/anti-patterns.md` — named patterns + Meta Anti-Pattern
- `data/risk-method-matrix.md` — method-risk alignment check
- `data/discovery-methods-full.md` — method lookups if needed
- `templates/review-template.md` — output card format

**Step 1**: Read `data/anti-patterns.md` in full.

**Step 2**: Analyze the described plan against these criteria:
- Are methods matched to specific named risks? (G2)
- Is evidence threshold appropriate for the bet size? (G3)
- Are both generative and evaluative methods present, or only one type?
- Is Compliance & Ethics addressed if applicable? (G4)
- Are decision criteria defined before research starts?
- Is AI used as accelerator only, not as replacement for user signal? (G5)
- Does the plan match any of the named anti-patterns or the Meta Anti-Pattern (Static Playbook)?

**Step 3**: For each karaoke symptom found, **name the specific anti-pattern** from `data/anti-patterns.md`. Do not use generic descriptions.

**Step 4**: Read `templates/review-template.md`. Deliver output using that card structure exactly.

**Step 5: Offer follow-up**:
- `/discovery-karaoke assess [situation]` — get a fresh method recommendation for the same situation
- `/discovery-karaoke plan [situation]` — map the full discovery arc across all stages
- `/discovery-karaoke diagnose` — check if the karaoke patterns found here extend across your broader discovery practice

**Note**: Health score uses the same 4-band scale as `diagnose` (read bands from `data/anti-patterns.md`).
