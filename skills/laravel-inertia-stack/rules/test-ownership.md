# Test Ownership

`testing-best-practices` owns the layer-ownership principle: the class a request calls owns its complete
matrix, and the endpoint test keeps only what proves the wiring. This file specializes that principle
into this stack's concrete classes — where each class's test lives and what it owns — and adds the
wiring exception nested, route-bound, and pivot endpoints need.

The locations below override Boost's mirror-the-class-path layout: this stack places every
framework-dependent test under `tests/Feature`, grouped by the owning application area, and keeps HTTP
tests per endpoint (see `blueprints/pest-testing.md`, which owns the `tests/Unit`/`tests/Feature`
boundary, the self-referential-expected-value warning, and Pest capability gating).

## Ownership

| Class | Test location | Owns |
|---|---|---|
| Action | `tests/Feature/Actions/{Domain}/{Verb}{Model}ActionTest.php` | Complete mutation behavior: defaults, transaction outcome, audit fields, slug/derivation rules, branches, dispatched side effects |
| Policy | `tests/Feature/Policies/{Model}PolicyTest.php` | The complete permission matrix, asserted directly via `$user->can()`/`$user->cannot()` |
| Filter | `tests/Feature/Filters/{Model}FilterTest.php` | The complete filter-method matrix plus boundary cases, exercised directly against a real query — no HTTP |
| Sorter | `tests/Feature/Sorts/{Model}SortTest.php` | The complete sort-column matrix plus tie-breaking behavior, exercised directly — no HTTP |
| Resource | `tests/Feature/Resources/{Model}ResourceTest.php` | Non-trivial project-defined transformations and conditional-field behavior — not every field, only the ones with real logic |
| Model | `tests/Feature/Models/{Model}Test.php` | Project-owned behavior, scopes, and relationship constraints whose failure would materially affect application behavior — not Laravel, Pest, or Inertia internals, and not every cast/relationship/scope merely because it exists |
| HTTP (Controller) | `tests/Feature/Http/{Domain}/{Endpoint}Test.php` | Public endpoint behavior: authentication, authorization wiring, validation, route-model and controller-to-Action wiring, response status, redirects, flash messages, and the Inertia component/prop contract — proven with representative cases, not a lower layer's complete matrix |

## Group assertions by scenario

Within one layer, keep related assertions from the same scenario together. A successful Action test may
verify submitted fields, defaults, tenant association, and audit fields in one pass; do not create a
separate test for each field solely to make each test assert one value. Keep materially different
contexts and failure paths separate. HTTP and Action tests still have distinct owners and remain separate.

## Test shared behavior at its owner

Test behavior inherited from a shared base class at that shared owner once, then keep concrete-class tests
for their own search fields, boundaries, and overrides. For example, test generic empty/unknown-filter
handling in the shared query-filter tests and test each concrete filter's specific behavior in its own
suite. Retain representative integration coverage where a caller's wiring could fail independently.

## Exact persisted values

Use `assertDatabaseHas()` rather than existence alone when a test must prove an exact persisted value —
for example after a mutation that derives or transforms a field — or a specific persisted association
needed to prove endpoint wiring (see the wiring exception below).

## No redundancy across layers

If an Action test already proves a value was persisted correctly, the HTTP test for the same endpoint
does not repeat that assertion — it proves the HTTP contract (status, redirect, flash, prop shape)
instead. The same applies to a Filter or Sorter already proven directly against a query: an HTTP test
for that index endpoint does not re-prove the filter matrix, only that the endpoint passes the request
through to it.

A lower-layer test that proves correct behavior given correct arguments does not prove the controller
supplied those arguments. For a nested, route-model-bound, or pivot endpoint, an HTTP test may — and
sometimes must — retain one minimal persisted-state or association assertion proving the endpoint wired
the correct route-bound model, parent/child relationship, authenticated actor, tenant, or pivot pair into
the Action. A global `assertDatabaseCount()` is not sufficient for this: it passes just as well when the
wrong parent, child, actor, tenant, or pivot pair was wired in, as long as the row count matches. Keep only
the identity or association needed to prove wiring — not the Action test's full field, derivation, audit,
branching, or side-effect matrix already covered there. A higher-layer assertion is redundant only when it
proves nothing beyond what the lower layer already proves.

For example, on an endpoint that attaches a member to a team through a pivot table: the Action test owns
the complete attach mutation behavior, including the transaction outcome, any derived pivot fields, and
dispatched side effects. The HTTP test retains the exact pivot pair —
`assertDatabaseHas('team_user', ['team_id' => $team->id, 'user_id' => $user->id])` — to prove the
endpoint wired the correct team and user into the Action, but omits any other mapped field the Action
test already covers.
