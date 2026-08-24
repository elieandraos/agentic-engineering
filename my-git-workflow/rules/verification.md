# Verification

## Principle

> Verify the property that matters at the boundary being crossed. The completed working tree, each
> semantic implementation step, the integrity of an intermediate committed state when that itself
> needs proof, and the final assembled history are different things to prove — proving one does not
> substitute for proving another.

This rule owns what verification is required at each lifecycle boundary in `my-git-workflow`, and
the isolation-verification escalation for when an intermediate committed state itself needs proof.
It does not own commit boundaries (`rules/commit-boundaries.md`) or the review gates verification
results get reported into (`rules/review-gates.md`).

The lifecycle this rule verifies:

```
implementation complete → full-suite verification → Gate 1
Gate 1 approved → build semantic commits → targeted verification per commit
  (when an intermediate committed state itself needs proof → isolation verification)
all commits assembled → final full-suite verification at the completed-issue boundary
```

Two full-suite runs appear in that lifecycle — one before Gate 1, one at the completed-issue
boundary — and they are not a duplicate of each other, even when both run the same command:

> The pre-Gate-1 full suite proves the completed implementation works as one working tree, before
> any commit history exists to review or split. The completed-issue full suite proves the final
> assembled commit history — however many commits the issue became, whatever order they landed in —
> reconstructs that same correct result once the semantic commits actually exist.

Both stay in the loop. Don't drop one because the other already ran green — they prove different
things, even when the command that produces the result is identical.

## Discover the project's verification tools

This rule does not prescribe a test runner, formatter, or linter. Determine what the consuming
project actually uses — its:

- test runner;
- formatter/linter or other static checks;
- mechanism for running a targeted subset of tests (by path, tag, or similar);
- full regression command.

Discover these from the repository's own instructions, applicable project/stack skills,
configuration, scripts, CI definitions, or established usage — the same discovery discipline
`rules/release.md` applies to release mechanism, not an assumption this rule makes in advance. Git
and GitHub remain core substrate for this workflow; test and format tooling is stack- and
project-specific composition on top of it.

## Pre-Gate-1 verification

Once the approved issue's implementation is complete, and before reporting at Gate 1
(`rules/review-gates.md`):

1. Run the project's formatting/lint check.
2. Run the full regression suite.
3. Report the exact results at Gate 1.

This validates the complete working tree as one coherent whole, before any commit history has been
written to split it. It is the last point at which "does the implementation work" is answered
without any interference from how it will later be divided into commits.

## Default commit-building loop: targeted per commit, full suite once at the issue boundary

While building each semantic commit — whether the issue lands as one commit or several
(`rules/commit-boundaries.md`) — verify it with:

- the tests actually relevant to that commit's change;
- the project's formatting/lint check.

Do not reflexively run the full regression suite after every commit. It's slow, and for a commit
that's deliberately inert — structurally complete but not yet activated, per
`rules/commit-boundaries.md` — a full-suite run proves nothing the targeted run didn't already
cover.

Run the **full regression suite once**, at the completed-issue boundary: after the last commit for
the issue, before reporting the issue done. Report the exact pass/skip/fail results wherever the
project's tooling provides them.

The two verifications prove different things:

- targeted verification proves the semantic decision that commit represents is correct;
- the completed-issue full suite proves that the issue, landed as however many commits it took,
  did not regress anything else in the system.

## Isolation verification: a deliberate escalation, not the default

> Do not use isolation verification merely because an issue was split into multiple commits. Use it
> when the correctness of an intermediate committed state is itself a property that needs to be
> proven — not assumed from how the working tree was tested during implementation.

Reach for this when, for example:

- semantic history is being reconstructed from an already-implemented diff, after the fact;
- commit order is itself load-bearing for correctness — an activation step depends on earlier
  commits already being in place (see "Ordering commits" below);
- an intermediate commit's standalone correctness can't safely be inferred from how the working
  tree was tested during implementation.

The technique:

1. Commit the semantic group.
2. `git stash push -u -m "<description>"` — hides every remaining change (staged, unstaged, and
   untracked), leaving the working tree at exactly the state of the commits made so far.
3. Run the project's formatting/lint check and its **full** regression suite against that isolated
   committed state.
4. `git stash pop` — restores the remaining work.
5. Repeat for each subsequent semantic commit: stage the next group, commit, stash the rest, verify
   in isolation, pop.
6. After the final commit, run the completed-issue full-suite check with nothing stashed — the
   same check described above.

This is intentionally expensive — a full suite run per commit — which is exactly why it stays an
escalation, not the default for every multi-commit issue. An issue with no ordering or
reconstruction risk verifies each commit with its own targeted tests, same as the default loop, and
needs isolation verification for none of them.

## Ordering commits to keep intermediate states valid

Watch for any change to configuration, feature flags, environment-conditioned behavior, or another
runtime activation gate — flipping one of these can retroactively change what's under test. A test
conditioned on that gate is silent until the moment it flips, and the instant it does, every test
that was quietly inactive starts running immediately, against whatever code currently exists.

Before committing a step that activates a gate:

1. Identify what behavior and tests become active as a result.
2. Inspect existing tests too, not only ones the current issue adds — an unrelated pre-existing test
   can be gated on the same condition.
3. Verify every dependency those newly active paths require is already present in an earlier
   commit.
4. If it isn't, reorder the commits so it is.

The underlying principle:

> Activation comes after the dependencies required by what it activates. A commit must not read as
> green merely because a gate hid the assertions that would have failed once activated.

For example: commit A introduces supporting code while a feature stays disabled; commit B wires the
behavior to that support, still inactive; commit C flips the feature on. C must land after A and B —
enabling the feature activates tests and code paths that depend on both, and landing C first would
make it green only because the gate was still hiding what it activates.

## Do / Don't

**Do**
- Run the full suite before Gate 1, against the complete working tree.
- Verify each semantic commit with the tests and checks relevant to its own decision.
- Run the full suite once more at the completed-issue boundary, after all commits are assembled.
- Use isolation verification when an intermediate committed state itself needs proof.
- Inspect activation/configuration changes for tests and dependencies they newly make active.
- Discover the project's test, format, and lint tooling from the repository itself.

**Don't**
- Treat the pre-Gate-1 and completed-issue full-suite runs as duplicates of each other.
- Run the full suite after every commit by default.
- Reach for isolation verification merely because an issue has multiple commits.
- Assume a project's test/format/lint commands without discovering them from the repository.
- Land an activation commit before the code and tests it activates can stand behind it.
