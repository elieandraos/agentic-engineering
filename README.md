# agentic-engineering

An evidence-driven engineering ecosystem: a portable methodology for architecting, planning, and
delivering software work, paired with stack-specific companions that carry technology knowledge
without leaking it into that portable core. It is a reusable engineering workflow, not a prompt
collection for one repository or framework.

## Ecosystem model

The ecosystem is layered, and each layer supplies a different kind of knowledge:

```
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
                             |
                    my-laravel-stack
             (Laravel + InertiaJS + Vue 3 + Pest —
              additive to Laravel Boost, not a
                    replacement for it)
                             |
                    PROJECT-SPECIFIC INPUT
                 domain decisions / repo rules /
                 deployment conventions / product
```

The portable methodologies at the top are stack-neutral by design: they assume nothing about which
language, framework, or tracker a consuming project uses. A stack companion supplies the
technology-specific knowledge a portable skill deliberately doesn't carry. Project-specific input —
one product's domain model, conventions, and deployment choices — stays outside both layers.

## Portable methodology skills

Three skills form the portable core. Each owns a distinct stage of engineering work and stops at an
intentional boundary — architecture work never drafts a tracker issue, planning never re-litigates
approved architecture, and neither writes application code.

| Skill | Owns |
|---|---|
| [`my-architecture-laboratory`](my-architecture-laboratory/) | Investigating and explaining how a system actually works, then producing a new architecture guide, an updated existing guide, or an approved `plan.md` handoff for a planning initiative. |
| [`my-feature-planning`](my-feature-planning/) | Turning a feature request or an approved `plan.md` into a reviewed, drafted set of GitHub issues — classification, scope, design reconciliation, sequencing, review. |
| [`my-git-workflow`](my-git-workflow/) | Moving an already-approved issue through implementation review, commits, verification, closure, release, and milestone completion. |

None of the three assume a particular language, framework, or project layout — a consuming project
supplies its own framework, directories, and concrete artifacts; each skill supplies the method. See
each skill's own `README.md` for the full walkthrough and `SKILL.md` for the operational rules.

## Stack companions

[`my-laravel-stack`](my-laravel-stack/) is a stack-specific companion for a **Laravel + InertiaJS +
Vue 3 + Pest** stack. It is not a fourth portable methodology skill — it answers implementation
questions the portable skills deliberately don't, and a consuming project loads it alongside the
three portable skills rather than in place of any of them.

It carries only the delta genuinely additive to Laravel Boost's `laravel-best-practices` and
`testing-best-practices`, organized as:

- **`rules/`** — independently applicable conventions and invariants.
- **`blueprints/`** — multi-component implementation shapes that compose several rules into one
  recognizable pattern.
- **`templates/`** — complete, installable starting points meant to be copied and adapted.

Laravel Boost remains an external dependency throughout: `my-laravel-stack` composes with it but
never absorbs, renames, or duplicates what it already owns. A different stack would get its own,
separate companion built the same way — evidence-backed conventions layered on top of whatever that
stack's own first-party capabilities already provide.

## How the pieces work together

Work moves through the portable skills in one direction, with each stage handing off a concrete,
approved artifact to the next:

```
my-architecture-laboratory → approved architecture / plan.md
  → my-feature-planning     → GitHub issues
  → my-git-workflow (Git/GitHub delivery) + stack companions (application code)
```

`my-architecture-laboratory` investigates and, where the goal is a real change rather than
documentation, produces an approved `plan.md` — current-state facts, locked decisions, derived
constraints, and open implementation details, kept visibly distinct. `my-feature-planning` treats
that plan as canonical, resolving only the remaining open details that materially affect scope,
dependencies, or acceptance criteria, and drafts reviewed GitHub issues from it. `my-git-workflow`
then picks up one already-approved issue at a time and owns implementation review, commit structure,
verification, closure, and the release/milestone lifecycle — while a stack companion answers the
implementation-level questions that arise along the way. Each handoff crosses only once its artifact
is approved; none of the three re-derives a decision the stage before it already settled.

## Knowledge boundaries

Four kinds of knowledge are in play, and the ecosystem is careful to keep them distinct:

- **Portable methodology** — the engineering method itself: how to investigate, plan, implement,
  review, commit, release. Cross-stack by design.
- **Stack companion knowledge** — genuinely owned, technology-specific implementation knowledge for
  one stack, such as `my-laravel-stack`. A stack companion answers implementation questions without
  the portable methodology ever needing to know which stack it's operating on.
- **Project-specific knowledge** — one product's domain model, repo conventions, and deployment
  choices. This is the boundary the portable skills and stack companions stay clear of; a consuming
  project supplies it as input, not something either layer re-sorts.
- **External first-party capabilities** — upstream dependencies such as Laravel Boost's
  `laravel-best-practices` and `testing-best-practices`. These aren't owned by this repository and
  aren't extraction targets; a stack companion composes with them but never absorbs, renames,
  duplicates, or presents them as owned by this ecosystem.

## Repository structure

```
agentic-engineering/
├── README.md                    this file
├── roadmap.md                   living architecture and evolution notes
├── docs/                        timeless, cross-skill methodology
├── my-architecture-laboratory/  portable skill — investigation and architecture
├── my-feature-planning/         portable skill — scoping and issue drafting
├── my-git-workflow/             portable skill — implementation and delivery
├── my-laravel-stack/            stack companion — Laravel + InertiaJS + Vue 3 + Pest
└── skill-audits/                per-skill dossiers: purpose, boundaries, open questions
```

Each skill directory carries its own `README.md` (the walkthrough), `SKILL.md` (the operational
routing and rules an agent actually loads), and a `rules/` directory of individually applicable
rule files. `my-laravel-stack` additionally carries `blueprints/` and `templates/`. `skill-audits/`
holds supporting analysis per skill — it complements each skill's `README.md`/`SKILL.md` rather than
replacing them as the operational source of truth. `docs/` holds methodology that applies across
every skill rather than to one in particular — currently
[`skill-authoring-methodology.md`](docs/skill-authoring-methodology.md), the current guide to
evidence-backed skill authoring, knowledge classification, ownership, and reconciliation.

## Consumption

There is no packaged installer. To use a skill in another project:

1. Clone this repository.
2. Copy each desired top-level skill directory (e.g. `my-architecture-laboratory/`,
   `my-feature-planning/`, `my-git-workflow/`, `my-laravel-stack/`) into a location Claude Code
   scans for skills — personal `~/.claude/skills/<name>/` or project `.claude/skills/<name>/`.

Copy only the skills a project actually needs; a stack companion is only useful alongside a project
that runs on that stack.

## Evolution principle

Rules in this ecosystem evolve from demonstrated need and real use, not from speculative
generalization. A rule earns a place in the portable core, in a stack companion, or in neither, based
on the evidence behind it — not on how general it could theoretically be made. See `roadmap.md` for
how the ecosystem's architecture and direction continue to develop under that principle.
