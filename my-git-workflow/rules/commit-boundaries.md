# Commit Boundaries

> Issues describe outcomes. Commits describe coherent, verified implementation steps.

An issue answers "what should exist when we're done, and why." A commit answers "what is the
smallest coherent, independently-true step that got us there." Nothing forces those two counts to
match.

## Do not choose commit count in advance

Neither "one commit per issue" nor "many small commits" is the default. Commit count is not
determined by issue size, file count, how many directories or file types are touched, or how a
previous issue happened to split — it is discovered from the actual, finished, reviewed diff, every
time (see "How to derive commit boundaries" below).

A large diff can be one commit, if it's one decision applied consistently everywhere it reaches. A
small diff can be several commits, if it actually contains several decisions. File count in
particular is not commit count: splitting a single decision by directory or file type — routes in
one commit, app code in another, tests in a third — produces commits that each leave the app in a
half-migrated state. That's worse history, not better, even though it looks more organized.

### What this repository's evidence shows

Four issues, four different shapes, decided by the diff each time rather than a rule of thumb:

| Issue | Shape | Commits |
|---|---|---|
| #288 — provision an org + its first Owner via a CLI command | One coherent new capability (action + command + a notification widened to match + tests) | **1** |
| #287 — remove public registration | One coherent subtractive decision, applied everywhere it reached | **1** |
| #120 — add 2FA to the backend (built TDD) | One issue, three layered implementation steps (persistence → HTTP wiring → activation) | **3** |
| #289 — add an org-level 2FA requirement + enforcement | One cross-cutting issue, four dependency-ordered steps (persistence → policy → settings UI → enforcement) | **4** |

The one-commit issues above were not small. #287 alone touched 21 files across app code, 11
separate route files, a migration, and tests, and still landed as one commit — because it was one
decision (public registration is gone, and its dead `verified` middleware goes with it), not because
it was simple.

## What makes a semantic commit

A semantic commit is one implementation decision you could summarize in a single sentence of *why*
— not a bucket defined by folder, file type, or how the diff happened to be typed out over the
course of implementation. Ask, for each candidate grouping: if this commit existed alone on top of
what came before it, does it represent one real, describable decision, and does the app still work?

"Still work" is narrower than "safe to deploy" or "user-visible":

> Every semantic commit leaves a coherent, structurally valid state that does not depend on a later
> commit to become structurally valid.

- A commit can be coherent and still be inert — dead code today, live tomorrow — as long as it's
  structurally complete and correct on its own terms. A migration with no consumer yet is coherent
  (it does nothing, and does it correctly). A change gated behind a feature flag that's still off is
  coherent (it's dead code today, live once the flag flips).
- A commit that depends on a class, route, or column that isn't defined until the *next* commit is
  **not** coherent, no matter how small it is. That's the actual line — structural
  self-sufficiency, not user-visible behavior.

### What this repository's evidence shows

#289's four commits were each one sentence, one decision: "add the requirement column" / "add the
Owner-only policy" / "add the toggle page" / "enforce it via middleware." #120 shows the inert case:
its first two commits — the 2FA data layer, then wiring the Security settings page to read it —
were each structurally complete but did nothing observable yet, since the feature flag gating them
was still off. Its third commit turned the flag on, activating both — and retroactively proving the
first two correct, once there was finally something to observe.

## How to derive commit boundaries

Never decide commit boundaries before the implementation exists and has been reviewed. Planning
boundaries speculatively while writing code — or copying how a previous, superficially similar issue
happened to split — produces exactly the file-type/directory split this rule exists to avoid.

The procedure:

1. Finish the implementation.
2. Pass implementation review (Gate 1 — `rules/review-gates.md`).
3. Inspect the actual diff (`git status`, `git diff --stat`, then per-file diffs).
4. Identify the implementation decisions the diff actually contains.
5. Group changes by decision, not by file location or type.
6. Order the groups by dependency.
7. Verify each intermediate state would be coherent, per "What makes a semantic commit" above.
8. Propose the commit plan for human review (Gate 2 — `rules/review-gates.md`) before writing a
   single commit.

This is also why the commit plan is its own review gate, separate from implementation review — see
`rules/review-gates.md`.

## Commit messages and issue references

> Commit messages explain the decision, not the diff.

Prefer a concise title and, when useful, a short body describing the outcome and important
guarantees or boundaries. Don't turn the message into a file-by-file implementation summary — the
diff and the issue already carry that detail; the message's job is to carry the one-sentence "why"
into the permanent record. History should read as a sequence of engineering decisions, not a
transcript of the development conversation.

Every commit that implements a tracked, approved issue carries a `Refs #N` trailer — never `Closes`,
`Fixes`, or `Resolves`. Issue closure in this workflow is an explicit, human-approved step that
happens after commits exist and verification passes (`rules/issue-closure.md`); an auto-closing
keyword would let `git push` close the issue on its own, silently skipping that approval. `Refs #N`
links the commit to the issue without closing anything.

- The trailer is its own line, after the body — not folded into the title or body, which stay
  focused on the decision.
- For a multi-commit issue, every commit carries the same `Refs #N`. The issue doesn't change
  mid-split; only the commit boundaries do.
- Not every commit made while this skill is in use implements a tracked issue — a commit made for an
  unrelated reason (a documentation fix, a backlog item) correctly carries no trailer. When a commit
  isn't implementing a tracked issue, omit the reference rather than inventing one.
- This is a rule about this skill's own commits for the dependency-ready, approved issue currently
  being implemented, not a general policy for every commit in the repository.

```
Add rate limiting to the password-reset endpoint

Limits reset requests to 5 per hour per account. Requests over the
limit return 429 without revealing whether the account exists.

Refs #{xxx}
```

## Tests travel with the decision

When a commit introduces behavior that's independently observable, its proving tests land in the
same commit — never split "the code" into one commit and "the tests that prove it" into another.

Not every commit needs new tests. A commit that's intentionally inert (see "What makes a semantic
commit" above) can legitimately ship with none, as long as its proof is negative: the full suite
stays exactly as green as it was before the commit landed (`rules/verification.md`). Once a later
commit activates the behavior, that commit's own tests retroactively prove the earlier, inert-looking
commits correct too. Conversely, a change that's fully testable in isolation the moment it lands —
a policy or validation rule with no HTTP layer needed, say — carries its test immediately, in the
same commit.

### What this repository's evidence shows

#120's first two commits shipped with no new tests, for exactly the reason above — neither was
independently observable until the third commit turned the feature on. #289's policy commit is the
cleaner case: the policy was fully testable in isolation via `$user->can(...)`, with no HTTP layer
needed, so its test landed in the same commit as the policy, immediately.

## Review corrections fold into their semantic commit

A correction discovered during review does not automatically become its own commit. Where it lands
depends on whether anything has been committed yet.

**Nothing committed yet.** The correction is simply part of whichever semantic commit it belongs to.
No separate "fix review comments" commit exists, because none of the work had been committed when
the correction was made.

**Something already committed, correction needed before push.** Don't bolt a fixup commit on top.
Rebuild history so the correction lands inside the commit it actually belongs to:

1. `git reset --soft HEAD~1` — undoes the commit, keeps every change staged.
2. Selectively `git add` and `git commit` per semantic group.
3. Verify each resulting commit in isolation before moving to the next (`rules/verification.md`).

The result reads as if it had been built that way from the start — there's no trace in the history
that it was originally committed differently.

Never preserve every conversational step as its own commit "for the record." The history should read
as a sequence of decisions, not a transcript.

### What this repository's evidence shows

#289's two review-driven refinements — renaming a bespoke policy ability to match the codebase's
`update` convention, and trimming a middleware allowlist to the one route that's actually reachable
— landed straight inside the policy commit and the middleware commit respectively; nothing had been
committed yet when they were made. #120 is the rebuild case: it was first implemented and committed
as a single commit, then split into its three semantic steps after the fact, safely, because nothing
had been pushed yet — `git reset --soft HEAD~1`, then selective `git add` + `git commit` per group,
verifying each in isolation before moving to the next.
