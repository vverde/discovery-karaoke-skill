# AI in Discovery: Guardrails & Opportunities

> **Core principle**: AI compresses time to signal. It NEVER replaces real user signal.
> AI-simulated feedback is a hypothesis accelerator, not evidence.
>
> **2026 update**: AI increases validation burden, it does not reduce it. The easier it is to generate synthetic insights, the more critical real evidence becomes. This applies doubly when teams are using AI to discover how to build AI features — the circularity is a real risk.

---

## What AI CAN Do in Discovery

### Preparation Tasks

| Task | How AI Helps | Example |
|------|-------------|---------|
| **Theme clustering** | Analyze interview transcripts to surface patterns | 10 interview transcripts → 5 recurring themes with representative quotes |
| **Survey feedback summarization** | Compress hundreds of open-ended responses into themes | 500 NPS comments → Top 10 themes with frequency counts |
| **Discussion guide drafting** | Generate interview questions from research objectives | "We want to understand why users churn" → 15 structured interview questions |
| **Usability task drafting** | Create task scenarios from user stories | User stories → 8 usability tasks with success criteria for M16/M17 |
| **Objection extraction** | Analyze sales call recordings for common objections (M8) | 20 sales calls → Top 5 objections ranked by frequency |
| **Regulatory risk flagging** | Scan requirements against legal and regulatory frameworks | Feature spec → Potential GDPR/EU AI Act/HIPAA exposure flagged (legal regimes) |
| **Control framework flagging** | Scan requirements against assurance and control frameworks | Feature spec → Potential SOC 2/ISO 27001 control gaps flagged (attestation frameworks, not regulations) |
| **Assumption generation** | Surface implicit assumptions in a product brief | Product brief → 20 assumptions to test, ranked by risk level |
| **Behavioral pattern detection** | Identify patterns in usage analytics data | Session data → Usage clusters and behavioral segments |
| **Competitive landscape mapping** | Synthesize competitive intelligence from public sources (M42) | Market category → Feature comparison matrix + gap analysis |
| **Survey question review** | Check for bias, leading questions, and double-barrel items | Draft survey → Flagged issues with suggested rewrites |
| **Capability Contract drafting** | Generate initial v0 contract from a feature brief (M89) | AI feature spec → Proposed Allowed/Forbidden/Evidence/Retrieval fields |
| **Test case generation** | Generate diverse test cases for AI capability evaluation (M90) | Capability claim → 50 test cases including edge cases and failure modes |
| **Data gap mapping** | Suggest common data quality dimensions by domain (M91) | AI feature spec → Data readiness assessment template |

### Analysis Acceleration Tasks

| Task | How AI Helps | Guardrail |
|------|-------------|-----------|
| **Transcript analysis** | Code and tag interview data | Always validate AI codes against source material |
| **Sentiment analysis** | Score feedback at scale (M12) | Use for triage and prioritization, not as final evidence |
| **Pattern matching** | Find similar issues across data sources | Verify matches; AI may conflate similar-but-different issues |
| **Data visualization prep** | Structure data for charts and presentations | Review for accuracy before presenting to stakeholders |
| **Synthesis drafts** | Draft research reports from raw data | Always review and validate against primary sources |
| **Co-analysis** | AI as a second analyst during synthesis workshops | The researcher decides which themes are real; AI suggests, humans judge |
| **Heatmap and session interpretation** | Flag rage clicks, dead zones, error patterns (M58, M59) | AI tools surface anomalies; human judgment required for root cause |
| **Churn pattern analysis** | Identify exit cohort patterns from CRM and product data (M92) | Structural patterns only; exit reasons require real interviews |

### Hypothesis Acceleration Tasks (with caveats)

| Task | How AI Helps | Critical Caveat |
|------|-------------|----------------|
| **User response simulation** | Predict how users might react to concepts | NEVER use as evidence. Use only to generate hypotheses to test with real users |
| **Assumption stress-testing** | Challenge your assumptions with counterarguments (M32) | AI may miss domain-specific realities. Use as a thinking prompt, not as validation |
| **Edge case generation** | Identify scenarios the team has not considered | Supplement with real user data. AI imagines edge cases; users reveal real ones |
| **Persona enrichment** | Add depth to persona attributes (M38) | Validate enriched personas against real user segments |
| **Pre-mortem scenario generation** | Generate failure scenarios from comparable products (M64) | AI generates plausible failures; real domain experts identify critical ones |

---

## What AI CANNOT Do in Discovery

### Never Use AI As...

| Misuse | Why It Fails | What to Do Instead |
|--------|-------------|-------------------|
| **Substitute for user interviews** | AI generates plausible but not necessarily true user perspectives | Talk to real users (M1, M2, M60). AI helps you prepare, not replace |
| **Final evidence for go/no-go decisions** | AI confidence ≠ user reality. Models reflect training data, not your users | Use real-world evidence: experiments, observations, live data |
| **Replacement for usability testing** | AI-moderated sessions cannot probe unexpected behavior or adapt in real time; NN/g notes AI cannot know what users are actually doing | Test with real users (M16, M17). AI can draft the test plan |
| **Market validation** | AI can reflect what people have said publicly; it cannot tell you whether your specific users will pay under your conditions | Run real demand tests: M23, M24, M26, M48 |
| **Compliance sign-off** | AI is not a lawyer and is not calibrated to your regulatory context; flags are inputs, not clearance | Use AI to flag potential issues; have qualified experts evaluate (M76, M84) |
| **Replacement for observation** | AI has no access to the physical context of use | Contextual inquiry (M3), ethnographic research (M4), and shadowing (M66) remain irreplaceable |
| **AI capability confirmation** | AI-based evaluation can support scoring at scale but is not sufficient evidence for production readiness or go/no-go decisions on its own | Run a structured AI Capability Assessment (M90) against real representative data |
| **Data readiness confirmation** | AI cannot access your data systems to verify permissions, availability, or quality | Run a Data Readiness Assessment (M91); requires human access to actual data systems |

---

## The Simulation Trap

**Danger zone**: Teams that use AI to "simulate user feedback" and then treat the output as evidence.

**Why it is dangerous:**
1. AI generates plausible text, not truthful text
2. AI reflects training data distributions, not your specific users
3. AI cannot surprise you with behaviors you have not conceived of
4. AI-simulated feedback creates false confidence that forecloses real discovery

**The Synthetic Population Warning**: AI can now generate entire synthetic user populations — personas with backstories, simulated survey responses, even fake interview transcripts. The output looks indistinguishable from real research. This makes the simulation trap far more dangerous than in 2023–2024: the failure mode is no longer "obviously fake data" but "convincingly fake data that passes review."

**Acceptable use**: "AI, given what we know about our users, what objections might they have to this feature?" → Use this to generate hypotheses, then test them with real users.

**Unacceptable use**: "AI, would our users like this feature?" → Treating the response as evidence.

---

## AI in AI Product Discovery (Special Case)

When teams are using discovery methods to evaluate, design, or validate AI features, standard guardrails apply — but there are additional risks specific to this domain.

### The Circularity Problem

Using AI to assess AI is not inherently circular — LLM-as-judge evaluation (using a strong judge model to score outputs at scale) is a legitimate technique for scaling quality assessment when calibrated against human labels. It is now standard in evaluation pipelines (Zheng et al., 2023 — MT-Bench, Chatbot Arena). Known limits apply: position bias, verbosity bias, self-enhancement bias when the judge and the evaluated model share the same family, and no inherent calibration to your business definition of "good enough."

The real circularity risk is narrower: asking a conversational AI whether your AI feature *will work*, whether your capability claim *is met*, or whether your data *is sufficient* — without a structured test set, without real representative data, and without human judgment on the acceptance threshold. AI can score outputs at scale; it cannot set the bar or confirm the system meets it. LLM-as-judge can be one scoring mechanism inside an AI Capability Assessment (M90) — it does not replace the representative test set, the threshold definition, or the human go/no-go decision.

A language model also cannot reliably tell you what data permissions your AI system needs, or whether your AI feature creates ethical or regulatory exposure. Those require structured methods with real data and qualified expert judgment.

### The Three AI Feasibility Methods

The database includes a dedicated cluster for AI-specific feasibility discovery:

| Method | What It Does | When to Use |
|--------|-------------|-------------|
| **M89 Capability Contract Workshop** | Defines the explicit boundaries of an AI system — Allowed/Forbidden/Evidence/Retrieval/Escalation — before committing to build | At the start of any AI feature, before architecture decisions |
| **M90 AI Capability Assessment** | Tests whether available AI technology meets the performance threshold required for a feature to be viable, against real representative data | Before committing engineering resources to an AI feature |
| **M91 Data Readiness Assessment** | Evaluates whether required training, fine-tuning, RAG, or evaluation data is available, permissioned, and quality-sufficient | Before any feature requiring proprietary or curated data |

**Sequence matters**: Run M89 first to surface constraints, then M91 to assess data availability against those constraints, then M90 to test whether the capability claim holds. Skipping M89 means M90 tests the wrong thing; skipping M91 means M90 runs on unverified data.

### What AI CAN Do in AI Product Discovery

- Draft the initial Capability Contract (v0) from a feature brief for the team to validate (M89)
- Generate diverse test cases for capability assessment, including edge cases the team missed (M90)
- Draft the data readiness assessment template for a specific feature type (M91)
- Flag terms in a feature specification that indicate regulatory exposure under GDPR, EU AI Act, or HIPAA

> **EU AI Act timing note (April 2026)**: The Act entered into force 1 August 2024. Prohibited practices and AI literacy obligations applied from 2 February 2025; GPAI model obligations from 2 August 2025. Full applicability for most high-risk system provisions: 2 August 2026. As of April 2026, full obligations are not yet live — but risk assessment and documentation practices should be in place now for any system that will be subject to them.

### What AI CANNOT Do in AI Product Discovery

- Confirm whether a capability claim is met — that requires running the actual test against real data (M90)
- Verify data permissions or availability — that requires human access to data systems (M91)
- Provide compliance sign-off on AI system design — that requires qualified legal and compliance review (M76, M77, M84)
- Validate AI outputs for safety, bias, or fairness — that requires AI Red Teaming (M81) and structured Fairness Assessment (M80)

---

## AI Integration by Discovery Method

### Methods Where AI Adds High Value

| Method | AI Role | Time Impact |
|--------|---------|-------------|
| **M11/M12 Surveys** | Theme extraction, sentiment scoring, response clustering | Handles the bulk of categorization work |
| **M1 User Interview preparation** | Discussion guide drafting, question review | Cuts prep time significantly |
| **M42 Competitive analysis** | Data gathering, feature comparison matrices | Handles most of the data-gathering pass |
| **M6 Support ticket analysis** | Categorization, trend identification, sentiment at scale | Handles most categorization work |
| **M8 Sales call analysis** | Objection extraction, competitor mention tracking, pattern scoring | AI tools (Gong, Chorus) make this near-automatic |
| **M32 Assumption mapping** | Assumption generation from brief, risk scoring | Accelerates workshop preparation significantly |
| **M60 Continuous interviewing** | Real-time transcription, pattern tracking across weeks, insight repository maintenance | Reduces the administrative burden of high-cadence research |
| **M89 Capability Contract drafting** | Generate v0 contract with common patterns for review | Cuts drafting time from hours to minutes |
| **M90 AI capability test case generation** | Produce diverse test cases including edge cases | Reduces manual test case design significantly |

### Methods Where AI Adds Moderate Value

| Method | AI Role | Limitation |
|--------|---------|-----------|
| **M16/M17 Usability testing** | Task scenario drafting, post-session issue tagging | Cannot replace human observation or real-time facilitation |
| **M35 Journey mapping** | Draft map from existing data, identify gaps | Cannot replace workshop co-creation with real users |
| **M38 Persona development** | Enrichment from data, behavioral attribute suggestions | Must be validated against real user segments |
| **M20 A/B testing** | Hypothesis generation, segment analysis | Cannot replace statistical rigor or production traffic |
| **M91 Data Readiness Assessment** | Template generation, gap analysis drafting | Cannot assess actual data quality or permissions |
| **M64 Pre-mortem** | Failure scenario generation from comparable products | AI generates plausible scenarios; experts identify critical ones |

### Methods Where AI Adds Low Value

| Method | Why AI Does Not Help Much |
|--------|--------------------------|
| **M3 Contextual inquiry** | Requires being physically present with users |
| **M4 Ethnographic research** | Requires immersion in user environment over time |
| **M5 Diary studies** | Requires real user self-reporting over time |
| **M31 Design Sprint** | Requires real-time cross-functional collaboration and human judgment |
| **M26 Concierge MVP** | Requires delivering real service to real users |
| **M10 Focus groups** | Requires managing real group dynamics in real time |
| **M80 Fairness and Bias Assessment** | Requires domain expertise and structured evaluation of model behavior on real data |
| **M81 AI Red Teaming** | Requires adversarial human creativity; AI cannot red-team itself reliably |

---

## Guardrails Summary: Allowed vs. Prohibited

| Use | Allowed | Prohibited |
|-----|---------|-----------|
| **Qualitative synthesis** | Cluster themes from interviews, summarize open text | Treat AI clusters as ground truth without human review |
| **Test design** | Draft tasks, prompts, and scenarios | Let AI pick the research question or declare success |
| **Sales signals** | Extract objections from calls (M8) | Fabricate evidence of demand |
| **Compliance signals** | Flag terms that indicate regulatory risk | Treat flags as legal sign-off |
| **Copy exploration** | Simulate responses for shaping copy variants | Use simulation as substitute for desirability or usability evidence |
| **AI capability discovery** | Draft Capability Contract (M89), generate test cases (M90) | Treat AI self-assessment as a capability confirmation |
| **Data readiness** | Draft assessment template, suggest quality dimensions (M91) | Accept AI output as proof that data is available or permissioned |
| **Assumption generation** | Generate counterarguments and edge cases (M32, M64) | Treat AI-generated challenges as validation |

---

## Implementation Checklist

When using AI in your discovery process:

- [ ] **Label all AI-generated insights as hypotheses**, not findings
- [ ] **Track which insights came from AI vs. real users** in your research repository
- [ ] **Never present AI-generated feedback to stakeholders as user evidence**
- [ ] **Use AI outputs as inputs to real research**, not replacements for it
- [ ] **Validate AI-identified patterns** with at least 2–3 real user data points before acting
- [ ] **Keep AI in preparation and analysis phases**, not in the evidence-gathering phase
- [ ] **Document your AI usage** in research methodology notes for transparency
- [ ] **Review AI suggestions for bias** — models may reflect dominant user patterns and miss minority segments
- [ ] **For AI features**: run M89 → M91 → M90 before committing to build — do not let AI simulate this feasibility check
- [ ] **For compliance-sensitive features**: use AI to flag, not to clear — always route to M76, M77, or M84 for human expert review

---

## Sources

1. **NIST (2024)**. *Artificial Intelligence Risk Management Framework: Generative AI Profile (NIST AI 600-1)*. National Institute of Standards and Technology. doi:10.6028/NIST.AI.600-1 — Defines trustworthiness dimensions for GenAI systems including reliability, safety, and explainability. Grounds the evaluation and capability assessment guardrails.

2. **European Parliament (2024)**. *Regulation (EU) 2024/1689 — Artificial Intelligence Act*. Official Journal of the European Union. https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401689 — Entry into force: 1 August 2024. Key dates: prohibited practices 2 Feb 2025; GPAI obligations 2 Aug 2025; high-risk system provisions fully applicable 2 Aug 2026.

3. **Nielsen Norman Group (2024)**. *AI Can Damage UX Research if Used Incorrectly*. NN/g Report. https://www.nngroup.com/articles/ai-ux-research/ — Documents the "realism gap" in AI-simulated user research and the conditions under which AI augmentation is and is not appropriate. Basis for simulation trap and AI-moderated testing guardrails.

4. **Zheng, L. et al. (2023)**. *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*. arXiv:2306.05685. https://arxiv.org/abs/2306.05685 — Establishes LLM-as-judge as a legitimate evaluation technique while documenting known biases (position, verbosity, self-enhancement). Basis for the circularity nuance in the AI product discovery section.

5. **AICPA (2017, updated)**. *SOC 2 — Service Organization Control Reports*. American Institute of CPAs. https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2 — SOC 2 is an attestation framework for controls at service organizations, not a legal or regulatory regime. Relevant to the compliance taxonomy distinction between regulatory obligations (GDPR, EU AI Act, HIPAA) and assurance frameworks (SOC 2, ISO 27001).
