---
name: my-git-workflow
description: "Delivery-stage skill in the Agentic Engineering pipeline (my-architecture-laboratory understands reality → my-feature-planning turns understanding into approved work → my-git-workflow turns approved work into verified delivery). Takes one already-approved GitHub issue that my-feature-planning has drafted, reviewed, and created, and moves it through implementation, human review, a semantic commit-plan proposal, verified commits, optional issue closure, and dependency-set recalculation. Once a PR carrying that work merges, runs a separate release phase (discover the project's actual release policy, classify, draft, get explicit approval, publish, validate). Once that release is validated, runs a separate milestone-completion phase. Trigger on requests shaped like 'implement issue {xxx}', 'commit issue {xxx}', 'close issue {xxx}', 'release {version}', or 'check whether milestone {name} is ready to close'. Composes with whatever stack-specific implementation and testing skills the project uses, loaded alongside it — this skill owns the Git/GitHub workflow machinery (commits, closure, release, milestone completion), never the application code, tests, or framework conventions. Does not decide what work should exist and does not draft or create issues or milestones (that's my-feature-planning) — this skill never starts before a work item is already approved."
---

# My Git Workflow

### Role

`my-git-workflow` is the delivery stage of the Agentic Engineering pipeline:

`my-architecture-laboratory → my-feature-planning → my-git-workflow`

It starts from approved work produced by `my-feature-planning` and carries that work through the
Git/GitHub delivery lifecycle.

### Input

The input is an already-approved GitHub issue produced by the planning stage
(`my-feature-planning`). This is an intentional pipeline boundary: this skill never decides what
work should exist, and never starts earlier than an already-approved item.

### What it owns

- Implementation and commit-plan review gates.
- Semantic commit planning and construction.
- Verification.
- Issue closure.
- Dependency-ready recalculation.
- Release.
- Post-release milestone completion.

### What it does not own

- Deciding what work should exist.
- Defining or scoping milestones.
- Application or framework implementation.
- Stack-specific conventions.
- PR creation and merge strategy, where not yet covered.
- Deployment automation.

### Composition

- Git and GitHub are intentional core substrate for this methodology, not an abstraction to be
  swapped out.
- This skill composes with whatever implementation, testing, and tooling skills the consuming
  project's stack requires, loaded alongside it.
- Stack-specific knowledge does not belong in this skill.

### Activation

Trigger on requests shaped like:

- `implement issue {xxx}`
- `commit issue {xxx}`
- `close issue {xxx}`
- `what's next in milestone {name}`
- `release {version}`
- `is milestone {name} ready to close`

A short prompt like these invokes the full workflow, including its review gates — never a shortcut
past them.

### Detailed rules

> Detailed workflow and decision rules live in `rules/*.md`.
