# laravel-inertia-stack — Architecture Dossier

Status: Current
Scope: `laravel-inertia-stack` as it stands in this repository
Purpose: A compact architecture artifact for the skill — what it provides, where it sits in the
ecosystem, what it owns versus what it deliberately leaves to others, how its package is organized,
how its rules/blueprints/templates cooperate, where each decision has a single owner, how an agent
consumes it, and its current confidence and limits. [`SKILL.md`](../skills/laravel-inertia-stack/SKILL.md) remains
the operational activation and routing entrypoint; [`README.md`](../skills/laravel-inertia-stack/README.md) is the
human-facing orientation. This document does neither of those jobs again — it explains the
architecture behind them.

## 1. Purpose and activation boundary

`laravel-inertia-stack` is an opinionated companion for a **Laravel + InertiaJS + Vue 3 + Pest**
stack. Laravel Boost's `laravel-best-practices` and `testing-best-practices` are the first-party baseline
for general Laravel and Pest, and `inertia-vue-development` is the reference for Inertia/Vue client-side
patterns. The companion never substitutes for them; it activates alongside the matching Boost skill(s).
If a task needs a Boost skill the installation lacks, the companion says so rather than improvising the
missing baseline.

It activates for implementation and review work that needs this stack's concrete conventions:
composing or reviewing a controller, Form Request, Action, Policy, or Resource; adding index
filtering or sorting; writing or organizing a Pest test; defining an Eloquent local scope, a migration
column, or a backed enum's option list; generating factory or seeder data; or wiring a Laravel endpoint
to a new Inertia page component.

## 2. Ownership model

Three parties hold three distinct areas of responsibility:

| Owner | Owns |
|---|---|
| **Laravel Boost** (`laravel-best-practices`, `testing-best-practices`, `inertia-vue-development`) | The first-party Laravel/Pest/Inertia-Vue baseline — validation, Eloquent mechanics, resource/CRUD organization, the thin-controller principle, migrations in general, layer-ownership test de-duplication, record-level test-data minimalism, test-suite performance settings, security, style. An external dependency whose mechanics are not re-taught here. |
| **`laravel-inertia-stack`** | The durable, opinionated conventions for this stack, verified framework behavior Boost does not teach, implementation blueprints, and reusable templates — portable across compatible consuming projects by copy/reinstall. |
| **Consuming project** | Its own domain model, product rules, repository policy, established conventions, and any project-specific adaptation of a blueprint or template — tenancy mechanism, UI decisions such as flash-message presentation, deployment conventions. These live in the project's code, instruction files, and recorded project rules; none of it is the skill's to prescribe. |

The companion relates to Boost in three ways, and the distinction is part of each rule's meaning:

- **Extends** — covers what Boost does not address: Action payload shapes, child-resource authorization,
  option projections, Inertia form serialization, Precognition's lifecycle, tenancy leak paths, factory
  realism, and similar verified framework behavior.
- **Specializes** — turns a Boost principle into a concrete stack shape: layer ownership mapped onto
  Actions, Filters, Sorters, and Resources; the known-value assertion rule refined for Resource
  comparison macros; `<Form>` preferred over `useForm()`.
- **Overrides** — deliberately chooses a different default: Actions for every mutation, Form Requests
  for every validated input, `#[Authorize]` attributes, plural resource controllers, `tests/Feature` for
  framework-dependent tests, and endpoint-oriented HTTP test files. The owning rule states the override
  and its reason in one sentence, as a durable position rather than commentary on an upstream version.

Precedence follows ownership. An established project convention wins. The companion's conventions are
the defaults where the project has no established position, as in a fresh application, and conditional
patterns are introduced when a feature first needs them. Starter-kit and package-contract code keeps the
shape its framework or package requires. There is no list of conventions that override a project's own
decisions; even the `#[Scope]` preference distinguishes new code without a project position,
compatibility with a project's established style, and an incremental migration the project has
explicitly adopted.

Rules signal their strength through wording rather than metadata: "must"/"never" for correctness,
security, and data-integrity requirements; plain imperatives for stack defaults; "prefer" for
preferences; a leading "when" for conditional patterns; plain statements for framework behavior. The
clearest case is `rules/resources.md`, which separates the invariant (no prop carries data the user may
not see) from the convention that meets it (an explicit response projection).

A corollary of this split: `laravel-inertia-stack` states several of its own conventions as conditional
rather than universal — tenancy, filters/sorters, non-CRUD controller shapes, and the Inertia page boundary.
That conditionality is a deliberate architectural boundary between what this skill can responsibly
generalize and what only a concrete project can decide, not an omission to tighten later.

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

[`blueprints/resource-controller.md`](../skills/laravel-inertia-stack/blueprints/resource-controller.md)
states the reference composition — **Controller → Form Request → Policy/`#[Authorize]` → Action →
Resource → Inertia/HTTP response** — and immediately qualifies it: this is a reference shape a full
CRUD endpoint follows, not a mandatory sequence every endpoint must implement in full. Each stage is
included only when the endpoint actually needs what it does, and the blueprint treats single-action
controllers, non-Inertia responses (a binary export), a Resource returned directly from an XHR
endpoint, and a controller implementing fewer than the seven resourceful methods as first-class
shapes — not exceptions to patch around. It also owns controller naming: plural resource segments
for resource, nested, and single-action controllers, singular only for a singleton resource. A
business operation on an existing resource gets a single-action controller; an operation that is
really an independent resource with its own lifecycle gets that resource's controller. Within this
composition:

- The **Form Request** owns validation for every validated input, including small rule sets, and
  request normalization
  ([`rules/request-normalization.md`](../skills/laravel-inertia-stack/rules/request-normalization.md))
  — `prepareForValidation()` is where coercion and defaulting happen once, so an Action or Filter
  can trust `validated()` as already correct rather than re-defaulting downstream.
- **Authorization** is declarative and resolved before the method body runs
  ([`rules/authorization.md`](../skills/laravel-inertia-stack/rules/authorization.md)) — the
  `#[Authorize]` attribute rather than an inline `$this->authorize()` call, with the array form
  required specifically for `create`/`viewAny` on a child resource, where no bound instance exists
  yet to infer a policy from.
- The **Action** owns the mutation itself
  ([`rules/actions.md`](../skills/laravel-inertia-stack/rules/actions.md)) — a fixed `handle()`
  entry point, no HTTP-layer globals inside it, a transaction where several writes must be atomic,
  and external side effects deferred with `->afterCommit()` so they never execute until the
  enclosing transaction actually commits.
- The **Resource** owns the response contract
  ([`rules/resources.md`](../skills/laravel-inertia-stack/rules/resources.md)) — the invariant that
  no prop carries data the user may not see, met by the convention of an explicit projection rather
  than a serialized model or query result; a relation field is exposed through `whenLoaded()`, never
  a bare accessor or a model-wide `$with`, so the Resource stays safe regardless of which caller
  reaches it.
- The **Inertia page boundary** owns one small but important cross-layer invariant
  ([`rules/inertia-pages.md`](../skills/laravel-inertia-stack/rules/inertia-pages.md)) — when a Laravel endpoint
  introduces a new Inertia component name, the corresponding Vue page component must exist in the same
  implementation boundary. If the real frontend belongs to a later issue, a minimal placeholder is
  acceptable; the issue should not fail simply because the named page does not exist yet.

### Filtering and sorting

[`blueprints/filters-and-sorting.md`](../skills/laravel-inertia-stack/blueprints/filters-and-sorting.md) is itself
conditional — loaded only when an index endpoint genuinely needs filtering or sorting, not a mandatory
part of every controller. It composes: query-parameter validation in the Form Request (including the
`direction` default from `rules/request-normalization.md`, since `QuerySorter`'s constructor takes a
non-nullable `string`); a concrete `{Model}Filter`/`{Model}Sort` class per model; the reusable
`QueryFilter`/`QuerySorter` base classes and `Filterable`/`Sortable` model traits shipped as templates;
and controller-level query composition that stays a no-op when no query params are present. Filter and
Sorter classes never validate — they trust an already-validated value exactly as an Action trusts
`validated()`.

### Testing

Three distinct decisions compose here, deliberately kept apart:

- [`blueprints/pest-testing.md`](../skills/laravel-inertia-stack/blueprints/pest-testing.md) owns the
  **execution-boundary configuration** — classifying `tests/Unit` versus `tests/Feature` by what a
  test actually boots (database, container, facades), confirming what the project's own
  `tests/Pest.php` binds before trusting a directory name, and the safe order for narrowing that
  binding. It also owns endpoint-oriented HTTP test-file
  organization, the warning against building a test's expected value from the same production Resource
  it's supposed to verify, gating optional Pest capabilities (TIA, architecture testing) behind
  what a project actually has installed, global-class imports in namespace-free test files, and
  absence assertions over rendered output that can contain random identifiers.
- [`rules/test-ownership.md`](../skills/laravel-inertia-stack/rules/test-ownership.md) owns **per-layer test
  responsibility** — the concrete Action/Policy/Filter/Sorter/Resource/Model/HTTP location-and-scope
  mapping, when to assert existence versus an exact persisted value, and the no-redundancy rule that a
  higher layer proves only what a lower layer doesn't already prove (with the minimal-wiring exception:
  an HTTP test may keep one persisted identity/association assertion to prove the correct route-bound
  model, actor, or pivot pair reached the Action — a bare row-count assertion cannot prove that).
- [`rules/test-execution.md`](../skills/laravel-inertia-stack/rules/test-execution.md) owns **how
  the suite runs** — what to measure before restructuring tests, the canonical full-suite and
  coverage commands, runner flags passed through a wrapper, impact analysis, cached state in tests,
  what to check before changing the database refresh strategy, and verifying what a run executed.
  Version-specific behavior appears there only as labeled examples to recheck. Boost's
  `testing-best-practices` keeps the baseline performance settings it already owns.

A test file therefore answers "where does this test physically live and what does the suite boot for
it" from the blueprint, and "what does this specific layer's test assert, and where does its
responsibility stop" from the rule — two different questions with two different owners, composed
rather than duplicated. How the suite runs is a third question, owned by `rules/test-execution.md`;
neither the blueprint nor the ownership rule restates it.

### Supporting rules

The remaining rules apply independently wherever their narrow subject appears: computed Eloquent
`Attribute` accessors and the scope-style decision
([`rules/eloquent-attributes.md`](../skills/laravel-inertia-stack/rules/eloquent-attributes.md)) —
`#[Scope]` where the project has no established position, the project's established style otherwise,
and new attribute scopes alongside legacy ones only once the project has explicitly adopted an
incremental migration; `when()` over an `if` block for a mid-chain query conditional
([`rules/query-conditionals.md`](../skills/laravel-inertia-stack/rules/query-conditionals.md)); a
static `all()` on a backed enum instead of mapping `::cases()` at each call site
([`rules/enum-options.md`](../skills/laravel-inertia-stack/rules/enum-options.md)); deriving
dependent factory fields from one source of truth and structuring dev-only seeders
([`rules/factories-and-seeders.md`](../skills/laravel-inertia-stack/rules/factories-and-seeders.md));
`final`-by-default concrete application classes
([`rules/php-conventions.md`](../skills/laravel-inertia-stack/rules/php-conventions.md)); and
non-nullable-by-default migration columns, including why `->notNull()` silently does nothing across
every schema grammar ([`rules/migrations.md`](../skills/laravel-inertia-stack/rules/migrations.md)).

## 5. Single-owner boundaries

Every architectural decision in this package has exactly one file that states it; every other file
that touches the same territory cross-references that owner instead of restating it:

| Decision | Owner |
|---|---|
| Relationship to Boost, precedence against project conventions, adoption in a fresh application, and how rule wording signals strength | `SKILL.md` |
| An Action's own shape — naming, `handle()`, the `$attributes` PHPDoc derivation, transaction/`afterCommit()` discipline | `rules/actions.md` |
| How Controller, Form Request, Policy, Action, Resource, and response compose into one endpoint; controller naming; redirect and flash-data principles | `blueprints/resource-controller.md` |
| `#[Authorize]` mechanics, including the child-resource array-form requirement | `rules/authorization.md` |
| The exposure invariant, the explicit-projection convention, the JsonResource contract, and safe relation exposure | `rules/resources.md` |
| Where input coercion/defaulting happens | `rules/request-normalization.md` |
| The multi-component filter/sorter wiring across Form Request, model, and controller | `blueprints/filters-and-sorting.md` |
| `tests/Unit`/`tests/Feature` execution-boundary classification and suite binding | `blueprints/pest-testing.md` |
| Concrete per-class test location, ownership, and the no-redundancy rule | `rules/test-ownership.md` |
| How the suite runs: measuring before restructuring tests, full-suite and coverage commands, runner flags through a wrapper, impact analysis, cached state in tests, changing the database refresh strategy, run verification | `rules/test-execution.md` |
| Model responsibility and calculation placement; computed Eloquent attributes; scope style (`#[Scope]` vs. prefixed) | `rules/eloquent-attributes.md` |
| Mid-chain query conditionals | `rules/query-conditionals.md` |
| Backed-enum option lists | `rules/enum-options.md` |
| Factory/seeder realism and structure | `rules/factories-and-seeders.md` |
| Concrete-class finality | `rules/php-conventions.md` |
| Migration column nullability | `rules/migrations.md` |
| Backend-to-Inertia page-component boundary | `rules/inertia-pages.md` |
| Global-scope tenancy, including explicit tenant boundaries outside HTTP | `rules/global-scope-tenancy.md` |

This matters because two files that each describe part of the same decision can drift independently
while each still assumes the other owns it. The clearest example still visible in the package's shape
is the test-ownership split above: `blueprints/pest-testing.md` states outright that it does not
restate the concrete class-taxonomy mapping, and `rules/test-ownership.md` states that it does not
restate the general execution-boundary or de-duplication principles already owned elsewhere. A
cross-reference composes the two into one coherent testing story without either file duplicating the
authority.

## 6. Templates

Five templates, each a complete, syntactically valid PHP implementation rather than a placeholder or
generator stub:

- [`templates/app/Filters/QueryFilter.php`](../skills/laravel-inertia-stack/templates/app/Filters/QueryFilter.php)
  — the abstract base every domain filter extends. Dispatch is convention over configuration:
  `apply()` camel-cases each validated array key and calls the same-named method on the concrete
  filter, silently skipping a key with no matching method or a `null`/`''` value.
- [`templates/app/Models/Concerns/Filterable.php`](../skills/laravel-inertia-stack/templates/app/Models/Concerns/Filterable.php)
  — the trait wiring a `#[Scope]`-based `filter` scope onto a model, delegating to an injected
  `QueryFilter`.
- [`templates/app/Sorts/QuerySorter.php`](../skills/laravel-inertia-stack/templates/app/Sorts/QuerySorter.php)
  — the abstract base every domain sorter extends. Resolves a requested column the same way
  `QueryFilter` resolves a key, falls back to an abstract `default()` implementation the concrete
  sorter must supply, and always breaks ties on the model's qualified primary key so pagination and
  tests get a stable order regardless of the database's query plan, and a sort that joins another
  table stays unambiguous.
- [`templates/app/Models/Concerns/Sortable.php`](../skills/laravel-inertia-stack/templates/app/Models/Concerns/Sortable.php)
  — the trait wiring a `#[Scope]`-based `sort` scope onto a model, delegating to an injected
  `QuerySorter`.
- [`templates/app/Providers/TestingServiceProvider.php`](../skills/laravel-inertia-stack/templates/app/Providers/TestingServiceProvider.php)
  — registers five Inertia-testing Pest macros (`hasResource`, `hasPaginatedResource`,
  `assertHasResource`, `assertHasPaginatedResource`, `assertHasInertiaFlash`), guarded by a
  `runningUnitTests()` boot check so they exist only while the test suite runs.
  `assertHasInertiaFlash` asserts one key of Inertia's flash data, so it carries no
  application-specific flash contract.

Each carries its own prerequisites inline: the `#[Scope]`-based traits require confirming that the
target project's installed `laravel/framework` version actually provides
`Illuminate\Database\Eloquent\Attributes\Scope`; the filter/sorter templates require the paired
base-class-and-trait pairing to be installed together; the testing provider requires
`inertiajs/inertia-laravel` (with `Inertia::flash()` for the flash macro) and Pest, and must be
registered in `bootstrap/providers.php`. Every
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
for them. Tenancy mechanism, flash-message presentation, UI-framework specifics, and deployment
conventions are project-owned decisions this skill deliberately does not prescribe, and a project's
established naming takes precedence over the stack's naming defaults — where a blueprint discusses
tenancy, for example, it identifies the questions a multi-tenant project must answer (read scoping,
authorization, creation-time assignment, route-model isolation) without naming which mechanism a
project must use to answer them.

## 8. Boundaries and confidence

The skill's Laravel, Inertia, and Pest guidance has been checked against real implementation and
verification work, not authored and left untested. That confidence does not extend to broad,
multi-project portability. Most rules rest on one consuming project. A second, model-less consuming
project started from a fresh application, and inspection of its code shows the Action, Form Request,
and class-finality conventions establishing its architecture from the start; it does not exercise the
Eloquent, Resource, filtering, or tenancy guidance.

The plural resource-controller naming is an approved stack convention matching one consuming project's
resource and nested controllers. It is declared explicitly because examples alone did not carry it.

The flash macro and the sorter's qualified tie-breaker are verified by a scripted harness against
installed framework and Inertia packages, and the column ambiguity the qualified key prevents is
reproduced on MySQL. This is runtime evidence for the templates themselves, not evidence from a
consuming project's suite.

`rules/test-execution.md` rests on measurements from one consuming project's suite and on reading the
Pest 5 and Collision 8 sources. Its decisions are a working conclusion pending evidence from another
project. Its version-specific examples were confirmed against those sources only, and the rule tells
readers to recheck them against installed versions.

The preference for explicit tenant boundaries in context-independent Actions is an approved
stack convention based on design review in one consuming project. Its proposed implementation
has not yet been verified in that project; it is conditional on the complete operation being
independent of ambient context.

Engineering judgment in the runtime entrypoint governs architectural choices across the
stack rather than adding a separate procedure. It is written as portable methodology, as is part of
the testing guidance (consolidating tests by behavior, measuring before restructuring a suite,
verifying what a run executed). Both stay resident in this stack companion because their evidence
comes from one stack; they move only if another stack companion supplies evidence that they hold
there too. It is an approved convention supported by
reported design iteration and targeted implementation verification in one consuming project;
generalization to other projects and independent skill-driven behavior remain unvalidated.
Proportionality of safeguards is an approved extension informed by concurrency design review.
It does not prescribe a particular concurrent-edit policy or waive integrity guarantees.
The simplified concurrency design has not yet been verified in implementation.

The preference for focused models and support classes for context-dependent calculations
is an approved stack convention informed by design review in one consuming project.
The revised implementation is not yet verified. It is a placement preference, not a ban
on model domain methods or a requirement to introduce support classes for local behavior.

Vue 3 is part of the declared stack boundary. The Vue guidance here is limited to the Laravel/Inertia
boundary — custom-control serialization and bounds in `rules/inertia-forms.md`, page existence in
`rules/inertia-pages.md`. Other Vue implementation questions route to `inertia-vue-development` rather
than to this skill filling the gap with improvised guidance.

These limitations bound the current confidence claim and should be revisited as the package gains
broader consumer evidence; a resolved finding is not carried forward here once corrected in the rule,
blueprint, or template file it belonged to.
