# Risk-Method Matrix

<!--
version: 2.1
last_updated: 2026-04-12
status: Production

changelog:
  2.1 (2026-04-12): Context Tools Index corrected. M31 (Design Sprint) removed — has no Context
    Tool Note in DB; it is a method. M42 (Competitive Analysis) and M89 (Capability Contract
    Workshop) added — both have Context Tool Note in DB. Index now lists 11 tools, matching DB.
  2.0 (2026-04-12): Full rewrite. All expanded section cells trimmed to 2–3 methods (was 6–17).
    All T-codes replaced with M-codes throughout. M43 (deprecated) and phantom
    "Synthetic User Research (AI)" row removed. M92–M96 added to Complete Method Index.
    Thinking Tools Pairing tables (5 scattered tables) and Decision Tree removed — redundant
    given other navigation. Thinking Tools Index renamed to Context Tools Index; active
    methods only (M31, M32, M33, M35, M36, M37, M38, M39, M64, M88). Method count note
    removed; discovery-methods-full.md is authoritative.
  1.3 (2026-04-10/11): Compliance Explore corrected; B2B/B2C context flags added to top matrix.
    Matrix refs updated after T42 rename.
  1.2 (2026-04-10): T42 renamed from T-NEW; matrix references updated.
  1.1 (2026-04-09): Visual 5×3 grid header added. Top 2 methods per cell for fast scanning.
    Full lists, constraint filters, and pairings retained in expanded sections.
  1.0 (2026-04-09): Initial version. 52-method matrix with T-codes. Thinking Tools Pairing
    tables + Decision Tree included. Cells with 6–17 methods each.
-->

> Quick-reference: **Risk × Stage → Top Methods**. Pick your risk, find your stage, start there.

---

## The Matrix

| Risk | **Explore** | **Validate** | **Optimize** |
|---|---------|--------------|--------------|
| **Value / Desirability** | M1 User Interviews | M23 Fake Door Test | M20 A/B Testing |
| *Will they want this?* | M2 JTBD Interviews | M48 Pre-sales / LOI `B2B` | M55 Cohort Analysis |
| **Usability** | M3 Contextual Inquiry `B2B` | M16 Usability Testing (Mod) | M58 Session Recordings |
| *Can they use it?* | M66 Shadowing `B2B` | M18 Heuristic Review | M59 Heatmap Analysis |
| **Feasibility** | M9 Stakeholder Interviews | M44 Spike Solution | M68 Dogfooding |
| *Can we build it?* | M89 Capability Contract `AI` | M45 Proof of Concept | M72 Beta Testing |
| **Viability** | M8 Sales Call Analysis `B2B` | M48 Pre-sales / LOI `B2B` | M56 Funnel Analysis |
| *Does it work for the business?* | M42 Competitive Analysis | M24 Landing Page Test `B2C` | M57 Feature Audit |
| **Compliance & Ethics** | M75 Data-flow Mapping | M19 Accessibility Audit | M82 Post-market Monitoring |
| *First-class risk* | M76 DPIA / PIA | M81 AI Red Teaming | M57 Feature Audit *(compliance)* |

---

## 1. Value/Desirability Risk

*"Will customers want this? Will they buy/use it?"*

| Stage | Methods | Evidence Range |
|-------|---------|----------------|
| **Explore** | M1 (User Interviews), M2 (JTBD Interviews), M8 (Sales Call Analysis) | Weak–Strong |
| **Validate** | M23 (Fake Door Test), M47 (Concept Testing), M48 (Pre-sales/LOI) | Moderate–Strong |
| **Optimize** | M20 (A/B Testing), M55 (Cohort Analysis), M56 (Funnel Analysis) | Moderate–Strong |

### Quick Picks by Constraint

**Urgent + Low budget** (days, minimal spend):
- Explore: M7 (Forum Analysis), M6 (Support Ticket Analysis)
- Validate: M23 (Fake Door Test), M54 (Preference Testing), M15 (Five-Second Test)
- Optimize: M56 (Funnel Analysis), M57 (Feature Audit)

**No user access** (what works without talking to users):
- Explore: M7 (Forum Analysis), M6 (Support Ticket Analysis), M8 (Sales Call Analysis), M42 (Competitive Analysis)
- Validate: M23 (Fake Door Test) [existing traffic only]
- Optimize: M55 (Cohort Analysis), M56 (Funnel Analysis), M57 (Feature Audit)

**B2B specific**:
- Explore: M8 (Sales Call Analysis), M9 (Stakeholder Interviews), M3 (Contextual Inquiry), M66 (Shadowing)
- Validate: M48 (Pre-sales/LOI), M67 (Sales-Led Prototype Testing), M26 (Concierge MVP)
- Optimize: M55 (Cohort Analysis), M20 (A/B Testing)

**Pre-launch** (no existing product/users):
- Explore: M1 (User Interviews), M2 (JTBD Interviews), M7 (Forum Analysis), M42 (Competitive Analysis)
- Validate: M24 (Landing Page Test), M47 (Concept Testing), M26 (Concierge MVP), M48 (Pre-sales/LOI), M49 (Crowdfunding)

---

## 2. Usability Risk

*"Can users figure out how to use it?"*

| Stage | Methods | Evidence Range |
|-------|---------|----------------|
| **Explore** | M3 (Contextual Inquiry), M66 (Shadowing) | Moderate–Strong |
| **Validate** | M16 (Usability Testing — Moderated), M17 (Usability Testing — Unmoderated), M18 (Expert/Heuristic Review) | Weak–Strong |
| **Optimize** | M58 (Session Recording Analysis), M59 (Heatmap Analysis), M20 (A/B Testing) | Moderate–Strong |

### Quick Picks by Constraint

**Urgent + Low budget** (days, minimal spend):
- Explore: (Usability explore is inherently time-intensive — skip to Validate with M18 or M71)
- Validate: M18 (Expert/Heuristic Review), M71 (Cognitive Walkthrough), M15 (Five-Second Test), M70 (First-Click Testing), M28 (Paper Prototyping)
- Optimize: M59 (Heatmap Analysis), M58 (Session Recording Analysis)

**No user access** (what works without talking to users):
- Validate: M18 (Expert/Heuristic Review), M71 (Cognitive Walkthrough), M19 (Accessibility Audit — expert-based), M68 (Dogfooding)
- Optimize: M58 (Session Recording Analysis), M59 (Heatmap Analysis), M68 (Dogfooding)

**B2B specific**:
- Explore: M3 (Contextual Inquiry), M66 (Shadowing)
- Validate: M16 (Usability Testing — Moderated), M68 (Dogfooding), M72 (Beta Testing)
- Optimize: M58 (Session Recording Analysis), M20 (A/B Testing)

**Pre-launch** (no existing product/users):
- Validate: M28 (Paper Prototyping), M29 (Digital Prototyping), M18 (Expert/Heuristic Review), M71 (Cognitive Walkthrough), M13 (Card Sorting), M14 (Tree Testing), M16 (Usability Testing — Moderated with prototype)

---

## 3. Feasibility Risk

*"Can we actually build this? At what cost?"*

| Stage | Methods | Evidence Range |
|-------|---------|----------------|
| **Explore** | M9 (Stakeholder Interviews), M89 (Capability Contract Workshop) `AI`, M91 (Data Readiness Assessment) `AI` | Moderate / N/A |
| **Validate** | M44 (Spike Solution), M45 (Proof of Concept), M26 (Concierge MVP) | Moderate–Strong |
| **Optimize** | M68 (Dogfooding), M72 (Beta Testing) | Moderate–Strong |

Note: Feasibility has fewer methods because it is primarily an engineering risk. Explore surfaces the question; Validate answers it with code. Optimize is about reliability at scale.

**AI Feasibility addendum**: For products built on AI/LLM capabilities, run M89 (Capability Contract Workshop) first to define what the system is allowed and required to do, then M91 (Data Readiness Assessment) to validate data availability and permissions, then M90 (AI Capability Assessment) to test whether the model meets the performance threshold. M89 is a context tool (Evidence Strength: N/A); M90 and M91 generate Moderate evidence.

### Quick Picks by Constraint

**Urgent + Low budget** (days, minimal spend):
- Explore: M42 (Competitive Analysis — what have others built?), M89 (Capability Contract Workshop — team time only, AI products)
- Validate: M44 (Spike Solution — hours to days, time only)

**No user access** (all Feasibility methods work without users):
- Validate: M44 (Spike Solution), M45 (Proof of Concept)
- Optimize: M68 (Dogfooding)

**B2B specific**:
- Explore: M9 (Stakeholder Interviews — surface integration constraints), M89 (Capability Contract Workshop — scope enterprise AI constraints)
- Validate: M45 (Proof of Concept — B2B buyers often need to see it work)

**Pre-launch** (no existing product/users):
- Validate: M44 (Spike Solution), M45 (Proof of Concept), M26 (Concierge MVP — test if humans can deliver the service before automating)

**AI products specifically**:
- Explore: M89 (Capability Contract Workshop) → M91 (Data Readiness Assessment) → M90 (AI Capability Assessment)
- Run in this sequence: scope first (M89), then validate data (M91), then test model capability (M90)

---

## 4. Viability Risk

*"Does this work for the business? Is it sustainable?"*

| Stage | Methods | Evidence Range |
|-------|---------|----------------|
| **Explore** | M8 (Sales Call Analysis), M9 (Stakeholder Interviews), M42 (Competitive Analysis) | Weak–Moderate |
| **Validate** | M48 (Pre-sales/LOI), M24 (Landing Page Test), M67 (Sales-Led Prototype Testing) | Moderate–Strong |
| **Optimize** | M55 (Cohort Analysis), M56 (Funnel Analysis), M20 (A/B Testing — pricing) | Moderate–Strong |

### Quick Picks by Constraint

**Urgent + Low budget** (days, minimal spend):
- Explore: M42 (Competitive Analysis), M8 (Sales Call Analysis)
- Validate: M23 (Fake Door Test), M24 (Landing Page Test)
- Optimize: M56 (Funnel Analysis), M57 (Feature Audit)

**No user access** (what works without talking to users):
- Explore: M42 (Competitive Analysis), M8 (Sales Call Analysis — existing recordings), M9 (Stakeholder Interviews — internal)
- Optimize: M55 (Cohort Analysis), M56 (Funnel Analysis), M57 (Feature Audit)

**B2B specific**:
- Explore: M8 (Sales Call Analysis), M9 (Stakeholder Interviews)
- Validate: M48 (Pre-sales/LOI), M67 (Sales-Led Prototype Testing), M69 (Conjoint Analysis)
- Optimize: M55 (Cohort Analysis), M20 (A/B Testing — pricing)

**Pre-launch** (no existing product/users):
- Explore: M42 (Competitive Analysis)
- Validate: M24 (Landing Page Test), M48 (Pre-sales/LOI), M49 (Crowdfunding), M47 (Concept Testing — for value + viability)

---

## 5. Compliance & Ethics Risk

*"Is this legal, ethical, and responsible? FIRST-CLASS RISK — not an afterthought."*

**Ethics beyond compliance**: Compliance checks whether you meet legal requirements. Ethics asks whether you *should* build this, even if you legally *can*. Add these questions to your discovery process:
- Who could be harmed by this product, even if they're not our target users?
- What happens if this feature works exactly as designed but at 100× scale?
- Are we testing with populations that represent the people most affected?
- Would we be comfortable if our discovery process and decisions were public?

**Pre-mortem prompt**: When running M64 (Pre-mortem) for regulated or sensitive products, add the specific failure mode: *"We launched, and it caused real harm to a vulnerable population. What happened?"*

| Stage | Methods | Evidence Range |
|-------|---------|----------------|
| **Explore** | M75 (Data-flow Mapping), M76 (DPIA/PIA), M9 (Stakeholder Interviews — legal/compliance) | Moderate–Strong |
| **Validate** | M19 (Accessibility Audit), M81 (AI Red Teaming), M80 (Fairness & Bias Assessment) | Moderate–Strong |
| **Optimize** | M82 (Post-market Compliance Monitoring), M57 (Feature Audit — compliance check), M80 (Fairness & Bias Assessment) | Moderate–Strong |

### Quick Picks by Constraint

**Urgent + Low budget** (days, minimal spend):
- Explore: M9 (Stakeholder Interviews — legal team), M84 (LIA — hours to days), M75 (Data-flow Mapping — team time only)
- Validate: M18 (Expert/Heuristic Review — compliance focus), M19 (Accessibility Audit — expert-based)
- Optimize: M57 (Feature Audit — compliance check), M82 (Post-market Monitoring)

**No user access** (all core Compliance methods work internally):
- Explore: M9 (Stakeholder Interviews), M75 (Data-flow Mapping), M76 (DPIA), M84 (LIA)
- Validate: M77 (Privacy Threat Modeling), M18 (Expert/Heuristic Review), M19 (Accessibility Audit — expert-based), M80 (Fairness Assessment — existing data), M81 (AI Red Teaming — no users needed)
- Optimize: M82 (Post-market Monitoring), M57 (Feature Audit)

**B2B specific**:
- Explore: M9 (Stakeholder Interviews — legal, procurement, security teams), M75 (Data-flow Mapping), M76 (DPIA)
- Validate: M19 (Accessibility Audit — VPAT requirements), M72 (Beta Testing — controlled pilot), M79 (Notice Comprehension Testing)
- Optimize: M82 (Post-market Monitoring)

**Pre-launch** (no existing product/users):
- Explore: M9 (Stakeholder Interviews — regulatory landscape), M75 (Data-flow Mapping), M76 (DPIA), M83 (FRIA — for AI products), M84 (LIA)
- Validate: M19 (Accessibility Audit), M18 (Expert/Heuristic Review), M77 (Privacy Threat Modeling), M79 (Notice Comprehension Testing)

---

## Evidence Threshold by Blast Radius

| Blast Radius | Methods Needed | Evidence Bar | Example |
|--------------|---------------|-------------|---------|
| **Small bet** (feature tweak, UI change) | 1 method | Moderate signal | M57 shows low usage → M20 to test a fix |
| **Medium bet** (new feature, workflow change) | 2 methods, converging evidence | Consistent signal across methods | M1 + M23 both confirm demand |
| **Large bet** (new product, pivot, major investment) | 3+ methods, strong converging evidence | Strong signal across methods, multiple risk types covered | M2 + M26 + M48 all validate demand and willingness to pay |

### Blast Radius Decision Aid

- **Small bet**: Pick the fastest, cheapest method that addresses your risk. Move on.
- **Medium bet**: Use one generative + one behavioral method. If they converge, proceed. If they diverge, add a third.
- **Large bet**: Cover at least 2 risk types (e.g., Value + Viability). Require behavioral evidence (not just stated preference). Run M64 (Pre-mortem) before committing.

---

## When Evidence Conflicts: The Divergent Signal Protocol

When two methods give contradictory results (e.g., interviews say users want X, but a fake door test shows no demand), don't average them — diagnose why they diverge.

### Step 1: Classify the Divergence

| Type | Example | Likely Cause |
|------|---------|-------------|
| **Say vs. Do** | Interviews positive, behavioral test negative | Users state aspirations, not behavior. Trust the behavioral signal. |
| **Small sample vs. large sample** | 5 interviews say yes, 500 survey responses say no | Small samples find patterns; large samples find prevalence. The pattern may be real but rare. |
| **Problem vs. solution** | Users confirm the problem, but reject your solution | The problem is real. Your solution isn't the right one. Explore alternative solutions. |
| **Segment divergence** | Power users love it, new users are confused | You have two audiences with different needs. Segment your analysis. |
| **Time horizon** | Short-term test positive, longitudinal data negative | Novelty effect. Require sustained usage data before committing. |

### Step 2: Apply the Tiebreaker Hierarchy

When you must decide and signals conflict:

1. **Behavioral evidence beats stated preference** — what people do outweighs what they say
2. **Larger sample beats smaller sample** — unless the small sample reveals a pattern the large sample can't detect
3. **Real-stakes evidence beats hypothetical** — pre-orders beat survey intent; usage beats concept test approval
4. **Converging weak signals beat one strong signal** — three moderate signals pointing the same way are more reliable than one strong outlier
5. **When nothing resolves it** — run one more method specifically designed to break the tie (e.g., M26 Concierge MVP combines behavioral + qualitative signal), or accept the uncertainty and make a reversible bet

### Step 3: Document, Don't Suppress

Record the divergent findings and your resolution rationale. Teams that bury conflicting evidence repeat the same mistakes. Add a "Divergent Signals" section to your research repository.

---

## Multi-Risk Combinations

Common risk pairings and recommended method sequences.

### Value + Usability (Most Common)

| Stage | Sequence |
|-------|----------|
| Explore | M1 (User Interviews) → M35 (Customer Journey Mapping) |
| Validate | M29 (Digital Prototype) + M16 (Usability Testing) → M23 (Fake Door Test) |
| Optimize | M20 (A/B Testing) + M58 (Session Recordings) + M12 (NPS/CSAT) |

### Value + Viability (New Product/Bet)

| Stage | Sequence |
|-------|----------|
| Explore | M2 (JTBD Interviews) → M32 (Assumption Mapping) → M9 (Stakeholder Interviews — market/business) |
| Validate | M24 (Landing Page Test) → M26 (Concierge MVP) → M48 (Pre-sales/LOI) |
| Optimize | M55 (Cohort Analysis) → M56 (Funnel Analysis) → M20 (A/B Testing — pricing) |

### Value + Feasibility (Technical Innovation)

| Stage | Sequence |
|-------|----------|
| Explore | M1 (User Interviews) → M44 (Spike Solution) → M42 (Competitive Analysis) |
| Validate | M27 (Wizard of Oz) → M45 (Proof of Concept) → M47 (Concept Testing) |
| Optimize | M57 (Feature Audit) → M20 (A/B Testing) |

### Value + Compliance (Regulated Industry)

| Stage | Sequence |
|-------|----------|
| Explore | M9 (Stakeholder Interviews — legal) → M1 (User Interviews) → M7 (Forum Analysis) |
| Validate | M18 (Expert Review — compliance) → M26 (Concierge MVP — controlled) → M19 (Accessibility Audit) |
| Optimize | M57 (Feature Audit — compliance) → M12 (NPS/CSAT) → M58 (Session Recordings) |

### Usability + Feasibility (Complex Technical UX)

| Stage | Sequence |
|-------|----------|
| Explore | M3 (Contextual Inquiry) → M32 (Assumption Mapping) |
| Validate | M44 (Spike Solution) + M29 (Digital Prototype) → M16 (Usability Testing) |
| Optimize | M68 (Dogfooding) → M58 (Session Recordings) → M20 (A/B Testing) |

---

## Complete Method Index

> Primary evidence-generating methods. Context tools are listed separately in the Context Tools Index below.

**Risk codes**: V = Value/Desirability · U = Usability · F = Feasibility · Vi = Viability · C = Compliance & Ethics

| ID | Method | Risk | Stage | Time | Cost | User Access |
|----|--------|------|-------|------|------|-------------|
| M1 | User Interviews (Problem Discovery) | V | Explore | 1–2w | Low | Moderate |
| M2 | JTBD Interviews | V | Explore | 2–4w | Low–Med | Moderate |
| M3 | Contextual Inquiry | V, U | Explore | 2–4w | Med | High |
| M4 | Ethnographic Research | V | Explore | 4+w | High | High |
| M5 | Diary Studies | V, U | Explore | 2–4w | Med | Moderate |
| M6 | Support Ticket Analysis | V, U | Explore, Opt | Days | Time only | None |
| M7 | Forum/Community Analysis | V | Explore | Days | Time only | None |
| M8 | Sales Call Analysis | V, Vi | Explore, Val | Days | Time only | None |
| M9 | Stakeholder Interviews | Vi, F, C | Explore | 1–2w | Time only | None |
| M10 | Focus Groups | V | Explore | 1–2w | Med | Mod–High |
| M11 | Surveys (Problem Validation) | V | Validate | 1–2w | Low | Moderate |
| M12 | Surveys (NPS/CSAT/CES) | V, U, Vi | Optimize | Ongoing | Low | Low |
| M13 | Card Sorting | U | Validate | 1–2w | Low | Moderate |
| M14 | Tree Testing | U | Validate | Days–1–2w | Low | Moderate |
| M15 | Five-Second Test | U, V | Validate | Hours–Days | Low | Low–Mod |
| M16 | Usability Testing (Moderated) | U, V | Validate | 1–2w | Med | Mod–High |
| M17 | Usability Testing (Unmoderated) | U | Validate | Days | Low–Med | Moderate |
| M18 | Expert/Heuristic Review | U | Validate | Hours–Days | Time only | None |
| M19 | Accessibility Audit | C, U | Validate | 1–2w | Low–Med | None–Mod |
| M20 | A/B Testing | V, U | Optimize | 1–2w | Med | Low |
| M21 | Multivariate Testing | V, U, Vi | Optimize | 2–4w | Med–High | Low |
| M22 | Switchback Testing | V, Vi | Optimize | 2–4w | Med | Low |
| M23 | Fake Door Test | V | Validate | Days | Low | Low |
| M24 | Landing Page Test | V, Vi | Validate | Days–1–2w | Low–Med | Moderate |
| M26 | Concierge MVP | V, F, Vi | Validate | 2–4w | Med | Moderate |
| M27 | Wizard of Oz | V, U | Validate | 1–2w | Med | Moderate |
| M28 | Paper Prototyping | U | Validate | Hours–Days | Time only | Moderate |
| M29 | Digital Prototyping | U, V | Validate | Days–1–2w | Low–Med | Moderate |
| M42 | Competitive Analysis | Vi, V | Explore | Days–1–2w | Low | None |
| M44 | Spike Solution | F | Validate | Hours–Days | Time only | None |
| M45 | Proof of Concept (PoC) | F | Validate | 1–2w | Med | None–Low |
| M47 | Concept Testing | V | Validate | Days–1–2w | Low | Moderate |
| M48 | Pre-sales / LOI | V, Vi | Validate | 2–4w | Low | Moderate |
| M49 | Crowdfunding Validation | V, Vi | Validate | 4+w | Med–High | Moderate |
| M53 | Kano Model Analysis | V | Validate | 1–2w | Low | Moderate |
| M54 | Preference Testing | V, U | Validate | Hours–Days | Low | Low–Mod |
| M55 | Cohort Analysis | V, Vi | Optimize | Days–1–2w | Low | None |
| M56 | Funnel Analysis | V, U, Vi | Optimize | Days | Low | None |
| M57 | Feature Audit / Usage Analytics | V, Vi | Optimize | Days–1–2w | Low | None |
| M58 | Session Recording Analysis | U | Optimize | Days | Low | None |
| M59 | Heatmap Analysis | U | Optimize | Days | Low | None |
| M60 | Continuous Interviewing | V | Explore, Val, Opt | Ongoing | Low | Moderate |
| M65 | Experience Sampling Method (ESM) | V, U | Explore | 2–4w | Med | Moderate |
| M66 | Shadowing (Passive Observation) | V, U | Explore | 1–2w | Med | High |
| M67 | Sales-Led Prototype Testing | V, Vi | Validate | 2–4w | Med | Moderate |
| M68 | Dogfooding | V, U, F | Val, Opt | Ongoing | Time only | None |
| M69 | Conjoint Analysis | V, Vi | Validate | 2–4w | Med–High | Moderate |
| M70 | First-Click Testing | U | Validate | Hours–Days | Low | Low–Mod |
| M71 | Cognitive Walkthrough | U | Validate | Hours–Days | Time only | None |
| M72 | Beta Testing / Controlled Pilot | V, U, F, Vi | Val, Opt | 2–4w | Med | Mod–High |
| M73 | Usability Benchmarking (SUS/UMUX-Lite) | U | Val, Opt | Days | Low | Moderate |
| M74 | In-Product Intercept Research | V, U | Val, Opt | Days–1–2w | Low | Moderate |
| M75 | Data-flow Mapping | C | Explore | Days–1–2w | Time only | None |
| M76 | Data Protection Impact Assessment (DPIA/PIA) | C | Explore | 1–2w | Low–Med | None |
| M77 | Privacy Threat Modeling (LINDDUN) | C | Explore, Val | Days–1–2w | Time only | None |
| M78 | Participatory Engagement with Affected Communities | C | Explore, Val | 2–4w | Low–Med | High |
| M79 | Transparency & Notice Comprehension Testing | C | Validate | Days–1–2w | Low | Moderate |
| M80 | Fairness and Bias Assessment | C | Val, Opt | 1–2w | Low–Med | Low |
| M81 | AI Red Teaming / Adversarial Testing | C | Val, Opt | 1–2w | Low–Med | None |
| M82 | Post-market Compliance Monitoring | C | Optimize | Ongoing | Low–Med | Low |
| M83 | Fundamental Rights Impact Assessment (FRIA) | C | Explore, Val | 1–2w | Low–Med | None |
| M84 | Legitimate Interests Assessment (LIA) | C | Explore | Hours–Days | Time only | None |
| M89 | Capability Contract Workshop `AI` | F, C | Explore | Days–1w | Low | None |
| M90 | AI Capability Assessment `AI` | F | Explore, Val | 1–2w | Low–Med | None |
| M91 | Data Readiness Assessment `AI` | F, C | Explore | 1–2w | Low | None |
| M92 | Churn and Lost Customer Interviews | V, Vi | Explore, Val | 1–2w | Low | Moderate |
| M93 | Pricing and Willingness-to-Pay Testing | V, Vi | Validate | 1–2w | Low–Med | Moderate |
| M94 | Search and Query Log Analysis | V, U | Explore, Opt | Days | Time only | None |
| M95 | Win/Loss Interviews | Vi, V | Explore, Val | 1–2w | Low | Moderate |
| M96 | Comparative Usability Testing | U | Validate | 1–2w | Med | Moderate |

---

## Context Tools Index

> Context tools are frameworks, synthesis tools, and operating practices that structure discovery thinking — they do not generate independent user evidence but are used alongside evidence-generating methods.

| M-code | Tool | Type | Primary Pairing |
|--------|------|------|----------------|
| M32 | Assumption Mapping | Framework | All — start of any discovery cycle |
| M33 | Opportunity Solution Trees (OST) | Framework | V, Vi — connect experiments to outcomes |
| M35 | Customer Journey Mapping | Synthesis | V, U — end-to-end experience synthesis |
| M36 | Service Blueprinting | Synthesis | C, Vi — map front/backstage + compliance touchpoints |
| M37 | Empathy Mapping | Synthesis | V — quick interview synthesis |
| M38 | Persona Development | Synthesis | V, U — behaviour-based segmentation |
| M39 | Value Proposition Canvas | Framework | V, Vi — articulate fit before testing |
| M42 | Competitive Analysis | Strategic Framing | V, Vi — calibrate landscape before demand validation |
| M64 | Pre-mortem (Prospective Hindsight) | Framework | All — surface hidden risks before large bets |
| M88 | JTBD Framework (Forces of Progress) | Framework | V — context tool for JTBD interview design |
| M89 | Capability Contract Workshop | Framework | F, C — AI products; scope before building |
