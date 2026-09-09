# Commit Boundaries

> Issues describe outcomes. Commits describe coherent, verified implementation steps.

An issue answers "what should exist when we're done, and why." A commit answers "what is the
smallest coherent, independently-true step that got us there." Nothing forces those two counts to
match.

A semantic commit represents one coherent implementation decision. Read in order, a sequence of
semantic commits should make the implementation path understandable from the history alone: a
developer — or an agent — should be able to reconstruct what decisions were made, and how the
implementation evolved from the approved outcome, using nothing but the commit log and the diffs it
contains.

The commit boundary is what makes that possible: it decides which decision gets recorded as one
historical unit. Within that unit, the commit message explains the decision and the guarantees it
establishes, and the diff shows how the decision was actually implemented. Draw the boundary wrong —
too broad, too narrow, split along the wrong axis — and neither the message nor the diff can recover
the reasoning; the history stops teaching anything and becomes a raw file-change log.

## Do not choose commit count in advance

Neither "one commit per issue" nor "many small commits" is the default. Commit count is not
determined by issue size, file count, how many directories or file types are touched, or how a
previous change happened to split — it is discovered from the actual, finished, reviewed diff, every
time (see "How to derive commit boundaries" below).

A large diff can be one commit, if it's one decision applied consistently everywhere it reaches. A
small diff can be several commits, if it actually contains several decisions. A twenty-file change
that removes one capability everywhere it appears is one decision, and belongs in one commit; a
three-file change that happens to touch a model, a route, and a template can still be three separate
decisions, if each one is independently true without the others.

File count in particular is not commit count: splitting a single decision by directory or file
type — data-layer changes in one commit, request-handling in another, tests in a third — produces
commits that each leave the implementation in a half-migrated state. That's worse history, not
better, even though it looks more organized on the surface.

## What makes a commit coherent

A semantic commit is one implementation decision you could summarize in a single sentence of *why*
— not a bucket defined by folder, file type, or how the diff happened to be typed out over the
course of implementation.

Apply this test to every candidate commit: if it existed alone, on top of everything that came
before it, does it represent one real, describable decision — and does the resulting state hold
together on its own terms?

"Hold together on its own terms" is a narrower bar than "safe to deploy" or "user-visible":

> Every semantic commit leaves a coherent, structurally valid state that does not depend on a later
> commit to become structurally valid.

- **Coherent does not mean deployable, and it does not mean user-visible.** A commit can be coherent
  and still be inert — dead today, live once something later activates it — as long as it's
  structurally complete and correct on its own terms. A data-model change with no consumer yet is
  coherent: it does nothing, and does it correctly. A code path gated behind a flag that's still off
  is coherent: it's dead code today, live once the flag flips.
- **A commit that depends on a definition introduced only by a later commit is not coherent**, no
  matter how small it is — a reference to a class, function, route, or column that doesn't exist yet
  breaks structural self-sufficiency. That's the actual line: structural self-sufficiency, not
  user-visible behavior.

For example, a feature built in layers might land as three coherent commits: the data layer, then
the code path that reads it while still gated off, then the commit that flips the gate on. The first
two are each structurally complete and inert; the third activates both at once.

## How to derive commit boundaries

Never decide commit boundaries before the implementation exists and has been reviewed. Planning
boundaries speculatively while writing code — or copying how a previous, superficially similar change
happened to split — produces exactly the file-type/directory split this rule exists to avoid.

The procedure:

1. Finish the implementation.
2. Pass implementation review (Gate 1 — `rules/review-gates.md`).
3. Inspect the actual diff (`git status`, `git diff --stat`, then per-file diffs).
4. Identify the implementation decisions the diff actually contains.
5. Group changes by decision, not by file location or type.
6. Order the groups by dependency. `rules/verification.md`'s activation-ordering rule can require
   reordering on top of this — see that rule's "Relationship to dependency ordering" for how the two
   interact.
7. Verify each intermediate state would be coherent, per "What makes a commit coherent" above.
8. Propose the commit plan for human review (Gate 2 — `rules/review-gates.md`) before writing a
   single commit.

This is also why the commit plan is its own review gate, separate from implementation review — see
`rules/review-gates.md`.

## Commit messages and issue references

> Commit messages explain the decision, not the diff.

Prefer a concise title and, when useful, a short body describing the outcome and important
guarantees or boundaries. Don't turn the message into a file-by-file implementation summary — the
diff already shows what changed; the message's job is to preserve the reasoning behind the change —
the one-sentence "why" — in the permanent record. History should read as a sequence of engineering
decisions, not a transcript of the development conversation.

```
Add rate limiting to the password-reset endpoint

Limits reset requests to 5 per hour per account. Requests over the
limit return 429 without revealing whether the account exists.
```

Every commit that implements a tracked, approved issue also carries a `Refs #N` trailer — never
`Closes`, `Fixes`, or `Resolves`. Issue closure in this workflow is an explicit, human-approved step
that happens after commits exist and verification passes (`rules/issue-closure.md`); an auto-closing
keyword would let `git push` close the issue on its own, silently skipping that approval. `Refs #N`
links the commit to the issue without closing anything:

```
Refs #{xxx}
```

- The trailer is its own line, after the body — not folded into the title or body, which stay
  focused on the decision.
- For a multi-commit issue, every commit carries the same `Refs #N`. The issue doesn't change
  mid-split; only the commit boundaries do.
- Not every commit made while this skill is in use implements a tracked issue. When a commit isn't
  implementing one, omit the reference rather than inventing one.
- This is a rule about this skill's own commits for the dependency-ready, approved issue currently
  being implemented, not a general policy for every commit in the repository.

**Do**
- Add `Refs #N` as its own trailer, on every commit that implements the tracked issue.
- Reuse the same reference across every commit in a multi-commit issue.

**Don't**
- Use `Closes`, `Fixes`, or `Resolves`.
- Invent a reference for a commit that doesn't implement a tracked issue.
- Fold the reference into the semantic title or body.

## Tests travel with the decision

When a commit introduces behavior that's independently observable, its proving tests land in the
same commit — never split "the code" into one commit and "the tests that prove it" into another.

Not every commit needs new tests. A commit that's intentionally inert (see "What makes a commit
coherent" above) can legitimately ship with none, as long as its proof is negative: the full suite
stays exactly as green as it was before the commit landed (`rules/verification.md`). Once a later
commit makes that behavior observable, that activating commit's own tests retroactively prove the
earlier, inert-looking commits correct too. Conversely, a change that's fully testable in isolation
the moment it lands — a validation rule with no surrounding system needed to exercise it, say —
carries its test immediately, in the same commit.

## Review corrections fold into their semantic commit

A correction discovered during review does not automatically become its own commit. Where it lands
depends on whether anything has been committed yet.

**Nothing committed yet.** The correction is simply part of whichever semantic commit it belongs to.
No separate "fix review comments" commit exists, because none of the work had been committed when
the correction was made.

**Something already committed, correction needed before push.** Don't bolt a fixup commit on top.
Rebuild history so the correction lands inside the commit it actually belongs to — but only within
the unpublished range. Rewriting a commit already reachable on the remote branch is outside this
recipe entirely: that requires specific human authorization and a different path, never a silent
rewrite. This maintenance boundary applies generally, not only to this skill's own commits.

1. **Find the owning commit and confirm it's unpublished.** Identify which commit the correction
   actually belongs to — call it O. Confirm every commit from O through `HEAD` is still unpublished
   (`rules/issue-closure.md`'s "Push readiness": `git fetch origin <branch>`, then
   `git log origin/<branch>..HEAD --oneline` — every commit this reconstruction touches must appear
   in that list). If O predates the unpublished range, this recipe does not apply.
2. **Establish a scratch location for this reconstruction's own recovery artifacts, outside the
   repository working tree** — an explicit, uniquely-named directory (for example, one made with
   `mktemp -d`), never a path inside the worktree. Every file this procedure captures for its own
   bookkeeping — a correction's isolated content, a private index, an extracted or merged result —
   lives there. A recovery artifact placed inside the worktree instead is exactly the kind of
   untracked content `git stash -u` (used below) would sweep away. Preserve everything in this
   location until reconstruction is verified complete; remove it only then, never on a failure.
3. **For each path the correction touches, establish what's already staged for it, cleanly — without
   ever mutating the real index to find out.** Compare the path's current real-index content
   (`git show :<path>`) against its committed content (`git show HEAD:<path>`, or nothing for a new
   path):
   - **If they're identical** — nothing is staged for this path, so the correction and any unrelated
     content sharing the file are both still unstaged and undifferentiated. Isolate the correction
     without touching the real index at all: seed a private index copy from `HEAD`
     (`GIT_INDEX_FILE=<scratch>/index git read-tree HEAD`), then interactively stage only the
     correction's own hunk(s) into that private copy
     (`GIT_INDEX_FILE=<scratch>/index git add -p -- <path>`). If the correction and unrelated content
     can't be cleanly separated this way — presented as one hunk with no way to select one without
     the other — stop; this is a capture-time ambiguity, not something to guess past. Otherwise,
     materialize the private index's blob as the correction's known content
     (`GIT_INDEX_FILE=<scratch>/index git show :<path> > <scratch>/known--<path>`), then discard the
     private index file. The real index and working tree are untouched throughout — this is what
     keeps any already-staged content elsewhere, and its staged/unstaged arrangement, exactly as
     found; a whole-path `git restore --staged <path>` after ordinary `git add -p` cannot make this
     guarantee once other content in the same path was already staged.
   - **If they differ, and the difference is recognized as exactly the correction, nothing else** —
     the correction is already staged, cleanly. Use the real index's blob directly as the
     correction's known content: `git show :<path> > <scratch>/known--<path>`.
   - **If they differ, and the difference is recognized as unrelated content, not the correction** —
     the same real-index blob is the *unrelated* content's known state instead:
     `git show :<path> > <scratch>/known--<path>`, understood as unrelated-only rather than as the
     correction.
   Also save the path's committed content (`git show HEAD:<path> > <scratch>/head--<path>`, empty for
   a new path) and its actual current combined content (`cp <path> <scratch>/combined--<path>`).
4. **Extract whichever piece step 3 didn't already establish, and verify the split before trusting
   it.** A successful command is not, by itself, proof of correct attribution — a context-matched or
   zero-context patch can silently apply against the wrong occurrence of identical-looking content
   without ever reporting a conflict (reproduced concretely; see `scenarios.md`). Use a real
   three-way merge instead, which fails honestly on a genuine ambiguity rather than guessing:
   ```
   cp <scratch>/head--<path> <scratch>/other--<path>
   git merge-file -p <scratch>/other--<path> <scratch>/known--<path> <scratch>/combined--<path> \
     > <scratch>/extracted--<path>
   ```
   This replays whatever changed between `known` and `combined` — exactly the piece not yet known —
   onto `head`. **A nonzero exit code is a conflict: stop.** Do not resolve it by guessing which
   occurrence is which. Report the conflict; every file step 3 captured remains in the scratch
   location as recovery data, and nothing about the real repository has been touched yet. On a zero
   exit code, **verify by round-trip before trusting the result** — reconstruct the original combined
   content independently and require an exact match:
   ```
   cp <scratch>/known--<path> <scratch>/roundtrip--<path>
   git merge-file -p <scratch>/roundtrip--<path> <scratch>/head--<path> <scratch>/extracted--<path> \
     > <scratch>/roundtrip-result--<path>
   diff <scratch>/roundtrip-result--<path> <scratch>/combined--<path>
   ```
   Anything but an exact match means the split is not trusted, exactly as if the merge had
   conflicted — stop and report; do not proceed with reconstruction on an unverified split. This
   establishes both the correction's content and the unrelated-only content for this path, verified,
   whichever direction step 3 produced which.
5. **Exclude a correction-touched shared path from the general protection step below; protect
   everything else there instead.** For a path where step 4 shows no genuine unrelated content
   (unrelated-only is byte-identical to `head`), there's nothing to protect for that path at all. For
   a path with genuine unrelated content sharing the file with the correction, set its working tree
   content to `head` directly (`cp <scratch>/head--<path> <path>`, unstaging first if needed) — its
   unrelated content stays safe in the scratch location, to be reapplied in step 10 against the
   *reconstructed* content, not restored through git's stash. Git stash's own restoration depends on
   the commit its entry was taken against still matching history; a shared path's committed content
   changes by the very act of reconstruction, which can make an ordinary `git stash apply` conflict
   against content a direct merge handles cleanly (verified in practice; see `scenarios.md`).
6. **Protect whatever unrelated content remains** — every path the correction never touched, plus any
   correction-touched path step 5 didn't already clear — using the qualified procedure in
   `rules/verification.md`'s "Preserving unrelated worktree content during a Git rewrite," unmodified.
   When nothing remains (every touched path was cleared in step 5, and nothing else was ever
   uncommitted), that procedure's own clean-tree check means it protects nothing, correctly.
7. **Rewind to the owning commit's parent, keeping everything from O through `HEAD` staged**:
   `git reset --soft O~1` (or the equivalent parent reference) — not a hard-coded `HEAD~1`, which
   only reaches the single most recent commit and cannot fold a correction into an earlier one. This
   stages the combined diff of every commit from O through `HEAD` in one index; it does not, on its
   own, separate that index back into O's corrected content and whatever later commits actually
   contain.
8. **Reapply the correction directly from its captured content — never by pattern-matching a patch,
   and never by retyping it from memory.** For each path the correction touches, the working tree is,
   at this point, exactly `head` (nothing else is present, per steps 5–6): `cp <scratch>/known--<path>
   <path>` when step 3 captured the correction directly as `known`, or `cp <scratch>/extracted--<path>
   <path>` when step 4 extracted it — then `git add <path>`. This is a direct, exact, byte-for-byte
   write of already-verified content, with no patch-matching ambiguity possible.
9. **Rebuild each semantic commit from that combined index, in order, staging only that commit's own
   content each time.** A single reconstructed commit is not the same thing as "one whole file" —
   use `git restore --staged <path>` to unstage what a later commit owns, and `git add -p` (or an
   equivalent patch-level staging tool) to stage only part of a file when O's correction and a later
   commit's content share one file.
   - **Before every `git commit` in this rebuild, inspect the actual staged diff**
     (`git diff --staged`) and confirm it contains exactly the intended semantic group — no more, no
     less — rather than trusting which `git add` commands were run.
   - Commit, then verify the resulting commit in isolation before moving to the next group — every
     commit this reconstruction produces needs `rules/verification.md`'s isolation-verification
     technique, not only when it happens to be convenient. Reconstructing semantic history from an
     already-implemented diff, after the fact, is exactly the case that technique reserves the
     escalation for.
   - Repeat until every group from O through `HEAD` has its own commit again: O reconstructed with
     the correction folded in, then each subsequent original commit rebuilt intact from the
     remaining staged content — unless the correction itself changes what a later commit should
     contain.
10. **Restore the protected content.** For an ordinary path, restore from step 6's stash entry using
    that procedure's own restoration steps, once every reconstructed commit exists. **For a
    correction-touched path step 5 set aside separately, restore by the same merge technique as
    step 4 — against the path's *new*, reconstructed content, not the pre-reconstruction committed
    state.** Use whichever of step 3/4's captured files actually holds the unrelated-only
    content — `<scratch>/known--<path>` if step 3 captured the unrelated content directly, or
    `<scratch>/extracted--<path>` if step 4 extracted it (the mirror image of step 8's choice for the
    correction):
    ```
    cp <path> <scratch>/final--<path>
    git merge-file -p <scratch>/final--<path> <scratch>/head--<path> <scratch>/<unrelated-only file> \
      > <scratch>/final-result--<path>
    ```
    A nonzero exit code, or a result missing either the correction's own content or the unrelated
    content, is a restoration failure — stop, report it, and drop or discard nothing; the scratch
    location still holds every piece needed to retry or hand off. On success, write the result back
    (`cp <scratch>/final-result--<path> <path>`) and stage it only if step 3 found the unrelated
    content already staged in the real index — otherwise leave it unstaged, matching its original
    state.
11. **Confirm nothing unrelated leaked in.** After the last commit, `git status` and `git diff`
    should show exactly the restored unrelated content and nothing else outstanding from this
    reconstruction. Only once this holds, remove the scratch location from step 2 — not before, and
    never on a failure.

The result reads as if it had been built that way from the start — there's no trace in the history
that it was originally committed differently, and every intermediate commit still satisfies "What
makes a commit coherent" above.

Never preserve every conversational step as its own commit "for the record." The history should read
as a sequence of decisions, not a transcript.

## Do / Don't summary

**Do**
- Split commits by implementation decision.
- Order commits by dependency.
- Keep proving tests with the change they prove.
- Make each intermediate commit structurally coherent on its own.
- Inspect the finished, reviewed diff before proposing boundaries.

**Don't**
- Split by directory or file type.
- Force one commit per issue, or assume many commits by default.
- Create extra commits merely because a diff is large.
- Preserve review chatter as separate fixup commits.
- Reference a definition that only exists in a later commit.
