# Phase 26 Coordination Ownership Audit

> **Status:** an execution-side evidence and ownership audit, to be reconciled later against the
> canonical orchestration research. It is **not** the Control Room design, a responsibility
> contract, or an approved methodology change. Nothing here is a rule or an architecture decision.
>
> **How it was built:** reconstructed from useOrbit Phase 26 session evidence and the locally
> installed skill rules in useOrbit (`.claude/skills/*`). The Agentic Engineering `orchestration`
> branch was **not** inspected or interpreted while producing it. It was committed to this branch
> afterwards only to preserve it.

## Scope and evidence

**Question:** across the whole observed engineering lifecycle, what responsibilities and decisions did
the coordinating parent session actually have to own that were not already owned by a specialist
Agentic Engineering skill, an individual issue worker, Claude Code/runtime mechanics,
project/stack-specific knowledge, or the human?

**Framing:** orchestration is not equated with parallel execution. Each responsibility is checked
against both shapes: one issue executed serially, several executed concurrently, and no
implementation at all (Lab, Plan, Review, Ship).

**Sources:**
- the 2026-09-29 useOrbit session that ran E8 and produced this audit;
- eight earlier Phase 26 session transcripts, extracted read-only by four agents. Quotes and
  timestamps below come from their reports and were not all re-checked first-hand;
- useOrbit memory evidence files;
- useOrbit git history and GitHub issue/PR state;
- the rule text of the skills installed locally in useOrbit.

**Episodes:**

| Ref | Date | What happened |
|---|---|---|
| E1 | 09-22 | #334/#344/#345 wave (older AE, before v2.2.0), then ship-it creates PR #357, then AE v2.2.0 methodology work |
| E2 | 09-23 | PR #357 review findings go through Lab → Plan and become #358–#367 |
| E3 | 09-24 | Manual UI findings from testing PR #357 go through Lab → Plan and become #368–#373 |
| E4 | 09-24 | Two "what's next" implement-it sessions. The wrong copy of the skill loaded, then the recommendation was redone. |
| E5 | 09-27 | #368 on its own (single issue, no workers) |
| E6 | 09-28 | Four-issue wave #362/#358/#363/#373 |
| E7 | 09-28 | Deliberately overlapping #359/#360 wave |
| E8 | 09-29 | #369/#372/#364 wave |

**Limits of the evidence:**
- document-it and steward-it were never invoked in any Phase 26 session.
- ship-it evidence covers one readiness check and PR creation (E1). There was no CI-correction or
  post-merge evidence.
- **"Code surface" provenance:** the preference for a compact "Code surface" view in Review
  implementation is human feedback preserved retrospectively. It appears only in the human's E7
  retrospective prompt ("I wanted a compact 'Code surface' view in Review implementation, grouped by
  responsibility rather than a raw filename dump"). The audit could not establish that it was
  requested during the live wave itself.

**Classification vocabulary:**
- **Decision provenance:** Skill-prescribed → Parent-applied; Parent-originated judgment;
  Worker-local judgment; Runtime-determined; Project/stack-guided; Human decision.
- **Recurrence:** one occurrence; repeated; repeated across materially different situations.
- **Execution shape:** applies to both single and parallel implementation; parallel-specific
  horizontal coordination; lifecycle coordination independent of implementation shape; not
  orchestration.
- **Extraction assessment:** keep in specialist skill; candidate Control Room responsibility;
  candidate runtime capability/adapter responsibility; keep with human; insufficient evidence.

## Candidate responsibilities

### C1: Knowing where the lifecycle stands (cross-session orientation)

**Observed evidence (E2–E8, in every session):**
- **State that GitHub can't reconstruct had to be carried or re-established each time.** Examples:
  - PR #357 was open while the milestone gained new issues.
  - The uncommitted `plan.md` deletion. It was flagged as a risk in E4, E5 and E6, and the human had
    to say "preserve it untouched" twice.
  - Human dispositions such as "evidence only, don't record rules" and "don't merge PR #357".
  - Leftover worktrees and stale build output.
  - The milestone count including the PR. It confused E4 ("15 vs 14") and was left unexplained in E6.
- **Recommendations flipped between sessions with the same inputs:** #369 → #368 (E4, minutes apart),
  then #362 (E5, refactors first), then #359 as the first option (E7). The human's chosen ordering
  strategy wasn't persisted anywhere except the conversation.
- **Where the context came from:** memory files, fresh `gh`/`git` queries, and the human's
  restatements. `/clear` or a new session reset it each time.
- **Why no specialist had enough context:**
  - implement-it reads the issue graph and the branch, not PR or working-tree dispositions.
  - lab-it and plan-it end at their own handoffs.

**Decision provenance:**
- No skill policy covers it.
- Deciding what matters was Parent-originated judgment.
- The dispositions themselves were Human decisions.
- Storing them in memory was Parent-originated, done on the human's instruction.

**Existing owner:** none; genuinely cross-lifecycle. **Recurrence:** repeated across materially
different situations. **Execution shape:** lifecycle coordination independent of implementation
shape. **Extraction:** candidate Control Room responsibility.

### C2: Routing raw observations into a stage when no stage is active

**Observed evidence (E2, E3; also E1 before the PR):**
- In both E2 and E3 the human wrote the routing themselves: "Lab → Plan → later Implement", "use
  lab-it only where investigation is actually needed", "Stop for my approval before invoking
  plan-it".
- Nothing in ship-it routes PR-review findings to Lab. ship-it's CI-correction entry was never used;
  in E2, lab-it checked CI itself.
- plan-it's `discovered-work.md` covers turning a raw finding into planning input, but it was never
  the entry point.

**Decision provenance:**
- The routing was a Human decision, by prompt.
- Invoking lab-it was Skill-prescribed → Parent-applied (by lab-it's trigger description).
- Grouping the findings and challenging proposed solutions happened inside lab-it.

**Existing owner:** human. **Recurrence:** repeated (2 times). **Execution shape:** lifecycle,
independent of shape. **Extraction:** keep with human. There's no evidence the parent was expected to
route on its own and failed.

### C3: Stage-exit proposals (Lab→Plan, Plan→Implement, Implement→Ship)

**Observed evidence:**
- **Lab→Plan:** lab-it stopped for approval (E2, E3); the human authorized it.
- **Plan→Implement:** plan-it's Handoff ended with "implement-it can pick these up".
- **Implement→Ship:** in E1 the parent cited implement-it's zero-open rule, and the human then asked
  for the readiness check.

**Decision provenance:** Skill-prescribed → Parent-applied, with a Human decision at each transition.

**Existing owner:** lab-it, plan-it and implement-it respectively. **Recurrence:** repeated.
**Execution shape:** lifecycle. **Extraction:** keep in specialist.

**Note:** in E2, plan-it also recommended execution waves ("Wave A = #358/#359/#362/#363/#364…")
without recording them as dependencies. That falls outside plan-it's stated scope. It's a single
occurrence.

### C4: Next-issue and execution-shape recommendation

**Observed evidence:**
- Every "what's next" went through `sequencing.md`.
- In E4, E5 and the start of E6 the parent didn't raise concurrency; the human did. By E7 and E8 the
  parent proposed waves unprompted, and in E8 it included an overlap table.
- The human overrode the recommendation in E7 (they picked an overlapping pair).

**Decision provenance:**
- The policy is Skill-prescribed (`sequencing.md`: ready set, "may recommend a concurrent subset",
  "recommendation is not authorization") → Parent-applied.
- The choice was a Human decision each time.

**Existing owner:** implement-it. **Recurrence:** repeated across materially different situations.
**Execution shape:** both. **Extraction:** keep in specialist.

### C5: One issue's implementation lifecycle

**Observed evidence (E5):** companion activation, the review-it fix, both gates, skip full suite, the
commit trailer check, push, closure, and the #370 handoff all followed implement-it's rules in the
main checkout. There was no coordination residue.

**Decision provenance:** Skill-prescribed; Human decisions at the gates.

**Existing owner:** implement-it, with review-it for the review. **Recurrence:** repeated.
**Execution shape:** both. **Extraction:** keep in specialist.

### C6: Worker briefing

The brief tells each worker its issue boundary, base commit, the state to hold at, what it may not
do, and which coordination notes to honor.

**Observed evidence (E1, E6, E7, E8):**
- The parent wrote every brief.
- Errors in the briefs:
  - a false claim about the base commit (E6);
  - an instruction to symlink `vendor`, which broke autoloading (E6, E7).
- Only in E8 did the brief carry the earlier lessons, after they were written to memory.
- Workers hadn't seen the other workers' scopes or the gates already decided, so each brief supplied
  that.

**Decision provenance:**
- No skill policy covers the brief. `review-gates.md` defines the hold state ("ready for combined
  verification"), and the parent copied it into briefs.
- The content was Parent-originated.

**Existing owner:** none; cross-worker. **Recurrence:** repeated across materially different
situations. **Execution shape:** parallel-specific horizontal. **Extraction:** candidate Control Room
responsibility. The environment part of the brief belongs under runtime (C16).

### C7: Worker identity, progress vs candidate-ready, asynchronous arrival

**Observed evidence (E6, E7, E8):**
- The parent mapped agent ID → issue → worktree by hand. E7 had four agent IDs for two issues.
- "Holding" meant the worker's session ended and was later resumed with SendMessage (E6). One
  completion notice arrived twice (E6).
- In E8 the human asked "how is #369 going?". The parent could only see the worktree diff (64 files),
  not whether the worker was verifying, reviewing or ready.

**Decision provenance:**
- Notifications are Runtime-determined.
- Interpreting them was Parent-originated judgment.
- The "ready" definition is Skill-prescribed (`review-gates.md`).

**Existing owner:** Claude Code/runtime for the mechanics; interpretation cross-worker.
**Recurrence:** repeated. **Execution shape:** parallel-specific. **Extraction:** candidate Control
Room responsibility (interpretation), plus a runtime capability dependency.

### C8: Routing worker-surfaced decisions to the human

**Observed evidence:**
- Workers never asked the human directly. They put decisions in their reports:
  - the #373 label (E6);
  - the #363 and #358 scope questions (E6);
  - the need to re-seed (E8).
- In E1 two workers made the per-issue full-suite decision themselves and went to Gate 1 early. The
  parent corrected them.

**Decision provenance:**
- Who decides is Skill-prescribed (`verification.md`: one decision for the wave).
- Routing was Parent-originated.
- The answers were Human decisions.

**Existing owner:** cross-worker. **Recurrence:** repeated. **Execution shape:** parallel-specific.
**Extraction:** candidate Control Room responsibility.

### C9: Combined-candidate assembly

This means assembling all workers' changes into one tree for verification.

**Observed evidence (E1, E6, E7, E8):**
- The parent assembled it every time: a detached worktree at the milestone tip, with each worker's
  patch applied.
- The situations differed: no overlap (E6, E8), a conflict (E7), and a pre-v2.2.0 methodology (E1).
- `verification.md` says it "does not specify how, when, or by whom the combined candidate state is
  assembled".

**Decision provenance:**
- Whether to verify the combined state is Skill-prescribed (the wave-level decision).
- The assembly itself was Parent-originated.
- The method converged across waves through Parent-originated repetition, not through a rule.

**Existing owner:** unresolved, explicitly left open by implement-it. **Recurrence:** repeated across
materially different situations. **Execution shape:** parallel-specific. **Extraction:** candidate
Control Room responsibility.

### C10: Wave-level full-suite decision

**Observed evidence:** the human chose "run" in E1, E6, E7 and E8.

**Decision provenance:** Skill-prescribed → Parent-applied; Human decision.

**Existing owner:** implement-it (the policy). **Recurrence:** repeated. **Execution shape:**
parallel-specific instance of a policy that applies to both shapes. **Extraction:** keep in
specialist. Only where it runs depends on C9.

### C11: Reconciling overlapping edits

**Observed evidence (E7 only):**
- The parent hand-wrote a `routes/members.php` line that existed in neither worker's tree. No worker
  was consulted.
- It was tested but never reviewed by review-it.
- The Gate 1 note didn't say outright that review-it hadn't covered it.

**Decision provenance:**
- No skill policy covers it.
- It was Parent-originated.
- The human's Gate 1 approval covered it only implicitly.

**Existing owner:** unresolved. **Recurrence:** one occurrence. **Execution shape:**
parallel-specific. **Extraction:** insufficient evidence.

### C12: Review validity after the parent or a later change alters reviewed state

**Observed evidence:**
- **E7:** the reconciled line was never reviewed.
- **E6:** the #373 relabel wasn't re-reviewed; the worker judged the earlier result still held.
- **E8:** no change was made after review.

**Decision provenance:**
- The policy is Skill-prescribed: `review-gates.md`'s approval-validity rule ("a material change
  requires the affected review and approval to be renewed").
- Applying it to code that lives outside every worker's reviewed tree has no owner. It was
  Parent-originated or skipped.

**Existing owner:** implement-it (the policy); its application across workers is unresolved.
**Recurrence:** repeated (2 times). **Execution shape:** parallel-specific. **Extraction:**
insufficient evidence on ownership. The gap itself is real.

### C13: Composing per-issue gates into one decision surface for the human

**Observed evidence:**
- Gates were per issue by rule, but the parent always presented them together:
  - E6: one question per issue;
  - E7: two blocks;
  - E8: one table.
- The human approved them together every time.
- The "Code surface" preference (preserved retrospectively; see the evidence limits above) isn't met
  by any rule. In E8, the Gate 1 table grouped scope by issue but had no such view.

**Decision provenance:**
- The semantics are Skill-prescribed (`review-gates.md`).
- The presentation was Parent-originated.

**Existing owner:** implement-it (the gate); composition cross-worker. **Recurrence:** repeated.
**Execution shape:** parallel-specific for aggregation. The Code-surface preference would apply to
both shapes. **Extraction:** candidate Control Room responsibility, limited to human-facing
composition.

### C14: Convergence (commit location, merge order and mechanics)

**Observed evidence:**
- **Where commits were built:**
  - E6: the workers built them;
  - E7 and E8: the parent built them inside the workers' worktrees.
- **Merges** were always made by the parent in the main checkout with `--no-ff`.
- **Merge order:**
  - E1: the human chose it;
  - E6: the parent attempted all four merges without asking and was blocked by the classifier;
  - E7 and E8: stated in the commit plan and approved.
- **Trap:** a `# Conflicts:` message left in a merge commit (E7).

**Decision provenance:**
- `sequencing.md` calls convergence "normal mechanical progression" but "does not define how".
- The mechanics and the order were Parent-originated.
- Authorization was a Human decision, bundled into Gate 2 in E7 and E8.

**Existing owner:** unresolved, left open by implement-it. **Recurrence:** repeated across materially
different situations. **Execution shape:** parallel-specific. **Extraction:** candidate Control Room
responsibility.

### C15: Final-tree equivalence

This means proving the merged tip's tree is the tree the full suite ran on.

**Observed evidence:**
- **E7, E8:** the parent compared `write-tree` of the combined candidate with `HEAD^{tree}` and got
  identical results. This is what let the combined suite result carry over to the final history.
- **E6:** only a chain of partial checks.
- **E1:** can't establish.

**Decision provenance:**
- No skill policy covers it. The closest is `verification.md`: "Assume a full-suite result still
  applies after relevant content … changes" is a listed Don't.
- It was Parent-originated.

**Existing owner:** none. **Recurrence:** repeated. **Execution shape:** parallel-specific.
**Extraction:** candidate Control Room responsibility.

### C16: Workspace provisioning and retirement

This covers creating, equipping and later removing worker worktrees and branches.

**Observed evidence:**
- **Provisioning:**
  - E6, E7: worktrees were auto-created from `main`, not the milestone branch;
  - E7, E8: worktrees were created by hand from the tip;
  - `vendor` had to be copied, not symlinked (E1, E6, E7);
  - Wayfinder `--with-form` needed in fresh worktrees (E6, E8);
  - `public/build` copied (E6).
- **Retirement:**
  - After E1 and E6, leftovers remained: 12 old worktrees and 22 runtime branches. The E1 merge also
    left a stale Vite manifest in the main checkout, which caused 11 false failures in E2.
  - In E7 and E8 cleanup happened only on the human's conditional authorization.

**Decision provenance:**
- Worktree mechanics are Runtime-determined.
- Environment needs are Project/stack-guided.
- The workarounds were Parent-originated.
- Cleanup was a Human decision.

**Existing owner:** runtime plus project knowledge; retirement unowned. **Recurrence:** repeated
across materially different situations. **Execution shape:** parallel-specific. **Extraction:**
candidate runtime capability/adapter responsibility. The decision to retire is a Control Room
candidate (see Ownership questions still open).

### C17: Push, closure and bundled tail approvals

**Observed evidence:**
- The human bundled the tail approvals three times:
  - "Push all three and close" (E1);
  - "approve, push and close both issues" (E7);
  - "push, close the issues and clean up" (E8).
- Push was denied by the permission classifier in E6 and E8.
- In E8, closure waited for push, per `push-readiness.md`, and cleanup went ahead on its own because
  the branches were merged locally.
- In E1, the parent closed the issues without following `issue-closure.md`, and the human later
  ordered a repair.

**Decision provenance:**
- The order is Skill-prescribed (`push-readiness.md` → `issue-closure.md`).
- Authorization was a Human decision.
- Splitting "cleanup doesn't depend on push" from "closure does" was a Parent-originated judgment
  (E8, once).

**Existing owner:** implement-it. **Recurrence:** repeated. **Execution shape:** both; batching across
issues is parallel-specific. **Extraction:** keep in specialist. Executing a partially failed bundle in
the right order is human-facing coordination.

### C18: Carrying runtime lessons from one wave to the next

**Observed evidence:**
- Carried from E7 to E8 through memory: the hand-made worktrees and the copied `vendor`. Both applied
  cleanly.
- Not carried: the Wayfinder `--with-form` trap. It was known in E6, and workers had to rediscover it
  in E8.
- The `vendor` symlink lesson from E1 wasn't carried into E6 or E7.

**Decision provenance:** memory writes were Parent-originated; the "evidence only" status was a Human
decision.

**Existing owner:** none; personal memory is doing it. **Recurrence:** repeated. **Execution shape:**
mainly parallel-specific. **Extraction:** unresolved; see Ownership questions still open.

## Vertical lifecycle coordination

**Owned by specialists, working as designed:**
- **lab-it:**
  - investigation;
  - grouping raw observations into scopes (E2: 5 scopes; E3: A–F);
  - challenging proposed solutions (E2 "Keep it" on `PolicySort`; E3 RadioChips vs RadioCard and
    type-to-search);
  - stopping for approval before Plan.
- **plan-it:**
  - drafting;
  - review passes;
  - metadata, including the assignee from history;
  - "Coordination (not a prerequisite)" lines;
  - checkpoints that create nothing before approval;
  - the handoff statement.
- **implement-it:** the zero-open handoff to ship-it (E1).
- **ship-it:** the readiness verdict and PR creation (E1).

**What the human owned:**
- Every transition between stages: Ship→Lab, Lab→Plan, Plan→create, Implement→Ship. The human wrote
  Ship→Lab and Lab→Plan in advance, in the prompt.
- The product and architecture decisions inside Lab (canonical subclasses, no migration, re-seed).

**What the parent coordinated (C1):**
- Cross-session and cross-stage orientation.
- Specifically, keeping state that no stage owns:
  - PR #357 open while issues were added to its milestone;
  - the uncommitted `plan.md` deletion;
  - evidence-only dispositions;
  - loose ends such as leftover worktrees and the stale build.
- **Lab → Plan context:** it lived only in the conversation, not in `plan.md`, in both E2 and E3.
  plan-it accepted conversation input, and its issue bodies became the durable record.

**Not observed:**
- Any automatic Ship→Lab routing.
- Any handling of "the milestone regained open issues after its PR was created". It happened
  (#358–#373 were added after PR #357), but no rule addressed it and nothing broke because of it.

## Single-issue coordination

The E5 single-issue lifecycle had no coordination residue inside the issue. implement-it and review-it
covered:
- activation and verification;
- both gates, commits, push and closure;
- the handoff and the recompute.

**What remained around it:**
1. **Session-entry orientation (C1).** Establishing where the lifecycle stands before invoking
   implement-it:
   - branch and milestone;
   - PR open;
   - uncommitted `plan.md`;
   - dispositions the human stated earlier.
2. **Continuity of sequencing intent.** Keeping the ordering strategy the human chose (bugs first,
   refactors first) across sessions so that recommendations don't flip on the same inputs
   (E4 → E5 → E6).
3. **Loading the right specialist.** In E4 the user-level v2.1.4 copy of implement-it overshadowed
   the project v2.2.0 copy, producing a wrong "no concurrency" claim. This is runtime/adapter, not
   coordination, but it happened at the point of entry.

Nothing else observed in single-issue work needs a coordinating layer.

## Horizontal execution coordination

Everything in this section is parallel-specific.

- **Worker briefing (C6):**
  - the issue boundary and the base commit;
  - the hold state;
  - what the worker may not do;
  - coordination notes from other issues.
- **Worker identity and state (C7):** mapping async completions to issues, and telling observable
  progress apart from candidate-ready.
- **Routing worker-surfaced decisions to the human (C8):** including stopping workers from making
  wave-level decisions (E1).
- **Combined-candidate assembly (C9):** explicitly left open by `verification.md`, and performed by
  the parent in all four waves.
- **Convergence execution and ordering (C14):** left open by `sequencing.md`.
- **Final-tree equivalence (C15):** this is what connects the wave-level verification to the
  published history.
- **Deciding when workspaces are retired (C16).** The mechanics are runtime; the decision was always
  the human's or undone.

**Parallel-specific but unresolved:** reconciliation authorship (C11) and review validity across
workers (C12).

**Not horizontal, although it touches several issues:**
- The wave-subset recommendation. `sequencing.md` already prescribes the overlap assessment.
- Per-issue gates, commit boundaries, and push/closure order. These are implement-it policy.
- Deferred-context propagation. `issue-closure.md` prescribes it. In E8 the parent put the #361/#365
  notes in #369's closing comment and offered to propagate them after closing, instead of asking
  before closing as the rule says. That's a single deviation, not an ownership gap.

## Runtime / adapter responsibilities

| Need | Portable capability need | Claude Code behavior observed | Laravel/useOrbit knowledge | Parent workaround used |
|---|---|---|---|---|
| Worker workspace on the right base | Create an isolated workspace from a named commit | `isolation:"worktree"` cut from `main` (E6, E7); unchanged ones auto-removed, deleting evidence (E7) | none | `git worktree add -b … <tip>`; worker base check (E7, E8) |
| Dependencies in the workspace | A workspace whose code, not the source checkout's, is what runs | none | Composer autoload resolves through a `vendor` symlink; `node_modules` symlink is fine; `.env` must be copied | `cp -R vendor`, link `node_modules`, copy `.env` |
| Generated and build state | Regenerate gitignored generated state per workspace, and refresh the target checkout after convergence | none | Wayfinder `--with-form` (`formVariants: true`); Vite manifest needed for Inertia tests (E2's 11 false failures) | Regenerate per worktree; `npm run build` |
| Shared Git state | Isolation from state shared across workspaces | Stash shared across worktrees (the runtime warned in E8) | none | Briefs say "no `git stash`" |
| Permissions | Pre-authorizing actions a human already approved | Classifier denied merges (E6) and pushes (E6, E8) even after human approval | none | Stop; the human ran `!` or asked for a retry |
| Worker resumption and notification | Resume a worker with its context; reliable completion signals | Workers end instead of holding; resumed by SendMessage; duplicate notice (E6) | none | Track by agent ID and worktree path |
| Workspace and branch retirement | Remove workspaces and runtime-created branches safely | 22 `worktree-agent-*` branches left behind (E6) | none | Safety checks (merged, clean, unlocked, empty stash), then `worktree remove` / `branch -d` |
| Lesson carryover | Durable, shared knowledge of environment traps | Personal memory only | Wayfinder and `vendor` traps are useOrbit/Laravel-specific | Memory evidence files; partial carryover (C18) |
| Skill resolution | Know which copy of a skill loaded | User scope overshadowed project scope (E4) | none | The human diagnosed it step by step |
| Shell quirks | Robust command construction | zsh didn't split an unquoted list variable into separate arguments (E3, E2, E8) | none | Retry with arrays |

## Specialist responsibilities that should stay put

- **Investigation, grouping, and challenging premature solutions.**
  - **Owner:** lab-it.
  - **Parent's part:** it only invoked it, on the human's prompt.
  - **Why keep it:** moving it up would duplicate lab-it's materiality test and evidence method.
- **Issue drafting, metadata, and coordination lines.**
  - **Owner:** plan-it.
  - **Why keep it:** plan-time coordination lines ("Coordination (not a prerequisite)") were the
    cross-issue signal every later wave used. They work where they are.
- **Ready set and execution-shape recommendation.**
  - **Owner:** implement-it `sequencing.md`.
  - **Parent's part:** it applied the rule; the human decided.
  - **Why keep it:** the rule already prescribes the overlap assessment and the stop that says a
    recommendation isn't authorization. Moving it would split dependency reading away from the issue
    convention it depends on.
- **Gate 1 and Gate 2 semantics, the approval-validity check, and the wave-level full-suite decision.**
  - **Owner:** implement-it `review-gates.md` and `verification.md`.
  - **Parent's part:** it presented them.
  - **Why keep it:** the gates define what an approval covers. Composing them for the human (C13)
    doesn't need to own them.
- **Commit boundaries, the trailer check, push-readiness, issue closure, and deferred-context
  propagation.**
  - **Owner:** implement-it.
  - **Evidence:** E8's commit reordering was `commit-boundaries.md` applied ("every intermediate state
    coherent"). It wasn't new coordination.
  - **Counter-evidence for moving it:** in E1 the parent closed issues without that rule and needed a
    repair. When lifecycle steps are executed outside the specialist, the specialist's policy is what
    gets skipped. That's an argument for keeping it put.
- **Review semantics.**
  - **Owner:** review-it.
  - **Parent's part:** it never ran review-it itself and only aggregated the workers' results.
  - **Why keep it:** nothing observed justifies moving review semantics up. The gap is *which tree
    gets reviewed* (C12), not *what a review is*.
- **Milestone PR readiness and PR creation.**
  - **Owner:** ship-it (E1).
  - **Parent's part:** it recognized the handoff by quoting implement-it's rule; the human authorized
    it.

## Ownership questions still open

- **Code the parent writes to reconcile conflicts (E7).**
  - **Known:** the parent authored a one-line composition in neither worker's tree, without consulting
    either worker. It was tested (418 targeted tests and the full suite) but not reviewed.
  - **Unanswered:** who should author a reconciliation, and whether it counts as part of either
    issue's reviewed scope. There is only one occurrence.
- **Review validity after reconciliation or relabel (E6, E7).**
  - **Known:** the approval-validity policy exists, and no one applied it to code outside the workers'
    reviewed trees.
  - **Unanswered:** whether a reconciled state needs its own review, and who invokes it.
- **Final-tree equivalence.**
  - **Known:** it was proved by tree hash in E7 and E8, and done less rigorously in E6. It is what
    justified reusing the combined suite as each issue's closure evidence.
  - **Unanswered:** whether it's required, or just good practice that happened to be done.
- **Workspace retirement.**
  - **Known:** without an explicit authorization, leftovers accumulated (E1, E6) and caused false
    failures (E2). With the human's conditional authorization, cleanup was safe (E7, E8).
  - **Unanswered:** whether retirement is part of convergence, a separate step the human approves, or a
    runtime default.
- **Generated state and environment preparation.**
  - **Known:** the needs are stack-specific (Composer autoload, Wayfinder form variants, the Vite
    manifest), and every wave had to rediscover or re-apply them.
  - **Unanswered:** whether a worker can safely prepare its own environment. In E7 one worker caught
    the symlink problem and the other didn't until corrected, so only in part. Also unanswered: who
    refreshes the target checkout after convergence (E1→E2).
- **Carrying runtime lessons across waves.**
  - **Known:** personal memory carried some lessons, not all. The human kept these as evidence, not
    rules.
  - **Unanswered:** where lessons that are durable but stack-specific should live, and who decides
    they're settled.
- **Holding versus finishing.**
  - **Known:** the "hold" state is a skill concept. At runtime a worker ends and is resumed.
  - **Unanswered:** whether "candidate-ready" can be observed from outside a worker without its
    report. E8's "how is #369 going?" could only be answered by inspecting its files.
- **Where merge authorization lives.**
  - **Known:** the rule says convergence is mechanical, yet the parent asked (E7, E8), didn't ask (E6),
    or the human decided the order (E1).
  - **Unanswered:** whether the human wants it as its own decision.

## Decision provenance map

| # | Decision | Policy owner | Situational decision-maker | Human authorization | Physical executor | Shape | Classification |
|---|---|---|---|---|---|---|---|
| 1 | E1: run #334/#344/#345 in parallel | implement-it (older version) | human | "Implement … in parallel" | parent → 3 workers | parallel | Human decision |
| 2 | E1: defer the convergence question | none | human | "not needed yet" | parent | parallel | Human decision |
| 3 | E1: workers must not make per-issue full-suite decisions | implement-it `verification.md` | parent (correction) | none | parent → workers | parallel | Skill-prescribed → Parent-applied |
| 4 | E1: assemble the combined candidate and run the suite | none (assembly) / implement-it (decision) | parent proposed, human chose | AskUserQuestion | parent | parallel | Parent-originated + Human decision |
| 5 | E1: merge order and timing | none | human | "Merge sequentially now" | parent | parallel | Human decision |
| 6 | E1: close issues (bypassing `issue-closure.md`) | implement-it | parent | "Push all three and close" | parent | both | Parent-originated (deviation); later human-ordered repair |
| 7 | E1: Implement → Ship | implement-it and ship-it | parent cited the rule | "Check if the milestone PR is ready" | parent via ship-it | lifecycle | Skill-prescribed → Parent-applied |
| 8 | E1: PR #357 readiness, draft, create | ship-it | ship-it | manual testing done; "create the PR without the attribution footer" | parent via ship-it | lifecycle | Skill-prescribed → Human decision |
| 9 | E2: route PR review into Lab → Plan | none | human | written into the prompt | parent via lab-it | lifecycle | Human decision |
| 10 | E2: 11 failures are environment-only (stale manifest) | lab-it (evidence) | lab-it | accepted | parent via lab-it | lifecycle | Skill-prescribed → Parent-applied |
| 11 | E2: challenge proposed solutions; pick scopes 1–5 | lab-it | lab-it; human decided | "Approve Scopes 1–5 …" | parent via lab-it | lifecycle | Skill-prescribed + Human decision |
| 12 | E2: create #358–#367 | plan-it | plan-it | two checkpoints; "create" | parent via plan-it | lifecycle | Skill-prescribed → Human decision |
| 13 | E2: recommend execution waves at plan time | none (outside plan-it's scope) | parent inside plan-it | none | parent | parallel | Parent-originated judgment |
| 14 | E3: route UI findings (Lab only where needed) | none | human | written into the prompt | parent via lab-it | lifecycle | Human decision |
| 15 | E3: canonical subclasses, no migration, controls | lab-it surfaces them | human | explicit lists | human | lifecycle | Human decision |
| 16 | E3: create #368–#373 | plan-it | plan-it | "Approved A–F", then "create" | parent via plan-it | lifecycle | Skill-prescribed → Human decision |
| 17 | E4: which skill copy is authoritative | none (runtime scope order) | human-driven diagnosis | removal and restore approved | parent | lifecycle | Runtime-determined + Human decision |
| 18 | E4/E5: next issue (#369 → #368 → #362) | implement-it `sequencing.md` | parent | "implement issue 368" | parent | single | Skill-prescribed → Parent-applied; Human decision |
| 19 | E5: #368 gates, full-suite skip, push, closure, #370 note | implement-it | implement-it / parent | each approved | parent | single | Skill-prescribed → Human decision |
| 20 | E6: consider a wave | implement-it allows it | human raised it | "consider an authorized parallel wave" | parent | parallel | Human decision |
| 21 | E6: subset #362/#358/#363/#373 | implement-it (overlap assessment) | parent | "launch the four-issue wave" | parent | parallel | Skill-prescribed → Parent-applied; Human decision |
| 22 | E6: worker briefs (wrong base claim, symlinked `vendor`) | none | parent | none | parent | parallel | Parent-originated judgment |
| 23 | E6: workers reset their own base | none | workers | none | workers | parallel | Worker-local judgment |
| 24 | E6: #373 label | none | human (via parent) | "keep Export" | worker | parallel | Human decision |
| 25 | E6: assembly method and the combined suite | none / implement-it | parent / human | "Run combined suite" | parent | parallel | Parent-originated + Human decision |
| 26 | E6: batched Gate 1 and Gate 2 | implement-it (per issue) | parent (presentation) | approved as a batch | parent | parallel | Skill-prescribed; presentation Parent-originated |
| 27 | E6: attempt merges without asking | `sequencing.md` ("mechanical", how undefined) | parent | blocked, then retried with human approval | parent | parallel | Parent-originated; Runtime-determined block |
| 28 | E6: mid-wave cleanup of old worktrees | none | human | "clean up the 13 old worktrees" | parent | parallel | Human decision |
| 29 | E7: overlapping pair #359/#360 against the recommendation | implement-it | human | "Run #359 and #360 concurrently" | parent | parallel | Human decision |
| 30 | E7: hand-made worktrees after runtime base failure | none | parent | none | parent | parallel | Runtime-determined → Parent-originated workaround |
| 31 | E7: `vendor` correction to #359 | none | parent (after #360 worker found it) | none | parent → worker | parallel | Worker-local finding → Parent-applied |
| 32 | E7: author the `routes/members.php` reconciliation | none | parent | implicit in Gate 1 | parent | parallel | Parent-originated judgment |
| 33 | E7: no review-it pass on the reconciliation | `review-gates.md` validity (unapplied) | parent (by omission) | none | none | parallel | Parent-originated (gap) |
| 34 | E7: Gate 2 combined with merge approval | implement-it / none | parent / human | "approve, create the commits and merge" | parent | parallel | Human decision |
| 35 | E7: final-tree equivalence | none | parent | none | parent | parallel | Parent-originated judgment |
| 36 | E7: conditional cleanup (4 safety checks) | none | human set the condition; parent set the checks | "only once they're confirmed safe" | parent | parallel | Human decision + Parent-originated |
| 37 | E8: proactive wave recommendation #369 + #372 + #364 | implement-it `sequencing.md` | parent | "run the … wave" | parent | parallel | Skill-prescribed → Parent-applied; Human decision |
| 38 | E8: provisioning from memory lessons | none (memory) | parent | none | parent | parallel | Parent-originated (carried lesson) |
| 39 | E8: Wayfinder `--with-form` rediscovered | project/stack | workers | none | workers | parallel | Project/stack-guided; Worker-local |
| 40 | E8: combined assembly (temporary index, no conflicts) and full suite | none / implement-it | parent / human | "Run it" | parent | parallel | Parent-originated + Human decision |
| 41 | E8: reorder #369 commits so each runtime state is coherent | implement-it `commit-boundaries.md` | parent | "approved, commit and merge" | parent | both | Skill-prescribed → Parent-applied |
| 42 | E8: per-commit verification reusing the combined worktree | `verification.md` (narrowest reliable check) | parent | none | parent | both | Skill-prescribed; method Parent-originated |
| 43 | E8: final-tree equivalence | none | parent | none | parent | parallel | Parent-originated judgment |
| 44 | E8: push | implement-it `push-readiness.md` | parent | "push, close … clean up"; denied, then the human pushed with `!` | human | both | Runtime-determined block → Human decision |
| 45 | E8: hold closure but do cleanup while the push was blocked | `push-readiness.md` (closure only) | parent | covered by the bundle | parent | parallel | Parent-originated judgment |
| 46 | E8: closure; #361/#365 notes in the comment instead of asking first | implement-it `issue-closure.md` | parent | bundle | parent | both | Skill-prescribed → Parent-applied (partial deviation) |

## Potential extraction from specialist skills

Extraction is not assumed to be desirable. Each row states the case for and against moving a
responsibility out of its current specialist.

| Specialist | Responsibility | Current owner (rule) | What the specialist decides | What the parent applies or executes | Evidence to reconsider | Shape | Needs context beyond specialist? | Strongest reason to keep | Lost or duplicated if moved | Case |
|---|---|---|---|---|---|---|---|---|---|---|
| lab-it | Proceeding to Plan after approval | lab-it SKILL "Ownership and handoff" + `plan-synthesis.md` | when decisions are resolved | invoking plan-it | The human scripted Lab→Plan themselves (E2, E3) | lifecycle | No | The materiality test is lab-it's | lab-it's stop-for-approval contract | unsupported |
| lab-it | Routing guide work to document-it | lab-it SKILL | the route | none observed | none (never exercised) | lifecycle | none | not exercised | none | unsupported |
| plan-it | Handing off to implement-it and ship-it | plan-it "Handoff" | end of its own responsibility | none | none | lifecycle | No | It only declares its own boundary | nothing | unsupported |
| plan-it | Recommending execution waves at plan time (observed, not in any rule) | none (outside plan-it's scope) | none by rule | parent-originated inside plan-it (E2) | Once; `sequencing.md` owns it later | parallel | Yes (execution state) | It isn't plan-it policy at all | risk of two sources of execution-shape advice | weak (as a problem to remove, not something to extract) |
| plan-it | Routing unresolved material decisions "to owning gate" | `discovered-work.md` | stop drafting | none observed | not exercised | lifecycle | maybe | not exercised | none | unsupported |
| implement-it | Milestone ready-set recompute and execution-shape recommendation | `sequencing.md` | ready set, recommendation, no chaining | presentation | Recommendations flipped across sessions (E4–E6), because sequencing intent wasn't persisted | both | Yes (cross-session intent) | Dependency reading is tied to the issue convention; the rule worked each time | the tie to issue conventions and "recommendation ≠ authorization" | weak (the gap is C1 orientation, not the rule) |
| implement-it | Parallel-worker branch policy and "convergence is mechanical" | `sequencing.md` "Parallel workers" | per-worker branch from the milestone branch; stop only on unsafe convergence | all convergence mechanics | The rule itself leaves convergence open; the parent filled it in 4 waves | parallel | Yes (all workers) | The branch-base requirement is part of issue branch readiness | an issue-local skill holding cross-worker policy | plausible |
| implement-it | Wave-level combined-verification decision | `verification.md` "Concurrent workers" | one run/skip decision per wave; Gate 1 evidence | assembly, running, reuse at closure | Assembly explicitly left open; performed by the parent 4 times | parallel | Yes | The decision defines Gate 1 evidence per issue | Gate 1's evidence contract | weak for the decision; plausible for assembly (never in the skill) |
| implement-it | Worker hold state ("ready for combined verification") | `review-gates.md` | where a worker stops | briefing it, detecting it | Runtime ends workers instead of holding them (E6, E7) | parallel | Yes | It is part of the gate's definition | gate semantics | weak |
| implement-it | Approval validity after change | `review-gates.md` | a material change renews the review | not applied to reconciled code (E7) | Parent-authored code sits outside every worker's scope | parallel | Yes | The policy is correct as written | nothing; what's missing is applying it | weak |
| implement-it | Deferred-context propagation | `issue-closure.md` | ask, then update the later issue | executed (E5, E6); partial in E8 | Crosses issues, but at closure time | both | Slightly | Closure knows what was deferred | the closing-comment/propagation link | weak |
| implement-it | Handing off to ship-it at zero open issues | `sequencing.md` "When the ready set is empty" | recognizing zero open vs all blocked | citing it (E1) | worked (E1) | lifecycle | No | ship-it re-checks independently anyway | nothing | unsupported |
| review-it | Review of whatever state is passed in | review-it SKILL / `scope.md` | findings, clean result, limitations | aggregation | Parent-authored reconciliation was never passed to it (E7) | parallel | The *choice of target* does; the semantics don't | review-it is target-agnostic by design | independent review semantics | unsupported (semantics); the target choice is C12 |
| ship-it | PR readiness and creation; CI correction handoff | ship-it SKILL, `milestone-pr-readiness.md`, `ci-failure-correction.md` | readiness verdict; correction scope | invoking it (E1) | PR review findings went to Lab by the human's prompt, not via ship-it; the milestone regained issues after its PR existed | lifecycle | Yes (post-PR discovered work) | ship-it correctly doesn't decide what work should exist | none observed | insufficient evidence |

document-it and steward-it are not audited here: Phase 26 never exercised either one, so there is no
evidence for or against a coordination role for them.

## V2.3 extraction residue

After removing what specialists, individual workers, the runtime, project knowledge and the human
already own, this is what's left. It is the smallest set the evidence supports, not a design.

**1. Vertical lifecycle coordination (applies whether implementation is serial or parallel)**
- **Lifecycle-position orientation across sessions and stages.** Knowing and preserving where the work
  stands, including state no specialist or GitHub query holds:
  - an open milestone PR while issues are still being added to its milestone;
  - uncommitted working-tree dispositions;
  - the human's standing dispositions ("evidence only", "don't merge");
  - unresolved loose ends from earlier stages.

  Evidence: repeated in every session from E2 to E8. Nothing else in the residue is as well evidenced.

**2. Single-issue coordination**
- **Session-entry orientation**, the same responsibility as above, before a specialist is invoked.
- **Continuity of the human's chosen sequencing intent across sessions.** Evidence: the flip-flopping
  recommendations in E4–E6.
- Nothing inside the single-issue lifecycle itself; E5 shows implement-it covers it.

**3. Horizontal execution coordination (parallel-specific)**
- Briefing each worker with its issue boundary, base and hold contract.
- Tracking worker identity and state through to candidate-ready.
- Routing worker-surfaced decisions to the human, including keeping wave-level decisions away from
  workers.
- Assembling and verifying the combined candidate. implement-it explicitly leaves this open.
- Convergence execution and ordering, plus final-tree equivalence between the verified state and the
  published history.

Each of these was repeated across E1, E6, E7 and E8, in materially different situations: no overlap,
deliberate overlap, and an older methodology version.

**4. Human-facing coordination**
- Composing the specialists' per-issue evidence into one decision surface without changing what each
  gate means. The human approved every batched presentation, and has stated (retrospectively; see the
  evidence limits) a preference for a "Code surface" view grouped by responsibility.
- Keeping the human's decision state straight: what's approved, what's pending, and what's bundled.
  That includes carrying out a bundled approval in the correct dependency order when one step fails
  (E8: push blocked, closure held, cleanup went ahead).

**Excluded from the residue:**
- **Too little evidence:** conflict-reconciliation authorship, review validity across workers, and
  workspace retirement.
- **Runtime/adapter capabilities, not coordination:** environment and generated-state preparation, and
  carrying lessons across waves. They're listed under Ownership questions still open and Runtime /
  adapter responsibilities.
