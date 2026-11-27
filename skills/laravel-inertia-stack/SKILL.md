---
name: laravel-inertia-stack
description: "Companion conventions for a Laravel + InertiaJS + Vue 3 + Pest stack, loaded alongside Laravel Boost's laravel-best-practices and testing-best-practices skills — never a replacement for them. Activate for Laravel, Inertia, or Pest work on this stack — always alongside the matching Boost skill(s), never alone. See the routing table inside for the specific capabilities covered."
---

# laravel-inertia-stack

Personal companion conventions for Laravel + InertiaJS + Vue 3 + Pest. Laravel Boost's
`laravel-best-practices` and `testing-best-practices` are the first-party baseline for general Laravel
and Pest, and `inertia-vue-development` is the reference for Inertia/Vue client-side patterns. Load this
skill alongside the matching Boost skill(s), never as a substitute for them. If a task needs a Boost
skill this installation doesn't have, say so explicitly and treat this skill as an incomplete companion
for that area rather than improvising the missing baseline.

## Relationship to Boost

Each convention here relates to Boost in one of three ways:

- **Extends** — covers a topic Boost does not address.
- **Specializes** — turns a Boost principle into a concrete shape for this stack.
- **Overrides** — deliberately chooses a different default than Boost. The rule file that owns an
  override says so in one sentence and states this stack's position.

Mechanical framework explanation Boost already covers is not repeated here.

## Precedence and adoption

- An established project convention takes precedence over this skill, including conventions recorded in
  project instruction or rule files.
- This skill's conventions are the defaults where the project has no established position — for
  example, in a fresh application.
- Introduce a conditional pattern (filters/sorters, tenancy rules, testing macros, templates) when a
  feature first needs it. Do not scaffold it in advance.
- Starter-kit and package-contract code keeps the shape its framework or package requires — for
  example, Fortify action contracts, starter-kit shared props, and singleton settings controllers. It
  is neither a precedent this skill must follow nor a violation to correct.

Rules state their strength in their wording: "must" and "never" mark correctness, security, or
data-integrity requirements; plain imperatives are this stack's defaults under the precedence above;
"prefer" marks a preference; a leading "when" marks a conditional pattern; a plain statement of fact
describes framework behavior.

Some conventions depend on newer framework attributes (`Illuminate\Database\Eloquent\Attributes\Scope`,
`Illuminate\Routing\Attributes\Controllers\Authorize`). Confirm the class exists in the installed
`laravel/framework` before relying on it.

Vue 3 is part of the stack boundary. The Vue guidance here is limited to the Laravel/Inertia boundary
(`rules/inertia-forms.md`, `rules/inertia-pages.md`); route other Vue implementation questions to
`inertia-vue-development`.

## Engineering judgment

Prefer familiar, discoverable Laravel architecture over custom machinery. Inspect existing
application conventions, actual consumers and native framework capabilities before introducing
a new pattern. Reuse established mechanisms when they satisfy the requirements; evaluate
consistency across the application, not just within the feature.

Distinguish duplicated business rules from harmless structural repetition. Introduce abstractions
to solve concrete problems, not to anticipate hypothetical consumers or extension points.
Evaluate whether an abstraction reduces the overall effort to understand, maintain and change
the feature, rather than merely reducing repeated code. Avoid forwarding layers that do not
provide meaningful behavior or reuse.

Keep safeguards proportionate to the invariants and risks they protect. Assess the consequences
of failure, realistic execution paths and the complexity of prevention. Prefer database constraints,
transactions and established locking patterns for data integrity. Do not introduce additional
coordination mechanisms solely to eliminate theoretical races when ordinary concurrent behavior
is acceptable. Preserve security, tenant isolation and material business invariants.

When designs preserve the same correctness, security, data integrity and operational guarantees,
prefer the clearest execution flow, most discoverable responsibilities and fewest unnecessary
concepts. Simplicity is not a reason to weaken those guarantees or avoid justified abstractions.
Respect approved architecture and scope; route material changes through the active workflow.

## Routing

Load only the rule, blueprint, or template file(s) the current task needs — do not read every file for
every Laravel task. Resolved decisions live in the file that owns them; this table routes to them rather
than repeating them. See `README.md` for what `rules/`, `blueprints/`, and `templates/` each mean.

| Task | Load |
|---|---|
| Composing or naming a CRUD, nested, or single-action controller | `blueprints/resource-controller.md` |
| Writing or organizing a Pest test | `blueprints/pest-testing.md`, then `rules/test-ownership.md` for the concrete class-ownership mapping |
| Speeding up the suite or changing how it runs (test scripts, parallelism, coverage, impact analysis, cached test state, database refresh, the CI test job) | `rules/test-execution.md` |
| Wiring Form Request -> Action -> Controller | `rules/actions.md` |
| Authorizing a controller method | `rules/authorization.md` |
| Placing model behavior, or defining an Eloquent local scope or computed model attribute | `rules/eloquent-attributes.md` |
| Adding index filtering and/or sorting | `blueprints/filters-and-sorting.md` + `rules/request-normalization.md` (a sort `direction` must be defaulted, not left nullable) + `templates/app/Filters/QueryFilter.php`, `templates/app/Sorts/QuerySorter.php`, `templates/app/Models/Concerns/Filterable.php`, `templates/app/Models/Concerns/Sortable.php` |
| Exposing a backed enum as select options | `rules/enum-options.md` |
| Exposing model records as select or filter options | `rules/resources.md` |
| Coercing or defaulting request input, or restoring optional query state into a form | `rules/request-normalization.md` |
| Building a JsonResource or other response projection for Inertia | `rules/resources.md` |
| Building an Inertia form, adapting custom controls to `<Form>` serialization, setting a reusable control's range/option bounds, or validating before submit with Precognition | `rules/inertia-forms.md` |
| Enforcing or testing tenant isolation through a global Eloquent scope | `rules/global-scope-tenancy.md` |
| Rendering a new Inertia page from a Laravel endpoint | `rules/inertia-pages.md` |
| Writing a factory or a dev-only seeder | `rules/factories-and-seeders.md` |
| Adding a mid-chain conditional query clause | `rules/query-conditionals.md` |
| Declaring a new concrete application class | `rules/php-conventions.md` |
| Writing a schema migration column | `rules/migrations.md` |
| Asserting an Inertia prop or flash data in a Pest HTTP test | `blueprints/pest-testing.md` + `templates/app/Providers/TestingServiceProvider.php` |

## Boundary

This skill is not a generic Laravel manual, a complete Vue guide, or documentation for any single
consuming project. Its blueprints are conditional shapes, not an architecture every project or feature
must adopt.

Code examples throughout this skill use neutral, invented domain concepts. They are not drawn from, and do not document, any specific consuming project.
