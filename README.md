> A portable, evidence-driven engineering methodology for understanding, planning, implementing, reviewing, and shipping software — with an opinionated approach to Laravel engineering where it applies. Not a prompt collection for one repository or framework.

# Principles of agentic engineering

- **Evidence before assumptions.** Agents investigate the actual system before proposing or implementing changes.
- **Human authority.** Agents investigate, execute and verify. Humans own material decisions and approvals.
- **Separation of knowledge.** Engineering methodology, stack conventions and project context remain distinct.
- **Simplicity by design.** Keep solutions and workflows as simple as the problem allows.

# The lifecycle

**Lab → Plan → Implement → Review → Ship**

| Stage | Purpose |
|---|---|
| [`lab-it`](skills/lab-it/) | Investigate the system and establish verified architecture understanding, or produce an approved `plan.md`. |
| [`plan-it`](skills/plan-it/) | Turn approved intent into implementation-ready GitHub issues. |
| [`implement‑it`](skills/implement-it/) | Implement an approved issue using project context and the applicable stack companion. |
| [`review-it`](skills/review-it/) | Independently assure the implementation against scope, architecture, conventions, tests, and regressions. |
| [`ship-it`](skills/ship-it/) | Close the milestone, propose the milestone PR, and handle release once merged. |

- **These skills do not assume a language, framework, or project layout.** The consuming project supplies those; each skill supplies the method.
- **The lifecycle is composable, not mandatory end-to-end.** Use the skills independently or combine them into the workflow your project needs.

# Beyond the delivery lifecycle.

Complementary engineering capabilities that work independently or alongside the delivery lifecycle.

| Skill | Purpose | Focus |
|---|---|---|
| [`pair-it`](skills/pair-it/) | Engineering together | Collaborative implementation, architectural reasoning and guided verification |
| [`audit-it`](skills/audit-it/) | Assessing the system | Security, data integrity, performance and operational reliability |
| [`document-it`](skills/document-it/) | Documenting the system | Creation, maintenance and review of technical documentation grounded in verified system understanding |
| [`steward-it`](skills/steward-it/) | Investigating the engineering process itself | Retrospective investigation of agentic engineering sessions, identifying inefficiencies, recurring problems and evidence-driven improvements |

# Laravel engineering, with a point of view.

[`laravel-inertia-stack`](skills/laravel-inertia-stack/) combines engineering philosophy, code conventions, architectural blueprints and testing practices for Laravel, InertiaJS, Vue 3 and Pest.

| Dimension | Purpose | Focus |
|---|---|---|
| Engineering philosophy | Making sound decisions | Simplicity, practical trade-offs and complexity justified by real needs |
| Code style | Writing maintainable code | Clarity, consistency and expressive use of the framework |
| Architecture | Organizing complexity | Well-defined responsibilities, deliberate boundaries and purposeful abstractions |
| Implementation | Solving practical problems | Framework-native solutions, reusable patterns and proportionate safeguards |
| Testing | Proving behavior | Behavioral correctness, test ownership and meaningful coverage |

It works alongside Laravel Boost — **extends** where Boost is silent, **specializes** where its guidance is general, and **deliberately overrides** where engineering positions differ.

Established project conventions take precedence. The companion provides defaults where no convention exists.

# Ten skills, ten distinct engineering questions

| Skill | Responsibility |
|---|---|
| `lab-it` | What exists, and what should change? |
| `plan-it` | What work should we perform? |
| `implement-it` | How do we execute approved work? |
| `review-it` | Is the implementation correct? |
| `ship-it` | Is the work ready for delivery? |
| `pair-it` | How do we engineer together? |
| `audit-it` | Is the existing system sound? |
| `document-it` | How do we preserve system understanding? |
| `steward-it` | How do we improve the engineering process? |
| `laravel-inertia-stack` | How do we engineer within this particular stack? |

# Boring prompts. Serious engineering.

State the goal, not the choreography. Investigation methods, planning checks, review checklists, and delivery rules already live in versioned, reviewable skills.

```shell
"Investigate how authentication works and prepare the change plan."  # lab-it
"Turn the approved plan into GitHub issues."                         # plan-it
"Implement issue #42."                                               # implement-it + laravel-inertia-stack when relevant
"Implement issue #42 and pair-program with me."                      # implement-it + pair-it
"Pair-program with me on this feature."                              # pair-it
"Review this branch before I open a PR."                             # review-it
"Create the milestone PR."                                           # ship-it
"Audit the billing module for security and data-integrity risks."    # audit-it
"Document how authentication and tenant isolation work."             # document-it
"Steward this session. Tell me where the time, tokens, and workflow friction went."  # steward-it
```

The stages compose into a human workflow, but each prompt also works on its own. Each skill's own README describes its workflow in detail.

# Getting started

Install the skills you need, and choose which coding agent(s) should use them:

```shell
npx skills add elieandraos/agentic-engineering
```

The install target selects which agent reads the installed skills, not a set of subagent definitions this repository supplies. Install `laravel-inertia-stack` only in projects on that stack.

* [Roadmap](roadmap.md) · [Skill-authoring methodology](docs/skill-authoring-methodology.md) · [License](LICENSE)
