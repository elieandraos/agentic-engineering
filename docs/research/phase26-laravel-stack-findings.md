# Phase 26 Laravel stack findings

> **Status:** reconciliation record for the v2.2.2 patch candidate. These findings come from normal
> useOrbit Phase 26 implementation and are classified against the current `laravel-inertia-stack`
> on `main`. This document records why a finding did or did not become portable stack guidance; it is
> not useOrbit project documentation.

## Included in the patch

| Finding | Classification | Destination | Portable lesson |
| --- | --- | --- | --- |
| Factories generated cross-attribute combinations rejected by application validation | MODIFY | `rules/factories-and-seeders.md` (existing dependent-fields section) | Default factories should satisfy the record's own cross-attribute invariants; derive dependent attributes from the final merged value through closure attributes. Bounded to the record's invariants, not every Form Request rule or workflow. |
| Random factory data collided with deterministic fixture identities | MODIFY | `rules/factories-and-seeders.md` | When a unique attribute is drawn from a small finite pool that fixtures also own, exclude the fixture-owned values; `fake()->unique()` does not know about seeded rows. Concrete reserved values remain project knowledge. |
| Optional query state used to pre-fill an Inertia form accepted array-shaped input and could throw | MODIFY | `rules/request-normalization.md` | Check runtime shape before enum/membership checks (`$request->enum()` throws on array input); ignore invalid preselection rather than redirecting; only preselect related IDs present in the rendered option set. |
| 27 tests repeated large valid request/action arrays through 42 local helpers; an update test's submitted value accidentally matched the shared default | MODIFY (narrowed) | `blueprints/pest-testing.md` | Narrowed to the stack-specific delta: Form Request and Action share one validated shape, so a plain payload builder may supply a valid baseline while asserted values stay explicit overrides and update tests submit a changed value. General test-data, assertion, and coverage-preservation guidance stays with `testing-best-practices`. |
| Reusable UI date bounds made server-valid future values unreachable | MODIFY | `rules/inertia-forms.md` | A reusable control's defaults must not exclude values the Form Request accepts, and valid persisted values must remain representable on Edit; the page passes a feature-specific bound. Not a requirement to mirror server rules in the UI. |
| A finite Travel tier list existed only in the UI while the server accepted arbitrary strings | MODIFY | `rules/enum-options.md` | Validate against the same enum whose `all()` feeds the options; do not infer that every select needs an enum. |

## Already covered or not yet promoted

### Nested validation keys in user-facing copy

Nested Form Request keys leaked into user-facing validation messages. Laravel's Form Request
`attributes()` (including wildcard keys) and `messages()` already provide the mechanism, and the stack
has no position of its own on top of it. Framework-owned; project application. **No change.**

### Predictable database uniqueness conflict surfacing as a 500

A scoped uniqueness invariant was predictable from normal input but surfaced only as a database
exception. `laravel-best-practices`'s `validation.md` already owns uniqueness validation and the
constraint/race boundary; aligning the rule's scope is `Rule::unique()` mechanics; and
`rules/request-normalization.md` owns coercion/defaulting, not validation. **Already covered — no
change.**

### Shared form-option assembly across six controllers

Six Create/Edit controllers repeated the same stable option lists while retaining class-specific
options. Extracting them was a sound project refactor, but one project's six related controllers is the
same evidence bar as the deferred Form Request rule extraction below, and the prop-contract protection
is already owned by `rules/test-ownership.md`. **Defer pending recurrence.**

### Shared variant page shells and headers

Six page shells/headers differed only by class routes and one small conditional, and a shared
Documents/Notes page reused the concrete Medical shell and inherited its routes. This is Vue component
composition: `rules/resources.md` owns the JsonResource contract, and the skill carries no independent
Vue rules (`SKILL.md`). **Wrong owner / project application — no change.**

### Dependent factory values

The existing factory rule already said to derive related fields from one source of truth. Phase 26
strengthened the reason: this is not only about realistic/plausible fake data; default factory output
must also satisfy current application/domain invariants, including after a state or override replaces
the driving value. The patch refines the existing section rather than adding a parallel convention.

### Narrow Action inputs

`rules/actions.md` already owns the Action boundary, validated-array shape, and absence of HTTP
concerns. Phase 26's class-specific Action narrowing is consistent with that guidance, but the evidence
does not justify a new portable rule beyond the current Action contract.

### Resource base composition

Phase 26 benefited from composing common Policy resource fields while avoiding relation-dependent
fields that were not safe to inherit blindly. `rules/resources.md` already requires explicit field
selection and safe conditional relation exposure. The exact `baseAttributes()` shape is a project
design, not yet a portable convention. **No change.**

### Route middleware replacing repeated controller guards

Moving repeated class/URL guards to route middleware was effective and preserved 404-before-validation
behavior, but this is a contextual HTTP architecture decision. There is not enough evidence for a
stack-wide threshold saying when a repeated controller guard must become middleware. **No change.**

### Invokable single-endpoint controllers

The existing resource-controller blueprint already owns controller composition. Phase 26's conversions
were idiomatic but do not establish a missing durable stack convention. **No change.**

### Shared Form Request rule extraction

Phase 26 showed value in sharing common policy validation and in using declarative conditional rules.
The current stack has no dedicated validation-extraction rule, but one project with twelve closely
related requests is not enough to prescribe a reusable abstraction shape. Laravel's baseline validation
guidance remains authoritative. **Defer pending recurrence.**

### Concrete fixture identities

Specific reserved country codes and fixture ownership are useOrbit project knowledge. Only the
portable collision-avoidance principle was promoted.

### Runtime/worktree preparation

Copied `vendor`, `public/build`, Wayfinder generation, worktree base selection, permission prompts,
and cleanup are execution/runtime evidence. They do not belong in the Laravel application stack skill.
**Wrong owner.**

## Boundary of v2.2.2

This patch is intentionally limited to normal-use stack findings that sharpen existing Laravel/Inertia/
Pest conventions or fill a small, reusable gap.

It does not include:

- Control Room/orchestration research;
- useOrbit-specific Policy domain rules;
- runtime/worktree procedures;
- a new generic validation architecture;
- a requirement to introduce JavaScript tests;
- broad Laravel guidance already owned by Boost.

The final Phase 26 UI/domain audit has now been reconciled above. Product-specific findings remain in useOrbit; only the portable stack lessons were promoted.
