# Agentic Engineering Roadmap

## Purpose

`agentic-engineering` is the home for a growing, portable system of agentic software-engineering methodologies.

The goal is not to collect prompts for one repository or one framework. The goal is to build reusable engineering workflows that can operate across projects and technology stacks, while keeping stack-specific implementation knowledge and project-specific conventions out of the portable core.

The system is being developed from real use rather than designed in a vacuum. `useOrbit` is the first proving ground, and is now becoming the system's first real consumer: the canonical skills need to be consumed and used for genuine `useOrbit` work before any further generalization. A second, materially different application stack will later provide a portability test, but only once that consumption relationship and the evidence it produces are in place.

---

## The story so far

The first generation of the system grew inside the `useOrbit` project as local Claude Code skills.

`useOrbit` is a Laravel/Vue/Inertia application. Its current engineering workflow includes three mature capabilities:

- `my-feature-planning`
- `my-git-workflow`
- `my-architecture-laboratory`

The skills evolved through real feature work, especially the Auth & 2FA milestone, and were repeatedly refined when real development exposed gaps.

The important design principle that emerged is:

> Extract rules from evidence, not from imagination.

That principle applies both to the product architecture being documented and to the agentic workflows themselves.

The skills are now ready to leave their original repository and become an external, reusable engineering system.

---

# 1. Current architecture of the ecosystem

The long-term model is a layered system.

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
                       STACK ADAPTERS
                             |
               +-------------+-------------+
               |                           |
        Laravel / Vue / Inertia      Nuxt / Vue / Vite
        Pest / Eloquent / Fortify    Supabase / Vercel
               |                           |
               +-------------+-------------+
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

### Stack adapters

Technology-specific implementation knowledge:

- Laravel / Eloquent / Inertia / Fortify / Pest;
- Nuxt / Vue / Vite;
- Supabase;
- Vercel;
- other stack conventions discovered later.

### Project-specific input

Things that belong to one product or repository:

- domain model and business decisions;
- repository conventions;
- deployment/environment choices;
- naming dialects;
- existing architecture decisions;
- project-specific release or issue conventions.

The exact adapter architecture is intentionally **not designed yet**. We do not have enough cross-project evidence yet to know the right configuration/schema boundary.

---

# 2. Phase A — Externalize the skills

## Objective

Move the current local skills out of the `useOrbit` working tree and establish `agentic-engineering` as their external source of truth.

## Current repository

GitHub repository:

`agentic-engineering`

Repository description:

> A portable agentic engineering system for architecture, feature planning, implementation workflows, and software delivery across technology stacks.

## Initial skill set

```text
agentic-engineering/
├── README.md
├── my-feature-planning/
│   ├── SKILL.md
│   └── rules/
├── my-git-workflow/
│   ├── SKILL.md
│   └── rules/
└── my-architecture-laboratory/
    ├── SKILL.md
    └── rules/
```

`architecture-laboratory` becomes `my-architecture-laboratory` so the three core skills form a coherent family without changing what the skill does.

## Principles for this phase

Do not rewrite the methodologies just because they are moving repositories.

First establish a clean external source of truth. Then test that the skills can be consumed from GitHub.

The first externalization pass should preserve behavior and structure unless a change is necessary for portability or installation.

## Completion criteria

- [x] The three skills live in `agentic-engineering`. (2026-08-22, published to GitHub `main` @ `fe5bd297908b1245b5670341eb3ac0a5253b149a` — see "Current status" below)
- [x] Each skill has its own `SKILL.md`.
- [x] Internal rule files remain reachable from each skill.
- [x] The architecture skill is renamed to `my-architecture-laboratory`.
- [x] Repository README explains the purpose and current skill family.
- [x] Each skill can be installed/loaded from the GitHub repository. (2026-08-22, independently verified via a fresh `git clone` of `main` @ `fe5bd297...` into a scratch location, then copying each skill directory into an isolated test project's `.claude/skills/<name>/`, with no pre-existing copy in that project or in personal `~/.claude/skills/` — see "Current status" below.)
- [x] No skill depends on files that only exist inside `useOrbit` unless that dependency is explicitly documented as project-specific. (Findings recorded in root `README.md`, "Current portability status".)

**Phase A is complete.**

---

# 3. Phase B — Establish useOrbit as the first real consumer

## Objective

Phase A proved the installation mechanism: fresh-clone `agentic-engineering`, then copy the desired top-level skill directories into a consuming project's `.claude/skills/<name>/`. That mechanism is not being redesigned or re-tested here — Phase B is not another portability test of it. It puts the proven mechanism to work on the relationship that actually matters first:

```text
agentic-engineering/main
        ↓
useOrbit/.claude/skills/
```

`agentic-engineering` becomes the **sole canonical source of truth** for the three portable skills and the sole durable, Git-tracked source of their content and upstream history. `useOrbit` holds upstream-derived, project-local runtime *snapshots* of them — not an independently authored source of truth or a second durable copy. `useOrbit/.claude` remains gitignored, and the consumed snapshots are not committed to the `useOrbit` repository. The pre-Phase-A copies that used to be edited directly inside `useOrbit/.claude/skills/` are what this phase retires from active use.

## Requirements

- **Provenance is required; no general format is fixed yet.** Every active snapshot consumed into `useOrbit` must be operationally traceable to the exact upstream `agentic-engineering` commit it came from. During Phase B, that provenance record may remain local alongside the consumed snapshots; it does not need to be committed to the `useOrbit` repository. The snapshots themselves remain uncommitted because `useOrbit/.claude` stays gitignored. What form the provenance record takes should continue to follow what the real consume/refresh work demonstrates is adequate, rather than being designed speculatively. This establishes the ownership and persistence boundary only; it does not design a synchronization, bootstrap, installation, or packaging mechanism.
- **Preserve the old copies as rollback material until validated, then retire them.** The independently-authored `useOrbit` originals remain preserved as rollback material until the canonical, upstream-derived snapshots have been validated on real `useOrbit` work. Only then are the old copies retired from active use — how they're preserved in the meantime is not specified here.
- **A genuine refresh/update-and-verification cycle is the remaining lifecycle gate; contribution is conditional, not a completion gate.** Phase B's second output is an operational lifecycle: how a skill gets consumed into `useOrbit`, how it gets used there, and — critically — how `useOrbit` pulls an updated snapshot from upstream and verifies it still works as a consumer. Only that refresh/update-and-verification cycle gates Phase B's completion. If real `useOrbit` work surfaces a fix or improvement worth contributing upstream, record it when it happens; if no such change is warranted, recording that outcome is itself sufficient — contribution is conditional on what real use actually produces, not a checklist item that has to fire. Document the lifecycle as it is actually exercised during real feature work — do not manufacture a change to a skill merely to rehearse it, and do not write the lifecycle down before it has actually happened.

## Completion criteria

- [x] Canonical skill copies are consumed into `useOrbit/.claude/skills/` and used for real, in-progress `useOrbit` work (not a synthetic or throwaway test). (2026-08-23 — consumed from `agentic-engineering` @ `12d9c1df75dde5fb1d944b62b0679c1e211137a4`; the canonical `my-feature-planning` snapshot used on a genuine discovered-work investigation and planning pass, producing [useOrbit#299](https://github.com/elieandraos/useOrbit/issues/299).)
- [x] The active local snapshots are traceable to their exact upstream commit, in whatever provenance format the real work shows is adequate; the snapshots remain uncommitted, and the provenance record may remain local alongside them. (2026-08-23 — consumed at commit `12d9c1df75dde5fb1d944b62b0679c1e211137a4`, recorded locally in `useOrbit/.claude/skills/UPSTREAM_PROVENANCE.md`.)
- [ ] At least one genuine refresh/update-and-verification cycle has been observed and recorded from actual `useOrbit` work: an updated skill snapshot pulled from upstream and verified as a consumer. (Not yet met — no newer upstream skill-content update or genuinely updated skill snapshot exists yet to refresh from. The subsequent commit `c09f15f9127317cc0faf79f03ff5072441c22d04` changed documentation only; it does not trigger or satisfy this criterion.)
- [x] The old, independently-maintained `useOrbit` skill copies are retired from active use. (2026-08-23 — moved to `.claude/_rollback/pre-phase-b-skills/`, outside `.claude/skills/` discovery scope; preserved as rollback material, not deleted.)

---

# 4. Phase C — Classify the proven skills' content

## Objective

Once Phase B's consumer relationship is established and its consume/use/refresh lifecycle has been observed — not merely once consumption is underway — analyze the three proven skills as they actually exist and are actually used, and classify their content into:

1. **portable methodology** — survives independent of stack or project;
2. **Laravel / Vue / Inertia stack knowledge** — technology-specific, but not `useOrbit`-specific;
3. **`useOrbit`-specific project knowledge** — belongs to this one product/repository.

This is an evidence-gathering pass, not an architecture pass. Its output is a classification of what already exists, not a new package, folder, or adapter.

## Important rule

This analysis produces evidence. Evidence may or may not justify a Laravel/Inertia adapter — that decision belongs to Phase D, not this one. Do not pre-sort content into an adapter shape while doing this classification; classify first, decide what to build second.

---

# 5. Phase D — Extract a Laravel/Inertia adapter, if justified

Only after Phase C's classification exists should we decide whether a Laravel/Inertia adapter is worth creating.

A stack skill should be created when the Phase C evidence shows a set of conventions is:

1. technology-specific;
2. reusable across multiple features;
3. useful to an agent during implementation;
4. distinct from product/domain rules.

**Do not create the adapter upfront as a dumping ground** for anything that isn't obviously portable. If Phase C's evidence doesn't clearly justify an adapter yet, leave the content where it is and wait for more evidence — including, potentially, evidence from Phase E (Project B).

### Example boundary

Core methodology:

> Walk the resource lifecycle, resolve authorization, identify persistence changes, determine tests, then sequence backend and frontend work appropriately.

Laravel adapter:

> Use migrations, Eloquent models, policies, FormRequests, API Resources, Actions, routes, Pest, and the project's established Vue/Inertia patterns.

The methodology should not need to know which one it is using.

---

# 6. Phase E — Project B: the cross-stack proving ground

Project B remains the later proving ground for cross-stack portability — it is **not the immediate next step**. It comes after canonical consumption is established (Phase B) and after the `useOrbit` skills have been analyzed for portable vs. stack vs. project content (Phase C), because that analysis is expected to produce most of the near-term portability evidence more cheaply than a second full project would.

### Project A — useOrbit

Current stack:

- Laravel
- Vue
- Inertia
- Eloquent
- Fortify
- Pest
- GitHub
- Claude Code

### Project B — new AI/training application

Known stack direction:

- Vue
- Nuxt
- Vite
- Supabase
- Vercel
- GitHub
- SSO / authentication
- AI training / personas domain

The exact architecture and conventions of Project B should be discovered, not assumed.

## Goal of the comparison

Run the same portable methodologies against Project B and observe where they diverge from how they were actually used on `useOrbit` — including from any Laravel/Inertia adapter Phase D may have produced.

Examples of questions to learn from:

- Does feature classification remain useful without Laravel resource conventions?
- Does architecture reconstruction need anything inherently Laravel-specific?
- Does issue planning depend on Eloquent-style CRUD assumptions?
- What parts of the Git workflow are truly GitHub-level versus repository-specific?
- Which implementation patterns belong in a stack skill rather than in the core methodology?
- Which rules survive unchanged across Laravel/Inertia and Nuxt/Supabase/Vercel?

## Important rule

Do not generalize from one project when a second project can provide evidence. But do not treat Project B as more urgent than the consumption and analysis work (Phases B and C) that comes first — that work is expected to sharpen what Project B should even be checked against.

---

# 7. Phase F — Establish the general adapter boundary

At this stage, synthesize the `useOrbit` classification (Phase C) and the Project B comparison (Phase E) and explicitly separate:

```text
portable methodology
        |
        +---- stack-specific knowledge
        |
        +---- project-specific conventions
```

This is the eventual **adapter problem**.

The adapter is the place where technology and repository conventions plug into a portable methodology without contaminating the core skill.

Examples of information that may eventually become adapter inputs:

- stack/framework;
- implementation patterns;
- testing conventions;
- UI conventions;
- persistence and authorization mechanisms;
- CI/release mechanics;
- naming and repository dialect;
- project-specific architecture files or decision sources.

Do not design a universal adapter schema until multiple projects have demonstrated what it needs to contain.

---

# 8. Phase G — Harden Git / issue / release portability

`my-git-workflow` has already evolved beyond simple Git commands.

Its current conceptual lifecycle is:

```text
implementation
→ issue closure
→ PR
→ merge
→ release
→ release validation
→ milestone completion check
→ milestone closure
```

The workflow now treats these as distinct artifacts and lifecycle events:

- Commit: technical change/history.
- Issue: unit of planned/discovered work.
- PR: integrated engineering change.
- Release: shipped outcome.
- Milestone: delivery intent and completion boundary.

The methodology already distinguishes project-specific conventions from portable workflow principles in several places. This should continue as the ecosystem is externalized.

## Release portability

The release methodology should discover the project's actual release/version policy rather than assuming:

- SemVer;
- GitHub Releases;
- lightweight tags;
- a specific tag target;
- a specific changelog format.

The portable release method is:

```text
policy discovery
→ release intent
→ release notes
→ approval
→ publish
→ post-publication validation
```

## Milestone portability

The current intended lifecycle is:

```text
issues complete
≠
milestone complete
```

A delivery milestone becomes eligible for closure only after:

1. it is a delivery/phase milestone, not the persistent Backlog;
2. its intended release has been published and validated;
3. it has zero open issues at the time of the closure check.

This is a workflow decision, not merely a historical repository convention.

---

# 9. Phase H — Architecture artifact ecosystem

`my-architecture-laboratory` now supports more than a single monolithic architecture document in practice.

The current `useOrbit` example demonstrates a useful parent/child architecture relationship.

### Parent

**Organization Identity & Authentication Architecture**

Owns the macro architecture:

- organization provisioning;
- membership and roles;
- authentication;
- 2FA;
- organization-wide 2FA enforcement;
- reset/recovery;
- tenancy/security relationships.

### Child

**Dormant User & Invitation Lifecycle Architecture**

Owns the implementation-near architecture for the shared dormant-User/invitation mechanism:

- dormant User state;
- token lifecycle;
- two entry points;
- acceptance/concurrency;
- revoke/expiry;
- policy-only isolation;
- notifications;
- concrete backend/frontend/test ownership.

This parent/child relationship is currently an **observed working pattern**, not yet a formal rule of `my-architecture-laboratory`.

Do not modify the architecture skill solely because this pattern exists once. Look for repeated evidence in future architecture work before generalizing it.

---

# 10. Phase I — Use architecture as upstream input to planning

The intended lifecycle is increasingly:

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

`my-feature-planning` should consume approved architectural decisions without re-litigating them.

The skills already distinguish:

- current-state facts;
- locked decisions;
- derived constraints;
- open implementation details.

The roadmap should preserve that separation as stack adapters are introduced.

A stack adapter should not quietly turn an implementation convention into a product decision.

---

# 11. Phase J — Validate installation and distribution

Phase A's completion already covered the parts that would otherwise sit here: a fresh-clone install into a clean environment, verified discovery/loading, verified `rules/*.md` references, and confirmation that the skills don't depend on the original `useOrbit` filesystem layout. Do not redo that verification — see Phase A's completion criteria and the root `README.md`'s "Current portability status" for what was already established.

What remains open:

1. validate that the repository structure is compatible with the current skills.sh ecosystem;
2. only then prepare for public distribution.

The repository should remain useful even before public publication.

The first goal is:

> **portable source of truth**

not:

> **public marketplace package**

---

# 12. Phase K — Prepare for reusable publication

Once cross-stack validation is credible, prepare the repository for wider reuse.

Potential work:

- polished repository README;
- per-skill README or usage notes where helpful;
- installation examples;
- contribution guidance;
- versioning/release policy for the skill repository itself;
- examples showing portable methodology vs stack adapters;
- documentation of supported adapters;
- changelog/release notes for major workflow changes.

README documentation for **consuming, refreshing, and contributing** skills specifically is deferred until Phase B's operational lifecycle has actually been exercised on real `useOrbit` work — writing it earlier would mean documenting a lifecycle that hasn't been lived yet.

Only at this stage should we decide how much of the project history and development story belongs in public documentation.

---

# 13. Future ecosystem shape

The target is not simply a skills repository. It is a small ecosystem of interoperable engineering methods.

```text
agentic-engineering
│
├── Portable engineering methods
│   ├── my-feature-planning
│   ├── my-architecture-laboratory
│   └── my-git-workflow
│
├── Stack adapters (shape and names to emerge from evidence, not predefined)
│   ├── framework/ORM implementation conventions (e.g. Laravel/Eloquent/Inertia)
│   ├── frontend build/runtime conventions (e.g. Nuxt/Vite)
│   └── platform/hosting conventions (e.g. Supabase/Vercel)
│
└── Examples / project integrations
    ├── useOrbit
    └── AI training application
```

Eventually, an agent working on a project should be able to assemble the appropriate capabilities rather than receiving one giant, stack-bound skill.

Conceptually:

```text
project context
      +
portable engineering methodology
      +
stack adapter
      +
project-specific decisions
      ↓
agentic engineering workflow
```

---

# 14. Working principles for the roadmap

## Evidence before abstraction

Do not generalize a rule merely because it sounds reusable. Prefer repeated evidence from real projects.

## Consume for real before formalizing the lifecycle

The consume/use/contribute/refresh relationship between `agentic-engineering` and its consumers should be documented from lifecycle events that actually happened, not designed in advance and then exercised to match the design.

## Core before adapter

When a rule can be expressed without knowing the framework, keep it in the portable methodology.

When it requires a framework or technology, consider a stack adapter.

When it is unique to one repository or product, keep it project-specific.

## Human decisions remain visible

Architecture decisions, product calls, release approval, milestone closure, and other meaningful mutations should remain explicit rather than being hidden behind automation.

## Verification is part of the workflow

A successful command is not proof that the intended state exists. Re-fetch and validate when the workflow mutates durable external state.

## Don't overfit to useOrbit

`useOrbit` is the first source of evidence, not the definition of the standard.

## Don't optimize for publication before portability

The public/reusable version should emerge from proven cross-project methodology rather than from premature packaging decisions.

---

# 15. Current status

## Completed

- [x] Three core local skills developed and repeatedly used on `useOrbit`.
- [x] Planned vs discovered work model established in feature planning.
- [x] Portable issue-title convention extracted from project-specific title history.
- [x] Release methodology extracted from repository release evidence.
- [x] Milestone description guidance extracted and later extended with an explicit completion lifecycle.
- [x] Release → milestone completion lifecycle established.
- [x] Phase milestone historical state migrated so completed delivery milestones are closed while Backlog remains open.
- [x] Architecture reconstruction completed for Organization Identity & Authentication.
- [x] Parent/child architecture artifact pattern successfully demonstrated.
- [x] `agentic-engineering` GitHub repository created.
- [x] Local externalization pass (2026-08-22): all three skills copied into `agentic-engineering` from the untracked, local `useOrbit/.claude/skills/` originals; `architecture-laboratory` renamed to `my-architecture-laboratory` (name, invocation, and prose references only); one literal `useOrbit` reference in the architecture template's footer replaced with a `{{Project}}` placeholder; structural and referential fidelity verified against the `useOrbit` originals (diffed, cross-skill `rules/`/`references/` links resolved). Root `README.md` written. `useOrbit` originals left untouched as rollback source.
- [x] Publication + GitHub install/load verification pass (2026-08-22): the local externalization committed as one coherent commit and pushed to `main` (`fe5bd297908b1245b5670341eb3ac0a5253b149a`), independently confirmed via `git ls-remote` against the GitHub URL itself. All three skills then verified installable and loadable from that exact commit: a fresh `git clone` of the GitHub repo into a scratch location, then copying each of the three skill directories from that clone into an isolated project's `.claude/skills/<name>/` (outside both `useOrbit` and the working `agentic-engineering` checkout). Neither that isolated project nor personal `~/.claude/skills/` held any pre-existing copy of the three skills beforehand — the `useOrbit` originals still existed on the machine, just outside both of those discovery scopes. Claude Code discovered all three by external name, loaded each `SKILL.md`, and read verbatim, distinguishing content out of their `rules/`/`references/` files, including confirming the `my-architecture-laboratory` rename and the `{{Project}}` footer fix survived the round-trip. No packaging (`marketplace.json`/`plugin.json`) was added to force the test — none exists, and none is claimed to. **Phase A is now complete.**
- [x] Phase B consumption + first real use (2026-08-23): all three canonical skills consumed from `agentic-engineering` @ `12d9c1df75dde5fb1d944b62b0679c1e211137a4` into gitignored `useOrbit/.claude/skills/`, with upstream commit provenance recorded locally alongside the snapshots. The pre-Phase-A, independently-maintained originals were moved to `.claude/_rollback/pre-phase-b-skills/`, outside active skill discovery, and preserved rather than deleted. The canonical `my-feature-planning` snapshot was then used on genuine, already-intended `useOrbit` work — a discovered-work investigation into 2FA login precedence, resolved as intended behavior, and a drafted-then-created issue for the remaining actionable finding — producing [useOrbit#299](https://github.com/elieandraos/useOrbit/issues/299). No upstream contribution was warranted from this pass; that outcome is recorded rather than left silent. **Phase B's refresh/update-and-verification requirement remains unmet — this is real use, not yet a completed lifecycle.**

## In progress / next

Phase B is underway, not complete. Consumption, local provenance, first genuine real use (`useOrbit#299`), and retirement of the old copies from active discovery are done — see "Completed" above. What remains open: a genuine refresh/update-and-verification cycle (pulling and verifying an updated upstream skill snapshot), which has not happened because no genuine upstream skill-content update exists yet to refresh from — one will not be manufactured to close this out artificially. Real use continues through `useOrbit#299`; the applicable canonical workflow (`my-git-workflow`) is used for that issue's implementation only once separately authorized — Phase B does not authorize implementation on its own. Phase C (classification) stays blocked until the refresh lifecycle has actually been observed, not merely until consumption and one round of use are done.

## Future

- [x] Consume the canonical skills into `useOrbit/.claude/skills/` for real work. (Phase B — completed 2026-08-23.)
- [x] Track upstream commit provenance for consumed copies, in a format decided from real need. (Phase B — completed 2026-08-23.)
- [ ] Observe and record a genuine refresh/update-and-verification cycle from actual `useOrbit` work. (Phase B.)
- [x] Retire the old, independently-maintained `useOrbit` skill copies from active use. (Phase B — completed 2026-08-23.)
- [ ] Classify the three skills' content into portable / Laravel-Inertia / `useOrbit`-specific. (Phase C.)
- [ ] Extract a Laravel/Inertia adapter, only if the Phase C evidence justifies it (Phase D).
- [ ] Apply the same methodologies to the Nuxt/Vite/Supabase/Vercel project (Phase E, later).
- [ ] Compare `useOrbit` and Project B and record real portability differences (Phase E, later).
- [ ] Synthesize both into the general adapter boundary (Phase F).
- [ ] Validate skills.sh compatibility (Phase J).
- [ ] Prepare public reusable releases, including the deferred consume/refresh/contribute README docs (Phase K).

---

# 16. Immediate next move

Phase A is complete. Phase B is underway, not complete: the three canonical skills are consumed
into `useOrbit/.claude/skills/` from `agentic-engineering` @ `12d9c1df75dde5fb1d944b62b0679c1e211137a4`,
with provenance recorded locally, and the canonical `my-feature-planning` snapshot has already been
used on genuine `useOrbit` work, producing `useOrbit#299`.

The next task is still Phase B, not Phase C and not Project B:

> **Continue real use through `useOrbit#299`** — implementation of that issue happens through the
> applicable canonical workflow (`my-git-workflow`) only once separately authorized; Phase B's real-use
> requirement does not itself authorize writing code. **Observe a genuine refresh/update-and-verification
> cycle when one is actually available** — pull an updated upstream skill snapshot into `useOrbit` and
> verify it still works as a consumer — but only once a genuine upstream skill-content update exists; do
> not manufacture an upstream change to close this out artificially. Record any real upstream contribution
> that real use warrants, understanding that contribution alone, without an observed refresh/verification
> cycle, does not complete Phase B.

Phase C (classifying the three skills' content into portable / Laravel-Inertia / `useOrbit`-specific)
remains blocked until the refresh/update-and-verification lifecycle above has actually been observed —
not merely once consumption and one round of real use are done. Applying the methodologies to the
Nuxt/Vite/Supabase/Vercel project (Project B) comes later still, after Phase C.
