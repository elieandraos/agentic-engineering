---
name: my-laravel-stack
description: "Personal companion conventions for a Laravel + InertiaJS + Vue 3 + Pest stack, additive to Laravel Boost's laravel-best-practices and testing-best-practices skills — never a replacement for them. Covers the Controller-to-Form-Request-to-Policy/#[Authorize]-to-Action-to-Resource-to-Inertia composition, the Pest Unit/Feature execution-boundary taxonomy and per-layer test ownership, #[Authorize] attribute authorization, #[Scope]-based Eloquent scopes, class-based QueryFilter/QuerySorter query conditioning with reusable installable base classes, enum option lists, factory/seeder realism, request normalization in prepareForValidation(), final-by-default application classes, and Laravel migration column-nullability behavior. Activate for Laravel, Inertia, or Pest work on this stack — always alongside the matching Boost skill(s), never alone."
---

# My Laravel Stack

Personal companion conventions for Laravel + InertiaJS + Vue 3 + Pest. This skill is additive only:
Laravel Boost's `laravel-best-practices` and `testing-best-practices` own the general Laravel and Pest
baseline, and `inertia-vue-development` owns Inertia/Vue client-side patterns. This skill contains only
the delta genuinely additive to those skills — load it alongside the matching Boost skill(s), never as a
substitute for them, and never as a generic Laravel manual, a complete Vue guide, or documentation for
any one consuming project.

If a task needs a Boost skill this installation doesn't have, say so explicitly and treat this skill as
an incomplete companion for that area rather than silently filling the gap with improvised baseline
guidance.

Current evidence is strongest for Laravel, Inertia, and Pest. Vue 3 is part of the declared stack
boundary, but this skill carries no independent Vue-specific rules — route Vue implementation questions
to `inertia-vue-development`.

## When this activates

- Writing or reviewing a Laravel controller, Form Request, Action, Policy, or Resource in this stack.
- Adding query filtering or sorting to an Eloquent index query.
- Writing or organizing a Pest test.
- Defining an Eloquent local scope, a migration column, or a backed enum used as select options.
- Generating factory or seeder data.

## Routing

Load only the rule file(s) the current task needs — do not read every file for every Laravel task.
Resolved decisions live in the file that owns them; this table routes to them rather than repeating them.

| Task | Load |
|---|---|
| Composing a CRUD or single-action controller | `rules/resource-controller-blueprint.md` |
| Writing or organizing a Pest test | `rules/pest-testing-blueprint.md`, then `rules/testing-strategy.md` for the concrete class-ownership mapping |
| Wiring Form Request -> Action -> Controller | `rules/actions-pattern.md` |
| Authorizing a controller method | `rules/authorization.md` |
| Defining an Eloquent local scope | `rules/eloquent-attributes.md` |
| Adding index filtering and/or sorting | `rules/filters-pattern.md` + `rules/request-normalization.md` (a sort `direction` must be defaulted, not left nullable) + `assets/app/Filters/QueryFilter.php`, `assets/app/Sorts/QuerySorter.php`, `assets/app/Models/Concerns/Filterable.php`, `assets/app/Models/Concerns/Sortable.php` |
| Exposing a backed enum as select options | `rules/enum-options.md` |
| Coercing or defaulting request input | `rules/request-normalization.md` |
| Building a JsonResource for Inertia | `rules/resources.md` |
| Writing a factory or a dev-only seeder | `rules/factories-and-seeders.md` |
| Adding a mid-chain conditional query clause | `rules/query-conditionals.md` |
| Declaring a new concrete application class | `rules/php-conventions.md` |
| Writing a schema migration column | `rules/migrations.md` |
| Asserting an Inertia prop or flash message in a Pest HTTP test | `rules/pest-testing-blueprint.md` + `assets/app/Providers/TestingServiceProvider.php` |

## Boundary

This skill is not:

- a replacement for `laravel-best-practices`, `testing-best-practices`, or `inertia-vue-development`;
- a generic Laravel manual or a complete Vue guide;
- documentation for any single consuming project;
- an architecture every project must adopt — the controller and Pest blueprints stay conditional
  (tenancy, non-CRUD shapes, filters/sorters) rather than mandatory for every feature.

Code examples throughout this skill use neutral, invented domain concepts. They are not drawn from, and
do not document, any specific consuming project.
