# Lab. Plan. Build. Ship — with the right stack.

Understand in the Lab. Plan the work. Build with the Stack. Ship the change.

> A portable, evidence-driven methodology for understanding, planning, building, and shipping software—with stack-specific companions where needed. Not a prompt collection for one repository or framework.

## The pipeline

| Stage | Skill and context | Result |
|---|---|---|
| Understand | [`lab-it`](skills/lab-it/) | Architecture understanding or an approved `plan.md` |
| Plan | [`plan-it`](skills/plan-it/) | Implementation-ready GitHub issues |
| Build | [`ship-it`](skills/ship-it/) + project context + applicable stack companion | Verified implementation |
| Ship | [`ship-it`](skills/ship-it/) | Commits and delivery lifecycle |

These skills do not assume a language, framework, or project layout. The consuming project supplies those; each skill supplies the method.

Use only the stage you need. [`plan-it`](skills/plan-it/) can start from a direct feature request or an approved `plan.md`; [`ship-it`](skills/ship-it/) can start from any approved GitHub issue, whether or not [`plan-it`](skills/plan-it/) created it.

## Boring prompts

**Boring prompts. Serious engineering.**

State the goal, not the choreography. Investigation methods, planning checks, review gates, and delivery rules already live in versioned, reviewable skills.

```shell
"Investigate how authentication works and prepare the change plan."  # lab-it
"Turn the approved plan into GitHub issues."                         # plan-it
"Implement issue #42."                                               # ship-it + stack companion when relevant
```

The stages compose into a human workflow, but each prompt also works on its own.

## Build with the right stack

Stack companions carry technology-specific implementation knowledge without becoming another pipeline stage.

* [`laravel-inertia-stack`](skills/laravel-inertia-stack/) — Laravel, InertiaJS, Vue 3, and Pest. It works alongside relevant Laravel Boost skills.
* A different stack can get its own companion when real use justifies it.

## Install

```shell
npx skills add elieandraos/agentic-engineering
```

Choose the skills and agents you need. Install a stack companion only where it applies.

## Knowledge boundaries

The ecosystem keeps four kinds of knowledge separate:

* **Portable methodology** — [`lab-it`](skills/lab-it/), [`plan-it`](skills/plan-it/), and [`ship-it`](skills/ship-it/); independent of language and framework.
* **Stack knowledge** — implementation conventions for one compatible stack.
* **Project knowledge** — domain rules and repository conventions owned by the consuming project.
* **First-party capabilities** — external skills such as Laravel Boost, composed with rather than copied or renamed.

## Evolution principle

Rules in this ecosystem evolve from demonstrated need and real use, not speculative generalization. See [`roadmap.md`](roadmap.md).
