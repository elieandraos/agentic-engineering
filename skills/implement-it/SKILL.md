---
name: implement-it
description: "Implementation-stage skill in the Agentic Engineering pipeline. Takes any approved GitHub issue satisfying its entry contract — whether `plan-it` drafted it or it already existed some other way — and carries it through working-branch readiness, the implementation itself, verification, semantic commits, issue closure, and dependency-ready recalculation for the next issue. Use when implementing, committing, verifying, or closing an approved issue, checking what's next in a milestone, or performing an authorized delivery correction handed back from `ship-it`. Performs the approved implementation itself, consulting the applicable stack companion for implementation knowledge and conventions — it does not own framework-specific conventions, decide what work should exist, or handle milestone PR readiness, PR creation, or release."
---

# implement-it

## What this skill is

`implement-it` is the implementation stage of the Agentic Engineering pipeline. It starts from an
approved GitHub issue produced by `plan-it` and carries that single issue's work through verified
Git/GitHub implementation, ending at issue closure and the next-issue recommendation.

## Pipeline position

`lab-it → plan-it → implement-it → ship-it`

This skill intentionally begins only once planning has produced approved work — it never decides
what work should exist, and never starts earlier than an already-approved issue. It hands off to
`ship-it` once a milestone's dependency-ready set is genuinely empty, or when `ship-it` itself hands
back an authorized delivery correction during milestone delivery.

## What it owns

- Working-branch readiness: the Backlog/hotfix-vs-milestone-branch decision, before implementation
  starts.
- Performing the approved implementation itself.
- Applying project conventions and applicable implementation/testing/tooling skills, and loading an
  applicable custom stack companion when one is available.
- Implementation and commit-plan review gates (Gate 1 and Gate 2).
- Verification, including the regression-baseline treatment of pre-existing lint/format/static debt.
- Semantic commit planning and construction.
- Authorized push and issue closure — intentionally before the milestone's PR merges.
- Dependency-ready recalculation and the next-issue recommendation.
- The authorized fix itself for an in-flight delivery correction `ship-it` hands back (see
  "Delivery corrections" below), using this same lifecycle.

## What it does not own

- Deciding what work should exist.
- Defining or scoping milestones.
- Application or framework implementation conventions — a stack companion, when one applies, owns
  those; this skill performs the work using them.
- Milestone PR readiness, PR creation, and merge strategy.
- Investigating or explaining a delivery/CI failure before a correction is authorized (`ship-it`'s
  job) — this skill performs the correction once `ship-it` hands it back as authorized.
- Post-merge authorization, release, and post-release milestone completion.
- Deployment automation.

A custom stack companion is optional, used when available and not required for every
implementation. Technology-specific knowledge — commands, branch-naming conventions, framework
idioms — belongs entirely to that companion or to project instructions, never hardcoded here.

## Entry contract

Accept any approved issue that meets `plan-it`'s entry contract, regardless of whether `plan-it`
drafted it — what matters is that it's approved, not who authored it. For a single named issue,
complete only that issue's authorized lifecycle (implementation through closure and the next-issue
recommendation); this does not by itself authorize continuing into another issue, or into milestone
delivery. For a milestone request, manage progress issue by issue, per "Milestone progression"
below.

## Milestone progression

After each issue closes, recompute the dependency-ready set (`rules/sequencing.md`) and recommend
the next issue, explaining the choice when several are ready. A recommendation is not authorization
to continue — wait for the human's selection before implementing another issue. When the ready set
is empty because every open issue remains blocked, report the blockers; only a genuinely empty
milestone (zero open issues) hands off to `ship-it`'s milestone PR-readiness assessment.

## Delivery corrections

When `ship-it` investigates a CI failure on an open milestone PR and determines a correction is
within approved scope (`ship-it/rules/milestone-completion.md`'s "CI failure on an open milestone
PR"), it hands the fix to this skill. Perform that correction through this same lifecycle — Gate 1
and Gate 2 as applicable, verification, commit construction, and authorized push — whether or not
the original issue is still open. This route stays available without requiring an open issue to
exist; it does not require reopening a closed issue, and it is separate from genuinely new scope,
which still goes through `plan-it`'s discovered-work intake. Once the correction is verified and
pushed, `ship-it` resumes the delivery workflow.

## Composition

- Git and GitHub are intentional core substrate for this methodology, not an abstraction to be
  swapped out.
- This skill composes with whatever implementation, testing, and tooling skills the consuming
  project's stack requires, loaded alongside it.
- Stack-specific knowledge does not belong in this skill.

## Activation

Trigger on requests shaped like:

- `implement issue {xxx}`
- `commit issue {xxx}`
- `close issue {xxx}`
- `what's next in milestone {name}`
- an authorized delivery correction handed back from `ship-it`

## Rules

- `review-gates.md` — the two pre-merge human approval gates (implementation review, then
  commit-plan review) and the conditions that always warrant a stop; consult once implementation is
  ready to report, and again once a commit plan is ready to propose.
- `commit-boundaries.md` — how to turn an approved diff into semantic commits: boundary reasoning,
  message content, the `Refs #N` trailer, and safely folding in review corrections; consult while
  inspecting the diff and building the commit plan, after Gate 1.
- `verification.md` — verification scope: the narrowest reliable scope per commit across tests,
  formatting, linting, and static analysis, the two distinct full-suite moments, the stronger
  isolation technique for proving a split, and ordering commits around feature-activation risk;
  consult while implementing and while building/ordering commits.
- `issue-closure.md` — whether and how to close an issue: asking first, the closing recipe, and
  post-mutation validation; consult after the completed-issue full-suite pass, once commits exist.
  Closure is intentional before a milestone's PR merges.
- `sequencing.md` — branch readiness before starting an issue (Backlog/hotfix on the trunk branch vs.
  a shared milestone branch, inspected/recommended/created only with human approval), and, after a
  validated closure, recomputing the milestone's dependency-ready set and reporting/recommending the
  next issue — or handing off to `ship-it/rules/milestone-completion.md` when the milestone is
  genuinely empty.

> Detailed operational behavior lives in `rules/*.md`.
