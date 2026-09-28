# Normal Parallel Wave Evidence — Phase 26 #362/#358/#363/#373

Status: Evidence. Observed during normal useOrbit delivery on released Agentic Engineering v2.2.0, not a designed smoke test.

## Boundary

The human authorized one four-issue wave after the parent inspected thirteen dependency-ready issues and mapped expected file overlap. The selected issues were #362, #358, #363, and #373. No two selected workers ultimately touched the same file.

The wave ran from approximately 10:46 to 11:22 EEST and ended with all four issues merged into `feat/policies-http-frontend`, pushed, and closed.

This record preserves observed behavior. It does not prescribe a Control Room architecture or runtime procedure.

## Wave lifecycle observed

The parent:

1. selected a concurrent-safe subset after explicit human interest in parallel execution;
2. launched four general-purpose Claude Code workers with worktree isolation;
3. collected worker reports asynchronously while keeping the human in the parent session;
4. routed one product decision back to the correct worker;
5. waited for all four candidate implementations before the wave-level full-suite decision;
6. assembled a temporary combined candidate and ran one fresh full suite;
7. batched four Review implementation decisions into one human interaction;
8. resumed workers to derive commit plans and batched the four Commit-plan approvals;
9. resumed workers to create approved commits;
10. converged the four approved issue branches sequentially into the milestone branch;
11. obtained push authorization, pushed, then batched issue-closure choices;
12. wrote durable closing records and handoffs, re-fetched GitHub state, and recomputed the milestone.

The combined suite passed 1331 tests / 4493 assertions with `--no-tia`.

## Human decision routing

This run directly exercised a responsibility that earlier smoke tests had not.

Issue #373 initially implemented a button labelled `Export PDF`. The worker surfaced the wording choice. The parent presented it while the other workers continued. The human chose `Export`. The parent resumed the #373 worker, which changed all six headers, re-ran its frontend checks, and returned to candidate-ready state.

The combined candidate was assembled only after that correction, so the wave-level regression evidence covered the human-approved label.

This is direct evidence that the coordinating context can receive a worker decision, present it to the human, route the answer back to the correct worker, and allow siblings to continue independently.

## Human-facing gate presentation

### What worked

The parent successfully synchronized asynchronous work into shared human boundaries:

- one wave-level full-suite run/skip decision;
- one batched Review implementation interaction containing four per-issue decisions;
- one batched Commit-plan approval after all four plans existed;
- one push authorization;
- one batched closure interaction with per-issue selection.

Per-issue approval semantics remained distinct even when the UI batched them.

The Commit-plan presentation preserved useful decision evidence: commit count, semantic grouping, messages, ordering, and notable reconstruction constraints per issue.

### What did not

Review implementation was too compressed to support a confident human review.

The installed rule requires each Review implementation report to include activated skills, what changed, implementation approach, verification, and `review-it` result. The parent omitted the `Activated skills:` line for all four. More importantly for human usability, #362 never received a substantive text summary before its approval question; the parent incorrectly said all issue details had already been relayed.

The human therefore had the approval controls but not one compact wave-level summary preserving enough implementation substance for each issue.

This repeats the earlier human-presentation signal from the smoke tests, but with a clearer boundary: batching itself worked; evidence compression was the problem.

### Real-time orientation

Intermediate checkpoints arrived as workers/plans/commits completed:

- workers: 1/4, 2/4, 3/4, then 4/4;
- commit plans: 1/4, then 3/4, then 4/4;
- commits: 2/4, then 3/4, then 4/4.

The human reported the overall UX as good but occasionally lost orientation when a large partial table was followed by another worker result later.

This suggests a presentation question, not a worker-lifecycle failure: a coordinating surface may need a compact, stable wave-progress view while still surfacing material exceptions and batching decision-ready evidence.

## Combined candidate verification

The parent created a detached temporary worktree at the milestone base `151a6b0`.

For each worker it:

- produced a binary diff from `151a6b0`;
- applied that patch to the combined copy;
- copied untracked files;
- prepared local dependencies/runtime state.

Worker branches remained unmodified and uncommitted during this step.

The full PHP suite ran fresh with TIA disabled:

```text
1331 passed
4493 assertions
```

The temporary combined worktree was then removed.

After commit creation and convergence, the parent verified each issue branch's files were identical in final HEAD and that all 47 changed files matched the approved content. It did not directly diff the already-deleted combined worktree against final HEAD, so final equivalence was established through a chain of per-worker/final-state checks rather than one direct comparison.

No combined frontend type check or build ran; #373 had performed its own frontend checks.

This is a second normal execution data point showing a workable uncommitted-union verification mechanism, but the mechanism remains runtime-specific and is not promoted here into portable methodology.

## Runtime and provisioning observations

### Worker base mismatch

All four Claude Code isolated worktrees were initially created from `main` at `a529ff6`, despite the parent brief describing them as cut from the milestone branch at `151a6b0`.

#373 detected the mismatch. The parent broadcast the invariant to the other workers. Each worker corrected its branch to `151a6b0` before editing. The recovery instruction explicitly prohibited resetting over existing work.

The final issue branches were therefore based correctly, but the runtime did not provision them in the state the parent believed it had requested.

### Dependency provisioning

The parent brief told workers to symlink `vendor`. That failed: Pest/autoload resolution followed the main checkout rather than worker code. Workers replaced the symlink with copied dependencies; some ran `composer dump-autoload` and one independently confirmed class resolution from its own worktree.

`node_modules` was symlinked successfully in this run. Workers copied `.env`; backend workers also copied `public/build`.

For #373, Wayfinder generation required `--with-form` because the project enables form variants.

These are runtime/stack observations, not portable worker-provisioning rules.

### Permission layer

Claude Code auto-mode blocked:

- the initial batched convergence merge;
- a read-only status command immediately after that block;
- the initial push.

The parent stopped each time and did not route around the permission boundary. The operations succeeded after the human explicitly asked it to retry.

This produced duplicate human friction after Agentic Engineering had already authorized the engineering action, but the runtime permission layer and methodology approval layer are distinct concerns.

### Worker lifecycle and cleanup

A worker described as "holding" had actually ended and was later resumed through the runtime.

Twelve older clean/merged worktrees were removed during the wave only because the human explicitly requested cleanup. The four current worker worktrees remained after successful convergence and issue closure. Runtime-created `worktree-agent-*` branches also remained; twenty-two were observed after cleanup of the old worktrees.

This repeats the earlier evidence that temporary workspace retirement has no clear owner after a wave completes. Do not infer a blanket cleanup command from this observation: interrupted, dirty, locked, or otherwise recoverable workspaces require different handling.

## Methodology adherence

Observed deviations from already-correct guidance:

- Review implementation presentations omitted the required `Activated skills:` line.
- #362's substantive Review implementation report was not relayed before approval.
- immediate trailer verification was not performed after every merge commit; later range verification caught up before push.
- worker branches were initially provisioned from the wrong base, though corrected before implementation.

These are not evidence that the corresponding methodology rules are missing.

One unresolved review question remains: #373's label-only change was re-verified with frontend checks but `review-it` was not re-run. Whether that materiality threshold should invalidate the prior review remains unresolved.

## Durable records

All four issues were closed with all task boxes checked and commit/test evidence in their closing comments. #362 also left implementation handoffs on #369 and #371 because its refactor changed the surface those approved issues will later modify.

The #373 closing comment says browser verification had not happened. The human reports that the Export behavior was manually checked before closure. The durable comment is therefore stale on that point even though the implementation itself was verified and closed.

## Responsibility evidence

### Specialist skills

`implement-it` and `review-it` continued to own per-issue engineering semantics: implementation, targeted verification, review, Review implementation evidence, Commit plan, commit correctness, push readiness, and closure requirements.

### Workers

Each worker owned one issue's implementation and specialist evidence. Workers surfaced decisions or observations rather than resolving genuine human choices silently.

### Coordinating parent

The parent performed responsibilities requiring cross-worker/lifecycle context:

- concurrent-safe issue selection;
- worker launch and synchronization;
- routing a human decision to one worker;
- deciding when the wave had reached combined-verification readiness;
- assembling/running the combined candidate mechanism;
- batching human-facing Review implementation and Commit-plan interactions;
- choosing convergence order and performing convergence;
- coordinating push and individual issue closures;
- carrying forward implementation handoffs.

### Runtime

Claude Code supplied isolated workers/worktrees, completion/resumption mechanics, permission enforcement, and worker identity. It also created worktrees from an unexpected base and retained runtime branches/workspaces after the wave.

### Human

The human authorized concurrency, chose the #373 product wording, chose to run combined verification, approved four implementations and four commit plans, authorized push and closure, requested old-worktree cleanup, and supplied manual UI verification.

## Findings to retain

1. Human decision routing is now directly observed in normal parallel work.
2. Batched human gates can preserve per-issue decisions; batching itself is not the UX problem.
3. Review implementation needs enough implementation substance to make approval meaningful; this presentation gap has now recurred beyond designed smoke tests.
4. Real-time parent checkpoints can become disorienting when partial batches are presented without a stable wave-progress orientation.
5. Combined uncommitted-union verification worked again, but its assembly mechanism remains runtime-specific.
6. Runtime worker provisioning can violate the intended milestone base; effective workspace state must be verified before implementation.
7. Dependency sharing through symlinked `vendor` was unsafe in this Laravel worktree setup.
8. Runtime permission prompts can duplicate already-made methodology decisions without changing the underlying engineering authorization.
9. Temporary worktree/branch retirement remains unowned after successful wave completion and has now recurred during normal post-release use.
10. Parent-performed convergence/push/closure can preserve issue lifecycle semantics without requiring the original worker process to perform every mutation.
11. Research/watch evidence must remain distinct from active execution policy; none of these runtime observations is automatically a new portable rule.
