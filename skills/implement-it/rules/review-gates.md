# Review Gates

## Principle

> Two human approvals gate everything before a merge — not one — and a genuine unresolved decision
> found along the way gets an explicit human stop, never a silent guess.

```
implement + verify → Gate 1: implementation review → derive commit plan → Gate 2: commit-plan review → build commits
```

Gate 1 and Gate 2 are never collapsed into a single approval, and approval at Gate 1 does not imply
approval at Gate 2. No commit is created before Gate 2 is approved.

The post-merge release workflow has its own separate approval boundary
(`ship-it/rules/release.md`), over the proposed version, tag target, title, and body. That boundary
is not part of either gate below — a merged PR does not satisfy it.

`rules/issue-closure.md`'s push-authorization request — asking whether to push already-approved
commits to the correct remote branch, before asking to close the issue — is a similar separate
boundary, not a third review gate. It approves nothing about the implementation or the commit
structure; Gate 1 and Gate 2 below remain the only approvals of either.

## Gate 1 — implementation review

Stop here once:

- the approved issue scope has been implemented;
- the verification appropriate to it has been run (`rules/verification.md`);
- `review-it`'s pass against the completed implementation is either clean, or its findings have
  been resolved and re-verified.

Invoke `review-it` standalone against the completed working tree once the first two bullets hold,
before reporting at this gate — see "Consuming review-it's result," below. A `review-it` pass does
not grant authorization by itself; it is evidence this gate's report cites, and Gate 1's approval
mechanics — the report below, then explicit human approval — stay exactly as they were.

Report concisely:

- what changed;
- the implementation approach;
- files or surface area touched, where useful;
- verification results;
- `review-it`'s result: clean, or each finding and how it was resolved and re-verified.

Then wait for explicit human approval. Approval at this gate authorizes moving on to commit
planning — nothing more. Do not begin deriving commit structure before it.

If implementation surfaces a genuine unresolved decision before reaching this point, stop and ask
then, per "When to stop and ask" below, rather than silently choosing an answer and presenting the
choice as part of this report.

## Consuming review-it's result

Once implementation and verification are complete, invoke `review-it` the same way a standalone
caller would (`review-it/rules/scope.md`) against the completed working tree, supplying the
approved issue as the intended scope. Treat its result as follows before reporting at this gate:

- **Clean.** Report it as such and proceed to the Gate 1 report above.
- **Findings, within this skill's authorized scope to resolve.** Fix them, then request a re-review
  scoped to the affected surface — a material change invalidates `review-it`'s prior pass for that
  surface (`review-it/rules/verification.md`'s staleness rule). Report the original findings and
  their resolution, plus the re-review's clean result, at Gate 1.
- **A finding that reveals a genuine unresolved decision** — architecture, scope, or a choice with
  no clearly better answer — is not this gate's to resolve silently. Stop and ask, per "When to
  stop and ask," below, citing `review-it`'s finding as the evidence.

Never report a finding as resolved, or treat an unresolved finding as if it were clean, without an
actual fix and an actual re-review behind that claim — the same discipline `review-it` itself
applies to its own report (`review-it/rules/verification.md`).

## Gate 2 — commit-plan review

Only after Gate 1 is approved:

1. Inspect the completed diff (`rules/commit-boundaries.md`).
2. Derive the semantic commit plan.
3. Present the plan before creating any commit.

The plan must communicate:

- the proposed grouping — which files, in which commit;
- the commit order, and why (dependency order, or activation order — see `rules/verification.md`'s
  ordering note);
- which tests travel with which commit, and why any commit is intentionally test-free
  (`rules/commit-boundaries.md`);
- draft commit messages, or at minimum the one-sentence implementation decision each commit
  represents;
- the `Refs #N` trailer for any commit implementing the tracked issue (`rules/commit-boundaries.md`).

Get explicit human approval of the complete plan before writing a single commit. Approval at this
gate is what authorizes creating commits.

If the human requests a change — to grouping, ordering, splitting, merging, messages, or anything
else in the plan — revise it and present the complete, resulting plan again before committing.
Partial feedback on part of a plan is not approval of the rest of it.

## When to stop and ask

An agent may investigate and recommend. It must never convert a genuine unresolved human decision
into an implementation fact by silently choosing one. Stop, at either gate or during implementation,
whenever:

- a product or architecture decision is missing;
- implementation evidence contradicts approved architecture or assumptions;
- multiple valid sequencing choices exist and none is already authorized — whether that's
  implementation order or which dependency-ready issue to pick up next (`rules/sequencing.md`);
- the commit decomposition has multiple defensible boundaries with no clearly better answer.

Ordinary engineering choices — ones the approved scope, repository conventions, applicable skills,
and available evidence already support — are part of normal execution, not a reason to stop. Reserve
a stop for a genuinely missing decision, a contradiction, or a choice the evidence can't narrow down;
otherwise, keep executing.

A stop is a report plus a question, not a context-free question or a wall of unexplored options:

1. Investigate enough to understand the decision.
2. Report the relevant evidence.
3. State a recommendation, when the evidence supports one.
4. Ask the human to decide.

For example: implementation reveals that the approved plan assumed three affected surfaces, but the
repository actually has many more — or two commit decompositions are both structurally coherent and
neither is clearly better. Both call for a stop built the way above, not a silent pick.

## Do / Don't

**Do**
- Stop at Gate 1 once implementation, verification, and a clean-or-resolved `review-it` pass are
  complete.
- Invoke `review-it` before reporting at Gate 1, and again, scoped to the affected surface, after
  fixing any finding it raises.
- Derive the commit plan only after Gate 1 is approved.
- Show the complete commit plan before creating any commit, and get explicit approval of it.
- Investigate a genuine unknown and offer a recommendation before asking the human to decide.

**Don't**
- Collapse Gate 1 and Gate 2 into one approval.
- Treat implementation approval as commit-plan approval.
- Report a `review-it` finding as resolved without an actual fix and an actual re-review behind
  that claim.
- Treat a clean `review-it` result as authorization by itself — it is evidence Gate 1's report
  cites, not a substitute for the human's approval.
- Create a commit before Gate 2 is approved.
- Silently resolve a missing product or architecture decision.
- Ask the human to choose among unexplored options when evidence could narrow the decision first.
