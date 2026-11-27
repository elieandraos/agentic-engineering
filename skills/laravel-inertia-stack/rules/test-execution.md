# Test Execution

How this stack runs its test suite locally, for coverage, and in CI. `testing-best-practices`'s
`rules/performance.md` owns the baseline settings: Xdebug off, `WithCachedConfig` and
`WithCachedRoutes`, `--parallel`, global fakes, and the conditions for parallel-safe tests. This file
adds the decisions around those settings. The consuming project owns its commands, thresholds, and
process counts.

Runner and wrapper behavior changes between versions. A version-specific behavior named below is an
example of what to check. Confirm it against the installed versions before relying on it.

## Measure before restructuring tests

`testing-best-practices` already requires measuring before changing a setting. Before you restructure
tests, also measure where the suite's time goes, in this order:

1. **Instrumentation** — a coverage driver active for runs that collect no coverage.
2. **Runner configuration** — impact analysis, recording, or other features on by default.
3. **Parallelism** — a suite on one process, or something that blocks a parallel run.
4. **Framework bootstrap** — configuration and routes reloaded for every test.

Do not delete, merge, or weaken tests to save time until these are measured, and fixed where they are
a cause. A per-test cost that is flat across the suite points at setup overhead rather than at
individual tests. Measure each change against the same baseline — same machine, same test count — and
record wall time.

## One canonical full-suite command

- Expose the full suite as one project script that sets the runner flags and environment for its run.
  Agents and documentation use that script, not a reconstructed runner command.
- Set the coverage driver's mode inside that script. With Composer, use `@putenv XDEBUG_MODE=off` (or
  `coverage`): Composer restarts itself without Xdebug, but its `@php` children and parallel workers
  still inherit the mode from the local `php.ini`. Never depend on, or change, a developer's global PHP
  configuration.
- Let the runner detect the process count, and allow an environment-variable override. Never commit a
  machine-specific count.
- Give coverage its own script that turns instrumentation on explicitly and sets a minimum. Prove the
  minimum enforces: run once with a minimum above the measured coverage and confirm a non-zero exit.

Example for Composer and a Pest version with impact analysis (`${VAR:+…}` needs a POSIX shell):

```json
"test": [
    "Composer\\Config::disableProcessTimeout",
    "@putenv XDEBUG_MODE=off",
    "@php vendor/bin/pest --parallel --no-tia ${TEST_PROCESSES:+--processes=$TEST_PROCESSES}"
]
```

## Runner flags through a wrapper

A framework wrapper can handle the runner's arguments differently from the runner itself. Before a
script passes a runner-only flag through a wrapper, confirm that the wrapper forwards it. Otherwise,
call the runner directly. For example, with Collision 8 and Pest 5, `php artisan test --parallel`
rejects Pest-only flags such as `--no-tia`, while `vendor/bin/pest --parallel` accepts them and applies
Laravel's parallel-testing setup itself.

## Test impact analysis

- Where the runner provides impact analysis, a full-suite command and any CI job that claims full
  regression verification turn it off explicitly. Configuration defaults and environment variables can
  turn it on, and an explicit off flag overrides them. In Pest 5, for example, `PEST_TIA` turns TIA on
  regardless of `tests/Pest.php`, `pest()->tia()->locally()` stays on unless `--ci` is passed, and
  `--no-tia` overrides both.
- Impact analysis records only with a coverage driver active. Enabling it by default keeps
  instrumentation on for every local run.
- Decide from measurement whether it pays off. Check which file changes the runner maps to affected
  tests: an unmapped change reruns the whole suite with instrumentation. In Pest 5, for example, edits
  to Inertia page components map to their tests, but edits to shared Vue components, composables, and
  layouts do not.

## Cached configuration and routes in tests

With `WithCachedConfig` and `WithCachedRoutes` on the base test case, each process captures
configuration and routes once, before the first test body runs. Every later test starts from that
snapshot:

- Change configuration in a test with `config([...])`. The change stays in that test.
- An environment-variable change (`putenv()`, `$_ENV`, `$_SERVER`) does not reach configuration after
  the snapshot. A change made before the snapshot reaches every later test in that process.
- A route registered in a test body applies to that test only. After adopting the traits, verify that a
  route the application changes at boot still carries that change.

Before adopting the traits, search the suite for tests that change environment variables before boot
or reload the application. Then prove isolation with a temporary pair of tests that exercise the
cached state itself: the first changes a cached config value or registers a route, and the second
asserts the original. Keep both in one test file, so they run in order in one process. Tests in
separate files can run in different workers during a parallel run, and then prove nothing. Run the
file on one process and inside a parallel run.

## Changing the database refresh strategy

`testing-best-practices` owns the choice of database refresh trait. Before switching between
`RefreshDatabase` and `LazilyRefreshDatabase`, find tests that depend on when the per-test transaction
starts:

- `RefreshDatabase` begins the wrapping transaction during test setup.
- `LazilyRefreshDatabase` migrates and begins it only when the connection runs its first query or
  starts its first transaction.

A test that leaves the wrapping transaction on purpose — for example, calling `DB::rollBack()` first so
that it can exercise outermost-transaction behavior such as deadlock retries — behaves differently under
the lazy trait when that call comes before the test's first query on the connection. There is no
transaction to roll back yet, so the call does nothing. The test's next query or transaction then
triggers the refresh, and the test's own transaction runs nested inside the wrapping one. The test can
still pass while no longer exercising the behavior it targets. After switching, confirm that each such
test still fails when the behavior under test is broken.

## Verify what a run executed

- Compare the run's test count with the suite's collected count. A matching count alone does not prove
  fresh execution: a replayed run reports the full count too. Also confirm impact analysis was off and
  the output reports no replayed or skipped-by-selection tests.
- Repeat parallel runs to surface order- and timing-dependent failures. A failure that also appears on
  one process, or in the baseline before the change, is not caused by parallel execution alone.
  Investigate its cause — timing, ordering, shared state, environment, or a real defect — before
  attributing it to parallelism or to the test.
