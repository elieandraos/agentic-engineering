# Establishing the Review

## When to consult this file

Always, at the start of every `review-it` invocation, before running `rules/checklist.md`.

## Principle

> A review is only as trustworthy as the target, baseline, and scope it was actually checked
> against. Establish all three before inspecting a single line, and report plainly whichever one
> couldn't be established rather than substituting a guess.

## Establish the review target

Determine whether the review covers a worktree (uncommitted or locally committed changes), a
branch (its full diff against a base), or a PR (its actual current diff on GitHub, not a stale
local checkout).

Discover the target from what's actually available: a target named explicitly in the request (a
branch name, a PR number or URL, "review my current changes"), the repository's current git state
when nothing else is named, or a PR already linked to the work under discussion. Ask the human only
when the target is genuinely ambiguous — more than one plausible candidate, or no working-tree
changes and nothing named — and the choice can't be resolved from a single unambiguous current
state.

## Establish the comparison baseline, where one applies

A worktree or branch review needs a baseline to diff against:

- Uncommitted changes compare against `HEAD`.
- A branch's full diff compares against its merge-base with the project's trunk branch, unless the
  request names a narrower comparison. Default to the merge-base when nothing narrower is stated,
  since that's what would actually land.
- A PR's baseline is the PR's own declared base branch, discovered from GitHub — never assumed from
  local branch naming.

Not every review needs a baseline — inspecting one already-isolated commit or a single file in
isolation does not. Treat this as conditional, not universal.

## Establish the intended scope

Discover intended scope from whatever is actually available: a linked issue or milestone
description, a PR description, an approved `plan.md`, explicit scope stated directly in the
request, or `Refs #N` trailers and commit messages already present in the diff.

`review-it` does not require a `plan-it`-authored issue, an approved `plan.md`, or a prior
`implement-it` session to run. A standalone worktree, branch, or PR with no issue at all is a
valid, ordinary target. When no scope evidence exists, state that plainly as a limitation in the
final report — never infer an intended scope from the diff's own shape and then treat that
inference as if it had been approved. A diff is evidence of what changed, never proof of what was
authorized.

## Establish available evidence

Gather what's actually reachable before starting: the diff itself, a linked issue or PR body,
`plan.md` or an architecture guide, CI results already produced by someone else, applicable project
instructions, and an applicable stack companion if one is installed. State plainly, in the final
report, which of these existed and which didn't — missing evidence is a limitation to report, not a
gap to silently fill by inference.

## Ask only when it materially matters

Ask the human only when an unresolved ambiguity would materially change what gets reviewed or the
standard it's checked against — for example, two equally plausible target branches, or a request
that could mean either "review my uncommitted changes" or "review the whole feature branch." Do not
ask about an ambiguity that wouldn't change the review's outcome; note it as a limitation instead
and proceed with the most defensible reading.

## Discover applicable conventions — portable and stack-aware

Discover applicable project instructions, repository conventions, and — when one is installed and
actually applicable to the reviewed change — a stack companion's rules, using the same
discoverable-tooling model `implement-it/rules/verification.md` already applies to test and lint
tooling: read from the repository's own instructions, configuration, and established usage, never
assumed in advance.

An optional stack companion sharpens the "Architectural fit," "Project/stack convention
compliance," and "Correctness and edge cases" checks when it applies to the reviewed stack. It is
never a prerequisite for running this review. Run the full checklist with no stack companion
installed; skip only the specific sub-checks a missing companion would have informed, and say so in
the report rather than silently treating the review as complete on that point.

## Entry points reuse this procedure identically

Whether `review-it` is invoked standalone, by `implement-it` before Gate 1, or by `implement-it`
during an authorized delivery correction, this procedure runs the same way every time. A call from
`implement-it` typically supplies richer scope evidence (the approved issue, the completed diff);
a standalone call may supply less. Neither situation changes the procedure — only how much evidence
turns out to be available, which the final report states either way.
