# my-laravel-stack — Architecture Dossier

Status: Current
Scope: `my-laravel-stack` as it stands in this repository
Purpose: A compact architecture artifact for the skill — what it provides, where it sits in the
ecosystem, what it owns versus what it deliberately leaves to others, how its package is organized,
how its rules/blueprints/templates cooperate, where each decision has a single owner, how an agent
consumes it, and its current confidence and limits. [`SKILL.md`](../my-laravel-stack/SKILL.md) remains
the operational activation and routing entrypoint; [`README.md`](../my-laravel-stack/README.md) is the
human-facing orientation. This document does neither of those jobs again — it explains the
architecture behind them.

## 1. Purpose and activation boundary

`my-laravel-stack` is a personal, portable companion for a **Laravel + InertiaJS + Vue 3 + Pest**
stack. It is additive only: Laravel Boost's `laravel-best-practices` and `testing-best-practices`
skills already own the general Laravel and Pest baseline, and `inertia-vue-development` owns
Inertia/Vue client-side patterns. `my-laravel-stack` never substitutes for any of them — it activates
*alongside* the matching Boost skill(s), carrying only the delta genuinely additive to what they
already cover.

It activates for implementation and review work that needs this stack's concrete conventions:
composing or reviewing a controller, Form Request, Action, Policy, or Resource; adding index
filtering or sorting; writing or organizing a Pest test; defining an Eloquent local scope, a migration
column, or a backed enum's option list; generating factory or seeder data. If a task needs a Boost
skill this installation doesn't have, the skill says so explicitly rather than silently filling the
gap with improvised baseline guidance — it is an incomplete companion for that area, not a substitute
author for it.

## 2. Ownership model

Three parties hold three distinct, non-overlapping kinds of knowledge:

| Owner | Owns |
|---|---|
| **Laravel Boost** (`laravel-best-practices`, `testing-best-practices`, `inertia-vue-development`) | The general Laravel/Pest/Inertia-Vue baseline — validation, Eloquent mechanics, resource/CRUD organization, thin-controller and FormRequest-boundary philosophy, migrations in general, layer-ownership test de-duplication, record-level test-data minimalism, security, style. An external dependency, never extracted, renamed, or duplicated here. |
| **`my-laravel-stack`** | The reusable custom stack delta — conventions, implementation blueprints, and reusable support templates verified for this stack, portable across this user's own projects by copy/reinstall. |
| **Consuming project** | Its own domain model, product rules, repository policy, and any project-specific adaptation of a blueprint or template — tenancy mechanism, naming, UI decisions, deployment conventions. None of this is the skill's to prescribe. |

A corollary of this split: `my-laravel-stack` states several of its own delta items as conditional
rather than universal — tenancy, filters/sorters, non-CRUD controller shapes. That conditionality is a
deliberate architectural boundary between what this skill can responsibly generalize and what only a
concrete project can decide, not an omission to tighten later.

`my-phpstorm-conventions` is a separate, unrelated companion (IDE/static-analysis knowledge) — not a
fourth layer of this model.

## 3. Package architecture

The package is organized by what kind of resource each file *is*, not merely by directory convention:

- **`rules/`** — independently applicable conventions and invariants. Each file stands alone: a rule
  about Eloquent scope attributes, request normalization, or PHP class finality doesn't require any
  other file to make sense on its own.
- **`blueprints/`** — multi-component implementation shapes that compose several rules and
  responsibilities into one recognizable pattern. A blueprint is where several independently valid
  rules meet in one worked structure — a full controller composition, a filter/sorter wiring across a
  Form Request/model/controller, a Pest execution-boundary taxonomy.
- **`templates/`** — complete, installable PHP starting points, structured to mirror their intended
  project-relative path (`templates/app/...` mirrors `app/...` in a consuming project).

These are semantically different resources, not an arbitrary three-way split of the same content. A
rule answers "what is the invariant." A blueprint answers "how do several invariants compose into one
shape, and in what order." A template answers neither — it is executable code, meant to be inspected,
reconciled against what a project already has, and copied or adapted, never installed blindly on the
assumption a project has nothing there already.

## 4. Operational architecture

### Resource controller composition

[`blueprints/resource-controller.md`](../my-laravel-stack/blueprints/resource-controller.md) states
the reference composition — **Controller → Form Request → Policy/`#[Authorize]` → Action → Resource →
Inertia/HTTP response** — and immediately qualifies it: this is a reference shape a full CRUD endpoint
follows, not a mandatory sequence every endpoint must implement in full. Each stage is included only
when the endpoint actually needs what it does, and the blueprint treats single-action controllers,
non-Inertia responses (a binary export), a Resource returned directly from an XHR endpoint, and a
controller implementing fewer than the seven resourceful methods as first-class shapes — not
exceptions to patch around. Within this composition:

- The **Form Request** owns validation and request normalization
  ([`rules/request-normalization.md`](../my-laravel-stack/rules/request-normalization.md)) —
  `prepareForValidation()` is where coercion and defaulting happen once, so an Action or Filter can
  trust `validated()` as already correct rather than re-defaulting downstream.
- **Authorization** is declarative and resolved before the method body runs
  ([`rules/authorization.md`](../my-laravel-stack/rules/authorization.md)) — the `#[Authorize]`
  attribute, never `$this->authorize()`, with the array form required specifically for `create`/
  `viewAny` on a child resource, where no bound instance exists yet to infer a policy from.
- The **Action** owns the mutation itself
  ([`rules/actions.md`](../my-laravel-stack/rules/actions.md)) — a fixed `handle()` entry point, no
  HTTP-layer globals inside it, and external side effects deferred with `->afterCommit()` so they
  never execute until the enclosing transaction actually commits.
- The **Resource** owns the response contract
  ([`rules/resources.md`](../my-laravel-stack/rules/resources.md)) — a controller never passes a raw
  Eloquent result to Inertia, and a relation field is exposed through `whenLoaded()`, never a bare
  accessor or a model-wide `$with`, so the Resource stays safe regardless of which caller reaches it.

### Filtering and sorting

[`blueprints/filters-and-sorting.md`](../my-laravel-stack/blueprints/filters-and-sorting.md) is itself
conditional — loaded only when an index endpoint genuinely needs filtering or sorting, not a mandatory
part of every controller. It composes: query-parameter validation in the Form Request (including the
`direction` default from `rules/request-normalization.md`, since `QuerySorter`'s constructor takes a
non-nullable `string`); a concrete `{Model}Filter`/`{Model}Sort` class per model; the reusable
`QueryFilter`/`QuerySorter` base classes and `Filterable`/`Sortable` model traits shipped as templates;
and controller-level query composition that stays a no-op when no query params are present. Filter and
Sorter classes never validate — they trust an already-validated value exactly as an Action trusts
`validated()`.

### Testing

Two distinct decisions compose here, deliberately kept apart:

- [`blueprints/pest-testing.md`](../my-laravel-stack/blueprints/pest-testing.md) owns the
  **execution-boundary configuration** — classifying `tests/Unit` versus `tests/Feature` by what a
  test actually boots (database, container, facades), confirming what the project's own
  `tests/Pest.php` binds a database-refresh trait to before trusting a directory name, and the safe
  order for narrowing that binding during a migration. It also owns endpoint-oriented HTTP test-file
  organization, the warning against building a test's expected value from the same production Resource
  it's supposed to verify, and gating optional Pest capabilities (TIA, architecture testing) behind
  what a project actually has installed.
- [`rules/test-ownership.md`](../my-laravel-stack/rules/test-ownership.md) owns **per-layer test
  responsibility** — the concrete Action/Policy/Filter/Sorter/Resource/Model/HTTP location-and-scope
  mapping, when to assert existence versus an exact persisted value, and the no-redundancy rule that a
  higher layer proves only what a lower layer doesn't already prove (with the minimal-wiring exception:
  an HTTP test may keep one persisted identity/association assertion to prove the correct route-bound
  model, actor, or pivot pair reached the Action — a bare row-count assertion cannot prove that).

A test file therefore answers "where does this test physically live and what does the suite boot for
it" from the blueprint, and "what does this specific layer's test assert, and where does its
responsibility stop" from the rule — two different questions with two different owners, composed
rather than duplicated.

### Supporting rules

The remaining rules apply independently wherever their narrow subject appears: `#[Scope]` over the
legacy `scope`-prefixed method name for Eloquent local scopes
([`rules/eloquent-attributes.md`](../my-laravel-stack/rules/eloquent-attributes.md)); `when()` over an
`if` block for a mid-chain query conditional
([`rules/query-conditionals.md`](../my-laravel-stack/rules/query-conditionals.md)); a static `all()`
on a backed enum instead of mapping `::cases()` at each call site
([`rules/enum-options.md`](../my-laravel-stack/rules/enum-options.md)); deriving dependent factory
fields from one source of truth and structuring dev-only seeders
([`rules/factories-and-seeders.md`](../my-laravel-stack/rules/factories-and-seeders.md)); `final`-by-
default concrete application classes
([`rules/php-conventions.md`](../my-laravel-stack/rules/php-conventions.md)); and non-nullable-by-
default migration columns, including why `->notNull()` silently does nothing across every schema
grammar ([`rules/migrations.md`](../my-laravel-stack/rules/migrations.md)).

## 5. Single-owner boundaries

Every architectural decision in this package has exactly one file that states it; every other file
that touches the same territory cross-references that owner instead of restating it:

| Decision | Owner |
|---|---|
| An Action's own shape — naming, `handle()`, the `$attributes` PHPDoc derivation, transaction/`afterCommit()` discipline | `rules/actions.md` |
| How Controller, Form Request, Policy, Action, Resource, and response compose into one endpoint | `blueprints/resource-controller.md` |
| `#[Authorize]` mechanics, including the child-resource array-form requirement | `rules/authorization.md` |
| The JsonResource contract and safe relation exposure | `rules/resources.md` |
| Where input coercion/defaulting happens | `rules/request-normalization.md` |
| The multi-component filter/sorter wiring across Form Request, model, and controller | `blueprints/filters-and-sorting.md` |
| `tests/Unit`/`tests/Feature` execution-boundary classification and suite binding | `blueprints/pest-testing.md` |
| Concrete per-class test location, ownership, and the no-redundancy rule | `rules/test-ownership.md` |
| Eloquent local-scope attribute convention | `rules/eloquent-attributes.md` |
| Mid-chain query conditionals | `rules/query-conditionals.md` |
| Backed-enum option lists | `rules/enum-options.md` |
| Factory/seeder realism and structure | `rules/factories-and-seeders.md` |
| Concrete-class finality | `rules/php-conventions.md` |
| Migration column nullability | `rules/migrations.md` |

This matters because two files that each describe part of the same decision can drift independently
while each still assumes the other owns it. The clearest example still visible in the package's shape
is the test-ownership split above: `blueprints/pest-testing.md` states outright that it does not
restate the concrete class-taxonomy mapping, and `rules/test-ownership.md` states that it does not
restate the general execution-boundary or de-duplication principles already owned elsewhere. A
cross-reference composes the two into one coherent testing story without either file duplicating the
other's authority.

## 6. Templates

Five templates, each a complete, syntactically valid PHP implementation rather than a placeholder or
generator stub:

- [`templates/app/Filters/QueryFilter.php`](../my-laravel-stack/templates/app/Filters/QueryFilter.php)
  — the abstract base every domain filter extends. Dispatch is convention over configuration:
  `apply()` camel-cases each validated array key and calls the same-named method on the concrete
  filter, silently skipping a key with no matching method or a `null`/`''` value.
- [`templates/app/Models/Concerns/Filterable.php`](../my-laravel-stack/templates/app/Models/Concerns/Filterable.php)
  — the trait wiring a `#[Scope]`-based `filter` scope onto a model, delegating to an injected
  `QueryFilter`.
- [`templates/app/Sorts/QuerySorter.php`](../my-laravel-stack/templates/app/Sorts/QuerySorter.php) —
  the abstract base every domain sorter extends. Resolves a requested column the same way
  `QueryFilter` resolves a key, falls back to an abstract `default()` implementation the concrete
  sorter must supply, and always breaks ties on the model's primary key so pagination and tests get a
  stable order regardless of the database's query plan.
- [`templates/app/Models/Concerns/Sortable.php`](../my-laravel-stack/templates/app/Models/Concerns/Sortable.php)
  — the trait wiring a `#[Scope]`-based `sort` scope onto a model, delegating to an injected
  `QuerySorter`.
- [`templates/app/Providers/TestingServiceProvider.php`](../my-laravel-stack/templates/app/Providers/TestingServiceProvider.php)
  — registers five Inertia-testing Pest macros (`hasResource`, `hasPaginatedResource`,
  `assertHasResource`, `assertHasPaginatedResource`, `assertHasInertiaFlash`), guarded by a
  `runningUnitTests()` boot check so they exist only while the test suite runs.

Each carries its own prerequisites inline: the `#[Scope]`-based traits require confirming that the
target project's installed `laravel/framework` version actually provides
`Illuminate\Database\Eloquent\Attributes\Scope`; the filter/sorter templates require the paired
base-class-and-trait pairing to be installed together; the testing provider requires
`inertiajs/inertia-laravel` and Pest, and must be registered in `bootstrap/providers.php`. Every
template's docblock also states the reconciliation instruction: check whether an equivalent already
exists at the target path before installing, and reconcile rather than overwrite. They are inspectable
starting points meant to be read, adapted, and validated in the consuming project — not instructions
to overwrite existing project code blindly, and not a generator contract with placeholders to
substitute.

## 7. Consumption and adaptation

An agent working in this stack loads only the rule, blueprint, or template file(s) the current task
needs — `SKILL.md`'s routing table is the entrypoint for that selection, and this dossier does not
repeat it. The skill is always combined with the matching Boost skill(s) for the same task, never
loaded as a substitute for them, and any project-specific context the consuming project supplies
(existing code, product decisions, repository policy) sits above the skill's own defaults.

Before adopting a blueprint or template in a real project, inspect what the project already has at
the equivalent path or endpoint. A template exists to be reconciled against an existing implementation,
not dropped in on the assumption nothing is there yet; a blueprint's conditional stages (tenancy
handling, filters/sorters, a full CRUD chain) apply only where the endpoint or project genuinely calls
for them. Tenancy mechanism, naming conventions, UI-framework specifics, and deployment conventions are
project-owned decisions this skill deliberately does not prescribe — where a blueprint discusses
tenancy, for example, it identifies the questions a multi-tenant project must answer (read scoping,
authorization, creation-time assignment, route-model isolation) without naming which mechanism a
project must use to answer them.

## 8. Boundaries and confidence

The skill's Laravel, Inertia, and Pest guidance has been checked against real implementation and
verification work, not authored and left untested. That confidence does not extend to broad,
multi-project portability — validation beyond one real consuming project remains unproven, and this
document does not claim otherwise.

Vue 3 is part of the declared stack boundary, since the stack this skill targets genuinely includes
it, but mature, independently-owned Vue-specific guidance remains limited here. A Vue implementation
question routes to `inertia-vue-development` rather than to this skill filling the gap with
improvised guidance.

No other limitation currently applies to the package as it stands; a resolved finding is not carried
forward here once corrected in the rule, blueprint, or template file it belonged to.
