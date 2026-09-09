# Activation Ordering

## When this applies

`rules/commit-boundaries.md`'s derivation procedure orders commits by structural dependency (its
step 6); `rules/verification.md`'s default commit-building loop hands off here whenever that
ordering also touches a change to configuration, feature flags, environment-conditioned behavior,
or another runtime activation gate. Consult this file only once one of those changes is actually
part of the commits being built — ordinary dependency ordering with no such gate needs nothing
beyond `rules/commit-boundaries.md`'s own step 6.

## Ordering commits to keep intermediate states valid

Watch for any change to configuration, feature flags, environment-conditioned behavior, or another
runtime activation gate — flipping one of these can retroactively change what's under test. A test
conditioned on that gate is silent until the moment it flips, and the instant it does, every test
that was quietly inactive starts running immediately, against whatever code currently exists.

Before committing a step that activates a gate:

1. Identify what behavior and tests become active as a result.
2. Inspect existing tests too, not only ones the current issue adds — an unrelated pre-existing test
   can be gated on the same condition.
3. Verify every dependency those newly active paths require is already present in an earlier
   commit.
4. If it isn't, reorder the commits so it is.

The underlying principle:

> Activation comes after the dependencies required by what it activates. A commit must not read as
> green merely because a gate hid the assertions that would have failed once activated.

For example: commit A introduces supporting code while a feature stays disabled; commit B wires the
behavior to that support, still inactive; commit C flips the feature on. C must land after A and B —
enabling the feature activates tests and code paths that depend on both, and landing C first would
make it green only because the gate was still hiding what it activates.

### Relationship to dependency ordering

`rules/commit-boundaries.md`'s derivation procedure already orders commits by structural dependency
(its step 6); this section layers activation-safety ordering on top of that same sequence. No real
work has yet produced a case where the two orderings actually disagree — this is recorded here as an
observed non-conflict, not a claim that they can never conflict. No precedence rule is defined for
if they do. Should that situation actually arise, it's a genuine unresolved decision for
`rules/review-gates.md`'s "when to stop and ask" to surface, not a default to invent here in advance.

## Relationship to isolation verification

An activation step whose correctness depends on earlier commits already being in place is one of
the examples `rules/verification.md`'s "Isolation verification: a deliberate escalation, not the
default" names for when an intermediate committed state's own correctness needs proving — see that
section for the full escalation criteria, and `rules/isolation-verification.md` for the technique
itself. Reordering the commits correctly under this rule does not by itself supply that proof; when
the activation step's own intermediate state also needs proving, both apply together.
