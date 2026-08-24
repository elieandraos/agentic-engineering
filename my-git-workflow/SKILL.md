---
name: my-git-workflow
description: "Delivery-stage skill in the Agentic Engineering pipeline (my-architecture-laboratory understands reality → my-feature-planning turns understanding into approved work → my-git-workflow turns approved work into verified delivery). Takes one already-approved GitHub issue that my-feature-planning has drafted, reviewed, and created, and moves it through implementation, human review, a semantic commit-plan proposal, verified commits, optional issue closure, and dependency-set recalculation. Once a PR carrying that work merges, runs a separate release phase (discover the project's actual release policy, classify, draft, get explicit approval, publish, validate). Once that release is validated, runs a separate milestone-completion phase. Trigger on requests shaped like 'implement issue {xxx}', 'commit issue {xxx}', 'close issue {xxx}', 'release {version}', or 'check whether milestone {name} is ready to close'. Composes with whatever stack-specific implementation and testing skills the project uses, loaded alongside it — this skill owns the Git/GitHub workflow machinery (commits, closure, release, milestone completion), never the application code, tests, or framework conventions. Does not decide what work should exist and does not draft or create issues or milestones (that's my-feature-planning) — this skill never starts before a work item is already approved."
---

# My Git Workflow

This is the delivery stage of the Agentic Engineering pipeline. It starts from approved work
produced by `my-feature-planning` and owns the Git/GitHub workflow from implementation through
verified delivery and the related release/milestone lifecycle.

## Pipeline role

```
my-architecture-laboratory   → understand and reconstruct reality
my-feature-planning          → turn that understanding into approved work
my-git-workflow              → turn approved work into verified delivery      (this skill)
```

## Input

- One already-approved GitHub issue that `my-feature-planning` has drafted, reviewed, and created.
- This is an intentional pipeline boundary, not incidental project coupling: this skill never
  decides what work should exist, and never starts earlier than an already-approved item.

## What this skill owns

- Picking up one dependency-ready approved issue at a time.
- Two pre-merge human review gates — implementation, then the commit plan.
- Proposing and building semantic commit boundaries from the actual diff.
- Verification scope (targeted vs. full-suite vs. isolation-proving a split) and commit ordering
  around feature-activation risk.
- The issue-closure recipe and its post-mutation validation.
- Recalculating and reporting the milestone's dependency-ready set.
- After a PR merges: release-policy discovery, classification, outcome-level drafting, the release
  approval gate, publishing, and post-publication validation.
- After release validation passes: the milestone-completion gate and its closure mutation.

## What this skill does not own

- Deciding what work should exist, or drafting/creating issues or milestones (`my-feature-planning`).
- The application code, tests, or framework-specific conventions (the stack-specific implementation
  skills).
- Product/architecture decisions, any review-gate outcome, or final sequencing among ready issues
  (the human, always).
- PR creation, merge strategy, or deployment automation (not designed yet — see "Left for later
  versions").

## Composition and Git/GitHub

This skill composes with whatever implementation, testing, and tooling skills match the consuming
project's actual stack, loaded alongside it. It owns the workflow machinery, never the code, tests,
or framework conventions themselves.

Git and GitHub are not incidental — they're the substrate this stage of the pipeline is written
against. Issues, milestones, commits, and releases are load-bearing concepts here, not a detail
abstracted behind a generic platform adapter. What's reusable across projects is the methodology
(review gates, commit-boundary reasoning, verification discipline, the release/milestone lifecycle)
applied to *this* substrate, discovering each project's own concrete policy where this skill says
"the project's own."

> Issues describe outcomes. Commits describe coherent, verified implementation steps.

## A minimal human prompt is enough — it invokes the workflow, not a shortcut past it

A prompt like "implement issue {xxx}" or "commit this" or "close issue {xxx}" is enough — the human
doesn't need to restate the review gates, verification scope, or closure recipe each time. But
brevity invokes the workflow; it never bypasses its gates:

- "implement issue {xxx}" still stops at Gate 1 for implementation review.
- "commit this" starts the commit-boundary proposal; it is not itself approval of that plan — Gate
  2 still requires an explicit yes before any commit is written.
- "close issue {xxx}" still runs the full closure recipe, not a shortcut straight to `gh issue
  close`.

## Quick Reference

1. **Commit boundaries** → `rules/commit-boundaries.md` — one issue does not equal one commit; the
   diff decides the split, never file count or issue size.
2. **Verification** → `rules/verification.md` — targeted per commit, one full suite at Gate 1 and
   one at the completed-issue boundary; isolation verification when a split itself needs proof;
   ordering commits so activation can't retroactively break a landed one.
3. **Review gates** → `rules/review-gates.md` — two separate human approvals (implementation, then
   commit plan) and the conditions that always warrant a stop.
4. **Issue closure** → `rules/issue-closure.md` — ask first; check off Tasks, closing comment,
   close, then post-mutation validation.
5. **Sequencing** → `rules/sequencing.md` — recompute the dependency-ready set after every closure,
   report the graph, recommend, leave the choice to the human.
6. **Release** → `rules/release.md` — discover the project's real release policy; classify by theme,
   never by size; draft at release altitude; explicit approval of version/tag/title/body; publish
   and re-validate.
7. **Milestone completion** → `rules/milestone-completion.md` — after release validation, not at
   issue closure or PR merge; close only when delivery/phase, release published-and-validated, and
   zero open issues all hold at once; Backlog is exempt.

## Lifecycle

```
approved issue
  → implement scope → verify → STOP (Gate 1: implementation review)
  → inspect diff → propose commit plan → STOP (Gate 2: commit-plan review)
  → build commits → full-suite at issue boundary → ask to close → (yes) close + validate
  → recompute dependency-ready set, recommend, stop
                                    ⋮
PR merges (may bundle several issues)
  → discover release policy → classify → draft → STOP (release approval) → publish → validate
                                    ⋮
release validated
  → check gate: delivery/phase + release published-and-validated + zero open issues, all fresh
  → STOP (closure approval) → close → validate
```

Each arrow is one line here; the reasoning behind it lives in the rule file from the Quick Reference
above — this diagram is the map, not the manual. See `README.md`'s "Real example of usage" for what
this looked like on a real pass through the loop.

## Left for later versions

Not designed yet, because no real evidence exists to extract from:

- PR creation and description conventions.
- Merge strategy (merge commit vs. squash vs. rebase-and-merge).
- Deployment triggers.
- A branch-naming convention beyond taking whatever branch is already checked out — ask rather than
  assume "one branch per issue" or "one branch per milestone" until there's a repeated convention to
  extract.

When real evidence for any of these shows up, extract the rule from what actually happened, the same
way `rules/release.md` was — not from what seemed reasonable in advance.
