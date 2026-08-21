# Agentic Engineering Roadmap

## Purpose

`agentic-engineering` is the home for a growing, portable system of agentic software-engineering methodologies.

The goal is not to collect prompts for one repository or one framework. The goal is to build reusable engineering workflows that can operate across projects and technology stacks, while keeping stack-specific implementation knowledge and project-specific conventions out of the portable core.

The system is being developed from real use rather than designed in a vacuum. `useOrbit` is the first proving ground. A second, materially different application stack will provide the next portability test.

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
- [x] Each skill can be installed/loaded from the GitHub repository. (2026-08-22, independently verified via a fresh `git clone` of `main` @ `fe5bd297...` into an isolated project directory outside both `useOrbit` and this checkout — see "Current status" below.)
- [x] No skill depends on files that only exist inside `useOrbit` unless that dependency is explicitly documented as project-specific. (Findings recorded in root `README.md`, "Current portability status".)

**Phase A is complete.**

---

# 3. Phase B — Prove the skills outside their birthplace

The second step is not to generalize everything immediately. It is to **test portability**.

The first proving ground is:

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

The second proving ground is a materially different application currently entering development at the user's day job.

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

Run the same portable methodologies against both projects and observe where they diverge.

Examples of questions to learn from:

- Does feature classification remain useful without Laravel resource conventions?
- Does architecture reconstruction need anything inherently Laravel-specific?
- Does issue planning depend on Eloquent-style CRUD assumptions?
- What parts of the Git workflow are truly GitHub-level versus repository-specific?
- Which implementation patterns belong in a stack skill rather than in the core methodology?
- Which rules survive unchanged across Laravel/Inertia and Nuxt/Supabase/Vercel?

## Important rule

Do not generalize from one project when a second project can provide evidence.

Project B is not just another application. It is the first deliberate portability test.

---

# 4. Phase C — Extract stack adapters

Only after using the workflows on both projects should we decide what deserves to become a stack adapter.

Potential future adapter family:

```text
my-laravel-patterns
my-nuxt-patterns
my-supabase-patterns
my-vercel-patterns
```

These names are provisional. They should not be created merely because they sound useful.

A stack skill should be created when repeated implementation evidence shows that a set of conventions is:

1. technology-specific;
2. reusable across multiple features;
3. useful to an agent during implementation;
4. distinct from product/domain rules.

### Example boundary

Core methodology:

> Walk the resource lifecycle, resolve authorization, identify persistence changes, determine tests, then sequence backend and frontend work appropriately.

Laravel adapter:

> Use migrations, Eloquent models, policies, FormRequests, API Resources, Actions, routes, Pest, and the project's established Vue/Inertia patterns.

Nuxt/Supabase adapter:

> Use Supabase RLS, composables, server routes, Nuxt data-fetching patterns, Vercel environment conventions, and the project's chosen validation/testing stack.

The methodology should not need to know which one it is using.

---

# 5. Phase D — Establish the adapter boundary

At this stage, compare the two projects and explicitly separate:

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

# 6. Phase E — Harden Git / issue / release portability

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

# 7. Phase F — Architecture artifact ecosystem

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

# 8. Phase G — Use architecture as upstream input to planning

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

# 9. Phase H — Validate installation and distribution

Once the skills are stable in GitHub:

1. install each skill from the repository in a clean environment;
2. verify discovery and loading behavior;
3. verify references to `rules/*.md` remain valid;
4. verify the skills do not rely on the original `useOrbit` filesystem layout;
5. validate that the repository structure is compatible with the current skills.sh ecosystem;
6. only then prepare for public distribution.

The repository should remain useful even before public publication.

The first goal is:

> **portable source of truth**

not:

> **public marketplace package**

---

# 10. Phase I — Prepare for reusable publication

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

Only at this stage should we decide how much of the project history and development story belongs in public documentation.

---

# 11. Future ecosystem shape

The target is not simply a skills repository. It is a small ecosystem of interoperable engineering methods.

```text
agentic-engineering
│
├── Portable engineering methods
│   ├── my-feature-planning
│   ├── my-architecture-laboratory
│   └── my-git-workflow
│
├── Stack adapters
│   ├── my-laravel-patterns
│   ├── my-nuxt-patterns
│   ├── my-supabase-patterns
│   └── my-vercel-patterns
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

# 12. Working principles for the roadmap

## Evidence before abstraction

Do not generalize a rule merely because it sounds reusable. Prefer repeated evidence from real projects.

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

# 13. Current status

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
- [x] Publication + GitHub install/load verification pass (2026-08-22): the local externalization committed as one coherent commit and pushed to `main` (`fe5bd297908b1245b5670341eb3ac0a5253b149a`), independently confirmed via `git ls-remote` against the GitHub URL itself. All three skills then verified installable and loadable from that exact commit: a fresh `git clone` of the GitHub repo into an isolated project directory (outside both `useOrbit` and the working `agentic-engineering` checkout, with no pre-existing copy of any of the three skills anywhere else on the machine) was used to populate a project-level `.claude/skills/`; Claude Code discovered all three by external name, loaded each `SKILL.md`, and read verbatim, distinguishing content out of their `rules/`/`references/` files, including confirming the `my-architecture-laboratory` rename and the `{{Project}}` footer fix survived the round-trip. No packaging (`marketplace.json`/`plugin.json`) was added to force the test — none exists, and none is claimed to. **Phase A is now complete.**

## In progress / next

Phase A is done — see "Completed" above. Nothing currently in progress.

## Future

- [ ] Apply the same methodologies to the Nuxt/Vite/Supabase/Vercel project.
- [ ] Compare the two projects and record real portability differences.
- [ ] Extract stack adapters only where repeated evidence justifies them.
- [ ] Define the eventual project/stack adapter boundary from that evidence.
- [ ] Validate skills.sh compatibility and installation conventions.
- [ ] Prepare public reusable releases.
- [ ] Publish the stable skill family and appropriate adapters.

---

# 14. Immediate next move

Phase A is complete: the three skills are published on GitHub `main` and independently verified
installable/loadable from that commit by their external names.

The next task is the first Phase B evidence-gathering step:

> **Apply `my-feature-planning`, `my-git-workflow`, and `my-architecture-laboratory` to Project B —
> the Nuxt/Vite/Supabase/Vercel AI training application — and record where they diverge from how
> they were actually used on `useOrbit`.**

This is not a redesign pass. The goal is observation: run the same portable methodologies against a
materially different stack and let repeated evidence, not assumption, decide what's actually
portable versus Laravel/Vue-specific.

The system should evolve by proving its portability one real project at a time.
