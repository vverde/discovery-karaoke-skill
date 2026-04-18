# CMD: help

**Trigger**: No argument, `help`, or unrecognized single word.

**Two modes**:

**Mode 1 — No-args or `help` alone (orientation first):**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DISCOVERY KARAOKE Prevention Engine
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Discovery Karaoke = defaulting to the same familiar discovery methods
out of habit rather than deliberately matching methods to your actual
risk and context. Default ≠ Deliberate. Familiar ≠ Fit-for-purpose.

This skill helps product teams match the RIGHT method to their situation.
The framework: Risk → Stage → Method → Evidence.

Not sure where to start?
  Describe your situation:   /discovery-karaoke assess [situation]
  See the method matrix:     /discovery-karaoke matrix
  Learn the framework:       /discovery-karaoke about
  Quick recommendation:      /discovery-karaoke quick [situation]
  Run the diagnostic:        /discovery-karaoke diagnose

Available commands:
  about | assess | quick | ai | list | describe | compare
  matrix | diagnose | review | config

Type /discovery-karaoke help commands for the full reference.
```

**Mode 2 — `help commands` (full reference):**

```
Discovery Karaoke Prevention Engine — Command Reference

  about                      Framework, toolkit, credits, guardrails
  assess [situation]         Full recommendation — context questions → matched methods → plan
  quick [situation]          Fast recommendation — 4 questions → top methods
  ai [situation]             AI product discovery — M89/M91/M90 sequence + guardrails
  list methods [filter]      Browse methods by risk, stage, category, or constraint
  list methods all           Show all 80 active methods
  list tools                 Browse 11 context tools
  describe [M##]             Deep-dive on a specific method or context tool
  compare [M##] vs [M##]     Side-by-side comparison of two methods
  matrix                     Compact 5×3 overview — top methods per cell
  matrix full                Full 5×3 — all methods per cell
  matrix [risk]              Full row — all stages + constraint picks
  matrix [risk] [stage]      Single cell — all methods + constraint picks
  diagnose                   Interactive karaoke diagnostic scorecard
  review [plan]              Review a discovery plan for karaoke symptoms
  config save|show|clear     Save/view/clear team context for faster assessments

Risks:     value | usability | feasibility | viability | compliance
Stages:    explore | validate | optimize
List filters: risk, stage, category (generative/evaluative/experimentation/analytics/compliance),
              constraint (B2B/B2C/startup/enterprise/solo/urgent/no-users)

Examples:
  /discovery-karaoke assess We're considering a self-serve tier for SMBs
  /discovery-karaoke quick Should we add dark mode to the dashboard?
  /discovery-karaoke ai We're building an AI-powered document summarizer
  /discovery-karaoke list methods value B2B
  /discovery-karaoke list methods compliance validate
  /discovery-karaoke describe M23
  /discovery-karaoke compare M1 vs M23
  /discovery-karaoke matrix viability validate
  /discovery-karaoke matrix full
  /discovery-karaoke diagnose
  /discovery-karaoke review We interview users, then prototype, then usability test

Framework: The Thinking Lens — the-thinking-lens.com
Toolkit: 80 methods + 11 context tools | 11 anti-patterns | 11 guardrails
```
