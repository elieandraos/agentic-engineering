# my-laravel-stack — Skill Dossier

Status: Current
Scope: `my-laravel-stack` as it stands at `agentic-engineering@main` (`4609cd50eb4f002036b5e1eb9e8a5c4ab01e7121`)
Purpose: Supporting analysis of the current skill — purpose, ownership boundaries, package
architecture, evidence, authoring history, and open questions. The operational authority remains
`my-laravel-stack/SKILL.md`, its `rules/`, `blueprints/`, and `templates/` files — this document is
supporting analysis, not a runtime instruction file and not a changelog. Canonical authoring is
complete; the refresh into `useOrbit` and the consumer exercise are still pending.

## 1. Purpose and status

This is supporting analysis, not the operational skill. `SKILL.md`, `README.md`, and the files under
`rules/`, `blueprints/`, and `templates/` remain the authoritative source of what the skill says and
does; where anything here disagrees with them, this document is stale, not the other way around. It
describes the skill as it currently stands. `phase-d-stack-synthesis.md` and the authoring commits
between it and the current endpoint appear only where they explain why a current contract is shaped
the way it is — never as a chronological account of how the skill got here. This is not an operational
rule file, not a `SKILL.md` replacement, not a change log, and not an invitation to reopen the
completed authoring pass.

## 2. Purpose and boundary

`my-laravel-stack` is a personal, portable companion for a **Laravel + InertiaJS + Vue 3 + Pest**
stack. It carries evidence-backed conventions, implementation blueprints, and reusable code templates
established for that stack — the delta genuinely additive to Laravel Boost, never a standalone Laravel
education.

- It loads **alongside** Laravel Boost's `laravel-best-practices` and `testing-best-practices`, and
  alongside `inertia-vue-development`, never instead of them. It contains only what those skills don't
  already cover.
- **Current evidence is strongest for Laravel, Inertia, and Pest.** Every conventions, blueprint, and
  template file in the current tree rests on verified application behavior, tests, or framework source.
- **Vue 3 is part of the declared stack boundary, but the skill currently owns no mature independent
  Vue-specific rules.** This is stated openly in both `SKILL.md` and `README.md`, not implied as equal
  coverage. Vue implementation questions route to `inertia-vue-development` instead.
- It is **stack knowledge**, not portable cross-stack methodology (that is `skill-audits/
  skill-authoring-methodology.md`'s domain) and not `useOrbit` project documentation (that belongs to
  `useOrbit` itself, not this repository).

## 3. Three-layer ownership model

| Layer | Owns |
|---|---|
| **Laravel Boost** (`laravel-best-practices`, `testing-best-practices`, `inertia-vue-development`) | The general Laravel/Pest/Inertia-Vue baseline: validation, Eloquent mechanics, resource/CRUD controller organization, thin-controller and FormRequest-boundary philosophy, migrations, layer-ownership test de-duplication, record-level test-data minimalism, security, style. External dependency — never extracted, renamed, or duplicated into this skill. |
| **`my-laravel-stack`** | The verified custom stack delta: conventions, implementation blueprints, and reusable support templates genuinely additive to Boost. Travels across this user's projects by copy/reinstall. |
| **Consuming projects** (e.g. `useOrbit`) | Installed/adapted implementations of the skill's blueprints and templates, plus genuinely project-specific decisions (product facts, literals, one-off rules with no cross-project generality claim). |

`useOrbit` supplied the empirical evidence this skill's content was verified against (§8), but that
does not make `useOrbit`'s own implementation choices universally correct — a project's specific
tenancy mechanism, pagination size, or route naming is evidence for what one real project did, not a
portable rule this skill imposes on every consumer. Where the skill states a delta as conditional
(tenancy, filters/sorters, non-CRUD shapes), that conditionality is deliberate, not an oversight to
tighten later.

`my-phpstorm-conventions` is a separate, fully deferred companion (IDE/static-analysis knowledge) — not
a fourth layer of this architecture and not touched by this pass.

## 4. Package architecture

Content is classified by purpose, not forced into one prose-rule shape:

- **`rules/`** — independently applicable conventions and invariants. Each file stands alone: a rule
  about Eloquent scope attributes, request normalization, or PHP class finality doesn't require any
  other file to make sense.
- **`blueprints/`** — multi-component implementation shapes that compose several rules and
  responsibilities into one recognizable pattern, such as a full controller composition or a Pest test
  taxonomy. A blueprint is where several rules meet in one worked structure.
- **`templates/`** — complete, installable PHP starting points structured to mirror their intended
  project-relative path (`templates/app/...` mirrors `app/...` in a consuming project). These are
  inspected, reconciled against whatever a project already has, and copied or adapted — never installed
  blindly on the assumption a project has nothing there already.

**`README.md` vs. `SKILL.md`.** `README.md` is the human-facing conceptual map: what the skill is (and
isn't), the three-kind content model, what's here today at a glance, and the general installation
discipline for a template. `SKILL.md` is the operational activation and routing entrypoint — the
frontmatter description, activation conditions, and the routing table that sends a given task to
exactly the file(s) it needs. The two are read together during reconciliation specifically to confirm
they stay complementary rather than duplicating each other: `README.md` never repeats `SKILL.md`'s
routing table, and `SKILL.md` never repeats `README.md`'s conceptual framing.

Current tree:

```text
my-laravel-stack/
├── README.md
├── SKILL.md
├── blueprints/
│   ├── filters-and-sorting.md
│   ├── pest-testing.md
│   └── resource-controller.md
├── rules/
│   ├── actions.md
│   ├── authorization.md
│   ├── eloquent-attributes.md
│   ├── enum-options.md
│   ├── factories-and-seeders.md
│   ├── migrations.md
│   ├── php-conventions.md
│   ├── query-conditionals.md
│   ├── request-normalization.md
│   ├── resources.md
│   └── test-ownership.md
└── templates/app/
    ├── Filters/QueryFilter.php
    ├── Models/Concerns/Filterable.php
    ├── Models/Concerns/Sortable.php
    ├── Providers/TestingServiceProvider.php
    └── Sorts/QuerySorter.php
```

## 5. Operational ownership

The skill's architectural centers of gravity, without reproducing every runtime rule:

- **Conditional Resource Controller composition** (`blueprints/resource-controller.md`) — Controller →
  Form Request → Policy/`#[Authorize]` → Action → Resource → Inertia/HTTP response, stated explicitly as
  a *reference composition*, not a mandatory sequence: an endpoint includes only the components it
  actually needs, and single-action, non-Inertia, and partial-resourceful controllers are first-class,
  not exceptions to the shape.
- **Action conventions** (`rules/actions.md`) — naming/location, the fixed `handle()` entry point, the
  `$attributes` PHPDoc-shape derivation (presence and nullability and type are three independent
  questions, never inferred from a validation rule name alone), no HTTP-layer globals inside `handle()`,
  and the `DB::transaction()`/`->afterCommit()` discipline for external side effects.
- **`#[Authorize]` authorization** (`rules/authorization.md`) — the attribute over `$this->authorize()`,
  never adding `AuthorizesRequests` to the base controller, and the array-form requirement for a child
  resource's `create`/`viewAny` where no bound instance exists yet.
- **Resource boundaries** (`rules/resources.md`) — a JsonResource always sits between the query and the
  view; `whenLoaded()` over a bare accessor or model `$with` for any relation field.
- **Form Request normalization** (`rules/request-normalization.md`) — coercion and defaulting belong in
  `prepareForValidation()`, not `??` fallbacks scattered across the controller.
- **Filters/sorting composition and templates** (`blueprints/filters-and-sorting.md` +
  `templates/app/Filters/QueryFilter.php`, `templates/app/Sorts/QuerySorter.php`,
  `templates/app/Models/Concerns/{Filterable,Sortable}.php`) — a multi-component blueprint: query-param
  validation, concrete Filter/Sorter classes, reusable base-class and trait templates, model scope
  wiring, and controller query composition, explicitly optional and loaded only when an index endpoint
  needs it.
- **Pest execution-boundary blueprint** (`blueprints/pest-testing.md`) — classify by execution boundary
  first (does the suite's own `tests/Pest.php` actually isolate `Unit` from `Feature`, or bind both to
  the database?), then mirror the owning application area; preserve endpoint-oriented HTTP test files;
  the self-referential-expected-value warning against building a test's expected value from the same
  production Resource under test; capability-gate optional Pest plugins.
- **The separate test-ownership rule** (`rules/test-ownership.md`) — the single source of truth for
  where each class type's test lives, what each layer owns, existence-versus-exact-value assertion
  choice, and the no-redundancy boundary between HTTP tests and the lower layers they must not duplicate.
- **Supporting conventions** — final-by-default concrete classes (`rules/php-conventions.md`), `when()`
  over `if` for mid-chain query conditionals (`rules/query-conditionals.md`), enum `all()` over
  inline `::cases()` mapping (`rules/enum-options.md`), realistic dependent-field factories and seeder
  structure (`rules/factories-and-seeders.md`), Eloquent `#[Scope]` over the legacy `scope`-prefixed
  method name (`rules/eloquent-attributes.md`), and non-nullable-by-default migration columns with the
  `->notNull()` correctness warning (`rules/migrations.md`).

The full controller pipeline is a reference composition, not a checklist every endpoint must satisfy in
full; filters and sorting are optional capabilities loaded only when an index endpoint needs them;
tenancy guidance in `blueprints/resource-controller.md` applies only when a consuming project is
actually multi-tenant, and prescribes no single mechanism; optional Pest capabilities (TIA, arch
testing, `LazilyRefreshDatabase`) must be detected in the consuming project before use, never assumed;
and every template requires inspecting and reconciling an existing project implementation before
installing, never a blind copy.

## 6. Single-owner model

Final ownership decisions, each stated once and cross-referenced rather than restated:

- **`rules/actions.md`** owns an Action's own conventions — naming, `handle()`'s shape, the
  transaction/`afterCommit()` discipline. It does not restate the controller composition an Action sits
  inside; that's `blueprints/resource-controller.md`'s job.
- **`blueprints/resource-controller.md`** owns how controllers, Form Requests, authorization, Actions,
  Resources, and responses compose into one endpoint — not any single component's own internal rules,
  each of which it cross-references instead of restating.
- **`rules/test-ownership.md`** owns concrete test locations, per-layer behavior, assertion selection
  (existence vs. exact value), and the no-redundancy rule between HTTP tests and lower layers — the
  single source of truth for this stack's Action/Controller/Policy/Filter/Sorter/Resource/Model
  taxonomy.
- **`blueprints/pest-testing.md`** owns suite structure: the Unit/Feature execution-boundary taxonomy,
  endpoint-oriented HTTP test-file organization, the Resource-assertion self-reference warning, the
  reusable Inertia testing macros, and Pest capability gating. It explicitly does not restate the
  concrete class-ownership mapping `rules/test-ownership.md` owns.
- **`blueprints/filters-and-sorting.md`** owns the multi-component filter/sorter implementation shape —
  the wiring across a Form Request, concrete Filter/Sorter classes, the reusable base-class/trait
  templates, model scope wiring, and controller composition.

This boundary matters because two files that each describe part of the same decision can drift
independently while each still believes the other owns it — the exact failure the authoring pass
corrected once (§8): `blueprints/pest-testing.md` originally duplicated `rules/test-ownership.md`'s
concrete ownership mapping and existence-vs-exact-value rule; the consistency pass removed the
duplicate from the blueprint and left the rule as sole owner.

## 7. Templates

Five current templates, each a valid, complete PHP implementation, not a generator stub:

- **`templates/app/Filters/QueryFilter.php`** — the abstract base class every domain filter extends;
  convention-over-configuration dispatch (`Str::camel()`s a validated array key onto a same-named
  method), silently skipping a key with no matching method or a `null`/`''` value.
- **`templates/app/Models/Concerns/Filterable.php`** — the trait wiring a `#[Scope]`-based `filter` scope
  onto a model, delegating to an injected `QueryFilter`.
- **`templates/app/Sorts/QuerySorter.php`** — the abstract base class every domain sorter extends;
  resolves a requested column the same way `QueryFilter` resolves a key, falls back to an abstract
  `default()` implementation, and breaks ties on the model's primary key for stable pagination.
- **`templates/app/Models/Concerns/Sortable.php`** — the trait wiring a `#[Scope]`-based `sort` scope
  onto a model, delegating to an injected `QuerySorter`.
- **`templates/app/Providers/TestingServiceProvider.php`** — registers five Inertia-testing Pest macros
  (`hasResource`, `hasPaginatedResource`, `assertHasResource`, `assertHasPaginatedResource`,
  `assertHasInertiaFlash`), guarded by a `runningUnitTests()` boot check so the macros exist only while
  the suite runs.

They remain `.php` files, not `.stub` files, because they represent intended final implementations —
each is syntactically valid PHP that can be lint-checked and reasoned about directly, not a
placeholder-substitution artifact. Calling something a generator stub is accurate only when an actual
generator or substitution contract consumes named placeholders; none of these five files has one.
Their project-relative directory structure (`templates/app/Filters/...` mirroring `app/Filters/...`)
mirrors their intended installation path directly, and each file's own docblock states its target path,
its prerequisites (a required Laravel version for the `#[Scope]` attribute; the paired trait or base
class it depends on), and the reconciliation instruction to check for an existing equivalent before
installing. This is not a universal claim that every skill should ship a `templates/` directory —
it is this skill's evidence-backed answer for content that is complete, installable PHP rather than
prose guidance.

## 8. Evidence and authoring history

- **Phase D discovery and synthesis** (`phase-d-stack-discovery.md`, `phase-d-stack-synthesis.md`)
  supplied the initial classification and evidence: full reads of `useOrbit`'s controllers, Form
  Requests, Actions, Policies, Resources, and Pest test tree; the complete installed
  `laravel-best-practices`/`testing-best-practices` rule files (Boost v2.7.0); and the installed Laravel
  framework source (v13.29.0) for the migration-nullability finding.
- **The authoring pass** (`ee72858` through `4609cd5`, eight commits scoped to `my-laravel-stack/`)
  rewrote the gitignored origin skill into the current tree, then corrected it across several rounds:
  Action HTTP/transaction accuracy, `destroy()` routed through an Action, testing-taxonomy wording,
  provider finality (`43b5d8a`); the PHPDoc typing-derivation model (presence, nullability, and type as
  three independent questions) and the `afterCommit()`/transaction model (`2778643`); a narrower
  database-queue-driver caveat (`1cdfd46`); the `rules/`/`blueprints/`/`templates/` taxonomy plus
  `README.md` (`8c5f8ef`); a README wording fix (`38a4d0a`); and a whole-skill consistency pass renaming
  `test-ownership.md`, promoting `filters-and-sorting.md` to a blueprint, and clarifying the controller
  composition as a reference shape (`59c9b9b`), followed by one further rename correcting
  `actions-pattern.md` to `actions.md` (`4609cd5`).
- **The owner reviewed the macro structure and rule content** during this pass, prompting the
  Action/provider corrections in `43b5d8a` and `2778643` rather than leaving the initial authored draft
  as final.
- Current endpoint: `4609cd50eb4f002036b5e1eb9e8a5c4ab01e7121`.

Keep `useOrbit` evidence here, in this dossier, never in the runtime skill's public-facing examples —
`SKILL.md` states this explicitly, and every code example across `rules/` and `blueprints/` uses
neutral, invented domain concepts (orders, customers, tasks, projects) rather than `useOrbit`'s own
models, routes, or literals.

## 9. Authoring observations

Reusable lessons from this pass are consolidated in `skill-audits/skill-authoring-methodology.md`. This
dossier retains only the skill-specific evidence for them:

- **One canonical owner per decision** — demonstrated by the `test-ownership.md`/`pest-testing.md`
  duplication found and corrected in `59c9b9b` (§6).
- **Semantic classification over historical filenames** — `filters-pattern.md` lived under `rules/`
  from the initial authoring commit but was always a multi-component implementation shape; it was
  reclassified to `blueprints/filters-and-sorting.md` in the consistency pass. `actions-pattern.md`
  stayed a rule throughout, but its `-pattern` filename incorrectly suggested blueprint semantics and
  was corrected to `actions.md` in `4609cd5` — a distinct, later correction from the same taxonomy pass
  that reclassified the filter file, not the same fix applied twice.
- **Conditionality must survive diagrams, summaries, examples, and blueprints** — `59c9b9b` corrected
  `blueprints/resource-controller.md`'s opening composition statement to say explicitly that the full
  Controller → Form Request → Policy → Action → Resource → Inertia chain is a reference composition,
  not a mandatory sequence, even though the file's own later sections already documented non-CRUD and
  single-action controllers that omit stages of it.
- **Examples must remain coherent across a skill** — `rules/resources.md`'s single-resource example was
  standardized to `OrderResource::make($order)` in the same consistency pass, matching
  `blueprints/resource-controller.md`'s and `blueprints/pest-testing.md`'s own usage rather than leaving
  an inconsistent construction style across files that all illustrate the same Resource contract.
- **Cross-directory references need unambiguous paths and actual validation** — moving the two
  blueprints and renaming `assets/app` to `templates/app` in `8c5f8ef` required updating `SKILL.md`'s
  routing table, every blueprint-to-rule and rule-to-blueprint cross-reference, and every template
  installation path in the same commit, not a partial move left for a later pass to reconcile.
- **A README is justified when it supplies a necessary human-facing conceptual map** — `8c5f8ef` added
  `README.md` specifically to explain the `rules`/`blueprints`/`templates` taxonomy and installation
  discipline for a human maintainer, distinct from `SKILL.md`'s routing table, which stays focused on
  activation and file selection.
- **Complete copy/adapt implementations are templates, not generator stubs** — the five `.php` files
  under `templates/app/` were kept as complete, syntactically valid implementations with inline
  installation docblocks, never abstracted into a placeholder-substitution format no generator actually
  consumes (§7).

## 10. Known boundaries and pending evidence

Stated honestly, not carried forward as resolved or silently dropped:

- **The current canonical skill has not yet been refreshed into `useOrbit`.** Nothing in this pass
  touched `useOrbit`.
- **Template parity with `useOrbit`'s existing implementations has not yet been rechecked against this
  final canonical version.** `phase-d-stack-synthesis.md` recorded that `useOrbit` already has working
  equivalents of all five templates; whether the current, corrected template content still matches
  those implementations exactly is unverified since this authoring pass's corrections.
- **The two-stage consumer exercise remains pending**: (1) a no-edit, repository-wide conformance audit
  of `useOrbit`'s current controllers and Pest tests against the authored blueprints; (2) a reviewed
  real consumer exercise, beginning with the test-directory organization and later the representative
  Clients CRUD slice, as approved.
- **Restructuring `useOrbit`'s test directory is a real application mutation, not a read-only smoke
  test**, and must be proposed and approved before execution — it is not authorized by this
  documentation pass.
- **No second Laravel/Inertia/Vue/Pest consumer has validated portability.** Every piece of evidence
  behind this skill's content comes from exactly one real project, `useOrbit`, plus Laravel Boost's and
  the Laravel framework's installed source.
- **Independent Vue-specific guidance remains unproven.** The skill declares Vue 3 as part of its stack
  boundary but currently owns no mature Vue-specific rule (§2).
- **`my-phpstorm-conventions` remains separate and deferred**, untouched by this pass.

Resolved, and not to be presented as current defects: the prior README absence; the
`assets`/`templates` naming and blueprint-location questions; the former duplication between
`blueprints/pest-testing.md` and `rules/test-ownership.md`; the `resources.md` example's inconsistent
Resource-construction style (`new OrderResource(...)` versus `OrderResource::make(...)`), now
standardized to `OrderResource::make(...)` everywhere; and the retired filenames
(`actions-pattern.md`, `filters-pattern.md`, `testing-strategy.md`, `resource-controller-blueprint.md`,
`pest-testing-blueprint.md`, `assets/app/**`) — none exist in the current tree.

## 11. Current assessment

**Architectural coherence.** Strong for the current scope. The `rules`/`blueprints`/`templates`
taxonomy tracks a real distinction (independently applicable convention vs. multi-component composed
shape vs. complete installable implementation), and no file in the current tree claims ownership of a
decision another file already owns (§6).

**Authoring quality.** The pass corrected real technical defects found during the work itself (the
PHPDoc typing/nullability model, the `afterCommit()` transaction model, provider finality), removed
every `useOrbit` fingerprint from public examples, and completed a whole-skill consistency pass that
caught a real cross-file duplication and a stale example construction style. Nothing in the current
tree carries an unresolved contradiction between its opening framing and its own later content.

**Laravel/Inertia/Pest maturity.** Evidence-backed and current for the concrete delta this skill
targets: controller composition, Action conventions, authorization, Resources, request normalization,
filters/sorting, and Pest test ownership all rest on verified `useOrbit` code and Boost/framework
source, not invented convention.

**Template readiness.** The five templates are complete, syntactically valid PHP with explicit
prerequisites and reconciliation instructions — ready to inspect and adapt into a project, but not yet
re-verified against `useOrbit`'s current live implementations since this pass's corrections (§10).

**Portability confidence.** Moderate, not proven. Every piece of evidence traces to one real consumer.
The skill states this limit openly rather than implying broader validation.

**Remaining consumer-validation risk.** The two-stage consumer exercise (conformance audit, then the
Clients CRUD slice) is the next real test of whether these blueprints hold up against actual
implementation work, not merely internal coherence. Until that exercise runs, this skill should be read
as evidence-backed and internally consistent, not as consumer-validated.
