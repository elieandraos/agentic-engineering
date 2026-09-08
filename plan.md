# Ecosystem migration plan — Lab · Document · Plan · Implement · Review · Ship

**Status: Steps 1–6 approved; v2.0.0 publication pending separate approval.** Step 3 passed Control Room review at commit
`ab3ea28413d28b0a20a7d7a2c0f73a9e2587b9ea`, and the user's confirmation to record that approval was
itself recorded at commit `b2fad42f1e4e73e482e7a49921bed6e47b1795a7`. Step 4 — establishing
`review-it` and integrating it before Gate 1 (§5) — was implemented on top of that HEAD at commit
`8dc3eaec11b52b829b54e7e224b1b0daae809ec4`, then received one correction pass, approved by the
Control Room, at commit `7750870bb1b1251f256649352fa380db3037b058` (Gate 1's review-input/outcome
contract, the authorized-scope-change exemption's breadth, and stack-companion-independent framework
checking), and a second, bounded correction pass narrowing comparison-base selection and comparison
identity in `review-it` at commit `dfad7309aaac5747234a462094af050a371b3e84`. See Step 4's own
implementation, correction, and approval records below. **Step 4 passed Control Room review at that
commit, and the user confirmed proceeding.** Step 5 — strengthening recovery and adopting the
approved verification policy (§5) — has been implemented on top of that HEAD, with its two
previously open decisions (§7) settled directly by the user ahead of implementation: canonical
issue-definition durable storage deferred, not resolved; the completed-issue-boundary full-suite
reuse-eligibility rule adopted as stated in `implement-it/rules/verification.md`'s "Completed-issue
verification: run or reuse" — that decision settlement is distinct from, and does not itself
constitute, Control Room approval of this step's own implementation. Step 5 was implemented at
commit `297036f1aa36aff934c82fcc2fc65e96ab2827ab`, then received one bounded correction pass
separating recovered content from approval evidence, making the approval-validity check reachable
on every continuation path, distinguishing a discovered PR from a recovered creation attempt, and
reconciling the final isolation run with completed-issue verification, at commit
`45509d7aaf63b18d637ea42c596ad829ebc4b6b9`. See Step 5's own implementation, correction, and
approval records below. **Step 5 passed Control Room review at that commit, with one small,
wording-only cleanup applied on top of it while recording the approval** (generalizing a leftover
narrow-reuse phrase in "Default commit-building loop" to match the two reuse sources
"Completed-issue verification: run or reuse" already defines). Step 6 — reconciling public
documentation, validating the combined ecosystem from source, and preparing consumer-validation and
publication proposals (§5) — was implemented at commit `d9f1f710ca4c1cd0c2ecf78907ccbe43f09013a6`,
then received a bounded correction/completion pass adding the three remaining architecture dossiers
and correcting several inaccurate claims found in the first pass's documentation and consumer/
release proposals, at commit `bbed1f367e2b870168d6d3ab94198b8c430c8972`, then a second, narrower
correction pass fixing five remaining findings against `ship-it.md`'s entry-condition scoping,
`review-it.md`'s comparison-override wording, `implement-it.md`'s stack-composition explanation, the
consumer-exercise prerequisites, and the evidence statements' precision, at commit
`4247a829e55f260ab86a61daf72ef6193b21979c`. See Step 6's own implementation, correction, and approval
records below. **Step 6 passed Control Room review at that commit, and the user confirmed proceeding
to finalize the v2.0.0 release proposal.** This approval covers the reviewed source and documentation
at that commit; it does not establish successful consumer execution.
This revision corrects the previously reviewed version (HEAD `468715d`) per explicit feedback. The
architecture and decisions recorded here are settled, and Step 1 (this plan) is approved. Step 2 —
extracting `document-it` and narrowing `lab-it` (§5) — was implemented on top of reviewed HEAD
`0b6b5587c56d40eda18e8fb1294913af83e52e8d`, then received one correction pass on top of reviewed
HEAD `84877dfca972e91c413370f2609a8c81aeba54f4`, and that corrected result was approved by the
Control Room at HEAD `894a6af508c9f574bd739e4974deff780c88b406`; see the implementation and
correction records appended to Step 2's own entry below. Step 3 — extracting `implement-it` and
narrowing `ship-it` (§5) — was implemented on top of that approved HEAD at commit
`40c7b9b374894d2e9cbb59c9f6cc37661dd8d1be`, then received one correction pass on top of that same
implementation correcting authorization wording, entry-condition scope, and blocked-vs-completed
language. The corrected result passed Control Room review at commit
`ab3ea28413d28b0a20a7d7a2c0f73a9e2587b9ea`; the user requested that approval be recorded before
starting Step 4. See Step 3's implementation, correction, and approval records below. Approval of
Step 3 does not authorize Step 4 or any later step — each remaining step requires its own go-ahead,
per §5.

**Source of truth for this initiative.** This is the change plan for splitting the current
`lab-it` / `plan-it` / `ship-it` ecosystem into `lab-it` (narrowed), `document-it` (new), `plan-it`
(unchanged), `implement-it` (new), `review-it` (new), and `ship-it` (narrowed). It does not
implement any of the moves it describes.

**Inspected state.** Branch `main`, HEAD `f951bbebdeb13f4673accc97eaeaa35546c8a4b9` — unchanged
before and after this planning pass; `git status --porcelain` showed only `control-room-
responsibilities.md`, `skills-audit.md`, and `subagents.md` untracked, `plan.md` did not exist yet.

**Evidence base.** `skills-audit.md` (this repo, untracked) is used as evidence to verify against
source, not as unquestionable authority — every load-bearing claim below was checked against the
actual `skills/**` files, `docs/skill-authoring-methodology.md`, and `docs/skill-consumption.md`
during this pass, not copied from the audit. The audit's finding numbers (`#N`) are cited as
pointers, not restated. `control-room-responsibilities.md` and `subagents.md` are untracked,
unapproved proposals — cited below only as evidence for what `review-it`'s substantive checklist
can draw on, never adopted wholesale, and not a specification for anything in this plan.

**Supersedes.** This plan supersedes any earlier proposal to keep implementation review inside
`ship-it` or to keep deferring the `review-it` extraction (`roadmap.md`'s existing bullet is
retired by Step 6 once this plan executes).

---

## 1. Agreed target — identity and ownership

**Lab. Plan. Implement. Review. Ship — with the right stack.** `document-it` is an independently
available companion capability, not a pipeline stage every initiative must pass through.

| Skill | Owns | Explicitly does not own |
|---|---|---|
| `lab-it` (narrowed) | Architecture investigation; verified explanations; architecture decisions reached with the user; approved `plan.md` synthesis. An investigation can end in a verified answer alone — no guide is required. | New/updated architecture guides, guide review (→ `document-it`); unrestricted general research — the narrowing removes guide output, not the investigation method itself. |
| `document-it` (new) | Creating and maintaining explanatory guides; owning documentation review; Markdown and Artifact output. | Investigation from scratch when understanding already exists and is fresh — draws on `lab-it` when understanding is missing or stale, reusing sufficient verified evidence rather than repeating a full investigation. File extension does not decide ownership: an approved initiative `plan.md` stays `lab-it`'s even though it is a `.md` file. |
| `plan-it` (unchanged) | Implementation-ready GitHub issues; milestone/label planning; issue-set review; dependency planning. | Implementation, delivery, or review of implemented code. |
| `implement-it` (new) | Approved issue/milestone intake; working-branch readiness; implementation; verification; issue-level Git workflow; Gate 1 and Gate 2; commit construction; authorized push; issue closure and its completion comment; next-issue recommendations; the authorized fix itself for an in-flight delivery correction `ship-it` hands it (§2.2/§3.1), using this same lifecycle. | Choosing what work exists; milestone PR readiness/creation, milestone closure, release (→ `ship-it`); investigating or explaining a delivery/CI failure before a correction is authorized (→ `ship-it`). A specific-issue request ends after that issue's authorized lifecycle — it does not imply milestone-delivery authorization. |
| `review-it` (new) | Independently callable implementation assurance for a worktree, branch, or PR — callable standalone, by `implement-it` before Gate 1, or by `implement-it` during an authorized delivery correction (§3.2 CI-failure flow). Reports verified findings, unresolved limitations, or a clean result. | Implementing corrections (returns to `implement-it`); investigation-quality, guide, plan-synthesis, issue-planning, or commit-plan review — those stay with their owning skills. |
| `ship-it` (narrowed) | Milestone PR readiness; authorized PR creation; investigating a delivery/CI failure on an open milestone PR and explaining the correction needed (handing authorized fixes to `implement-it`, §2.2); post-merge delivery; milestone closure; release preparation/publication; resulting-state verification. | PR approval and merge — the human retains both; implementing a delivery correction itself (→ `implement-it`). |
| Stack companions (unchanged) | Technology-specific implementation conventions (e.g. `laravel-inertia-stack`). | Becoming a pipeline stage; used when available, not required for every implementation. |

**Handoffs**

```
lab-it ──approved plan.md──▶ plan-it ──approved issue/milestone──▶ implement-it
  ▲                                                                     │
  └── draws on, when stale/missing ── document-it                      ├──before Gate 1──▶ review-it ──findings──▶ implement-it
                                                                        │                     (also callable standalone, or
                                                                        │                      by implement-it during an
                                                                        │                      authorized delivery correction)
                                                                        │
                                                                        └──milestone ready for delivery──▶ ship-it (authorized PR creation)
                                                                                                              │
                                                                                                              ▼
                                                                                              human: PR approval and merge
                                                                                                              │
                                                                                                              ▼
                                                                                        post-merge authorization ──▶ ship-it
                                                                                        (closure; release: draft → human
                                                                                         approval → authorized publish → validate)
```

The human owns PR approval and merge — that step is never delegated. Release *execution* (drafting,
publishing, validating) is `ship-it`'s authorized job once the human gives post-merge
authorization, with the human's approval sitting inside that flow (`release.md`'s own draft →
approve → publish → validate sequence) rather than release being a human-executed step by itself.

No permanent subagent definitions, hooks, autonomous orchestration, deployment/promotion/rollback
features, or new stack companions appear anywhere in this plan.

---

## 2. Migration mapping

### 2.1 `lab-it` → `lab-it` (narrowed) + `document-it` (new)

| Current file | New owner / path | Change |
|---|---|---|
| `SKILL.md` §"Document existing architecture" (lines 49-91) | `document-it/SKILL.md` | Moved, restructured as `document-it`'s own workflow |
| `SKILL.md` §"Update an existing architecture guide" (93-110) | `document-it/SKILL.md` | Moved, restructured |
| `SKILL.md` §"Shared investigation and decision discipline" (24-47) | Stays `lab-it/SKILL.md` | Preserved — canonical home; `document-it` routes to it rather than duplicating it (see §3) |
| `SKILL.md` §"Plan feature architecture" (112-154) | Stays `lab-it/SKILL.md` | Preserved verbatim |
| `SKILL.md` §"Ownership and handoff" / "Rule and supporting-file routing" / "Output-specific non-negotiables" | Split across both `SKILL.md`s | Guide-specific rows move; plan-specific rows stay |
| `README.md` | Split | Guide-lifecycle narrative moves to `document-it/README.md`; investigation/plan-synthesis narrative stays |
| `rules/doc-style.md` | `document-it/rules/doc-style.md` | Moved; investigation/writing principles preserved, adapted for Markdown output alongside Artifact (§3.3) |
| `rules/template.html` | `document-it/rules/template.html` | Moved verbatim — this file stays Artifact-specific; Markdown output has no template.html equivalent (§3.3) |
| `rules/review.md` (guide review) | `document-it/rules/review.md` | Moved; one shared checklist, with medium-conditional items for Artifact vs. Markdown (§3.3) — not a verbatim copy, since the source file's checks currently assume Artifact only |
| `rules/maintenance.md` | `document-it/rules/maintenance.md` | Moved; maintenance and continuity principles (the claim graph, reconcile-before-editing, preserve-unaffected-claims) preserved, but output-specific identity language is adapted, not copied verbatim — the current file says "Preserve the Artifact's identity" throughout; the moved file states an equivalent for Markdown (file path, then unaffected front matter/title) alongside it, without treating Markdown metadata as universally immutable the way the current text treats Artifact identity (§3.3) |
| `rules/plan-synthesis.md` | Stays `lab-it/rules/plan-synthesis.md` | Unchanged |

No file outside `lab-it` references `doc-style.md`, `template.html`, `lab-it/rules/review.md`, or
`maintenance.md` (confirmed by repo-wide search) — this move has no external cross-reference
fallout. "Moved" above means relocated with its investigation/writing/maintenance discipline
intact; it does not mean every sentence carries over unchanged, since these files are currently
written in Artifact-only terms and must now also cover Markdown (§3.3) — Step 2's own review
checks this adaptation, it is not assumed here.

### 2.2 `ship-it` → `implement-it` (new) + `ship-it` (narrowed)

| Current file | New owner / path | Change |
|---|---|---|
| `rules/review-gates.md` | `implement-it/rules/review-gates.md` | Moved; Gate 1's stop condition gains a `review-it` bullet (Step 4, §3.1); its own cross-reference to `rules/release.md` (line 15) becomes `ship-it/rules/release.md` since that file stays behind |
| `rules/commit-boundaries.md` | `implement-it/rules/commit-boundaries.md` | Moved verbatim — confirmed no self- or cross-reference inside this file needs updating |
| `rules/verification.md` | `implement-it/rules/verification.md` | Moved; boundary set revised per approved verification policy (Step 5, §3.4); its self-description ("verification required at each lifecycle boundary in `ship-it`", line 10) is corrected to `implement-it` as part of this move, independent of the Step 5 content change; its cross-reference to `rules/release.md` (line 50) becomes `ship-it/rules/release.md` |
| `rules/issue-closure.md` | `implement-it/rules/issue-closure.md` | Moved; gains partial-mutation re-query (Step 5, §3.2); its cross-references to `rules/release.md` and `rules/milestone-completion.md` (lines 74-75, 199, 206) become `ship-it/rules/release.md` and `ship-it/rules/milestone-completion.md` since those files stay behind |
| `rules/sequencing.md` | `implement-it/rules/sequencing.md` | Moved, not verbatim: its hand-off pointer to `ship-it/rules/milestone-completion.md` is unaffected (that file stays in `ship-it`, so only this file's own path changes) — but its self-reference ("a new pass through `ship-it`", line 111) is corrected to `implement-it`, and its "When the ready set is empty" section gains the empty-set/blocked-issues distinction from §3.2 before handing off to `milestone-completion.md` |
| `rules/milestone-completion.md` | Stays `ship-it/rules/milestone-completion.md` | Gains authorized-PR-creation (new, §3.5); its "three conditions" for PR readiness stay three — the verification-policy correction (§3.4) does not add a fourth (real CI on an already-open PR is a separate, later, already-existing moment this file's own diagram already names, not a PR-readiness precondition); its five cross-references to `rules/verification.md`, `rules/review-gates.md`, `rules/commit-boundaries.md`, `rules/sequencing.md`, and `rules/issue-closure.md` (lines 128-129, 153, 210, 215, 227, 372-385) become `implement-it/rules/...` since those files move; its "CI failure on an open milestone PR" section is rewritten per the delivery-correction ownership split (§3.2/§2.2 below) |
| `rules/release.md` | Stays `ship-it/rules/release.md` | Unchanged in substance; its "PR creation and merge strategy are not owned by this rule" line stays true and now points at `milestone-completion.md` as the file that does own PR creation, not at itself; its own cross-references to `rules/commit-boundaries.md`, `rules/sequencing.md`, `rules/review-gates.md`, and `rules/issue-closure.md` (lines 11, 36, 62, 94, 165, 202, 220) become `implement-it/rules/...` since those files move |
| `SKILL.md` | Split | `implement-it/SKILL.md` (new) takes activation triggers `implement issue`, `commit issue`, `close issue`, `what's next in milestone`; `ship-it/SKILL.md` (narrowed) keeps `is milestone ready for a PR`, `create milestone PR`, `is milestone ready to close`, `release {version}` |
| `README.md` | Split | Same split as `SKILL.md` |

**Delivery-correction ownership**, rewritten into `milestone-completion.md`'s "CI failure on an
open milestone PR" section as part of this same pass (not deferred to Step 5): `ship-it` keeps
steps 1-3 of that section — the PR stays unmerged, it investigates the failure, and it determines
whether the fix stays in already-approved scope or is genuinely new work — and explains what
correction is needed. Any authorized code correction is `implement-it`'s job: it owns the fix
itself, invoking `review-it` and Gate 1/Gate 2 as applicable, constructing the commit(s) per
`commit-boundaries.md`, verifying per `verification.md`, and pushing once authorized — the same
lifecycle it already owns for ordinary issue work, applied here to a correction instead of a fresh
issue. `ship-it` resumes the delivery workflow (re-running real CI, reporting) once the correction
lands and CI is green. The existing authorized-direct-fix route for an already-closed issue's scope
(current step 4: human authorization required, no new issue needed) is preserved exactly — only
who performs the fix changes, from an unstated actor to `implement-it` by name. This does not
require reopening the closed issue, and does not require a new issue for a narrowly authorized,
already-in-scope correction; genuinely new scope still goes through `plan-it` via the existing
discovered-work intake (current step 5, unchanged). `ship-it` does not implement code under this
corrected flow, and this route stays available without requiring an open issue to exist.

**Cross-references outside `ship-it` that this split breaks and must be updated** (found by repo-
wide search, not assumed):

| File | Line(s) | Current text | Required update |
|---|---|---|---|
| `plan-it/SKILL.md` | 93 | "`ship-it` owns the downstream Git/GitHub delivery workflow — branch readiness..." | → `implement-it` |
| `plan-it/rules/discovered-work.md` | 174 | "`ship-it` owns the downstream Git/GitHub delivery workflow" | → `implement-it` |
| `plan-it/rules/review.md` | 293 | "implementation review, issue closure, or delivery progression (`ship-it`)" | Splits three ways, not one: "implementation review" → `review-it` (this plan introduces that owner; the line currently has no such distinction); "issue closure" → `implement-it`; "delivery progression" stays `ship-it`, for milestone/release only |
| `plan-it/rules/issue-conventions.md` | 235, 252, 265 | `ship-it/rules/verification.md` | → `implement-it/rules/verification.md` |
| `plan-it/rules/issue-conventions.md` | 155, 277, 299 | `ship-it`'s `rules/milestone-completion.md` | Unchanged — that file stays in `ship-it` |
| `plan-it/rules/sequencing.md` | 8, 82, 123 | "`ship-it`, particularly its own `rules/sequencing.md`" / "`ship-it`'s job after creation" | → `implement-it` for branch readiness and next-issue recommendation; a milestone-level mention (readiness/closure) stays `ship-it` |
| `plan-it/README.md` | 42 | "[`ship-it`](../ship-it/) — this skill plans the work, it doesn't build it." | → points at `implement-it` as the immediate next stage, with `ship-it` named separately for milestone delivery |
| `lab-it/README.md` | 45 | "implementing it belongs to [`ship-it`](../ship-it/)." | → `implement-it` — missed in the prior pass; found by this correction's repo-wide re-check. `lab-it` is narrowed by Step 2, not Step 3, but this line is about who implements, so it's corrected in the same Step 3 pass as the rest of this table, not Step 2's |

`plan-it`'s own rule content is not restructured by this migration — only these handoff pointers
change, because the skill immediately downstream of `plan-it` becomes `implement-it` rather than
`ship-it`. This is corrected in the same pass that extracts `implement-it` (Step 3), per the
authoring methodology's reconciliation discipline (`docs/skill-authoring-methodology.md` §11):
correct stale references in the same coherent pass, don't leave every consumer to drift.

### 2.3 `review-it` (new, no predecessor file)

Built from scratch as an operational skill, informed by — but not copied from — the untracked
`control-room-responsibilities.md`'s "Engineering reviewer" responsibility (lines 123-152) and the
audit's own framing of what committed `ship-it` does not currently prescribe (`skills-audit.md`
finding #1, decision-brief topic 1). See §3.1 for the procedure design.

---

## 3. Strengthening to plan

Each subsection states what changes, why, what it proves, and — where the prompt that produced this
plan explicitly withholds a default — what stays an open decision rather than being silently
resolved here.

### 3.1 Implementation review (`review-it`)

**Procedure, not category names.** `review-it` runs a skip-if-inapplicable checklist — the same
established pattern `lab-it`'s guide review and `plan-it`'s issue review already use, not a new
review shape:

| Category | What it checks |
|---|---|
| Requirements compliance | The approved issue/plan scope is what was actually implemented — no silent narrowing or expansion. |
| Correctness | The change does what it claims, including edge cases the approved scope implies. |
| Security | Authorization, input handling, and secret/data exposure at every surface the change touches. |
| Data integrity | Migrations, defaults, and concurrent-write behavior don't corrupt or silently drop existing data. |
| Likely regressions | Behavior the suite doesn't cover but the diff plausibly affects. |
| Architectural fit | Consistency with the guide/plan's approved architecture and this project's own conventions. |
| Maintainability | Unnecessary complexity, duplication, or a shape that will fight the next change. |
| Project/stack convention compliance | Applicable project instructions and the loaded stack companion's rules, where one applies. |
| Test adequacy | Tests prove the decision, not merely that something ran. |
| Accidental scope expansion | Changes outside the approved issue/plan that weren't flagged as a stop (`review-gates.md`'s "when to stop and ask"). |

**Verification and evidence.** Every finding is verified before being reported — reproduced,
traced to a concrete file/line or command output — never a suspicion stated as fact. `review-it` may
run the project's own existing verification commands (tests, linters, static analysis) to confirm a
claim; this is diagnostic execution, not a claim of read-only purity — running a test suite can
still write to caches or temp state. What it never does: edit application code, or mutate GitHub or
any other live/production state. Corrections are always handed back to `implement-it`; `review-it`
reports, it does not fix.

**Staleness.** A finding — or a clean result — is tied to the specific commit/diff state it was
checked against, the same discipline `plan-it/rules/review.md` already applies to issue review
("a correction invalidates the affected issue's prior record entry until it is re-rendered and
rechecked"). Any material change after a `review-it` pass invalidates that pass for the changed
surface; `implement-it` requests a fresh pass (full or scoped to the correction) before Gate 1 can
rely on it again.

**Gate 1's revised stop condition** (in `implement-it/rules/review-gates.md`): the approved issue
scope has been implemented; the verification appropriate to it has run; and `review-it`'s pass is
either clean or its findings have been resolved and re-verified. The approval mechanics at Gate 1
(stop, 4-item report, explicit human approval) are unchanged — only the third bullet is new.

**A second invocation point: delivery corrections.** `review-it` is not only a pre-Gate-1 check.
When `implement-it` performs an authorized correction during `ship-it`'s delivery-correction flow
(§2.2 above — a CI failure on an open milestone PR), `implement-it` invokes `review-it` the same
standalone way, before that correction's own Gate 1/Gate 2 pass. This is the same capability used
at a different trigger point, not a second review procedure.

### 3.2 Recovery

Smallest sufficient additions to the file that already owns the adjacent behavior — no new file,
gate, or execution context, per the audit's own recommended-smallest-change framing (decision-brief
topic 3):

| Gap (audit finding) | Owning file after migration | Proposed addition |
|---|---|---|
| Worktree provenance (finding, Section 3 scenario 3) | `implement-it/rules/verification.md` §"Discover the verification starting state" | Preserve pre-existing worktree changes by default. Recency, being uncommitted, or matching the approved issue's scope does not by itself prove a change belongs to this session — appearance is not provenance. Use whatever reliable provenance is actually available (e.g., git reflog, the session's own recorded start point, an explicit statement from the human) to judge origin; ask the human when the ambiguity would materially affect whether it's safe to continue, rather than on any ambiguity at all. Never invent ownership from appearance, and never modify content whose origin can't be established this way. **Resolved by Step 5**, implemented in that section's "Preserve pre-existing worktree changes": the three signals named above are the reliable, portable provenance sources this rule states directly — not a project-specific inventory left open. |
| Empty dependency-ready set treated as sufficient for delivery handoff | `implement-it/rules/sequencing.md` §"When the ready set is empty" | An empty ready set is not, by itself, sufficient to hand off to `ship-it`'s Milestone PR readiness. `rules/sequencing.md`'s own definition allows an empty ready set with open issues still outstanding — nothing dependency-ready right now, but one or more issues blocked on something rather than closed. Before handing off, distinguish "zero open issues remain" (the genuine completion case, hand off as today) from "open issues remain, all currently blocked" (report the blocked state; do not hand off, since the milestone isn't done). The existing recommend-and-stop behavior — the human, not this rule, chooses the next issue — is unchanged either way. **Implemented at Step 3**, ahead of this table (`implement-it/rules/sequencing.md`'s "When the ready set is empty"), not deferred to Step 5. |
| Partial GitHub mutation before resuming a batch (finding #10) | `plan-it/rules/sequencing.md` (issue batches); `ship-it/rules/milestone-completion.md` and `rules/release.md` (milestone/release mutations) | Before creating/mutating more of a batch, re-query GitHub for members this same interrupted batch may already have created — extends the existing post-mutation re-fetch pattern already present in four files, not a new mechanism. **Resolved by Step 5**: `plan-it/rules/sequencing.md`'s "Resuming an interrupted batch creation," `ship-it/rules/milestone-completion.md`'s PR-creation and closure re-query additions, and `ship-it/rules/release.md`'s step 5 partial-publish re-query. |
| Canonical issue-definition durable storage (finding #21) | `plan-it/rules/issue-conventions.md` | **Resolved by Step 5's review: explicitly deferred, not implemented by this migration.** No `issue-plan.md`-equivalent file, approval registry, or other persistence mechanism is introduced. Retained instead: a simple recovery procedure stated in `plan-it/rules/sequencing.md`'s "Resuming an interrupted batch creation" — after interrupted issue creation, query GitHub before retrying; continue only from reliably available canonical definitions, scope, and authorization; explain what's missing and ask the human, rather than reconstructing the approved batch from guesses, when they can't be recovered. |
| Approval staleness after a material change (finding #13/#4) | `implement-it/rules/review-gates.md` | Before Gate 2 and before push, compare the current diff/issue body against what was approved; a material difference invalidates that approval and requires re-review — extends the existing "never silently convert an unresolved decision into a fact" principle already stated four times across the ecosystem. **Resolved by Step 5**: `review-gates.md`'s "Approval validity before Gate 2 and before push," which also states that ordinary staging/assembling of unchanged, already-approved content must not automatically invalidate Gate 1, and that remote commit reachability proves presence, not verification or authorization. |
| Verification evidence tied to the state checked | Existing report shapes (Gate 1 report, `review-it` findings, closing comment) | Cite the commit SHA/diff the evidence was produced against, so a later reader can tell whether it still covers current state. Already carried by `review-it`'s own report shape (Step 4) and `implement-it/rules/issue-closure.md`'s closing comment; unaffected by Step 5. |

### 3.3 Documentation output (`document-it`)

Covers creation and maintenance for both Markdown and Artifact — the audit explicitly flags that a
fallback for creation without an equal one for maintenance/update would be incomplete (decision-
brief topic 4); this plan does not repeat that gap.

**A new guide.**

- **Format selection.** Ask the user whether they want an Artifact, Markdown, or both — unless
  they've already specified. Don't infer the format from context.
- **Markdown location.** Lives under the consuming repository's own `docs/` directory; create that
  folder if it doesn't already exist. This is now a settled default, not an open item.
- **Respect the requested format.** If the capability the requested format needs is unavailable
  (e.g., no Artifact tool), explain that plainly and ask the user how to proceed — do not silently
  substitute the other format and report success as if the request were fulfilled.

**An existing guide.**

- **Locate and inspect the target first**, rather than assuming its current content.
- **Distinguish three different failure modes**, since each needs a different response: the target
  is genuinely missing (no guide exists yet at the expected identity); the target exists but is
  inaccessible (e.g., an Artifact URL that can't be reached); or the publishing capability itself is
  unavailable (e.g., no Artifact tool in this session) even though the target is fine.
- **Preserve the existing identity by default** — same file path for Markdown, same `url` and
  favicon for Artifact (existing `maintenance.md` rule, stated with equal weight for both formats,
  not an afterthought for Markdown).
- **When the requested update can't be performed**, explain the limitation concretely and ask the
  user whether to: prepare/create/update a Markdown version instead; create a replacement Artifact
  where that's possible; or change which format is the maintained one going forward. Never claim
  that writing a Markdown update updated the original Artifact — those are different documents once
  an Artifact can't be reached or written.
- **No formal taxonomy required.** The user doesn't need to understand a "draft vs. migration"
  distinction to make this choice — state the concrete consequence of each option (which document
  ends up updated, which stays stale) rather than naming a category.

**When both formats are maintained for the same guide.**

- **Keep architectural claims synchronized** across both on an update, unless the user explicitly
  says otherwise for that update.
- **Format-appropriate presentation, not identical rendering.** One review procedure
  (`document-it/rules/review.md`), not two — the architectural-communication checklist generalizes
  across both media; a handful of items stay medium-conditional (favicon/URL checks apply to
  Artifact only; a link-integrity/structure check applies to Markdown only).
- **Report precisely which outputs were updated**, and name any remaining divergence or failure
  rather than reporting a single "done."
- **Keep the association between the two outputs discoverable** — e.g., a cross-reference each
  carries to the other's location. A minimal mechanism is proposed and reviewed as part of Step 2's
  own authoring; this plan does not invent an elaborate registry now, and does not require one.

### 3.4 Verification policy

**The settled policy, stated plainly** (correcting an earlier, mistaken version of this section
that invented an extra "milestone-entry baseline" and framed the result as "two new boundaries" —
neither survives this correction):

- **Targeted tests during implementation and corrections.** Unchanged from today's
  narrowest-reliable-scope-per-commit model.
- **The full project-defined suite before each issue's Gate 1.** This is the existing, unconditional
  per-issue requirement (proves the complete working tree before any commit split exists) — it is
  not new, and it does not gain a separate, additional "milestone-entry" trigger. A milestone is
  worked one issue at a time; each of those issues already passes through its own Gate 1. Whether
  the user's original request named a single issue or a milestone does not change this standard —
  there is no extra full-suite run that fires merely because the session is in "milestone mode."
- **Additional checks scoped to a `review-it` finding**, when one surfaces something needing
  verification beyond what already ran. New, but narrow — it extends coverage to what the finding
  actually implicates, not a second full-suite run.
- **The completed-issue-boundary full-suite run and isolation verification's escalation for
  load-bearing ordering stay in force exactly as they exist today**, until Step 5 explicitly
  approves a replacement. This correction does not silently authorize removing or weakening either
  — both are preserved requirements, not open questions this pass resolves by omission.
- **PR CI must pass before merge — a separate, later fact, not a new verification-policy boundary.**
  Once `ship-it` creates the milestone PR (§3.5), real CI runs against it automatically —
  `milestone-completion.md`'s own diagram and "CI failure on an open milestone PR" section already
  name this moment; it is existing behavior, not something this policy adds. The distinction that
  matters: checks above (targeted tests, per-issue full suite, completed-issue-boundary suite,
  isolation verification) are things `implement-it` can and does run *before* a PR exists; PR-
  triggered CI only starts running *after* the PR is created, and merge is blocked until it's green.
  Nothing in this plan turns that PR-triggered CI into an extra local, pre-creation gate.
- **Discover the project's actual test/CI commands and configuration** — this plan does not
  prescribe Laravel-specific commands or any other stack's specific tooling, following the existing
  discoverable-tooling model already in `verification.md`.

**Resolved by Step 5's review**, no longer open: the reuse-eligibility rule for the completed-issue
checkpoint. Both checkpoints (pre-Gate-1, completed-issue) remain required — reuse is a way to
satisfy the second, never a reason to drop it. The completed-issue checkpoint may be satisfied by
reusing an earlier full-suite result — the pre-Gate-1 run, or one already executed directly against
the final committed state (e.g. isolation verification's last per-commit run, when nothing remained
stashed afterward) — only once four conditions are all established: identifiable evidence
of an actual successful, complete run; the final committed content matching the tested content
(never inferred from a clean worktree, an unchanged `HEAD`, or a successful commit command alone);
equivalent relevant test inputs and environment (dependencies, configuration, generated inputs, and
consumed commit metadata); and no unresolved limitation undermining that equivalence. A cache hit or
an impact-analysis-selected subset can never by itself satisfy the first condition. When any
condition fails, the full suite runs again — a corrected state must itself satisfy this checkpoint,
and a narrower per-commit check never substitutes where the full suite is required. Reuse is
reported honestly, identifying the earlier result and why it still applies, never presented as a
newly executed run. See the settled rule, implemented at Step 5, in
[`skills/implement-it/rules/verification.md`](skills/implement-it/rules/verification.md)'s
"Completed-issue verification: run or reuse." No other part of this policy is open.

### 3.5 `ship-it`'s new PR-creation responsibility

**Implemented and approved in Step 3** at commit
`ab3ea28413d28b0a20a7d7a2c0f73a9e2587b9ea`. `ship-it` owns authorized milestone PR creation;
the human retains PR approval and merge. The operational procedure lives in
[`skills/ship-it/rules/milestone-completion.md`](skills/ship-it/rules/milestone-completion.md),
under "Milestone PR creation."

The reviewed procedure:

1. Once the three PR-readiness conditions pass, discover the project's PR conventions.
2. Check for an existing matching PR before proposing creation.
3. Prepare the title, base/head branches, and body referencing the milestone.
4. Obtain explicit approval of that exact proposal before creating the PR. An existing request to
   check readiness or create the PR already authorizes preparation; no redundant start request is
   required.
5. Create through the discovered mechanism, then re-fetch and validate the actual result.
6. Leave PR approval and merge with the human; follow the existing CI-failure procedure when needed.

This approval records source review of the implemented procedure. No live PR-creation exercise or
consumer validation has been performed.

---

## 4. Behavior deltas

**Preserved, moved.** `lab-it`'s investigation discipline and plan-synthesis method;
`document-it`'s guide-writing grammar, template, review checklist, and maintenance procedure's
principles — relocated with the discipline intact, but not a byte-for-byte copy, since the source
files are currently Artifact-only and now also cover Markdown (§2.1, §3.3); `implement-it`'s Gate
1/Gate 2 state machine, commit-boundary derivation, existing verification lifecycle (completed-issue
full-suite run and isolation-verification escalation both preserved as-is per §3.4's correction),
issue-closure procedure, and branch-readiness/next-issue-recommendation logic; `ship-it`'s milestone
PR-readiness conditions — still exactly three, not four (§3.4's correction removes the earlier,
mistaken fourth-condition framing) — closure gate, and release-policy
discovery/drafting/publish/validation; the two-gate-never-collapsed invariant; closure always opt-in;
the existing discoverable-configuration-vs-fixed-structure distinction (finding #20, untouched by
this migration); Git/GitHub as intentional core substrate.

**Clarified, not changed.** Gate 1/Gate 2 are now explicitly `implement-it`'s own gates, not
ambiguously "`ship-it`'s"; file extension does not decide `document-it`-vs-`lab-it` ownership —
`plan.md` stays `lab-it`'s; milestone PR-readiness stays "a report, not a mutation" for the readiness
conditions themselves, distinguished from the new PR-*creation* mutation that follows a positive
report; a specific-issue request ending after that issue's lifecycle (already true — `sequencing.md`
already forbids chaining into the next issue) is now stated as the explicit boundary between
`implement-it` and `ship-it`/human authorization for milestone delivery; PR approval and merge stay
human-owned exactly as today, while release *execution* (draft/publish/validate) is `ship-it`'s
authorized job once post-merge authorization is given — the earlier diagram's "human (PR approval,
merge, release)" wrongly lumped release execution in with the two steps that are actually
human-owned, and is corrected (§1); the underlying narrow-fix-vs-discovered-work policy for a CI
failure on an open milestone PR is unchanged — only who executes an authorized correction moves,
from an unstated actor to `implement-it` by name, as a mechanical consequence of `verification.md`/
`commit-boundaries.md`/`review-gates.md` relocating there (§2.2).

**New behavior** (agreed target for this migration, not an extraction of already-existing,
undocumented practice — stated plainly per the audit's own caution, decision-brief topic 1):
`review-it` as an independently callable skill, including its second invocation point during an
authorized delivery correction (§3.1); Gate 1's substantive checklist (§3.1); `ship-it`'s authorized
PR creation (§3.5); the recovery-contract additions, including the empty-ready-set/blocked-issues
distinction (§3.2); Markdown as a first-class, equally-maintained `document-it` output alongside
Artifact, with its location now settled under the consuming repo's `docs/` (§3.3).

**Proposed, still requiring a decision** (not silently approved by this plan): canonical
issue-definition durable storage location and lifecycle (§3.2); the completed-issue-boundary
full-suite reuse-eligibility rule (§3.4 — this is now the only open item in the verification
policy). `ship-it`'s PR-creation procedure is implemented and approved under Step 3 (§3.5).
Checklist wording, exact filenames, and other procedural detail (`review-it`'s per-item checklist,
the exact worktree-provenance signal, the approval-staleness re-confirmation wording, the
Markdown/Artifact association mechanism) are authoring work for their owning steps' own review, not
separate architecture questions held open here (§7).

---

## 5. Incremental execution plan

Each step is independently reviewable. No step activates a skill that doesn't yet exist, and no
step is published in a mixed or half-migrated state.

### Step 1 — This design/change plan

- **Outcome/boundaries.** `plan.md` written and presented for review. Nothing else touched.
- **Affected files.** `plan.md` only (new).
- **Preserved vs. changed.** N/A — planning only.
- **Dependencies.** None; every later step depends on this being approved.
- **Acceptance criteria.** `git status` shows `plan.md` as the only change; the user has reviewed
  and approved this plan's architecture, ownership, and step sequence. Approving this step approves
  that sequence — it does not require resolving every item in §7's material-decisions list up
  front; each of those is resolved at its own owning step, per that step's own dependencies below.
- **Result to present.** This document, plus the material-decisions list (§7).

### Step 2 — Extract `document-it`, narrow `lab-it`

- **Outcome/boundaries.** `document-it` exists as a fully self-contained skill (§2.1); `lab-it`
  no longer routes to guide-workflow files; §3.3's reviewed decisions are implemented here, since
  this is `document-it`'s own domain.
- **Affected files.** New: `document-it/SKILL.md`, `README.md`, `rules/doc-style.md`,
  `rules/template.html`, `rules/review.md`, `rules/maintenance.md`. Modified: `lab-it/SKILL.md`,
  `lab-it/README.md`. Unaffected: `lab-it/rules/plan-synthesis.md`.
- **Preserved vs. changed.** Guide grammar, template, review checklist, and maintenance procedure's
  principles move intact; their Artifact-only wording is adapted to also cover Markdown (§2.1). All
  of §3.3's format-selection, location, no-silent-substitution, and both-formats-maintained behavior
  is already settled by this plan — nothing here is deferred to this step as an open architecture
  choice.
- **Dependencies.** None beyond Step 1's approval. This step's own authoring produces the minimal
  Markdown/Artifact association mechanism and the review checklist's exact medium-conditional
  wording, reviewed as part of this step's own result — not decided in advance.
- **Acceptance criteria.** `document-it` activates on "document/update/review a guide" without
  invoking `lab-it` except for its stated investigation-reuse step; no reference to
  `doc-style.md`/`template.html`/guide `review.md`/`maintenance.md` remains under `lab-it/`; a
  repo-wide search confirms no external file still points at the old paths.
- **Validation (static).** Walk through "document existing architecture," "update an existing
  guide," and "review a guide" against `document-it`'s new files only.
- **Result to present.** Diff of new `document-it` files and narrowed `lab-it` files, plus
  confirmation that no `plan-it`/`ship-it` file needed updating (verified — none references the
  moved files).

**Implemented.** Starting point: branch `main`, HEAD `0b6b5587c56d40eda18e8fb1294913af83e52e8d`
(the last reviewed commit), working tree clean except the three pre-existing untracked files
(`control-room-responsibilities.md`, `skills-audit.md`, `subagents.md`), left untouched.

- `document-it/SKILL.md`, `README.md`, `rules/doc-style.md`, `rules/review.md`,
  `rules/maintenance.md` created; `rules/template.html` moved verbatim (byte-identical, path only).
  `doc-style.md`, `review.md`, and `maintenance.md` carry the same writing grammar, evidence
  standards, review substance, and maintenance discipline as their `lab-it` originals, adapted so
  every previously Artifact-only rule (favicon, `url` identity, redeploy sequence, format-specific
  review checks) now states an equivalent for Markdown (file path identity, front matter/title
  handled as non-immutable metadata, `docs/`-relative saving) alongside the unchanged Artifact
  behavior, per §3.3.
- `lab-it/SKILL.md` and `README.md` narrowed: the "Document existing architecture" and "Update an
  existing architecture guide" workflow sections removed; "Shared investigation and decision
  discipline" and "Plan feature architecture" preserved, the former's closing paragraph adapted
  (guide-specific conditionals replaced with the `document-it` routing case; a stray reference to
  the removed "Document existing architecture" heading in "Plan feature architecture"'s
  preconditions corrected to point at the retained "Shared investigation and decision discipline"
  section instead). `rules/plan-synthesis.md` untouched.
- Git recorded all four moved `rules/*` files as renames, not delete+add.
- **Unexpected finding, corrected.** `artifacts/lab-it.md` (a tracked architecture dossier for
  `lab-it`, not listed as affected by §2.1's cross-reference search) carries seven Markdown links
  into `../skills/lab-it/rules/{doc-style.md,template.html,review.md,maintenance.md}` — a live
  pointer this extraction breaks that §2.1's "no file outside `lab-it` references" claim missed.
  Corrected with the smallest necessary change: the seven links now point at
  `../skills/document-it/rules/...`; the dossier's own prose (which still describes these
  workflows as `lab-it`'s) is untouched — that content reconciliation is Step 6's "broader
  public-documentation rewrite," not this step's. `artifacts/lab-it.md`'s one link to
  `../skills/lab-it/rules/plan-synthesis.md` was already correct and needed no change.
- `rules/template.html`'s own header comment still said "the lab-it guide-writing workflow" — left
  as-is per this step's explicit "moved verbatim" instruction; flagged here as a stale
  self-reference inside an unmodified file, not a broken cross-file link. Corrected in this step's
  own follow-up correction pass, below.
- **Validation performed:** full re-read of both resulting skills and every affected supporting
  file; frontmatter and Markdown structure checked in both `SKILL.md` files; a diff of each moved
  rule file against its pre-move committed content, confirming every delta is an intentional
  Markdown/Artifact adaptation or terminology fix, not a dropped requirement; `template.html`
  confirmed byte-identical to its pre-move content; a repo-wide search confirming `lab-it/` no
  longer references or routes to `doc-style.md`/`template.html`/guide `review.md`/`maintenance.md`;
  a repo-wide search for the four moved filenames outside `document-it/`, `plan.md`, and the
  untracked `skills-audit.md`, which surfaced only the `artifacts/lab-it.md` finding above; `git
  diff --check` clean; seven bounded static walkthroughs run against the actual file content
  (investigation ending in an answer plus the retained `plan.md` handoff; new guide with
  unspecified and explicit format; Markdown-only work with no Artifact tool; existing-guide update
  and standalone review; missing/inaccessible target and unavailable publishing tool; both formats
  with a partial update failure; reusing sufficient evidence versus routing a missing investigation
  through `lab-it`) — all traced correctly through the new files with no coherence gap found. No
  Artifact was published and no consuming project was touched, per this step's authorization scope.

**Corrected.** One correction pass on top of reviewed HEAD
`84877dfca972e91c413370f2609a8c81aeba54f4`, addressing four findings against `document-it`:

1. `document-it/SKILL.md`'s frontmatter and `README.md`'s "not for" line previously implied
   debugging and diff review "stay with `lab-it`," alongside investigation, architecture decisions,
   and `plan.md` synthesis, which do. Corrected to state debugging/diff review as simply out of
   scope, with no owner implied — no new owner introduced, no unbuilt skill activated.
2. Reconciled Markdown location: `docs/` is now stated as the default for a *new* guide only, in
   `SKILL.md`'s "Format selection." An update preserves the guide's existing path, including one
   outside `docs/`, unless the user explicitly authorizes relocation — stated in `SKILL.md`'s
   identity-preservation bullet, and `rules/review.md`'s Markdown format-specific check now accepts
   a preserved out-of-`docs/` path rather than flagging it.
3. Carried the existing single-format-update exception (`SKILL.md`'s "Maintaining both formats")
   through `rules/maintenance.md` (claim-graph, redeployment, and sequence steps) and
   `rules/review.md` (the "Both formats maintained" check and a new "does not flag" entry): default
   stays synchronized; an explicit single-format request updates only that format and reports the
   other's resulting divergence, never presented as a failure or as both outputs being current.
4. `rules/template.html`'s header comment corrected: "the lab-it guide-writing workflow" →
   "the document-it guide-writing workflow"; the favicon cross-reference anchor updated from
   `#choosing-a-favicon` to `#choosing-a-favicon-artifact-only`, matching `doc-style.md`'s actual
   heading. No other HTML, CSS, or JavaScript changed — confirmed by diffing the corrected file
   against its prior committed content, which shows only these two comment-text hunks.

**Validation performed:** full re-read of every edited file; a repo-wide search confirming no
remaining reference to the old `#choosing-a-favicon` anchor or to the debugging/diff-review
misattribution; `git diff --check` clean; four focused static walkthroughs against the corrected
files (a debugging/diff-review request lands with neither skill claiming it; updating an existing
root-level `architecture.md` preserves its path outside `docs/` without the review checklist
flagging it; updating only the Markdown half of a maintained pair honors that scope and reports the
Artifact's resulting divergence, not a failure; an ordinary paired update with no format
restriction still synchronizes both outputs) — all four traced correctly with no coherence gap
found.

### Step 3 — Extract `implement-it`, narrow `ship-it`

**Approved by Control Room** at commit `ab3ea28413d28b0a20a7d7a2c0f73a9e2587b9ea`, with the
user's confirmation to record the approval. The correction pass resolved the authorization,
entry-condition, and blocked-versus-completed findings. Existing review gates, test policy, commit
rules, and release mechanics remain preserved. This is source-review approval; consumer execution
remains untested. Step 4 requires its own go-ahead.

- **Outcome/boundaries.** `implement-it` exists and handles single-issue and milestone-mode
  implementation identically to current `ship-it`, using only moved files; `ship-it` is narrowed to
  milestone delivery and gains the reviewed PR-creation procedure (§3.5); every cross-reference in
  §2.2's table is updated in this same pass, in both directions — retained `ship-it` files' pointers
  into the files that just moved, and moved files' self-references and pointers back to the files
  that stayed behind.
- **Affected files.** New: `implement-it/SKILL.md`, `README.md`, `rules/review-gates.md`,
  `commit-boundaries.md`, `verification.md`, `issue-closure.md`, `sequencing.md`. Modified:
  `ship-it/SKILL.md`, `README.md`, `rules/milestone-completion.md` (PR creation; its five
  cross-references to the relocated files; its "CI failure on an open milestone PR" section rewritten
  per the delivery-correction ownership split), `rules/release.md` (its own cross-references to the
  relocated files); `implement-it/rules/verification.md` and `rules/sequencing.md` (self-references
  renamed from "`ship-it`" to "`implement-it`" as part of the move itself, separate from Step 5's
  later policy content); `implement-it/rules/sequencing.md` (empty-ready-set/blocked-issues
  distinction, §3.2); `plan-it/SKILL.md`, `rules/discovered-work.md`, `rules/review.md` (its
  three-way split — `review-it`/`implement-it`/`ship-it` — not a single blanket rename),
  `rules/issue-conventions.md`, `rules/sequencing.md`, `README.md` (handoff pointers only — no
  owned-content change); `lab-it/README.md` (its "implementing it belongs to `ship-it`" line, found
  by this correction's repo-wide re-check — corrected here since it's about implementation
  ownership, not documentation, even though `lab-it` itself was narrowed in Step 2).
- **Preserved vs. changed.** Gate mechanics, commit derivation, existing verification lifecycle,
  issue closure, branch readiness, and next-issue recommendation move intact (self-referential
  wording is corrected as part of the move; content is otherwise unchanged here — Step 5 owns the
  verification-policy content change). Deliberate: `ship-it` gains PR creation (§3.5, implemented
  and approved through this step's review);
  `milestone-completion.md`'s CI-failure section is rewritten so `ship-it` investigates/explains and
  `implement-it` performs any authorized correction (§2.2) — the underlying policy (narrow authorized
  direct fix vs. discovered-work intake) is unchanged, only the named executor is. `review-it` is
  **not** wired into Gate 1 yet — that's Step 4; Gate 1's text in this step notes the pending
  integration explicitly, so the transition state is never ambiguous.
- **Dependencies.** Step 2 complete (kept sequential so only one mixed-ownership state exists at a
  time, even though the two domains are independent).
- **Acceptance criteria.** `implement-it` reproduces current `ship-it` behavior for "implement issue
  #N" end to end; `ship-it` additionally handles an authorized PR-creation request once PR readiness
  passes; no file anywhere still says "`ship-it`" for branch readiness, Gate 1/2, commits,
  verification, or issue closure; `release.md`'s "not owned by this rule" statement no longer
  conflicts with `milestone-completion.md`; `milestone-completion.md`'s and `release.md`'s own
  cross-references to the five relocated files all read `implement-it/rules/...`; the CI-failure
  section names `implement-it` as the one performing an authorized correction, without requiring an
  open issue or ship-it implementing code; `sequencing.md`'s empty-ready-set handoff distinguishes
  zero-open-issues from open-but-blocked before reporting to `milestone-completion.md`.
- **Validation (static).** Single-issue implementation walkthrough; milestone-mode walkthrough
  (branch readiness → issues → empty ready set, including the all-blocked case → hand off to
  `ship-it` only when genuinely zero open issues remain); the new PR-creation flow through to a
  human-merge stop; a CI failure on an open milestone PR walked through end to end — `ship-it`
  investigates and explains, `implement-it` fixes and pushes, `ship-it` resumes once green.
- **Result to present.** Diff of new `implement-it` files, narrowed `ship-it` files, the proposed
  PR-creation procedure text, the rewritten CI-failure/delivery-correction section, and every
  cross-reference update from §2.2's table (both directions), for review.

**Implemented.** Starting point: branch `main`, HEAD `894a6af508c9f574bd739e4974deff780c88b406`
(the Control-Room-approved Step 2 result), working tree clean except the three pre-existing
untracked files (`control-room-responsibilities.md`, `skills-audit.md`, `subagents.md`), left
untouched.

- `implement-it/rules/{review-gates,commit-boundaries,verification,issue-closure,sequencing}.md`
  moved via `git mv` (recorded as renames); `implement-it/SKILL.md` and `README.md` created new.
  `commit-boundaries.md` moved byte-identical. The other four rule files' self- and cross-references
  to `rules/release.md` and `rules/milestone-completion.md` were corrected to
  `ship-it/rules/release.md` and `ship-it/rules/milestone-completion.md` since those files stay
  behind; `verification.md`'s and `sequencing.md`'s self-descriptions were corrected from
  "`ship-it`" to "`implement-it`"; `sequencing.md`'s "When the ready set is empty" section gained
  the empty-set/blocked-issues distinction from §3.2; `review-gates.md`'s Gate 1 gained an explicit
  note that `review-it` is a planned, not-yet-built skill, so its stop condition stays exactly two
  bullets until Step 4 exists — no dangling reference to an unbuilt skill.
- `ship-it/SKILL.md` and `README.md` narrowed to milestone PR readiness/creation, CI-failure
  investigation, post-merge closure, and release; `rules/milestone-completion.md` gained a
  "Milestone PR creation" section implementing §3.5's discover → check-for-duplicate → draft →
  approve → create → validate procedure, and its "CI failure on an open milestone PR" section was
  rewritten so this file investigates, explains the needed correction, and gates authorization,
  while `implement-it` performs the correction through its own lifecycle once authorized — reopening
  a closed issue is not required. Both files' cross-references to the five relocated rule files were
  corrected
  to `implement-it/rules/...`; `rules/release.md` received the same cross-reference correction, with
  no substantive change otherwise.
- `plan-it/SKILL.md`, `README.md`, `rules/discovered-work.md`, `rules/sequencing.md`,
  `rules/issue-conventions.md` (verification-execution pointers only — its milestone-completion.md
  pointers were already correct and stay unchanged), and `rules/review.md` (split three ways:
  issue closure → `implement-it`; milestone/release delivery progression → `ship-it`; independent
  implementation review → named as `review-it`, explicitly flagged as not yet built) had their
  downstream-delivery handoff pointers corrected from `ship-it` to `implement-it` (or split between
  the two) — no owned planning content changed. `lab-it/README.md`'s "implementing it belongs to
  ship-it" line was corrected to `implement-it`.
- **Unexpected findings, corrected.** (1) `plan-it/rules/issue-conventions.md`'s §11 closing
  sentence — "It doesn't decide branch strategy, when a milestone issue actually closes, or when a
  milestone's PR opens — those stay `ship-it`'s" — was not, contrary to §2.2's table, actually about
  `rules/milestone-completion.md` specifically; it named three delivery facts now split across two
  skills. Corrected to attribute branch strategy and issue-closure timing to `implement-it` and PR
  opening to `ship-it`, rather than leaving all three attributed to `ship-it` alone. (2)
  `implement-it/rules/issue-closure.md` carried two further bare `rules/milestone-completion.md`
  references (its "Principle" section and its "What this rule does not do" reopening note) that
  §2.2's table did not enumerate; both corrected to `ship-it/rules/milestone-completion.md` by the
  same repository-wide search this step's instructions required. (3) `artifacts/ship-it.md` (a
  tracked architecture dossier, not listed as affected by §2.2) carries five Markdown links into
  `../skills/ship-it/rules/{sequencing,review-gates,commit-boundaries,verification,issue-closure}.md`
  — the same kind of live pointer Step 2 found and fixed in `artifacts/lab-it.md`. Corrected the five
  links to `../skills/implement-it/rules/...`; the dossier's own prose, which still describes these
  workflows as `ship-it`'s, is untouched — that reconciliation is Step 6's public-documentation
  rewrite, not this step's. (4) `artifacts/plan-it.md` (also untracked by §2.2) carries prose in its
  "Decomposition and sequencing" section attributing implementation order, next-issue choice, branch
  strategy, and commit structure to "`ship-it`'s" job, with no broken link involved. Left as-is, per
  the same precedent as (3) and as Step 2's own `artifacts/lab-it.md` prose — flagged here, not
  corrected, since it is content reconciliation rather than a broken pointer.
- **Validation performed:** full re-read of every new and modified file; a diff of each moved rule
  file against its pre-move committed content, confirming `commit-boundaries.md` is byte-identical
  and the other four carry only the documented self-/cross-reference and empty-ready-set changes;
  a repository-wide search for `ship-it/rules/{review-gates,commit-boundaries,verification,
  issue-closure,sequencing}.md` confirming zero remaining references outside `plan.md`'s own
  historical mapping table and the untracked `skills-audit.md`; a repository-wide search for bare
  `` `rules/milestone-completion.md` ``/`` `rules/release.md` `` references inside `implement-it/`
  confirming none remain unprefixed; a targeted search for "`ship-it`" combined with branch
  readiness/Gate 1/Gate 2/commit/verification/issue-closure language across `skills/` confirming no
  remaining stale ownership claim; `git diff --check` clean; relative Markdown links in every
  touched `README.md`/dossier confirmed to resolve; YAML frontmatter of both `SKILL.md` files parsed
  successfully. Seven bounded static walkthroughs run against the actual file content (single-issue
  implementation through both gates, verification, push, and closure; a milestone where B and C
  become ready after A, recommend-and-wait; open-but-blocked issues vs. zero-open-issues before any
  `ship-it` handoff; implementation with and without a stack companion; PR preparation and approved
  creation through to the human-merge stop; a delivery correction within a closed issue's approved
  scope, and a genuinely new-scope correction routed to `plan-it`; continued release behavior with
  every relocated reference resolving) — all traced correctly through the new files with no
  coherence gap found. This is source validation from static walkthroughs, not runtime or consumer
  proof — no skill was actually invoked, no PR or milestone was created, and no consuming project was
  touched, per this step's authorization scope.

**Corrected.** One correction pass on top of the implementation commit
`40c7b9b374894d2e9cbb59c9f6cc37661dd8d1be`, addressing three findings against `implement-it` and
`ship-it`:

1. **Authorization and CI-correction ownership.** Replaced every instance of wording that treated
   `ship-it`'s own investigation or scope determination as sufficient to authorize a delivery
   correction (`implement-it/SKILL.md`'s "What this skill is," "What it does not own," and "Delivery
   corrections"; `ship-it/SKILL.md`'s "Composition" and "What it owns"; `ship-it/rules/
   milestone-completion.md`'s "CI failure on an open milestone PR" intro and steps framing, "Cross-
   rule dependencies," and "What this rule does not do"). The human authorizes; `ship-it`
   investigates, explains, and requests any missing authorization; `implement-it` performs the
   authorized correction using project guidance and applicable stack/implementation skills; new-scope
   findings still route to `plan-it`'s discovered-work intake; `ship-it` resumes delivery afterward.
   Corrected the CI-failure section's step attribution: steps 1–5 (investigate, determine scope, ask
   for and secure authorization, route new scope) are `ship-it`'s; only step 6 (performing the
   correction) is `implement-it`'s, and only once authorized — the prior text wrongly attributed
   steps 4 onward to `implement-it`. `implement-it/SKILL.md`'s "Delivery corrections" now explicitly
   states that `ship-it`'s scope determination is necessary but never sufficient by itself, and that
   this skill accepts the entry only once human authorization actually accompanies the handoff.
   `ship-it/rules/milestone-completion.md`'s "Milestone PR creation" was also corrected: an existing
   request to check readiness or create the PR already authorizes preparing the proposal (steps 1–3)
   without a redundant "may I start" question, while explicit approval of the exact title/base/head/
   body (step 4) before creation is preserved unchanged.
2. **Entry-condition reconciliation.** `implement-it/SKILL.md`'s "What this skill is" no longer
   restricts entry to an issue "produced by `plan-it`"; its "Entry contract" now points to `plan-it`'s
   actual `rules/issue-conventions.md` and `rules/review.md` instead of an undefined "`plan-it`'s
   entry contract," states the ordinary-issue prerequisite applies "for ordinary implementation
   work" specifically, and adds that an authorized delivery correction is a separate entry route
   needing no issue at all — reconciling the two without contradiction, and without requiring
   recreating or replanning a valid issue. `ship-it/SKILL.md`'s "What this skill is" and "Pipeline
   position" no longer state a single shared precondition ("once `implement-it` has closed every
   issue"); they now distinguish three entry points with different prerequisites — PR-readiness/
   creation (zero open issues, re-checked fresh), investigation/continuation on an already-open PR
   (starts from the PR's own state, no re-required issue count), and post-merge closure/release
   (starts from the human's merge confirmation and authorization, independent of any `implement-it`
   session history) — and state plainly that each checks GitHub's actual current state rather than
   requiring proof of a prior `implement-it` session. `ship-it/README.md` and `implement-it/README.md`
   received the matching narrative corrections.
3. **Blocked-versus-completed correction.** Replaced remaining uses of an empty dependency-ready set
   as sufficient for PR-readiness handoff with the actual condition, zero open issues, distinguished
   from an empty ready set that can still hold open, blocked issues:
   `implement-it/SKILL.md`'s "Pipeline position" and its `sequencing.md` rule-index entry;
   `ship-it/rules/milestone-completion.md`'s "Where this phase starts," "The three conditions" item
   1, "Cross-rule dependencies," "What this rule does not do," and "Do / Don't."

**Validation performed:** full re-read of every corrected file; a repository-wide search for
"investigation authorizes," "its investigation," "ready set is actually empty," "ready set comes
back empty," "dependency-ready set is genuinely empty," "produced by `plan-it`," and "`plan-it`'s
entry contract," confirming zero remaining matches; `git diff --check` clean; YAML frontmatter of
both `SKILL.md` files parsed successfully. Six focused static walkthroughs run against the corrected
files: an approved issue authored outside `plan-it` (accepted without replanning, per the actual
quality/approval bar it must meet); an authorized correction to a closed issue versus the same
correction without authorization (the former proceeds through `implement-it`'s lifecycle, the latter
has nothing for `implement-it` to perform); an existing open PR's CI failure investigated and
continued after a follow-up issue reopens the milestone's issue count (not blocked by the
reintroduced open issue, since PR investigation/continuation doesn't re-require zero open issues); a
post-merge release entry with no prior `implement-it` session history in the conversation (proceeds
from the human's merge confirmation and authorization alone); open-but-all-blocked issues correctly
reported as blockers, not handed to `ship-it`, versus a genuinely zero-open-issues milestone that is;
and a PR-creation request proceeding directly to proposal preparation with no redundant "may I
start" question, then stopping for explicit approval of the exact title/base/head/body before
creation. All six traced correctly through the corrected files with no coherence gap found. This is
source validation from static walkthroughs, not runtime or consumer proof — no skill was actually
invoked and no issue, PR, or release was created. Test policy, commit rules, and release mechanics
are unchanged by this pass; `review-it` remains unbuilt and outside Gate 1, per Step 4's own pending
boundary.

### Step 4 — Establish `review-it`, integrate before Gate 1

- **Outcome/boundaries.** `review-it` exists as a standalone skill, callable independently of
  `implement-it`; `implement-it/rules/review-gates.md`'s Gate 1 consumes its result; the same
  standalone call is also what `implement-it` uses during an authorized delivery correction
  (§2.2/§3.1) — one capability, two trigger points, not a second procedure.
- **Affected files.** New: `review-it/SKILL.md`, `README.md`, `rules/*.md` (the §3.1 checklist,
  authored to item-level detail here). Modified: `implement-it/rules/review-gates.md` (Gate 1's
  third bullet), `implement-it/SKILL.md` (routing table gains `review-it`).
- **Preserved vs. changed.** Gate 1's approval mechanics unchanged. New: the substantive checklist
  and its staleness rule (§3.1).
- **Dependencies.** Step 3 (Gate 1 must already live in `implement-it`); §3.1's category list
  agreed here — item-level wording is this step's own authoring output, reviewed at this step, not
  presumed final by virtue of §3.1's outline.
- **Acceptance criteria.** `review-it` runs standalone against an arbitrary worktree/branch/PR with
  no `implement-it` context; it never edits source or mutates GitHub/live state; `implement-it`'s
  Gate 1 report cites `review-it`'s result explicitly; a correction after a `review-it` pass
  triggers a scoped re-review before Gate 1 can stop again.
- **Validation (static).** Standalone `review-it` invocation directly on a branch/PR; `implement-it`
  invoking `review-it` before Gate 1, finding issues, fixing them, re-reviewing, then a clean stop.
- **Result to present.** New `review-it` skill and the updated Gate 1 text, for review.

**Implemented.** Starting point: branch `main`, HEAD `b2fad42f1e4e73e482e7a49921bed6e47b1795a7`
(the commit recording Step 3's Control Room approval), working tree clean except the three
pre-existing untracked files (`control-room-responsibilities.md`, `skills-audit.md`,
`subagents.md`), left untouched.

- `review-it/SKILL.md`, `README.md`, and `rules/{scope.md,checklist.md,verification.md}` created
  new. `review-it` is a standalone skill: it establishes its review target, comparison baseline
  where one applies, intended scope, and available evidence from the request and repository before
  running any check (`rules/scope.md`), asking the human only when unresolved ambiguity would
  materially change the review; it requires no prior `implement-it` session and no
  `plan-it`-authored issue. `rules/checklist.md` authors §3.1's ten categories to item-level
  inspection instructions, each skip-if-inapplicable rather than skip-by-default, with an explicit
  "what this review does not flag" list guarding against invented or speculative findings.
  `rules/verification.md` states the verify-before-reporting standard (a finding is traced to
  concrete evidence, never a suspicion stated as fact — the same non-negotiable
  `skills-audit.md`'s cross-skill review comparison already documents), the diagnostic-execution
  boundary (existing project tests/linters/static analysis may run to confirm a concern; this is
  execution with local side effects, not read-only inspection; an unavailable or unsafe diagnostic
  is reported as a limitation, never skipped silently or guessed at), the staleness rule (a finding
  or clean result is tied to the commit/diff state checked, and a material change afterward
  invalidates it for that surface), and the required report shape (reviewed target and state,
  confirmed findings with location/evidence/consequence, verification performed versus evidence
  supplied by others, material limitations, and a scoped clean result when warranted). `SKILL.md`
  states the reviewer boundary directly: `review-it` reports, and never edits application code,
  applies formatting fixes, commits, pushes, approves a gate, merges, or mutates GitHub or other
  live state — every correction returns to `implement-it`. Its "Ownership and handoff" section
  explicitly excludes guide review, issue/plan-synthesis review, investigation discipline, and
  commit-plan review, naming `document-it`, `plan-it`, `lab-it`, and `implement-it` as their owners,
  per §2.3/§3.1's "does not absorb other skills' specialized reviews."
- `implement-it/rules/review-gates.md`: Gate 1 gains its agreed third stop condition —
  `review-it`'s pass against the completed implementation is either clean, or its findings have
  been resolved and re-verified — and a new "Consuming review-it's result" section states how to
  invoke it (standalone, against the completed working tree, once verification is otherwise
  complete) and how to handle each outcome: a clean pass proceeds to the Gate 1 report; a finding
  within this skill's authorized scope is fixed and re-reviewed, scoped to the affected surface,
  before Gate 1 can rely on it again; a finding that reveals a genuine unresolved decision routes to
  the existing "when to stop and ask" rather than being resolved silently. Gate 1's approval
  mechanics — the report, then explicit human approval — are otherwise unchanged; a `review-it`
  result is stated as evidence the report cites, never as authorization by itself. The Do/Don't list
  gained matching entries.
- `implement-it/SKILL.md`: "What it owns" now states that Gate 1 invokes `review-it` and consumes
  its result as the third stop condition; "What it does not own" gained an explicit line that
  `review-it` owns the checklist and the finding, this skill invokes it and fixes what it finds;
  "Delivery corrections" and "Composition" both state that an authorized delivery correction invokes
  `review-it` the same standalone way before that correction's own Gate 1 — the second invocation
  point from §3.1; the "Rules" index gained a `review-it` entry routing to the skill.
  `implement-it/README.md`'s lifecycle list and "Ownership" section received the matching minimal
  correction.
- `ship-it/rules/milestone-completion.md`'s "CI failure on an open milestone PR" step 6 — where
  `implement-it` performs the authorized correction through its own lifecycle — now names the
  `review-it` invocation before that correction's Gate 1, reconciling this live cross-reference with
  `implement-it`'s own updated text rather than leaving it to drift.
- `plan-it/rules/review.md`'s "Responsibility boundaries" transitional statement — "independent
  implementation review — planned as `review-it`, not yet built in this repository" — is corrected
  to name `review-it` as the actual owner, per this step's explicit instruction to remove every
  transitional not-yet-built statement.
- **Validation performed:** full re-read of every new and modified file; YAML frontmatter of
  `review-it/SKILL.md` parsed successfully; a repository-wide search for "not yet built," "planned
  as," and "does not exist" confirming no remaining transitional `review-it` statement anywhere
  under `skills/`; a link-resolution check confirming every relative Markdown link in the new and
  modified files resolves from the file that contains it; `git diff --check` clean. Eight bounded
  static walkthroughs run against the actual file content: a standalone branch/PR review with no
  prior `implement-it` session and no `plan-it`-authored issue; a request with no scope evidence
  available, producing an explicit reported limitation rather than an inferred, silently-approved
  scope; a suspected defect traced to its actual code path and dropped, not reported, once the
  evidence didn't support it; a confirmed finding fixed by `implement-it` and re-reviewed, scoped to
  the affected surface, before Gate 1's stop; a material change made after a clean `review-it` pass
  invalidating that pass for the changed surface, per the staleness rule; an authorized delivery
  correction with no open issue, `review-it` running the identical standalone way; a review with no
  stack companion installed, running the full checklist and skipping only the stack-specific
  sub-checks; and an unavailable diagnostic (no discoverable test command, or one needing
  credentials this session lacks) reported as an explicit limitation rather than skipped silently or
  guessed at. All eight traced correctly through the actual file content with no coherence gap
  found. This is source validation from static walkthroughs, not runtime or consumer proof — no
  skill was actually invoked, no branch or PR was reviewed, no GitHub state was touched, and no
  consuming project was refreshed, per this step's authorization scope.
- **Departure from the step's own outline, noted for transparency.** The outline above's "Affected
  files" line named only `implement-it/rules/review-gates.md` and `implement-it/SKILL.md` as
  modified; the task's own governing instructions (§5's "Reconcile affected references") separately
  called for minimal related README and live cross-reference corrections and for removing every
  transitional not-yet-built statement, which is why `implement-it/README.md`,
  `ship-it/rules/milestone-completion.md`, and `plan-it/rules/review.md` were also touched — each a
  minimal, single-purpose correction traceable to that same instruction, not scope drift.
- **No unresolved material issue from this step.** §7's remaining open items (canonical
  issue-definition storage; the completed-issue-boundary reuse-eligibility rule) are unchanged and
  stay Step 5's own scope.

**Corrected.** One correction pass on top of the implementation commit
`8dc3eaec11b52b829b54e7e224b1b0daae809ec4`, addressing four findings against `review-it` and
`implement-it`:

1. **Gate 1's review-input and outcome contract.** `implement-it/rules/review-gates.md`'s
   "Consuming review-it's result" previously said this gate always supplies "the approved issue" as
   `review-it`'s intended scope, unconditionally requiring an issue and contradicting the authorized
   delivery-correction route. Corrected to supply the approved issue for ordinary implementation
   work, or the explicitly authorized correction scope and its supporting evidence for a delivery
   correction; Gate 1's own first stop-condition bullet received the matching correction, without
   weakening it — an approved scope, from one of those two sources, is still required either way. A
   new fourth outcome bullet handles a material review limitation explicitly: obtain the missing
   evidence and request a fresh pass when it's actually obtainable from this skill's own context;
   otherwise report the specific blocker as a stop, per "When to stop and ask," never as a silent
   gap or an implied clean result. An optional absent artifact `review-it` itself treated as
   inapplicable does not by itself trigger this. A closing sentence states plainly that stopping to
   ask about a limitation or finding is not, by itself, Gate 1's approval — the gate's own explicit
   human approval of the complete report is still required afterward. The Do/Don't list gained
   matching entries.
2. **The authorized-change exemption, narrowed.** `review-it/rules/checklist.md`'s "Accidental
   scope expansion" section and its "What this review does not flag" summary previously exempted an
   authorized change from review broadly. Corrected so an explicitly authorized scope change is
   exempt only from Accidental scope expansion's own finding — never from Correctness, Security,
   Data integrity, Likely regressions, Architectural fit, Maintainability, Project/stack convention
   compliance, or Test adequacy. A defect discovered in an authorized change is now stated as
   reported exactly as it would be anywhere else in the diff; the authorization approved the work
   happening, not its correctness or safety.
3. **Stack-aware review without a custom companion, preserved.** `review-it/rules/scope.md`'s
   "Discover applicable conventions" and `rules/checklist.md`'s "Project and stack convention
   compliance" previously said a missing stack companion skips its informed sub-checks without
   distinguishing which ones those actually are, reading as license to skip applicable framework
   checks generally. Corrected: only the specific sub-check that depends on a custom companion's own
   rules, with no other available authoritative source, is skipped; framework and technology
   conventions are otherwise discovered the same way project conventions are — from project
   instructions, configuration, and established repository usage — and a finding states whether it
   rests on an established project requirement or on general technical reasoning with no such
   backing, rather than presenting the latter as a discovered project rule.
4. **Review target, coverage, and identity, made precise.** `rules/scope.md`'s comparison-baseline
   procedure previously defaulted every branch review to the trunk merge-base regardless of the
   branch's actual intended target, and treated a branch's configured upstream/tracking branch as
   valid evidence of that target. Corrected — see this step's own subsequent correction pass below,
   which supersedes both of those points: an explicit request controls the comparison outright, then
   an associated PR's declared base, then other reliable integration-target evidence; a configured
   upstream/tracking branch is explicitly excluded, since it names where a branch's own commits push,
   not what it merges into; trunk is a last-resort fallback; and the diff is taken from the
   merge-base with the resolved base, not the base's current tip. The same section states that a
   worktree review's in-scope content includes staged, unstaged, and untracked files, that an
   untracked file needs its own direct inspection since a `HEAD`-relative diff never surfaces one,
   and that no file is ever staged or otherwise mutated merely to bring it into view.
   `rules/verification.md`'s "Staleness" section is renamed "Staleness and review identity." Its
   original description here — that a committed target's identity is its commit SHA alone — was
   itself inaccurate for a branch or PR review and is corrected by this step's subsequent correction
   pass, below, to also record the resolved base, the comparison-start SHA, and the comparison
   method; an isolated commit reviewed with no comparison is still identified by its SHA alone. A
   dirty worktree's identity remains `HEAD` plus the actual diff/untracked-content identity actually
   reviewed, since `HEAD` alone cannot distinguish two different dirty states. None of this is a
   registry or durable review-storage mechanism — only each invocation's own report stating what it
   checked. A material change invalidates the prior pass for that surface even when `HEAD` doesn't
   move. A scoped re-review names the surface it actually rechecked and must not imply it
   independently rechecked the whole implementation; the "Reviewed target and state" report-shape
   bullet was corrected to match.
- **Validation performed:** full re-read of every corrected file; a repository-wide search
  confirming no other file restated the old broad authorized-change exemption or the old
  unconditional trunk-baseline default; `git diff --check` clean; YAML frontmatter of
  `review-it/SKILL.md` parsed successfully; every relative Markdown link in the corrected files
  confirmed to resolve. Static walkthroughs re-run against the corrected files: an authorized
  delivery correction with no open issue, traced through `review-it`'s intended-scope supply and
  Gate 1's stop condition without invoking any issue-only wording; a request with a genuine missing-
  evidence gap, ending in an explicit reported limitation and, where unobtainable, a stop-and-ask —
  never a false clean result; an authorized scope expansion that also contains a separate security
  defect, with the defect still reported despite the scope authorization; a project with framework
  conventions but no custom stack companion, still catching a framework-convention violation through
  project instructions and established usage; a branch whose real target is another feature branch,
  correctly diffed against that branch rather than trunk; and a worktree with staged, unstaged, and
  new untracked implementation files, followed by a material edit to an already-reviewed file with no
  new commit, correctly triggering staleness despite `HEAD` being unchanged. All traced correctly
  through the corrected file content with no coherence gap found. This is source validation from
  static walkthroughs, not runtime or consumer proof — no skill was actually invoked, no branch,
  worktree, or PR was reviewed, and no GitHub or live state was touched. The review procedure's
  overall shape, the testing policy, diagnostic-execution boundaries, specialized review ownership,
  and the publication-approval mechanics are otherwise unchanged by this pass.
- **No unresolved material issue from this correction.** §7's remaining open items are unchanged and
  stay Step 5's own scope. At the end of that correction pass, Step 4 was pending Control Room
  review; the subsequent correction and final approval are recorded below.

**Corrected (comparison-base and comparison-identity precision).** A second, bounded correction pass
on top of commit `7750870bb1b1251f256649352fa380db3037b058`, addressing the one remaining
review-comparison issue in `review-it`; the Gate 1, authorization-exemption, and stack corrections
above passed Control Room review and are preserved unchanged. Two findings corrected, both in
`rules/scope.md` and `rules/verification.md`:

1. **Comparison-base selection.** The prior pass's discovery order treated a branch's configured
   upstream/tracking branch as valid evidence of its intended integration target. Corrected: an
   explicit request comparison controls the review outright; otherwise an associated PR's declared
   base, or other reliable evidence of the actual intended target; a configured upstream/tracking
   branch is explicitly excluded, since a feature branch commonly tracks its own remote counterpart
   rather than its intended merge target; trunk is used only as a last-resort fallback. The ordinary
   comparison now diffs from the merge-base with the resolved base, not the base's current tip, and a
   requested comparison that differs from a PR's actual declared base is labeled as such rather than
   presented as the PR's own.
2. **Comparison identity.** The prior pass's staleness rule claimed a committed target — including a
   branch or PR — is identified by its head commit SHA alone. That claim was itself inaccurate: the
   identical head diffed against two different bases produces two different diffs. Corrected to
   record the head SHA, the resolved base, the comparison-start (merge-base) SHA where one applies,
   and the comparison method; an isolated commit reviewed with no comparison is still identified by
   its SHA alone, and dirty-worktree content identification is unchanged. A changed base or
   comparison — not only a changed `HEAD` — now explicitly invalidates a prior clean result. A scoped
   re-review states its checked surface alongside this same state/comparison identity, not the
   surface alone. No registry, persistence mechanism, or new tooling was introduced.

- **Validation performed:** full re-read of both corrected files; `git diff --check` clean; every
  relative Markdown link in the corrected files confirmed to resolve; a repository-wide search
  confirming no other file (`SKILL.md`, `README.md`, `checklist.md`, `implement-it/rules/
  review-gates.md`) restated the corrected upstream-tracking or commit-SHA-alone claims, so no
  further cross-reference correction was needed. A disposable Git repository (created and destroyed
  outside the working tree) verified the underlying Git mechanics the corrected text depends on: a
  pushed feature branch tracking its own remote counterpart, confirmed to produce an empty, useless
  diff against that counterpart; an explicit comparison against a parent feature branch via their
  merge-base, confirmed to isolate exactly the child branch's own introduced change; the identical
  head commit diffed against two different bases (the parent branch versus trunk), confirmed to
  produce two different diffs — trunk's additionally, silently including the parent branch's own
  commit; and a material edit to an already-reviewed file with no new commit, confirmed to leave
  `HEAD` unchanged while the reviewed content changed, with the resulting scoped re-review able to
  state both the checked surface and the full state/comparison identity together. This is Git-
  mechanics verification of the corrected procedure's claims, not proof from invoking `review-it`
  itself — the skill was not invoked, and no consuming project was touched.
- **No unresolved material issue from this correction.** §7's remaining open items are unchanged and
  stay Step 5's own scope. At the end of that correction pass, Step 4 was pending Control Room
  review; final approval is recorded below.

**Approved.** Step 4 passed Control Room review at commit
`dfad7309aaac5747234a462094af050a371b3e84`, and the user confirmed proceeding and recording that
approval. No blocking findings remain in the reviewed changes. Validation comprises source review
and Git-mechanics checks; no consuming-project invocation of `review-it` has been performed.
Step 5 is next. Its implementation has not started, and its two open decisions in §7 remain
unresolved; this approval does not settle either decision or authorize Step 5 implementation.

### Step 5 — Strengthen recovery, adopt the approved verification policy

- **Outcome/boundaries.** The §3.2 recovery additions and the §3.4 verification-policy decisions —
  as actually resolved at this step's review, not as defaults this step invents — are applied to
  their owning files.
- **Affected files.** `implement-it/rules/verification.md` (the completed-issue-boundary reuse-
  eligibility rule — the only open item left in §3.4 — and worktree provenance),
  `rules/review-gates.md` (approval validity), `rules/issue-closure.md`; `plan-it/rules/sequencing.md`
  (interrupted-batch-creation recovery), `rules/issue-conventions.md` (recording the durable-storage
  deferral, per the user's settled decision, not a location); `ship-it/rules/milestone-completion.md`
  and `rules/release.md` (partial-mutation re-query only — PR-readiness stays three conditions;
  §3.4's correction removed the earlier, mistaken fourth-condition framing, so there is no condition
  count to update here).
- **Preserved vs. changed.** This step is entirely deliberate change — every edit traces to §3.2 or
  §3.4 above; nothing here is a pure move.
- **Dependencies.** Steps 2-4 complete (files must exist at their new locations); the specific open
  decisions in §3.2 (canonical issue-definition storage; which provenance signals are reliably
  available in a given project) and §3.4 (the reuse-eligibility rule) resolved before their
  corresponding edits — this step cannot silently fill them in.
- **Acceptance criteria.** A worktree-provenance check exists, uses reliable provenance rather than
  appearance, and is exercised by a scenario with pre-existing uncommitted changes that must be
  preserved; partial-mutation re-query exists for both `plan-it`'s issue batches and `ship-it`'s
  milestone/release mutations; canonical issue-definition durable storage is explicitly recorded as
  deferred, not resolved — no durable location is implemented by this step, per the user's settled
  decision (below); PR-readiness's three conditions are undisturbed by the reuse-eligibility rule's
  resolution.
- **Validation (static).** Interrupted-worktree resume, including a case with pre-existing unrelated
  changes that must survive untouched; interrupted issue-batch-creation resume; approval-then-
  material-change resume; PR readiness against an open PR with red CI; a milestone with open issues
  that are all blocked (not closed) confirming no premature handoff to PR readiness.
- **Result to present.** Diff plus an explicit list of which audit findings (§Section 3 scenarios,
  #10, #13, #21) are now resolved and how.

**Implemented.** Starting point: branch `main`, HEAD `ace3453596624c1baf6295549de4fc7bd96e9480`
(the commit recording Step 4's Control Room approval; that commit itself left this step's two
decisions in §7 open — the user settled them directly in the handoff that authorized this step's
implementation, not through a separate commit, and that settlement is distinct from Control Room
approval of this step's own implementation, which remains pending), working tree clean except the
three pre-existing untracked files (`control-room-responsibilities.md`, `skills-audit.md`,
`subagents.md`), left untouched.

**Decisions applied**, both recorded here as the user's explicit settlement, superseding the prior
open-item wording in §3.2/§3.4/§7:

- **A. Canonical issue-definition durable storage deferred, not resolved.** No `issue-plan.md`-
  equivalent file, approval registry, or other persistence mechanism is introduced by this
  migration. Retained instead: the simple recovery procedure below.
- **B. Full-suite result reuse permitted at the completed-issue boundary.** The full suite before
  each issue's Gate 1 remains required, whether implementing one issue or working through a
  milestone; after commits are assembled, an earlier successful full-suite result may satisfy
  completed-issue verification only once its continued applicability is established — otherwise, run
  the full suite
  again.

**Owning files and behavioral changes:**

- `implement-it/rules/verification.md` (primary owner of the reuse rule) — the lifecycle diagram and
  the "two full-suite runs" framing now state both checkpoints as required while allowing the
  completed-issue one to be satisfied by reuse; a new "Completed-issue verification: run or reuse"
  section states the four reuse conditions (identifiable evidence of an actual complete run;
  final-content equivalence, never inferred from a clean worktree/unchanged `HEAD`/successful commit
  command alone; equivalent relevant test inputs and environment, including consumed commit
  metadata; no unresolved limitation), the practical, proportionate evidence standard with no
  mandatory snapshot system or exhaustive inventory, the requirement to run the full suite again on
  any relevant change or established-limitation failure (including a post-Gate-1 correction, which
  a narrower per-commit check can never substitute for), and the honest-reporting requirement (a
  reused result is never presented as freshly executed). The "Default commit-building loop" section
  and its heading were reconciled to route to this rule rather than restate "run once"
  unconditionally; isolation verification's final checkpoint (step 6) was reconciled to allow reusing
  its own last per-commit isolated run only under the same conditions; the cache/impact-analysis
  section gained an explicit statement that a cache hit or impact-analysis-selected subset can never
  by itself satisfy the reuse rule's first condition; the Do/Don't lists were updated to match. A new
  "Preserve pre-existing worktree changes" subsection (under "Discover the verification starting
  state") implements decision-adjacent recovery item A of §3.2: reliable provenance (`git reflog`,
  the session's own recorded start point, an explicit human statement) over appearance, asking only
  when unresolved provenance would materially affect safe continuation.
- `implement-it/rules/review-gates.md` — a new "Approval validity before Gate 2 and before push"
  section: a material change requires the affected review/approval to be renewed (routing to
  `review-it`'s own staleness contract where the change affects a surface it already reviewed);
  ordinary staging/assembling of unchanged, already-approved content must not automatically
  invalidate Gate 1 merely because `HEAD` or the remaining diff changed; remote commit reachability
  proves presence, not verification or authorization. Gate 1's first stop-condition bullet and the
  Do/Don't lists were reconciled to match.
- `implement-it/rules/issue-closure.md` — "Push readiness" step 3 now confirms approval validity
  (routing to `review-gates.md`) before asking to push; the closing comment's verification-results
  bullet now requires stating plainly when the completed-issue checkpoint was satisfied by reuse,
  naming the earlier run.
- `plan-it/rules/sequencing.md` — a new "Resuming an interrupted batch creation" subsection under
  "Dependency-safe GitHub creation": re-query GitHub for members an interrupted attempt may already
  have created (never by title alone; a failed/timed-out query is not proof nothing happened),
  validate matches against their approved canonical definitions, create only the remaining approved
  members, and — when canonical definitions, scope, or approval can no longer be reliably
  established — explain what's missing and ask the human rather than reconstructing the batch from
  guesses or inferring missing members from what already exists.
- `plan-it/rules/issue-conventions.md` — "Canonical definitions" gained the explicit deferral
  statement (decision A) and a pointer to the recovery procedure above.
- `ship-it/rules/milestone-completion.md` — "Milestone PR creation" step 2 strengthened: identity by
  head branch, not title alone; a failed/timed-out query re-tried before concluding creation is still
  needed; a match validated against the approved proposal, never duplicated. "Closing the milestone"
  gained a re-query-before-retry step: a prior successful closure is validated and reported, not
  re-mutated. Do/Don't updated to match.
- `ship-it/rules/release.md` — step 5 gained a re-query-before-publishing step covering a partial
  prior outcome (a tag pushed with no release yet, or an ambiguous lost response), validating what
  already exists against the step-4-approved content and performing only the remaining steps, never
  recreating/retargeting/overwriting/deleting an existing correct resource. Step 6 now treats a
  partial outcome (tag without release, or vice versa) as remaining work to finish, not a failure to
  restart. Do/Don't updated to match.
- `implement-it/SKILL.md` — the `verification.md` and `review-gates.md` rule-index entries updated
  minimally to name the reuse rule, worktree provenance, and approval-validity check.

**Validation performed:** full re-read of every modified file; `git diff --check` clean; YAML
frontmatter of `implement-it/SKILL.md` parsed successfully; every relative Markdown link in the
modified files confirmed to resolve; a repository-wide search confirming no file still asserts an
unconditional "run the full suite once" requirement, introduces a durable issue-definition storage
mechanism, or claims a commit SHA alone identifies a branch/PR review (unaffected by this step, and
unchanged). A disposable Git repository (created and destroyed outside the working tree) verified
the concrete git-mechanics claim behind reuse condition 2: diffing an uncommitted "pre-Gate-1
tested" change against its base, then reassembling that identical content into two separate commits,
produced a byte-identical combined diff (confirmed by content hash) — establishing that comparing
the pre-Gate-1 diff against the assembled commits' combined diff is a real, reliable technique for
confirming final-content equivalence; a follow-up edit made after that point correctly produced a
diverging hash, confirming the same technique correctly disqualifies reuse when content actually
changed. Eight bounded static walkthroughs run against the actual file content: a successful
full-suite run followed only by assembling identical content into commits (reuse justified); changed
code, dependencies, or generated inputs, or missing prior evidence (fresh run required); a cached or
impact-analysis-selected result unable to establish complete prior execution (reuse condition 1
fails); interrupted work with unrelated pre-existing changes surviving untouched; a GitHub mutation
that succeeded before its response was lost, validated on resume rather than duplicated (traced
through `plan-it`'s batch recovery, `ship-it`'s PR-creation and closure re-query, and `release.md`'s
partial-publish re-query); missing canonical definitions or approval evidence producing an explicit
ask rather than an invented remainder; a material scope change invalidating the relevant approval,
distinguished from ordinary approved commit construction which does not; and the pre-existing
delivery constraints (blocked-issue milestones are not complete; red PR CI blocks merge) confirmed
still intact and untouched by this pass. All eight traced correctly through the actual file content
with no coherence gap found. This is source validation from static walkthroughs plus a bounded
git-mechanics check, not runtime or consumer proof — no skill was actually invoked, and no real
issue, PR, milestone, tag, or release was created for testing, per this step's authorization scope.

**Findings addressed:** none surfaced beyond the two settled decisions and the reconciliation work
they required — this pass implements the outline's own proposals (§3.2's remaining rows, §3.4) as
designed, with no unexpected defect discovered in the files it touched.

**Durable issue-definition storage remains explicitly deferred** (decision A above) — this is a
recorded scope boundary, not an oversight; no location, creation/update timing, approval
relationship, mapping, or retirement mechanism is introduced by this or any step of this migration.

**Corrected.** One bounded correction pass on top of the implementation commit
`297036f1aa36aff934c82fcc2fc65e96ab2827ab`, addressing four findings against the recovery and
reuse rules above. Both settled decisions (A and B) are preserved unchanged — no durable
issue-planning file or registry, and conditional full-suite reuse at the completed-issue boundary.

1. **Content recovery separated from approval evidence.** `plan-it/rules/sequencing.md`'s
   "Resuming an interrupted batch creation" previously allowed canonical definitions, scope, and
   approval to all be reconstructed from a created issue's body once checked against
   `rules/issue-conventions.md`'s format. A live issue's conformity with that format proves what got
   published, never that a human approved it or approved it as part of the original batch. Corrected
   to require independently available evidence of the actual approval (this session's own record, or
   an explicit human statement) before treating a recovered definition as still approved; a
   definition recovered without that evidence is a **draft** routed back through `rules/review.md`'s
   normal review and approval gates, not an already-approved member to create directly. When
   canonical definitions or approval evidence can't be reliably recovered, this rule already asked
   the human rather than guessing — that behavior is preserved, now correctly gated on approval
   evidence specifically, not merely on published content. No persistence machinery introduced.
2. **The approval-validity check made reachable on every continuation path.** `implement-it/rules/
   issue-closure.md`'s "Push readiness" previously ran the "Approval validity before Gate 2 and
   before push" check (`rules/review-gates.md`) only on the path that still needed to push — the
   "already remote" path skipped straight to "Ask first," bypassing it. Corrected so step 3 confirms
   approval validity on both paths before advancing toward closure; the substantive check stays owned
   by `review-gates.md`, this rule only routes to it. For a pending push, applicability is now
   re-checked immediately before the actual push mutation even when authorization was already granted
   earlier in the session — a still-applicable authorization is preserved without a redundant
   question; one that no longer applies is a stop, not a silent reuse. Missing or stale approval
   evidence is reported and resolved through `review-gates.md`, never silently assumed valid because
   commits are already remote.
3. **Discovering an existing PR separated from validating a recovered creation attempt.**
   `ship-it/rules/milestone-completion.md`'s "Milestone PR creation" step 2 previously required
   validating any found PR against "the approved proposal," which only exists when this workflow
   itself proposed it — a manually created or otherwise independently opened PR has no such proposal
   to validate against. Corrected into three cases: an existing PR is identified and reported from
   repository/head/base and milestone evidence alone, with no prior proposal required to recognize
   it; a PR that is this workflow's own interrupted creation attempt, with its approved proposal still
   available, is validated against that exact title/branches/body; and when the necessary proposal or
   approval evidence is missing, that limitation is reported plainly rather than inventing a proposal,
   duplicating the PR, or silently changing its content. Exact-content approval before any new
   creation (step 4) and the human merge boundary are both unchanged.
4. **The final isolation run reconciled with completed-issue verification.** `implement-it/rules/
   verification.md`'s reuse conditions previously named only the pre-Gate-1 run as reusable evidence,
   while isolation verification's own final checkpoint (step 6) separately permitted reusing its own
   last per-commit run under those same conditions — a run that was never the pre-Gate-1 run, an
   incoherence between the two sections. Corrected: "Completed-issue verification: run or reuse" now
   recognizes two reuse sources — the pre-Gate-1 run (still requiring the diff-equivalence check to
   establish condition 2) and a full-suite run already executed directly against the final committed
   state itself, such as isolation verification's last per-commit run when nothing remained stashed
   afterward (which satisfies condition 2 by construction, since it already ran against exactly that
   content). Conditions 1, 3, and 4 apply to both sources equally. An intermediate isolated run that
   does not correspond to the actual final committed state — superseded by a later commit — cannot
   satisfy this checkpoint under either source; only a run genuinely executed against the final state
   qualifies. Isolation step 6 was reconciled to state this directly rather than vaguely gesture at
   "reuse... under conditions above." The lifecycle diagram, the "two full-suite runs" framing, the
   "Default commit-building loop" closing paragraph, the honest-reporting requirement (now naming
   which specific execution satisfies the checkpoint, never mislabeling an isolation run as the
   pre-Gate-1 run), and the Do list were all generalized to match — one owner
   ("Completed-issue verification: run or reuse") still states the four conditions; nothing else
   restates them. `implement-it/SKILL.md`'s rule-index entry and `plan.md`'s own §3.4/§7 summaries
   received the same minimal correction.

`plan.md` also corrected its own inaccurate claim that commit `ace3453596624c1baf6295549de4fc7bd96e9480`
recorded this step's two settled decisions — that commit recorded Step 4's Control Room approval and
left those two decisions open in §7; the user settled them afterward, directly in the handoff that
authorized this step's implementation, not through a separate commit. Decision settlement and Control
Room approval of this step's own implementation are kept distinct throughout; the storage gap (decision
A) remains explicitly deferred, not resolved, by this correction.

- **Validation performed:** full re-read of every corrected file; a repository-wide search confirming
  no remaining reference to validating a discovered PR against a proposal that may not exist, or to
  reconstructing approval from a created issue's body alone. **This search was incomplete**: it missed
  one remaining narrow-reuse reference — "Default commit-building loop"'s completed-issue-checkpoint
  summary still named only the pre-Gate-1 run as reusable, rather than both sources the owning
  section actually defines. That gap was found and corrected in this step's own follow-up cleanup
  pass, below; it does not indicate a defect in the owning "Completed-issue verification: run or
  reuse" section itself, which already stated both sources correctly at the time. `git diff --check`
  clean; YAML frontmatter of
  `implement-it/SKILL.md` parsed successfully; every relative Markdown link in the corrected files
  confirmed to resolve. Seven bounded static walkthroughs run against the corrected file content: a
  published issue whose content is recoverable but whose human-approval evidence is missing, correctly
  producing a draft routed back through normal review rather than a silently reused approval; commits
  already remote with prior gate evidence missing, correctly stopping at the approval-validity check
  instead of proceeding straight to "Ask first"; existing, still-applicable push authorization reused
  without a redundant question, re-checked immediately before the actual push mutation; a manually
  created PR discovered with no earlier proposal from this workflow, correctly identified and reported
  without inventing or requiring a proposal; an interrupted PR-creation attempt recovered and validated
  against its actually-available approved proposal; the final isolated full-suite run, covering exactly
  the completed committed state with nothing left stashed, directly satisfying the completed-issue
  checkpoint; and an earlier isolated run superseded by a later commit correctly failing to satisfy
  that checkpoint, requiring a fresh or genuinely final run instead. All seven traced correctly through
  the corrected file content with no coherence gap found. This is source validation from static
  walkthroughs, not runtime or consumer proof — no skill was actually invoked, and no real GitHub
  issue, PR, milestone, tag, or release was created or exercised, per this pass's authorization scope.

**Bounded cleanup**, on top of commit `45509d7aaf63b18d637ea42c596ad829ebc4b6b9` (the corrected and
Control-Room-reviewed result): `implement-it/rules/verification.md`'s "Default commit-building loop"
completed-issue-checkpoint summary — the one gap the correction pass's own validation search missed
(see the corrected validation note above) — now names reuse of "an earlier qualifying full-suite
result (the pre-Gate-1 run, or a run already executed directly against the final committed state)"
and explicitly states that "Completed-issue verification: run or reuse" owns the eligibility
conditions, without restating or altering them. A repository-wide search after this edit confirmed
no remaining reference names only the pre-Gate-1 run as reusable anywhere in the repository. This
edit is wording-only: it does not change which content qualifies for reuse, only which section of
the rule states that both sources qualify. This is source review of a small, targeted text change,
distinct from any actual consumer execution — no skill was invoked, and no consuming project was
touched.

**Approved.** Step 5 passed Control Room review at commit
`45509d7aaf63b18d637ea42c596ad829ebc4b6b9`, with this minor wording cleanup applied on top of that
reviewed commit as part of recording the approval, not as new substantive change. No blocking
findings remain in the reviewed changes. Validation comprises source review, static walkthroughs,
and bounded Git-mechanics checks recorded above; no consuming-project invocation of any skill in
this ecosystem has been performed. Durable issue-definition storage remains explicitly deferred, not
resolved, by this approval. Step 6 is next; its implementation has not started, and this approval
does not authorize it.

### Step 6 — Reconcile public documentation, validate the combined ecosystem, prepare publication

**Approved by Control Room** at commit `4247a829e55f260ab86a61daf72ef6193b21979c`, with the user's
confirmation to record the approval. The third correction pass resolved the `ship-it.md`
entry-condition scoping, `review-it.md` comparison-override wording, `implement-it.md`
stack-composition explanation, consumer-exercise prerequisite, and evidence-precision findings. This
is source-review approval — a full re-read, repository-wide searches, `git diff --check`, and bounded
static walkthroughs against the reconciled documentation and the underlying skill contracts; it does
not establish successful consumer execution. Publication of `v2.0.0` requires its own, separate
approval (see the finalized release proposal below).

- **Outcome/boundaries.** `README.md`, `roadmap.md`, `docs/skill-consumption.md` (only if its
  illustrated skill list/paths actually changed), and every `skills/*/README.md` reconciled to the
  six-capability shape in §1. No runtime behavior changes in this step. This step grants no commit
  or publication authority by itself — it only prepares for a later, separately authorized one.
- **Affected files.** `README.md`, `roadmap.md`, `docs/skill-consumption.md` (conditionally),
  `skills/*/README.md`.
- **Preserved vs. changed.** Documentation/publication reconciliation only.
- **Dependencies.** Steps 2-5 complete and internally consistent — a full re-read and scope
  verification (`docs/skill-authoring-methodology.md` §13) precedes this step's own edits.
- **Acceptance criteria.** `README.md`'s pipeline table matches §1's identity; `roadmap.md`'s
  `review-it` bullet is removed or marked done; a repo-wide search finds no stale reference to
  `ship-it` owning what `implement-it` now owns.
- **Validation — planned, not executed in this step or by this plan.** A real `useOrbit` consumer
  install/refresh exercise (`npx skills add` or the project's own `skills:refresh` script against
  this updated source, then one full pipeline pass exercised end to end in that project) and a
  bounded non-Laravel portability check covering all six current portable skills — `lab-it`,
  `document-it`, `plan-it`, `implement-it`, `review-it`, and `ship-it` — activating correctly with
  no stack companion installed, in a sample project that isn't Laravel/Inertia (superseding this
  outline's original "three portable skills" wording, written before `document-it`, `implement-it`,
  and `review-it` existed; see this step's own implementation record for the justified scope). Both
  are scoped here as planned exercises for a later, explicit go-ahead — neither is performed, and no
  consumer is changed, by this plan.
- **Result to present.** Final reconciled documentation diff, plus the two planned exercises' scope,
  for the user's explicit authorization before running them or requesting publication.

**Implemented.** Starting point: branch `main`, HEAD
`891b2ee887917b2145b37f85860697301a5c1db6` (the commit recording Step 5's Control Room approval),
working tree clean except the three pre-existing untracked files (`control-room-responsibilities.md`,
`skills-audit.md`, `subagents.md`), left untouched and unstaged throughout.

**Changed files.** `README.md`, `roadmap.md`, `artifacts/lab-it.md`, `artifacts/ship-it.md`,
`artifacts/plan-it.md`, `skills/laravel-inertia-stack/README.md`. No `skills/*/SKILL.md`, rule file,
or runtime contract was touched — this step is documentation reconciliation only, per its own
authorization scope.

**Documentation decisions:**

- **`README.md` rewritten** to the agreed identity, **Lab. Plan. Implement. Review. Ship — with the
  right stack.** The pipeline table now lists all five stages (`lab-it`, `plan-it`, `implement-it`,
  `review-it`, `ship-it`) with their current results; a new "Document as you go" section states
  `document-it` as an independently available companion, explicitly not a mandatory pipeline stage,
  rather than folding it into the table as a sixth stage. The boring-prompts block gained one
  natural prompt per skill, including `document-it` and `review-it`, which the prior version didn't
  mention at all. "Knowledge boundaries"'s portable-methodology bullet now names all six skills
  instead of the prior three. The Install section's wording was corrected: "choose the skills you
  need, and the coding agent(s) to install them for (`-a/--agent`, e.g. `claude-code`) — that
  selects which agent reads the installed skills, not a set of subagent definitions this repository
  supplies" — replacing the prior "choose the skills and agents you need," which read as though this
  repository might publish subagent definitions alongside skills. Confirmed by inspection: no
  `agents/` directory exists anywhere in this repository, and `docs/skill-consumption.md`'s own
  `-a/--agent` documentation already describes it as a coding-agent target, not a subagent kind —
  the README previously just didn't say so.
- **`roadmap.md`**: the `review-it` bullet under "Future directions" — proposing exactly the
  extraction Steps 2-4 already implemented and Control Room approved — is retired (removed, not
  marked "done in place," since a roadmap of *future* directions has no use for a completed one and
  this isn't a migration log). The Purpose section's verb list ("understanding systems, planning
  work, building with appropriate stack knowledge, and shipping verified changes") is corrected to
  name implementation and review explicitly ("implementing and reviewing changes with appropriate
  stack knowledge, and shipping verified releases"), matching the identity now stated everywhere
  else. Every other future direction (cross-ecosystem comparison, consumption tooling, Project B,
  stack-companion criteria, optional stewardship) is preserved verbatim and unreordered — none of
  them is retired, resolved, or expanded into a committed phase by this pass.
- **`artifacts/lab-it.md` narrowed.** The two guide-authoring workflows ("Document existing
  architecture," "Update an existing architecture guide"), the guide-as-published-artifact section,
  and the four guide-related rule-ownership rows (`doc-style.md`, `template.html`, `review.md`,
  `maintenance.md`) are removed — that architecture belongs to `document-it` now, per Steps 2-5's
  actual code migration, which this dossier's prose had not caught up to. A new §7, "Boundary with
  `document-it`," states the relationship explicitly and in one direction: `document-it` draws on
  this skill's evidence discipline when its own evidence is missing or stale; this skill never hands
  work to `document-it`, and a guide never implies a handoff back. Per the authoring methodology's
  "do not create extra dossiers merely for symmetry" and this migration's own instruction not to
  create one, **no `document-it.md` dossier was created** — `document-it`'s own `SKILL.md` and rule
  files remain its sole operational contract, exactly as they were left by Step 2, and the detailed
  guide-rendering/identity/accessibility reasoning the old `lab-it.md` §6 carried is not relocated
  into a new file; it is superseded by `document-it`'s own rule files where that detail still lives
  operationally. The remaining content — the evidence discipline, the two current workflows, the
  four-stage model (renumbered from five), the `plan.md` claim model, and rule ownership — is
  preserved with only the ownership-boundary correction, not rewritten wholesale.
- **`artifacts/ship-it.md` narrowed**, the larger of the two dossier rewrites. Branch readiness, the
  two review gates (including `review-it`'s Gate 1 invocation), commit architecture, the
  verification model, and issue closure/sequencing — all migrated to `implement-it` by Steps 3-5 —
  are removed from this dossier; a new §2, "Boundary with `implement-it`," states that a
  Backlog/hotfix issue never reaches this skill at all (it terminates entirely inside
  `implement-it`), and that this skill's only upstream input is `implement-it`'s already-closed,
  already-verified milestone work. The retained architecture — three independent entry points (PR
  readiness/creation; investigation/continuation on an open PR; post-merge closure and release),
  the CI-failure/delivery-correction ownership split, and the post-merge lifecycle — was rewritten to
  match the actual corrected split in `skills/ship-it/rules/milestone-completion.md`'s "CI failure on
  an open milestone PR" (this rule investigates, explains, and secures authorization — steps 1-5;
  `implement-it` performs the authorized correction — step 6), verified directly against that file's
  current text rather than assumed from the old dossier's framing. Per the same "no extra dossiers
  merely for symmetry" instruction, **no `implement-it.md` dossier was created**; `implement-it`'s own
  `SKILL.md` and rule files remain its sole operational contract. The rule-ownership table now lists
  only `milestone-completion.md` and `release.md` — the two rule files this skill still owns.
- **`artifacts/plan-it.md`**: three narrow prose corrections, no restructuring — matching the
  "plan-it's own rule content is not restructured, only these handoff pointers change" precedent
  from Step 3. §8's "all of that is `ship-it`'s" (implementation order, next-issue choice, branch
  strategy, commit structure) and "both of which belong to `ship-it` once issues exist" are corrected
  to `implement-it`. §10's "Handoff to `ship-it`" is split into "Handoff to `implement-it` and
  `ship-it`": `implement-it` owns branch readiness, review gates (including the `review-it`
  invocation), commits, verification, and issue closure; `ship-it` owns PR readiness/creation,
  post-merge milestone closure, and release, starting only once a milestone has zero open issues
  remaining.
- **`skills/laravel-inertia-stack/README.md`**: one stale reference — "Bring evidence-backed
  Laravel... conventions into the Build stage" — corrected to "the Implement stage," matching the
  renamed pipeline stage; nothing else in this file needed correction.
- **`docs/skill-consumption.md` — inspected, not changed.** It names no specific skill or skill
  count anywhere; its `-a/--agent`, managed-skill, and refresh-script illustrations already use
  generic placeholders (`<managed-skill-a>`, `<managed-skill-b>`) rather than an enumerated list that
  this migration could make stale. Per this step's own scope ("only where its illustrated skill
  list/paths actually changed"), it is left untouched.
- **`skills/*/README.md` (all six) — inspected, not changed.** Every one of `lab-it`, `document-it`,
  `plan-it`, `implement-it`, `review-it`, and `ship-it`'s `README.md` was already correctly
  reconciled to current ownership during its own extraction/narrowing step (2-4) — full re-read
  confirmed no stale reference to the old `ship-it`-owns-everything or `lab-it`-owns-guides shape in
  any of them. No edit was needed or made.

**Validation performed.** Full re-read of every changed file. `git diff --check` clean. A
Python-based relative-Markdown-link resolution check across every changed file confirmed every
link resolves to an existing path from the file that contains it. Repository-wide searches for
stale ownership: every remaining `` `ship-it` `` mention paired with gate/commit/verification/
closure language, and every remaining `` `lab-it` `` mention paired with guide ownership, resolved
to one of three expected sources — a file this step corrected, a file already correct (confirmed by
direct inspection: `plan-it/README.md`, `plan-it/rules/issue-conventions.md`, `plan-it/rules/
review.md`, `review-it/SKILL.md`, `implement-it/*`, `ship-it/*` all describe current, accurate
ownership), or this step's own excluded scope (`plan.md`'s historical implementation record, and
the three untracked evidence files `skills-audit.md`, `control-room-responsibilities.md`,
`subagents.md`, left untouched and unstaged as required) — no unexpected stale reference found
anywhere else in the repository.

Static walkthroughs were run against the actual owning `SKILL.md`/rule files this step's dossiers
and README now point to, not against the rewritten prose alone: a newcomer following each of
`README.md`'s six boring prompts into the matching skill's own trigger conditions
(`document-it`'s and `review-it`'s prompts in particular, since the prior README never mentioned
either skill); `artifacts/lab-it.md` §7's one-directional `document-it` boundary against
`document-it/SKILL.md`'s own "routing to `lab-it`'s investigation method... when evidence is missing
or stale" and `lab-it/SKILL.md`'s "Ownership and handoff" section, confirming both files describe
the identical one-directional relationship; `artifacts/ship-it.md` §4's CI-failure split traced
step-by-step against `skills/ship-it/rules/milestone-completion.md`'s actual "CI failure on an open
milestone PR" section (steps 1-5 investigate/explain/authorize are `ship-it`'s, step 6 perform is
`implement-it`'s, step 7 resumes), and §3's PR-creation description traced against that same file's
"Milestone PR creation" section; `artifacts/plan-it.md` §6.10's split handoff against
`implement-it/rules/sequencing.md` and `ship-it/rules/milestone-completion.md`'s "Where this phase
starts" diagram, confirming the zero-open-issues boundary between the two skills matches exactly.
All traced correctly with no coherence gap found.

**This is source validation, not runtime or consumer proof.** No skill was invoked, and no
`useOrbit` or other consuming project was touched. This step's own authorized commit and push to
this source repository's `origin/main` is a real GitHub mutation and did occur, per its own
explicit authorization (§6 below) — it is not covered by "no GitHub state was mutated." What did not
occur: any consumer-repository mutation, and any PR, tag, release, or deployment anywhere, per this
step's own authorization scope (§5's boundaries above).

**Remaining findings.** None beyond what was already known and explicitly out of scope: the
`laravel-inertia-stack`/Boost precedence question (§7 item 1) is unaffected by this pass and remains
flagged, not addressed. No new runtime-contract contradiction was found during this reconciliation;
none is reported separately, since none exists to report.

**Deferred consumer-validation options — not the immediate next task.** The user will handle
consumer installation/update manually; a separate `useOrbit` inspection, adoption plan, or formal
exercise of either proposal below is not the immediate next task and is not required to finalize or
publish the `v2.0.0` release proposal (see "Finalized v2.0.0 release proposal" below). Both proposals
are retained here, bounded and separately authorized, as optional validation a human may choose to
run later — not as mandatory next steps:

1. **A real `useOrbit` installation/refresh and end-to-end consumer exercise.**
   - **Prerequisites.** Access to `useOrbit`'s actual local environment — its current
     `.agents/skills/**` real files, `skills-lock.json`, and any tracked agent-discovery symlinks —
     is not assumed obtainable from its GitHub remote alone; the human must provide or grant access
     to that local state before the exercise can be scoped precisely. This source repository at the
     Control-Room-reviewed Step 6 commit (or later, once further reviewed) is the install source.
   - **The exercise's actual prerequisite: the participating skills installed at compatible,
     reviewed versions — not merely present.** "Scenarios" below exercises a full pipeline pass
     through `implement-it` (including its own Gate-1 invocation of `review-it`) plus a separate,
     standalone `document-it` invocation. That means `document-it`, `implement-it`, and `review-it`
     must actually be installed and current for the exercise to run at all, and every skill it
     touches — including `lab-it`, `plan-it`, and `ship-it` if they're already present — must come
     from the same reviewed source state, not a mismatched mix of a stale pre-migration `ship-it`
     (which still claims implementation/gate/commit ownership its own contract no longer owns)
     alongside a newly added `implement-it` making the identical claim. A partial or mismatched
     installed set is a real prerequisite failure for this exercise, not a detail to paper over.
   - **Determine what `useOrbit` actually needs from its real state when the exercise is later
     authorized — not a fixed prescription written now.** This proposal does not assume `useOrbit`'s
     installed state (per this step's own "do not assume `useOrbit`'s ignored local environment can
     be established from GitHub alone"). Inspect its actual current `skills-lock.json` and managed
     set first, then determine the minimum combination of refresh and addition that gets the
     resulting set to what the prerequisite above actually requires. **"Refresh-only," "add-the-
     three," and "both" are not interchangeable choices with the same downstream capability**: a
     refresh alone only updates skills `useOrbit` already has installed and never adds a skill it
     doesn't (`docs/skill-consumption.md` §8's "naming the managed skills explicitly keeps a refresh
     scoped to what the project actually installed") — if `useOrbit` currently has only the
     pre-migration `lab-it`/`plan-it`/`ship-it` set, refresh-only leaves `document-it`, `implement-it`,
     and `review-it` entirely absent and **does not satisfy this exercise's prerequisite**; only
     adding those three (alongside refreshing whatever else is already present, so every skill
     shares one reviewed source state) actually makes the full pipeline scenario runnable. State
     this to the human explicitly before running anything, so the choice is made with the actual
     consequence in view, not as a preference among equivalent options.
   - **A partial installation may be its own separately scoped check — it is never a substitute for
     the complete exercise.** If the human authorizes less than what the prerequisite above
     requires, whatever gets exercised against that partial set (e.g., confirming a refreshed
     `ship-it` still behaves correctly for milestone delivery on already-existing scope) may be a
     legitimate, narrower validation in its own right — but it must never be reported, or counted,
     as having successfully executed the complete pipeline exercise "Scenarios" below describes.
   - **Preserve what's unrelated.** `useOrbit`'s existing stack companions (e.g.
     `laravel-inertia-stack`, if installed) and any other skill this repository doesn't publish are
     left untouched by either a refresh or an addition — this exercise never implies the six
     portable skills replace `useOrbit`'s entire installed set, only that they're the set this
     repository's own pipeline consists of now.
   - **Intended changes (in `useOrbit`, not this repository).** Whichever of refresh or addition the
     human chooses, run it via `npx skills add`/`skills update` (per `docs/skill-consumption.md`
     §3/§8) against this source; commit the resulting `.agents/skills/**`, updated
     `skills-lock.json`, and any newly needed agent-discovery symlinks and refresh-script entries
     under the repository-managed model (§4-§5 of that document) — reconciling each of those four
     artifacts only where `useOrbit`'s actual setup requires it, not as a blanket rewrite.
   - **Scenarios, with an exact stopping point.** One full pipeline pass exercised against a real,
     human-chosen, low-risk `useOrbit` issue or small milestone: investigation or planning through
     implementation, `review-it`'s Gate-1 invocation, Gate 2's commit-plan approval, push, and issue
     closure. **This exercise is scoped to stop at milestone PR readiness or, at most, an actual
     approved PR's creation** — it does not extend through human PR merge, post-merge milestone
     closure, or release. If it stops at PR readiness or creation, post-merge delivery and release
     remain unexercised by this proposal and need their own later exercise or authorization before
     either is considered validated. A standalone `document-it` invocation independent of the
     pipeline confirms its "companion, not mandatory stage" identity holds in real use.
   - **Success evidence.** `skills-lock.json` reflects whichever skills were refreshed or added at
     this source's current content hash; `.agents/skills/**` and any tracked discovery symlinks
     match; unrelated installed skills and stack companions are byte-identical to their pre-exercise
     state; the exercised pipeline pass reaches its expected human checkpoints (Gate 1 citing
     `review-it`'s result, Gate 2's commit-plan approval) with no unexplained gap or misrouted skill.
     Any defect found is reproduced, attributed to a specific owning file in this source repository,
     and corrected there — never patched only in `useOrbit`'s installed copy.
   - **Restoration needs.** Agree with the human, before starting, whether any real GitHub artifacts
     the exercise creates in `useOrbit` (an issue, a milestone, a PR) are kept as genuine low-risk
     work or explicitly closed/cleaned up afterward. Capture `useOrbit`'s pre-exercise branch,
     working-tree, `.agents/skills/**`, `skills-lock.json`, and refresh-script state before starting,
     so an unwanted result can be reverted.

2. **A non-Laravel portability exercise, without a custom stack companion.**
   - **Coverage scope**, explicit and justified — replacing this step's own outline's stale
     "three portable skills" wording, written before `document-it`, `implement-it`, and `review-it`
     existed: all six current portable skills — `lab-it`, `document-it`, `plan-it`, `implement-it`,
     `review-it`, `ship-it`. None of the six carries stack-specific vocabulary in its current rule
     files; the migration's own goal is that none of the six requires a stack companion to run.
     `laravel-inertia-stack` itself is explicitly excluded — it is the one skill meant to be
     stack-specific, and exercising it against a non-Laravel project would prove nothing.
   - **Prerequisites.** A sample project on a genuinely different stack (no Laravel, Inertia, Vue, or
     Pest), with no stack companion from this repository installed into it.
   - **Intended changes.** Install (disposable or personal-mode, per `docs/skill-consumption.md` §2
     — repository-managed commitment is not required for this exercise) this source's six portable
     skills into the sample project.
   - **Scenarios, with an exact stopping point.** `lab-it` investigates something real in the sample
     project's actual stack; `document-it` creates or updates a guide there; `plan-it` plans a small
     feature into GitHub issues against that project's real conventions; `implement-it` implements
     one approved issue there, verified with that project's own discovered test/lint tooling,
     invoking `review-it` before Gate 1; `review-it` runs standalone against that branch/PR,
     confirming `rules/scope.md`'s "Discover applicable conventions" and `rules/checklist.md`'s
     "Project and stack convention compliance" actually hold against a real, non-Laravel project —
     see "Correcting no-companion review expectations" below for what this specifically checks;
     `ship-it` takes the resulting milestone through PR readiness/creation. **This exercise, like
     the `useOrbit` one, is scoped to stop at milestone PR readiness or PR creation** — post-merge
     closure and release are not exercised by it.
   - **Correcting no-companion review expectations.** The owning rule
     (`review-it/rules/scope.md`'s "Discover applicable conventions") does not say a missing stack
     companion goes quiet on framework concerns — it says the opposite: framework and technology
     conventions are discovered the same way project conventions are, from project instructions,
     configuration, established repository usage, and other available authoritative guidance the
     project itself references, plus ordinary engineering reasoning about the stack; only the
     specific sub-check that depends on a *custom companion's own rules*, with no other available
     authoritative source, is skipped. This exercise's success bar reflects that precisely: a
     `review-it` finding about the sample project's real stack is expected and correct when it's
     grounded in one of those available sources, and each finding states plainly whether it rests on
     an established project requirement or on general technical reasoning with no such backing —
     `rules/scope.md`'s own text was source-reviewed for this proposal, but this exact behavior has
     not yet been exercised against a real non-Laravel project (see `artifacts/review-it.md` §8 for
     what a prior Git-mechanics experiment actually tested instead — comparison-base and
     state-identity behavior, not this stack-aware discovery path).
   - **Judge portability by correct behavior, not silence about technology names.** The sample
     project's own real stack (its actual framework, language, and tooling) is expected to appear by
     name throughout every skill's output where it's actually relevant — a `review-it` finding
     grounded in that project's own conventions, an `implement-it` verification report naming its
     actual test runner, a `document-it` guide describing its actual architecture. What each skill
     must *not* do is state or assume a Laravel-, Inertia-, Vue-, or Pest-specific convention as a
     general rule when the sample project's own evidence doesn't support it, or silently degrade a
     framework check to nothing merely because `laravel-inertia-stack` isn't installed. A defect (a
     hidden Laravel-shaped assumption anywhere in the six skills, or a check that goes silent it
     shouldn't) is reproduced, attributed to a specific file, and corrected in this source
     repository.
   - **Restoration needs.** The sample project should be disposable or already treated as low-stakes
     by the human, since `implement-it`'s exercise necessarily produces a real commit and, if carried
     through `ship-it`, a real PR; agree on cleanup (deleting the sample repository, or
     reverting/closing what was created) before running it.

**Finalized v2.0.0 release proposal.** This is the one concrete, current proposal for this release —
it replaces the outline above in place rather than standing alongside it as a competing version. It
remains a proposal: not approved, and no tag, draft release, published release, PR, or deployment has
been created for it.

**Proposed tag and title.** Tag `v2.0.0`; release title **"Agentic Engineering v2.0.0."** The agreed
headline — **Lab. Plan. Implement. Review. Ship — with the right stack.** — is kept inside the notes
body, not folded into the title.

**Why this is a major release.** Responsibilities moved between skills, not merely within one:
implementation, verification, Gate 1/Gate 2, commit construction, and issue closure moved out of
`ship-it` into new `implement-it`; guide creation, review, and maintenance moved out of `lab-it` into
new `document-it`; independent implementation review is now a separately named skill, `review-it`. A
consumer who only refreshes its existing managed skills keeps `lab-it`, `plan-it`, and `ship-it`
working, but does not thereby gain any of that relocated behavior — that requires an explicit
migration step (below), which is the definition of a breaking, major-version change for this
ecosystem's consumers.

**Complete proposed release-note text:**

> ## Agentic Engineering v2.0.0
>
> **Lab. Plan. Implement. Review. Ship — with the right stack.**
>
> This release splits the previous three-skill pipeline (`lab-it` / `plan-it` / `ship-it`) into six
> capabilities, moving implementation-review, recovery, and verification responsibilities to where
> they now belong. It is a major release: responsibilities moved between skills, and a project that
> only refreshes its existing managed skills will not gain the relocated behavior described below
> without an explicit migration step.
>
> ### What changed
>
> - **`document-it` (new).** An independently available companion capability, not an inserted
>   pipeline stage — creates, updates, and reviews explanatory architecture guides, in Markdown, a
>   Claude Artifact, or both. Narrowed out of `lab-it`, which no longer owns guide creation, review,
>   or maintenance: `lab-it` routes guide requests to `document-it`; `document-it` reuses current
>   evidence and calls on `lab-it` for investigation when evidence is missing or stale.
> - **`implement-it` (new).** Owns approved issue/milestone intake, working-branch readiness,
>   implementation, verification, issue-level Git workflow, Gate 1 and Gate 2, commit construction,
>   authorized push, issue closure, and next-issue recommendations. Narrowed out of `ship-it`, which
>   no longer performs any of this.
> - **`review-it` (new).** Independently callable implementation assurance for a worktree, branch, or
>   PR. Invoked by `implement-it` before Gate 1, and again during an authorized delivery correction;
>   also callable entirely standalone, with no prior session required.
> - **`lab-it` (narrowed).** Architecture investigation, verified explanations, and approved
>   `plan.md` synthesis only. Guide output moved to `document-it`.
> - **`ship-it` (narrowed).** Milestone PR readiness and authorized creation, post-merge delivery,
>   milestone closure, and release. No longer implements, verifies, or closes individual issues —
>   that is `implement-it`'s job. On a CI failure on an open milestone PR, `ship-it` investigates,
>   explains, and secures the human's authorization; `implement-it` performs the authorized
>   correction.
> - **Implementation-review, recovery, and verification improvements.** Gate 1's stop condition now
>   requires `review-it`'s pass to be clean, or its findings resolved and re-verified; worktree
>   provenance is judged from reliable signals (git reflog, a session's own recorded start point, an
>   explicit human statement) rather than appearance; an empty dependency-ready set is no longer
>   treated as sufficient for milestone handoff when issues remain open but blocked; interrupted
>   batch creation re-queries GitHub before retrying; approval validity is re-checked against the
>   current diff/issue body before Gate 2 and before push; verification evidence is tied to the
>   commit/diff it was produced against; the completed-issue full-suite checkpoint may reuse an
>   established earlier full-suite result under four stated conditions, never a cache hit or a
>   selected subset alone.
>
> ### Install / migrate
>
> ```shell
> npx skills add elieandraos/agentic-engineering
> ```
>
> This installs or refreshes directly from the repository's current default branch, at whatever
> commit `main` is at when the command runs — an unpinned GitHub-source install does not guarantee
> the exact `v2.0.0` contents once `main` has advanced further. Select all six portable skills —
> `lab-it`, `document-it`, `plan-it`, `implement-it`, `review-it`, `ship-it` — as the intended
> installation scope, so your existing skills are refreshed from the repository's current default
> branch and the three new names are added. **Refreshing only the skills you already have updates
> `lab-it`, `plan-it`, and `ship-it` in place but does not add `document-it`, `implement-it`, or
> `review-it`** — a refresh never adds a skill a project didn't already install. Keep any applicable
> stack companion (e.g. `laravel-inertia-stack`) installed as before; this release does not change
> stack-companion behavior.
>
> ### Validation
>
> This release was validated by source review: a full re-read of every changed and new file,
> repository-wide searches for stale ownership references, `git diff --check`, relative-Markdown-link
> resolution across every changed file, and bounded static walkthroughs of each migration step's key
> scenarios against the actual owning `SKILL.md`/rule files. Two bounded, disposable-repository
> experiments checked the underlying Git mechanics `review-it`'s rules depend on — comparison-base
> and state/comparison-identity behavior, and final-content equivalence for the completed-issue reuse
> rule; neither experiment executed `review-it` itself. **No skill was invoked end to end, and no
> consuming project's installation, refresh, or pipeline run was performed as part of this
> release** — this is source-level validation, not consumer proof.
>
> ### Known deferred items
>
> - Canonical issue-definition durable storage remains deferred — no `issue-plan.md`-equivalent file
>   or approval registry is introduced; recovery relies on querying GitHub directly.
> - The `laravel-inertia-stack` / Laravel Boost precedence rule for conflicting guidance remains
>   unresolved and out of scope for this release.
> - A real consumer installation/refresh exercise and a non-Laravel portability exercise remain
>   available as optional, separately authorized follow-up validation — not performed for this
>   release, and not a precondition of it.

**Migration instruction (short form, for consumers).** Reinstall or select all six portable skills
from this repository — `lab-it`, `document-it`, `plan-it`, `implement-it`, `review-it`, `ship-it` —
as the intended installation scope, so existing skills are refreshed from the repository's current
default branch and the three new names are added. A GitHub-source install tracks the source
repository's default branch at install/update time, not a pinned ref — it does not by itself
guarantee the exact `v2.0.0` contents once `main` has advanced further. Preserve any applicable stack
companion already installed (e.g. `laravel-inertia-stack`); this release does not change
stack-companion behavior. Updating only the skill names a project already has does **not** add the
three missing skills — a refresh never adds a skill a project didn't already install.

**Validation actually performed for this release (accurate, not end-to-end).** Source review of
every changed and new file across Steps 2-6; repository-wide searches for stale ownership and
cross-reference claims; `git diff --check` on every touched pass; a Python-based relative-Markdown-
link resolution check; bounded static walkthroughs (reasoning through the relevant rule files against
a scenario, no skill invoked) covering each step's key scenarios, listed in full in §6 above; and two
bounded, disposable-repository experiments checking the underlying Git mechanics `review-it`'s rules
depend on — comparison-base and state/comparison-identity behavior (Step 4's correction record) and
final-content equivalence for the completed-issue reuse rule (Step 5's correction record). **Neither
experiment executed `review-it` itself.** No end-to-end consumer execution was performed: no skill
was invoked as a live session, and no `useOrbit` or other consuming project's installation, refresh,
or pipeline run occurred. The two consumer-validation exercises above remain available, deferred,
optional follow-up — not a precondition of this proposal.

**Known deferred items (brief, not expanding this release's scope).** Canonical issue-definition
durable storage (§3.2, §7); the `laravel-inertia-stack`/Boost precedence question (§7 item 1); the
real `useOrbit` consumer exercise and the non-Laravel portability exercise (above) — both now
explicitly deferred, optional options rather than a gate on this proposal, since the user will handle
consumer installation/update manually.

**Proposed publication procedure (this repository's established direct-main release approach).**
`ship-it/rules/release.md` governs a *consuming project's* release, entered once that project's own
milestone PR has merged — this repository does not run its own pipeline against changes to itself.
Every commit in this migration was authored, reviewed, and pushed directly to `main` by explicit
human authorization, with no PR or merge step anywhere in this repository's own history: `gh pr list
--state all` returns zero pull requests in any state, and this repository's prior release, `v1.0.0`,
was tagged and published the same way, directly from commit
`585a5d426e55fc3d586a9d3b95a43f85baf974ad` on `main` (confirmed via `git log -1 v1.0.0` and `gh
release view v1.0.0`), with no PR behind it. The applicable path for `v2.0.0` is that same
established precedent: apply `release.md`'s substantive draft → explicit approval → publish →
re-fetch-and-validate sequence directly against `main`'s reviewed tip.

**Release candidate.** The candidate commit for the `v2.0.0` tag is `main`'s tip immediately after
this plan-finalization edit is committed and pushed — the final commit reported at the end of this
task — not a SHA hard-coded into this file, since this file cannot reference the hash of the commit
that contains it without an editing loop. Before publication, `ship-it` must independently re-fetch
and confirm that candidate commit and this exact release-note text against the human's explicit
approval — publication is a separate, later authorized action, not performed by this proposal.
**Available on `main` is distinct from published:** everything this migration describes is already
reachable by a fresh `npx skills add elieandraos/agentic-engineering` GitHub-source install
(`docs/skill-consumption.md` §13 — no release or tag is required for that), but no `v2.0.0` tag or
GitHub Release exists yet, and none is created by this plan.

**Corrected.** A bounded correction/completion pass on top of the reviewed commit
`d9f1f710ca4c1cd0c2ecf78907ccbe43f09013a6`, addressing findings against Step 6's first pass:

- **The architecture dossier set is now complete.** New: `artifacts/document-it.md`,
  `artifacts/implement-it.md`, `artifacts/review-it.md` — each covering that skill's own current
  architecture, rationale, ownership, and evidence-calibrated confidence, inspecting the pre-Step-6
  dossiers at `891b2ee887917b2145b37f85860697301a5c1db6` for rationale worth preserving in its new
  owner (the guide rendering/identity/accessibility reasoning moved from the old `lab-it.md` §6 into
  `document-it.md` §4; the branch-readiness/gates/commits/verification/closure/sequencing reasoning
  moved from the old `ship-it.md` into `implement-it.md` §3-§9, updated for `review-it`'s Gate 1 role,
  the completed-issue reuse rule, worktree-provenance preservation, and delivery corrections;
  `review-it.md` is written fresh, since that skill has no predecessor). **The first pass's stated
  reason for omitting these — "the authoring methodology's 'do not create extra dossiers merely for
  symmetry'... and this migration's own instruction not to create one" — was a misapplication of
  that principle, not a categorical prohibition.** These three dossiers exist for a substantive
  reason the principle's own text permits: explaining architecture actually distinct from any
  existing dossier and preserving rationale that would otherwise have no home now that `lab-it.md`
  and `ship-it.md` are narrowed — not adding files merely to match sibling skills' shape.
- **`artifacts/lab-it.md` §7 corrected from one-directional to reciprocal.** The prior text claimed
  "this skill never hands work to `document-it`." `lab-it/SKILL.md`'s own routing table contradicts
  that: a guide-shaped request is routed to `document-it` — a real handoff `lab-it` performs, not
  only one `document-it` reaches backward for. §7, §6, and §8 were corrected to state both
  directions: `lab-it` routes a guide-shaped request to `document-it`; `document-it` draws on
  `lab-it`'s evidence discipline only for its own narrower missing/stale-evidence sub-problem and
  receives verified findings back. Neither direction was ever, or is now claimed to be, the other
  skill's terminal output.
- **`artifacts/ship-it.md` corrected on three points.** (1) §2 and §7's "this skill's only
  input"/"only upstream input" framing was in tension with §1's own "never requires proof that a
  particular `implement-it` session produced the state" claim — corrected so both sections agree:
  milestone work ordinarily arrives as `implement-it`'s closed work, but this skill checks GitHub's
  actual current state directly rather than requiring evidence of a specific session. (2) §3's
  readiness conditions stated "required manual verification is complete, or explicitly not
  applicable" — the owning rule (`milestone-completion.md`'s "The three conditions") states no such
  alternative; corrected to the rule's actual two conditions, "final manual testing has actually
  happened" and "that testing found nothing further to do," with no "not applicable" branch. (3) §4's
  CI-failure resumption was corrected to state precisely what the owning rule's steps 6-7 actually
  say: this skill resumes by confirming CI runs again once a correction is verified and pushed — not
  by waiting until CI is already green — and a red result on that re-run returns to step 1, repeating
  until CI is genuinely green, with no merge/closure/release proceeding merely because it is.
- **`artifacts/plan-it.md`'s handoff explanation corrected** to stop implying all of `ship-it`'s
  ownership begins "once a milestone has zero open issues remaining" — only PR readiness/creation
  actually shares that precondition; investigation/continuation on an open PR and post-merge closure/
  release each start from their own separate condition, per `ship-it.md` §1.
- **`README.md` corrected**: the Ship row's result column implied `ship-it` owns merge
  ("Milestone PR, merge, and release lifecycle") — corrected to "Milestone PR proposed, then release
  once merged," with an explicit added sentence that PR approval and merge always stay with a human,
  no skill in this pipeline merges its own work. Also added: `implement-it` invokes `review-it`
  before its own implementation gate, while `review-it` remains independently callable on its own —
  the prior text only implied the second half of that.
- **This proposal's consumer and release content corrected**, in place, above:
  - The `useOrbit` exercise now explicitly distinguishes refreshing an existing managed set from
    adding the three newly named skills (a refresh alone does not add `document-it`, `implement-it`,
    or `review-it`), states that existing stack companions and unrelated skills are preserved, and
    names its own exact stopping point (milestone PR readiness or creation — post-merge delivery and
    release are not exercised by it).
  - The portability exercise's success criterion — "no skill's output... references Laravel,
    Inertia, Vue, Pest" — was a blanket prohibition on naming any technology, when the actual owning
    rule (`review-it/rules/scope.md`'s "Discover applicable conventions") explicitly keeps framework
    checks available from project instructions, configuration, established usage, and ordinary
    engineering reasoning even with no stack companion installed, skipping only the one sub-check
    that genuinely depends on a custom companion's own rules. Corrected to judge portability by
    correct behavior against the sample project's own real stack, not silence about that stack's
    name.
  - The claim that this behavior was "narrowly verified by Step 4's Git-mechanics pass" was
    inaccurate — that experiment (recorded in Step 4's own correction record above) tested Git
    comparison-base and state-identity mechanics, not `review-it`'s stack-aware convention discovery
    at all. Corrected to state plainly that this specific behavior remains source-reviewed only, not
    exercised by any experiment to date (see `artifacts/review-it.md` §8, which states the same
    correction on the skill's own side).
  - The remaining-validation bar previously required both exercises in one paragraph
    ("plus both unrun exercises proposed above") and then quietly reduced that to "ideally... at
    least one" in the release-procedure paragraph — two different bars stated in two places.
    Corrected to one consistent bar: static/source validation alone does not establish consumer
    correctness; running at least one real exercise does, and the two exercises test different
    things (repository-managed adoption without regression, versus cross-stack portability), so
    running both is stronger than either alone. A recommendation — run the `useOrbit` exercise before
    publishing, treat the portability exercise as valuable but not release-blocking — is offered for
    the human's own later approval, not silently decided by this correction.
  - The publication-procedure section previously pointed at `ship-it/rules/release.md`'s
    merged-PR-triggered entry with no acknowledgment that this repository has never merged a PR
    against itself. Corrected by inspecting this repository's actual history (`git log --merges`:
    zero merge commits across every step of this migration; `gh release view v1.0.0`: this
    repository's one prior release was tagged and published directly from a `main` commit,
    `585a5d426e55fc3d586a9d3b95a43f85baf974ad`, with no PR) and proposing the applicable path
    accordingly: apply `release.md`'s substantive draft/approve/publish/validate sequence directly
    against `main`'s reviewed tip, matching this repository's own `v1.0.0` precedent, rather than
    `release.md`'s consuming-project merged-PR entry trigger. This does not invent a merged PR,
    does not create an artificial PR to satisfy the wording, and does not change `release.md`'s own
    portable rule, which remains correctly written for what it actually governs.
- **This step's own execution record corrected.** The closing line previously read "No commit, PR,
  tag, release, or deployment was created by this step" — inaccurate: this step's own authorized
  commit and push to `origin/main` did occur (that is how the reconciled documentation and this
  record exist on `main` at all); only PR/tag/release/deployment were correctly stated as not
  created. Corrected above.

**Validation performed for this correction pass.** Full re-read of every corrected and newly created
file. `git diff --check` clean. The same Python-based relative-Markdown-link resolution check,
re-run across every changed and new file, confirmed every link resolves. Repository-wide searches
confirmed each corrected claim's old wording no longer appears anywhere in the repository: "never
hands work to," "one direction only"/"one-directional" (`lab-it.md`'s old §7 framing); "explicitly
not applicable" (the readiness-condition wording, checked against both `artifacts/ship-it.md` and
the owning rule file itself); "narrowly verified by Step 4"; the blanket Laravel/Inertia/Vue/Pest
technology-name prohibition; and the "No commit, PR, tag" closing line. `git status --porcelain`
confirmed the three pre-existing untracked files (`control-room-responsibilities.md`,
`skills-audit.md`, `subagents.md`) remain untouched and unstaged, and confirmed no runtime file
(`skills/*/SKILL.md` or `skills/*/rules/*.md`), `roadmap.md`, `docs/skill-consumption.md`, or
`docs/skill-authoring-methodology.md` was touched by this pass, per its own authorization scope.

Static walkthroughs were re-run against the actual owning files, this time specifically exercising
the corrected handoffs and independent entry points: a guide-shaped request reaching `lab-it` and
being routed to `document-it`, traced against `lab-it/SKILL.md`'s own routing table rather than
assumed; a missing-evidence documentation request routed from `document-it` into `lab-it`'s
investigation discipline and back, traced against `document-it/SKILL.md`'s "Evidence: reuse first,
route to `lab-it` only when needed"; an open milestone PR's CI failure followed through
`milestone-completion.md`'s steps 1-7 exactly (investigate → determine scope → authorize → correct
via `implement-it` → resume → re-check CI → repeat on red, proceed only on green plus separate
authorization) rather than the dossier's own earlier, looser paraphrase; a milestone PR-readiness
check walked against `milestone-completion.md`'s literal three conditions, confirming no
"not-applicable" branch exists for manual testing; and a non-Laravel `review-it` invocation walked
against `rules/scope.md`'s "Discover applicable conventions" and `rules/checklist.md`'s "Project and
stack convention compliance," confirming a framework finding grounded in project instructions,
configuration, or established usage is expected and correctly attributed, not suppressed, with no
stack companion installed. All traced correctly through the actual current file content with no
coherence gap found. **This remains source validation, not runtime or consumer proof** — no skill
was invoked, and no `useOrbit` or other consuming project was touched. As with the first pass, this
correction pass's own authorized commit and push to this source repository's `origin/main` is a real
GitHub mutation and did occur, per its own explicit authorization; no consumer-repository mutation,
and no PR, tag, release, or deployment anywhere, occurred.

**Remaining decisions**, presented with evidence and a recommendation, for the human's own later
approval — none silently resolved by this pass: which of the two proposed consumer exercises (or
both) to require before authorizing `v2.0.0` publication (this pass recommends the `useOrbit`
exercise as release-relevant and the portability exercise as valuable but not release-blocking, per
the release proposal above); whether to run either exercise now or defer publication further; and
the `laravel-inertia-stack`/Boost precedence question (§7 item 1), unaffected by this pass and still
out of scope for this migration.

**Superseded by the Step 6 approval and the finalized release proposal below.** The human has since
decided to handle consumer installation/update manually; a formal `useOrbit` exercise or portability
exercise is not required before this release proposal, and neither is presented as a publication gate
in the "Finalized v2.0.0 release proposal" section above. Both remain available as deferred, optional
validation a human may choose to run later. The `laravel-inertia-stack`/Boost precedence question
remains unaffected and out of scope.

**Third correction pass.** A bounded pass on top of commit
`bbed1f367e2b870168d6d3ab94198b8c430c8972`, limited to `artifacts/ship-it.md`,
`artifacts/review-it.md`, `artifacts/implement-it.md`, and this file, addressing five remaining
findings against the second pass's own corrections:

- **`ship-it.md` §2-§3: the entry condition still read as a blanket dependency on `implement-it`'s
  own recomputation event.** §2's opening scoped the whole "only milestone work continues into this
  skill" statement together with the zero-open-issues condition, and §3 said this gate "starts only
  once a delivery/phase milestone's dependency-ready-set recompute (owned by `implement-it`) reports
  zero open issues left" — both still read as if `ship-it`'s entry required `implement-it`'s own
  recompute to have specifically run and reported, contradicting §1's own three-entry-point
  description. Corrected: §2 now states the ordinary implementation-to-PR-readiness handoff as its
  own labeled paragraph, scoped away from the other two entry points, and both sections now say this
  skill establishes the zero-open-issues state itself by freshly querying GitHub directly, never by
  waiting for or requiring `implement-it`'s own recompute event. §3's first condition is also
  corrected: "issue closure alone does not independently prove verification or approval happened for
  each issue" replaces the prior framing that per-issue verification was "already part of" what
  closure represents — this condition confirms only that the count is currently zero, and is not a
  second verification gate over each issue's history.
- **`review-it.md` §2: the comparison-baseline claim was stated as an unconditional "never."**
  "the diff is taken from the merge-base... never a direct comparison against the base's current
  tip" contradicted `rules/scope.md`'s own explicit-comparison override (tier 1 of "Discover the
  intended base"). Corrected: merge-base diffing is now stated as the *ordinary* method, with an
  explicit request controlling outright even when it differs, and the report's obligation to label
  a requested comparison honestly as such — matching the owning rule's actual discovery order and
  identity requirements, both preserved unchanged.
- **`implement-it.md` §11: the stack-composition explanation named only "skills loaded alongside"
  as the source of implementation guidance.** Corrected to state the actual model
  `SKILL.md`'s "Composition" and `verification.md`'s "Discover the project's verification tools" own:
  project instructions, established repository conventions, and applicable implementation/testing/
  tooling skills all supply guidance; an applicable custom stack companion is loaded when available
  and adds technology-specific knowledge on top, but stays optional — this skill must function
  correctly with none installed. The corrected paragraph links to `SKILL.md`'s owning statement
  rather than restating its procedure.
- **This proposal's `useOrbit` exercise prerequisite was underspecified.** It presented
  "refresh-only," "add-the-three," and "both" as interchangeable human choices with no statement of
  which one(s) actually make the proposed full pipeline scenario (which specifically exercises
  `implement-it`, `review-it`, and a standalone `document-it` invocation) runnable at all. Corrected
  to state the actual prerequisite precisely: the participating skills installed at compatible,
  reviewed versions (not a stale pre-migration `ship-it` alongside a newly added `implement-it`
  making an identical implementation-ownership claim); that refresh-only does not by itself satisfy
  this prerequisite when `document-it`/`implement-it`/`review-it` aren't already present; that the
  actual combination needed is determined from `useOrbit`'s real installed state when the exercise
  is later authorized, not prescribed now; and that a partial installation may be its own separately
  scoped check but must never be reported or counted as having executed the complete proposed
  pipeline exercise.
- **The evidence statements were corrected on two points.** First, "no GitHub state was mutated" was
  inaccurate in both the first pass's and the second pass's own validation summaries — each pass's
  own authorized commit and push to this source repository's `origin/main` is itself a real GitHub
  mutation, and each did occur; both summaries are corrected to state that explicitly, distinguishing
  it from the consumer-repository mutations, PRs, tags, releases, and deployments that genuinely did
  not occur. Second, the publication-history claim previously cited only `git log --merges` (zero
  merge commits) as evidence that this repository has never merged a PR against itself — a squash or
  rebase merge can integrate a PR while leaving no merge commit, so that evidence alone would not
  have ruled out a PR having existed. Corrected to cite direct evidence instead: `gh pr list --state
  all` against this repository returns zero pull requests in any state (open, closed, or merged),
  confirming no PR has ever existed here, not only that none left a merge commit; `v1.0.0`'s tag
  target and publish record were independently re-confirmed via `git log -1 v1.0.0` and `gh release
  view v1.0.0` directly, consistent with that result. The direct-main publication path remains a
  proposal only — this correction does not authorize publication or settle which consumer exercise
  is required first.

**Validation performed for this pass.** Full re-read of every corrected file. `git diff --check`
clean. The same Python-based relative-Markdown-link resolution check, re-run across all four changed
files, found no broken link introduced by this pass. Repository-wide searches confirmed none of the
corrected phrasings survive elsewhere in the four files: "never a direct comparison," the
recompute-dependent entry-condition framing in `ship-it.md`, the alongside-only stack-composition
framing in `implement-it.md`, and the unqualified "no GitHub state was mutated" claim. `git status
--porcelain` confirmed the three pre-existing untracked files remain untouched and unstaged, and
confirmed no runtime file (`skills/*/SKILL.md` or `skills/*/rules/*.md`), `README.md`, `roadmap.md`,
or either `docs/*.md` file was touched by this pass. Direct evidence for the publication-history
claim was gathered as described above (`gh pr list --state all`, `git log -1 v1.0.0`, `gh release
view v1.0.0`), not asserted from inference.

Five bounded static walkthroughs were traced against the actual owning rule files and the corrected
summaries: an existing open milestone PR with a follow-up issue reopening the milestone's issue
count, traced against `ship-it.md` §1/§4 and `milestone-completion.md`'s own text, confirming
continuation on the open PR doesn't re-require zero open issues; a milestone PR-readiness assessment
with no prior `implement-it` session in the conversation, traced against the corrected §3 and
`milestone-completion.md`'s "checked directly against current GitHub state rather than requiring
evidence that a specific `implement-it` session produced it"; an explicitly requested base-tip
comparison, traced against the corrected `review-it.md` §2 and `rules/scope.md`'s tier-1 override
and honest-labeling requirement; `implement-it` implementing against project conventions with no
custom stack companion installed, traced against the corrected §11 and `verification.md`'s tooling-
discovery discipline; and a migration from `useOrbit`'s old `lab-it`/`plan-it`/`ship-it`-only
installed set to the set the proposed pipeline exercise actually requires, traced against the
corrected proposal text, confirming refresh-only is correctly identified as insufficient and a
partial install is correctly barred from counting as the complete exercise. All five traced
correctly through the actual current file content with no coherence gap found. This remains source
validation, not runtime or consumer proof — no skill was invoked, no `useOrbit` or other consuming
project was touched, and this pass's own commit and push to `origin/main` (a real GitHub mutation)
is the only GitHub-state change it made; no PR, tag, release, or deployment occurred.

**Step 6 passed Control Room review at commit `4247a829e55f260ab86a61daf72ef6193b21979c`, and the
user confirmed recording that approval.** This step's own authorized commit and push to `origin/main`
did occur, per the explicit authorization that opened this step and its correction passes — that is
how this record and the reconciled documentation exist on `main` at all. No PR, tag, release, or
deployment was created by any of its passes. Neither consumer exercise above was run, and no
consuming project was touched or refreshed. **This approval covers the reviewed source and
documentation; it does not establish successful consumer execution.** Publication of `v2.0.0` remains
a separate, later decision — see the finalized release proposal above.

---

## 6. Validation approach

Six static walkthroughs (reasoning through the relevant rule files against a scenario — no skill is
actually invoked by this plan) cover the pipeline's shape end to end, one per step above:
investigation without documentation and an approved `plan.md` handoff, including the boundary
between `lab-it`'s standalone investigation ending in a verified answer alone (no guide, no
`plan.md`) and `plan-it`'s own discovered-work intake (`rules/discovered-work.md`) for a raw finding
surfaced during planning or implementation — the two are different entry points into investigation
and are not interchangeable; guide creation/update in both supported formats, including the
new-guide format-selection question and the existing-guide missing/inaccessible/unavailable-
capability distinction (§3.3); single-issue and branching milestone dependency flows, including the
empty-ready-set/blocked-issues distinction (§3.2); standalone review and finding/correction/re-
review, exercised both before Gate 1 and during an authorized delivery correction (§3.1); interrupted
planning and implementation, including worktree-provenance using reliable signals rather than
appearance (§3.2); milestone PR creation through human merge, a CI failure on the open PR routed
through the corrected delivery-correction flow, and authorized release. Step 6's `useOrbit` exercise
and portability check are **execution**, not static walkthroughs — planned only, per that step's own
scope, not performed by this plan.

## 7. Material decisions still needed

Only genuinely unresolved architecture choices are listed here — checklist wording, exact filenames,
and other procedural detail are authoring work for their owning step's own review, not separate
questions for the user (§5).

1. `laravel-inertia-stack`'s unresolved precedence rule for conflicting Boost-skill guidance
   (finding #7) — out of scope for this migration; flagged only so it isn't lost, not addressed by
   any step above.

This is now the only remaining item in this list — both decisions previously listed here were
settled by the user directly ahead of Step 5's implementation, not silently resolved by writing
default text into this plan.

Resolved by Step 3's Control Room review: `ship-it`'s PR-creation procedure (§3.5), approved as
implemented at commit `ab3ea28413d28b0a20a7d7a2c0f73a9e2587b9ea`.

Resolved by explicit user decision ahead of Step 5, implemented and pending Control Room review:
**canonical issue-definition durable storage is deferred, not resolved** — no `issue-plan.md`-
equivalent file, approval registry, or other persistence mechanism is introduced; a simple
GitHub-query recovery procedure is retained instead (§3.2, finding #21; see Step 5's own record);
**the completed-issue-boundary full-suite reuse-eligibility rule** is settled — both checkpoints
stay required, and the completed-issue one may be satisfied by an established reuse of an earlier
full-suite result (the pre-Gate-1 run, or one already executed against the final committed state)
under the four conditions stated in
`skills/implement-it/rules/verification.md`'s "Completed-issue verification: run or reuse" (§3.4;
see Step 5's own record).

Resolved by the earlier planning correction pass, no longer open: `document-it`'s Markdown location (settled as the
consuming repo's `docs/`, §3.3); the format-selection and no-silent-substitution behavior for a new
or existing guide (§3.3); the delivery-correction ownership split (§2.2); the verification policy's
per-issue vs. milestone-entry question (there is no separate milestone-entry boundary, §3.4); the
worktree-provenance principle (use reliable provenance, not appearance — implemented at Step 5 with
`git reflog`, the session's own recorded start point, and an explicit human statement as the
reliable signals, §3.2).

---

## Verification of this planning pass

- Original planning pass: `git status --porcelain` before writing showed only
  `control-room-responsibilities.md`, `skills-audit.md`, `subagents.md` untracked; `plan.md` did not
  exist. HEAD was `f951bbe`; the commit that added `plan.md` is `468715d`.
- This correction pass: branch `main`, HEAD `468715d` (unchanged before and after); `git status
  --porcelain` before editing showed the same three pre-existing untracked files plus `plan.md`
  itself (tracked, no local modifications yet) — nothing else. Only `plan.md` was edited by this
  task. No skill file, `README.md`, `roadmap.md`, `docs/` file, or the three pre-existing untracked
  files was touched. Nothing was staged, committed, pushed, or changed on GitHub; `plan.md` is left
  unstaged.
- This pass (recording Step 6's approval and finalizing the v2.0.0 release proposal): branch `main`,
  local and `origin/main` both at `4247a829e55f260ab86a61daf72ef6193b21979c` before editing (verified
  by `git fetch` and comparing `git log` on both); `git status --porcelain` before editing showed only
  the same three pre-existing untracked files (`control-room-responsibilities.md`, `skills-audit.md`,
  `subagents.md`) — no intervening changes to reconcile. Only `plan.md` was edited: the top-of-file
  status line and Step 6 narrative were updated to record Control Room approval of Steps 1-6; the two
  consumer-exercise proposals under Step 6 were marked deferred, optional options rather than
  mandatory next steps; and the release-proposal section was rewritten in place into one concrete,
  finalized `v2.0.0` proposal (tag, title, complete release-note text, migration instructions,
  accurate validation statement, deferred items, and a publication procedure identifying the release
  candidate as this task's final pushed commit rather than a self-referential hard-coded SHA). No
  skill file, `README.md`, `roadmap.md`, `docs/` file, or the three pre-existing untracked files was
  touched. `git diff --check` on the resulting change is clean. Nothing was tagged, released,
  drafted, or deployed; `plan.md` is the only file staged and committed, then pushed to `origin/main`
  without force.
