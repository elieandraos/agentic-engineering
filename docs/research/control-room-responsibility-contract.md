# Control Room Responsibility Contract — v2.3 Candidate

> **Status:** proposed responsibility contract for the v2.3 orchestration investigation. This document is a decision candidate, not yet canonical methodology. It changes no skill by itself.
>
> **Basis:** current specialist contracts on this branch, `orchestration.md`, the independent `phase26-coordination-ownership-audit.md`, and the normal-use Phase 26 evidence those documents retain.
>
> **Question:** if a first-class Control Room had existed when the specialist skills were designed, what is the smallest coherent responsibility each specialist would own, and what connective responsibility would sit above or below it?

## Decision test

A responsibility is not kept merely because the current skill performs it correctly, and it is not moved merely because a parent session happened to perform it.

For every responsibility apply both tests:

1. **Evidence test** — has real execution shown that the responsibility requires context beyond one specialist or worker, or that its current placement creates duplicated/cross-context ownership?
2. **Counterfactual ownership test** — if Control Room had existed from the start, would this responsibility naturally be part of the specialist's intrinsic job?

Classifications:

- **KEEP** — intrinsic specialist responsibility.
- **MOVE CANDIDATE** — currently valid where it is, but evidence plus the counterfactual test support moving ownership upward.
- **ADD** — repeated parent responsibility with no durable specialist owner.
- **RUNTIME** — required execution capability whose mechanism is runtime/stack-specific.
- **HUMAN** — judgment or authorization retained by the human.
- **UNRESOLVED** — evidence is real but insufficient for an ownership decision.

No MOVE becomes canonical until its consequences are reviewed and explicitly approved.

## Core boundary

> **A specialist owns how to perform its engineering stage correctly and how to report that stage's result. Control Room owns continuity of the engineering journey, coordination across simultaneously active specialist executions, and composition/routing of state and decisions across those boundaries. Runtime capabilities make the requested execution state real. The human retains product judgment and authorization.**

Control Room is not synonymous with parallelism. It must remain useful when there is no implementation worker, one implementation worker, or several concurrent workers.

## Responsibility matrix

| Current responsibility | Current owner | v2.3 classification | Proposed owner | Reason |
| --- | --- | --- | --- | --- |
| Architecture/system investigation | `lab-it` | KEEP | `lab-it` | Intrinsic Lab work; Phase 26 repeatedly showed Lab doing the evidence/materiality work correctly. |
| Challenge premature architecture solutions | `lab-it` | KEEP | `lab-it` | Part of investigation and decision discipline, not coordination. |
| Determine whether Lab's own investigation is resolved | `lab-it` | KEEP | `lab-it` | A specialist must know whether its own result is complete enough to report. |
| Declare/recommend that resolved Lab output can proceed to Plan | `lab-it` | MOVE CANDIDATE | Control Room | Correct today, but it crosses a stage boundary. Counterfactually Lab can return an explicit resolved/approved result while Control Room decides/routs what stage is next. Evidence is weaker than for horizontal coordination because the human explicitly scripted Lab→Plan in E2/E3. |
| Route architecture-guide work to `document-it` | `lab-it` | UNRESOLVED | TBD | Correct current boundary but not exercised in Phase 26; no extraction evidence. |
| Turn approved intent into implementation-ready issues | `plan-it` | KEEP | `plan-it` | Intrinsic Plan work. |
| Scope/decompose issues, dependencies, metadata and coordination notes | `plan-it` | KEEP | `plan-it` | Later implementation relied on these outputs; no ownership gap. |
| Determine whether Plan's own output is complete/reviewed | `plan-it` | KEEP | `plan-it` | Specialist completion semantics. |
| Declare downstream implementation handoff | `plan-it` | MOVE CANDIDATE | Control Room | The specialist can return “planning complete”; routing that result into implementation is cross-stage. Current evidence does not show a failure, so this is architectural cleanup only if the broader lifecycle-routing contract is adopted. |
| Reconstruct/preserve lifecycle position across sessions/stages | none; parent session | ADD | Control Room | Strongest vertical evidence, repeated E2–E8. No specialist owns PR/milestone state plus human dispositions plus unresolved cross-stage loose ends. |
| Preserve human dispositions and unresolved cross-stage context | none; parent session | ADD | Control Room | Same cross-session continuity problem; survives single and parallel execution. |
| Choose the lifecycle specialist to invoke when work changes kind | human/parent; specialist triggers | ADD, human-authorized | Control Room + human | Control Room may recommend/route based on state; human retains material redirection/authorization. Existing evidence has the human explicitly choosing Lab→Plan, so autonomous routing is not established. |
| Compute implementation ready set | `implement-it` sequencing | KEEP | `implement-it` | Depends directly on issue/dependency conventions owned by implementation methodology; v2.2.1 works. |
| Recommend next execution shape (one issue or safe subset) | `implement-it` sequencing | MOVE CANDIDATE | Control Room, consuming implementation readiness evidence | Counterfactually “what execution shape should happen next?” is journey/execution coordination, not one issue's implementation. Evidence shows the current rule works and is tightly coupled to issue conventions, so any move must preserve `implement-it` as the source of readiness/dependency semantics rather than duplicate them. |
| Human authorization of selected execution shape | human | HUMAN | human | Recommendation never equals authorization. |
| Implement one approved issue | `implement-it` | KEEP | `implement-it` | E5 showed no coordination residue inside the single-issue lifecycle. |
| Issue-local targeted/quality verification | `implement-it` | KEEP | `implement-it` | Intrinsic implementation evidence. |
| Invoke/consume independent implementation review | `implement-it` + `review-it` | KEEP | same | Gate semantics and assurance remain specialist-owned. |
| Review implementation semantics / approval-validity policy | `implement-it` | KEEP | `implement-it` | Defines what issue approval means; parent presentation must not own semantics. |
| Commit plan and semantic commit boundaries | `implement-it` | KEEP | `implement-it` | E8 showed the rule correctly drove coherent intermediate states. |
| Push readiness, issue closure, deferred-context propagation | `implement-it` | KEEP | `implement-it` | Issue-local lifecycle semantics; bypassing them caused defects in E1. |
| Recognize implementation phase has no open milestone issues | `implement-it` | KEEP | `implement-it` | It owns the issue graph and can report the state accurately. |
| Route a completed implementation phase into Ship | `implement-it` | MOVE CANDIDATE | Control Room | Counterfactually Implement should report “no implementation work remains”; lifecycle routing to Ship belongs above the stage. `ship-it` independently re-checks readiness, so moving the routing does not weaken delivery semantics. |
| Worker brief composition | none; parent session | ADD | Control Room | Repeated cross-worker responsibility; each worker lacks wave context. Runtime/environment details are excluded and delegated below. |
| Worker identity/state and wave synchronization | none + runtime signals | ADD | Control Room | Repeated E6–E8. Runtime supplies events; Control Room interprets issue/wave meaning. |
| Route worker-specific human decisions | none; parent session | ADD | Control Room | Repeated; preserves worker identity while human retains the decision. |
| Wave-level full-suite run/skip policy | `implement-it` verification | KEEP | `implement-it` | Defines implementation evidence and Gate 1. |
| Assemble a combined candidate | explicitly unowned | ADD / RUNTIME boundary | Control Room coordinates; runtime realizes | Repeated four waves. Control Room needs the combined state; Git/worktree/dependency mechanics must not become portable coordination policy. |
| Author semantic conflict reconciliation | none | UNRESOLVED | TBD | One occurrence. Parent-authored code existed in neither reviewed worker state. |
| Determine review validity after cross-worker reconciliation | policy in `implement-it`; cross-worker application unowned | UNRESOLVED | TBD | Policy is correct; ownership of materiality/renewed review across workers is not settled. |
| Coordinate convergence of approved worker results | partially `implement-it` sequencing; mechanics unowned | MOVE CANDIDATE | Control Room | Repeated cross-worker activity. Keep worker eligibility/invariants in `implement-it`; move wave-level ordering/progression only if this split is approved. |
| Prove verified combined state corresponds to converged history | none | UNRESOLVED | TBD | Final-tree identity worked repeatedly but is not yet proven as a universal invariant. |
| Compose several specialist/per-issue results into one decision surface | none; parent session | ADD | Control Room | Repeated E6–E8; presentation/orientation only, never gate or review semantics. |
| Compact code-surface orientation for implementation approval | none; human preference | ADD candidate | Control Room presentation | Human-facing requirement applies to decision composition; does not belong in `review-it`. Preference is retrospective evidence, not a live-wave rule. |
| Independent implementation assurance | `review-it` | KEEP | `review-it` | Target-agnostic independent specialist; no evidence supports moving semantics upward. |
| Determine what implementation state should be sent for assurance | caller/parent | UNRESOLVED for reconciled waves | Control Room candidate | Straight issue-local calls are already clear; reconciled cross-worker state exposed an unresolved target-selection question. |
| Milestone PR readiness and creation | `ship-it` | KEEP | `ship-it` | Intrinsic delivery semantics. |
| CI/delivery-failure investigation and correction scoping | `ship-it` | KEEP | `ship-it` | Intrinsic delivery work; correction implementation remains `implement-it`. |
| Milestone closure/release semantics | `ship-it` | KEEP | `ship-it` | Intrinsic Ship work. |
| Decide that the journey has entered a Ship concern | currently human/preceding handoff | ADD / MOVE CANDIDATE | Control Room + human | Cross-stage orientation is a Control Room concern, but evidence for autonomous entry is limited. |
| Documentation authoring/review | `document-it` | KEEP | `document-it` | Intrinsic documentation specialist. |
| Route missing/stale documentation evidence into Lab | `document-it` | UNRESOLVED | TBD | Current rule is coherent; Phase 26 did not exercise it. |
| Retrospective workflow diagnosis | `steward-it` | KEEP | `steward-it` | Explicitly human-invoked and outside normal lifecycle. |
| Automatic stewardship as a lifecycle stage | none | KEEP ABSENT | none | No evidence supports adding it. |

## Counterfactual specialist contracts

These are the smallest coherent specialist boundaries if Control Room exists. They are design candidates, not yet skill edits.

### lab-it

**Intrinsic contract:** investigate and validate architecture/system behavior; challenge unsupported solutions; resolve architecture decisions with the human; return explicit investigation state and, when requested, an approved `plan.md`.

**Potential extraction:** downstream lifecycle routing after Lab reports a resolved result.

Lab still owns its materiality test and knows whether its own investigation is resolved. Control Room must not duplicate Lab's architecture judgment.

### plan-it

**Intrinsic contract:** transform approved intent or an approved plan into reviewed, dependency-aware, implementation-ready GitHub issues and return explicit planning state.

**Potential extraction:** downstream lifecycle routing after Plan completes.

Plan does not choose implementation waves. The one observed plan-time wave recommendation was outside its stated scope.

### implement-it

**Intrinsic contract:** own one approved issue's implementation lifecycle: entry readiness, implementation, issue-local verification, independent review integration, Review implementation, Commit plan, semantic commits, push readiness, issue closure, and deferred-context handling.

**Cross-issue semantics retained as specialist knowledge:** dependency/readiness interpretation and the evidence requirements that make one or several issues safe candidates for implementation.

**Potential extraction:**
- presentation/selection of the next execution shape at the journey level, while preserving `implement-it` as the source of issue/dependency readiness semantics;
- wave-level convergence coordination after issue candidates are approved;
- lifecycle routing to Ship after `implement-it` reports that no implementation work remains.

This is the skill with the strongest plausible narrowing, but the split must not duplicate sequencing or weaken issue-local gates.

### review-it

**Intrinsic contract:** independently assure the exact implementation state supplied to it and report verified findings/limitations without mutation.

**No semantic extraction proposed.**

Open question: who selects/reselects the review target when a coordinating context creates reconciled code outside individual worker candidates?

### ship-it

**Intrinsic contract:** delivery semantics: milestone PR readiness/creation, open-PR CI/delivery investigation, authorized correction handoff, post-merge milestone closure, release preparation/publication/validation.

**Potential extraction:** only the surrounding lifecycle decision that Ship is now the appropriate specialist. Ship still independently proves its own entry conditions.

### document-it

**Intrinsic contract:** create/update/review architecture guides from sufficient current evidence.

No extraction decision from Phase 26. Its current conditional route to Lab remains until exercised evidence justifies change.

### steward-it

**Intrinsic contract:** human-invoked retrospective diagnosis and improvement recommendations.

No role in automatic lifecycle progression.

## Control Room candidate contract

### 1. Journey continuity

Control Room maintains the cross-specialist state needed to answer:

- where is the engineering journey now?
- what specialist work has completed?
- what human decisions/dispositions remain in force?
- what unresolved context must survive the next handoff?
- what work or decision is pending?

This state is broader than GitHub/repository state and narrower than duplicating specialist internals.

### 2. Lifecycle routing

Control Room coordinates entry into the appropriate specialist based on journey state and specialist results, while preserving human authorization where current methodology requires it.

A specialist reports its own completion/readiness state. Control Room owns the cross-stage interpretation/routing, not the specialist's internal completion semantics.

Whether every existing specialist handoff sentence should be removed is a later editing decision; duplicate ownership should not remain after the final contract is approved.

### 3. Execution-shape coordination

Control Room coordinates implementation as one issue or several concurrent issue lifecycles.

Candidate split:

- `implement-it` remains authoritative for issue readiness/dependency semantics;
- Control Room owns journey-level selection/presentation of the execution shape and coordination of the selected shape;
- the human authorizes execution.

This MOVE CANDIDATE requires explicit approval before skill changes because current v2.2.1 sequencing works correctly.

### 4. Horizontal worker coordination

When several issue lifecycles execute concurrently, Control Room owns:

- worker briefing with wave-relevant context;
- worker/issue/state identity;
- synchronization at shared boundaries;
- routing worker-specific decisions;
- coordination of combined-state preparation;
- coordination of approved-result convergence.

It does not own issue implementation, verification semantics, review semantics, or commit semantics.

### 5. Human-facing coordination

Control Room composes specialist/runtime evidence into decision-specific presentations while preserving the semantics of the owning skill.

It tracks what is pending, approved, blocked, or bundled and routes human answers back to the correct lifecycle/work item.

Candidate presentation distinction supported by Phase 26:

- **candidate checkpoint:** cross-worker outcome/interaction plus combined-verification decision;
- **Review implementation:** implementation outcome, compact code-surface orientation, evidence and review supporting approval;
- **Commit plan:** semantic history and convergence implications.

These are presentation responsibilities, not new approval semantics.

## Runtime capability boundary

Control Room expresses required execution state; runtime/stack capabilities make it real.

Observed capability needs include:

- start an isolated execution context from an exact source state;
- maintain stable worker identity and completion/resumption signals;
- prepare dependencies/environment so the worker executes its own source;
- prepare required generated/build state;
- expose effective skill/runtime state where precedence matters;
- execute authorized Git/GitHub operations subject to platform permissions;
- isolate or safely mediate repository-shared execution state;
- retire temporary execution resources safely.

Claude Code worktrees, `SendMessage`, copied Laravel `vendor`, Wayfinder commands, Vite builds, shell quirks, and permission-classifier behavior are evidence about one runtime/stack combination, not Control Room semantics.

## Human contract

The human retains:

- product and architecture decisions;
- approval at specialist-defined human gates;
- authorization of an execution shape;
- implementation approval;
- commit-plan approval;
- publication/push/PR/merge/release authorizations where current methodology requires them;
- explicit redirection of the journey.

Control Room may recommend, orient, compose, and route. It does not convert a recommendation into authorization.

## Unresolved ownership

Do not assign these merely to make the architecture look complete:

1. **Conflict reconciliation authorship** — one real occurrence is insufficient to decide who should author code present in neither worker candidate.
2. **Review validity after reconciliation** — the policy exists; ownership of cross-worker materiality/renewed review remains unsettled.
3. **Final-tree equivalence** — repeated and useful, but not yet established as a portable invariant.
4. **Workspace retirement decision** — runtime owns mechanics; evidence does not yet settle whether retirement is automatic runtime policy, Control Room progression, or a human-approved action.
5. **Durable runtime/stack lessons** — personal/session memory is incomplete; where settled stack/runtime knowledge lives is not decided here.
6. **Post-PR lifecycle reopening** — PR #357 later gained milestone work, but one occurrence is insufficient to redefine Ship/Control Room ownership.
7. **Documentation-to-Lab routing** — current specialist rule is coherent but untested in this evidence set.

## Proposed v2.3 delta

If this contract is approved, the next design pass should evaluate concrete skill edits in this order:

1. **Add Control Room responsibilities** for journey continuity, lifecycle routing, horizontal coordination, and human-facing composition.
2. **Narrow cross-stage handoff language** in Lab/Plan/Implement/Ship only where it would duplicate approved Control Room routing. Specialists must still report explicit completion/readiness states.
3. **Evaluate `implement-it` extraction candidates** separately:
   - next execution-shape presentation/selection;
   - wave-level convergence coordination;
   - zero-open lifecycle routing to Ship.
   Keep readiness/dependency semantics, verification policy, gates, commits, push readiness, and issue closure in `implement-it`.
4. **Leave `review-it`, `document-it`, and `steward-it` semantics intact** unless later evidence changes the boundary.
5. **Define the runtime capability contract** without embedding Claude Code/Laravel mechanics.
6. Resolve or explicitly defer the unresolved ownership questions before declaring the 2.3 architecture complete.

## Approval questions

Before any skill or executable Control Room artifact is changed, decide:

1. Should cross-stage routing be owned by Control Room while specialists retain only their own completion/readiness semantics?
2. Should journey-level execution-shape selection move to Control Room while `implement-it` remains authoritative for ready/dependency semantics?
3. Should wave-level convergence coordination move to Control Room while issue-local eligibility and gates remain in `implement-it`?
4. Is the proposed human-facing composition responsibility correctly above the specialists rather than inside `review-it` or `implement-it`?
5. Are the unresolved items correctly deferred rather than assigned prematurely?
