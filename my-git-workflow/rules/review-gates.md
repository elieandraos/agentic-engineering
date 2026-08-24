# Review Gates

Two human approvals gate the pre-merge side of this workflow, not one. Never collapse them, and
never proceed past either one without an explicit yes. (The release phase that starts after a PR
merges has its own analogous approval gate, over the proposed version/tag target/title/body —
see `rules/release.md` step 4 — rather than being folded into Gate 1 or Gate 2 below.)

## Gate 1 — implementation review

After implementing an issue's scope and running the verification appropriate to it
(`rules/verification.md`), stop. Report what changed and how it was verified — files touched, a
short description of the approach, the test and formatting-check results (whatever those tools are
for this project — see `rules/verification.md`) — and wait. Do not start thinking about commit
structure yet; that's a separate step that only starts after this gate opens.

If implementation surfaces a genuine unknown — not a style preference, an actual decision the human
hasn't made — stop and ask before finishing the implementation, rather than guessing and presenting
the guess at this gate. See "When to stop" below.

## Gate 2 — commit-plan review

Only after Gate 1 is approved: inspect the completed diff (`rules/commit-boundaries.md`), propose a
semantic commit plan, and show it before writing a single commit. A commit plan is:

- The proposed grouping — which files, in which commit.
- The order, and *why* that order (dependency order, or activation order — see
  `rules/verification.md`'s ordering note).
- Which tests travel with which commit, and which commits are intentionally test-free and why.
- Draft commit messages, or at minimum the one-sentence "why" each commit represents — plus the
  `Refs #N` trailer each of these issue-implementing commits carries (`rules/commit-boundaries.md`).

Get explicit approval of *this plan* before creating any commit. Approval of the implementation at
Gate 1 is not approval of a commit structure — #289's actual sequence was implementation approved →
two separate architectural questions raised and resolved → diff inspected → plan proposed → plan
approved → commits built. Skipping straight from "the code looks good" to committing skips a real
decision point: the same diff can be split several defensible ways, and the human should see the
split before it becomes permanent history.

If the human requests changes to the plan itself (different grouping, different order, merge two
commits, split one further), revise the plan and show it again — don't start committing against a
partially-approved plan.

## When to stop and ask, at either gate

Preserve an explicit human stop whenever:

- **A product or architecture decision is missing.** Don't invent one and present it as a fact
  during implementation review.
- **Implementation reveals a contradiction with approved architecture.** #287's discovery that
  `verified` middleware actually existed in 13 route groups across 8 files the original plan never
  named — not the 3 it expected — was exactly this: the plan's own investigation was wrong about
  the codebase's current state, discovered mid-implementation. It was surfaced and the human chose
  the resolution (remove it everywhere) before implementation continued.
- **Multiple valid sequencing choices exist**, whether that's implementation order or which
  dependency-ready issue to pick up next (`rules/sequencing.md`). Don't silently pick one.
- **The proposed commit decomposition is ambiguous** — more than one defensible way to draw the
  boundaries, with no clearly-better answer. #289 is the evidence here in the other direction:
  after the plan was proposed and approved, a later review pass asked two independent architecture
  questions (was a bespoke policy-ability name actually consistent with the rest of the codebase;
  was a defensive-looking middleware allowlist entry actually reachable) — both were investigated
  with evidence (reading every existing policy; resolving real route middleware with
  `gatherMiddleware()`) and reported as findings with a recommendation, *not* silently applied,
  before the human said to apply them.

A stop is a report plus a question, not a wall of options with no recommendation — investigate
enough to have a position, state it, and let the human decide.
