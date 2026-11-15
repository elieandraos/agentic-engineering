# Test Execution

How this stack runs its test suite: locally, for coverage, and in CI. `testing-best-practices`'s
`rules/performance.md` owns the baseline settings — Xdebug off, `WithCachedConfig` and
`WithCachedRoutes`, `--parallel`, global fakes, and the conditions a test must meet to run in
parallel. This file does not restate them. It adds measurement discipline, command-scoped
instrumentation, the tooling traps behind those settings, and how to verify that a run executed what
it claims. The consuming project owns its actual commands, thresholds, and process counts.

## Measure before restructuring tests

A slow suite is usually slow because of what surrounds the tests, not the tests themselves.
Investigate in this order before you restructure tests:

1. **Instrumentation** — whether a coverage driver (Xdebug in `coverage` mode, PCOV) is active for
   runs that collect no coverage.
2. **Runner configuration** — whether impact analysis, recording, or other runner features are on by
   default.
3. **Parallelism** — whether the suite runs on one process, and what blocks a parallel run.
4. **Framework bootstrap** — whether each test reloads configuration and routes.

Do not delete, merge, or weaken tests to save time until these four are measured, and fixed where they
are a cause. A per-test cost that is flat across the suite points at setup overhead, not at individual
tests. Measure each change against the same baseline — same machine, same test count — and record wall
time.

## One canonical full-suite command

- Expose the full suite as one project script that sets the runner flags and environment for its own
  run. Agents and documentation use that script, not a reconstructed runner command.
- Scope the coverage driver to the command. With Composer, set `@putenv XDEBUG_MODE=off` (or
  `coverage`) inside the script. Composer restarts itself without Xdebug, but `@php` children and
  parallel workers still inherit the mode from the local `php.ini`; `@putenv` reaches all of them.
  Never depend on, or change, a developer's global PHP configuration.
- Let the runner detect the process count, and allow an environment-variable override. Never commit a
  machine-specific count. The detected count is logical CPUs; measure whether speed keeps improving up
  to it before treating a higher count as faster.
- Give coverage its own script that turns instrumentation on explicitly and sets a minimum. Prove the
  minimum enforces: run once with a minimum above the measured coverage and confirm a non-zero exit.

Example for a Composer project on Pest 5 with TIA available (drop `--no-tia` where the installed Pest
has no TIA, because the option is then unknown):

```json
"test": [
    "Composer\\Config::disableProcessTimeout",
    "@putenv XDEBUG_MODE=off",
    "@php vendor/bin/pest --parallel --no-tia ${TEST_PROCESSES:+--processes=$TEST_PROCESSES}"
]
```

`${VAR:+…}` expansion needs a POSIX shell.

## Call Pest directly for parallel runs

As of Collision 8 with Pest 5, `php artisan test --parallel` validates its arguments against ParaTest's
option set. It rejects Pest-only flags such as `--no-tia` ("The "--no-tia" option does not exist") and
handles `--coverage` and `--min` itself. A serial `php artisan test` forwards Pest-only flags, but it also
removes some options (`--compact`, `--coverage`, `--min`, `--profile`, `--env=`) and handles them
itself. For parallel runs, call `vendor/bin/pest --parallel`: Pest's own Laravel parallel handler
sets Laravel's `ParallelRunner` and the `LARAVEL_PARALLEL_TESTING` environment, as artisan does.
Recheck this after upgrading Collision or Pest.

## Test impact analysis

Durable guidance:

- Where the installed runner provides impact analysis, a full-suite command and every CI test job turn
  it off explicitly. A run that claims fresh execution must not select or replay tests.
- Impact analysis records only with a coverage driver active. Enabling it by default keeps
  instrumentation on for every local run.
- Decide from measurement whether it pays off for the project. When the full suite is already fast,
  the saving is small, and every fallback to a full rerun costs a full instrumented run.

Current Pest 5 behavior (recheck after upgrading Pest):

- `pest()->tia()->locally()` turns TIA off only when `--ci` is passed. A CI job that runs
  `vendor/bin/pest` without `--ci` records coverage for every test and discards it when the job ends.
- The `PEST_TIA` environment variable turns TIA on regardless of `tests/Pest.php`. An explicit test
  path or filter also switches TIA off, but a full-suite run has neither, so full-suite commands pass
  `--no-tia` explicitly.
- Pest maps an edit to an Inertia page component (`resources/js/pages/`, `resources/js/Pages/`) to the
  tests that render that page. Other frontend files depend on Pest's Vite dependency resolver, which
  cannot parse Vue single-file components. An edit to a shared component, composable, or layout
  therefore falls back to rerunning every test with coverage recording.

## Cached configuration and routes in tests

When the base test case uses `WithCachedConfig` and `WithCachedRoutes`, each process captures
configuration and compiled routes in the first test's `setUp`, and every later test starts from that
snapshot.

- Change configuration inside a test with `config([...])`. The change stays inside that test.
- Changing an environment variable (`putenv()`, `$_ENV`, `$_SERVER`) to influence configuration has no
  effect after the first test in a process, because configuration files are not read again. The reverse
  also holds: an environment change made before the snapshot is taken ends up in the configuration of
  every later test in that process.
- A route registered in a test body applies to that test only. Routes the application changes at boot
  (for example, in a `booted` callback) still apply; verify one such route after adopting the traits.

Before adopting the traits, search the suite for tests that change environment variables before boot
or reload the application. Prove isolation with a temporary pair of tests — one changes a config
value, the next asserts the original — on one process and in parallel.

## Verify what a run executed

- Compare the run's test count with the suite's collected count. A matching count alone does not prove
  fresh execution: a replayed run reports the full count too. Also confirm impact analysis was off and
  the output reports no replayed or skipped-by-selection tests.
- Repeat parallel runs to surface order- and timing-dependent failures. A failure that also appears on
  one process, or in the baseline before the change, is a determinism defect in that test, not a
  parallel-run defect.
