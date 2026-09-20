# Agentic Engineering v3 — The Control Room

Status: Investigation.

This document follows `v3-vision.md`, `v3-execution-architecture.md`,
`v3-execution-2-architecture.md`, and `v3-execution-3-architecture.md`.

Those documents built up the execution architecture experiment by
experiment: the three-layer separation, the boundary between
orchestration and engineering lifecycle, and the requirement for an
interactive pause/resume mechanism at human gates.

This document names and consolidates the responsibility that keeps
recurring across all three experiments: **Control Room**.

Two further useOrbit smoke tests, `#351` and `#352`, moved part of
this document from working theory to observed evidence. Both are
single-worker experiments, not multi-worker ones. A follow-up `#352`
integration smoke test then validated that integration can run as a
separate Control Room lifecycle after worker completion (see
["Integration lifecycle"](#integration-lifecycle)). Section
["Evidence"](#evidence) below states plainly what all of this
validated and what it did not.

This is not a finalized implementation design.

## Core model

Control Room is a coordination/orchestration responsibility layer
above the existing Agentic Engineering skills.

Today, the ChatGPT project effectively acts as the Control Room
through conversation state:

```text
You
  ↓
ChatGPT / Control Room
  ↓
lab-it / plan-it / implement-it / review-it / ship-it
```

The emerging durable model, based on the useOrbit experiments, is:

```text
You
  ↓
Control Room
  ↓
execution runtime
  ↓
workers
```

The rest of this document describes what each layer in that second
diagram is responsible for.

## Control Room

Control Room coordinates worker execution and integration. Worker
execution remains owned by the normal engineering lifecycle; Control
Room owns execution state, human decisions, resume/progression, and
the transition from completed workers into integration.

Concretely, that includes:

- reading the current issue dependency graph;
- recalculating readiness after meaningful state changes;
- deciding which dependency-ready work can form an execution wave;
- launching or requesting isolated workers;
- tracking worker lifecycle state;
- knowing which workers are implementing, waiting, completed,
  blocked, or failed;
- surfacing human decisions when a worker reaches a human approval
  boundary, in a compact, decision-focused form (see
  ["Rich internal state, compact external presentation"](#rich-internal-state-compact-external-presentation));
- resuming the specific worker after a human decision;
- coordinating integration as a lifecycle distinct from worker
  completion (see ["Integration"](#integration));
- verifying authoritative external state before resuming a worker
  whose last state is uncertain (see
  ["Recovery after interruption"](#recovery-after-interruption));
- presenting the next actionable decision to the human.

### Ownership distinction

Control Room does not replace `plan-it` or `implement-it`. It sits
between the human and the skills, consuming what planning produces and
coordinating what implementation executes.

```text
plan-it
    defines or maintains the engineering dependency graph.

Control Room
    consumes that graph, evaluates readiness, forms execution
    waves, and tracks execution state.

implement-it
    owns the lifecycle for one implementation worker.
```

This mirrors the boundary already established in
`v3-execution-2-architecture.md`:

> Control Room coordinates engineering skills. It does not replace
> their lifecycle contracts.

The `#351`/`#352` smoke tests reinforce this boundary directly: both
workers ran the unmodified `implement-it` methodology, and every
human decision point they hit was one `implement-it` already defines.
Control Room's job in both runs was to present those decisions and
resume the worker — not to decide what counted as a decision.

## Workers

Workers are normal engineering agents, not a separate methodology.

A worker receives:

- an issue;
- a repository;
- a branch/worktree;
- approved context;
- applicable skills;
- applicable stack companions.

It then runs the normal engineering lifecycle — specifically, normal
`implement-it`. There is no separate "parallel implement-it", and
`#351`/`#352` confirm there does not need to be one: both workers
completed a full issue lifecycle using the standard methodology,
pausing and resuming under Control Room's coordination rather than
under a modified skill.

Keep the ownership distinction explicit:

```text
implement-it
    what the worker does.

Control Room
    coordinates workers, state, human decisions, resume, and
    integration.
```

This distinction matters because the experiments in
`v3-execution-3-architecture.md` showed that unattended background
workers can accidentally bypass normal human gates when the
orchestration layer has no way to pause and resume them at those
gates. The fix is not a lighter-weight lifecycle for workers. It is
giving the orchestration layer the ability to pause a normal
`implement-it` run at a gate and resume it afterward — the mechanism
`#351` and `#352` exercised end to end.

## Runtime

The runtime is execution infrastructure, not methodology.

Possible runtime responsibilities:

- create worktrees;
- create branches;
- launch sessions;
- track sessions/workers;
- pause;
- resume;
- send messages;
- collect results;
- clean up workspaces;
- potentially perform mechanical merge/integration operations.

`#351` and `#352` also showed that the runtime's available
interaction primitives shape how a human decision gets presented, even
though the decision itself is skill-owned and Control Room decides how
to use whatever primitive exists. See
["Structured human interaction belongs to Control Room"](#structured-human-interaction-belongs-to-control-room).

Herdr is an example of the kind of runtime companion discussed in
`v3-execution-architecture.md`. It is not a formal dependency, and
this document does not claim a final architecture for it. Another
runtime could provide the same capabilities without changing the
Control Room methodology.

## Skills

Skills remain the reusable engineering methodology:

- `lab-it`
- `plan-it`
- `implement-it`
- `review-it`
- `ship-it`

Control Room coordinates skills and workers. It does not replace them.
The engineering lifecycle, gate semantics, and approval requirements
stay owned by the skills, exactly as established in
`v3-execution-2-architecture.md` and `v3-execution-3-architecture.md`,
and now confirmed by real execution in `#351`/`#352`.

## Structured human interaction belongs to Control Room

`#351` and `#352` ran the same five human decision boundaries but
presented them differently:

- `#351` used structured `AskUserQuestion` interaction for the
  full-suite decision, Review implementation, and Commit plan.
- `#352` used plain text for all five human decisions.

`implement-it` did not mandate either mechanism. It defines *when* a
decision must happen; it says nothing about *how* the decision is
rendered to the human. This gives a third layer to the ownership
split already established for gates:

```text
implement-it
    defines what decision must happen and when.

Control Room
    owns how that decision is presented to the human.

runtime
    provides the available interaction primitive.
```

Preferred Control Room behavior, based on this comparison:

- use structured `AskUserQuestion`-style interaction for finite human
  choices when that runtime capability is available;
- do not replace the structured interaction with verbose prose merely
  to simulate a decision UI.

Do not claim structured interaction (such as `AskUserQuestion`) is
available in every future runtime. Where it is not, Control Room must
still present a compact decision — see the next section.

## Rich internal state, compact external presentation

The `#351` experiment used verbose state reporting to make the smoke
test observable to the human running it. Comparing `#351` against
`#352` showed that this increased human reading time and token/context
cost without changing the lifecycle outcome.

> Control Room state should be rich internally and compact externally.

Internal state may contain:

```text
issue
worker
branch
worktree
lifecycle state
pending decision
```

Human-facing interaction should normally be compact, for example:

```text
Review implementation

Approve to proceed to Commit plan?
```

Do not require the human to read the full internal state unless
diagnostic detail is necessary.

A related failure mode surfaced in `#352`: a background worker can
produce a detailed report while Control Room also surfaces that same
output, effectively duplicating it into the human-facing conversation.
This is not yet a settled protocol, only an emerging direction:

```text
worker
    produces structured lifecycle state/result/event.

Control Room
    consumes worker state, decides what the human needs to see,
    and presents the compact human decision.
```

Avoid presenting the worker's full diagnostic transcript as Control
Room's primary human interface. Do not turn the `#351`/`#352` token
counts into a generic performance claim — see
["Token/context observation"](#tokencontext-observation).

## State model

The prior execution architecture documents distinguish worker state
from wave state. That distinction carries forward here, refined
slightly with the terminology surfaced in the later experiments.

These are candidate models, not final contracts.

### Candidate worker states

```text
READY
RUNNING
REVIEW_IMPLEMENTATION
WAITING_HUMAN
RESUMING
COMMIT_PLAN
PUSH_READY
CLOSED
FAILED
BLOCKED
```

### Candidate wave states

```text
PLANNED
RUNNING
WAITING_ON_HUMAN
PARTIALLY_COMPLETE
READY_FOR_INTEGRATION
INTEGRATING
VERIFYING
COMPLETE
BLOCKED
```

Neither list should be read as an accepted state machine. They are
working vocabulary for describing what Control Room needs to track.
`#351`/`#352` validated the worker-state side of this model for a
single worker; the wave-state side remains untested (see
["Validated vs open questions"](#validated-vs-open-questions)).

## Human gates

The parallel experiments recorded in `v3-execution-2-architecture.md`
and `v3-execution-3-architecture.md` first established the need for a
pause/resume mechanism at human gates. `#351` and `#352` are the first
real, single-worker executions of that mechanism.

Established observations:

- `#339` demonstrated that the normal single-issue lifecycle works.
- `#346`–`#348` demonstrated isolated parallel workers and exposed
  merge/shared-file conflicts.
- `#328`–`#330` demonstrated that parallel workers can bypass the
  normal human approval flow when the orchestration setup is
  unattended.
- `#332`–`#333` demonstrated that even explicitly saying "preserve the
  normal implement-it lifecycle" is insufficient when an unattended
  worker has no mechanism to pause at a human gate and resume
  afterward.
- `#351` and `#352` demonstrated, for the first time with real
  execution, that a single worker can pause at each human gate in
  `implement-it` and resume the same worker after approval, all the
  way to a completed issue lifecycle.

The key architectural conclusion, first stated in
`v3-execution-3-architecture.md`, is:

> An unattended worker cannot perform a real human approval.

`#351`/`#352` validate the mechanism that follows from that
conclusion for a single worker:

```text
worker reaches human gate
    ↓
worker reports "human decision required"
    ↓
Control Room surfaces the decision
    ↓
human approves/rejects
    ↓
Control Room resumes that specific worker
```

### The validated single-worker gate sequence

`#351` and `#352` both exercised the same five human decision
boundaries, in the same order, on real `implement-it` runs:

```text
implement
  ↓
verification decision
  ↓
Review implementation
  ↓
human approval
  ↓
Commit plan
  ↓
human approval
  ↓
commit
  ↓
Push authorization
  ↓
human approval
  ↓
push + verify
  ↓
Issue closure authorization
  ↓
human approval
  ↓
close + validate
  ↓
worker complete
```

The same worker resumed after each human approval and completed its
issue lifecycle. The worker lifecycle portion of the Control Room
model — pause at a skill-owned gate, surface the decision, resume the
same worker after approval — is no longer hypothetical.

The earlier documents used **Gate 1** and **Gate 2** as the internal
lifecycle identifiers for two of these boundaries. Later discussion,
confirmed by the human-facing language actually used in `#351`/`#352`,
settled on:

- **Review implementation** (Gate 1)
- **Commit plan** (Gate 2)

Both sets of names refer to the same underlying approval points. Use
the human-facing terms when describing what a human is being asked to
do, and keep Gate 1 / Gate 2 as internal lifecycle identifiers where
that is more convenient.

### Recovery after interruption

`#352` experienced an account-level rate-limit interruption mid-run.
Recovery behavior was correct:

- authoritative external state was re-checked;
- the worker was confirmed to be in the expected state;
- issue state was verified before resuming;
- no duplicate closure or stale action occurred.

This gives an emerging Control Room recovery invariant:

> When a worker is interrupted or its last state is uncertain, Control
> Room must verify authoritative external state before resuming from
> that state.

This is a Control Room recovery principle, not an automatic change to
`implement-it`.

### Concurrent gates remain unvalidated

One worker waiting for a human must not stop the others from
progressing. For example:

```text
#328  Review implementation → waiting for human
#329  Implementing
#330  Commit plan → waiting for human
```

This concurrent-lifecycle model was already described in
`v3-execution-3-architecture.md`. `#351`/`#352` did not test it — both
were single-worker runs. Multiple workers waiting at different gates
simultaneously, and how Control Room would present that queue of
decisions to the human, remain open (see
["Validated vs open questions"](#validated-vs-open-questions)).

## Integration lifecycle

A follow-up `#352` integration smoke test validated that integration
can run as a distinct Control Room lifecycle after a worker completes.
This is a single-worker integration, not a multi-worker one — see
["Validated vs open questions"](#validated-vs-open-questions) for the
exact boundary.

Observed flow:

```text
worker complete
    ↓
integration decision
    ↓
human approval
    ↓
dedicated integration worktree
    ↓
merge
    ↓
post-integration verification
    ↓
integration complete
```

Observed facts from the experiment:

- the `#352` worker lifecycle was already complete; the source branch
  (`issue-352-policies-expat-pages`) remained untouched throughout
  integration;
- integration was performed separately from the worker lifecycle, from
  a dedicated integration worktree created from the target branch
  (`feat/policies-http-frontend`);
- the integration decision was presented through structured
  `AskUserQuestion` (see
  ["Human interaction for integration"](#human-interaction-for-integration));
- after approval, the branch merged cleanly, with no conflict;
- the target integration branch was advanced to the resulting merge
  commit, and the temporary integration worktree/branch were removed
  afterward;
- post-integration verification ran the narrowest relevant Pest suite:
  18/18 tests passing, 88 assertions;
- the experiment stopped after integration verification and did not
  automatically continue to another issue;
- the resulting `feat/policies-http-frontend` branch was pushed
  manually by the human after the experiment concluded — this smoke
  test did not validate Control Room ownership of pushing the
  integrated branch.

This establishes an ownership boundary that was previously only a
candidate model:

```text
Worker
    owns implementation and its own issue lifecycle.

Control Room
    owns the transition from completed worker to integration.
```

Integration is not implicit in worker completion, and the worker
branch is not modified by the integration operation.

## Integration

Integration stays separate from worker lifecycle completion, as
established in `v3-execution-2-architecture.md` and reinforced by
`#352`: a worker can finish with approved commits, a pushed branch,
and a closed issue, while remaining unmerged into any shared
integration branch. Worker completion is not integration.

For example:

```text
#328 worker complete
#329 worker complete
#330 waiting at Review implementation

Integration:
#328/#329 may be eligible
#330 is not yet eligible
```

The integration state model, extended with the states the `#352`
integration smoke test actually exercised:

```text
WORKER_COMPLETE
    ↓
AWAITING_INTEGRATION
    ↓
INTEGRATION_APPROVED
    ↓
INTEGRATING
    ↓
VERIFYING_INTEGRATION
    ↓
INTEGRATED
```

This sequence is now validated by `#352` for a single completed
worker. It has not been exercised for concurrent integration of
multiple completed workers.

### Human interaction for integration

Integration is a finite human decision, and the `#352` experiment
validated the structured `AskUserQuestion` interaction mechanism for
it, the same way `#351` validated it for worker-lifecycle gates (see
["Structured human interaction belongs to Control Room"](#structured-human-interaction-belongs-to-control-room)).
Conceptually:

```text
Integrate #352?

[Merge into feat/policies-http-frontend]
[Not yet]
```

The exact option labels shown above are illustrative, not a permanent
UI contract. What is validated is the mechanism — presenting
integration as a compact, structured human decision — not any specific
wording. As with worker-lifecycle gates, `implement-it`-style
methodology defines *when* a decision boundary exists; Control Room
decides *how* it is presented:

```text
implement-it
    defines what engineering decision must happen.

Control Room
    decides how human decisions are surfaced and coordinates
    state/resume/integration.

runtime
    provides the underlying session/worktree/interaction primitives.
```

### Merge worktree ownership

Control Room owns integration coordination. A worker does not merge
its own branch into the shared integration branch.

Validated by `#352`, for a single completed worker:

```text
worker branch
    ↓
worker complete
    ↓
integration decision
    ↓
human approval
    ↓
Control Room creates dedicated integration worktree from target branch
    ↓
merge
    ↓
verify integrated state
    ↓
remove temporary integration worktree/branch
```

`#352` produced no merge conflict, so conflict resolution during
integration remains untested. Concurrent integration of multiple
completed workers, and merge conflict handling in a live multi-worker
wave, also remain untested — see
["Validated vs open questions"](#validated-vs-open-questions).

## Token/context observation

Do not turn the observed `#351`/`#352` token numbers into a generic
performance claim. The comparison showed:

- verbose experimental reporting in `#351` increased context/output
  cost without changing the lifecycle outcome;
- the rate-limit interruption in `#352` caused a real context
  discontinuity that required legitimate re-verification;
- the pause/resume lifecycle itself was not demonstrated to be the
  main source of token cost in either run.

The useful architecture principle is the same one stated in
["Rich internal state, compact external presentation"](#rich-internal-state-compact-external-presentation):

> Rich execution state should remain available internally without
> forcing rich state into every human-facing message.

Detailed timing and token telemetry for `#351`/`#352` belongs in the
stewardship reports for those runs, not in this document.

## Agent vs skill vs runtime

The current discussion has surfaced several possible implementation
forms for Control Room, without settling on one:

- Control Room as a coordinator/orchestrator responsibility;
- a possible Control Room **skill** containing reusable execution
  rules;
- a possible Control Room **agent** holding execution state and
  coordinating workers;
- a **runtime companion** providing process/worktree/session
  mechanics.

None of these should be treated as decided. `#351`/`#352` validated
the responsibility (pause/resume, gate presentation, recovery) without
committing to any of these implementation forms. The current evidence
only supports defining Control Room as a responsibility/layer first —
what it must do, not what artifact implements it.

The eventual implementation form (skill, agent, service, or some
combination) remains an open question for later experiments, in
keeping with the open question already recorded in `v3-vision.md`:

> What is the execution-layer artifact?

## Architectural diagrams

### Validated: single-worker pause/resume

```text
Control Room
    ↓
  Worker
    ↓
normal implement-it
    ↓
human decision
    ↓
  pause
    ↓
Control Room
    ↓
human approval
    ↓
resume same worker
```

This loop repeats at each gate — verification decision, Review
implementation, Commit plan, Push authorization, Issue closure
authorization — until the worker completes, exactly as observed in
`#351` and `#352`.

### Emerging: multi-worker fan-out, with a validated integration tail

```text
                    CONTROL ROOM
              coordination + state + UX
                       │
                dependency graph
                       │
                 execution wave
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Worker A     Worker B     Worker C
          │            │            │
      implement-it  implement-it  implement-it
          │            │            │
      human stops  human stops  human stops
          │            │            │
          └──── independent resume ────┘
                       │
                 worker complete
                       │
              integration decision
                       │
             dedicated worktree
                       │
                    merge
                       │
            post-integration verify
                       │
                 integrated
```

Only part of this diagram has real execution evidence behind it.
`Worker → implement-it → human stops → independent resume` is
validated, but only for one worker at a time — `#351`/`#352` never ran
Worker A/B/C concurrently, so the fan-out itself remains the working
model this document is tracking toward, not confirmed behavior. The
tail from `worker complete` through `integrated` is now validated by
the `#352` integration smoke test, for a single completed worker (see
["Integration lifecycle"](#integration-lifecycle)) — concurrent
integration of multiple completed workers is not.

### Broader layering

Consistent with `v3-execution-architecture.md`:

```text
Agentic Engineering skills
          ↓
     Control Room
          ↓
   Execution runtime
          ↓
  Workers / sessions / worktrees
```

Control Room sits above the runtime. Workers are execution instances
that still run the existing engineering methodology; they are not a
separate layer of methodology.

## Evidence

- `#339` established the normal single-issue lifecycle as a clean
  baseline.
- `#346`–`#348` demonstrated isolated parallel workers and exposed
  merge conflicts/shared-resource issues
  (`v3-execution-2-architecture.md`).
- `#328`–`#330` demonstrated parallel workers but bypassed normal
  human approvals (`v3-execution-2-architecture.md`).
- `#332`–`#333` demonstrated that even an explicit "preserve the
  normal implement-it lifecycle" instruction did not preserve human
  gates, because unattended workers had no pause/resume mechanism
  (`v3-execution-3-architecture.md`).
- `#351` and `#352` demonstrated, for the first time with real,
  single-worker execution, that the pause/resume mechanism works
  across all five human decision boundaries in `implement-it`, that
  workers need no parallel variant of the methodology, that structured
  vs. plain-text human interaction is a Control Room presentation
  choice rather than a methodology requirement, and that recovery
  after interruption can correctly re-verify authoritative state
  before resuming.
- a follow-up `#352` integration smoke test demonstrated, for the
  first time with real execution, that integration can run as a
  distinct Control Room lifecycle after worker completion: an explicit
  integration decision presented through structured `AskUserQuestion`,
  a dedicated integration worktree, a clean merge with the worker
  branch left untouched, and targeted post-integration verification
  (see ["Integration lifecycle"](#integration-lifecycle)).

## Validated vs open questions

### Validated

- isolated worker execution;
- normal `implement-it` lifecycle inside the worker;
- pause/resume at the verification decision;
- Review implementation;
- Commit plan;
- Push authorization;
- Issue closure authorization;
- same-worker continuation after approval;
- recovery after interruption with authoritative-state verification;
- worker completion independent of integration;
- explicit integration decision;
- structured human interaction for integration;
- dedicated integration worktree;
- clean merge into the integration branch;
- post-integration targeted verification.

### Not yet validated

- multiple workers simultaneously waiting at different human gates;
- clean presentation of multiple concurrent human decisions;
- wave-level Control Room state across several workers;
- concurrent integration of multiple completed workers;
- merge conflict handling in a live multi-worker wave;
- partial-wave failure behavior;
- wave completion verification;
- Control Room ownership of pushing the integrated branch (the
  integrated branch in `#352` was pushed manually by the human, not by
  Control Room).

Do not read the `#352` integration smoke test as proving any of these
multi-worker items — it exercised integration for exactly one
completed worker.

## Open questions

- What is the smallest viable Control Room runtime?
- Should Control Room ultimately be implemented as an agent, a skill,
  a service, or a combination?
- What exact worker-to-Control-Room protocol represents "human
  approval required"?
- How does pause/resume work across real runtimes other than the one
  used in `#351`/`#352`?
- Where should worker lifecycle state persist?
- How should merge/integration ownership and conflict resolution work
  when multiple completed workers integrate concurrently? (Ownership
  for a single completed worker is validated — see
  ["Integration lifecycle"](#integration-lifecycle) — but concurrent
  integration and conflict handling are not.)
- Should Control Room inspect likely file/resource conflicts before
  launching a wave?
- What context is shared across workers versus isolated?
- How should partial failure affect the rest of a wave?
- Should integration happen incrementally or only after wave
  completion?
- How should Control Room present multiple actionable gates from
  different workers at once?
- Should Control Room authorize and execute pushing the integrated
  branch after integration, and if so, under what human decision?

## Guiding principle

Control Room should evolve the same way the rest of Agentic
Engineering evolved:

```text
Observed behavior
    ↓
Evidence
    ↓
Explicit decision
    ↓
Reusable rule
```

`#351` and `#352` moved the single-worker pause/resume lifecycle from
working theory to observed evidence, and the follow-up `#352`
integration smoke test did the same for single-worker integration. The
next experiments should target the open questions above — starting
with multiple workers waiting at different gates at once — rather than
re-testing what these smoke tests already settled.
