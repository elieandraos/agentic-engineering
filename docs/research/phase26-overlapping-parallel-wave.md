# Normal Overlapping Parallel Wave Evidence — Phase 26 #359/#360

Status: Evidence. Observed during normal useOrbit delivery on released Agentic Engineering v2.2.1, not a designed smoke test.

## Boundary

A normal `what's next` request produced nine dependency-ready Phase 26 issues. Canonical v2.2.1 independently analyzed expected collisions, recommended a safe disjoint four-issue wave, offered #359 as a serial alternative, and waited for human authorization.

The human deliberately overrode that safe recommendation and authorized #359 and #360 together because their issue descriptions predicted overlap. The resulting overlap/conflict behavior is therefore evidence from an explicitly chosen experiment inside normal project work, not evidence that v2.2.1 failed to select safely.

The wave ended with both issues implemented, reviewed independently, combined and verified, approved, committed, converged, pushed, closed, and their temporary workspaces retired.

## v2.2.1 validation

The released sequencing correction behaved as intended:

- computed the ready set when asked what's next, without requiring a preceding closure;
- compared candidate issues and surfaced expected file collisions;
- recommended a materially useful concurrent subset rather than only one issue;
- preserved a serial alternative;
- did not treat recommendation as authorization;
- started no worker until the human explicitly chose an execution shape.

The real conflict, combined-candidate reconciliation, and convergence conflict happened only because the human deliberately selected the overlapping #359/#360 pair.

## Runtime worker provisioning

### Automatic worktree base

Both first-attempt Claude Code isolated workers were created from `main` at `a529ff6`, not the checked-out milestone branch at `8b6fc67`.

A base-invariant check in the worker prompts detected the mismatch before either worker edited anything. Both stopped. Claude Code automatically removed those unchanged runtime-created worktrees when the workers ended.

The parent then created explicit worktrees at `8b6fc67` and relaunched the workers there.

This repeats the wrong-base behavior already observed in the previous normal four-issue Phase 26 wave. It is recurring Claude Code runtime/provisioning evidence, not a missing branch-selection rule in `implement-it`.

### Laravel dependency isolation

The parent initially instructed workers to symlink `vendor`. #360 discovered that Composer/autoload resolution then loaded application classes from the main checkout rather than the worker worktree. Its first route test failed because the runtime found the old controller method.

#360 replaced the symlink with a real copied `vendor` tree. #359 had independently encountered the same class-resolution problem and also switched to a real copy before any passing test result. Every passing worker result therefore exercised that worker's own application code.

This repeats the symlinked-`vendor` failure from the previous normal wave and strengthens it: the failure can produce verification against the wrong source tree, not merely an inconvenient setup error.

Observed companion environment state in this run:

- symlinked `node_modules` worked for frontend type/build checks;
- `.env` was copied;
- worker and combined worktrees generated fresh frontend build output;
- Wayfinder output was regenerated for #360 and remained gitignored.

These are runtime/stack observations, not portable provisioning procedure.

## Per-issue candidate results

### #359 — policy-class enforcement at the route layer

Outcome:

- introduced `EnsurePolicyClass` middleware;
- registered `policy-class` after route-model binding in middleware priority;
- applied class middleware to six policy-class route groups and the members route;
- removed 26 inline class checks from thirteen controllers while retaining the Medical group-type check;
- added twelve Edit/Update regression tests.

The six invalid-payload Update tests failed before the change because validation redirected instead of returning the intended 404.

Worker verification: 296 targeted tests / 1485 assertions and Pint. `review-it` reported clean, with limitations noted around a route-parameter typo producing `ValueError`, no dedicated middleware test file, and expected overlap.

### #360 — invokable policy controllers

Outcome:

- converted Agent, Carrier, Client policy-tab controllers and `PolicyMembersController` to `__invoke()`;
- changed route registrations to controller-class form without changing names/URLs;
- changed Client policy-tab authorization to `#[Authorize('view', 'client')]`;
- added a 403 regression test.

The new authorization test failed when the old `viewAny` attribute was restored.

Worker verification: 22 targeted tests / 160 assertions, Pint, type check, and frontend build. `review-it` found one minor problem in the test's `Gate::before` closure; the worker fixed it with an `instanceof Client` guard and the scoped re-review was clean.

## Real overlap and reconciliation

The workers both changed three files:

| Surface | #359 candidate | #360 candidate | Combined behavior |
| --- | --- | --- | --- |
| `PolicyMembersController` | remove inline policy-class check/import | `index` → `__invoke` | auto-composed cleanly |
| `routes/policies.php` | six `policy-class:{class}` groups | Client tab uses invokable controller | auto-composed cleanly |
| `routes/members.php` | array controller action + `policy-class:medical` | invokable controller class, no class middleware | conflict |

The members-route conflict required a state present in neither worker candidate:

```php
Route::get('policies/{policy:slug}/members', PolicyMembersController::class)
    ->middleware('policy-class:medical')
    ->name('policies.members.index');
```

Choosing either worker's line alone would have dropped approved behavior from the other issue. The coordinating parent composed both intents.

This is the first normal-use evidence in this research set where a coordinating context authored reconciled implementation content that existed in neither worker's reviewed state.

## Combined candidate

The parent created a detached disposable worktree from milestone SHA `8b6fc67`.

Worker changes were captured as binary diffs; untracked content such as the new middleware was captured separately. #359 applied cleanly. Applying #360 with three-way patching produced the expected members-route conflict. The parent resolved that conflict by composing both workers' intent.

The combined worktree used a real copied `vendor`, symlinked `node_modules`, copied `.env`, and fresh frontend build state.

Combined targeted verification passed:

- 418 tests;
- 2118 assertions;
- Pint;
- frontend type check;
- frontend build;
- route inspection confirming the expected middleware chain;
- scan confirming no inline policy-class checks remained.

Neither worker worktree nor the milestone branch was mutated by combined verification.

## Wave-level regression verification

The human chose to run the full suite because #359 changed middleware ordering at an application boundary.

Command:

```shell
php artisan test --compact --no-tia
```

Result:

- 1344 tests passed;
- 4506 assertions;
- fresh run with impact analysis disabled;
- one warning was reported, but the available output contained no warning details.

The combined candidate's Git tree was recorded as `2c01b8c9…`.

## Review validity observation

Each worker's `review-it` ran before combination and covered only that worker's own uncommitted candidate.

No `review-it` invocation covered the parent-authored members-route reconciliation, and no review was rerun after combination.

Before Review implementation, the reconciled combined state did receive:

- 418 combined targeted tests;
- Pint;
- type check;
- frontend build;
- route/middleware inspection;
- the fresh 1344-test full suite.

The human-facing Review implementation reports explicitly noted that the one-line conflict resolution existed only in the combined worktree.

This is evidence to retain. It does not by itself decide when parent-authored reconciliation invalidates specialist review or who should own renewed assurance.

## Human-facing checkpoints

### Candidate / combined-verification checkpoint

The parent presented:

- how the combined candidate was assembled;
- the overlapping files and conflict;
- the actual reconciled route behavior;
- combined targeted verification;
- short per-worker implementation and `review-it` summaries;
- one wave-level full-suite run/skip decision.

The human liked the compact wave summary.

### Review implementation

After the full suite, the parent presented separate #359 and #360 approval blocks containing:

- `Activated skills:`;
- implementation outcome grouped by responsibility;
- tests and failing-before evidence;
- worker, combined, and full-suite verification;
- `review-it` result and limitations.

The human initially experienced this as a second review because it repeated some implementation information from the candidate checkpoint.

The distinction that emerged during use was:

- candidate checkpoint: what happened across workers, where they interacted, and what combined verification decision is needed;
- Review implementation: what changed in the codebase, how it was implemented, and what proof/review supports approval.

The human also wanted a compact **Code surface** view in Review implementation, grouped by responsibility rather than a raw filename dump.

### Commit plan

The Commit-plan checkpoint felt distinct because it answered how approved work should become Git history and converge:

- #359: one atomic middleware/route/controller/test commit;
- #360: one invokable-controller refactor commit, then one Client-authorization behavior/test commit;
- planned merge order;
- planned reproduction of the already-tested conflict resolution;
- planned final-tree equivalence check.

This sharpens the presentation problem: the lifecycle decisions are distinct, but candidate and Review implementation presentations need enough differentiation that they do not feel like duplicate reviews.

## Commit construction and convergence

#359 produced one semantic commit.

#360 produced two semantic commits because the invokable-controller refactor and Client authorization change were separate decisions. The intermediate invokable-only state was tested before the authorization commit was added.

Convergence order:

1. merge #359 into the milestone branch — clean;
2. merge #360 — the same `routes/members.php` conflict reproduced;
3. copy/reproduce the already-tested combined resolution.

The second merge's default `--no-edit` message included Git-generated `# Conflicts:` lines. Because the merge was still unpublished, the parent amended only the message to the approved clean merge message. The tree and merge parents remained unchanged.

Mechanical trailer checks were run after all three issue commits and both merge commits.

## Final-tree equivalence

After convergence, the parent compared the final milestone tree with the Git tree recorded for the fully tested disposable combined candidate.

They were identical.

This connected:

```text
uncommitted reconciled candidate
        ↓
combined targeted verification
        ↓
fresh full suite
        ↓
human implementation approval
        ↓
semantic issue commits
        ↓
real convergence + same conflict resolution
        ↓
identical final Git tree
```

No full suite was rerun after convergence because the final tree was the same tree that had already passed it.

This is direct evidence that final-tree identity can bridge verification of a disposable pre-approval combined candidate to later converged history in at least this small compatible-overlap case. It is not promoted here into a universal requirement.

## Push and closure

Five commits were unpushed: three issue commits and two merge commits.

The unpushed range passed the mechanical trailer re-check. The milestone tree still matched the approved combined candidate. The push was a normal fast-forward and remote reachability was verified afterward.

Both issues were closed with all four task boxes checked. Closing comments recorded implementation, targeted/failing-before evidence, `review-it`, the single combined full-suite result, commit/merge SHAs, concurrent-wave provenance, and the members-route reconciliation.

No deferred handoff to another issue was needed.

## Workspace lifecycle and cleanup

The human authorized cleanup after convergence only for items proven safe.

Before removal, the parent checked relevant workspace/branch state including:

- merged/reachable state;
- clean worktree state;
- lock/in-use state;
- stash state;
- no unmerged branch state.

Seven worktrees were removed:

- four left from the previous successful wave;
- #359;
- #360;
- the detached combined worktree.

The combined worktree required forced removal because it intentionally still contained staged combined-candidate content. Before force-removal, the parent verified no unstaged/untracked content and that its index tree equalled the pushed milestone tree.

Forty merged branches were removed with ordinary branch deletion:

- eighteen `issue-*` branches;
- twenty-two runtime-created `worktree-agent-*` branches.

Three unrelated `merge-issue-*` branches were left untouched because cleanup authorization did not cover them.

The two failed first-attempt automatic worker worktrees had behaved differently: Claude Code removed them automatically when their unchanged workers ended. Successful/manual worker worktrees persisted until explicit cleanup.

This sharpens the workspace-lifecycle question from "worktrees remain" to "which execution state makes a temporary workspace safe and appropriate to retire, and which layer owns proving that state?"

## Shared runtime state

#359 used `git stash` for a before-change verification check. The stash stack is repository-shared across worktrees, so a bare stash operation can interact with entries created from another worktree. The parent confirmed the stash was empty before combined assembly and cleanup.

No harm occurred in this run. Retain this as runtime/worktree evidence rather than portable procedure.

## Responsibility evidence

### Specialist methodology

Canonical v2.2.1 correctly owned:

- ready-set computation and execution-shape recommendation;
- explicit human authorization before concurrency;
- worker hold before Review implementation;
- one wave-level full-suite decision;
- Review implementation and Commit-plan approvals;
- semantic commit reasoning;
- push readiness and trailer discipline;
- issue closure;
- next-work recomputation.

### Workers and specialist review

Each worker owned one issue's implementation, targeted/failing-before verification, companion activation, and `review-it`.

### Coordinating parent

The parent owned or performed the cross-worker/runtime-sensitive work observed here:

- worker prompts and base invariants;
- explicit replacement-worktree provisioning after runtime mismatch;
- combined-candidate assembly;
- conflict reconciliation;
- combined verification;
- human-facing candidate/Review/Commit-plan presentation;
- commit splitting mechanics;
- convergence;
- reproduction of the tested reconciliation;
- final-tree equivalence;
- push/closure coordination;
- evidence collection and cleanup.

Some of these may eventually belong to runtime adapters rather than Control Room. This document records behavior, not final ownership.

### Claude Code runtime

Claude Code:

- created automatic isolated worktrees from `main` rather than the milestone tip;
- auto-removed unchanged failed-worker worktrees;
- locked a worktree while its worker was running;
- routed worker reports and parent corrections;
- retained runtime-created branches from successful prior work.

### Human

The human:

- deliberately authorized the overlapping pair despite the safer recommendation;
- chose the wave-level full suite;
- approved each implementation;
- approved the Commit plans/convergence;
- authorized push and closure;
- authorized bounded cleanup;
- supplied UX feedback after experiencing the checkpoints.

## Methodology adherence

v2.2.1's intended behavior held through the wave.

Observed deviations from existing project/runtime guidance included:

- the parent used `pint --test` in the combined worktree despite project instructions not to use that mode;
- one worker used `/tmp` rather than the designated scratchpad;
- one worker used shared `git stash` despite worktree guidance against bare stash usage.

These are execution deviations, not evidence that the portable methodology lacks those rules.

Parent mechanisms not specified by portable methodology included environment preparation, patch-based combined assembly, conflict reconciliation, final-tree equivalence, and cleanup.

## Findings to retain

1. v2.2.1's proactive execution-shape recommendation worked during normal milestone entry without weakening human authorization.
2. Wrong-base automatic worktree provisioning recurred across normal waves.
3. Symlinked Laravel `vendor` resolving application code from the main checkout recurred and can invalidate worker verification if undetected.
4. Real shared-file overlap can be mostly auto-composable while still producing a small semantic conflict.
5. The first real conflict required parent-authored code that existed in neither worker's reviewed state.
6. Combined targeted and full-suite verification can validate that reconciled state before Review implementation.
7. Specialist `review-it` did not cover the parent-authored reconciliation; review validity after material reconciliation remains unresolved.
8. The same conflict reproduced during real convergence.
9. Final Git-tree identity connected the fully tested disposable candidate to the final converged history in this run.
10. Candidate-verification and Review implementation are distinct human decisions but can feel duplicative when their presentations repeat the same implementation recap.
11. Review implementation would benefit from a compact code-surface view grouped by responsibility; retain this as human-facing coordination evidence, not a `review-it` rule.
12. Commit-plan presentation remained distinct because it represented approved work as semantic history and convergence.
13. Runtime-created failed workspaces may auto-retire while successful/manual workspaces persist, so workspace retirement depends on execution state rather than one blanket cleanup action.
14. Repository-shared stash state is another cross-worktree runtime concern.
15. Cleanup can involve worktrees and runtime-created branches, and bounded authorization matters when unrelated branches remain.
