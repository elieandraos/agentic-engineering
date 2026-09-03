# Agentic Engineering Roadmap

## Purpose

`agentic-engineering` is the home for a growing, portable system of agentic software-engineering methodologies.

The goal is not to collect prompts for one repository or one framework. The goal is to build reusable engineering workflows that can operate across projects and technology stacks, while keeping stack-specific implementation knowledge and project-specific conventions out of the portable core.

This document is the living Agentic Engineering roadmap: it describes the ecosystem's current architecture, the repository organization it has adopted, the working principles that govern how it evolves, and the future directions worth keeping in view. It is not a phase plan, and it does not track a program toward completion — the system continues to change as real use demonstrates a need.

---

## The story so far

The first generation of the system grew inside the `useOrbit` project as local Claude Code skills.

`useOrbit` is a Laravel/Vue/Inertia application. Its engineering workflow developed three mature capabilities:

- `my-feature-planning`
- `my-git-workflow`
- `my-architecture-laboratory`

The skills evolved through real feature work, especially the Auth & 2FA milestone, and were repeatedly refined when real development exposed gaps.

The principle that emerged, and that continues to govern this repository, is:

> Extract rules from evidence, not from imagination.

That principle applies both to the product architecture being documented and to the agentic workflows themselves.

Those three skills have since left `useOrbit`'s working tree and now form the portable core of this external, reusable engineering system — externalized, published, and consumed back into `useOrbit` as canonical upstream source. `useOrbit` remains both the origin of that three-skill family and the system's first real consumer, exercising each skill on genuine work rather than synthetic tests.

Alongside that portable family, [`my-laravel-stack`](skills/my-laravel-stack/) is a separate companion: technology-specific implementation knowledge for the Laravel + InertiaJS + Vue 3 + Pest stack that `useOrbit` runs on, extracted once repeated real-consumer evidence justified it. It is evidence-backed the same way the three portable skills are, but it is a stack companion alongside the portable three-skill family, not a fourth member of it — the portable methodology should never need to know which stack it is operating on.

---

# 1. Current architecture of the ecosystem

The system is a layered model:

```text
                    PORTABLE METHODOLOGIES
                             |
             +---------------+---------------+
             |               |               |
     Feature Planning   Architecture     Git Workflow
                         Laboratory
             |               |               |
             +---------------+---------------+
                             |
                    STACK COMPANION LAYER
                        my-laravel-stack
             (Laravel + InertiaJS + Vue 3 + Pest —
           the verified delta additive to Laravel Boost)
                             |
                    PROJECT-SPECIFIC INPUT
                             |
                 domain decisions / repo rules /
                 deployment conventions / product
```

The important boundaries are:

### Portable methodology

The engineering method itself:

- how to investigate and classify work;
- how to plan features and issues;
- how to reconstruct and lock architecture;
- how to implement, review, commit, release, and complete milestones.

### Stack companion layer

Technology-specific implementation knowledge that is genuinely owned/authored by this ecosystem for the Laravel + InertiaJS + Vue 3 + Pest stack `useOrbit` runs on, implemented as **[`my-laravel-stack`](skills/my-laravel-stack/)** — a portable stack companion carrying the verified delta additive to Laravel Boost (conventions, implementation blueprints, and reusable code templates); see `artifacts/my-laravel-stack.md` for the full record. This layer is distinct from **external first-party capabilities** such as Laravel Boost's `laravel-best-practices` and `testing-best-practices`: upstream dependencies `my-laravel-stack` may compose with, but never owns, absorbs, renames, or duplicates.

### Project-specific input

Things that belong to one product or repository:

- domain model and business decisions;
- repository conventions;
- deployment/environment choices;
- naming dialects;
- existing architecture decisions;
- project-specific release or issue conventions.

The stack-layer boundary is decided and implemented as `my-laravel-stack` (see `artifacts/my-laravel-stack.md` for the full evidence and current assessment). Stacks beyond Laravel/Vue/Inertia are a possible future direction, not committed work.

---

# 2. Repository organization direction

The adopted repository structure groups content into three explicit families: portable methodology
in `docs/`, installable operational skill packages in `skills/`, and maintainer-facing architectural
deep dives in `artifacts/`. Every skill — the three portable skills and `my-laravel-stack` — lives as
its own directory under `skills/`:

```text
agentic-engineering/
├── README.md
├── roadmap.md
├── docs/
├── skills/
│   ├── my-feature-planning/
│   ├── my-git-workflow/
│   ├── my-architecture-laboratory/
│   └── my-laravel-stack/
│       ├── README.md
│       ├── SKILL.md
│       ├── rules/
│       ├── blueprints/
│       └── templates/
└── artifacts/
```

Guardrails, retained for any future stack or skill addition:

- `my-laravel-stack`'s internal `rules/`/`blueprints/`/`templates/` split is the evidence-backed decomposition this repository actually reached (`artifacts/my-laravel-stack.md`) — a shape earned from that skill's own evidence, not a template any future stack companion should copy by default;
- a `project-specific/useOrbit` grouping was never populated and remains out of scope — project-specific knowledge stays in `useOrbit` itself, not in this repository;
- any future stack beyond Laravel/Vue/Inertia should reach its own package shape from its own evidence, installed alongside the others under `skills/`;
- `docs/` holds timeless, cross-skill guidance that applies across every skill rather than to one in particular: `docs/skill-authoring-methodology.md` — how skills in this repository are authored, classified into portable/stack/project knowledge, and kept reconciled as they evolve, reclassified there after outgrowing its original home as a per-skill dossier — and `docs/skill-consumption.md`, the proven lifecycle a consuming project uses to install, refresh, and validate skills from this repository. `artifacts/` itself stays reserved for the four current per-skill architecture dossiers, not general methodology.

The root `README.md` explains the current layered model and knowledge-boundary distinctions — see it for the up-to-date picture.

---

# 3. Working principles for the roadmap

## Evidence before abstraction

Do not generalize a rule merely because it sounds reusable. Prefer repeated evidence from real projects.

## Consume for real before formalizing the lifecycle

The consume/use/contribute/refresh relationship between `agentic-engineering` and its consumers should be documented from lifecycle events that actually happened, not designed in advance and then exercised to match the design.

## Core before stack layer

When a rule can be expressed without knowing the framework, keep it in the portable methodology.

When it requires a framework or technology, consider the stack companion layer.

When it is unique to one repository or product, keep it project-specific.

## Architecture feeds planning, not the other way around

The intended lifecycle:

```text
architecture discovery
        ↓
approved architecture / decisions
        ↓
feature planning
        ↓
issues + milestone
        ↓
implementation
```

`my-feature-planning` consumes approved architectural decisions without re-litigating them. The skills already distinguish current-state facts, locked decisions, derived constraints, and open implementation details — that separation should be preserved as the stack companion layer evolves. A stack layer should not quietly turn an implementation convention into a product decision.

## Human decisions remain visible

Architecture decisions, product calls, release approval, milestone closure, and other meaningful mutations should remain explicit rather than being hidden behind automation.

## Verification is part of the workflow

A successful command is not proof that the intended state exists. Re-fetch and validate when the workflow mutates durable external state.

## Don't overfit to useOrbit

`useOrbit` is the first source of evidence, not the definition of the standard.

## Don't optimize for publication before portability

The public/reusable version should emerge from proven cross-project methodology rather than from premature packaging decisions.

---

# 4. Future directions

These are possibilities worth keeping in view — not phases, dependencies, commitments, or a prescribed order:

- Project B as a possible later cross-stack proving ground;
- multi-project comparison to refine the portable / stack / project boundary;
- additional stack or platform capabilities when repeated needs appear;
- further consumption or refresh tooling beyond the lifecycle documented in `docs/skill-consumption.md`, if real use exposes a gap it doesn't cover;
- public distribution, reusable publication, versioning, and contribution guidance;
- continued refinement of architecture, planning, Git, issue, release, and delivery methodologies;
- `content-backlog` as a possible Agentic Engineering capability, potentially independent of stack work and possibly worth exploring before Project B if real priorities justify it.
