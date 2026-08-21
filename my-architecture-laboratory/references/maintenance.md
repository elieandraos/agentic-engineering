# Maintaining an architecture guide

This is not a guide to editing documents. It's the methodology developed while keeping the
Documents and Tags guides accurate as their implementations kept moving — how to change what a
guide says without changing the story it's telling. `references/review.md` judges whether a
document communicates its architecture; this file governs how you're allowed to touch a document
that already does, so a maintenance pass doesn't quietly undo that.

## When to consult this file

Whenever the user asks to update, refresh, or maintain an existing architecture guide — this is
required reading for Phase 4, not optional background. Not during Phase 1, 2, or 3: this file is
about *changing* an established narrative, and there's no established narrative yet on a first
pass.

## Philosophy

An architecture guide is a long-lived engineering document, not a snapshot of a pull request. An
implementation change should update the guide's *guarantees* without changing its *narrative* —
the same central idea, the same section names, the same reasoning, just accurate again. The goal
of a maintenance pass is continuity. If you find yourself rewriting a section, stop and ask
whether the architecture actually changed, or just one fact within it.

## Preserve the architecture

- Do not rewrite a section whose architectural meaning hasn't changed, even if you're already
  editing the section next to it. Touching prose you don't need to touch is how narrative drifts
  across a document's lifetime without anyone deciding it should.
- If an implementation change strengthens an existing guarantee — a retry count went up, a
  checksum check got added, a policy got stricter — update that guarantee exactly where it
  already lives (the same table row, the same sentence). Don't give it a new section just because
  it's new information; it's a fact changing, not a new architectural idea arriving.
- Avoid moving content between sections unless the architecture itself changed. A fact migrating
  from "Security" to "Runtime architecture" should only happen because what it describes actually
  moved responsibility — never as a tidiness pass.

## Update only affected guarantees

Before editing anything, identify which architectural guarantees actually changed. Then touch
only the sections that state those guarantees, and nothing else.

Maintenance scope is determined by the architectural guarantees themselves, not by the sections a
GitHub issue, PR description, or implementation request happens to mention. An issue write-up
naturally focuses on the one symptom that was visible — it is not a map of which sections teach
the underlying guarantee, and it is not a ceiling on the pass. Do not constrain the maintenance
pass to sections implied by the issue description. Once a changed guarantee is identified, update
every section that teaches it, not just the section where the bug was reported or the fix landed.
The same guarantee routinely surfaces in more than one place — a contract, a shared building
block, an integration section, a runtime description, a security row, a testing classification, a
decision's trade-off, the summary — and every section that states it needs to move together.
Follow the architecture, not the issue.

Common shapes this takes:

- a new runtime guarantee (something now happens atomically, idempotently, or in a defined order
  that didn't before) → update the runtime ownership table or the relevant flow description
- a strengthened security control → update the one row in the security table, add an `src-ref`
  if there wasn't one
- an additional lifecycle state → update the state diagram and the state table, and check whether
  a decision row needs a new trade-off
- an improved integrity guarantee (a new verification step, a new invariant) → update the
  guarantee's own sentence, not the surrounding narrative
- an updated testing boundary (a test moved from integration-specific to shared-capability, or a
  previously-deferred branch is now covered) → update the testing section's classification
- a completed improvement → see *Improvements are living*, below

If a change doesn't map to one of these — if it's purely internal refactoring with no observable
guarantee shift — the guide may not need an edit at all. Not every commit is a documentation
event.

## Improvements are living

Focused Improvements must always describe genuine, current future work — never a historical
record of what's already shipped. When an implementation change completes one of those items:

- remove it from Focused Improvements entirely; don't strike it through or leave it as a note
- update whatever section the completed work actually strengthens, using the same "update only
  affected guarantees" rule above
- never leave completed work sitting in the improvements list — a stale "still to do" item that's
  actually done is a worse failure than an outdated guarantee, because it actively misleads the
  next engineer about what's safe to build on

## Avoid release notes

A maintenance pass is not a changelog entry. Don't describe the commit, the pull request, or the
chronological sequence of what happened ("as of PR #142, retries now..."). Don't narrate the
history of the implementation. Instead, update the architecture as though the new guarantee had
always existed — write it the way you'd have written it if you were documenting this system for
the first time today. The guide describes the system that exists now, not the story of how it got
there; that story belongs in commit messages and PR descriptions, not here.

## Preserve architectural continuity

The document should read as one coherent guide when you're done, not as a sequence of edits from
different points in time. A reader should not be able to tell which sections were written months
apart. Every maintenance pass is a refinement of one architectural story, not an addendum to it —
if a change can't be woven into the existing narrative without seams showing, that's a sign the
architecture itself changed enough to warrant reconsidering the section's structure (still scoped
to that section — see *Preserve the architecture*, above — not an excuse to restructure the whole
guide).

## Before you redeploy

Run through this in order:

1. What architectural guarantee actually changed? State it in one sentence before touching the
   document.
2. Which section(s) state that guarantee today? Touch only those.
3. Did this complete anything listed in Focused Improvements? Remove it if so.
4. Read the edited section(s) as if encountering them fresh — does anything now read like a
   changelog entry, or reference "before" and "after"? Rewrite it as a present-tense statement of
   how the system works.
5. Redeploy through the `Artifact` tool with the same `url` and the same `favicon`, then run
   `references/review.md` against the sections you touched.