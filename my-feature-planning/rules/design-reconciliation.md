# Design Reconciliation

Design artifacts drift from what actually ships. That's normal — real product decisions get made
mid-implementation and never get folded back into the design source. This rule's job is to
**surface** that drift before it silently repeats, not to resolve it in either direction on its own.

## When this pass runs

Run this pass whenever an issue has any frontend/UI scope — any issue introducing or changing a
user-facing surface, not only ones focused on wiring an existing design. Backend-only or
infrastructure-only work with no user-facing surface skips this file entirely.

Once frontend/UI is in scope, running the pass is not discretionary. But discovering that no
relevant design artifact exists is a valid, ordinary outcome of running it — it does not by itself
block planning. See "No relevant artifact" below.

## Locating design artifacts

This rule does not assume a directory, filename, format, design provider or tool, tracked-vs-
untracked status, or refresh mechanism, and it does not depend on any private memory entry.
Discover the consuming project's actual design-artifact sources, and how to access them, from
project-provided documentation, configuration, or reliable context already established in
conversation.

If the location or access method is unclear, ask the user — but only when resolving it is
materially necessary to produce a correct, developer-ready issue. Don't invent an artifact, and
don't invent a project convention for where one would live.

## Authority model

Reconciliation compares sources; it doesn't decide who outranks whom on its own — that's fixed in
advance:

- An approved `plan.md` locked decision (`rules/plan-md-input.md`) governs the intended target for
  anything it covers. A design artifact or the current implementation can't silently override it.
- Current code is authoritative for current-state facts, and for discovering shipped product
  conventions elsewhere in the app.
- A design artifact is evidence of intended UI — not automatically the newest or winning source
  just because it exists.
- Shipping alone doesn't prove a deliberate, confirmed product decision. Something can ship without
  anyone having decided it should stay that way.
- When chronology or authority between two sources is genuinely unclear, and they express genuinely
  different product choices, the user decides — don't guess which one is "more current."
- A mismatch against an approved locked decision is recorded as drift against the approved target,
  not treated as grounds to re-litigate the decision. Only the user can amend a locked decision, and
  only explicitly.

Whether a derived constraint from `plan.md` has gone stale against current code is
`rules/plan-md-input.md`'s procedure, not this rule's — don't duplicate it here; apply this rule's
outcomes to whatever that check leaves in place.

## The procedure

Before drafting canonical issue definitions whose scope depends on a UI choice:

1. Identify any approved UI/product decisions that apply (from `plan.md` or otherwise established).
2. Locate and inspect the relevant available design artifacts, if any exist.
3. Inspect the affected shipped surface, and the closest established product precedent, where
   either exists — neither is guaranteed to exist for genuinely new UI.
4. Compare what the sources actually say.
5. Classify the result using the outcomes below, and record the resulting scope, constraint, drift
   note, or open product decision before drafting the affected issue(s).

## Outcomes

- **No material disagreement.** Sources agree, or only one carries real information. Proceed.
- **Superseded artifact.** The artifact is clearly superseded by a later confirmed product decision
  (an approved plan, a decision the user has confirmed, or comparably solid evidence — not shipping
  by itself). Use the newer decision. Note the drift only if it affects implementation
  understanding.
- **Genuine unresolved disagreement.** Sources express different product choices and neither
  clearly supersedes the other. This is the only outcome that blocks drafting the affected issue(s)
  — see "Presenting a blocking disagreement" below.
- **Genuinely new UI.** A design artifact describes UI with no shipped equivalent. Follow the
  design, subject to normal planning rules; there's nothing to reconcile.
- **No relevant artifact.** Nothing usable was found or applies. Use approved decisions and
  established product conventions when they give enough direction. Ask the user only when a
  material product choice remains unresolved and the issue can't become developer-ready without it.
  Never invent layout or interaction requirements to fill the gap.

## Presenting a blocking disagreement

When the outcome is a genuine unresolved disagreement, compile a short, decision-ready list before
drafting the affected issue(s):

- What each source indicates.
- Why neither clearly supersedes the other.
- The specific product decision required.
- An optional recommendation, with reasoning.

Don't silently pick a side. Don't draft the affected canonical issue definitions until the user
decides. Issues that don't depend on the open decision aren't blocked by it.

## What this rule owns

Comparing sources, classifying drift, and surfacing unresolved product choices. It does not create
or amend `plan.md`, update design artifacts, prescribe where a project stores design files, choose
implementation/component details, implement the UI, or duplicate issue drafting or review mechanics
owned elsewhere in this skill. Its output becomes input to canonical issue scope.
