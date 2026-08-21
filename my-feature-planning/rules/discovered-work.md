# Discovered Work

`SKILL.md`'s "Two work origins" distinguishes Planned work (already-understood or approved scope — a feature ask, or `plan.md`) from Discovered work (evidence of something unexpected found during implementation, code review, manual smoke testing, production/debugging, or another workflow). This file governs the Discovered path.

The defining trait of Discovered work: at the moment it's noticed, there is nothing yet to classify or scope. The symptom is real; the problem it points at, its blast radius, and sometimes even whether it's a defect at all, are not yet known. Classification (`rules/feature-classification.md`) and the checklists downstream of it all assume a validated finding — running them on a raw symptom is how a vague or wrong issue gets drafted. This file is what turns a raw finding into that validated input.

Three real Phase 22 findings ground everything below: #294 (stale `register()` references breaking two guest pages), #295 (revisiting Security settings silently disabling in-progress 2FA), and #296 (an automatic Inertia background revisit getting a full-page response instead of JSON on a 2FA-incomplete account's Security page). They illustrate the range this file covers — they don't define a rigid procedure to replay verbatim.

## What Discovered work is not

- **Not** an excuse to fix the code directly. This skill plans and drafts issues; it never carries a discovered finding into an application-code fix. Fixing belongs to the implementation skills, after an issue exists and is approved — same boundary Planned work already respects.
- **Not** license to file an issue from the first symptom. A toast that says "Something went wrong" is not itself a scoped issue — #295 shows exactly why: the toast was a downstream symptom of a silent 2FA reset, a materially different and more serious problem than the toast alone suggested.

## Intake path

Work through these in order. Each step earns the right to the next — don't skip to drafting because the first plausible story sounds right.

1. **Capture the raw finding as observed**, without theorizing about cause yet. What was actually seen (a blank page, a toast, a diff, a log line), where, and under what conditions.
2. **Separate what's known from what's assumed.** State plainly what was directly observed versus what's being inferred. A hypothesis is not a fact until reproduction or evidence confirms it.
3. **Reproduce when practical.** If the finding can be reproduced, do that before investigating further — reproduction is what let #295's investigation disprove its own first hypothesis (an "unfinished enrollment" problem) instead of running with it.
4. **Investigate enough to separate the symptom from the underlying problem**, at a depth proportional to what the evidence demands — see "Investigation depth" below.
5. **Determine blast radius.** What else shares the same code path, the same stale reference, the same condition that triggers the symptom? #294's blast radius was "exactly two frontend files" — cheap to determine, and determining it was still a required step, not an assumption.
6. **Distinguish a defect from intended behavior encountered during investigation.** Investigation sometimes proves the code is working as designed and the real gap is elsewhere (a missing explanation, a UX gap) — #296's "navigation looks broken" thread resolved this way: the mandatory-2FA redirect was correct behavior; the actual defect was that its message never reached the user.
7. **Check whether the finding contradicts an approved product/architecture decision**, or merely exposes an implementation defect inside already-agreed scope. A finding that touches a locked `plan.md` decision or an established convention is a different situation than a straightforward bug.
8. **Identify whether a human product/architecture decision is required** before the work can even be correctly scoped. If yes, stop and ask — don't guess at a product call and present it as settled, the same posture `rules/plan-md-input.md` already takes toward a stale derived constraint.
9. **Only once the finding is validated** — known/unknown boundary stated, reproduced where practical, blast radius understood, defect-vs-intended-behavior resolved, and no open product/architecture question blocking scope — hand it to the normal pipeline: classify (`rules/feature-classification.md`; a discovered finding is usually shape C or D, but classify it rather than assuming), draft per `rules/issue-conventions.md` (see that file's "Discovered-work issues" for the one legitimate difference and its "Title convention" for how the issue gets named), sequence per `rules/sequencing.md`'s discovered-work carve-out (a standalone finding is not forced into the backend-before-frontend batching template built for planned feature drafting), review per `rules/review.md`, create only after approval. From here on, Discovered work and Planned work are the same pipeline — there is no separate, lighter issue-quality bar for a discovered finding.

## Investigation depth

Proportional, not automatically exhaustive. These three bands describe a range, not a checklist to announce or a state machine to narrate — let the evidence in front of you decide how far to go, and let a finding escalate from one band to the next exactly when reproduction or falsification demands it, the way #295 actually did.

**Shallow** — the symptom and cause are obvious and deterministic (one plausible mechanism, easily confirmed). Once the cause is understood, the remaining work is verifying completeness/blast radius, then stopping.
> #294: a blank page and a runtime `TypeError` pointed straight at a stale `register()` import; a search of the frontend confirmed exactly two files referenced it. Nothing more to investigate — straight to scoping the issue.

**Focused** — multiple plausible causes exist, or the symptom crosses feature boundaries. Reproduce, isolate variables, and falsify wrong hypotheses one at a time rather than running with the first plausible story. Push to an actual root cause when it's reasonably reachable with the access already available.
> #295: the visible toast initially suggested an unfinished-enrollment problem. Reproduction disproved parts of that framing and traced the real mechanism instead: a GET to Security invoking Fortify's own abandoned-confirmation cleanup, silently clearing an unconfirmed `two_factor_secret`. The toast turned out to be a downstream symptom of a materially more serious defect — the investigation went deep because the first hypothesis was wrong, not because deep is the default.

**Deep** — destructive/security/data-integrity-relevant behavior, cross-layer or protocol-level interactions (framework internals, browser behavior, wire-level requests), contradictory evidence, or a symptom that may be hiding a materially different defect underneath. Trace across whatever boundaries are necessary and prove the claims that matter, rather than asserting them. Deep investigation still has a legitimate stopping point — see below.
> #296: the response mismatch (a full ~20KB HTML page instead of Inertia's expected ~500-byte JSON, on an automatic background revisit) was reproduced and characterized precisely enough to scope real work — but the exact request-header-level reason the server treats that particular automatic request as a plain page load was not resolved, because isolating it needed a captured request with headers: implementation-adjacent tooling this investigation pass didn't have. That remaining unknown was written honestly into the issue rather than forcing investigation to continue indefinitely.

The governing principle:

> Investigate until there is enough evidence to scope honest work — not necessarily until the fix, or even the root cause, is known.

## Investigation checkpoint

Not a fixed time or token budget — #295 needed real depth, and going that deep was correct. The checkpoint is a guidance mechanism, not a rigid state machine or timer: surface a compact checkpoint whenever the investigation itself produces one of these signals, rather than going silent until a finished narrative emerges:

- **A major hypothesis is falsified.** The story the investigation was following turns out to be wrong — #295's "unfinished enrollment" framing collapsing is exactly this.
- **Investigation crosses from application code into framework/vendor/browser/tooling internals.** Once the trail leaves this codebase's own code, the cost of continuing goes up and the human should see that transition happening.
- **A second distinct architectural/runtime layer becomes implicated.** The finding isn't confined to one layer anymore (e.g. a frontend symptom turns out to implicate server-side session/auth state, or a controller bug turns out to implicate a third-party package's own internal state machine, as in #295).
- **The remaining unknown appears likely to require unavailable tooling or implementation-adjacent instrumentation.** The trail is heading toward something this pass can't actually resolve (#296's request-header capture).
- **A natural point is reached where enough evidence may already exist to scope an honest issue.** Not every checkpoint means "keep going" — sometimes it's the moment to notice the finding is already scopeable.

Any one of these is enough to trigger a checkpoint — they aren't a checklist that all has to fire together. When a checkpoint is triggered, report:

- What's confirmed (directly observed or reproduced)
- What's been ruled out (a falsified hypothesis, and how it was falsified)
- What remains unknown
- The next highest-value diagnostic step
- Whether there's already enough evidence to write a truthful issue

The checkpoint exists to give the human visibility and the chance to say "enough — carry the remaining uncertainty into the issue," rather than have investigation continue by default just because it hasn't yet produced a complete story. It is not a license to stop at the first signal either — a checkpoint can conclude "still worth continuing," in which case investigation resumes at the depth the evidence actually calls for.

## Stopping condition

> Stop investigating when the remaining unknown would require disproportionate effort, tooling unavailable in this pass, invasive/implementation-adjacent instrumentation, or deeper exploration that isn't actually necessary to define a coherent issue — provided the known/unknown boundary can be stated honestly in the issue that gets written.

A Discovered-work issue does not need a predetermined fix. When the mechanism is still unresolved, it's legitimate for the issue to include investigation/instrumentation as one of its own Tasks (#296 is the model: "Capture the automatic Inertia revisit's actual request... to identify why the server responds with a full page instead of the expected Inertia JSON") — but the issue must keep confirmed facts and open hypotheses visibly distinct, never phrase a guess as settled fact. See `rules/issue-conventions.md`'s "Discovered-work issues" for how this is written, and `rules/review.md` for how it's checked before creation.

## Handoff boundary

This skill's ownership of a discovered finding stops exactly where it stops for any other issue: at creation. It owns the finding only far enough to determine whether it's real, investigate it proportionally, and turn it into one coherent, self-contained, appropriately-scoped issue — or to escalate it as a product/architecture question the human must resolve before an issue can even be correctly drafted. It does not fix code, and it does not carry the investigation into implementation.

Once an issue coming out of this path is approved, `my-git-workflow` owns everything from there — implementation, human review, semantic commits, verification, and closure — exactly as it does for any other approved issue. An agent mid-investigation under this skill should not start editing application code to "just fix it"; an agent implementing an approved discovered-work issue should not reopen the investigation-depth question — that was already settled when the issue was created and approved.
