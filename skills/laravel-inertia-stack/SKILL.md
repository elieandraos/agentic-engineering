---
name: laravel-inertia-stack
description: "Companion conventions for a Laravel + InertiaJS + Vue 3 + Pest stack, additive to Laravel Boost's laravel-best-practices and testing-best-practices skills — never a replacement for them. Activate for Laravel, Inertia, or Pest work on this stack — always alongside the matching Boost skill(s), never alone. See the routing table inside for the specific capabilities covered."
---

# laravel-inertia-stack

Personal companion conventions for Laravel + InertiaJS + Vue 3 + Pest. Laravel Boost's
`laravel-best-practices` and `testing-best-practices` are the first-party baseline and reference for
general Laravel and Pest, and `inertia-vue-development` is the reference for Inertia/Vue client-side
patterns. This skill states this stack's own durable, opinionated conventions on top of that
baseline — load it alongside the matching Boost skill(s), never as a substitute for them. A rule here
may restate or refine a topic Boost also covers when the stack has a stable, deliberate position on
it; Boost covering a topic is not, by itself, a reason to omit or remove that position — only
mechanical explanation Boost already covers well is trimmed. This skill is never a generic Laravel
manual, a complete Vue guide, or documentation for any one consuming project.

If a task needs a Boost skill this installation doesn't have, say so explicitly and treat this skill as
an incomplete companion for that area rather than silently filling the gap with improvised baseline
guidance.

Current evidence is strongest for Laravel, Inertia, and Pest. Vue 3 is part of the declared stack
boundary, but this skill carries no independent Vue-specific rules — route Vue implementation questions
to `inertia-vue-development`.

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

When designs preserve the same correctness, security, data integrity and operational guarantees,
prefer the clearest execution flow, most discoverable responsibilities and fewest unnecessary
concepts. Simplicity is not a reason to weaken those guarantees or avoid justified abstractions.
Respect approved architecture and scope; route material changes through the active workflow.

## When this activates

- Writing or reviewing a Laravel controller, Form Request, Action, Policy, or Resource in this stack.
- Adding query filtering or sorting to an Eloquent index query.
- Writing or organizing a Pest test.
- Changing how the test suite runs: test scripts, parallelism, coverage, impact analysis, the base test case, or the CI test job.
- Defining model behavior, an Eloquent local scope or computed model attribute, a migration column, or a backed enum used as select options.
- Generating factory or seeder data.
- Building or reviewing an Inertia form that uses the Laravel/Inertia request serialization boundary.
- Enforcing or testing tenant isolation through a global Eloquent scope.
- Adding or reviewing a backend endpoint that renders a new Inertia page component.

## Routing

Load only the rule, blueprint, or template file(s) the current task needs — do not read every file for
every Laravel task. Resolved decisions live in the file that owns them; this table routes to them rather
than repeating them. See `README.md` for what `rules/`, `blueprints/`, and `templates/` each mean.

| Task | Load |
|---|---|
| Composing a CRUD or single-action controller | `blueprints/resource-controller.md` |
| Writing or organizing a Pest test | `blueprints/pest-testing.md`, then `rules/test-ownership.md` for the concrete class-ownership mapping |
| Speeding up the suite or changing how it runs (test scripts, parallelism, coverage, impact analysis, cached test state, the CI test job) | `rules/test-execution.md` |
| Wiring Form Request -> Action -> Controller | `rules/actions.md` |
| Authorizing a controller method | `rules/authorization.md` |
| Placing model behavior, or defining an Eloquent local scope or computed model attribute | `rules/eloquent-attributes.md` |
| Adding index filtering and/or sorting | `blueprints/filters-and-sorting.md` + `rules/request-normalization.md` (a sort `direction` must be defaulted, not left nullable) + `templates/app/Filters/QueryFilter.php`, `templates/app/Sorts/QuerySorter.php`, `templates/app/Models/Concerns/Filterable.php`, `templates/app/Models/Concerns/Sortable.php` |
| Exposing a backed enum as select options | `rules/enum-options.md` |
| Exposing model records as select or filter options | `rules/resources.md` |
| Coercing or defaulting request input, or restoring optional query state into a form | `rules/request-normalization.md` |
| Building a JsonResource for Inertia | `rules/resources.md` |
| Building an Inertia form, adapting custom controls to `<Form>` serialization, setting a reusable control's range/option bounds, or validating before submit with Precognition | `rules/inertia-forms.md` |
| Enforcing or testing tenant isolation through a global Eloquent scope | `rules/global-scope-tenancy.md` |
| Rendering a new Inertia page from a Laravel endpoint | `rules/inertia-pages.md` |
| Writing a factory or a dev-only seeder | `rules/factories-and-seeders.md` |
| Adding a mid-chain conditional query clause | `rules/query-conditionals.md` |
| Declaring a new concrete application class | `rules/php-conventions.md` |
| Writing a schema migration column | `rules/migrations.md` |
| Asserting an Inertia prop or flash message in a Pest HTTP test | `blueprints/pest-testing.md` + `templates/app/Providers/TestingServiceProvider.php` |

## Boundary

This skill is not:

- a replacement for `laravel-best-practices`, `testing-best-practices`, or `inertia-vue-development`;
- a generic Laravel manual or a complete Vue guide;
- documentation for any single consuming project;
- an architecture every project must adopt — the controller and Pest blueprints stay conditional
  (tenancy, non-CRUD shapes, filters/sorters) rather than mandatory for every feature.

Overlapping a Boost topic is not itself a defect. A rule stays when it states this stack's own
durable position on that topic; it is trimmed only when it merely re-teaches mechanics Boost already
covers well, without adding one.

Code examples throughout this skill use neutral, invented domain concepts. They are not drawn from, and do not document, any specific consuming project.
