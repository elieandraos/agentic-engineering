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
                     CUSTOM STACK LAYER
                             |
              (not yet extracted/refined — roadmap.md
               Phase C classifies existing seams;
             Phase D acts on that evidence if justified)
                             |
                    PROJECT-SPECIFIC INPUT
                 domain decisions / repo rules /
                 deployment conventions / product
```

Four kinds of knowledge are in play, and this repository is careful to keep them distinct:

- **Portable custom methodology** — the engineering method itself: how to investigate, plan,
  implement, review, commit, release. This is what lives in this repository today
  (`my-feature-planning`, `my-architecture-laboratory`, `my-git-workflow`).
- **Custom stack/ecosystem knowledge** — genuinely owned, technology-specific implementation
  knowledge for the Laravel/Vue/Inertia stack (e.g. `my-laravel-patterns`,
  `my-phpstorm-conventions`). Not extracted or refined into this repository yet — `roadmap.md`
  Phase C classifies the existing seams first, and Phase D decides what, if anything, the evidence
  justifies: extracting one capability, refining an existing skill, combining/splitting skills, or
  no change. No stack-layer names or packages exist here yet.
- **Project-specific knowledge** — one product's domain model, repo conventions, and deployment
  choices. This is the intended boundary the skills should stay clear of; which existing content
  actually falls on which side of it is what `roadmap.md` Phase C classifies, not something already
  fully sorted here.
- **External first-party capabilities** — upstream dependencies such as Laravel Boost's
  `laravel-best-practices` and `pest-testing`. These are not owned by this repository and are not
  extraction targets; they compose with custom skills but are never absorbed, renamed, duplicated,
  or presented as Agentic Engineering-owned.

Extract rules from evidence, not from imagination — a rule graduates from project-specific to
portable only after repeated evidence, starting with the `useOrbit` classification pass
(`roadmap.md`, Phase C).

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
- Two known couplings remain, deliberately left alone as fidelity-first evidence rather than
  "fixed" into something more generic. These are observations noted during the Phase A pass, not a
  completed classification of what's portable, stack-specific, or `useOrbit`-specific — that
  classification is `roadmap.md` Phase C's job:
  - `my-feature-planning`'s design-reconciliation rule depends on `_design/*.jsx`, a
    `useOrbit`-local, gitignored convention (documented inline as project-specific already).
  - All three skills name `useOrbit`-only implementation skills as what to load once implementation
    starts, but those named skills are not all the same kind of thing: `my-laravel-patterns` and
    `my-phpstorm-conventions` are custom stack knowledge genuinely owned by this ecosystem, while
    `laravel-best-practices` and `pest-testing` are upstream Laravel Boost dependencies — external,
    first-party capabilities this repository does not own and will not absorb, rename, or duplicate.
    Distinguishing which of a skill's implementation-time references are custom versus external is
    exactly the kind of seam `roadmap.md` Phase C is meant to classify; what (if anything) Phase D
    extracts or refines from the custom side only follows once that evidence exists — not a defect
    to patch now.
- `my-architecture-laboratory`'s two style precedents (`Reusable Documents Architecture`,
  `Centralized Tagging Architecture`) are live `claude.ai` Artifact URLs tied to the user's account,
  not `useOrbit` repo files. This claim is now stale for the Tagging citation specifically:
  `roadmap.md` Phase C (`phase-discovery.md`) directly re-verified the cited "Centralized Tagging
  Architecture" URL and found it dead ("artifact not found"), independent of and prior to that phase's
  own work. A live, differently-titled replacement artifact ("Tagging Architecture") exists and was
  confirmed, on content, to document `useOrbit`'s current tagging architecture — but
  `my-architecture-laboratory` still cites the dead URL, not the live one. This is a
  documentation-currency gap in this Phase A finding, not a defect in Phase A's process at the time it
  was written; repairing the skill's citation is Phase D's (or a maintenance pass's) to address. See
  `phase-discovery.md` for the full evidence.

**Phase B (`roadmap.md`) is now underway.** The three canonical skills have been consumed from this
repository at commit `12d9c1df75dde5fb1d944b62b0679c1e211137a4` into gitignored
`useOrbit/.claude/skills/` as the active local snapshots, with upstream commit provenance recorded
locally alongside them. The pre-Phase-A originals are preserved as rollback material, moved outside
`useOrbit`'s active skill-discovery path rather than deleted. The canonical `my-feature-planning`
snapshot has already been used on genuine `useOrbit` work, producing
[`useOrbit#299`](https://github.com/elieandraos/useOrbit/issues/299) — the first durable consumer
artifact of this relationship; that first pass warranted no upstream skill contribution. Phase B's
remaining gate is a genuine refresh/update-and-verification cycle — real work warranting a canonical
skill update, that update pulled into `useOrbit`, and the refreshed skill verified there — which has
not yet occurred and remains open. `useOrbit#299` is not a mandatory step toward that gate; normal
`useOrbit` development continues independently of it.
