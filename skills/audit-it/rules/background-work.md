# Background-work audit

Use the checks that match the requested scope and the system's actual deferred execution: queued
jobs, queued notifications and listeners, batches and chains, scheduled tasks, and work that
events or webhooks start. Read the queue connection, the worker command and its options, and the
deployment's restart behavior when available.

Tenant context and data access on job paths belong to [Database audit](database.md). Sensitive
data in queue payloads belongs to [Security audit](security.md).

For each deferred unit in scope, record what dispatches it, when, and with what payload. List its
side effects in order: database writes, file operations, emails, notifications, broadcasts,
external calls, and further dispatches.

## Side effects under retry

- Assume that every unit can run more than once. For each side effect, determine what happens
  when the unit runs again after that effect has completed. Check whether the effect is
  idempotent, guarded by recorded state, or protected by a key that the receiver honors.
- Check the causes of another run: automatic retries, a reservation that expires before the work
  ends, manual retry of failed work, duplicate dispatch from repeated actions or events, and
  overlapping scheduled runs.
- When an external call succeeds and recording the success fails, determine what the next
  attempt does.

## Interruption and recovery

- Identify each point between claiming the work and recording its outcome. For each point,
  determine the state left behind when the process stops without running its handlers, for
  example on a timeout kill, memory exhaustion, or forced restart. Exception handlers and
  failure callbacks do not run on every interruption. For example, a Laravel worker that times
  out on an attempt below the maximum stops without calling the job's `failed()` method.
- Check that the next attempt or a recovery process completes unfinished work. A status that marks
  work as in progress needs a way to tell abandoned work from live work, such as an owner and an
  expiry. Without it, a guard that makes reruns safe can also make them skip unfinished work.
- Check what users see while work is unfinished, and what cleanup does with it. Include files or
  records that the interrupted run already created or moved.
- After final failure, check the recorded state, the message users receive, cleanup, and whether
  completion callbacks and summaries count the outcome correctly.

## Ordering and execution-time state

- Check whether work dispatched inside a transaction can run before the commit or after a
  rollback. Check the effective setting for each dispatch, not only the connection default. In
  Laravel, for example, compare each dispatch's `afterCommit()` call with the connection's
  `after_commit` option.
- Check that the unit reads the state its decision depends on when it executes, not when it was
  dispatched. Include permissions, membership, preferences, record status, and record existence.
  Check each delivery channel separately.
- Check ordering assumptions between related units, such as chains, batch callbacks, and event
  listeners, and between a unit and the request that dispatched it.
- For a race on shared records, apply the concurrent-write checks in [Database audit](database.md).

## Bounds and configuration

- Compare each unit's timeout, attempts, and backoff with the worker's timeout and memory options
  and the queue's reservation time, such as Laravel's `retry_after`. A reservation that expires
  before the work ends lets a second worker run the same unit.
- Check that calls outside the process, such as external requests and remote storage, have
  timeouts shorter than the unit's timeout.
- Check whether a unit's runtime or memory grows with data until it can exceed its limits at the
  expected workload.
- Check that non-local environments do not run deferred work in the request unless intended. Read
  the effective configuration. If the target environment is unavailable, mark these checks
  unverified.

## Verification

- Tests that call a handler directly or use a synchronous queue do not exercise retries,
  reservations, timeouts, or interruption. Treat that difference as an execution gap.
- Reproduce retry and interruption with a real worker in a disposable local environment. For
  example, stop the worker after the claim, or force a short timeout with a slow fake dependency.
  Let the next attempt run, then inspect records, files, messages, and completion callbacks.
- Separate what the source establishes from what depends on deployment settings that the audit
  could not read.

## Background-work scoring rubric

Use these category weights with the score breakdown in the main skill.

| Category | Points | What to assess |
|---|---:|---|
| Side effects under retry | 35 | Whether each side effect stays correct when a unit runs again, and the causes of repeated runs. |
| Interruption and recovery | 25 | State left by an interrupted run, completion of unfinished work, cleanup, and final-failure handling. |
| Ordering and execution-time state | 25 | Dispatch relative to commit, state and permissions read at execution, and ordering between units. |
| Bounds and configuration | 15 | Consistency of timeouts, attempts, backoff, reservation time, and worker limits with the work and workload. |
