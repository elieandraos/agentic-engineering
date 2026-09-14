# Agentic Engineering v3 (Working Notes)

Status: Investigation.

v3 is not a new engineering methodology. It is an investigation
into adding an execution layer above the existing methodology
while keeping the engineering methodology stable.

## Evolution

### v1 — Engineering methodology

Goal:

Extract a portable software engineering methodology from real project
work.

Problems solved:

- Engineering process lived inside long prompts.
- Decisions were hard to reuse.
- Workflow was inconsistent between projects.

Result:

Lab → Plan → Implement → Ship

The focus was how to engineer software.

### v2 — Mature ecosystem

Goal:

Mature the methodology through real projects.

Problems solved:

- Clear ownership between stages.
- Independent implementation review.
- Documentation separated from investigation.
- Stack knowledge separated from methodology.
- Publishing and consumption through skills.sh.

Result:

Engineering methodology

Lab → Plan → Implement → Review → Ship

Tooling

- document-it
- steward-it

Stack companions

Examples:

- Laravel / Inertia / Vue
- (future) Nuxt / Supabase

Methodology remains portable.

Stack knowledge remains separate.

GitHub is intentionally the only supported planning/versioning
platform. Supporting Jira, GitLab Issues, Azure Boards, etc. is
intentionally out of scope.

### v3 — Execution

Goal:

Keep the engineering methodology stable.

Improve execution.

Question:

How do we execute the same engineering methodology faster, with better
context usage and less human waiting, without reducing engineering
quality?

## What has stabilized

Three architectural layers already exist.

Engineering methodology

Lab → Plan → Implement → Review → Ship

Owns software engineering.

Tooling

document-it
steward-it

These support engineering without becoming lifecycle stages.

Knowledge

Stack companions.

Examples:

Laravel

Nuxt

Supabase

These contain implementation knowledge, not engineering methodology.

## New observation

Engineering skills currently contain two different concerns.

Engineering guidance:

- verification
- review
- commits
- issue closure
- planning

Execution guidance:

- what runs next
- scheduling
- worker coordination
- skill activation
- execution flow

The second category may belong somewhere else.

## Execution layer

A possible new architecture.

Control Room (Execution)

↓

Agentic Engineering (Engineering)

↓

Stack companions (Knowledge)

The execution layer coordinates work.

The engineering layer performs engineering.

The knowledge layer performs stack-specific implementation.

## Control Room

The current GPT Project is already acting as Control Room.

It:

- reasons
- researches
- investigates architecture
- plans
- reviews
- stewards
- prepares Claude Code handoffs
- coordinates repositories
- recommends direction

It rarely performs implementation itself.

## Responsibilities vs workers

### Responsibilities

Responsibilities are thinking lenses.

Examples:

- Principal engineer
- Architecture and domain investigator
- Planning partner
- Engineering reviewer
- Documentation reviewer
- Stack-aware specialist
- Agentic Engineering steward

These belong to Control Room.

One orchestrator changes hats as needed.

### Workers

Workers are intentionally small.

Input:

- one issue
- one repository
- one worktree
- engineering skills
- stack companions

Output:

engineering.

Nothing else.

## Dependency graph

Planning already produces a dependency graph.

Example:

```
    A
  /   \
 B     C
/ \     \
D  E     F
```

Current execution:

A → B → C → D → E → F

Possible execution:

Wave 1

A

Wave 2

B C

Wave 3

D E F

Planning already knows the graph.

Execution can eventually consume it.

## Human gates

v3 does not remove human approvals.

Current approval points include:

- plan approval
- issue creation approval
- Implement Gate 1
- Implement Gate 2
- push authorization
- issue closure confirmation
- milestone PR readiness
- PR approval
- release

Parallel execution changes when workers arrive.

It does not remove the gates.

## Context usage

The goal is not "more workers".

The goal is:

- less repeated repository discovery
- less repeated skill loading
- shared orchestration
- issue-specific context
- persistent workers where appropriate

Measure first.

Optimize second.

## Steward

Steward already reconstructs sessions, timings, context usage, findings
and evidence.

As the execution layer grows, Steward naturally becomes the place that
also evaluates orchestration decisions and their impact.

## Example skill extraction

Today:

implement-it

↓

Determine applicable skills

↓

Recommend next issue

↓

Wait

Possible future:

Control Room

↓

Determine applicable skills

↓

Spawn worker

↓

Worker already receives

- implement-it
- stack companion

implement-it no longer decides scheduling.

Another example:

Today:

implement-it recommends the next issue.

Future:

Control Room reads the dependency graph and decides which ready wave to
execute.

implement-it only engineers the assigned issue.

## Maintaining Agentic Engineering

There are now two execution domains.

Consumer repositories

Example:

useOrbit

Engineering execution.

Agentic Engineering

Methodology execution.

Typical flow:

Observe

↓

Collect evidence

↓

Update skills

↓

Update README / documentation

↓

Publish through skills.sh

↓

Refresh consuming projects

The methodology itself has its own maintenance lifecycle.

## High-level investigation plan

Unlike v1/v2, we do not yet know what the execution-layer artifact is.

Skills were the artifact for engineering methodology.

The equivalent for execution is still unknown.

Questions to answer:

- Is Control Room just project instructions?
- Is it versioned?
- Does it become its own repository?
- Are workers Claude Code subagents?
- How are worktrees managed?
- Does orchestration become installable?
- Which responsibilities stay in Control Room?
- Which execution guidance leaves the skills?

The first implementation should therefore be a Lab investigation, not
coding.

## Artifact candidates

Possible execution-layer artifacts:

- Control Room documentation
- orchestration guides
- worker definitions
- worktree conventions
- runtime prompts
- automation scripts

No decision yet.

Only implementation should decide.

## Deep architecture notes

The old "skill dossier" style artifacts may evolve.

Instead of large architecture documents, future deep dives may become a
collaboration between:

- steward-it (evidence and findings)
- document-it (durable documentation)

The exact shape is intentionally left open until more evidence exists.

## Guiding principle

Continue evolving exactly the same way Agentic Engineering itself
evolved.

Observed behavior

↓

Evidence

↓

Explicit decision

↓

Reusable rule

## Open questions

The following questions intentionally remain unanswered.

They define the investigation that should drive v3. None should be
solved speculatively. Each should be answered through real
implementation and evidence.

### Execution layer

- What is the execution-layer artifact?
- Is Control Room simply project instructions, or does it become a
  versioned component?
- Should Control Room live inside agentic-engineering, or become its
  own repository?
- Which parts of Control Room are reusable, and which remain
  project-specific?

### Workers

- Are Claude Code subagents the right worker abstraction?
- Should workers be long-lived or created per issue?
- How much context should a worker own?
- Can workers be safely reused across multiple issues?

### Worktrees

- What should the worktree lifecycle look like?
- Should worktrees be created automatically or manually approved?
- When should a worktree be reused versus destroyed?
- Which naming and cleanup conventions emerge naturally?

### Orchestration

- Which responsibilities belong exclusively to Control Room?
- Which execution responsibilities should be extracted from the
  existing skills?
- How should dependency waves be scheduled?
- How should potential file conflicts be detected before parallel
  execution?
- How are worker results collected and presented back to the human?

### Human approvals

- Which approvals remain per issue?
- Which approvals can safely become per execution wave?
- Can execution begin automatically after milestone approval, or
  should every wave require explicit authorization?

### Context

- How much repository discovery is currently repeated?
- Which context can be shared?
- Which context should always remain worker-specific?
- How should startup cost and context usage be measured?

### Steward

- Which execution metrics are worth collecting?
- Which orchestration findings become durable engineering evidence?
- When does an execution observation justify a Control Room change
  rather than a skill change?

### Skills

- Which parts of the current skills are truly engineering methodology?
- Which parts are actually execution guidance?
- What should never leave the engineering layer?
- Can skills become narrower without reducing their usefulness?

### Tooling

- Should execution-layer concepts eventually become versioned like
  skills?
- Do workers, orchestration, or worktrees deserve reusable artifacts?
- Or are they better represented as documentation, runtime
  configuration, or project instructions?

## Success criteria

How will we know v3 is successful?

Possible indicators:

- Lower wall-clock implementation time.
- Lower human waiting time.
- Lower repeated context usage.
- No reduction in engineering quality.
- No reduction in review quality.
- No increase in methodology complexity.

Control Room becomes simpler, not larger.
