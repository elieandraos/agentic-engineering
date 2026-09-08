---
name: ship-it
description: "Delivery-stage skill in the Agentic Engineering pipeline. Once `implement-it` has closed every issue in a milestone, this skill checks milestone PR readiness, prepares and creates the milestone PR through authorized human approval, investigates and explains delivery/CI failures on an open milestone PR (handing any authorized correction to `implement-it`), and — once the human confirms the PR merged and authorizes the post-merge progression — closes the milestone and prepares, publishes, and validates the release. Use when checking whether a milestone is ready for a PR, creating that PR, investigating a delivery/CI failure, checking whether a milestone is ready to close, or releasing a version. Does not implement code, decide what work should exist, or approve/merge the PR — the human retains both."
---

# ship-it

## What this skill is

`ship-it` is the delivery stage of the Agentic Engineering pipeline. It starts once
`implement-it` has closed every issue in a milestone, and carries that milestone through PR
readiness, authorized PR creation, delivery/CI-failure handling, post-merge closure, and release.

## Pipeline position

`lab-it → plan-it → implement-it → ship-it`

This skill intentionally begins only once `implement-it`'s dependency-ready recompute reports a
milestone with zero open issues remaining — it never decides what work should exist, never
implements code, and never starts earlier than a genuinely empty milestone.

## What it owns

- Milestone PR readiness, once a milestone's issues are all closed.
- Authorized milestone PR creation, once readiness passes.
- Investigating a delivery/CI failure on an open milestone PR, explaining the correction needed,
  and determining whether it stays within already-approved scope — handing any authorized
  correction to `implement-it`, and resuming delivery once it's verified and CI is green.
- The post-merge authorization gate, milestone closure, and release preparation, publication, and
  validation.

## What it does not own

- Deciding what work should exist.
- Defining or scoping milestones.
- Application or framework implementation, or any implementation itself — including a delivery
  correction, which `implement-it` performs once authorized.
- Stack-specific conventions.
- Working-branch readiness, implementation review, verification, commit construction, and issue
  closure — all `implement-it`'s.
- PR approval and merge — the human retains both.
- Deployment automation.

## Composition

- Git and GitHub are intentional core substrate for this methodology, not an abstraction to be
  swapped out.
- This skill composes with `implement-it` for any code correction its delivery-failure
  investigation authorizes.
- Stack-specific knowledge does not belong in this skill.

## Activation

Trigger on requests shaped like:

- `is milestone {name} ready for a PR`
- `create the milestone PR`
- `why is CI failing on this PR`
- `is milestone {name} ready to close`
- `release {version}`

## Rules

- `milestone-completion.md` — three milestone-level surfaces: PR readiness (all issues closed +
  confirmed manual testing + no follow-up found), consulted once `implement-it/rules/sequencing.md`
  reports a genuinely empty milestone; authorized PR creation once readiness passes; and the
  three-part closure gate plus the Backlog exemption and validated closure mutation, consulted once
  the human gives the post-merge authorization — that authorization is the approval for closure, so
  no second approval is asked, and closure is not gated on release publication itself. Also owns
  investigating and explaining a CI failure on an open milestone PR, and handing an authorized
  correction to `implement-it`.
- `release.md` — the release phase: a post-merge authorization gate right after the human confirms a
  PR merged (the same gate that also opens `milestone-completion.md`'s closure gate — neither branch
  waits on the other), then discovering the project's real release policy, understanding the release,
  drafting notes at release altitude, the content-approval gate, publishing, and post-publication
  validation; consult once a PR carrying committed work has merged. Does not apply to Backlog/hotfix
  work, which has no PR to merge.

> Detailed operational behavior lives in `rules/*.md`.
