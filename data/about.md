# Discovery Karaoke Prevention Engine

by Amodiovalerio Verde (The Thinking Lens) — the-thinking-lens.com

---

## What Is Discovery Karaoke?

Discovery Karaoke = defaulting to the same familiar discovery methods out of habit rather than deliberately matching methods to your actual risk and context.

**Default ≠ Deliberate. Familiar ≠ Fit-for-purpose.**

Most product teams over-rely on the same 3–5 methods — interviews, usability tests, surveys, a prototype, maybe a beta. Under time pressure, the familiar becomes the default. But default ≠ deliberate. Method mismatch leads to waste, delay, and blind spots.

Discovery is a decision engine. Its job is to reduce uncertainty so teams can move faster, with more confidence.

---

## The Framework

Three axes:
- **5 Discovery Risks** — the type of uncertainty your decision needs to reduce
- **3 Discovery Stages** — where you are in the product lifecycle
- **Evidence Thresholds** — how much evidence you need, tied to the size of the bet

### Five Discovery Risks

| Risk | Core Question |
|------|--------------|
| **Value/Desirability** | Will customers buy or use this? |
| **Usability** | Can users figure it out? |
| **Feasibility** | Can we build it? |
| **Viability** | Does it work for the business? |
| **Compliance & Ethics** | Are we allowed to build it? Should we? |

The 5th risk extends Marty Cagan's original four. First proposed in the original article (June 2025). Validated by EU AI Act enforcement (February 2026) and increased compliance-related launch blocks. In regulated and enterprise contexts, this risk comes first.

### Three Discovery Stages

| Stage | Purpose | Space |
|-------|---------|-------|
| **Explore** | Understand the problem, discover opportunities | Problem Space |
| **Validate** | Test solutions, reduce uncertainty | Solution Space |
| **Optimize** | Improve and measure what's live | Both |

### Evidence Thresholds (Blast Radius)

Tie the evidence bar to the size of the bet:
- **Small bet** (feature tweak): 1 method, moderate evidence
- **Medium bet** (new feature): 2 methods, converging evidence
- **Large bet** (new product/pivot): 3+ methods, strong converging evidence

---

## The Toolkit

**80 Discovery Methods** (M1–M96, 80 Active, 3 Superseded):

Evidence-generating activities. Each entry includes: Risk, Stage, Business Model Fit, User Access Required, Time, Cost Level, Evidence Strength, When to Use, When NOT to Use, Karaoke Check, AI Augmentation.

| Category | Count | Examples |
|----------|-------|---------|
| Generative | 15 | User Interviews (M1), JTBD Interviews (M2), Contextual Inquiry (M3), Diary Studies (M5), Continuous Interviewing (M60) |
| Evaluative | 19 | Usability Testing (M16/M17), Card Sorting (M13), Conjoint Analysis (M69), Usability Benchmarking (M73) |
| Experimentation | 14 | Fake Door Test (M23), Landing Page Test (M24), Concierge MVP (M26), Beta Testing (M72) |
| Analytics | 5 | Cohort Analysis (M55), Funnel Analysis (M56), Session Recordings (M58), Heatmaps (M59) |
| Compliance & Ethics | 10 | Data-flow Mapping (M75), DPIA/PIA (M76), AI Red Teaming (M81), Fairness Assessment (M80) |
| AI Feasibility | 3 | Capability Contract Workshop (M89), AI Capability Assessment (M90), Data Readiness Assessment (M91) |

**11 Context Tools** (M-coded frameworks and synthesis tools):

Context tools structure thinking — they are companions to discovery methods, not standalone activities. They do not generate independent user evidence.

| M-code | Tool |
|--------|------|
| M32 | Assumption Mapping |
| M33 | Opportunity Solution Trees (OST) |
| M35 | Customer Journey Mapping |
| M36 | Service Blueprinting |
| M37 | Empathy Mapping |
| M38 | Persona Development |
| M39 | Value Proposition Canvas |
| M42 | Continuous Interviewing |
| M64 | Pre-mortem (Prospective Hindsight) |
| M88 | JTBD Framework (Forces of Progress) |
| M89 | Capability Contract Workshop |

**AI Feasibility Sequence** (M89 → M91 → M90):

For any product built on AI/LLM capabilities — run in this order:
1. M89 Capability Contract Workshop — define what the system is allowed and required to do
2. M91 Data Readiness Assessment — validate data availability, permissions, and quality
3. M90 AI Capability Assessment — test whether the model meets the performance threshold

Skipping M89 means M90 tests the wrong thing. Skipping M91 means M90 runs on unverified data.

**11 Anti-Patterns**: Discovery Karaoke symptoms with diagnostic scorecard and recovery actions.

**11 Guardrails**: Rules that protect the intellectual integrity of every recommendation.

---

## Guardrails

| # | Guardrail | Rule |
|---|-----------|------|
| G1 | Source Integrity | Framework source in `about`, not on every output |
| G2 | Risk-Method Integrity | Methods recommended only with a named risk |
| G3 | Evidence = Blast Radius | More evidence required for bigger bets |
| G4 | Compliance First-Class | Auto-elevated for regulated industries, AI features, and data-sensitive products |
| G5 | AI ≠ Real Users | AI accelerates discovery; it never replaces real user signal |
| G6 | Anti-Pattern Check | Every recommendation includes a karaoke symptom check |
| G7 | Config Safety | Stores only constraints; never risk, stage, or recommendations |
| G8 | Data Integrity | Never modifies its own knowledge base |
| G9 | Graceful Degradation | Unknown commands get help, not errors |
| G10 | Minimum Sufficient Methods | 1–2 methods primary; never 3+ simultaneously |
| G11 | Guided Disclosure | No-arg commands surface options, never dump everything |

---

## Credits

**Framework**: Amodiovalerio Verde — "Stop Doing Discovery Karaoke", The Thinking Lens (June 4, 2025)
https://www.the-thinking-lens.com/stop-doing-discovery-karaoke/

**Methods** sourced from established product discovery literature:
Teresa Torres, Marty Cagan, Jake Knapp, Jeff Gothelf, Erika Hall, Carolyn Snyder, Eric Ries, and others.

**Web app**: https://vverde.github.io/discovery-karaoke-engine/

---

Type `/discovery-karaoke help` to see all commands.
