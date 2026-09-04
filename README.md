# Agentic Engineering

**Lab. Plan. Ship. Build with the right stack.**
Understand in the Lab. Plan the work. Build with the Stack. Ship the change.

A portable, evidence-driven methodology for architecting, planning, and delivering software — plus
stack-specific companions that carry technology knowledge without leaking it into that portable
core. Not a prompt collection for one repo or framework.

## The pipeline

| Skill | Owns |
|---|---|
| [`lab-it`](skills/lab-it/) | Investigate how a system actually works → a new or updated architecture guide, or an approved `plan.md` handoff. |
| [`plan-it`](skills/plan-it/) | Turn a feature request or an approved `plan.md` into a reviewed, drafted set of GitHub issues. |
| [`ship-it`](skills/ship-it/) | Move any approved GitHub issue meeting its entry contract through implementation review, commits, verification, and release. |

    lab-it  → approved architecture / plan.md
      → plan-it → GitHub issues
      → ship-it + applicable stack companion → verified change

None of the three assume a particular language, framework, or project layout — a consuming project
supplies its own; each skill supplies the method. They compose into the pipeline above, but none
requires every earlier stage to have actually run: `plan-it` starts equally well from a direct
feature request or from `lab-it`'s approved `plan.md`, and `ship-it` picks up any approved GitHub
issue meeting its entry contract, whether `plan-it` drafted it or not. See each skill's own
`README.md` for the walkthrough and `SKILL.md` for the operational contract.

## Build with the right stack

[`laravel-inertia-stack`](skills/laravel-inertia-stack/) is a companion for **Laravel + InertiaJS +
Vue 3 + Pest** — consulted during `plan-it` and `ship-it`, never a fourth pipeline stage. It owns
implementation knowledge and conventions for that stack; `ship-it` performs the approved
implementation itself, consulting the companion rather than the companion writing the code. It's
additive to Laravel Boost's own skills, never a replacement. A different stack gets its own
companion, built the same way.

## Install

    npx skills add elieandraos/agentic-engineering

Choose the skills and agents you need.

Install only what a project needs — the stack companion is only useful alongside a project that runs
on that stack. See [`docs/skill-consumption.md`](docs/skill-consumption.md) for personal, disposable,
and repository-managed install modes.

## Knowledge boundaries

Four kinds of knowledge stay distinct: **portable methodology** (cross-stack, the three skills
above), **stack companion knowledge** (one stack's implementation delta, e.g.
`laravel-inertia-stack`), **project-specific knowledge** (a consuming project's own domain and repo
conventions — never absorbed here), and **external first-party capabilities** (e.g. Laravel Boost —
composed with, never duplicated or renamed as this ecosystem's own). See
[`docs/skill-authoring-methodology.md`](docs/skill-authoring-methodology.md) for the full model.

## Repository structure

    agentic-engineering/
    ├── README.md     this file
    ├── roadmap.md    living architecture and evolution notes
    ├── docs/         cross-skill methodology (authoring, consumption)
    ├── skills/
    │   ├── lab-it/                 portable — investigation and architecture
    │   ├── plan-it/                portable — scoping and issue drafting
    │   ├── ship-it/                portable — implementation and delivery
    │   └── laravel-inertia-stack/  stack companion — Laravel + InertiaJS + Vue 3 + Pest
    └── artifacts/    maintainer-facing per-skill architecture dossiers

## Evolution principle

Rules in this ecosystem evolve from demonstrated need and real use, not speculative generalization.
See [`roadmap.md`](roadmap.md).
