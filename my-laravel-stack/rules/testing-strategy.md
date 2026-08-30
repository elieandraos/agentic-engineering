# Testing Strategy — Class Ownership Mapping

This file states where each class type's test lives and what it asserts, for this stack's
Action/Controller/Policy/Filter/Sorter/Resource/Model taxonomy. See `pest-testing-blueprint.md` for the
general `tests/Unit`/`tests/Feature` execution-boundary taxonomy, the self-referential-expected-value
warning, and Pest capability gating — this file does not restate any of that.

## Ownership

| Class | Test location | Owns |
|---|---|---|
| Action | `tests/Feature/Actions/{Domain}/{Verb}{Model}ActionTest.php` | Complete mutation behavior: defaults, transaction outcome, audit fields, slug/derivation rules, branches, dispatched side effects |
| Policy | `tests/Feature/Policies/{Model}PolicyTest.php` | The complete permission matrix, asserted directly via `$user->can()`/`$user->cannot()` |
| Filter | `tests/Feature/Filters/{Model}FilterTest.php` | The complete filter-method matrix plus boundary cases, exercised directly against a real query — no HTTP |
| Sorter | `tests/Feature/Sorts/{Model}SortTest.php` | The complete sort-column matrix plus tie-breaking behavior, exercised directly — no HTTP |
| Resource | `tests/Feature/Resources/{Model}ResourceTest.php` | Non-trivial project-defined transformations and conditional-field behavior — not every field, only the ones with real logic |
| Model | `tests/Feature/Models/{Model}Test.php` | Project-owned behavior, scopes, and relationship constraints whose failure would materially affect application behavior — not Laravel, Pest, or Inertia internals, and not every cast/relationship/scope merely because it exists |
| HTTP (Controller) | `tests/Feature/Http/{Domain}/{Endpoint}Test.php` | Public endpoint behavior: authentication, authorization wiring, validation, route-model behavior, response status, redirects, flash messages, and the Inertia component/prop contract — proven with representative cases, not a lower layer's complete matrix |

## Assertion note

Use `assertModelExists()` for existence (Boost's default). Use `assertDatabaseHas()` only when a test
genuinely needs to prove an exact persisted value — for example after a mutation that derives or
transforms a field, where existence alone wouldn't prove the derivation was correct.

## No-redundancy rule

A layer only asserts what it owns. If an Action test already proves a value was persisted correctly, the
HTTP test for the same endpoint does not repeat that assertion — it proves the HTTP contract (status,
redirect, flash, prop shape) instead. A Policy violation is confirmed in an HTTP test with one
`assertForbidden()`, not the full matrix already covered by the Policy test.
