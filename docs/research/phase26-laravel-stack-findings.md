# Phase 26 Laravel stack findings

> **Status:** reconciliation record for the v2.2.2 patch candidate. These findings come from normal
> useOrbit Phase 26 implementation and are classified against the current `laravel-inertia-stack`
> on `main`. This document records why a finding did or did not become portable stack guidance; it is
> not useOrbit project documentation.

## Included in the patch

| Finding | Classification | Destination | Portable lesson |
| --- | --- | --- | --- |
| Factories generated cross-attribute combinations rejected by application validation | MODIFY | `rules/factories-and-seeders.md` | Default factories should produce application-valid states; derive dependent attributes from the final owning value. |
| Random factory data collided with deterministic fixture identities | MODIFY | `rules/factories-and-seeders.md` | Exclude fixture-owned unique identities from random default pools; concrete reserved values remain project knowledge. |
| Optional query state used to pre-fill an Inertia form accepted array-shaped input and could throw | MODIFY | `rules/request-normalization.md` | Validate runtime shape before enum/membership checks and scope relationship preselection through the real tenant boundary. |
| Six form controllers repeated the same stable option lists while retaining class-specific options | MODIFY | `rules/inertia-forms.md` | Extract stable shared option assembly without creating a universal form-schema abstraction or moving feature-specific props out of their owner. |
| 27 tests repeated large valid request/action arrays through 42 local helpers | MODIFY | `blueprints/pest-testing.md` | Shared plain-array payload builders may provide valid defaults, while values under assertion remain explicit overrides; factories remain model-state builders. |
| An update test's submitted value accidentally matched the shared default | MODIFY | `blueprints/pest-testing.md` | Mutation tests must make the changed value explicit so they cannot pass without proving the mutation. |

| Reusable UI date bounds made server-valid future values unreachable | MODIFY | `rules/inertia-forms.md` | Client-side ranges/options must stay within the server/domain contract and valid persisted values must remain representable on Edit. |
| Nested Form Request keys leaked into user-facing validation copy | ALREADY COVERED / PROJECT APPLICATION | Laravel Form Request `attributes()` / focused messages | Important application polish, but Laravel already provides the mechanism; no stack-specific abstraction is needed. |
| A database uniqueness invariant was predictable from normal input but surfaced only as a 500 | MODIFY | `rules/request-normalization.md` | Keep the database constraint authoritative while mirroring predictable scoped conflicts in Form Request validation. |
| Six page shells/headers differed only by class routes and one small conditional; a shared page reused the concrete Medical copy and broke other classes | MODIFY | `rules/resources.md` | When presentation chrome is structurally identical, drive small variant differences through explicit configuration; never reuse one concrete variant as a generic shell. |
| A finite Travel tier list existed only in the UI while the server accepted arbitrary strings | MODIFY | `rules/inertia-forms.md` + existing `rules/enum-options.md` | Closed domain choices should have one authoritative application source shared by server validation and UI options; do not infer that every select needs an enum. |

## Already covered or not yet promoted

### Dependent factory values

The existing factory rule already said to derive related fields from one source of truth. Phase 26
strengthened the reason: this is not only about realistic/plausible fake data; default factory output
must also satisfy current application/domain invariants. The patch refines the existing rule rather
than adding a parallel convention.

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
