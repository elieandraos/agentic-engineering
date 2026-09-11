> A portable, evidence-driven methodology for understanding, planning, implementing, reviewing, and shipping software—with stack-specific companions where needed. Not a prompt collection for one repository or framework.

## The pipeline

**Lab → Plan → Implement → Review → Ship**

A human-guided delivery workflow:

| Stage | Purpose |
|---|---|
| [`lab-it`](skills/lab-it/) | Investigate the system and establish verified architecture understanding, or produce an approved `plan.md`. |
| [`plan-it`](skills/plan-it/) | Turn approved intent into implementation-ready GitHub issues. |
| [`implement-it`](skills/implement-it/) | Implement an approved issue using project context and the applicable stack companion. |
| [`review-it`](skills/review-it/) | Independently assure the implementation against scope, architecture, conventions, tests, and regressions. |
| [`ship-it`](skills/ship-it/) | Close the milestone, propose the milestone PR, and handle release once merged. |

These skills do not assume a language, framework, or project layout. The consuming project supplies those; each skill supplies the method.

**PR approval and merge always stay with a human.** No skill in this pipeline merges its own work.

The pipeline is composable, not mandatory end-to-end. Use only the stage you need. [`plan-it`](skills/plan-it/) can start from a direct feature request or an approved `plan.md`; [`implement-it`](skills/implement-it/) can start from any approved GitHub issue and invokes [`review-it`](skills/review-it/) before its implementation gate; `review-it` can also be used independently on an existing worktree, branch, or PR.

## Stack companions

Stack companions carry technology-specific implementation knowledge without becoming another pipeline stage.

* [`laravel-inertia-stack`](skills/laravel-inertia-stack/) — Laravel, InertiaJS, Vue 3, and Pest. It works alongside relevant Laravel Boost skills.
* A different stack can get its own companion when real use justifies it.

## Tools

Independent capabilities that support the workflow without becoming lifecycle stages.

* [`document-it`](skills/document-it/) — creates, updates, and reviews durable engineering documentation in the supported output format(s).
* [`steward-it`](skills/steward-it/) — retrospectively investigates real engineering sessions when something was unexpectedly slow, difficult, wasteful, repeatedly off course, or exposed a recurring workflow problem. It reconstructs timing, human waits, skill/rule usage, token and cache telemetry, verification, outcomes, and recurrence evidence, then recommends the smallest justified improvement.

## Installation and Usage

Install the skills you need, and choose which coding agent(s) should use them:

```shell
npx skills add elieandraos/agentic-engineering
```

The install target selects which agent reads the installed skills, not a set of subagent definitions this repository supplies. Stack companions are installed only where they apply.

**Boring prompts. Serious engineering.**

State the goal, not the choreography. Investigation methods, planning checks, review checklists, and delivery rules already live in versioned, reviewable skills.

```shell
"Investigate how authentication works and prepare the change plan."  # lab-it
"Document the billing architecture."                                 # document-it
"Turn the approved plan into GitHub issues."                         # plan-it
"Implement issue #42."                                               # implement-it + stack companion when relevant
"Review this branch before I open a PR."                             # review-it
"Create the milestone PR."                                           # ship-it
"Steward this session. Tell me where the time, tokens, and workflow friction went."  # steward-it
```

The stages compose into a human workflow, but each prompt also works on its own.

* [Roadmap](roadmap.md) · [License](LICENSE)