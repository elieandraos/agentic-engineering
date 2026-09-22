# Parallel Implementation Evidence

Status: Evidence from useOrbit #354/#355.

This document records the first real parallel implementation experiment that materially narrowed the execution-layer research. It distinguishes observed runtime behavior from Agentic Engineering behavior and from parent-session improvisation.

## Experiment

Repository: `elieandraos/useOrbit`

Issues:

- #354 — Life policy pages
- #355 — Travel policy pages

Both issues were dependency-ready and structurally parallel. The parent Claude Code session selected them as safe concurrent work and launched two general-purpose background agents in isolated worktrees.

The experiment was allowed to run naturally so that native Claude Code behavior and gaps in the existing Agentic Engineering workflow could be observed.

## Native Claude Code behavior observed

Claude Code successfully provided:

- two parallel background agents;
- an isolated worktree and topic branch for each worker;
- independent worker contexts;
- live progress summaries in the parent UI;
- the ability for the human to switch between the parent and worker sessions;
- completion notifications and terminal worker handback;
- preservation of the Life worker's worktree and branch after an out-of-band interruption;
- runtime notification containing the interrupted worker's worktree path and branch;
- successful restart with a fresh agent against the preserved Life worktree/branch.

The parent session remained active while both workers executed.

No custom worker agent definition, coordinator process, Control Room skill, Herdr runtime, or formal worker-event protocol was required for these capabilities.

## Delegation instructions

The parent explicitly instructed both workers to invoke `implement-it`.

However, the delegation also told each worker to stop once its branch was committed and tests passed.

That instruction conflicted with `implement-it`'s human-gate contract because it implicitly made commit the expected terminal action without requiring the worker to stop and return Review implementation and Commit plan decisions to the human first.

This conflict is important when interpreting the gate failures below.

## #354 Life worker

The completed Life worker invoked:

- `implement-it`;
- `inertia-vue-development`;
- `laravel-inertia-stack`;
- `wayfinder-development`;
- `testing-best-practices`;
- `review-it`.

Observed execution:

- implemented the Life pages;
- ran targeted Life tests: 34/34 passed;
- ran the broader Policies regression scope: 454/454 passed;
- ran frontend verification;
- invoked `review-it`, which reported no findings;
- did not surface Review implementation to the human;
- did not request human approval after the review;
- derived a commit plan internally rather than presenting it;
- did not request Commit plan approval;
- created two commits;
- stopped without pushing, merging, or closing the issue.

The Life worker did not run the unfiltered full project suite.

The first Life agent had previously been interrupted before writing code. Its worktree and branch survived. The parent verified the preserved state and launched a fresh agent into the same workspace.

## #355 Travel worker

The Travel worker invoked:

- `implement-it`;
- `laravel-inertia-stack`;
- `inertia-vue-development`;
- `laravel-best-practices`;
- `testing-best-practices`;
- `wayfinder-development`;
- `my-phpstorm-conventions`.

It did not invoke `review-it`.

Observed execution:

- implemented the Travel pages;
- ran targeted Travel tests: 41/41 passed;
- ran the broader Policies regression scope: 454/454 passed;
- ran the full unfiltered project suite: 1251/1251 passed, 3899 assertions;
- did not surface Review implementation;
- did not request human approval;
- did not invoke `review-it`;
- derived a commit plan internally;
- did not request Commit plan approval;
- created two commits;
- stopped without pushing, merging, or closing the issue.

## Verification inconsistency

The two workers made different full-suite decisions without asking the human:

```text
#354 Life
targeted 34/34
Policies 454/454
no unfiltered full suite

#355 Travel
targeted 41/41
Policies 454/454
full suite 1251/1251
```

This did not preserve the normal human verification decision.

The experiment suggests a cleaner parallel model to test:

- each worker performs targeted verification and the narrowest meaningful broader regression scope;
- each worker completes `review-it` and the normal implementation gates;
- after approved worker commits converge, the parent summarizes worker evidence and presents the normal full-suite decision against the combined state.

The experiment did not verify the final combined branch after both worker branches had been merged.

## Human gates were bypassed

Both workers invoked or operated under `implement-it`, but neither preserved its two human approval boundaries.

Life ran `review-it` but proceeded directly to committing.

Travel did not run `review-it` and also proceeded directly to committing.

Neither worker surfaced:

- Review implementation;
- the `review-it` result as evidence for human manual review;
- Commit plan;
- a human approval request before commit.

The evidence does not show that Claude Code background agents are incapable of preserving these gates.

The stronger direct explanation is that the parent's delegation prompt itself instructed the workers to finish by committing, creating a conflict with the skill-owned stop-and-wait behavior.

A corrected smoke test is required.

## Parent-session branch behavior

The current `implement-it` sequencing rule assumes all issues in a delivery/phase milestone use one shared working branch.

Parallel isolated worktrees made that impossible in practice because the same branch cannot be simultaneously checked out for multiple workers.

The parent therefore improvised:

```text
feat/policies-http-frontend
        │
        ├── issue-354-policies-life-pages
        │       └── Life worker
        │
        └── issue-355-policies-travel-pages
                └── Travel worker
```

After each worker completed, the parent merged its topic branch into `feat/policies-http-frontend` using `git merge --no-ff`.

This topic-branch/convergence behavior was not sourced from `implement-it`. It was parent reasoning introduced to make native parallel worktrees possible.

This exposes a real incompatibility between the current single-working-branch assumption and parallel isolated execution.

## Parent-session post-worker behavior

After worker completion, the parent:

- inspected worker branch state directly;
- merged both worker branches into the shared milestone branch;
- asked the human for approval before push and issue closure;
- after approval, pushed the shared branch and both topic branches;
- closed #354 and #355 with implementation-summary comments.

The parent did not invoke `ship-it` or the relevant `implement-it` push/issue-closure procedures before these actions.

Consequences:

- normal push-readiness validation was bypassed;
- normal issue-closure validation was bypassed;
- the final combined milestone branch was not re-verified after both merges;
- the issue task checkboxes remained unchecked even though the issues were closed and the closing comments described the tasks as implemented.

The last point is visible in GitHub: both #354 and #355 were closed with all task checkboxes still marked incomplete.

## Responsibility trace

```text
Parent
  → inspected milestone/dependencies
  → identified #354/#355 as parallel-safe
  → launched two isolated background agents
  → provided issue-specific delegation prompts
  → recovered interrupted Life workspace
  → received worker handbacks
  → merged worker branches
  → asked human before remote push/closure
  → pushed and closed directly

#354 worker
  → implement-it
  → implementation
  → targeted + broader verification
  → review-it clean
  → gates bypassed
  → commit
  → handback

#355 worker
  → implement-it
  → implementation
  → targeted + broader + full-suite verification
  → review-it not invoked
  → gates bypassed
  → commit
  → handback
```

## What the experiment supports

Observed successfully:

```text
Parallel workers                    ✓
Isolated worktrees                  ✓
Independent worker contexts         ✓
Live worker progress                ✓
Worker completion handback          ✓
Interrupted-worktree preservation   ✓
Worker recovery/restart             ✓ observed
Per-worker targeted verification    ✓
Per-worker broader verification     ✓
```

Not preserved or not validated:

```text
Consistent review-it per worker     ✗
Review implementation gate          ✗
Commit plan gate                    ✗
Human full-suite decision           ✗
Combined post-merge verification    ✗
Normal push-readiness procedure     ✗
Normal issue-closure procedure      ✗
Issue task completion               ✗
```

## Current interpretation

The experiment does not support building a new orchestration platform.

It supports a smaller hypothesis:

> Claude Code already provides the parallel execution substrate. Agentic Engineering needs to preserve its existing implementation, review, verification, commit, push, and closure contracts when multiple implementation workers run concurrently.

The next smoke test should test that hypothesis directly before any durable methodology change is accepted.
