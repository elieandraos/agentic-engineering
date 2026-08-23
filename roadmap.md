# Agentic Engineering Roadmap

## Purpose

`agentic-engineering` is the home for a growing, portable system of agentic software-engineering methodologies.

The goal is not to collect prompts for one repository or one framework. The goal is to build reusable engineering workflows that can operate across projects and technology stacks, while keeping stack-specific implementation knowledge and project-specific conventions out of the portable core.

The system is being developed from real use rather than designed in a vacuum. `useOrbit` is the first proving ground, and is now becoming the system's first real consumer: the canonical skills need to be consumed and used for genuine `useOrbit` work before any further generalization.

This document is the **near-term Agentic Engineering roadmap** — four active phases covering externalizing the portable core, operating the `useOrbit` consumer relationship, classifying the mature custom skill ecosystem, and deciding whether a stack layer is justified. It is not a speculative plan for the entire eventual ecosystem; longer-range ideas that aren't yet committed work are kept in "Future directions" below, not in the phase sequence.

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

The near-term model is a layered system:

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
                     CUSTOM STACK LAYER
                    (Laravel / Vue / Inertia)
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

### Custom stack layer

Technology-specific implementation knowledge that is genuinely owned/authored by this ecosystem — currently centered on the Laravel/Vue/Inertia stack `useOrbit` runs on, e.g. `my-laravel-patterns`, `my-phpstorm-conventions`. This is distinct from **external first-party capabilities** such as Laravel Boost's `laravel-best-practices` and `pest-testing`: upstream dependencies the custom stack layer may compose with, but never owns, absorbs, renames, or duplicates.

### Project-specific input

Things that belong to one product or repository:

- domain model and business decisions;
- repository conventions;
- deployment/environment choices;
- naming dialects;
- existing architecture decisions;
- project-specific release or issue conventions.

The exact stack-layer boundary is intentionally **not designed yet**. Phase C has classified the existing evidence (see `phase-discovery.md`); Phase D now decides what — if anything — to extract, refine, or leave unchanged. Stacks beyond Laravel/Vue/Inertia are a possible future direction, not part of this near-term roadmap.

---

# 2. Phase A — Externalize and prove the mature portable core

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

# 3. Phase B — Establish and operate the real `useOrbit` consumer relationship

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
- **A genuine skill-content refresh/update-and-verification cycle remains an open observational criterion of this phase — not a blocking dependency for the rest of the roadmap.** Phase B's own completion still depends on real `useOrbit` work producing this full cycle:

  1. real work warrants a canonical skill improvement;
  2. the canonical source (`agentic-engineering`) is updated;
  3. the consuming local copies in `useOrbit` are refreshed from the updated canonical source;
  4. the refreshed skill is verified in `useOrbit` as a consumer;
  5. the lifecycle evidence is recorded.

  A documentation-only repository commit does not satisfy this criterion. If real `useOrbit` work surfaces a fix or improvement worth contributing upstream, record it when it happens; if no such change is warranted, recording that outcome is itself sufficient — contribution is conditional on what real use actually produces, not a checklist item that has to fire. Document the lifecycle as it is actually exercised during real feature work — do not manufacture a change to a skill merely to rehearse it, and do not write the lifecycle down before it has actually happened. Normal `useOrbit` development and Phase C both proceed independently of this criterion; it is satisfied opportunistically whenever genuine skill-content evolution actually occurs, never manufactured to unlock other work.

## Completion criteria

- [x] Canonical skill copies are consumed into `useOrbit/.claude/skills/` and used for real, in-progress `useOrbit` work (not a synthetic or throwaway test). (2026-08-23 — consumed from `agentic-engineering` @ `12d9c1df75dde5fb1d944b62b0679c1e211137a4`; the canonical `my-feature-planning` snapshot used on a genuine discovered-work investigation and planning pass, producing [useOrbit#299](https://github.com/elieandraos/useOrbit/issues/299) — the first durable consumer artifact of this relationship.)
- [x] The active local snapshots are traceable to their exact upstream commit, in whatever provenance format the real work shows is adequate; the snapshots remain uncommitted, and the provenance record may remain local alongside them. (2026-08-23 — consumed at commit `12d9c1df75dde5fb1d944b62b0679c1e211137a4`, recorded locally in `useOrbit/.claude/skills/UPSTREAM_PROVENANCE.md`.)
- [ ] At least one genuine refresh/update-and-verification cycle has been observed and recorded from actual `useOrbit` work: an updated skill snapshot pulled from upstream and verified as a consumer. (Not yet met — no newer upstream skill-content update or genuinely updated skill snapshot exists yet to refresh from. The subsequent commit `c09f15f9127317cc0faf79f03ff5072441c22d04` changed documentation only; it does not trigger or satisfy this criterion. This stays open and outstanding as a Phase B observational criterion; it does not block Phase C or normal `useOrbit` development.)
- [x] The old, independently-maintained `useOrbit` skill copies are retired from active use. (2026-08-23 — moved to `.claude/_rollback/pre-phase-b-skills/`, outside `.claude/skills/` discovery scope; preserved as rollback material, not deleted.)
- [x] The first consumer pass warranted no upstream skill contribution — recorded rather than left silent. (2026-08-23.)

---

# 4. Phase C — Classify the mature custom skill ecosystem

## Objective

This is a deep evidence-gathering and classification phase, **not** an extraction or restructuring phase. Its scope is the mature custom `my-*` ecosystem as it actually exists and is actually used in `useOrbit`, including:

- `my-feature-planning`
- `my-git-workflow`
- `my-architecture-laboratory`
- `my-laravel-patterns`
- `my-phpstorm-conventions`
- any other genuinely owned, mature custom `my-*` skill discovered during inventory

## Method

Classification happens below whole-skill granularity. Inspect rules, references, responsibilities, dependencies, and interactions within and across skills, along with relevant `useOrbit` project memory and other project evidence — not just each skill's top-level description.

Distinguish at least:

1. **portable methodology** — survives independent of stack or project;
2. **reusable custom Laravel/PHP/Vue/Inertia/tooling/convention knowledge** — technology-specific, genuinely authored by this ecosystem, not `useOrbit`-specific;
3. **`useOrbit`-specific project knowledge** — belongs to this one product/repository;
4. **external first-party capabilities** — upstream dependencies such as Laravel Boost's `laravel-best-practices` and `pest-testing`. These may compose with custom skills but are not extraction targets, and must not be absorbed, renamed, duplicated, or presented as Agentic-Engineering-owned.

## Deliverable

An evidence-backed classification report/inventory and boundary model covering:

- clear classifications;
- mixed rules that may need separation;
- duplicated or misplaced knowledge;
- external dependencies;
- existing seams;
- candidate stack-layer capabilities;
- unresolved cases and open questions.

## Important rule

This analysis produces evidence, not restructuring. Rewritten skills, file movement, or a predefined adapter tree are **not** part of Phase C completion — that decision belongs to Phase D. Do not pre-sort content into an adapter shape while classifying; classify first, decide what to build second.

## Completion criteria

- [x] Inventory and classification performed below whole-skill level — rules, references, responsibilities, dependencies, and interactions, plus relevant `useOrbit` project memory, not just top-level skill descriptions. (`phase-discovery.md`, Iteration 1, §1–§9.)
- [x] Both custom stack candidates (`my-laravel-patterns`, `my-phpstorm-conventions`) deep-dived for reusable-extraction readiness. (`phase-discovery.md`, Iteration 2, §10–§12.)
- [x] All three canonical portable methodology skills (`my-architecture-laboratory`, `my-feature-planning`, `my-git-workflow`) deep-dived for readiness. (`phase-discovery.md`, Iteration 3, §14–§21.)
- [x] A final synthesis consolidating Iterations 1–3 into an evidence-backed readiness disposition per skill, including independent re-verification of load-bearing claims against live sources rather than restatement of the iterations' own text. (`phase-discovery.md`, "Phase C Synthesis — Current Disposition.")
- [x] Deliverable produced covering clear classifications, mixed rules needing separation, duplicated/misplaced knowledge, external dependencies, existing seams, candidate stack-layer capabilities, and unresolved cases/open questions. (`phase-discovery.md`, Synthesis §"Skill-by-skill synthesis," §"Mixed material synthesis," §"External capability boundary," §"Phase D entry conditions," §"Phase C conclusion.")
- [x] No restructuring performed as part of this phase — classification and judgment only; no skill, `useOrbit` file, or this roadmap was modified to produce the discovery or synthesis. (Stated method, `phase-discovery.md` Synthesis preamble.)

**Phase C is complete.** Full findings, scores, and supporting evidence live in `phase-discovery.md` — that document, not this roadmap, is the durable Phase C evidence artifact. Headline results, at roadmap altitude:

- The mature custom skill ecosystem — the five `my-*` skills plus the independently-discovered `content-backlog` — is now inventoried and classified below whole-skill level.
- The architecture → planning → Git/delivery three-skill lifecycle is confirmed a sound decomposition across three independent passes of increasing depth, with only one narrow, disclosure-shaped boundary gap found (`plan.md` section-pruning ownership).
- Targeted refinement needs were found in all three portable methodology skills: `my-git-workflow` (7.3/10) and `my-architecture-laboratory` (6.8/10) sit closest to clean; `my-feature-planning` (6.3/10) is sound overall but carries one heavily mixed file plus a smaller `SKILL.md` leak.
- Of the two custom stack candidates, `my-phpstorm-conventions` (8.2/10) is the strongest — zero product-domain leakage found across two full reads, only disclosure gaps remain. `my-laravel-patterns` (5.8/10) requires substantial refinement before reusable extraction: an undisclosed test-macro dependency, an active conflict with Laravel Boost's own guidance, a broken worked example, and a self-contradiction with a co-loaded sibling skill.
- Mixed stack/project material requiring separation was identified across the ecosystem, most heavily in `my-feature-planning/rules/resource-feature-checklist.md`, the ecosystem's densest concentration of interleaved generic and `useOrbit`-specific content — evidence across all three iterations agrees this needs a rewrite, not a mechanical extraction.
- Laravel Boost and other first-party capabilities remain confirmed external throughout — composed with, never absorbed, renamed, or duplicated.
- `content-backlog` is genuinely owned and mature but does not confidently fit any of the three defined layers; it is deliberately left unresolved and outside the current Phase D stack scope, consistent with this roadmap's own prior framing (§9, "Future directions").

---

# 5. Phase D — Extract or refine the custom Laravel/Vue/Inertia stack layer, if justified

## Objective

Phase D acts on Phase C's evidence — it does not automatically produce a singular adapter skill. Phase C's classification now exists in full (`phase-discovery.md`); Phase D decides what, if anything, that evidence justifies. No Phase D implementation decision has been made yet — this section still describes the space of legitimate outcomes, not a chosen one. `phase-discovery.md` is the evidence source Phase D should reason from; it is not reconstructed here.

## Evidence-supported outcomes

Any of the following are legitimate outcomes, depending on what Phase C actually finds:

- extracting one reusable stack capability;
- retaining several cooperating custom stack skills;
- combining or splitting skills;
- refining `my-laravel-patterns`;
- refining `my-phpstorm-conventions`;
- returning project-specific material to `useOrbit`;
- leaving some skills unchanged;
- deciding that no further extraction is justified yet.

## Constraints

Laravel Boost remains external and unchanged — it is a dependency the custom stack layer may compose with, never an extraction target. Do not prescribe a generic adapter folder structure, exact package names, or a one-skill decomposition before Phase C provides evidence.

### Illustrative boundary (methodology vs. stack knowledge)

Core methodology:

> Walk the resource lifecycle, resolve authorization, identify persistence changes, determine tests, then sequence backend and frontend work appropriately.

Stack knowledge:

> Use migrations, Eloquent models, policies, FormRequests, API Resources, Actions, routes, Pest, and the project's established Vue/Inertia patterns.

The methodology should not need to know which stack it is using.

---

# 6. Repository organization direction

This is a conceptual direction for how the repository could eventually be organized — **not** an implemented or mandatory structure:

```text
agentic-engineering/
├── README.md
├── roadmap.md
└── skills/
    ├── portable-core/
    │   └── current portable custom skills
    ├── stack-adapters/
    │   └── laravel-vue-inertia/
    │       └── custom stack capabilities
    └── project-specific/
        └── useOrbit/
            └── project-specific durable material, if and when it belongs here
```

Guardrails:

- this is structural direction, not a requirement to create these directories now;
- `portable-core` is a conceptual grouping, not a reason to redesign skills during Phase C;
- `laravel-vue-inertia` is a conceptual namespace, not a predetermined decomposition;
- Phase C classifies rather than restructures;
- Phase D determines whether structural changes are warranted;
- `project-specific/useOrbit` must not be populated speculatively;
- classifying project-specific knowledge does not mean it belongs in this repository.

The root `README.md` may eventually explain the full planning-through-learning workflow, with layer-level READMEs added when the real structure warrants them — that documentation is not written yet.

---

# 7. Current methodology and observed patterns

These describe methodology and patterns already in use. They're recorded here as current state and evidence for Phase C to classify — not as future phases.

## Git / issue / release / milestone methodology

`my-git-workflow` has already evolved beyond simple Git commands. Its current conceptual lifecycle:

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

It treats these as distinct artifacts and lifecycle events:

- Commit: technical change/history.
- Issue: unit of planned/discovered work.
- PR: integrated engineering change.
- Release: shipped outcome.
- Milestone: delivery intent and completion boundary.

Release methodology discovers the project's actual release/version policy rather than assuming SemVer, GitHub Releases, lightweight tags, a specific tag target, or a specific changelog format:

```text
policy discovery
→ release intent
→ release notes
→ approval
→ publish
→ post-publication validation
```

Milestone methodology treats "issues complete" as distinct from "milestone complete." A delivery milestone becomes eligible for closure only after:

1. it is a delivery/phase milestone, not the persistent Backlog;
2. its intended release has been published and validated;
3. it has zero open issues at the time of the closure check.

This is a workflow decision, not merely a historical repository convention.

## Architecture artifact pattern

`my-architecture-laboratory` supports more than a single monolithic architecture document in practice. The `useOrbit` **Organization Identity & Authentication Architecture** (parent — owning organization provisioning, membership/roles, authentication, 2FA, organization-wide 2FA enforcement, reset/recovery, and tenancy/security relationships) and **Dormant User & Invitation Lifecycle Architecture** (child — owning the implementation-near dormant-User/invitation mechanism: state, token lifecycle, entry points, acceptance/concurrency, revoke/expiry, policy-only isolation, notifications, and concrete backend/frontend/test ownership) demonstrate a useful parent/child relationship.

This parent/child pattern is currently an **observed working pattern awaiting repetition**, not yet a formal rule of `my-architecture-laboratory`. Do not modify the architecture skill solely because this pattern exists once — look for repeated evidence in future architecture work before generalizing it.

---

# 8. Working principles for the roadmap

## Evidence before abstraction

Do not generalize a rule merely because it sounds reusable. Prefer repeated evidence from real projects.

## Consume for real before formalizing the lifecycle

The consume/use/contribute/refresh relationship between `agentic-engineering` and its consumers should be documented from lifecycle events that actually happened, not designed in advance and then exercised to match the design.

## Core before stack layer

When a rule can be expressed without knowing the framework, keep it in the portable methodology.

When it requires a framework or technology, consider the custom stack layer.

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

`my-feature-planning` consumes approved architectural decisions without re-litigating them. The skills already distinguish current-state facts, locked decisions, derived constraints, and open implementation details — that separation should be preserved as the custom stack layer is considered. A stack layer should not quietly turn an implementation convention into a product decision.

## Human decisions remain visible

Architecture decisions, product calls, release approval, milestone closure, and other meaningful mutations should remain explicit rather than being hidden behind automation.

## Verification is part of the workflow

A successful command is not proof that the intended state exists. Re-fetch and validate when the workflow mutates durable external state.

## Don't overfit to useOrbit

`useOrbit` is the first source of evidence, not the definition of the standard.

## Don't optimize for publication before portability

The public/reusable version should emerge from proven cross-project methodology rather than from premature packaging decisions.

---

# 9. Future directions

These are possibilities worth keeping in view — not phases, dependencies, commitments, or a prescribed order:

- Project B as a possible later cross-stack proving ground;
- multi-project comparison to refine the portable / stack / project boundary;
- additional stack or platform capabilities when repeated needs appear;
- improvements to consumption, refresh, contribution, packaging, or installation when real use demonstrates a need;
- skills.sh compatibility;
- public distribution, reusable publication, versioning, and contribution guidance;
- continued refinement of architecture, planning, Git, issue, release, and delivery methodologies;
- `content-backlog` as a possible Agentic Engineering capability, potentially independent of stack work and possibly worth exploring before Project B if real priorities justify it.

---

# 10. Current status

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
- [x] Phase B consumption + first real use (2026-08-23): all three canonical skills consumed from `agentic-engineering` @ `12d9c1df75dde5fb1d944b62b0679c1e211137a4` into gitignored `useOrbit/.claude/skills/`, with upstream commit provenance recorded locally alongside the snapshots. The pre-Phase-A, independently-maintained originals were moved to `.claude/_rollback/pre-phase-b-skills/`, outside active skill discovery, and preserved rather than deleted. The canonical `my-feature-planning` snapshot was then used on genuine, already-intended `useOrbit` work — a discovered-work investigation into 2FA login precedence, resolved as intended behavior, and a drafted-then-created issue for the remaining actionable finding — producing [useOrbit#299](https://github.com/elieandraos/useOrbit/issues/299), the first durable consumer artifact of this relationship. No upstream contribution was warranted from this pass; that outcome is recorded rather than left silent. **Phase B's refresh/update-and-verification requirement remains unmet — this is real use, not yet a completed lifecycle.**
- [x] Phase C classification + synthesis (2026-08-23): the mature custom `my-*` skill ecosystem (`my-architecture-laboratory`, `my-feature-planning`, `my-git-workflow`, `my-laravel-patterns`, `my-phpstorm-conventions`) plus the independently-discovered `content-backlog` inventoried and classified below whole-skill level across three iterations of increasing depth, then consolidated into a synthesis with independently re-verified, evidence-backed readiness dispositions. The three-skill portable lifecycle is confirmed a sound decomposition; all three portable methodology skills need targeted refinement; `my-phpstorm-conventions` (8.2/10) is the strongest current custom stack candidate and `my-laravel-patterns` (5.8/10) needs substantial refinement before reusable extraction; `resource-feature-checklist.md` is the ecosystem's heaviest mixed stack/project content, requiring a rewrite to separate; Laravel Boost and other first-party capabilities remain confirmed external; `content-backlog` stays deliberately unresolved and outside the current Phase D stack scope. Full evidence: `phase-discovery.md`. **Phase C is now complete.**

## In progress / next

Phase B's consumer relationship is established: consumption, local provenance, first genuine real use (`useOrbit#299`), and retirement of the old copies from active discovery are done — see "Completed" above. What remains open, as an observational criterion rather than a blocking dependency: a genuine refresh/update-and-verification cycle (pulling and verifying an updated upstream skill snapshot), which has not happened because no genuine upstream skill-content update exists yet to refresh from — one will not be manufactured to close this out artificially. Phase C has now surfaced genuine evidence warranting possible canonical skill refinement across all three portable methodology skills (`phase-discovery.md`, "Phase D entry conditions"). If Phase D turns any of that evidence into a real canonical skill-content change, exercising that change through the consume → refresh → verify sequence is a natural opportunity to close this still-open Phase B observation out — but that change has not happened yet, and none is manufactured ahead of a genuine Phase D decision.

Phase C (classifying the mature custom skill ecosystem) is complete — see "Completed" above and `phase-discovery.md` for the full evidence base. Phase D — deciding what, if anything, Phase C's evidence justifies extracting, refining, combining, splitting, or leaving unchanged in the custom stack layer — is now the next active Agentic Engineering phase. No Phase D implementation decision has been made yet.

## Future

- [x] Consume the canonical skills into `useOrbit/.claude/skills/` for real work. (Phase B — completed 2026-08-23.)
- [x] Track upstream commit provenance for consumed copies, in a format decided from real need. (Phase B — completed 2026-08-23.)
- [ ] Observe and record a genuine refresh/update-and-verification cycle from actual `useOrbit` work, completed opportunistically whenever genuine skill-content evolution occurs. (Phase B — open observational criterion, non-blocking.)
- [x] Retire the old, independently-maintained `useOrbit` skill copies from active use. (Phase B — completed 2026-08-23.)
- [x] Classify the mature custom `my-*` skill ecosystem into portable methodology / custom stack knowledge / `useOrbit`-specific knowledge / external first-party capabilities. (Phase C — completed 2026-08-23; see `phase-discovery.md`.)
- [ ] Act on Phase C's evidence — extract, refine, combine, split, or leave the custom stack layer unchanged, only if justified. (Phase D — now the next active work; no implementation decision made yet.)

See "Future directions" above for later, non-committed possibilities (Project B, cross-stack comparison, publication, etc.) — these are not part of this phase sequence.

---

# 11. Immediate next move

Phase A is complete. Phase B has established the real `useOrbit` consumer relationship: the three
canonical skills are consumed into `useOrbit/.claude/skills/` from `agentic-engineering` @
`12d9c1df75dde5fb1d944b62b0679c1e211137a4`, with provenance recorded locally, the old
independently-maintained copies retired from active use, and the canonical `my-feature-planning`
snapshot already used on genuine `useOrbit` work, producing `useOrbit#299` — the first durable
consumer artifact of this relationship. No upstream skill contribution was warranted from that first
pass.

One Phase B criterion remains open as an observational item, not a blocking dependency: a genuine
refresh/update-and-verification cycle, where real work warrants a canonical skill improvement, the
canonical source is updated, the consuming local copies are refreshed, the refresh is verified in
`useOrbit`, and the evidence recorded. This has not happened yet because no genuine upstream
skill-content update exists yet to refresh from — one will not be manufactured to close this out
artificially. Phase C has now surfaced genuine evidence warranting possible canonical skill refinement
across all three portable methodology skills (`phase-discovery.md`, "Phase D entry conditions"). If
Phase D turns any of that evidence into a real canonical skill-content change, exercising that change
through the canonical-source → consumer-refresh → verification sequence is a natural opportunity to
close this Phase B observation out — but that change has not happened yet, and none is manufactured
ahead of a genuine Phase D decision.

`useOrbit#299` remains genuine `useOrbit` work, and its implementation (via `my-git-workflow`, once
separately authorized) is not a prerequisite for anything below — it is normal `useOrbit` development,
which continues independently of the roadmap's phase sequence.

Phase C — classifying the mature custom `my-*` skill ecosystem — is now **complete**. The inventory,
the deep-dives of both custom stack candidates (`my-laravel-patterns`, `my-phpstorm-conventions`) and
all three canonical portable methodology skills (`my-architecture-laboratory`, `my-feature-planning`,
`my-git-workflow`), and the final synthesis with evidence-backed readiness dispositions all live in
`phase-discovery.md`, which this roadmap does not reconstruct or duplicate.

Phase D — deciding what, if anything, Phase C's evidence justifies extracting, refining, combining,
splitting, or leaving unchanged in the custom stack layer — is now the next active Agentic Engineering
phase. No Phase D implementation decision has been made yet. `phase-discovery.md` is the evidence
source Phase D should reason from. Anything in "Future directions" comes later still.
