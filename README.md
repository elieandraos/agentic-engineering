# agentic-engineering

A portable system of agentic software-engineering methodologies — how to plan features, reconstruct
architecture, and move work through implementation, review, commits, and release. The goal is
reusable engineering workflow, not a prompt collection for one repository or framework.

The system is being developed from real use rather than designed in a vacuum. Its first proving
ground is `useOrbit`, a Laravel/Vue/Inertia application. See `roadmap.md` for the full plan.

## The three-skill family

| Skill | Owns |
|---|---|
| [`my-architecture-laboratory`](my-architecture-laboratory/) | Reconstructing and validating how a capability actually works, then handing that off as a published architecture guide, or as a canonical `plan.md` for a planning initiative. |
| [`my-feature-planning`](my-feature-planning/) | Turning an approved feature ask or `plan.md` into a reviewed, drafted set of GitHub issues — classification, scope, design reconciliation, sequencing, review. |
| [`my-git-workflow`](my-git-workflow/) | Moving an already-approved issue through implementation, review, commits, verification, closure, release, and milestone completion. |

Each owns a distinct stage and stops at an intentional boundary — architecture work never drafts a
GitHub issue, planning never re-investigates architecture, and neither writes application code. See
each skill's own `README.md` for the full walkthrough and `SKILL.md` for the operational rules.

## The layered model

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
                       STACK ADAPTERS
                             |
                  (not yet extracted — see
                   roadmap.md, Phase C)
                             |
                    PROJECT-SPECIFIC INPUT
                 domain decisions / repo rules /
                 deployment conventions / product
```

- **Portable methodology** — the engineering method itself: how to investigate, plan, implement,
  review, commit, release. This is what lives in this repository.
- **Stack adapters** — technology-specific implementation knowledge (Laravel/Eloquent/Inertia,
  Nuxt/Supabase/Vercel, etc.). Not designed yet — there isn't enough cross-project evidence to know
  the right boundary. Provisional names like `my-laravel-patterns` are recorded in `roadmap.md` but
  intentionally not created here.
- **Project-specific input** — one product's domain model, repo conventions, and deployment
  choices. Stays in the consuming project, never in this repository.

Extract rules from evidence, not from imagination — a rule graduates from project-specific to
portable only after repeated evidence from more than one project (`roadmap.md`, Phase B onward).

## Current portability status

This is a **Phase A** repository: a local externalization of the three skills out of `useOrbit`'s
working tree, done for fidelity, not redesigned. Concretely:

- The skills are copied local files, verified structurally and referentially against their
  `useOrbit` originals — they have **not** been installed or loaded from GitHub yet. Nothing here
  claims that installation path has been verified.
- `my-architecture-laboratory` (renamed from `architecture-laboratory`) had one literal
  `useOrbit` reference in its Artifact template's footer, replaced with a `{{Project}}` placeholder
  consistent with the template's existing convention — the only content fix made in this pass.
- Two known couplings remain, deliberately left alone as fidelity-first evidence rather than
  "fixed" into something more generic:
  - `my-feature-planning`'s design-reconciliation rule depends on `_design/*.jsx`, a
    `useOrbit`-local, gitignored convention (documented inline as project-specific already).
  - All three skills name `useOrbit`-only implementation skills (`my-laravel-patterns`,
    `laravel-best-practices`, `pest-testing`, etc.) as what to load once implementation starts —
    exactly the stack-adapter seam `roadmap.md` Phase C expects to formalize later, not a defect to
    patch now.
- `my-architecture-laboratory`'s two style precedents (`Reusable Documents Architecture`,
  `Centralized Tagging Architecture`) are live `claude.ai` Artifact URLs tied to the user's account,
  not `useOrbit` repo files — they resolve from any project context, so no fix was needed there.

The original skills remain untouched under `useOrbit/.claude/skills/` as the rollback source.
