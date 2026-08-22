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
              (not yet extracted — roadmap.md
               Phase C classifies existing seams;
             Phase D may extract one if justified)
                             |
                    PROJECT-SPECIFIC INPUT
                 domain decisions / repo rules /
                 deployment conventions / product
```

- **Portable methodology** — the engineering method itself: how to investigate, plan, implement,
  review, commit, release. This is what lives in this repository.
- **Stack adapters** — technology-specific implementation knowledge (Laravel/Eloquent/Inertia,
  Nuxt/Supabase/Vercel, etc.). Not designed yet — `roadmap.md` Phase C classifies the existing
  seams first, and Phase D may extract a Laravel/Inertia adapter only if that evidence justifies it.
  No adapter names or packages exist here yet.
- **Project-specific input** — one product's domain model, repo conventions, and deployment
  choices. This is the intended boundary the skills should stay clear of; which existing content
  actually falls on which side of it (portable / stack-specific / `useOrbit`-specific) is what
  `roadmap.md` Phase C classifies, not something already fully sorted here.

Extract rules from evidence, not from imagination — a rule graduates from project-specific to
portable only after repeated evidence, starting with the `useOrbit` classification pass and
continuing through later cross-stack validation (`roadmap.md`, Phase C onward).

## Current portability status

**Phase A is complete.** The three skills were externalized out of `useOrbit`'s working tree for
fidelity, not redesigned, published to this repository's GitHub `main`, and independently verified
installable and loadable from that published commit. Concretely:

- The skills were copied local files, verified structurally and referentially against their
  `useOrbit` originals, then committed and pushed to `github.com/elieandraos/agentic-engineering`
  (`main`, commit `fe5bd297908b1245b5670341eb3ac0a5253b149a`).
- Installation/loading was independently verified via a **fresh `git clone` of that GitHub commit**
  into a scratch location, then copying each of the three top-level skill directories from that
  clone into an isolated test project's `.claude/skills/<name>/`, outside both `useOrbit` and this
  checkout. Neither that isolated project nor personal `~/.claude/skills/` — the two locations
  Claude Code actually scans — held any pre-existing copy of the three skills beforehand; the
  original `useOrbit/.claude/skills/` copies still existed on the machine, just outside both of
  those discovery scopes. Claude Code discovered all three by their external names, loaded each
  `SKILL.md`, and read specific, verbatim content out of their `rules/`/`references/` files
  (including the renamed `my-architecture-laboratory` and the `{{Project}}` footer fix), proving the
  files actually came from that clone rather than being recalled from training data or a stale copy.
- There is **no built-in Claude Code command that installs a bare skill repository directly from
  GitHub** — no `marketplace.json`/`plugin.json` exists here, and none was added to force one. The
  verified, actually-supported mechanism is to clone the repository, then copy each desired
  top-level skill directory into a location Claude Code scans (personal `~/.claude/skills/<name>/`
  or project `.claude/skills/<name>/`). This is a real
  distribution gap, not a defect in this repository — Phase J is where a packaging answer (if any)
  belongs, and none is claimed here.
- `my-architecture-laboratory` (renamed from `architecture-laboratory`) had one literal
  `useOrbit` reference in its Artifact template's footer, replaced with a `{{Project}}` placeholder
  consistent with the template's existing convention — the only content fix made in this pass.
- Two known couplings remain, deliberately left alone as fidelity-first evidence rather than
  "fixed" into something more generic. These are observations noted during the Phase A pass, not a
  completed classification of what's portable, stack-specific, or `useOrbit`-specific — that
  classification is `roadmap.md` Phase C's job:
  - `my-feature-planning`'s design-reconciliation rule depends on `_design/*.jsx`, a
    `useOrbit`-local, gitignored convention (documented inline as project-specific already).
  - All three skills name `useOrbit`-only implementation skills (`my-laravel-patterns`,
    `laravel-best-practices`, `pest-testing`, etc.) as what to load once implementation starts —
    exactly the kind of seam `roadmap.md` Phase C is meant to classify, and which Phase D may later
    extract into an adapter, only if the evidence justifies it — not a defect to patch now.
- `my-architecture-laboratory`'s two style precedents (`Reusable Documents Architecture`,
  `Centralized Tagging Architecture`) are live `claude.ai` Artifact URLs tied to the user's account,
  not `useOrbit` repo files — they resolve from any project context, so no fix was needed there.

The original skills remain untouched under `useOrbit/.claude/skills/` as the rollback source.
