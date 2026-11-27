# Pest Testing Blueprint

## Boundary

This file owns this stack's test layout: the `tests/Unit`/`tests/Feature` execution boundary, HTTP test
file organization, and the testing patterns below. `testing-best-practices` owns the general testing
principles it builds on. `rules/test-ownership.md` owns the concrete per-class location and ownership
mapping — load it alongside this file when writing a layer-specific test.

## Unit vs. Feature — classify by execution boundary

This specializes Boost's "unit test only for logic that does not use the framework" into a layout, and
overrides Boost's mirror-the-class-path file placement: a framework-dependent class's test lives under
`tests/Feature`, even when its class is not an HTTP concern.

- **`tests/Unit`** — genuinely isolated only: no Laravel application boot, no database or factories, no
  service container, no Laravel facades. A plain enum, a plain value object, or any class with no
  framework dependency belongs here.
- **`tests/Feature`** — anything that boots Laravel or uses the database. This includes Action, Policy,
  Filter, Sorter, Resource, and Model tests in this stack, since they typically use factories, the
  database, or Laravel's container — not only HTTP tests. Mirror the owning application area inside
  `Feature` only where useful (`Http`, `Actions`, `Policies`, `Filters`, `Sorts`, `Resources`, `Models`)
  — do not force a category a feature has nothing to put in.

## Binding `tests/Pest.php` to the boundary

A directory name does not establish the boundary; the binding in `tests/Pest.php` does. Bind the
project's Laravel `TestCase` and its database-refresh trait to `Feature` only. Genuinely isolated `Unit`
tests receive no Laravel `TestCase` binding and fall back to Pest's default test case.

```php
pest()->extend(Tests\TestCase::class)
    ->use(RefreshDatabase::class)
    ->in('Feature');
```

The refresh trait shown is illustrative; the project chooses it (see `rules/test-execution.md` before
changing it). Binding the Laravel `TestCase` to `Unit` without a refresh trait does not make those tests
isolated: `Illuminate\Foundation\Testing\TestCase` boots the application in `setUp()` regardless.

Check the actual binding before treating a test under `tests/Unit` as isolated. When a suite still binds
the Laravel `TestCase` to `Unit`, move its framework-dependent tests to `Feature` before narrowing the
binding; narrowing first breaks the tests that still depend on it.

## Preserve endpoint-oriented HTTP test files

This overrides Boost's one-file-per-class layout with `describe()` groups: endpoint files keep each
endpoint's cases easy to find and keep files small.

Keep one Pest file per HTTP endpoint or closely related group (`IndexTest.php`, `ShowTest.php`,
`StoreTest.php`, `UpdateTest.php`, `DestroyTest.php`, and any custom-action endpoint's own file) inside
`tests/Feature/Http/{Domain}/`. Do not force every controller's tests into one oversized
`{Controller}Test.php` file merely for consolidation.

## Warning: don't let a resource-built comparison stand in for the value a test is specifically responsible for proving

This specializes Boost's rule to assert a known value rather than one computed by the implementation.
The reusable `assertHasResource`/`assertHasPaginatedResource` macros (below) compare the actual Inertia
prop against a value built by instantiating the same production Resource the endpoint itself uses. That
comparison is appropriate when what an HTTP test needs to prove is integration — the correct Resource
class wraps the correct model instance for this route — because the Resource's own field-level
correctness is the Resource test's job (see `rules/test-ownership.md`). It stops being appropriate
when the HTTP test is specifically responsible for proving a field's value or a transformation the
Resource performs: building the expected side of that assertion from the same Resource makes the
comparison self-referential — if the Resource's shape regresses in a way that stays internally
self-consistent, the test cannot catch it. In that case, assert the literal expected value instead of
deriving it from the Resource under test.

## Consolidate by behavior, not by test count

Group related assertions from one arranged scenario within its layer as `rules/test-ownership.md`'s
"Group assertions by scenario" describes. This section covers consolidating tests without losing what
they protect.

Use a dataset when it makes the same behavior easy to verify across several cases. Do not optimize for
fewer files or tests: keep separate tests or files when that makes behavior easier to find, and avoid a
dataset whose unused parameters or placeholder callbacks make the tests harder to understand.

Before removing or consolidating a test, identify where each meaningful assertion remains protected.
Shared line coverage is not enough to call tests redundant: two tests can execute the same code while
checking different outcomes.

When testing a relationship or association, arrange the expected identity independently. If a test
explicitly supplies a creator, parent, or other related model, assert that exact model is returned or
persisted. Reading the expected ID back from the record under test can make the assertion circular and
miss a failure to preserve the supplied value.

## Minimal test data — the attribute-level delta

`testing-best-practices`'s `test-data.md` already owns record-level minimalism ("create only the records
required to arrange the behavior or support an assertion"). This file adds the narrower, additive
attribute-level rule it doesn't cover:

> Each test sets only the attributes required to establish its preconditions and prove the behavior under
> test. Set additional attributes only when they are material to the case — for example ordering,
> filtering, tenant isolation, a collision, an absence, or complete field mapping. "Minimal" does not mean
> incomplete coverage: a test specifically proving field mapping may intentionally provide the complete
> relevant payload.

## Shared request/action payload builders

In this stack an Action receives the same validated array its Form Request produces (see
`rules/actions.md`), so HTTP and Action tests for one domain often repeat the same large valid input.
When that repetition is real, a plain test helper may return a valid baseline array with per-test
overrides. It builds input arrays, not models — persisted state stays with model factories — and the
attribute-level rule above still applies: every value a test asserts on is passed as an explicit
override, never read back from the builder's default. In an update test, submit a value that differs
from the record's current value, or the test can pass without proving the update.

## Reusable Inertia testing macros

`hasResource`, `hasPaginatedResource`, `assertHasResource`, `assertHasPaginatedResource`, and
`assertHasInertiaFlash` are custom Pest/Inertia-testing macros this stack ships as a reusable
implementation template — see
[`templates/app/Providers/TestingServiceProvider.php`](../templates/app/Providers/TestingServiceProvider.php)
for the implementation, required packages, and registration/guard instructions. Install and register that
provider before writing a test that calls any of these macros; do not write a test that assumes they
exist without checking first. `assertHasInertiaFlash($key, $value)` asserts one key of Inertia's flash
data, so it works with whatever flash key and shape the project uses.

```php
test('an authenticated user can view an order', function () {
    $user = User::factory()->create();
    $order = Order::factory()->create();

    $this->actingAs($user)
        ->get(route('orders.show', $order))
        ->assertOk()
        ->assertHasResource('order', OrderResource::make($order));
});
```

This proves integration — the `show` route wraps the requested `$order` in `OrderResource` — which is
exactly the case the warning above allows. It would stop being appropriate if the test's actual
responsibility were proving a specific field transformation `OrderResource` performs; that case calls for
a literal expected value instead.

Keep these Resource comparison macros for HTTP integration checks. Add focused known-value assertions for
meaningful calculations, formatting, and conditional fields when they lack independent verification.
Do not require a separate assertion for every straightforward passthrough field or broadly replace the
macros with manual shape checks.

## Global classes in namespace-free test files

Pest test files usually declare no namespace. In such a file, `use LogicException;` for a global class
has no effect and makes PHP emit a warning. The parallel runner turns that warning into an error and
aborts before any test runs. Reference global classes without an import.

## Absence assertions over rendered output

An absence assertion (`->not->toContain(...)`) over rendered output, such as a mail body or a page,
fails by chance when unrelated content can contain the value — for example a random UUID in an action
URL. In order of preference:

1. Control the fixture, so unrelated content cannot contain the value: generate known identifiers with
   `Str::createUuidsUsingSequence()`, one value per created model (it also sets `HasUuids` keys), or
   choose a hidden value that cannot occur in them.
2. Otherwise, exclude only the known irrelevant content (that identifier, that URL) before the
   assertion. Never strip broad parts of the output.

Either way, keep detection for every display format the value can appear in — for an amount, the raw
value, decimals, and thousands separators — not only the literal stored in the fixture.

## Tests that change configuration, environment variables, or routes

When the suite's base test case uses cached configuration and routes, read `rules/test-execution.md`'s
"Cached configuration and routes in tests" before writing a test that changes configuration, sets
environment variables, or registers routes.

## Confirm the effective database before targeting the test environment

The test runner and artisan can resolve different configuration. Values from `phpunit.xml` `<env>`
entries apply only under the test runner. `php artisan … --env=testing` loads `.env.testing` only when
that file exists and otherwise falls back to the project's normal environment file, and a cached
configuration ignores environment files altogether. Depending on the project, `migrate:fresh
--env=testing` or a tinker session can therefore run against the development database.

Before a writing or destructive artisan or tinker command meant for the test database, confirm the
connection and database name it will actually use (`php artisan db:show` with the same flags), not only
the environment name it reports. Prefer exercising factories and data setup inside a Pest test, which
runs under the runner's configuration.

## Capability gating

Pest TIA (a core Pest 5 feature) and optional Pest plugins follow Boost's rule to use only the test tools
the project installs. For TIA's tradeoffs and how full-suite and CI runs switch it off, see
`rules/test-execution.md`.
