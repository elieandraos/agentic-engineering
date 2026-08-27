# Sequencing

## What this rule owns

This rule owns two connected decisions: decomposing canonical scope into coherent issues, and
connecting and ordering those issues by real prerequisites. It does not decide implementation order,
which ready issue gets worked next, branch strategy, or commit structure — those belong to
`my-git-workflow`, particularly its own `rules/sequencing.md`.

## Decompose canonical scope into coherent issues

Every classification shape — new resource, cross-cutting capability, extension, or refactor —
decomposes the same way: by coherent outcome, real dependency, and independent provability. Checklist
answers supply scope, not a mechanical map to issues or batches — a question number never determines an
issue count.

Each issue should represent one coherent outcome that's independently understandable and, where
practical, independently landable and provable. Split work when:

- the parts produce independently meaningful outcomes;
- they have materially different prerequisite chains;
- one can be completed and verified without the other;
- combining them would obscure distinct acceptance criteria, risk boundaries, or ownership.

Bundle work when:

- the pieces have no meaningful or provable outcome apart from each other;
- a foundation can't be trusted without a real consumer exercising it — per
  `rules/capability-checklist.md` question 2, bundle the smallest consumer needed to prove it unless
  the foundation is independently provable on its own; never separate one just because separation
  looks architecturally tidy;
- splitting would create unused scaffolding;
- the smallest coherent deliverable necessarily crosses more than one implementation area.

Do not split mechanically — by checklist question or track, file/class/route/component/layer,
system-side vs. user-facing work, CRUD artifact, fixed issue count, or an earlier feature's structure.

Collateral work is recorded distinctly in canonical scope (`rules/capability-checklist.md` question
10) — whether it becomes its own issue is decided by this same test, not an automatic default.

## Define a real dependency

Issue B depends on issue A only when A's outcome must exist before B can be safely completed, landed,
or verified. A dependency is never a preferred order, shared subject matter, milestone membership,
drafting order, an implementation-layer convention, or a wish to keep the same context. If B can
proceed independently against a stable, already-approved contract, don't invent a dependency to
serialize it.

An external prerequisite this issue set doesn't itself own — a pending decision, a third-party
integration, another team's work — is recorded as an external constraint or blocker, never fabricated
as an internal issue.

## Build and validate the dependency graph

Each canonical issue is a node; each real prerequisite is a directed edge. The result must satisfy:

- every internal dependency points to another canonical issue;
- root issues have no prerequisites;
- the graph is acyclic, with unambiguous dependency direction;
- a dependent issue's body summarizes any relied-upon behavior a reader needs for standalone
  understanding, per `rules/issue-conventions.md`.

A cycle means the boundaries or a dependency claim are wrong — resolve it by combining inseparable work
or correcting a false dependency. Never accept a cycle, and never break one with an arbitrary ordering
decision instead of fixing what produced it.

## Preserve parallel-ready work

A dependency graph is a partial order, not one total implementation sequence. Represent readiness as
waves: roots are ready immediately, later issues become ready once their prerequisites close, and
issues in the same ready set may proceed independently unless a project-supplied constraint says
otherwise.

Present and create issues in a stable topological order so every dependency reference points backward
— an operational convenience for presentation and GitHub creation, not a claim that equally ready
issues must be implemented serially. Don't ask the user to choose between equivalent topological orders
unless the choice would materially change scope, boundaries, or risk. Choosing which ready issue to
implement next belongs to `my-git-workflow`, not this rule.

## Project-supplied delivery constraints

A consuming project may supply a documented or explicitly approved sequencing convention (e.g. "ship
behind a flag before wiring its trigger"). Treat it as project input, not methodology: identify it as
project-supplied, decide whether it creates a real prerequisite or only a preferred order, encode only
a real prerequisite as a dependency edge, and record a non-dependency preference separately rather than
fold it into the graph as a false edge. Ask the user only when applying it would materially change
scope or boundaries and its meaning is genuinely unclear.

This rule prescribes no fixed implementation-layer order of its own — vertical slices, parallel work
against a stable contract, interface-first delivery, or another approved model are all compatible with
the reasoning above.

## Planned and Discovered work use one method

Origin doesn't determine issue count or order. A validated Discovered finding
(`rules/discovered-work.md`) is decomposed from its own actual scope, using the same test as any other
work: integrate it into an existing planned capability's graph only when it shares a genuine dependency
with that capability; otherwise keep it independent — surfacing during a milestone doesn't entangle it
with the surrounding feature. A finding may resolve to one issue or reveal several; the same
decomposition test decides which.

## Dependency-safe GitHub creation

Before creation, canonical definitions may reference each other using canonical planning identifiers,
and the full set still needs to pass `rules/review.md`'s gates. Nothing is created merely because the
graph marks it ready.

After approval, create issues in the stable topological order: capture each created issue's real GitHub
number as it's created, resolve a dependent issue's canonical references to real `#N` references before
creating it, and never derive the issue set back from created issues or a rendered preview.

## Handoff

`rules/review.md` owns issue quality, dependency-quality validation, structural/rendered integrity, and
mutation validation. `SKILL.md` owns the two approval surfaces and the overall creation pipeline. Once
issues are created and approved, `my-git-workflow` owns branch readiness, choosing the next ready
issue, and recomputing the live dependency-ready set as issues close.
