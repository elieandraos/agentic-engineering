> A portable, evidence-driven engineering methodology for understanding, planning, implementing, reviewing, and shipping software — with an opinionated approach to Laravel engineering where it applies. Not a prompt collection for one repository or framework.

# Engineering philosophy

- **Evidence before conventions.** Skills inspect the real system — code, configuration, tests, and current state — before explaining or changing it. The system establishes what exists; the human decides what it should become.
- **Humans own decisions and approvals.** Material product and architecture choices are settled with a human, and PR approval and merge always stay with a human. No skill merges its own work.
- **Knowledge lives where it belongs.** Portable methodology stays independent of language and framework. Stack knowledge belongs to a stack companion. The consuming project remains authoritative for its domain, conventions, and delivery environment.
- **Proportionate engineering.** A rule earns its place by changing a decision or protecting an invariant, and safeguards stay proportionate to the risks they address.

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

# Engineering capabilities

Complementary capabilities that work alongside the lifecycle or on their own, without becoming lifecycle stages.

* [`pair-it`](skills/pair-it/) — collaborative implementation through human-approved checkpoints, architectural explanations, code walkthroughs, and targeted verification. When combined with `implement-it`, the lifecycle stays with `implement-it`.
* [`audit-it`](skills/audit-it/) — evidence-backed audits of a system's current behavior: data integrity and query performance, security, background-work reliability, and business-rule consistency. It reports verified findings with recommended corrections; it does not implement fixes.
* [`document-it`](skills/document-it/) — evidence-backed technical documentation, from architecture and infrastructure to operations, engineering practices, and costs.
* [`steward-it`](skills/steward-it/) — retrospective investigation of engineering sessions that were unexpectedly slow, difficult, or off course, recommending the smallest justified improvement.

# Opinionated Laravel engineering

[`laravel-inertia-stack`](skills/laravel-inertia-stack/) is our opinionated approach to engineering Laravel, InertiaJS, Vue 3, and Pest applications — conventions, architectural blueprints, testing methodology, and reusable implementation templates, guided by explicit engineering judgment.

It loads alongside Laravel Boost's skills rather than replacing them. It **extends** Boost where Boost is silent, **specializes** Boost's principles into concrete stack shapes, and **deliberately overrides** selected Boost defaults where this stack holds a different position. An established project convention still takes precedence; the skill supplies the defaults where a project has not decided yet. It is a stack companion, not a lifecycle stage: `implement-it` and `review-it` load it when work touches this stack.

# Installation and usage

Install the skills you need, and choose which coding agent(s) should use them:

```shell
npx skills add elieandraos/agentic-engineering
```

The install target selects which agent reads the installed skills, not a set of subagent definitions this repository supplies. Install `laravel-inertia-stack` only in projects on that stack.

**Boring prompts. Serious engineering.**

State the goal, not the choreography. Investigation methods, planning checks, review checklists, and delivery rules already live in versioned, reviewable skills.

```shell
"Investigate how authentication works and prepare the change plan."  # lab-it
"Turn the approved plan into GitHub issues."                         # plan-it
"Implement issue #42."                                               # implement-it + laravel-inertia-stack when relevant
"Implement issue #42 and pair-program with me."                      # implement-it + pair-it
"Review this branch before I open a PR."                             # review-it
"Create the milestone PR."                                           # ship-it
"Audit the billing module for security and data-integrity risks."    # audit-it
"Document how authentication and tenant isolation work."             # document-it
"Steward this session. Tell me where the time, tokens, and workflow friction went."  # steward-it
```

The stages compose into a human workflow, but each prompt also works on its own. Each skill's own README describes its workflow in detail.

* [Roadmap](roadmap.md) · [License](LICENSE)
