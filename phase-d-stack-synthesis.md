# Phase D — Stack Synthesis

This document converts `phase-d-stack-discovery.md`'s evidence into decisions. It is a synthesis and
decision artifact only: no skill was edited or created, no `.ai/rules` file was created, no runtime
code was installed, no Composer package was created, and no file was renamed to produce this document.
See `roadmap.md` §5 for Phase D's charter, `phase-discovery.md` for the original Phase C classification,
and `phase-d-stack-discovery.md` for the reconciliation this synthesis acts on.

This document does not restate discovery's evidence ledger, source reads, or per-file Boost-overlap
analysis — it cites `phase-d-stack-discovery.md` by section (`§n`) wherever a decision rests on a
specific finding, and states only the decision.

---

## 0. Locked direction

- The companion is named **`my-laravel-stack`**. Its description must state clearly that it is the
  custom companion for this user's Laravel + InertiaJS + Vue 3 stack.
- Laravel Boost owns the broader Laravel ecosystem baseline. `my-laravel-stack` contains only
  material genuinely additive to Boost.
- `my-phpstorm-conventions` stays a **separate**, **fully deferred** companion — not authored or
  changed in this pass or its implementation sequence. Its already-identified stale finding (the
  missing `getDiagnostics`-absence fallback, discovery §6.3/§10 Tier 2 #5) stays listed as deferred.
- **`.ai/rules` is out of the current direction**, including as an override mechanism for Boost. This
  doesn't declare it permanently invalid — it's simply not part of this target model or sequence.
- **No Composer package.** Not currently needed: the reusable support templates below ship as files
  bundled inside the skill, copied and adapted per project.
- Adopt Boost's `assertModelExists()` default; no custom assertion default. `assertDatabaseHas()`
  remains available only when a test genuinely needs to prove an exact persisted value.
- Don't duplicate Boost's "do not test framework behavior" guidance. Retain only testing guidance
  genuinely specific to our stack implementations and ownership boundaries.

---

## 1. Target model — three layers

| Layer | Owns |
|---|---|
| **Laravel Boost v2.7.0** | The general Laravel/testing baseline: validation, Eloquent mechanics, routing/controller philosophy, migrations, security, style, general assertion-decision guidance (including the `assertModelExists()` default). External dependency — never extracted, renamed, or duplicated. |
| **`my-laravel-stack`** | Portable custom conventions plus reusable implementation building blocks for Laravel + InertiaJS + Vue 3 — the delta genuinely additive to Boost. Travels across this user's projects by copy/reinstall. |
| **The consuming project** | Installed/adapted implementations (e.g. `useOrbit`) and genuinely project-specific decisions (product facts, literals, one-off rules with no cross-project generality claim). |

`my-phpstorm-conventions` is a **separate, deferred tooling companion** (IDE/static-analysis
knowledge) — not a fourth layer of this architecture, and not authored in this pass.

---

## 2. Internal shape of `my-laravel-stack`

Content is classified by purpose, not forced into a single "prose rule" shape:

1. **Conventions and decision guidance** — architectural and coding decisions (Actions, authorization
   attributes, resource boundaries, query conditionals, scopes, test ownership), scoped to only the
   delta not already owned by Boost.
2. **Implementation blueprints** — repeatable implementation shapes the user recreates across
   projects. Enum options belong here. These may remain documented examples where no shared
   executable file exists.
3. **Reusable support templates** — actual code intended to be copied and adapted into consuming
   projects: `QueryFilter`, `Filterable`, and the Inertia testing macros/`TestingServiceProvider`.
   These are part of the stack companion even though they aren't coding-style rules.

Installing a support template requires the agent to inspect the consuming project first, adapt to its
existing structure, expose the change in the normal diff, and never overwrite unrelated existing code.
In `useOrbit`, these implementations already exist, so the later consumer pass (sequence step 4)
compares and verifies them rather than reinstalling them.

---

## 3. File-by-file disposition — `my-laravel-patterns` (→ `my-laravel-stack`)

Legend: **convention** (convention/decision guidance) · **blueprint** (implementation blueprint) ·
**template** (reusable support template, listed separately in §4) · **keep** / **repair** / **narrow**
as before.

| File | Category | Disposition | Reasoning |
|---|---|---|---|
| `SKILL.md` | skill entry | repair | Names the retired Boost skill `pest-testing` instead of `testing-best-practices` (discovery §8.11, Tier 1 #1). State the reusable support templates as an explicit prerequisite the skill assumes exists, not an unstated fact. |
| `rules/actions-pattern.md` | convention | narrow | Boost's `architecture.md`/`routing.md` now name the general Action pattern (discovery §7.2). Trim to the Boost delta: `app/Actions/{Domain}/` location, `{Verb}{Model}Action` naming, fixed `handle()`, fixed `$attributes` param, the FormRequest-derived `@param array{...}` shape algorithm, and the `DB::transaction()`-pure / `->afterCommit()` discipline. |
| `rules/authorization.md` | convention | keep | Zero Boost coverage of the `#[Authorize]` attribute mechanism (discovery §8.4). Keep the portability claim and the 35-controller adoption claim as two distinct pieces of evidence. |
| `rules/eloquent-attributes.md` | convention | narrow | Boost's `eloquent.md` already demonstrates `#[Scope]` mechanics by example. Reduce to the actual delta: the migration-off-`scopeXxx` framing, the `❌ scopeXxx` counter-example, and the Laravel version pin (`^13.7`). |
| `rules/enum-options.md` | blueprint | keep, caveated | No Boost overlap found. Not independently re-audited against live code this pass (discovery §8.2). |
| `rules/factories-and-seeders.md` | convention | keep, caveated | Narrow overlap only (Boost's `test-data.md` endorses `for()` generally; field-derivation/email/date-chaining content has no Boost equivalent). Not independently re-audited this pass (discovery §8.3). |
| `rules/filters-pattern.md` | convention (wiring), referencing templates | repair | The FormRequest → `QueryFilter` → `Filterable` wiring pattern has no Boost overlap. Scrub the live `useOrbit` issue links (`#76`, `#71`) and the arbitrary `paginate(7)` literal (discovery §8.7) — those are `useOrbit` fingerprints, not part of the pattern. `QueryFilter`/`Filterable` themselves ship as reusable support templates (§4), not merely narrated prose. |
| `rules/query-conditionals.md` | convention | repair | Broken example and a dead `TagAttachment::forTaggableType()` citation (discovery §8.10, Tier 1 #3); the underlying `when()`-over-`if` rule needs no content change. |
| `rules/request-normalization.md` | convention | keep, caveated | No Boost overlap (Boost's `validation.md` covers rule syntax, not coercion/defaulting discipline). Checked only for internal consistency in discovery, not against live FormRequest code (discovery §8.8). |
| `rules/resources.md` | convention | repair | Its cited example (`ClientsController.php`) uses `inertia()` throughout while the file's own examples use `Inertia::render()`, inconsistent with it and with `filters-pattern.md` (discovery §6.2, §8.5, Tier 1 #2). Fix is a consistency correction — `Inertia::render()` isn't being declared invalid. The `whenLoaded()`/no-`$with` discipline is unchanged. |
| `rules/testing-strategy.md` | convention | repair + narrow | Defer to Boost for general assertion and framework-testing guidance: adopt `assertModelExists()` as the default for existence checks; don't restate "do not test framework behavior." Retain only the concrete Action/Controller/Policy/Filter/Resource/macro ownership mapping, `assertDatabaseHas()`'s narrowed role (only when a test needs to prove an exact persisted value the resource assertion doesn't cover), and the macro-support prerequisite pointing at §4. |

**`my-phpstorm-conventions`** — deferred in full. Its one known stale finding (`SKILL.md` states the
`getDiagnostics` prerequisite with no fallback for its absence, discovery §6.3/§10, Tier 2 #5) stays
listed here as a deferred repair, not authored in this pass or its sequence.

---

## 4. Reusable support templates

Actual code, bundled inside the skill and copied/adapted into a consuming project rather than
restated as prose:

- **`QueryFilter`** and **`Filterable`** — the base classes underlying `filters-pattern.md`'s wiring.
- **Inertia testing macros** (`TestingServiceProvider`'s five macro registrations: `hasResource`,
  `hasPaginatedResource`, `assertHasResource`, `assertHasPaginatedResource`, `assertHasInertiaFlash`,
  plus the `runningUnitTests()` boot guard).

Installing any of these requires inspecting the consuming project first, adapting to its existing
structure, exposing the change in the normal diff, and never overwriting unrelated existing code.
`useOrbit` already has all of these implemented — the consumer pass (§5, step 4) compares and
reconciles against that existing code rather than reinstalling it.

---

## 5. Implementation sequence

1. Author and rename `my-laravel-patterns` → `my-laravel-stack`, applying the approved repairs,
   Boost-delta narrowing, and the simplified internal classification (§2, §3).
2. Add the generic reusable support templates (§4) and their usage/prerequisite instructions
   atomically with the skill authoring — don't create instructions that reference a template not yet
   present.
3. Refresh the authored skill into `useOrbit`.
4. Compare its templates against `useOrbit`'s existing implementations; reconcile only intentional
   generic differences, and don't overwrite project-specific code.
5. Exercise the refreshed companion during the next genuine Laravel/Inertia implementation task.
6. Reconcile the dossier, README, and roadmap only after that real exercise.

---

## 6. Non-goals and confidence limits

- No skill file, `.ai/rules` file, runtime file, README, roadmap, or dossier was edited or created by
  this document.
- No Composer package — not currently needed (§0).
- `my-phpstorm-conventions` was not touched — fully deferred (§0, §3).
- **One-consumer evidence ceiling**: every classification in this document rests on Laravel Boost's
  installed source plus exactly one real project, `useOrbit` — none of it has been tested against a
  second Laravel+Vue+Inertia codebase.
- `enum-options.md`, `factories-and-seeders.md`, and `request-normalization.md` were not freshly
  re-audited against live `useOrbit` code this pass — their dispositions in §3 carry forward Phase C's
  evidence with that limit stated.
- `useOrbit`'s own removed design-system material (badge tones, breadcrumb rules, etc.) is out of
  `agentic-engineering`'s scope entirely.

---

## Coverage check (self-report)

- [x] Every retained file from `phase-d-stack-discovery.md`'s per-file findings has a disposition in
  §3 or an explicit deferral (`my-phpstorm-conventions`).
- [x] `QueryFilter`/`Filterable` and the Inertia testing macros are classified as reusable support
  templates (§4), not documentation-only patterns.
- [x] Enum options are classified as an implementation blueprint (§3).
- [x] `testing-strategy.md` defers to Boost for general assertion/framework-testing guidance and
  retains only the concrete ownership mapping (§3).
- [x] No `.ai/rules` proposal, five/six-boundary model, or Composer-package analysis remains beyond a
  brief "not currently needed" note (§0, §6).
- [x] The one-consumer evidence limit is stated once (§6).
- [x] Only `phase-d-stack-synthesis.md` changed in `agentic-engineering`. No `useOrbit` file changed —
  only reads were performed there.
