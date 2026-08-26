# my-feature-planning

A "turn the idea into buildable work" skill. It takes a feature or an approved `plan.md`, works out
the scope and dependencies, drafts the issues, reviews them, and creates them only after approval.

It plans the work. It does not implement it — that's a different skill's job, picked up after an
issue is approved.

## What it does

```
feature / approved plan
  → understand what needs to be done
  → classify the work
  → work out scope
  → reconcile UI/design when needed
  → draft canonical issues
  → review them
  → propose milestone/labels
  → get approval
  → create GitHub issues
```

The skill owns this workflow end to end. You don't need to hand it a giant prompt spelling out
every step — "plan this feature" or "plan the approved X from plan.md" is enough. It knows how to
classify the work, pick the right questions, and draft accordingly.

## Two ways to start

### 1. Start from a normal feature conversation

Use this when there's no approved `plan.md` yet — most features start here.

```
"Let's build X"
  → classify it
  → work out scope
  → ask the important unanswered questions
  → draft issues
```

### 2. Start from an approved `plan.md`

Use this when `my-architecture-laboratory` has already investigated the problem and the target
architecture has been approved.

```
approved plan.md
  → treat architecture + locked decisions as canonical
  → resolve remaining implementation-level details
  → scope the work
  → draft issues
```

The boundary matters:

> `plan.md` settles architecture and product decisions.
> `my-feature-planning` turns that settled plan into executable project work.

It must not re-litigate a decision the plan already locked.

## A third way to start: Discovered work

The two starts above both assume the scope is already known — a feature idea, or an
approved architecture. Not every issue starts that way. Sometimes the first thing
that exists is a symptom: a blank page during manual smoke testing, a stale
reference found in code review, an unexpected toast in production.

```
finding (implementation / code review / manual smoke testing / production)
  → don't fix it, don't file it yet
  → separate what's actually known from what's assumed
  → reproduce it when practical
  → investigate enough to find the real problem behind the symptom
  → work out blast radius, and whether it's actually a defect
  → check whether it contradicts an approved decision, or ask if it needs one
  → THEN draft a canonical issue, through the same pipeline as any other issue
```

This is `rules/discovered-work.md`. Investigation depth is proportional to the
evidence, not automatically exhaustive — an obvious stale reference gets a quick
completeness check, while a symptom that turns out to hide a silent security-state
bug gets traced until the real mechanism is understood. A compact checkpoint
(confirmed / ruled out / unknown / next step / enough-to-write-an-honest-issue)
surfaces whenever the investigation itself signals it — a hypothesis just got
falsified, the trail just crossed into framework/vendor/browser territory, a second
architectural layer just got implicated, the remaining unknown looks like it needs
tooling this pass doesn't have, or there's a natural moment to check whether enough
is already known — instead of a fixed time or token budget. Investigation stops once
the remaining unknown would take disproportionate effort or tooling this pass
doesn't have — the issue then carries that unknown honestly rather than pretending
it's resolved.

A validated discovered finding is also sequenced by its own scope, not forced into
the backend-then-frontend batching that's the default for planned features (see
"Sequencing" below) — a frontend-only fix ships without waiting on a backend batch
that doesn't exist for it, and vice versa. That batching convention only applies
when the finding turns out to be genuinely entangled with a larger planned
capability's own dependency graph.

This path only decides *whether there's a real, well-scoped issue* and writes it —
it doesn't fix code, and once the issue is approved, the implementation skills take
over exactly as they do for planned work.

## What a good issue looks like

An issue is not a code blueprint.

It should answer:

- What problem are we solving?
- Why are we doing it?
- What outcome should exist when we're done?
- What important constraints must remain true?
- What is in scope?
- What is explicitly out of scope?

It does that through four parts:

### Context
Why the issue exists and what outcome it's aiming for.

### Tasks
Where to work — the major pieces to implement.

### Acceptance Criteria
What must be true when the issue is complete.

### Tests
Only when it adds value to call out specific behaviors that need proof.

The simple way to remember it: tasks tell the developer where to work; acceptance criteria tell
the developer what success looks like.

Issues should never turn into:

- a copy of the architecture investigation;
- a list of every method to write;
- a step-by-step coding tutorial;
- an exact test recipe.

Once an issue is approved, the implementation skills take over — they own how the code actually
gets written.

## How it thinks about scope

Not every feature is shaped the same way, and the skill doesn't force one shape onto all of them.
It asks first: "what kind of feature is this?" — then loads only the questions that actually apply.

Four broad shapes:

- **New resource / CRUD** — a brand-new thing with its own lifecycle.
- **Cross-cutting capability** — infrastructure or behavior that spans several existing things,
  with no single owner.
- **Extension of something that already exists** — a slice bolted onto an existing capability.
- **Architectural / refactor work** — restructuring without new user-facing behavior.

Carriers and Notifications show up as examples in the rule files — they illustrate what each shape
looked like in this project, they don't define the categories.

One thing worth calling out: shared infrastructure isn't automatically its own issue. Whether it
splits out or gets bundled with the smallest meaningful pilot consumer is decided by the actual
dependency graph and whether the infrastructure can be proven correct without a real consumer —
not by a rule of thumb that infrastructure always deserves its own ticket.

## Design reconciliation

When frontend/UI is in scope, there's an extra check before drafting: compare the design file
against what the app actually ships.

- Design is simply older, and the shipped app is the clearer, newer decision → go with the shipped
  app.
- Design and shipped app genuinely disagree, and neither one clearly wins → stop and ask.
- The UI is genuinely new and the design is the only source → follow the design.
- An approved `plan.md` decision always beats a stale mockup.

The detailed rules for running this check live in the rule files — this is just the shape of it.

## Sequencing

Once issues are drafted, they're batched: backend/TDD work lands before frontend/UI work, for both
resource-shaped and cross-cutting features. This is the default shape, not a fixed issue count — the
feature's actual dependency graph decides how many issues exist in each batch.

In the project this skill was first built in, this held across two different feature shapes — a
resource with its own CRUD spine, and a cross-cutting capability with none — even though the batch
composition looked different each time. The full rule lives in `rules/sequencing.md`.

A discovered-work finding (see "A third way to start" above) isn't automatically bound by this batch
template — it sequences by its own scope, which may be backend-only, frontend-only, or genuinely
entangled with a larger feature's dependency graph that's already being batched this way.

## Milestones and labels

```
query current state
  → check project conventions
  → propose milestone/labels
  → show what already exists vs. what is new
  → get approval
  → create
```

The important distinction: project conventions help *shape* a proposal — they don't authorize a
GitHub change by themselves. The skill never silently creates a new milestone or label just because
the convention makes the answer obvious; it still has to be proposed and approved.

The exact naming pattern and label colors are this project's conventions, not part of the core
method — they live in the detailed rule files.

A milestone description is optional, proposed only when the milestone's intent, boundaries,
exclusions, governing principles, or completion criteria aren't already obvious from its title and
issue set — not written by default. When one exists, it's treated as that milestone's contract, the
same way an approved `plan.md` decision or an issue's Acceptance Criteria are treated as contracts
at their own level. A persistent catch-all milestone (this project's `Backlog`) is a different thing
from a delivery/phase milestone and doesn't get delivery-completion framing — see `rules/issue-conventions.md`.

This skill doesn't decide when a milestone closes, or treat "all currently-known issues closed" as
"done." A delivery/phase milestone does have a completion lifecycle now — it just belongs entirely
to `my-git-workflow`, running after a release built from the milestone ships and is validated. This
skill's responsibility ends at defining the milestone and its issue set; see `rules/issue-conventions.md`
for why that boundary matters and `my-git-workflow`'s `rules/milestone-completion.md` for the gate
itself.

## Canonical issues

The main safeguard in this workflow: there's one canonical definition per proposed issue. The full
draft, the compact manifest, any revisions, and the final GitHub issue body are all generated from
those canonical definitions — never copied from an earlier rendered preview.

That matters because a rendered preview is a one-way output, not a source of truth. Treating it as
one is exactly what causes duplicated sections, misplaced acceptance criteria, and other drift when
a large issue set goes through a few rounds of revision.

## Review and approval

Two main review checkpoints:

1. **Content review** — the user sees the full issue bodies and can fix scope, context, tasks,
   acceptance criteria, whatever needs it.
2. **Final approval** — the user sees a compact manifest plus the milestone/label proposal.

Nothing gets created on GitHub until the user has explicitly approved *both* the issue set and the
proposed GitHub metadata. Before that approval, structural checks confirm the canonical issue set
itself is sound, and a separate check confirms the compact manifest the user is approving actually
matches it — a render is a generated artifact, not automatically trustworthy just because it came
from the canonical definitions. After creation (and after any later edit to an already-created issue),
the skill re-fetches what GitHub actually has and checks it against the canonical definition — a `gh`
command succeeding is never treated as proof by itself.

## What the skill owns

**`my-feature-planning` owns:**
- feature classification
- scope discovery
- discovered-work investigation and triage (validating a finding before it becomes an issue)
- design reconciliation
- issue drafting
- dependency planning
- review
- milestone/label proposals
- GitHub issue creation after approval

**It does NOT own:**
- application implementation
- fixing a defect it discovers (that's implementation's job, once an issue exists)
- framework-specific coding conventions
- test implementation details
- commit structure/messages

Those belong to the implementation skills.

```
my-architecture-laboratory → approved architecture / plan.md
  → my-feature-planning
  → GitHub issues
  → implementation skills
```

## What a good result looks like

- Explains why the feature exists.
- Gives each issue one coherent outcome.
- Makes dependencies obvious.
- Keeps implementation detail at the right level.
- Preserves the architectural/product guarantees that actually matter.
- Lets a developer pick up an issue without having been in the planning conversation.
- Doesn't ask the developer to rediscover decisions buried in old chat history.

## What it should avoid

- Forcing every feature into a fixed number of issues.
- Treating old project examples as universal rules.
- Inventing future extension requirements nobody asked for.
- Writing code blueprints into issues.
- Silently deciding product questions.
- Silently creating GitHub metadata.
- Re-litigating an approved `plan.md`.
- Mixing planning with implementation.

## Is this portable?

The planning method — classify, scope, reconcile, draft, review, sequence, create — isn't specific
to any one project's stack and could apply to any codebase.

GitHub itself is a different kind of dependency from the rest, and it's worth naming separately from
stack conventions: it's the methodology's actual planning substrate, not an abstraction layered on
top of it. Milestones, labels, `#N` auto-linking, and the issue lifecycle this skill's issue and
review rules are built around are GitHub product concepts, not just a CLI choice — a team using a
different tracker would need to adapt those rules, not just point `gh` at a different host.

`SKILL.md` and this file now describe the methodology, its safeguards, and its boundaries in
project-agnostic terms; where an example is drawn from the project this skill was first built in,
it's labeled as that (the issue title convention itself — `<Area/Capability>: <action or outcome>` —
is written to be portable rather than tied to any one project's naming dialect; see
`rules/issue-conventions.md`).

That doesn't make the whole skill generic yet. The rule files underneath still carry some of that
project's conventions baked in more deeply than a labeled example:

- `rules/resource-feature-checklist.md` interleaves the generic resource-planning track structure
  (A–G) with that project's specific Laravel/Vue class names, file paths, and UI conventions closely
  enough that separating the two is a rewrite, not an extraction — the heaviest remaining item.
- `rules/design-reconciliation.md` and `rules/issue-conventions.md` each name a specific personal
  memory (`project-design-files`; `feedback_github_issues` and `feedback_github_label_colors`) that
  the rule depends on to know where design files live or how to format an issue — real dependencies
  on that project's own memory store, not yet generalized or made optional.

Refining those is a rule-file-level pass — each `rules/*.md` file receiving its own authoring pass —
not something these two top-level files can resolve on their own.

> The planning method is reusable. GitHub is a real dependency the method is built on. The specific
> stack conventions and personal-memory dependencies inside some rule files still belong to the
> project they were extracted from.

If this skill is ever made public, those rule-file conventions should move into a project-specific
adapter rather than staying baked into the core methodology.

## Relationship to my-architecture-laboratory

```
my-architecture-laboratory → understand / decide / document / synthesize plan.md
my-feature-planning     → classify / scope / reconcile / draft / review / create issues
implementation skills   → write code / tests / commits
```

`my-feature-planning` trusts an approved architecture guide or `plan.md` handoff as given — it
doesn't redo architecture work another skill has already settled.

---

`my-feature-planning` turns a settled feature idea into clear, reviewable, dependency-safe work
without making the developer rediscover the architecture or the planning conversation.
