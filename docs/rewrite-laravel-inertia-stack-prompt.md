# Laravel Inertia Stack Rewrite Handoff

I want to rewrite `laravel-inertia-stack` on the current `improve-2.1.4` branch of `elieandraos/agentic-engineering`.

This is part of the existing open PR #11. Do not create a new branch or PR.

## Goal

Rewrite the `laravel-inertia-stack` rules so the skill is a mature, portable, opinionated companion for:

- Laravel
- InertiaJS
- Vue 3
- Pest

It must remain additive to Laravel Boost, not a replacement for it.

The rewrite should make the rules feel like strong Laravel documentation: concise, practical, example-driven, neutral, and easy to apply.

The goal is not to reproduce Laravel Boost. The goal is to preserve the genuinely useful conventions that are additive to Boost.

## Scope

Keep these files and structures for now:

- `SKILL.md`
- `README.md`
- `blueprints/`
- `templates/`

Focus the rewrite on:

- `rules/*.md`

Do not redesign Agentic Engineering lifecycle skills such as `implement-it`, `review-it`, `plan-it`, or `ship-it`.

Do not turn this skill into a generic Laravel manual.

## Before editing

Inspect the complete current skill:

- `skills/laravel-inertia-stack/SKILL.md`
- `skills/laravel-inertia-stack/README.md`
- every file under `skills/laravel-inertia-stack/rules/`
- every blueprint
- every template

Then read the current Agentic Engineering skill-authoring methodology and any relevant authoring rules in this repository.

Follow the current methodology throughout this rewrite.

## Research the current Boost baseline

Compare this skill against the current first-party Laravel Boost ecosystem.

Inspect current Boost guidance for at least:

- `laravel-best-practices`
- `testing-best-practices`
- `inertia-vue-development`
- relevant current Laravel/Inertia/Wayfinder guidance

Use current Boost source/documentation as the comparison baseline, not an old snapshot.

The comparison should answer:

- What responsibilities already belong to Boost?
- What does `laravel-inertia-stack` genuinely add?
- Where are the current rules duplicating Boost?
- Which conventions are really stack-level?
- Which conventions are actually project-specific?
- Which existing rules should disappear rather than be rewritten?

Do not copy Boost content.

## Audit every existing rule

Before rewriting, classify every existing rule into one of these categories:

A. Keep conceptually, rewrite for portability and style.

B. Keep, but substantially rewrite.

C. Remove because Boost already owns the responsibility.

D. Remove or generalize because it is consuming-project-specific.

E. Keep because it is a genuine reusable delta for the Laravel + Inertia + Vue 3 + Pest combination.

F. Keep elsewhere because the content is better represented by an existing blueprint or template.

Do not preserve a rule merely because it already exists.

Do not modify files until this audit is understood.

## Ownership model

Preserve this boundary:

Laravel Boost
= general Laravel/PHP/Pest/Inertia ecosystem baseline.

`laravel-inertia-stack`
= opinionated, evidence-backed conventions for the Laravel + Inertia + Vue 3 + Pest combination.

Consuming project
= project-specific conventions and decisions.

If Boost already provides a strong baseline for something, do not duplicate it.

The stack skill should contain the delta.

## Portability

The rewritten rules must not contain:

- useOrbit-specific classes
- useOrbit-specific routes
- useOrbit-specific project paths
- issue numbers
- pull request numbers
- project-specific domain models
- project-specific tenant assumptions
- GitHub history
- historical implementation stories
- claims that a consuming project's architecture is mandatory for every project

Use neutral examples and invented domain concepts.

Good example domains:

- Order
- Invoice
- Account
- Customer
- Product
- Report
- User

When a convention is conditional, make that explicit.

Prefer:

"When this stack uses X, prefer Y because..."

or:

"For CRUD resources with this boundary, use this shape. Do not force it onto non-CRUD workflows."

Avoid:

"Always use X."

unless the convention is genuinely universal and well supported.

## Rule style

Rewrite the rules so they feel like Laravel documentation.

Prefer this shape:

# Topic

One or two short paragraphs explaining the convention.

## Why

Only when the reason is durable and useful.

## Example

A realistic Laravel/PHP/Inertia/Pest example.

Then a short explanation of the important detail.

Use fenced code blocks with language identifiers.

Examples should be:

- small
- concrete
- current
- complete enough to understand
- neutral
- easy to copy mentally
- written like first-party framework documentation

Avoid:

- giant application excerpts
- pseudo-code when real Laravel/PHP code works
- long historical explanations
- repeated caveats
- multiple competing implementations unless there is a real decision to make
- giant rule files that answer several unrelated questions

Each rule should answer one concrete implementation question well.

## Code examples

Make the code examples feel like Laravel documentation.

For example, instead of a consuming-project class:

```php
final class PolicyMedicalController
{
    //
}
```

use:

```php
final class OrderController
{
    //
}
```

Examples should demonstrate the convention rather than reproduce repository structure.

Prefer real Laravel syntax over abstract pseudo-code.

## Likely areas to evaluate

These are examples of conventions that may be genuine stack-level delta, but do not assume they should remain. Verify each one against Boost and the repository evidence:

- Form Request -> Action -> Controller boundaries
- Action class conventions
- authorization boundaries
- Inertia request/response boundaries
- Inertia page/component boundaries
- Resource conventions for Inertia payloads
- enum-to-option conventions
- request normalization
- Eloquent filtering and sorting composition
- factory/test ownership conventions
- migration conventions
- endpoint/page boundary conventions
- PHP conventions that are not simply generic Laravel advice
- query composition conventions

If Boost already covers one, remove it from this skill.

## Preserve conditional architecture

The existing blueprints are intentionally conditional.

Do not turn these into universal architecture:

- resource controller blueprint
- filtering/sorting blueprint
- Pest testing blueprint

The rules should explain the decision or convention.

The blueprints should continue to describe reusable shapes.

Do not make every Laravel application conform to a single architecture.

## Context discipline

This skill is loaded alongside Boost.

Therefore every rule must justify its context cost.

Prefer the smallest sensible rule boundary.

Do not split content artificially.

Do not create large rules that duplicate multiple topics.

## `SKILL.md` and `README.md`

After rewriting the rules, reconcile:

- `SKILL.md`
- `README.md`

with the new rule set.

Keep the important existing identity:

"This skill is additive only and never replaces Laravel Boost."

Keep the routing table accurate.

Do not turn `SKILL.md` into a copy of all rule contents.

Make sure routing points to the actual current ownership of rules, blueprints, and templates.

## Authoring review

After the rewrite, review the whole skill against the current skill-authoring methodology.

Check specifically:

- portability
- responsibility boundaries
- duplication with Boost
- rule discoverability
- context cost
- unnecessary abstraction
- clarity
- code-example quality
- conditionality
- consistency
- terminology
- project-knowledge leakage
- historical contamination
- whether each rule has a clear reason to exist
- whether the skill is materially more useful than simply installing Boost

If evidence is insufficient to generalize a convention safely, leave it out and report the open question.

Do not invent architecture.

## Validation

Before finishing:

1. Search every remaining `rules/*.md` for project-specific references.
2. Search for useOrbit names.
3. Search for issue numbers and PR numbers.
4. Search for concrete repository-specific paths.
5. Check code examples for consistency and current Laravel syntax.
6. Check internal links and routing.
7. Check markdown formatting.
8. Recompare the final rules against current Boost responsibilities.
9. Review the complete diff for accidental scope expansion.
10. Confirm that blueprints and templates were not unnecessarily rewritten.

Do not modify blueprints or templates unless a rule rewrite breaks an existing reference and the smallest repair is necessary. If that happens, explain exactly why.

## Commit strategy

Use a small number of semantic commits.

Do not create artificial fragmentation.

A reasonable structure would be:

1. rewrite/generalize the reusable Laravel/Inertia rules
2. reconcile `SKILL.md` and `README.md`

Use the repository's existing commit-message policy.

Do not push automatically unless the current workflow explicitly authorizes it.

Leave the branch in a reviewable state.

## Final report

Report:

1. Which rules were kept and why.
2. Which rules were substantially rewritten.
3. Which rules were removed because Boost already owns them.
4. Which rules were removed or generalized because they were project-specific.
5. Which conventions remain as the genuine stack-level delta.
6. What was intentionally left unresolved.
7. Whether any blueprint or template required a reference-only repair.
8. Validation performed.
9. Commit(s) created.
10. Whether PR #11's current title/description still accurately describe the patch, and what should be updated.

Most importantly:

Do not optimize for preserving the current rule count.

Optimize for a smaller, clearer, more portable companion skill whose rules feel like they belong next to Laravel's own documentation while providing useful opinions that Boost does not already provide.
