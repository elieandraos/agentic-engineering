# ship-it

Take an approved GitHub issue from implementation through verified delivery.

## When to use it

- Implementing, committing, verifying, or closing an approved issue.
- Checking whether a milestone is ready for a PR, or ready to close.
- Publishing a release once a milestone's PR has merged.

The issue can come from [`plan-it`](../plan-it/) or already exist through another valid
route — what matters is that it's approved, not who drafted it.

## Boring prompts

```shell
"Implement issue #42."
"Commit the approved work for issue #42."
"Check whether this milestone is ready for its pull request."
"Publish the approved release."
```

## What normally happens

1. Establish the correct branch for the work.
2. Implement and verify the issue's scope.
3. Stop for human review — once on the implementation, once on the proposed commit plan.
4. Build coherent commits and push them.
5. Close the issue only once its commits are reachable on the remote.
6. Continue into milestone PR-readiness, release, and post-release work when the
   situation calls for it.

## Ownership

Performs the approved implementation itself. Project context supplies repository and
domain conventions; an applicable stack companion (such as
[`laravel-inertia-stack`](../laravel-inertia-stack/)) supplies technology-specific
implementation knowledge. Deciding what work should exist belongs to
[`plan-it`](../plan-it/); reviewing and merging the PR belongs to the human.

## Install

```shell
npx skills add elieandraos/agentic-engineering --skill ship-it
```

See [`SKILL.md`](SKILL.md) for the complete operational contract.
