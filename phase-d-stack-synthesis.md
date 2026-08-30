# Phase D — Stack Synthesis

This document converts `phase-d-stack-discovery.md`'s evidence into decisions. It is a synthesis and
decision artifact only: no skill was edited or created, no `.ai/rules` file was created, no runtime
code was installed, no Composer package was created, and no file was renamed to produce this document.
See `roadmap.md` §5 for Phase D's charter, `phase-discovery.md` for the original Phase C classification,
and `phase-d-stack-discovery.md` for the reconciliation this synthesis acts on.

This document does not reproduce discovery's complete evidence ledger, source reads, or per-file
Boost-overlap analysis — it cites `phase-d-stack-discovery.md` by section (`§n`) wherever a decision
rests on a finding already established there. Where a new decision (the two blueprints, the two
recovered conventions, the minimal-test-data ownership call) needed verification discovery didn't
already supply, this pass performed focused fresh reads and states that evidence inline rather than
citing a section that doesn't exist yet.

**This reconciliation pass** was produced against current source, not prior summaries: full reads of
`useOrbit/app/Http/Controllers/Clients/ClientsController.php` and representative non-CRUD controllers
(`ClientsArchiveController`, `ClientsPdfExportController`, `NotesUpdateController`, `TagsController`),
the `Client` Form Requests/Action/Policy/Resource, `tests/Pest.php`, the `tests/Unit`/`tests/Feature`
trees and representative files in each, `app/Providers/TestingServiceProvider.php`, the complete
installed `laravel-best-practices`/`testing-best-practices` (Laravel Boost v2.7.0) rule files relevant
to controllers, migrations, and testing, and the installed Laravel framework source (v13.29.0,
`Illuminate\Support\Fluent`, `Illuminate\Database\Schema\Blueprint`/`ColumnDefinition`, and the four
schema grammars) for the migration-nullability finding in §6.2.

---

## 0. Locked direction

- The companion is named **`my-laravel-stack`**. Its declared stack is **Laravel + InertiaJS + Vue 3 +
  Pest**; its description must state clearly that it is the custom companion for this user's stack.
  **Current verified evidence is strongest for Laravel, Inertia, and Pest** (§3–§6 below all rest on
  fresh reads of real controllers, Actions, Policies, Resources, and Pest tests). Vue 3 is part of the
  locked stack boundary, but this document makes no claim that mature, additive Vue-specific guidance
  has been discovered — none has. Vue content grows later from real Vue implementation work, not from
  this pass's evidence.
- Laravel Boost owns the broader Laravel and Pest ecosystem baseline. `my-laravel-stack` contains only
  material genuinely additive to Boost.
- `my-phpstorm-conventions` stays a **separate**, **fully deferred** companion — not authored or
  changed in this pass or its implementation sequence. Its already-identified stale finding (the
  missing `getDiagnostics`-absence fallback, discovery §6.3/§10 Tier 2 #5) stays listed as deferred.
- **`.ai/rules` is out of the current direction**, including as an override mechanism for Boost. This
  doesn't declare it permanently invalid — it's simply not part of this target model or sequence. Do
  not reintroduce it.
- **No Composer package.** Not currently needed: the reusable support templates below ship as files
  bundled inside the skill, copied and adapted per project.
- Adopt Boost's `assertModelExists()` default; no custom assertion default. `assertDatabaseHas()`
  remains available only when a test genuinely needs to prove an exact persisted value.
- Boost's `endpoint-tests.md`/`review.md` fully own the general "which layer owns which case"
  de-duplication principle (verified: endpoint-tests.md's "Which Layer Owns Which Case" section, review.md's
  matching checklist items) and `test-data.md` fully owns record-level test-data minimalism (§5). Don't
  restate either. Retain only the concrete Action/Controller/Policy/Filter/Resource/Model class-taxonomy
  ownership mapping this stack actually uses, and the narrow attribute-level test-data delta (§5).

---

## 1. Target model — three layers

| Layer | Owns |
|---|---|
| **Laravel Boost v2.7.0** | The general Laravel/testing baseline: validation, Eloquent mechanics, resource/CRUD controller organization, thin-controller and FormRequest-boundary philosophy, migrations, layer-ownership test de-duplication, record-level test-data minimalism, security, style, general assertion-decision guidance (including the `assertModelExists()` default). External dependency — never extracted, renamed, or duplicated. |
| **`my-laravel-stack`** | Portable custom conventions plus reusable implementation building blocks for Laravel + InertiaJS + Vue 3 + Pest — the delta genuinely additive to Boost. Travels across this user's projects by copy/reinstall. |
| **The consuming project** | Installed/adapted implementations (e.g. `useOrbit`) and genuinely project-specific decisions (product facts, literals, one-off rules with no cross-project generality claim). |

`my-phpstorm-conventions` is a **separate, deferred tooling companion** (IDE/static-analysis
knowledge) — not a fourth layer of this architecture, and not authored in this pass.

---

## 2. Internal shape of `my-laravel-stack`

Content is classified by purpose, not forced into a single "prose rule" shape:

1. **Conventions and decision guidance** — architectural and coding decisions (Actions, authorization
   attributes, resource boundaries, query conditionals, scopes, test ownership, PHP class finality,
   migration column nullability), scoped to only the delta not already owned by Boost.
2. **Implementation blueprints** — repeatable implementation shapes the user recreates across
   projects: the CRUD/single-action controller composition (§3), the Pest testing taxonomy and
   ownership model (§4), and enum options. These may remain documented examples where no shared
   executable file exists.
3. **Reusable support templates** — actual code intended to be copied and adapted into consuming
   projects: `QueryFilter`, `Filterable`, and the Inertia testing macros/`TestingServiceProvider`.
   These are part of the stack companion even though they aren't coding-style rules.

Installing a support template requires the agent to inspect the consuming project first, adapt to its
existing structure, expose the change in the normal diff, and never overwrite unrelated existing code.
In `useOrbit`, these implementations already exist, so the later consumer pass (§10, stage 4) compares
and verifies them rather than reinstalling them.

---

## 3. CRUD and single-action controller blueprint

Target file: `rules/resource-controller-blueprint.md` (blueprint, author). This is an implementation
blueprint — a composition contract to recreate, not merely prose style.

### 3.1 Core composition (the additive delta)

Boost's `routing.md` already owns, explicitly, general resource/CRUD controller organization
(routing.md:50–52), the thin-controller principle (routing.md:95), and the FormRequest-vs-inline
boundary (routing.md:106; validation.md:3–16). The blueprint does not restate any of this. What it owns
is the concrete composition of those Boost-level principles with this stack's specific classes, verified
against `ClientsController` and its collaborators:

- **Controller** — coordinates HTTP/Inertia behavior only: resolve the FormRequest, delegate the
  mutation to an Action, build the Resource for read paths, return the Inertia response or redirect.
  Verified shape (`ClientsController::store()`): validate via `StoreClientRequest`, call
  `CreateClientAction::handle()`, flash, redirect — no business logic in the method body.
- **Form Requests** own validation and request normalization (`prepareForValidation()`), never business
  logic — verified: `IndexClientRequest::prepareForValidation()` normalizes `archived`/`direction` before
  validation runs.
- **Policies / `#[Authorize]`** own access enforcement, resolved before the method body runs. Verified
  resolution rule: a route-bound instance (`view`/`update`/`delete`) authorizes against the route
  parameter string directly (`#[Authorize('update', 'client')]`); an operation with no instance yet
  (`create`/`viewAny` on a child resource) must name the child policy explicitly and pass the parent as
  the second argument (`#[Authorize('create', [Document::class, 'client'])]`) — passing only the parent's
  route parameter would resolve the parent's policy, not the child's.
- **Actions** own mutations and business workflows: DB writes wrapped in `DB::transaction()`, audit
  fields, creation-time tenant assignment where the project is multi-tenant, side effects dispatched
  with `->afterCommit()` outside the transaction. Verified: `ArchiveClientAction` sends a `Notification`
  with `->afterCommit()` after the transaction closes, never inside it.
- **Resources** own the response/Inertia data contract — verified: `ClientResource` (`final class`,
  `/** @mixin Client */`) wraps every field the controller passes to Inertia; relation fields use
  `whenLoaded()` to avoid a silent N+1 for any caller that didn't eager-load.

### 3.2 What the controller must make explicit

- **Redirects and flash messages** — verified canonical shape: `Inertia::flash('toast', ['type' =>
  'success', 'message' => __('...')])` followed by `to_route(...)`. Boost states no principle here
  beyond bare code examples; this is a genuine additive delta.
- **Route-model binding behavior** — state explicitly whether an instance is already bound (authorize
  against the route parameter directly) or must be resolved via a named child policy plus parent
  parameter (§3.1) — this distinction is not obvious from Laravel's own attribute API and has caused
  real defects when skipped (discovery §8.4).
- **Tenant boundaries, where tenancy applies** — tenancy is **conditional, not a requirement of every
  project or every controller**. The blueprint does not prescribe a single portable tenancy mechanism.
  When a project genuinely is multi-tenant, the blueprint requires the author to identify, for the
  resource at hand, where each of the following is actually enforced: read scoping (does the index/show
  query itself filter by tenant, or is that left to a global scope?), authorization (does the Policy
  check tenant membership?), creation-time tenant assignment (does the Action stamp the tenant, and from
  what source?), and route-model isolation (can a route parameter resolve to another tenant's record at
  all, and if so, what rejects it?). The blueprint must not assert that Policy checks plus a
  request-scoped context object is *the* mechanism, and must not reject a scoped route binding, a global
  Eloquent scope, or another verified design — any of those can be the right answer for a given project.
  `useOrbit`'s own approach (Policy-layer `organization_id` equality checks, e.g.
  `ClientPolicy::view/update/delete`, plus `OrganizationContext` — a request-scoped singleton — stamping
  `organization_id` at Action creation time, with no scoped route-model binding or global scope in the
  read path) is recorded here as this synthesis's evidence for what an "identify where each boundary is
  enforced" answer looks like in one real project, and as a later smoke-test subject (§10) — not as
  portable skill guidance to prescribe elsewhere.

### 3.3 Non-CRUD and single-action controllers are first-class, not an exception

The blueprint must not manufacture CRUD symmetry the application doesn't have. Verified real examples
that the blueprint must explicitly accommodate:

- **Single-action `__invoke` controllers** for non-resourceful operations — `ClientsArchiveController`,
  `ClientsUnarchiveController` (archive/unarchive); `ClientsPdfExportController`, which returns a raw
  binary `Response` with no Inertia involvement at all; `NotesUpdateController`, which returns a
  `Resource` directly (an XHR/partial-update flow), not a redirect.
- **Controllers implementing fewer than the seven resourceful methods**, or none of them mapped to
  Inertia — `TagsController` implements only `index/store/update/destroy`, returns JSON
  Resources/`noContent()` throughout, and never touches Inertia; it is a pure API-style sub-resource
  controller embedded in an otherwise Inertia application.

The blueprint must never require a feature to have `create`/`edit`/`show` methods it has no route for,
and must never introduce a generic shared `CrudController` base merely to force structural symmetry.

### 3.4 Explicitly out of the CRUD core

Not part of this blueprint's core contract — optional patterns loaded only when a feature genuinely
needs them, documented (or already documented) elsewhere:

- Exports (PDF/Excel) — real capability (`ClientsPdfExportController`), but a separate pattern.
- Filters and sorters — `filters-pattern.md`; the base classes ship as reusable support templates (§8),
  not as part of the controller blueprint's core.
- Admin-oriented list tooling — bulk operations, admin tables, and other administration-specific
  capabilities.

---

## 4. Pest testing blueprint

Target file: `rules/pest-testing-blueprint.md` (blueprint, author), cross-referencing a narrowed
`rules/testing-strategy.md` (convention — the concrete layer-ownership class mapping) and the reusable
Inertia testing macros (§8).

### 4.1 Starting evidence (verified, current)

- `tests/Pest.php:24–26` applies both `TestCase` and `RefreshDatabase` to **both** `Feature` and `Unit`
  uniformly — there is no framework/DB isolation distinguishing the two directories today.
- Because of that binding, most current `tests/Unit/**` tests are actually Laravel-booted, DB-backed
  component tests despite their directory name: `CreateClientActionTest.php` persists via factories and
  asserts DB-level uniqueness; `ClientFilterTest.php` executes a real Eloquent query against a real
  table; `ClientPolicyTest.php` exercises the real Gate against persisted models. Only dependency-free
  classes are genuinely isolated today (verified: `OrganizationRoleTest.php`, a plain enum;
  `OrganizationContextTest.php`, a plain value object with no facades or DB).
- The tree has a real ownership intention — Actions, Filters, Policies, Models, Jobs, Listeners,
  Notifications, and Providers each get their own subtree mirroring `app/` — but the directory name
  ("Unit") hides the true execution boundary.
- Some HTTP tests duplicate Action-level detail: `StoreTest.php` re-checks persisted fields
  (`state_id`, `city`, company-specific nullability) already covered exhaustively by
  `CreateClientActionTest.php`'s full matrix (slug collision across organizations, `organization_id` vs.
  `OrganizationContext` override, `created_by`) — the HTTP test's version is lighter (spot checks, not
  the full matrix), but the overlap is real.

### 4.2 Target taxonomy

> First classify a test by execution boundary; then mirror the owning application area inside that
> boundary.

- **`tests/Unit`** — genuinely isolated only: no Laravel application boot, no database or factories, no
  service container, no Laravel facades.
- **`tests/Feature`** — anything that boots Laravel or uses the database. Mirror the owning application
  area inside it only where useful — `Http`, `Actions`, `Policies`, `Filters`, `Sorts`, `Resources`,
  `Models`, `Jobs`, `Listeners`, `Support` — never force a category a feature has nothing to put in.
- **Preserve the existing readable endpoint-oriented `Feature/Http` structure** — verified real shape:
  `tests/Feature/Http/Clients/{IndexTest,ShowTest,StoreTest,UpdateTest,DestroyTest,ArchiveTest,...}.php`.
  The target taxonomy keeps separate per-endpoint files; it does not force every controller into one
  oversized `{ControllerName}Test.php`.

This synthesis does **not** prescribe or perform a mass migration of useOrbit's existing test tree —
that remains a later, reviewed application decision (§10).

### 4.3 Testing responsibility

- **HTTP tests** own public endpoint behavior: authentication, authorization wiring, validation, tenant
  boundaries, route-model behavior, response status, redirects, flash messages, Inertia components and
  prop contracts.
- **Action tests** own complete mutation behavior: defaults, transactions, audit fields, slug rules,
  branches, side effects.
- **Policy tests** own the complete permission matrix; HTTP keeps representative cases proving
  authorization is wired.
- **Filter and sorter tests** own their complete query matrices; HTTP keeps representative wiring and
  request-validation cases.
- **Resource tests** own non-trivial project-defined transformations and conditional-field behavior;
  HTTP proves the correct Resource contract reaches Inertia.
- **Model tests** cover project-owned behavior, scopes, and meaningful relationship constraints — not
  Laravel framework behavior.
- **Reusable Inertia testing macros and `TestingServiceProvider`** belong to the skill's reusable
  support templates (§8), with explicit installation and prerequisite guidance — verified registration:
  `bootstrap/providers.php`, guarded by a `runningUnitTests()` boot check so the macros exist only while
  the suite runs.

> When a lower layer owns a complete behavioral matrix, the HTTP layer should retain enough evidence to
> prove integration without duplicating that matrix.

**Warning, grounded in a verified current anti-pattern:** don't generate a test's expected result by
invoking the same production Resource or query implementation under test. Verified: `ShowTest.php` and
`UpdateTest.php` build their expected Inertia prop via `ClientResource::make(...)` fed into the
`assertHasResource` macro — if `ClientResource`'s shape regresses in a way that's still internally
self-consistent, this comparison cannot catch it. Prefer known expected identifiers and literal contract
values instead, especially for the properties an HTTP test is specifically responsible for proving.

### 4.4 Capability gating

- Pest TIA (verified: `tests/Pest.php:28`, `pest()->tia()->always()->locally()` — a core Pest 5 feature,
  not a separate plugin) and any other optional Pest plugin (arch testing, type coverage — verified
  absent from `composer.json`) must be treated as capability-gated: check what the consuming project
  actually has installed/configured before assuming it's available. Never universally prescribe them.
- `LazilyRefreshDatabase` — verified entirely absent from useOrbit today (zero matches anywhere in the
  codebase). Record only as a future candidate to measure and verify, not a locked requirement.

---

## 5. Minimal test data — Boost vs. companion ownership

Boost files inspected in full: `testing-best-practices/rules/test-data.md`, `rules/review.md`,
`rules/isolation.md`, `rules/endpoint-tests.md`, `rules/assertions.md`, `rules/naming.md`,
`rules/finding-features.md`, `rules/performance.md`, `rules/security.md`.

**Boost already materially owns record-level minimalism**, verbatim: *"Create only the records required
to arrange the behavior or support an assertion"* (`test-data.md:32`), reinforced by
`review.md`'s matching checklist item. Defer to Boost for this; do not restate it.

**Ownership decision:** Boost's principle is scoped to *record necessity* — it says nothing about which
*attributes* a given factory call should set. `isolation.md` doesn't cover this angle either (it's scoped
to fakes/mocks/time/randomness). `my-laravel-stack` retains the narrow additive delta:

> Each test creates only the records and attributes required to establish its preconditions and prove
> the behavior under test. Additional records or values are introduced only when they are material to
> the case — for example ordering, filtering, tenant isolation, collisions, absence, or complete field
> mapping. "Minimal" does not mean incomplete coverage: a test specifically proving field mapping may
> intentionally provide the complete relevant payload.

This belongs in `rules/pest-testing-blueprint.md` (§4), stated as a delta on top of Boost's
`test-data.md`, not a duplicate of it.

---

## 6. Two recovered stranded conventions

### 6.1 Final-by-default application classes

**Evidence inspected:** grepped `"final class"` and `declare(strict_types` across every file in both
installed Boost rule directories (28 files total, `laravel-best-practices/rules/*` and
`testing-best-practices/rules/*`) — zero matches in either. Boost states no opinion, in either
direction, on class finality. Verified `useOrbit` evidence (this pass's own controller/Action/Resource
reads): `ClientsController` is `final class`; `CreateClientAction`, `UpdateClientAction`,
`ArchiveClientAction` are `final class`; `ClientResource`, `CountryResource` are `final class`;
`ClientFilter` is `final class`; its abstract base `QueryFilter` correctly is not. `my-laravel-patterns`
already states `final` narrowly for two class kinds (`resources.md`, `filters-pattern.md`) but never as
a general default.

**Boost coverage:** none. **Owner:** `my-laravel-stack`'s conventions/decision-guidance layer (§2,
category 1) — not `.ai/rules`, since this is a general authoring convention intended to travel across
this user's projects, not a `useOrbit`-only settled fact.

**Rule:** Declare concrete application classes `final` by default when they are not designed for
inheritance. Leave a class extensible only when it represents an intentional extension seam or a
verified framework, proxying, or tooling requirement.

**Scope and exceptions:**
- Applies to concrete classes (Controllers, Actions, Resources, Filters, Policies, Requests) — not to
  abstract classes (verified: `QueryFilter` stays non-`final` because it's `abstract` and designed for
  extension), interfaces, traits, or enums.
- Does not forbid deliberate inheritance — a class with a real extension seam stays open.
- Does not claim every PHP class is universally finalizable; it is a default, not an absolute — a
  verified framework/tooling requirement overrides it.
- Future skill code examples must model `final class` for every concrete class example unless the
  example is specifically illustrating an extension seam.
- **Internal home:** a new `rules/php-conventions.md` (convention, author) in `my-laravel-stack`,
  generalizing what `resources.md`/`filters-pattern.md` already state narrowly, cross-referenced from
  both rather than restated in each.

### 6.2 Laravel migration nullability

**Evidence inspected:** Boost's `laravel-best-practices/rules/migrations.md` (full read, 68 lines) — zero
mentions of `nullable()` or any nullability-default policy; grepped the whole `laravel-best-practices`
directory for `nullable()` (zero hits) and `notNull` (three hits, all unrelated `whereNotNull()`
query-builder calls in `eloquent.md`). Installed Laravel framework source verified directly (v13.29.0):

- `Illuminate\Database\Schema\ColumnDefinition extends Fluent`, and `Fluent::__call()`
  (`Support/Fluent.php:299–308`) accepts **any** method name, storing it as a plain attribute
  (`$this->attributes[$method] = ...`) with no validation against a known modifier list.
- Every schema grammar reads only the `nullable` attribute to decide whether to emit `NULL`/`NOT NULL`
  (`MySqlGrammar.php:1301,1304`; `SQLiteGrammar.php:1144,1147`; `PostgresGrammar.php:1226`;
  `SqlServerGrammar.php:977`); none reads a `notNull` attribute at all.

This establishes the precise three-way distinction the guidance must draw:

- **Not unsupported** — `->notNull()` does not throw; `Fluent::__call()` accepts any method name.
- **Accepted but ignored** — the correct description of `->notNull()` specifically: the resulting
  attribute is never read by any grammar, so it has zero effect on the generated SQL. It isn't a
  recognized no-op modifier; it simply vanishes.
- **Unnecessary** describes something different: explicitly calling `->nullable(false)`, or omitting
  `nullable()` altogether — both are real, recognized, and equivalent to the schema's default, just
  redundant to state.

**Rule:** Schema columns are non-nullable by default. Add `nullable()` only when `NULL` is a valid value
for the column. Do not use `->notNull()` — it is accepted by PHP's dynamic call resolution but silently
ignored by every installed schema grammar; it neither errors nor changes the generated SQL, and its
presence in a migration misleadingly suggests a real modifier exists.

**Boost coverage:** none (confirmed above) — this narrow correctness warning belongs entirely to
`my-laravel-stack`. **Scope:** applies uniformly across all four installed schema grammars; no exception
found. **Internal home:** a new `rules/migrations.md` (convention, author) in `my-laravel-stack` — there
is currently no migrations rule file in `my-laravel-patterns`; this becomes its first, narrow entry.

---

## 7. File-by-file disposition — `my-laravel-patterns` (→ `my-laravel-stack`)

Legend: **convention** (convention/decision guidance) · **blueprint** (implementation blueprint) ·
**template** (reusable support template, listed separately in §8) · **keep** / **repair** / **narrow**
/ **author** as before.

| File | Category | Disposition | Reasoning |
|---|---|---|---|
| `SKILL.md` | skill entry | repair | Names the retired Boost skill `pest-testing` instead of `testing-best-practices` (discovery §8.11, Tier 1 #1). State the reusable support templates as an explicit prerequisite the skill assumes exists, not an unstated fact. |
| `rules/actions-pattern.md` | convention | narrow | Boost's `architecture.md`/`routing.md` now name the general Action pattern (discovery §7.2). Trim to the Boost delta: `app/Actions/{Domain}/` location, `{Verb}{Model}Action` naming, fixed `handle()`, fixed `$attributes` param, the FormRequest-derived `@param array{...}` shape algorithm, and the `DB::transaction()`-pure / `->afterCommit()` discipline. Cross-reference `resource-controller-blueprint.md` (§3) rather than restating the controller-composition half. |
| `rules/authorization.md` | convention | keep | Zero Boost coverage of the `#[Authorize]` attribute mechanism (discovery §8.4). Keep the portability claim and the adoption-breadth claim (64 verified controller-method occurrences, this pass) as two distinct pieces of evidence. |
| `rules/eloquent-attributes.md` | convention | narrow | Boost's `eloquent.md` already demonstrates `#[Scope]` mechanics by example. Reduce to the actual delta: the migration-off-`scopeXxx` framing, the `❌ scopeXxx` counter-example, and the Laravel version pin (`^13.7`). |
| `rules/enum-options.md` | blueprint | keep, caveated | No Boost overlap found. Not independently re-audited against live code this pass (discovery §8.2). |
| `rules/factories-and-seeders.md` | convention | keep, caveated | Narrow overlap only (Boost's `test-data.md` endorses `for()` generally; field-derivation/email/date-chaining content has no Boost equivalent). Not independently re-audited this pass (discovery §8.3). |
| `rules/filters-pattern.md` | convention (wiring), referencing templates | repair | The FormRequest → `QueryFilter` → `Filterable` wiring pattern has no Boost overlap. Scrub the live `useOrbit` issue links (`#76`, `#71`) and the arbitrary `paginate(7)` literal (discovery §8.7) — those are `useOrbit` fingerprints, not part of the pattern. `QueryFilter`/`Filterable` themselves ship as reusable support templates (§8), not merely narrated prose. Excluded from the controller blueprint's core (§3.4). |
| `rules/query-conditionals.md` | convention | repair | Broken example and a dead `TagAttachment::forTaggableType()` citation (discovery §8.10, Tier 1 #3); the underlying `when()`-over-`if` rule needs no content change. |
| `rules/request-normalization.md` | convention | keep, caveated | No Boost overlap (Boost's `validation.md` covers rule syntax, not coercion/defaulting discipline). Checked only for internal consistency in discovery, not against live FormRequest code (discovery §8.8) — this pass's `IndexClientRequest::prepareForValidation()` read is consistent with the file's content but doesn't constitute the fuller re-audit still owed. |
| `rules/resources.md` | convention | repair | Its cited example (`ClientsController.php`) uses `inertia()` throughout while the file's own examples use `Inertia::render()`, inconsistent with it and with `filters-pattern.md` (discovery §6.2, §8.5, Tier 1 #2) — this pass reconfirms the controller still uses `inertia()` at every call site. Fix is a consistency correction — `Inertia::render()` isn't being declared invalid. The `whenLoaded()`/no-`$with` discipline is unchanged and reconfirmed. |
| `rules/testing-strategy.md` | convention | repair + narrow | Defer to Boost for record-level test-data minimalism and general layer-ownership de-duplication (§0, §4, §5 above); don't restate either. Retain only the concrete Action/Controller/Policy/Filter/Resource/Model class-taxonomy ownership mapping (§4.3), `assertDatabaseHas()`'s narrowed role, and a cross-reference to `pest-testing-blueprint.md` (§4) for the target Unit/Feature taxonomy and execution-boundary discipline — this file no longer independently states where Action/Filter/Policy tests should live. |
| `rules/resource-controller-blueprint.md` (new) | blueprint | author | Content specified in full in §3. Boost owns general resource/CRUD organization, thin controllers, and FormRequest boundaries; this file owns only the concrete composition with this stack's Action/`#[Authorize]`/Resource/Inertia contract, explicit redirect/flash conventions, conditional tenant-boundary identification when a project is multi-tenant (§3.2 — no single mechanism prescribed), and the non-CRUD/single-action allowance (§3.3). Excludes exports, filters/sorters, and admin-table capabilities from its core (§3.4). |
| `rules/pest-testing-blueprint.md` (new) | blueprint | author | Content specified in full in §4. Defines the target Unit/Feature taxonomy by execution boundary, per-layer testing responsibility, the self-referential-expected-value warning, and capability gating for optional Pest plugins — without prescribing a migration of the current tree. |
| `rules/php-conventions.md` (new) | convention | author | Content specified in full in §6.1: final-by-default for concrete application classes, with stated exceptions. |
| `rules/migrations.md` (new) | convention | author | Content specified in full in §6.2: the migration column-nullability default and the `->notNull()` correctness warning. |

**`my-phpstorm-conventions`** — deferred in full. Its one known stale finding (`SKILL.md` states the
`getDiagnostics` prerequisite with no fallback for its absence, discovery §6.3/§10, Tier 2 #5) stays
listed here as a deferred repair, not authored in this pass or its sequence.

---

## 8. Reusable support templates

Actual code, bundled inside the skill and copied/adapted into a consuming project rather than
restated as prose:

- **`QueryFilter`** and **`Filterable`** — the base classes underlying `filters-pattern.md`'s wiring.
- **Inertia testing macros** (`TestingServiceProvider`'s five macro registrations: `hasResource`,
  `hasPaginatedResource`, `assertHasResource`, `assertHasPaginatedResource`, `assertHasInertiaFlash`,
  plus the `runningUnitTests()` boot guard, registered in `bootstrap/providers.php`).

Installing any of these requires inspecting the consuming project first, adapting to its existing
structure, exposing the change in the normal diff, and never overwriting unrelated existing code.
`useOrbit` already has all of these implemented — the consumer pass (§10, stage 4) compares and
reconciles against that existing code rather than reinstalling it.

---

## 9. Code-example standard

An authoring constraint for the future `my-laravel-stack`, not optional polish: `useOrbit` is evidence
for *discovering* patterns; its domain language and implementation must not be copied into the portable
skill. Code examples must:

- Use neutral, recognizable domain concepts, not `useOrbit`'s specific models, routes, permissions,
  literals, issue references, or product behavior.
- Demonstrate one relevant contract at a time; omit unrelated complexity while preserving the
  architectural relationship being taught.
- Use syntax compatible with the supported Laravel, Inertia, Vue, and Pest versions.
- Remain coherent when multiple snippets form one flow (e.g. Request → Controller → Action → Resource →
  Pest test) — a reader following the whole chain should see one consistent example, not fragments from
  different fictional features.
- Avoid pseudocode that looks runnable but is incomplete or technically invalid.

**Illustrative snippets** (most of §3–§7's future content) may be intentionally partial when their
purpose and omissions are clear — they read like concise examples from high-quality Laravel
documentation, not like a copy of a real controller.

**Reusable support templates** (§8) are held to a stricter bar: complete enough to install, with stated
prerequisites and registration steps, and appropriate syntax or execution validation before being
treated as ready to copy into a project.

`useOrbit`'s own provenance and empirical evidence stay in discovery and any future dossier — never in
the skill's public-facing examples.

---

## 10. Implementation sequence

1. Author and rename `my-laravel-patterns` → `my-laravel-stack`, applying the approved repairs,
   Boost-delta narrowing, and the simplified internal classification (§2, §7) — including authoring
   `rules/resource-controller-blueprint.md` (§3), `rules/pest-testing-blueprint.md` (§4),
   `rules/php-conventions.md` (§6.1), and `rules/migrations.md` (§6.2), all held to the code-example
   standard (§9).
2. Add the generic reusable support templates (§8) and their usage/prerequisite instructions
   atomically with the skill authoring — don't create instructions that reference a template not yet
   present.
3. Refresh the authored skill into `useOrbit`.
4. Compare its templates against `useOrbit`'s existing implementations; reconcile only intentional
   generic differences, and don't overwrite project-specific code.
5. **Consumer smoke test**, in two stages, only after 1–4 are complete:
   1. **No-edit conformance audit** of `useOrbit`'s current controllers and Pest tests against the
      authored blueprints. Classify every finding as one of: conformance; harmless legacy organization;
      a legitimate project-specific exception; an application defect; or incorrect, incomplete, or
      over-absolute skill guidance. Do not modify the skill merely to make existing code appear
      compliant.
   2. **One representative CRUD vertical slice** — likely Clients — exercised as real implementation
      work, using the controller and Pest blueprints as they'd actually be applied.

   Together these establish **breadth** (does the skill accurately understand the application) and
   **depth** (are the blueprints actionable during real implementation), not just one or the other.
6. Reconcile the dossier, README, and roadmap only after that real exercise, using its empirical
   evidence rather than this document's assumptions.

---

## 11. Non-goals and confidence limits

- No skill file, `.ai/rules` file, runtime file, README, roadmap, or dossier was edited or created by
  this document.
- No Composer package — not currently needed (§0).
- `my-phpstorm-conventions` was not touched — fully deferred (§0, §7).
- **One-consumer evidence ceiling**: every classification in this document rests on Laravel Boost's
  installed source, the installed Laravel framework source, plus exactly one real project, `useOrbit` —
  none of it has been tested against a second Laravel+Vue+Inertia codebase.
- **Vue 3 evidence gap, stated explicitly**: this pass's fresh evidence covers Laravel, Inertia, and
  Pest; it contains no additive Vue-specific findings. Vue 3 remains part of the locked stack boundary
  (§0), not a claim of existing coverage.
- `enum-options.md`, `factories-and-seeders.md`, and `request-normalization.md` were not freshly
  re-audited line-by-line against live `useOrbit` code this pass — their dispositions in §7 carry
  forward Phase C's evidence, with a partial spot-check for `request-normalization.md` noted there.
- The Pest testing blueprint (§4) defines a target taxonomy only; it does not migrate `useOrbit`'s
  current `tests/Unit`/`tests/Feature` tree, and this document does not claim that migration is trivial
  or already scoped.
- `useOrbit`'s own removed design-system material (badge tones, breadcrumb rules, etc.) is out of
  `agentic-engineering`'s scope entirely.

---

## Coverage check (self-report)

- [x] Every retained file from `phase-d-stack-discovery.md`'s per-file findings has a disposition in
  §7 or an explicit deferral (`my-phpstorm-conventions`).
- [x] `QueryFilter`/`Filterable` and the Inertia testing macros are classified as reusable support
  templates (§8), not documentation-only patterns.
- [x] Enum options are classified as an implementation blueprint (§7).
- [x] The declared target is Laravel + InertiaJS + Vue 3 + Pest, with Vue's thinner evidence base stated
  explicitly rather than implied as equally mature (§0, §11).
- [x] The CRUD/single-action controller blueprint is additive to Boost's routing.md, actionable (§3.1–
  §3.2), and explicitly allows non-CRUD/single-action controllers without manufacturing symmetry (§3.3),
  excluding exports/filters/sorters/admin-table capabilities from its core (§3.4).
- [x] Unit vs. Feature is defined by execution boundary first, then mirrored by owning application area
  (§4.2), grounded in a verified current defect (`tests/Pest.php` binds `RefreshDatabase` to both).
- [x] Test ownership is assigned per layer (§4.3) without duplicating a lower layer's complete matrix,
  while HTTP still proves integration — including a verified anti-pattern warning against self-derived
  expected values (§4.3).
- [x] The minimal-test-data rule has an evidence-backed owner: Boost owns record-level minimalism
  (`test-data.md:32`); the companion owns only the attribute-level delta (§5).
- [x] The code-example standard (§9) prohibits `useOrbit`-specific public examples and distinguishes
  illustrative snippets from reusable support templates.
- [x] Both stranded conventions (final-by-default, migration nullability) have evidence-backed ownership,
  qualified wording, and a stated internal home in the future skill (§6.1, §6.2).
- [x] The consumer smoke test defines both an audit-breadth stage and a real-implementation-depth stage,
  sequenced after authoring and refresh (§10, step 5).
- [x] No `.ai/rules` proposal, five/six-boundary model, Composer-package proposal, or lengthy packaging
  analysis remains beyond a brief "not currently needed" note (§0, §11).
- [x] The one-consumer evidence limit is stated once (§11).
- [x] Only `phase-d-stack-synthesis.md` changed in `agentic-engineering`. No `useOrbit` file changed —
  only reads were performed there, including inside `vendor/laravel/framework`.
