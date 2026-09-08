# Ecosystem migration plan — Lab · Document · Plan · Implement · Review · Ship

**Status: Steps 1–3 approved.** Step 3 passed Control Room review at commit
`ab3ea28413d28b0a20a7d7a2c0f73a9e2587b9ea`. Step 4 is next and has not started.
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
| Worktree provenance (finding, Section 3 scenario 3) | `implement-it/rules/verification.md` §"Discover the verification starting state" | Preserve pre-existing worktree changes by default. Recency, being uncommitted, or matching the approved issue's scope does not by itself prove a change belongs to this session — appearance is not provenance. Use whatever reliable provenance is actually available (e.g., git reflog, the session's own recorded start point, an explicit statement from the human) to judge origin; ask the human when the ambiguity would materially affect whether it's safe to continue, rather than on any ambiguity at all. Never invent ownership from appearance, and never modify content whose origin can't be established this way. **Open**: which provenance sources are reliably available is discovered per project at Step 5, not fixed here. |
| Empty dependency-ready set treated as sufficient for delivery handoff | `implement-it/rules/sequencing.md` §"When the ready set is empty" | An empty ready set is not, by itself, sufficient to hand off to `ship-it`'s Milestone PR readiness. `rules/sequencing.md`'s own definition allows an empty ready set with open issues still outstanding — nothing dependency-ready right now, but one or more issues blocked on something rather than closed. Before handing off, distinguish "zero open issues remain" (the genuine completion case, hand off as today) from "open issues remain, all currently blocked" (report the blocked state; do not hand off, since the milestone isn't done). The existing recommend-and-stop behavior — the human, not this rule, chooses the next issue — is unchanged either way. |
| Partial GitHub mutation before resuming a batch (finding #10) | `plan-it/rules/sequencing.md` (issue batches); `ship-it/rules/milestone-completion.md` and `rules/release.md` (milestone/release mutations) | Before creating/mutating more of a batch, re-query GitHub for members this same interrupted batch may already have created — extends the existing post-mutation re-fetch pattern already present in four files, not a new mechanism. |
| Canonical issue-definition durable storage (finding #21) | `plan-it/rules/issue-conventions.md` | **Open, deliberately not resolved here** — a stated default location, mirroring `plan.md`'s own stated-default pattern, needs its location, creation/update timing, approval relationship, mapping to created issues, and retirement all decided together at Step 5's review. No file is introduced by this plan. |
| Approval staleness after a material change (finding #13/#4) | `implement-it/rules/review-gates.md` | Before Gate 2 and before push, compare the current diff/issue body against what was approved; a material difference invalidates that approval and requires re-review — extends the existing "never silently convert an unresolved decision into a fact" principle already stated four times across the ecosystem. |
| Verification evidence tied to the state checked | Existing report shapes (Gate 1 report, `review-it` findings, closing comment) | Cite the commit SHA/diff the evidence was produced against, so a later reader can tell whether it still covers current state. |

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

**Open, for Step 5's review only**: the reuse-eligibility rule for the completed-issue-boundary
full-suite run — what counts as "demonstrably applicable" prior coverage such that it can be reused
rather than re-run. Today's rule is unconditional ("don't drop either run because the other
passed"); whether and how that becomes conditional is Step 5's decision, not this pass's. No other
part of this policy is open.

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

### Step 5 — Strengthen recovery, adopt the approved verification policy

- **Outcome/boundaries.** The §3.2 recovery additions and the §3.4 verification-policy decisions —
  as actually resolved at this step's review, not as defaults this step invents — are applied to
  their owning files.
- **Affected files.** `implement-it/rules/verification.md` (the completed-issue-boundary reuse-
  eligibility rule — the only open item left in §3.4), `rules/review-gates.md`,
  `rules/issue-closure.md`; `plan-it/rules/sequencing.md`, `rules/issue-conventions.md` (whichever
  owns the approved canonical-definition-location decision); `ship-it/rules/milestone-completion.md`
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
  milestone/release mutations; the canonical-issue-definition location is stated, consistent with
  `plan.md`'s own default-location pattern; PR-readiness's three conditions are undisturbed by the
  reuse-eligibility rule's resolution.
- **Validation (static).** Interrupted-worktree resume, including a case with pre-existing unrelated
  changes that must survive untouched; interrupted issue-batch-creation resume; approval-then-
  material-change resume; PR readiness against an open PR with red CI; a milestone with open issues
  that are all blocked (not closed) confirming no premature handoff to PR readiness.
- **Result to present.** Diff plus an explicit list of which audit findings (§Section 3 scenarios,
  #10, #13, #21) are now resolved and how.

### Step 6 — Reconcile public documentation, validate the combined ecosystem, prepare publication

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
  bounded non-Laravel portability check (the three portable skills activate correctly with no stack
  companion installed, in a sample project that isn't Laravel/Inertia). Both are scoped here as
  planned exercises for a later, explicit go-ahead — neither is performed, and no consumer is
  changed, by this plan.
- **Result to present.** Final reconciled documentation diff, plus the two planned exercises' scope,
  for the user's explicit authorization before running them or requesting publication.

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

1. Canonical issue-definition durable storage: location, creation/update timing, approval
   relationship, mapping to created issues, retirement (§3.2, finding #21) — Step 5.
2. The completed-issue-boundary full-suite reuse-eligibility rule: what counts as "demonstrably
   applicable" prior coverage (§3.4) — this changes an existing unconditional requirement and is not
   treated as approved by writing it here — Step 5.
3. `laravel-inertia-stack`'s unresolved precedence rule for conflicting Boost-skill guidance
   (finding #7) — out of scope for this migration; flagged only so it isn't lost, not addressed by
   any step above.

Resolved by Step 3's Control Room review: `ship-it`'s PR-creation procedure (§3.5), approved as
implemented at commit `ab3ea28413d28b0a20a7d7a2c0f73a9e2587b9ea`.

Resolved by the earlier planning correction pass, no longer open: `document-it`'s Markdown location (settled as the
consuming repo's `docs/`, §3.3); the format-selection and no-silent-substitution behavior for a new
or existing guide (§3.3); the delivery-correction ownership split (§2.2); the verification policy's
per-issue vs. milestone-entry question (there is no separate milestone-entry boundary, §3.4); the
worktree-provenance principle (use reliable provenance, not appearance — the exact available signals
are Step 5's own discovery, not a standing decision, §3.2).

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
