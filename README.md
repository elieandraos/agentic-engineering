# agentic-engineering

A portable system of agentic software-engineering methodologies — how to plan features, reconstruct
architecture, and move work through implementation, review, commits, and release. The goal is
reusable engineering workflow, not a prompt collection for one repository or framework.

The system is being developed from real use rather than designed in a vacuum. `useOrbit`, a
Laravel/Vue/Inertia application, is both the origin of the three-skill family below and the system's
first real consumer of it as an external, canonical source. See `roadmap.md` for the full plan.

## The three-skill family

| Skill | Owns |
|---|---|
| [`my-architecture-laboratory`](my-architecture-laboratory/) | Reconstructing and validating how a system actually works, then producing a new architecture guide, an updated existing guide, or an approved `plan.md` handoff for a planning initiative. |
| [`my-feature-planning`](my-feature-planning/) | Turning an approved feature ask or `plan.md` into a reviewed, drafted set of GitHub issues — classification, scope, design reconciliation, sequencing, review. |
| [`my-git-workflow`](my-git-workflow/) | Moving an already-approved issue through implementation review, commits, verification, closure, release, and milestone completion. |

Each owns a distinct stage and stops at an intentional boundary — architecture work never drafts a
GitHub issue, planning never re-litigates approved architecture (though it still verifies relevant
current implementation evidence), and neither writes application code. See
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
                     CUSTOM STACK LAYER
                             |
                    my-laravel-stack
             (Laravel + InertiaJS + Vue 3 + Pest —
           the verified delta additive to Laravel Boost)
                             |
                    PROJECT-SPECIFIC INPUT
                 domain decisions / repo rules /
                 deployment conventions / product
```

Four kinds of knowledge are in play, and this repository is careful to keep them distinct:

- **Portable custom methodology** — the engineering method itself: how to investigate, plan,
  implement, review, commit, release. This is the portable three-skill family above
  (`my-feature-planning`, `my-architecture-laboratory`, `my-git-workflow`) — cross-stack by design,
  and distinct from the custom stack companion below.
- **Custom stack/ecosystem knowledge** — genuinely owned, technology-specific implementation
  knowledge for the Laravel + InertiaJS + Vue 3 + Pest stack, implemented as
  [`my-laravel-stack`](my-laravel-stack/). `roadmap.md` Phase C classified the existing seams and
  Phase D acted on that evidence, extracting this companion — see "Current stack status" below. It
  is a stack-specific companion alongside the portable three-skill family, not a fourth member of it.
  `my-phpstorm-conventions` remains a separate, fully deferred companion.
- **Project-specific knowledge** — one product's domain model, repo conventions, and deployment
  choices. This is the intended boundary the skills should stay clear of; which existing content
  actually falls on which side of it is what `roadmap.md` Phase C's completed classification
  determined (`phase-discovery.md`), not something this README re-sorts.
- **External first-party capabilities** — upstream dependencies such as Laravel Boost's
  `laravel-best-practices` and `testing-best-practices`. These are not owned by this repository and
  are not extraction targets; `my-laravel-stack` composes with them but never absorbs, renames,
  duplicates, or presents them as Agentic Engineering-owned.

Extract rules from evidence, not from imagination — a rule graduates from project-specific to
portable only after repeated evidence, starting with the completed `useOrbit` classification pass
(`roadmap.md`, Phase C) and continuing through the completed Phase D stack extraction.

## Current stack status

**Phase D is complete.** `roadmap.md` §5 records the decision; `phase-d-stack-discovery.md`,
`phase-d-stack-synthesis.md`, and [`skill-audits/my-laravel-stack.md`](skill-audits/my-laravel-stack.md)
carry the full evidence and current assessment — this README doesn't reproduce it. In short:
[`my-laravel-stack`](my-laravel-stack/) is a personal, portable companion for Laravel + InertiaJS +
Vue 3 + Pest, owning only the delta genuinely additive to Laravel Boost, organized as `rules/`,
`blueprints/`, and `templates/`. Canonical authoring completed through `4609cd5`; `useOrbit`'s
exhaustive `tests/` audit then supplied its first real consumer exercise, exposing two portable gaps
corrected upstream (`c424c3f`, `560556f`) and forward-verified by an independent reconciliation pass.

Honest limits, stated openly rather than implied as resolved: every piece of evidence still comes from
exactly one real project, `useOrbit`; the resulting `useOrbit` test-directory restructuring is
owner-approved but not yet executed or verified under a real test-suite run; no second
Laravel/Inertia/Vue/Pest consumer has tested this skill; and the skill declares Vue 3 as part of its
stack boundary but currently owns no mature, independent Vue-specific rules — Vue implementation
questions still route to Laravel Boost's `inertia-vue-development`.

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
  distribution gap, not a defect in this repository — a packaging answer (if any) belongs to a later,
  non-committed possibility (see "Future directions" in `roadmap.md`), and none is claimed here.
- `my-architecture-laboratory` (renamed from `architecture-laboratory`) had one literal
  `useOrbit` reference in its Artifact template's footer, replaced with a `{{Project}}` placeholder
  consistent with the template's existing convention — the only content fix made in this pass.
- Two couplings were noted during the Phase A pass, recorded as fidelity-first observations rather
  than "fixed" into something more generic. That pass was an observation, not a completed
  classification of what's portable, stack-specific, or `useOrbit`-specific — that classification was
  `roadmap.md` Phase C's job, and Phase C has since completed it. `my-feature-planning`'s own
  rule-by-rule authoring pass has since closed
  the first coupling for that skill specifically. Both couplings are now historical, not current:
  - **Resolved for `my-feature-planning`.** Its design-reconciliation rule depended on
    `_design/*.jsx`, a `useOrbit`-local, gitignored convention. Its `design-reconciliation.md` rule
    no longer assumes any directory, filename, format, design tool, or tracked-vs-untracked status —
    it discovers the consuming project's actual design-artifact sources from project-supplied context
    instead. This finding is Phase A history for `my-feature-planning`, not a current defect.
  - **No longer present in any of the three skills.** Phase A also observed all three naming
    `useOrbit`-only implementation skills such as `my-laravel-patterns` and
    `my-phpstorm-conventions`, alongside external Laravel Boost capabilities such as
    `laravel-best-practices` and `pest-testing`. None of those names appear in the current active
    files of `my-feature-planning`, `my-architecture-laboratory`, or `my-git-workflow` — this Phase A
    observation no longer describes current active skill content. Neither of the other two skills was
    touched by `my-feature-planning`'s authoring pass, so that pass does not explain the change.
    Distinguishing custom stack knowledge from external first-party capabilities generally — and
    ensuring the latter is never absorbed, renamed, or duplicated — is a boundary `roadmap.md` Phase C
    classified and Phase D has since acted on, producing `my-laravel-stack` (see "Current stack status"
    above).
- `my-architecture-laboratory`'s two original style precedents (`Reusable Documents Architecture`,
  `Centralized Tagging Architecture`) were live `claude.ai` Artifact URLs tied to the user's account,
  not `useOrbit` repo files. `roadmap.md` Phase C (`phase-discovery.md`) directly re-verified the
  cited "Centralized Tagging Architecture" URL and found it dead ("artifact not found"), independent
  of and prior to that phase's own work — a documentation-currency gap in the original Phase A
  finding, not a defect in Phase A's process at the time it was written. This is now resolved, not
  merely repaired: `my-architecture-laboratory`'s own authoring pass removed both precedent
  citations from the skill entirely, along with the framing that tied the methodology to them,
  rather than swapping in a fresh replacement link. See `skill-audits/my-architecture-laboratory.md`
  for the authoring evidence and `phase-discovery.md` for the original finding.

**Phase B (`roadmap.md`) is complete.** The three canonical skills were consumed into gitignored
`useOrbit/.claude/skills/` as the active local snapshots, with upstream commit provenance recorded
locally and the pre-Phase-A originals preserved as rollback material rather than deleted. Three
genuine consumer exercises have since occurred, each exercising a distinct part of the pipeline:
a subsequently-refined `my-git-workflow` was refreshed into the consumer, verified byte-identical to
canonical, and carried real Backlog/hotfix work end to end
([`useOrbit#299`](https://github.com/elieandraos/useOrbit/issues/299)); `my-feature-planning`'s
approved-`plan.md` input path was then exercised, producing `useOrbit#300`–`#302` and one portable
sequencing correction; and those same three issues were subsequently carried through
`my-git-workflow`'s full scoped-delivery-milestone path for the first time — shared milestone branch,
PR [`#303`](https://github.com/elieandraos/useOrbit/pull/303), two real-CI failure-and-recovery
cycles, merge, milestone closure, and a published, validated release `v0.17.1` — surfacing reusable
evidence behind several narrow rule corrections across both skills. Full evidence: `roadmap.md`,
Phase B; `skill-audits/my-git-workflow.md` and `skill-audits/my-feature-planning.md`.

**Portable-core authoring is complete.** All three canonical skills — `my-git-workflow`,
`my-feature-planning`, and `my-architecture-laboratory` — have now received the targeted
authoring/refinement pass `roadmap.md` Phase C's classification called for, and each has a current
dossier under `skill-audits/` (`my-git-workflow.md`, `my-feature-planning.md`,
`my-architecture-laboratory.md`), alongside a shared `skill-audits/skill-authoring-methodology.md`
now validated by three real passes. Unlike the other two skills above, `my-architecture-laboratory`'s
revision has not yet completed a fresh real-consumer exercise in `useOrbit` — see
`skill-audits/my-architecture-laboratory.md` for what remains unverified.
