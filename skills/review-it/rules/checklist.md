# The Review Checklist

## When to consult this file

After `rules/scope.md` has established the target, baseline, intended scope, and available
evidence — while inspecting the reviewed change itself. Read this file in full: each category
decides its own applicability, so a partial read cannot support a category result.

## Philosophy

- Every category is skip-if-inapplicable, not skip-by-default. Skip a category only when the
  reviewed change genuinely doesn't touch what it checks, and say so in the report.
- Every finding traces to concrete code, configuration, or a diagnostic command's actual output —
  never a suspicion stated as fact (`rules/verification.md`).
- A finding must materially affect correctness, security, data integrity, regressions,
  architectural fit, maintainability, convention compliance, test adequacy, or scope. A personal
  style preference the project's own conventions don't already support is not a finding.
- When a finding depends on a requirement or convention — not only on the implementation evidence
  — name that source concisely: an issue, `plan.md`, a PR description, project instructions,
  configuration, or an established repository convention. Never invent a source. When none exists,
  say the finding rests on general engineering reasoning. State the source next to the finding, not
  as a mandatory requirement-by-requirement table.
- Inspect the changed code and the surrounding behavior it touches — a caller, a shared helper, or
  an adjacent code path — not only the lines the diff highlights.

### Defects that already existed

Classify a defect by its relation to the reviewed change:

- **Introduced** — the change creates it. A new occurrence of an existing defect — new code that
  repeats a known flaw — is introduced, even when older code has the same flaw. It is a finding.
- **Exposed or worsened** — the defect existed, but the change makes it reachable, more likely,
  or more consequential. It is a finding.
- **Pre-existing and blocking the approved requirements** — the change cannot satisfy its intended
  scope while this problem remains. It is a finding.
- **Unrelated pre-existing** — none of the above. Report it briefly as a separate observation. It
  is not a finding, not a review limitation, and not automatic correction scope.

## Checklist

### Requirements compliance

Compare the reviewed change against the intended scope established in `rules/scope.md`. For each
capability the scope defines, confirm it is implemented — not silently narrowed, deferred, or
reinterpreted. For each part of the diff, confirm it traces to something the scope asked for; a part
that doesn't belongs under "Accidental scope expansion," below.

Skip only when no scope evidence exists at all, and state that absence in the report.

### Correctness and edge cases

Trace the code paths the change introduces or modifies against their real inputs, not only the
paths the tests exercise. For each new or changed branch, ask what input, state, or ordering takes
the other path, and confirm the change handles it. Check edge cases the scope implies even when
untested: empty, null, or zero values; boundary values; repeated or concurrent invocation; partial
failure mid-operation; a reachable but unexpected ordering of surrounding calls.

Include the performance consequence of a changed path when evidence shows one: added queries or
query cost, unbounded work, or a measured slowdown. Never report a speculative performance concern.

A suspected defect becomes a finding only once traced to the code path that produces it — state the
reasoning or the reproduction, not only the suspicion.

### Security

Inspect every surface the change touches for:

- authorization and authentication checks at every entry point that reaches the new or changed
  capability, not only the one the tests exercise;
- input validation and sanitization at trust boundaries — user input, external API responses, file
  paths, deserialized data;
- injection risk wherever the change builds a query, shell command, template, or file path from
  variable input;
- secret, token, credential, or sensitive-data exposure — in logs, error messages, client-visible
  responses, or a location with looser access control than the data warrants.

Skip only where the change touches none of these surfaces.

### Data integrity

For a schema migration or data-shape change: confirm it is reversible, or that its irreversibility
is deliberate and stated; check defaults and backfill against existing rows, not only new ones. For
a concurrent-write or shared-state path: check for race conditions, a missing lock or transaction
boundary, or a non-atomic read-modify-write where correctness requires atomicity. Confirm the change
cannot silently drop, truncate, or overwrite existing data.

Skip when the change touches no persisted or shared state.

### Likely regressions

Identify existing behavior the change plausibly affects that the test suite doesn't already cover:
a shared code path, a caller outside the diff's own files, or a configuration or feature-flag
interaction whose meaning the change alters. A regression is existing behavior put at risk, not a
new capability's own bug.

Include compatibility and deployment consequences where the change creates them:

- existing clients, persisted data, or public contracts that the change stops accepting or alters;
- the order in which migrations, configuration, and code must reach an environment, and
  environment configuration the change newly requires.

State which existing callers or behaviors were checked, and which weren't reachable to verify.

### Architectural fit

Compare the change's shape against the approved architecture — a linked guide, `plan.md`, or an
established repository pattern, whichever is available (`rules/scope.md`) — and the project's own
conventions. Flag a change that duplicates an existing abstraction, bypasses an established
boundary, or introduces a second way to do something the codebase already does one way. Ground the
finding in the concrete existing pattern the change conflicts with.

Skip when no architectural reference exists and the change is too small to imply one; state that
in the report rather than inventing an architecture.

### Maintainability

Identify unnecessary complexity, duplication, dead code the change leaves behind, or a shape likely
to fight the next foreseeable change. Ground each finding in the diff and a concrete foreseeable
consequence — not a style preference the project doesn't establish.

Before reporting an abstraction or layer of indirection as unnecessary, run this thought
experiment: if the layer were removed or inlined at its call sites, would that remove complexity,
or would it spread a validation rule, a derivation, or an invariant back across every caller? A
layer whose removal spreads that knowledge is doing real work; that result supports retaining it.

A single current caller or a thin wrapper is a fact, not a defect. Some single-caller layers
deliberately isolate a boundary the project has established — a repository pattern, a framework
seam, or a documented architectural layer. Report a finding only when the layer's continued
existence has a demonstrated cost attributable to the layer itself: duplication it introduces,
navigation or maintenance overhead it imposes, or an adjacent change it makes harder today.

### Project and stack convention compliance

Check the change against applicable project instructions and, where one is installed and
applicable, the stack companion's rules — naming conventions, established idioms, and required
patterns. `rules/scope.md`'s "Discover applicable conventions" owns how conventions are discovered,
which base they come from when the change modifies them, and which sub-checks a missing companion
skips. Never invent a companion rule from general knowledge and present it as the project's own.

### Test adequacy

For each test the change adds or modifies, confirm it proves the behavior it claims to. A test with
no assertion on the actual behavior or output, or whose mock hides the behavior under test, is a
finding. Confirm the scope's material edge cases have coverage, or state which don't. A passing
suite is not by itself evidence of adequate coverage — inspect what the tests assert.

Check that each expectation independently proves the behavior its test owns:

- An expected value built by running the same logic, class, or transformation the test exists to
  prove moves in lockstep with the code and cannot catch a self-consistent regression. That is a
  finding when the test is the one responsible for proving that value.
- Independence is necessary but not sufficient. A literal expectation that doesn't match the
  intended behavior, or an assertion too weak to fail when the behavior regresses, is also a
  finding.
- A legitimate integration assertion is not a defect. When the test is responsible for proving
  that the right object reached the right collaborator, and a lower-level test owns that value's
  own correctness, comparing against a production-built value proves wiring. Respect that
  established test-layer ownership.

This is a distinction to apply, never a rule against mocks, database assertions, or any other
testing technique. Where an applicable stack companion documents test-layer ownership or
test-execution mechanics, apply it.

When the change modifies test infrastructure — runner configuration, the base test case or global
bootstrap, test scripts, coverage settings, or the CI test job — also verify the properties that
specific change could affect, scaled to it:

- **Execution completeness** — the run executes the complete suite, with no filtering, selection,
  or replay, including when an environment variable could switch selection on. A matching test
  count is not sufficient proof: a replayed or impact-selected run can report the full count.
  Confirm from the runner's own output and configuration that every test executed.
- **Isolation** — state the change introduces (a cached snapshot, a static resolver, a shared
  directory) cannot carry from one test into another, in one process or across parallel processes.
- **Coverage enforcement** — a changed coverage minimum is proven to fail below its threshold, not
  only to pass above it.
- **Assertion preservation** — no test was deleted, skipped, or weakened to make the change pass.

### Accidental scope expansion

Compare every changed file and hunk against the intended scope (`rules/scope.md`). Flag a change
that doesn't trace to that scope: an unrelated refactor, an unrequested dependency bump, a drive-by
rename, or a file with no connection to the stated scope. Not every out-of-scope change is a defect,
but one without explicit authorization is a finding to surface, not to accept because it looks
harmless — the human decides whether to authorize it.

Only an explicitly authorized scope change is exempt from this category. A scope change that was
merely mentioned or raised with the human is not authorized by that alone — authorization is the
human's explicit decision. The exemption covers this category only: run every other applicable
category against the authorized change as thoroughly as against the rest of the diff. Authorization
approved the work happening; it did not verify the work, and it never suppresses a defect in it.

## What this review does not flag

- A stylistic preference the project's own conventions don't already support.
- A speculative concern with no traced code path or reproducible evidence behind it.
- A category the change genuinely doesn't touch — state it as skipped, not as passed.
- A finding invented to avoid a clean result. A clean result, stated with which categories applied,
  is a legitimate and complete outcome.
