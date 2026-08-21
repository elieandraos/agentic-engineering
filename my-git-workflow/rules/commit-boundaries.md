# Commit Boundaries

> Issues describe outcomes. Commits describe coherent, verified implementation steps.

An issue and a commit answer different questions. An issue answers "what should exist when we're
done, and why." A commit answers "what is the smallest coherent, independently-true step that got
us there." Nothing forces those two counts to match, and in the evidence this skill is built from,
they usually don't.

## Do not assume one issue equals one commit

Four issues, four different shapes, decided by the actual diff each time — never by a rule of
thumb applied in advance:

| Issue | Shape | Commits |
|---|---|---|
| #288 — provision org + first Owner via Artisan command | One coherent new capability (Action + command + notification widen + tests) | **1** |
| #287 — remove public registration | One coherent subtractive decision, applied everywhere it needed to apply | **1** |
| #120 — 2FA backend (TDD) | One issue, three layered implementation steps (persistence → HTTP wiring → activation) | **3** |
| #289 — org-level 2FA requirement + enforcement | One cross-cutting issue, four dependency-ordered steps (persistence → policy → settings page → enforcement) | **4** |

Neither shape is the default. A single-file issue can be one commit; a five-file issue can be
four. The diff decides — see "See the diff before deciding" below.

## File count is not commit count

#287 touched 21 files across app code, routes (11 separate route files), a migration, and tests —
and landed as **one** commit, because it was one decision (public registration is gone, and its
dead `verified` middleware goes with it) applied consistently everywhere that decision reached.
Splitting it by directory or file type (routes in one commit, app code in another, tests in a
third) would have produced three commits that each left the app in a half-migrated state — worse
history, not better.

Conversely, #120 landed as three commits touching as few as two files each. Small diffs don't
default to one commit either, if the diff actually contains more than one implementation decision
— see #120's shape below.

## What makes a boundary "coherent"

A semantic commit is one implementation decision you could summarize in a single sentence of *why*
— not a bucket defined by folder, file type, or how the diff happened to be typed out over the
course of the conversation. Ask, for each candidate grouping: if this commit existed alone on top
of what came before it, does it represent one real, describable decision, and does the app still
work?

Concretely, from the evidence:

- **#120's three commits** were: "add the 2FA data layer" / "wire the Security settings page to
  read it" / "turn the Fortify feature on and prove the whole pipeline end to end." Each is one
  sentence. Each is a real decision.
- **#289's four commits** were: "add the requirement column" / "add the Owner-only policy" / "add
  the toggle page" / "enforce it via middleware." Same shape — one sentence, one decision, per
  commit.

## Commit messages explain the decision, not the diff

> Commit messages explain the decision, not the diff.

Prefer a concise title and, when useful, a short body describing the outcome and important
guarantees or boundaries. Don't turn the commit message into a file-by-file implementation summary
— the detailed implementation already lives in the diff and the issue; the message's job is to
carry the "one sentence of *why*" from "What makes a boundary 'coherent'" above into the permanent
record, not to re-narrate what changed.

## Reference the issue, never close it, from the commit message

> Every commit that implements a GitHub issue carries a `Refs #N` trailer — never `Closes`,
> `Fixes`, or `Resolves`.

Scope: this applies to commits produced by this skill's working loop for the dependency-ready,
approved issue currently being implemented — not to every commit made while this skill happens to
be in use. Not every commit in this workflow implements an issue: the Phase 22 history this skill
was extracted from includes a content-backlog commit with no issue behind it at all, and it
correctly carries no `Refs #N` — there's nothing to reference. When a commit isn't implementing a
tracked issue, omit the trailer rather than inventing a reference. This rule is about this skill's
own commits, not a general policy for every commit in the repository.

Add the reference as its own trailer/footer, after the body — not folded into the semantic title or
body, which stay focused on the decision (see "Commit messages explain the decision, not the diff"
above). The trailer ties that decision back to the issue that motivated it; it isn't part of the
decision itself.

Never use GitHub's auto-closing keywords. Issue closure in this workflow is an explicit,
human-approved step that happens after commits exist and verification passes
(`rules/issue-closure.md`) — a `Closes #N` trailer would let `git push` close the issue on its own,
silently skipping that approval gate. `Refs #N` links the commit to the issue without closing
anything.

For a multi-commit issue, every commit carries the same `Refs #N` — the issue doesn't change
mid-split, only the commit boundaries do.

```
Add operator-run 2FA reset for a locked-out sole Owner

organizations:reset-owner-two-factor identifies the target by email,
requires explicit confirmation, and reuses ResetTwoFactorAuthenticationAction
directly — which now accepts a nullable actor for operator-triggered resets.

Refs #291
```

## See the diff before deciding

Never decide commit boundaries before the implementation exists and has been reviewed. Commit
structure is discovered by inspecting the *actual* `git status` / `git diff --stat` / per-file
diffs after the work is done and approved — not planned speculatively while writing code, and not
copied from how a previous issue happened to split. Planning commit boundaries in advance and then
forcing the code to fit them produces exactly the file-type/directory split this skill exists to
avoid.

This is also why the commit plan is its own review gate, separate from implementation review — see
`rules/review-gates.md`.

## For TDD work, keep proving tests with their step

When a commit introduces behavior that can be directly proven, its own tests travel with it in the
same commit — never split "the code" into one commit and "the tests that prove it" into another.

Not every commit has tests of its own, and that's fine. #120's first two commits (persistence,
then Security-page wiring) shipped with no new tests, because neither was independently observable
yet — the persistence layer had no consumer, and the controller change read a feature flag that
was still off. Their proof was negative: the full suite stayed exactly as green as it was before
either commit landed (see `rules/verification.md`). The third commit, which turned the feature on,
carried the tests that proved the whole activated pipeline — including retroactively proving the
first two commits' work, once there was finally something to observe.

#289's policy commit is the cleaner case: `OrganizationPolicy` is fully testable in isolation via
`$user->can('update', Organization::class)`, with no HTTP layer needed — so its test landed in the
same commit as the policy, immediately.

## Review corrections fold into their semantic commit — no fixup commits

A correction discovered during review does not automatically become its own commit. Where it lands
depends on whether anything has been committed yet:

- **Nothing committed yet** — the correction is simply part of whichever semantic commit it
  belongs to. #289's two review-driven refinements (renaming a bespoke policy ability to match the
  codebase's `update` convention; trimming a middleware allowlist to the one route that's actually
  reachable) landed straight inside the policy commit and the middleware commit respectively — no
  separate "fix review comments" commit ever existed, because none of the work had been committed
  when the corrections were made.
- **Something already committed, correction needed before push** — don't bolt a fixup commit on
  top. Rebuild history so the correction lands inside the commit it actually belongs to. #120 was
  first implemented and committed as a single commit; when asked to split it into semantic steps
  *after the fact*, the rewrite was done safely because nothing had been pushed yet:
  `git reset --soft HEAD~1` (undoes the commit, keeps every change staged), then selective
  `git add` + `git commit` per semantic group, verifying each one in isolation before moving to the
  next (`rules/verification.md`). The result reads as if it had been built that way from the start
  — there is no trace in the history of the fact that it was originally one commit.

Never preserve every conversational step as its own commit "for the record." The history should
read as a sequence of decisions, not a transcript.

## Each semantic commit leaves a coherent, non-broken state

The standing rule underneath everything above:

> Every semantic commit should leave a coherent, non-broken implementation state that does not
> depend on a later commit to become structurally valid.

That's a narrower bar than "safe to deploy from" — some coherent commits are intentionally inert
until a later commit activates them, and that's fine. #120's first two commits (persistence, then
Security-page wiring) are exactly that: each is structurally complete and correct on its own terms,
but neither does anything observable until the third commit turns the feature flag on. A migration
with no consumer is coherent (it does nothing yet, and does it correctly). A controller that reads
a feature flag that's still off is coherent (it's dead code today, live code tomorrow). A commit
that references a class, route, or column that doesn't exist until the *next* commit is not
coherent, no matter how small it is — that's the actual line: structural self-sufficiency, not
user-visible behavior.
