# my-git-workflow — Methodology Architecture Review

Status: Complete
Scope: Canonical my-git-workflow methodology
Purpose: Supporting evidence for methodology architecture and future refinement

> This document is supporting evidence produced by a methodology-architecture review pass. It is
> not the source of truth for the methodology itself — the current `my-git-workflow` skill files
> (`SKILL.md`, `README.md`, `rules/*.md`) remain authoritative. Where this document's findings and
> the live skill files diverge in the future, the live skill files win; this document records the
> reasoning and open questions from the review that produced it, at the time it was produced.

---

Scope: analysis only, no files modified. Reviewed at `agentic-engineering@main`, current `rules/*.md` content (post-authoring-pass, commits `04d6c3d`…`0537e7b`). The `skill-audits/my-git-workflow-portability.md` document was read as historical evidence only — its target commit (`4b759cc`) predates the current rule text and its findings are **not** treated as authority here. Where relevant I note that its findings were resolved by the later rewrite.

## 1. Executive verdict

**The seven-rule architecture is coherent and should remain intact.** No rule's *reasoning* duplicates another's, no rule is structurally misplaced, and the human-control and verification models are each internally sound. The methodology is unusually disciplined about non-conflation: every adjacent gate explicitly states that the one doesn't imply the other (Gate 1 ≠ Gate 2 ≠ closure ≠ release approval ≠ milestone approval; zero-open-issues ≠ release-validated ≠ milestone-complete).

What's actually wrong is smaller and more specific than "structure": (a) one stale cross-file summary (the flagged `verification.md` case, confirmed, plus two siblings of it), (b) one misattributed cross-reference between `review-gates.md` and `commit-boundaries.md`, (c) one unverified cross-skill claim (issue reopening), and (d) one substantive, previously-unexamined methodology question: whether requiring full-project-scope lint/format/static checks at the broad verification boundaries is itself an overgeneralization for projects that carry pre-existing lint/static debt. None of these warrant restructuring; they warrant sentence-level correction, which this pass reports but does not perform.

The one real architectural *seam* — not a defect — is the PR-creation/merge boundary. It is honestly and consistently declared as out of scope everywhere it touches (`README.md`'s Known Limitations, `release.md`'s "what this rule does not do," `SKILL.md`'s "what it does not own"). But it does create one concrete, unowned exposure: this workflow's own lifecycle closes the GitHub issue *before* a PR merges, and nothing in either `my-git-workflow` or `my-feature-planning` owns what happens if that PR is later abandoned or materially revised.

## 2. Reconstructed end-to-end lifecycle

```
[my-feature-planning: approved, dependency-ready GitHub issue]
        │
        ▼
implement approved scope
        │
        ▼
verification.md — full-project lint/format/static + full regression suite   (pre-Gate-1)
        │
        ▼
review-gates.md — Gate 1: implementation review ── STOP, human approves
        │
        ▼
commit-boundaries.md — inspect diff, derive semantic commit plan
        │
        ▼
review-gates.md — Gate 2: commit-plan review ── STOP, human approves
        │
        ▼
commit-boundaries.md + verification.md — build commits;
   narrowest-reliable verification per commit; isolation verification
   (escalation only) when an intermediate committed state itself needs proof
        │
        ▼
verification.md — full-project lint/format/static + full regression suite  (completed-issue boundary)
        │
        ▼
issue-closure.md — ask first ── (if yes) checklist/comment/close/validate
        │
        ▼
sequencing.md — recompute dependency-ready set, report, recommend ── human picks next issue
        │
        ▼
        ⚠ UNOWNED SEAM: PR creation, review, merge ⚠
        │
        ▼
release.md — [trigger: PR merged] discover policy → draft → STOP, approve → publish → validate
        │
        ▼
milestone-completion.md — [trigger: release validated] 3-condition gate → STOP, approve → close
```

**Missing transition (the one real gap):** nothing produces the event `release.md` waits on ("a PR merged"). `commit-boundaries.md` ends at "commits exist"; `release.md` begins at "PR merged." No rule pushes a branch, opens a PR, or merges one. This is *declared*, not hidden — every file that touches this boundary says so explicitly, and `README.md`'s "Known limitations" names it outright, with an explicit instruction not to generalize from the single branch-naming data point available. **Judgment:** this is the correct posture given the skill's own extraction discipline ("watch what actually happens... say so explicitly when the evidence isn't there yet") — inventing PR/merge methodology now would be exactly the kind of unevidenced generalization the skill elsewhere refuses to make. I am not proposing to fill it.

**Implicit assumption worth surfacing (Fact + Inference):** the working lifecycle's own diagram order — `issue closure → PR merge → release` (`milestone-completion.md`'s own diagram) — combined with `issue-closure.md`'s trigger ("once a committed... issue has passed verification," i.e., at the completed-issue boundary, *before* any PR/merge step) means **an issue can be marked `CLOSED` on GitHub while its implementing commits are not yet merged to the trunk branch, and may not even be pushed anywhere yet.** Nothing in either skill addresses what happens if that PR is later rejected, squashed differently, or abandoned. `issue-closure.md` explicitly disclaims "does not create or reopen issues — that's `my-feature-planning`'s territory" (line 108/123), but `my-feature-planning` **never claims that responsibility anywhere** (verified by grep across both skills — the only "reopen" hits are an unrelated design-decision sense and this one disclaimer). **This is the one genuinely unowned lifecycle state in the pipeline**: post-closure, pre-merge issue invalidation. It is low-probability in a disciplined solo workflow (closure only happens after the completed-issue full suite is green, and commits already exist), but it is real and currently has zero rule ownership on either side.

**Duplicated ownership:** none found. Every place two rules touch the same topic (see §4) is composition, not duplication.

**Lifecycle states with no clear owner, in full:**
1. Push / branch management between "commits exist" and "PR merged" (subsumed under the declared PR gap, but not itself named in Known Limitations — minor).
2. PR creation, review, merge (explicitly, consistently declared out of scope — coherent, not a defect).
3. Reopening a closed issue if its PR doesn't land as approved (unowned on both sides — see above).
4. What happens when the human declines milestone closure despite all three gate conditions holding — `milestone-completion.md` doesn't state a "don't re-ask unprompted" behavior the way `issue-closure.md` does for a declined close. Minor asymmetry, not a contradiction (the gate is explicitly re-checked "fresh" every time regardless), but worth noting since the two gates are otherwise structurally parallel.

## 3. Rule-by-rule responsibility map

| Rule | Owns | Explicitly disclaims |
|---|---|---|
| `review-gates.md` | The approval-boundary *procedure*: when to stop, what Gate 1/Gate 2 each require, the standing "genuine unknown" escalation rule that can fire anywhere. | The substance of verification scope, commit-splitting logic, sequencing choice — it composes those from the other rules. |
| `commit-boundaries.md` | Commit-decomposition semantics: what makes a decision coherent, the derivation procedure, message content, `Refs #N`, test-*placement* per commit, correction-folding. | Verification execution/scope, review-gate procedure, issue closure. |
| `verification.md` | Verification *scope* at each lifecycle boundary (full / narrowest-reliable / isolation-escalation), and activation-risk commit ordering. | Commit boundaries, the gate-reporting mechanism. |
| `issue-closure.md` | Whether/when to ask about closing, the four-part closure recipe, post-mutation validation of the closure itself. | Deciding closure (human's call), issue creation/reopening (asserted, not verified — see §5), anything beyond the one just-delivered issue. |
| `sequencing.md` | Recomputing dependency-readiness after a validated closure, reporting the graph, recommending — never choosing or chaining. | Dependency *representation* (my-feature-planning's), redesigning the graph, starting the next issue. |
| `release.md` | Release-policy discovery, drafting at release altitude, the publish-approval gate, publishing, post-publication validation. | Issue closure, PR creation/merge, milestone closure, invented deployment/rollback/changelog machinery. |
| `milestone-completion.md` | The three-condition closure gate (delivery/phase only), the Backlog exemption, the closure mutation and its validation. | Milestone scope/description/naming (my-feature-planning's), release drafting/publication. |

Each file's "what this rule does not do" section is internally consistent with what the other six actually claim — I checked every cross-disclaimer against the file it points to and found no case where a disclaimed responsibility is actually unclaimed by anyone (mostly), or claimed by two files at once.

## 4. Cross-rule overlap/conflict analysis (Q2)

No duplicated *authority* found. The three files divide the same broad territory cleanly by *question asked*, not by *artifact touched*:

- **Verification timing** → `verification.md` exclusively (pre-Gate-1, per-commit, isolation, completed-issue).
- **Test placement** (which commit a test lands in) → `commit-boundaries.md`'s "Tests travel with the decision." **Test scope** (what gets run, how broadly) → `verification.md`. Genuinely different questions about the same word ("tests"), correctly split.
- **Commit ordering** → split by *reason*, not duplicated: `commit-boundaries.md` orders by structural dependency (step 6 of its derivation procedure); `verification.md` layers activation-risk ordering on top (its own dedicated section). Neither rule discusses what happens if the two orderings conflict — a real but narrow open question, not evidence of duplicated authority.
- **Commit-plan contents** → `review-gates.md` specifies what Gate 2 must *report*; `commit-boundaries.md`/`verification.md` supply the substance being reported. One concrete defect here (see §9, finding 2): `review-gates.md` line 53 cites `rules/verification.md` for "which tests travel with which commit," but that rule actually lives in `commit-boundaries.md`.
- **Isolation-verification decision** → `verification.md` alone, cleanly; `commit-boundaries.md` never weighs in on when to escalate.

**Verdict:** the three-way split is healthy composition. The one real defect is a wrong citation, not duplicated methodology.

## 5. `my-feature-planning` contract analysis (Q7)

Verified directly against `my-feature-planning/SKILL.md`, `rules/issue-conventions.md`, `rules/sequencing.md`, `rules/review.md`, `rules/discovered-work.md`, `rules/feature-classification.md`.

| Assumption in `my-git-workflow` | Classification | Evidence |
|---|---|---|
| Approved issue is the input; planning's job ends at creation | **Legitimate contract, bidirectional** | `my-feature-planning/SKILL.md` step 18: "Planning's responsibility ends at issue creation... load [implementation skills] when work on an approved issue actually begins." Matches `my-git-workflow`'s own framing exactly. |
| Milestone naming/description convention is planning's | **Legitimate contract, bidirectional** | `issue-conventions.md`'s "Milestone rules"/"Milestone descriptions" sections explicitly state: "Milestone closure is not decided here... (`my-git-workflow`'s `rules/milestone-completion.md` owns that gate)." This is the strongest, most explicitly two-sided contract in the pipeline — each skill names the other correctly. |
| Dependency representation (syntax, e.g. `Depends on #N`) is planning's | **Legitimate contract, matched** | `issue-conventions.md`'s "Reference syntax" section defines it; `my-git-workflow/sequencing.md` explicitly says it "only reads and evaluates the resulting graph... does not redesign or invent one." |
| Issue *creation* is planning's | **Legitimate contract, matched** | `my-feature-planning/SKILL.md` steps 15–17 (`gh issue create`, dependency mapping, post-mutation validation) are exactly this. |
| Issue *reopening* is planning's | **Unverified / one-sided assumption** | `my-git-workflow/rules/issue-closure.md` asserts this twice ("that's `my-feature-planning`'s territory") but `my-feature-planning` never states ownership of reopening anywhere. Not stale (nothing changed), not duplicated (no one else claims it either) — simply an assertion the other side never makes. Low severity: reopening naturally clusters with creation as a GitHub-issue-lifecycle mutation, so the *inference* is reasonable, but it is currently presented as settled fact rather than flagged as an inference. |
| Milestone scope ownership (what belongs in a milestone) is planning's | **Legitimate contract, matched** | `milestone-completion.md`'s own "Cross-rule dependencies" section states this is consumed, not decided, and cites the right file. |

Four of five examined contracts are unusually well-matched, explicit, and bidirectional — a genuine strength of this pipeline, not a coincidence. One (reopening) is a plausible but currently unverified inference.

## 6. Human-control / gate analysis (Q8)

Seven decision points, mapped to what each uniquely protects:

1. **Genuine-unknown escalation** (standing rule, not a fixed checkpoint) — protects against silently resolving a missing product/architecture decision, anywhere in implementation or either gate.
2. **Gate 1** — protects "is the implementation/approach correct," before any commit history exists.
3. **Gate 2** — protects "is *this* historical decomposition acceptable," independent of #2 (same diff, multiple defensible splits — the file's own justification for keeping them separate holds up).
4. **Issue-closure ask** — protects "is this issue done enough to mark closed," independent of #2/#3 (commits can be correct and well-split while closure is still legitimately deferred, e.g. pending manual QA).
5. **Sequencing choice** (only when genuinely comparable options exist) — protects "which unit of work next," using delivery-time information (what the closure just unblocked).
6. **Release-content approval** — protects "what gets communicated as shipped, under what version," explicitly stated as not satisfied by the PR merge itself.
7. **Milestone-closure approval** — protects "is this bounded scope actually done," gated on three independently-checked conditions.

**No redundant or logically collapsible gates found.** The files are unusually explicit about non-implication between adjacent gates (direct quotes: "approval at Gate 1 does not imply approval at Gate 2," "a merged PR is not publication approval," "Zero open issues ≠ milestone complete. Release validated ≠ milestone complete."). This explicit anti-conflation, repeated at every boundary, is a coherent design pattern, not incidental repetition.

**Minor asymmetry (Fact):** `issue-closure.md` states what happens when the human declines closure ("don't ask again unprompted"); `milestone-completion.md` states no analogous behavior for a declined milestone-closure approval. Likely harmless given the gate is re-checked from scratch every time regardless, but it's an inconsistency between two structurally parallel gates worth naming.

## 7. Verification-model analysis (Q9)

The four scopes — pre-Gate-1 full, per-commit narrowest-reliable, isolation escalation, completed-issue full — are each independently justified:

- **Pre-Gate-1 full vs. completed-issue full** are explicitly argued as non-duplicate (prove "the working tree" vs. "the reconstructed history"). This reasoning is sound and I found no counter-evidence.
- **Per-commit narrowest-reliable** is the refined, load-bearing generalization the task flagged as newly written — it correctly extends "targeted" beyond tests to formatting/lint/static analysis, with an explicit, sensible fallback ("fall back to the broader mode when scoping isn't reliable, and that's correct, not a compromise"). This is a genuine methodological improvement over a cruder "always run everything" policy.
- **Isolation verification** is correctly scoped as a deliberate, expensive escalation with named trigger conditions, not the default — no overgeneralization found here.

**The specific challenge — is full-project lint/format/static-check scope at the broad boundaries genuinely methodology or an overgeneralization:**

**Fact:** `verification.md` requires *full-project-scope* formatting/lint/static checks (not scoped to the diff) at both the pre-Gate-1 and completed-issue boundaries, and again inside the isolation-verification loop per commit. The rule gives no treatment for a full-project lint/static run that surfaces pre-existing, unrelated violations.

**Judgment:** this is well-justified for the **regression test suite** — "did I break something that was passing" is a naturally binary, meaningful signal at full-project scope regardless of the codebase's history. It is **more questionable for lint/format/static-analysis specifically**, where many real codebases carry a pre-existing baseline of violations unrelated to any given change (legacy debt, suppressed warnings, incremental adoption of a linter). The rule's own "Discover the project's verification tools" section asks *what tool* and *what scoping capability* exists, but never asks whether "the whole project currently passes this check" is even a meaningful, currently-true baseline for this project. Running a full-project static check at a broad boundary and getting pre-existing, unrelated red is a real, foreseeable outcome the rule doesn't address — unlike the regression-suite case, where "was this already red before I touched it" is directly checkable (stash/diff against trunk) and the rule's careful commit-ordering section shows exactly this kind of before/after discipline being applied elsewhere.

**Open question:** should the broad-boundary full-project static/lint requirement carry the same "pre-existing failures are a different signal than newly introduced ones" discipline the rule already applies to activation-gated tests, or is "the project's static checks are meant to be all-green at all times" itself a legitimate baseline this rule is entitled to assume once discovered? This is exactly the kind of question that needs real-project evidence (does a lint-debt-carrying project ever actually run this workflow?) rather than a decision made in this pass — reported per the task's instruction, not resolved.

## 8. Post-merge / release / milestone analysis (Q5)

Both files are coherent continuations of the same substrate-ownership logic the skill states up front ("Git and GitHub are intentional core substrate for this methodology, not an abstraction to be swapped out"). A release (tag + hosted release) and a milestone closure are both Git/GitHub artifacts, exactly like a commit or an issue closure — there is no other skill in the pipeline that would sensibly own them (`my-feature-planning` explicitly stops at issue creation; no third "release" skill exists anywhere in the pipeline). By elimination and by the skill's own stated scope, they belong here.

The PR-creation/merge hole discussed in §2 is the one place this otherwise-coherent post-merge lifecycle touches an explicitly unowned gap — but as argued there, that gap is honestly modeled, not smoothed over, and filling it now would violate the skill's own evidence-extraction discipline. It is reported prominently, per the task's instruction, without proposing to fill it.

## 9. Cross-file coherence / stale-reference findings (Q10)

1. **Confirmed (the given candidate), and found in three places, not one.** `SKILL.md`'s rule index still summarizes `verification.md` as "targeted tests per commit" — narrower than the canonical rule, which is titled "narrowest reliable scope per commit" and explicitly generalizes beyond tests to "code-quality/static checks alike." The same narrower phrasing recurs in `README.md` (three separate spots: "verify (targeted + one full-suite pass)," "targeted verification per commit," "Verification is targeted per commit") **and inside `verification.md`'s own top-of-file lifecycle diagram** (line 19: "targeted verification per commit"), even though the file's own body (line 70 onward) has been refined to the broader principle. The drift is strongest between the file's opening diagram and its own later section — the top-level docs inherited the older framing consistently from there.

2. **New finding.** `review-gates.md` line 53 attributes "which tests travel with which commit, and why any commit is intentionally test-free" to `rules/verification.md`. That rule is actually defined in `commit-boundaries.md`'s "Tests travel with the decision" section. `verification.md` is only the correct citation for the negative-proof mechanism ("the full suite stays exactly as green as it was") that `commit-boundaries.md` itself cites separately — the primary rule being pointed at lives in the other file.

3. **Positive finding, confirming the authoring pass worked.** Two defects flagged by the historical portability audit no longer exist in the current text: `review-gates.md` no longer names "Pint" (grepped clean across all seven rules — no Laravel/Pest/Fortify/Pint terms remain anywhere in the skill), and `milestone-completion.md`'s definition of "delivery/phase milestone" is now cleanly generalized ("that's about scope and intent, not naming syntax") with the project-specific naming convention correctly delegated to `my-feature-planning` rather than embedded in the definition. `sequencing.md`'s ambiguous "this project" phrasing is likewise gone, replaced with a fully generic statement. The rewrite genuinely fixed what it set out to fix.

4. **Minor.** `milestone-completion.md` doesn't restate "don't re-ask unprompted" for a declined closure the way `issue-closure.md` does (see §6).

No other stale links, terminology drift, or ownership-claim mismatches were found on a full independent re-read of `SKILL.md`, `README.md`, and all seven rules against each other.

## 10. Structural disposition table

| Rule | Disposition | Basis |
|---|---|---|
| `review-gates.md` | **Keep as-is** | Distinct, non-duplicated human-control responsibility; one wrong citation to fix (§9.2), not a structural issue. |
| `commit-boundaries.md` | **Keep as-is** | No overlap or duplication found with either sibling. |
| `verification.md` | **Keep as-is** | Methodology sound and internally justified (§7); needs a wording refresh at its own top-of-file diagram, not restructuring. |
| `issue-closure.md` | **Keep as-is; clarify one claim** | Belongs in delivery per Q3 (trigger, durable record, and content all derive from committed/verified implementation, which planning has no access to). The "reopening is planning's territory" clause should be softened to an inference or verified with planning, not restructured away. |
| `sequencing.md` | **Keep as-is** | Belongs in delivery per Q4 — it observes graph state changed by an event this skill itself just caused, never redesigns the graph. Optional, non-warranted cosmetic note: it shares a filename with `my-feature-planning/rules/sequencing.md`, a different responsibility (planning-time batch ordering vs. delivery-time ready-set recalculation) — harmless in practice since references are skill-relative, worth knowing for cross-skill audits like this one. |
| `release.md` | **Keep as-is** | Coherent continuation of Git/GitHub substrate ownership; still the cleanest file in the skill. |
| `milestone-completion.md` | **Keep as-is** | Coherent terminal step of the same ownership logic; the historical audit's definitional wording defect is already fixed. |

**No merge, split, rename, move, or retirement is warranted by current evidence for any of the seven rules.**

## 11. Concrete methodology changes actually warranted now

These are the only changes this pass finds evidence for — all sentence/citation-level, none structural:

1. Reconcile `verification.md`'s own top-of-file lifecycle diagram (and its echoes in `SKILL.md`/`README.md`) with its refined "narrowest reliable verification scope" principle so the summary doesn't undersell the canonical rule as test-only.
2. Fix `review-gates.md` line 53's citation from `rules/verification.md` to `rules/commit-boundaries.md` for "which tests travel with which commit."
3. Either verify with `my-feature-planning` that issue-reopening is actually its territory (and have it say so), or reword `issue-closure.md`'s claim as an inference rather than a settled cross-skill contract.
4. (Optional, low priority) State explicitly in `milestone-completion.md` what happens when the human declines closure, mirroring `issue-closure.md`'s "don't ask again unprompted."

## 12. Open questions that should remain unresolved

- Should full-project lint/format/static checks at the pre-Gate-1 and completed-issue boundaries carry the same "pre-existing vs. newly introduced" discipline the rule already applies to activation-gated tests, or is "the project's static checks are all-green at all times" a legitimate assumed baseline? (§7 — needs real-project evidence, not a decision made here.)
- What should happen to a closed issue if the PR carrying its commits is later rejected or materially revised before merging? (§2/§5 — currently unowned on both sides; resolving it requires deciding whether issue-closure should move later in the lifecycle or whether reopening needs its own owned rule — a real design choice, not something to infer.)
- When dependency-order and activation-safety-order genuinely conflict during commit construction, which wins? (§4 — no evidence yet of this actually happening; not worth designing for speculatively.)

## Final recommendation

**Keep the seven-rule architecture intact.** It is not accidental — the decomposition tracks genuinely distinct questions (approval procedure vs. commit semantics vs. verification scope vs. closure vs. sequencing vs. release vs. milestone), the cross-rule contracts with `my-feature-planning` are unusually explicit and bidirectionally matched, and the human-control model has no redundant gates. Do the four sentence-level corrections in §11 before calling the skill fully refined — they're cheap and each is concretely evidenced. Do **not** invent PR/merge methodology, do **not** restructure `issue-closure.md` or `sequencing.md` out of this skill, and do **not** resolve the full-project-lint-scope question or the post-closure/pre-merge exposure in this pass — all three need either real usage evidence or an explicit human decision this review isn't positioned to make on its own.

---

## Resolution update (post-review real-world evidence pass)

The human maintainer subsequently confirmed a real observed workflow (two working paths — Backlog/hotfix directly on the trunk branch with no PR, vs. milestone work on a shared branch with a PR — plus a milestone PR-readiness gate, a post-merge authorization gate, and a regression-baseline verification model), and the seven-rule architecture was updated to absorb it without adding or splitting rules. This section records only what that evidence resolved in the open items above; it does not rewrite the analysis that produced them.

- **§7 / §12, full-project lint/static baseline** — **Resolved.** The confirmed workflow tolerates pre-existing, unrelated lint/format/static violations as baseline debt; the standard is "no new failures introduced by this work," not a fully clean historical baseline. This applies to lint/format/static-analysis only — the regression test suite's existing full-suite, no-exceptions treatment was already correct and is unchanged. See `rules/verification.md`'s "Regression baseline for lint/format/static checks."
- **§2 / §5, post-closure/pre-merge exposure** — **Resolved as intentional, with a defined (narrower) default.** The confirmed workflow closes every milestone issue before its PR even exists, by design — not the accidental gap this review flagged. The specific sub-case the new evidence actually covers is a manual-testing finding discovered after an issue closed: the default is a new issue referencing the original, never silently reopening it. See `rules/issue-closure.md`'s "This closure intentionally happens before any PR..." and `rules/milestone-completion.md`'s "When manual testing finds something." The narrower, still-open question this review's §5 also raised — a closed issue's PR being later *rejected or materially revised* rather than a fresh finding surfacing — has no evidence yet and remains unresolved (see updated `README.md` "Known limitations").
- **§4 / §12, dependency-order vs. activation-order precedence** — **Still open, as recommended.** The new evidence adds one data point (no real work has produced a conflict between the two orderings) but explicitly does not resolve precedence for if one occurs. Recorded as an observed non-conflict, not a rule, in `rules/verification.md`'s "Relationship to dependency ordering" — per this review's own recommendation not to design for it speculatively.
- **New methodology absorbed, not previously analyzed by this review:** working-branch readiness for milestone vs. Backlog/hotfix work (`rules/sequencing.md`), a milestone PR-readiness gate distinct from the existing post-release closure gate (`rules/milestone-completion.md`), and an explicit authorization gate right after PR-merge confirmation, before the release phase begins (`rules/release.md`). None of these required a new rule file or split an existing one.
