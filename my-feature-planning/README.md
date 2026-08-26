# my-feature-planning

A "turn the idea into buildable work" skill. It takes a feature request or an approved `plan.md`
section, works out the scope and dependencies, drafts reviewed GitHub issues, and creates them only
after approval. It plans the work — it does not implement it, that's a different skill's job, picked
up after an issue is approved.

## Three starting points, two work origins

A feature conversation and an approved `plan.md` are the two starting points for Planned work; an
unexpected finding is the starting point for Discovered work.

**From a feature conversation.** Most features start here: "let's build X" → classify → work out
scope → ask the important unanswered questions → draft issues.

**From an approved `plan.md`.** When `my-architecture-laboratory` has already investigated the
problem and the target architecture has been approved, this skill treats that architecture and its
locked decisions as canonical instead of re-deriving them from conversation, and resolves only the
remaining implementation-level details. It must not re-litigate a decision the plan already locked.

**From a Discovered finding.** Not every issue starts from known scope — sometimes the first thing
that exists is a symptom: a blank page during manual testing, a stale reference found in review, an
unexpected error in production. This skill investigates before drafting — separates what's actually
known from what's assumed, reproduces it when practical, and works out the real problem, the blast
radius, and whether it's actually a defect — proportional to the evidence, not automatically
exhaustive. Only a validated finding enters the same canonical-issue pipeline, and the same review
bar, as any other issue; this path decides *whether* there's a real issue and writes it, it doesn't
fix code. Full detail: `rules/discovered-work.md`.

## How it scopes a feature

It classifies first — new resource/CRUD, cross-cutting capability, extension of something that
already exists, or architectural/refactor work — then loads only the questions that shape actually
needs answered. Shared infrastructure isn't automatically its own issue; that's decided by the actual
dependency graph, not a rule of thumb.

When frontend/UI is in scope, it also reconciles the project's available design artifacts against
what's actually shipped and any locked `plan.md` decision — going with the shipped app when a design
is simply stale, following the design when the UI is genuinely new, and stopping to ask when the two
genuinely disagree and neither clearly wins. Full detail: `rules/feature-classification.md`, the
shape-specific checklist, and `rules/design-reconciliation.md`.

## What a good issue looks like

An issue is not a code blueprint. It answers what problem is being solved, why, what outcome should
exist, what constraints must remain true, and what's in and out of scope — through Context and Tasks,
with Acceptance Criteria and Tests added only where they earn their place. It must stand on its own:
understandable even if `plan.md`, the planning conversation, and this skill's own prior output all
disappeared tomorrow.

There's one canonical definition per proposed issue. Every rendered draft, the compact manifest, any
revision, and the final GitHub body are generated fresh from that definition — never copied from an
earlier rendered preview. That's what keeps a large issue set from drifting (duplicated sections,
misplaced acceptance criteria) as it goes through a few rounds of revision.

## Sequencing

Backend/TDD work is batched before frontend/UI work, for both resource-shaped and cross-cutting
features — the default shape, not a fixed issue count. The feature's actual dependency graph decides
how many issues exist in each batch. A Discovered-work finding isn't automatically bound by this
template; it sequences by its own scope unless it's genuinely entangled with a feature already being
batched this way. Full detail: `rules/sequencing.md`.

## Review and approval

Two checkpoints gate GitHub: a **content review** of the full issue set, where scope, context, tasks,
and acceptance criteria get fixed; and a **final approval** of the compact manifest plus the
milestone/label proposal. Nothing — no milestone, no label, no issue — gets created until both are
approved. Every issue body is checked once more immediately before it touches GitHub, and every
mutation is re-fetched from GitHub and validated again afterward, at creation and on any later edit —
a `gh` command succeeding is never treated as proof by itself. Full detail: `rules/review.md`.

## What it owns

Feature classification, scope discovery, discovered-work investigation and triage, design
reconciliation, issue drafting, dependency planning, review, milestone/label proposals, and GitHub
issue creation after approval.

**It does not own** application implementation, fixing a defect it discovers, framework-specific
coding conventions, test implementation details, commit structure/messages, or deciding when a
milestone closes — those belong to the consuming project's implementation skills and, for milestone
completion, to `my-git-workflow`.

```
my-architecture-laboratory → approved architecture / plan.md
  → my-feature-planning     → GitHub issues
  → implementation skills
```

## GitHub is the planning substrate

This skill plans work as GitHub milestones, labels, and issues intentionally, not as a stand-in for
some other tracker. Portability, for this skill, means being reusable across GitHub-based software
projects with different application stacks and project conventions — not across issue trackers.

Application-stack conventions, milestone-naming patterns, and label palettes are inputs the consuming
project supplies to the methodology, not part of the portable method itself. Where a rule file still
has a specific project's conventions folded into its methodology more deeply than a clearly-labeled
example, that's being addressed as each rule file receives its own authoring pass.

---

`my-feature-planning` turns a settled feature idea into clear, reviewable, dependency-safe work
without making the developer rediscover the architecture or the planning conversation.
