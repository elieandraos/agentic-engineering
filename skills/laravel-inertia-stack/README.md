# laravel-inertia-stack

An opinionated approach to engineering Laravel, InertiaJS, Vue 3 and Pest applications. It captures
not only how code should be written, but how architectural choices should be evaluated. The goal is
not merely consistent code, but consistent engineering judgment.

## How it relates to Laravel Boost

Laravel Boost provides the framework best practices, and this skill loads alongside the matching Boost
skill(s). On top of that baseline, each convention here does one of three things:

- **extends** Boost where it is silent — for example, Action payload shapes, child-resource
  authorization, Inertia form serialization, and tenancy paths a global scope does not reach;
- **specializes** a Boost principle into a concrete stack shape — for example, test-layer ownership
  mapped onto Actions, Filters, Sorters, and Resources;
- **overrides** a Boost default deliberately — for example, Actions for every mutation, Form Requests
  for every validated input, `#[Authorize]` attributes, plural resource controllers, and the Pest test
  layout. Each override states its reason where it is defined.

The consuming project stays authoritative; `SKILL.md` states how its conventions and this skill's
defaults combine.

## Boring prompts

```shell
"Add an is_active field with its migration, factory state, and tests."
"Build a filterable resource index."
"Implement the approved issue using this project's Laravel conventions."
```

## What normally happens

A task loads only the specific rule, blueprint, or template it needs — never the whole skill at once.
Three kinds of content back that up:

- **`rules/`** — independently applicable conventions (Actions, authorization, request normalization,
  and more).
- **`blueprints/`** — conditional shapes for multi-component work (resource controllers,
  filtering/sorting, Pest test taxonomy) — not mandatory architecture every project must adopt.
- **`templates/`** — adaptable starting points, never blindly copied: the consuming project is inspected
  for an existing equivalent, reconciled, and validated before a template is installed.

This is a companion, not a pipeline stage: `implement-it` and `review-it` load it when work touches this
stack.

## Install

```shell
npx skills add elieandraos/agentic-engineering --skill laravel-inertia-stack
```

See [`SKILL.md`](SKILL.md) for the complete operational contract.
