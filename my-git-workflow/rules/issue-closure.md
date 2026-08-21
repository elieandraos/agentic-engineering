# Issue Closure

Closure is opt-in, and it comes after commits exist — never before, and never assumed.

## Ask first

Once a committed, approved issue exists, ask whether the human wants to close it now. Don't close
automatically just because the commits landed, and don't ask before the commits exist. If the
answer is no or not yet, leave the issue open and don't ask again unprompted — the human will bring
it up when they're ready.

## If approved, the closure recipe

The closure recipe was directly observed in three issues — #288, #287, and #120 — and should stay
that consistent. #289 reached the commit stage — implemented, committed, and verified — but had not
yet gone through issue closure at the time this skill was extracted, so it's evidence for the
implementation and commit-boundary decisions elsewhere in this skill (`rules/commit-boundaries.md`,
`rules/verification.md`), not for this closure recipe specifically.

> Only cite an issue as evidence for a workflow rule once that part of its lifecycle has actually
> occurred.

The four-part sequence:

1. **Check off completed Tasks.** Fetch the current body (`gh issue view N --json body -q .body`),
   flip every `- [ ]` that's actually done to `- [x]`. Only the ones actually done — if a task was
   intentionally deferred to a later issue or trimmed from scope, leave it unchecked and say so in
   the closing comment rather than silently checking it to make the issue look complete.
2. **Add a concise closing comment.** What was implemented, the verification results (test counts,
   full-suite pass/skip/fail), and the actual commit SHAs. Include anything discovered during
   implementation or review that's worth preserving on the record — a scope discrepancy the plan
   got wrong (#287's 3-vs-13 route groups), a naming/architecture decision made during review
   (#289's policy-ability rename and allowlist trim). This is the durable trail for anyone reading
   the issue later; keep it a summary, not a transcript of the conversation.
3. **Persist and close.** `gh issue edit N --body-file` for the checked boxes, `gh issue comment N
   --body-file` for the closing comment, then `gh issue close N`.
4. **Post-mutation validation.** Never report closure as done on the strength of `gh issue close`'s
   exit code alone — re-fetch and check the actual result, the same discipline
   `my-feature-planning` applies to every GitHub mutation it makes:
   - `gh issue view N --json number,title,state,closed` — confirm `state: CLOSED` and
     `closed: true`.
   - Re-fetch the body and confirm the checked-box count matches the number of tasks actually
     completed.
   - Confirm the closing comment is present (fetch the last comment, don't assume the `gh issue
     comment` call succeeded just because it didn't error).

Report the validated result compactly — issue number, title, state, checked-task count, and a link
— not a re-print of the full body or comment.

## What this step does not do

It does not decide whether the issue *should* be closed (that's the "ask first" step, always a
human call). It does not touch any issue this skill didn't just help commit work for. It does not
create or reopen issues — that's `my-feature-planning`'s territory, not this skill's.
