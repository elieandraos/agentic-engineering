# Maintaining technical documentation

This file owns the "Update an existing document" workflow triggered from `SKILL.md`: locating the
target, reconciling it with verified current reality, and finishing with a review pass. It
preserves the identity and technical meaning a document already carries. `rules/doc-style.md` owns
the writing guidance; `rules/review.md` owns the evaluation.

Maintenance fails in two opposite directions: leaving stale documentation in place for the sake of
continuity, and rewriting or restructuring the document beyond what the verified change actually
requires. Both are defects this file exists to prevent.

## Locate the target

Locate and inspect the actual document before updating it. Discover it from what's supplied: a
stated file path, an existing cross-reference from another document or from project
documentation, or a repository search by subject. Ask the user when identification remains
ambiguous — don't guess, and don't assume the document's content from memory.

- **Genuinely missing** — no document exists for the subject. This is a new-document request;
  follow `rules/authoring.md`.
- **Unreachable** — the document is known but can't currently be read or written (for example, a
  path outside the accessible workspace, or no write access). Explain the limitation concretely
  and ask the user how to proceed. Never report a document as updated when it wasn't.

## The maintenance unit: technical claims

Treat every statement the document makes as a **technical claim** — for example a center of
gravity, a responsibility or ownership, a boundary, an invariant or guarantee, a lifecycle or
state, an integration or extension seam, a procedure step, a configuration value, a cost
assumption, a business rule or exception, a decision and its trade-off, a limitation or deferred
item, or a concrete evidence reference. A claim, not the section, table, or paragraph carrying it,
is the unit of maintenance — the same claim routinely repeats across several of those.

## Reconcile before editing

Compare the document's claims against current evidence, approved decisions, configuration, runtime
evidence, relevant tests and cost assumptions. Reuse evidence that is already sufficient and
current, per `SKILL.md`.

Classify what you find:

1. **No documentation event** — neither a claim nor its evidence reference changed. Leave the
   document alone; not every commit is a documentation event.
2. **A narrow update** — one fact or evidence reference is now wrong, with no material design or
   operational shift behind it. Correct it in place.
3. **A connected technical change** — several claims or structural elements depend on each
   other and must move together (see "Follow the claim graph," below).
4. **Unresolved authority, intent, or a material decision** — stop. Return it to the user rather
   than deciding it during maintenance. Maintenance updates a document to match an
   already-resolved reality; it does not resolve product or architecture questions itself. A
   decision that requires fresh investigation or an architecture decision with the user routes
   through `lab-it`.

## Preserve continuity without freezing the document

Preserve every unaffected claim, explanation, section, and presentation choice. Don't rewrite
nearby prose merely because the file is already open, and don't restructure for taste, tidiness, or
conformity with another document's shape.

Continuity is not the same as freezing the document's center of gravity, ownership, boundaries, or
reasoning in place. If verified reality actually changed one of those, the document must change
with it: a strengthened guarantee updates exactly where it already lives, but a moved
responsibility, a new center of gravity, or a shifted boundary requires restructuring that section,
a connected set of sections, or — rarely — the whole document, in proportion to what actually
changed. A prior documentation defect — a claim that was always misplaced or wrong, independent of
any new implementation change — can also justify moving or restructuring content.

**Preserve the document's identity by default.** Keep the same file path, including a path outside
`docs/` — `docs/` is only the default location for a new document. Relocate only when the user
explicitly authorizes it. Preserve front matter, the title, and other metadata the update doesn't
touch, while allowing the changes the update actually requires.

## Follow the claim graph, not the triggering issue

An issue, PR, or request names the trigger, not the documentation scope. Once a changed claim is
identified, find every place that depends on or repeats it, wherever the document actually has
them: the opening summary or summary facts, headings, prose, diagrams, tables, counts, source
references, decisions and trade-offs, limitations or deferred work, and closing material. None of
these is mandatory in every document — update whichever the document actually uses to state the
claim, forming the smallest complete connected set, not just the section the issue happened to
name.

For connected documentation, follow the affected claim graph across authoritative references,
primary summaries and dependent documents. Update the owning document first, then reconcile only
the materially affected summaries, links and claims. Do not duplicate detail or silently relocate
files. When the user limits an update to some of the connected documents, report which documents
still carry the superseded claim rather than presenting them as current.

## Implementation-only changes

Not every implementation change requires a document edit — but treat the document as unaffected
only when both hold:

- the technical understanding or procedure the document communicates remains accurate;
- every concrete evidence reference, path, symbol, configuration key, count, or other durable fact
  the document prints remains valid.

A refactor with no architectural effect can still invalidate a printed reference. When it does, the
document needs an edit even though the underlying design itself didn't move.

## Keep deferred work current

Wherever the document records limitations or deferred work, it must describe current reality:

- remove an item once it's completed — don't strike it through or leave it as a note;
- update whatever claim the completed work actually changed, using the rules above;
- don't retain completed work as release notes.

No section is required for this, and none should be added to hold a single completed-item note. A
document with no materially useful limitations doesn't need one.

## Current technical reality, not changelog

Describe the system as it works now, or the approved design explicitly as such — write it the way
you'd write it if documenting the system for the first time today. Don't narrate commits, pull
requests, or before/after implementation history.

This doesn't erase rationale. When a past decision or a rejected alternative materially explains
why the current design is shaped the way it is, preserve that reasoning as durable technical
content, not chronology. Omit only the parts that serve solely as release history.

## Sequence

1. Locate the target and gather current evidence — reuse what's sufficient and current; route
   through `lab-it` when it's missing or stale.
2. State the changed claim or evidence reference in one sentence.
3. Classify it (see "Reconcile before editing") and determine the complete connected scope.
4. Stop for unresolved authority or a material decision — route it to the user, or to `lab-it` when
   it requires fresh investigation or an architecture decision.
5. Update only the affected claim graph, preserving unaffected narrative and the document's
   identity.
6. Remove stale deferred-work claims and update whatever they affected.
7. Reread the edit as current technical documentation, not release notes.
8. Save the document at its existing path.
9. Run `rules/review.md` against the whole updated document, with emphasis on the changed claims
   and whatever depends on them, and confirm the changes don't contradict untouched material. Correct
   the material findings it reports and verify the corrections. Stop and return to the user when a
   correction requires an unresolved decision.
10. Report which documents changed, any material findings you corrected, and any remaining
    divergence or open finding with its reason.
