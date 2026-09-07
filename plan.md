# Ecosystem migration plan — Lab · Document · Plan · Implement · Review · Ship

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
| `implement-it` (new) | Approved issue/milestone intake; working-branch readiness; implementation; verification; issue-level Git workflow; Gate 1 and Gate 2; commit construction; authorized push; issue closure and its completion comment; next-issue recommendations. | Choosing what work exists; milestone PR readiness/creation, milestone closure, release (→ `ship-it`). A specific-issue request ends after that issue's authorized lifecycle — it does not imply milestone-delivery authorization. |
| `review-it` (new) | Independently callable implementation assurance for a worktree, branch, or PR — callable standalone or by `implement-it` before Gate 1. Reports verified findings, unresolved limitations, or a clean result. | Implementing corrections (returns to `implement-it`); investigation-quality, guide, plan-synthesis, issue-planning, or commit-plan review — those stay with their owning skills. |
| `ship-it` (narrowed) | Milestone PR readiness; authorized PR creation; post-merge delivery; milestone closure; release preparation/publication; resulting-state verification. | PR approval and merge — the human retains both. |
| Stack companions (unchanged) | Technology-specific implementation conventions (e.g. `laravel-inertia-stack`). | Becoming a pipeline stage; used when available, not required for every implementation. |

**Handoffs**

```
lab-it ──approved plan.md──▶ plan-it ──approved issue/milestone──▶ implement-it
  ▲                                                                     │
  └── draws on, when stale/missing ── document-it                      ├──before Gate 1──▶ review-it ──findings──▶ implement-it
                                                                        │
                                                                        └──milestone ready for delivery──▶ ship-it ──▶ human (PR approval, merge, release)
```

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
| `rules/doc-style.md` | `document-it/rules/doc-style.md` | Moved verbatim |
| `rules/template.html` | `document-it/rules/template.html` | Moved verbatim |
| `rules/review.md` (guide review) | `document-it/rules/review.md` | Moved verbatim |
| `rules/maintenance.md` | `document-it/rules/maintenance.md` | Moved verbatim |
| `rules/plan-synthesis.md` | Stays `lab-it/rules/plan-synthesis.md` | Unchanged |

No file outside `lab-it` references `doc-style.md`, `template.html`, `lab-it/rules/review.md`, or
`maintenance.md` (confirmed by repo-wide search) — this move has no external cross-reference
fallout.

### 2.2 `ship-it` → `implement-it` (new) + `ship-it` (narrowed)

| Current file | New owner / path | Change |
|---|---|---|
| `rules/review-gates.md` | `implement-it/rules/review-gates.md` | Moved; Gate 1's stop condition gains a `review-it` bullet (Step 4, §3.1) |
| `rules/commit-boundaries.md` | `implement-it/rules/commit-boundaries.md` | Moved verbatim |
| `rules/verification.md` | `implement-it/rules/verification.md` | Moved; boundary set revised per approved verification policy (Step 5, §3.4) |
| `rules/issue-closure.md` | `implement-it/rules/issue-closure.md` | Moved; gains partial-mutation re-query (Step 5, §3.2) |
| `rules/sequencing.md` | `implement-it/rules/sequencing.md` | Moved verbatim, including its hand-off pointer to `ship-it/rules/milestone-completion.md` (that file stays in `ship-it`, so the pointer's target is unaffected — only its own path changes) |
| `rules/milestone-completion.md` | Stays `ship-it/rules/milestone-completion.md` | Gains authorized-PR-creation (new, §3.5); "three conditions" language becomes four wherever the approved verification policy adds a PR-readiness CI condition (Step 5) |
| `rules/release.md` | Stays `ship-it/rules/release.md` | Unchanged in substance; its "PR creation and merge strategy are not owned by this rule" line stays true and now points at `milestone-completion.md` as the file that does own PR creation, not at itself |
| `SKILL.md` | Split | `implement-it/SKILL.md` (new) takes activation triggers `implement issue`, `commit issue`, `close issue`, `what's next in milestone`; `ship-it/SKILL.md` (narrowed) keeps `is milestone ready for a PR`, `create milestone PR`, `is milestone ready to close`, `release {version}` |
| `README.md` | Split | Same split as `SKILL.md` |

**Cross-references outside `ship-it` that this split breaks and must be updated** (found by repo-
wide search, not assumed):

| File | Line(s) | Current text | Required update |
|---|---|---|---|
| `plan-it/SKILL.md` | 93 | "`ship-it` owns the downstream Git/GitHub delivery workflow — branch readiness..." | → `implement-it` |
| `plan-it/rules/discovered-work.md` | 174 | "`ship-it` owns the downstream Git/GitHub delivery workflow" | → `implement-it` |
| `plan-it/rules/review.md` | 293 | "implementation review, issue closure, or delivery progression (`ship-it`)" | → `implement-it` (delivery progression stays a `ship-it` mention only for milestone/release) |
| `plan-it/rules/issue-conventions.md` | 235, 252, 265 | `ship-it/rules/verification.md` | → `implement-it/rules/verification.md` |
| `plan-it/rules/issue-conventions.md` | 155, 277, 299 | `ship-it`'s `rules/milestone-completion.md` | Unchanged — that file stays in `ship-it` |
| `plan-it/rules/sequencing.md` | 8, 82, 123 | "`ship-it`, particularly its own `rules/sequencing.md`" / "`ship-it`'s job after creation" | → `implement-it` for branch readiness and next-issue recommendation; a milestone-level mention (readiness/closure) stays `ship-it` |
| `plan-it/README.md` | 42 | "[`ship-it`](../ship-it/) — this skill plans the work, it doesn't build it." | → points at `implement-it` as the immediate next stage, with `ship-it` named separately for milestone delivery |

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

### 3.2 Recovery

Smallest sufficient additions to the file that already owns the adjacent behavior — no new file,
gate, or execution context, per the audit's own recommended-smallest-change framing (decision-brief
topic 3):

| Gap (audit finding) | Owning file after migration | Proposed addition |
|---|---|---|
| Worktree provenance (finding, Section 3 scenario 3) | `implement-it/rules/verification.md` §"Discover the verification starting state" | Before treating a pre-existing dirty worktree as safe to build on, check whether it looks like this session's own in-progress work (recent, uncommitted, matching the approved scope) versus unrelated content, and ask when ambiguous. **Open**: the exact signal used to judge "matches the approved scope" is not decided here. |
| Partial GitHub mutation before resuming a batch (finding #10) | `plan-it/rules/sequencing.md` (issue batches); `ship-it/rules/milestone-completion.md` and `rules/release.md` (milestone/release mutations) | Before creating/mutating more of a batch, re-query GitHub for members this same interrupted batch may already have created — extends the existing post-mutation re-fetch pattern already present in four files, not a new mechanism. |
| Canonical issue-definition durable storage (finding #21) | `plan-it/rules/issue-conventions.md` | **Open, deliberately not resolved here** — a stated default location, mirroring `plan.md`'s own stated-default pattern, needs its location, creation/update timing, approval relationship, mapping to created issues, and retirement all decided together at Step 5's review. No file is introduced by this plan. |
| Approval staleness after a material change (finding #13/#4) | `implement-it/rules/review-gates.md` | Before Gate 2 and before push, compare the current diff/issue body against what was approved; a material difference invalidates that approval and requires re-review — extends the existing "never silently convert an unresolved decision into a fact" principle already stated four times across the ecosystem. |
| Verification evidence tied to the state checked | Existing report shapes (Gate 1 report, `review-it` findings, closing comment) | Cite the commit SHA/diff the evidence was produced against, so a later reader can tell whether it still covers current state. |

### 3.3 Documentation output (`document-it`)

Covers creation and maintenance for both Markdown and Artifact — the audit explicitly flags that a
fallback for creation without an equal one for maintenance/update would be incomplete (decision-
brief topic 4); this plan does not repeat that gap:

- **Target discovery.** Artifact: ask the user for the URL when it can't otherwise be determined
  (the smallest sufficient fix for finding #4 — no independent lookup mechanism is invented).
  Markdown: discover an existing guide by the project's own documentation convention before
  assuming Artifact is the only medium.
- **Identity preservation.** Artifact: same `url`, same favicon (existing `maintenance.md` rule,
  unchanged). Markdown: same file path, same front matter/title, stated with equal weight to the
  Artifact rule — not an afterthought.
- **Format-appropriate review.** One review procedure (`document-it/rules/review.md`), not two —
  the architectural-communication checklist generalizes across both media; a handful of items stay
  medium-conditional (favicon/URL checks apply to Artifact only; a link-integrity/structure check
  applies to Markdown only).
- **Unavailable capability.** When the Artifact tool is unavailable, Markdown is the default output
  rather than no output — covering both the "new guide" and "update an existing guide" workflows.

**Open**: the exact default location/naming convention for a Markdown guide (mirroring `plan.md`'s
stated repo-root default) is not fixed here — proposed at Step 2, decided at that step's review.

### 3.4 Verification policy — explicit comparison

**Existing** (current, committed `ship-it/rules/verification.md`): narrowest-reliable scope per
commit during construction; one full-suite run before Gate 1 (proves the complete working tree
before any commit split exists); one full-suite run at the completed-issue boundary (proves the
reconstructed commit history); isolation verification as a deliberate escalation for load-bearing
ordering; both full-suite runs always required, never reused because the other already passed; no
automated full-suite requirement at milestone PR-readiness — that gate currently relies on closed-
issue count plus a human's direct confirmation of manual testing.

**Proposed** (this plan, per the instruction producing it): targeted tests during implementation and
corrections (unchanged); additional checks scoped to whatever a `review-it` finding needs verified
(new); the full project-defined suite before Gate 1 for **both** single-issue and milestone entry
(new — a milestone-entry baseline, not only a per-issue one); after commit construction,
proportionate verification, repeating the full suite when relevant code/configuration/execution
state changed (a conditional replacing today's unconditional "always run it" at that boundary);
full-suite verification of the final combined milestone state at PR readiness, normally through CI
(new — today's PR-readiness gate has no automated full-suite condition); reuse prior results only
when their coverage and relevant state are demonstrably applicable (a new, general reuse rule —
today's rule is unconditional, "don't drop either run because the other passed").

**What changes, stated plainly.** This is not a documentation clarification like Section 1's
discoverable-configuration-vs-fixed-structure finding (#20) — it changes an existing, unconditional
requirement (two full-suite runs, always both) into a conditional one, and adds two new boundaries.
**This plan does not treat that change as approved.** What each existing boundary proves must be
preserved regardless of the final wording: the pre-Gate-1 run proves the working tree as a whole
before any split; the completed-issue run proves the actual assembled commit history reconstructs
the same result; isolation verification's escalation stays reserved for load-bearing order, not the
default. The two new boundaries would prove, respectively, that the combined milestone branch state
is coherent before PR, and that the actual delivery-boundary environment (which no local run fully
replicates) is genuinely green.

**Open, for Step 5's review**: the exact reuse-eligibility rule (what counts as "demonstrably
applicable" prior coverage), and whether the new milestone-entry and PR-readiness-CI boundaries are
mandatory in every case or discovered per project (following the existing discoverable-tooling
model in `verification.md` — this rule already refuses to prescribe a specific test runner or
command; nothing here should hardcode one either).

### 3.5 `ship-it`'s new PR-creation responsibility

Today, PR creation is explicitly out of scope everywhere it's mentioned (`SKILL.md`'s "What it does
not own"; `milestone-completion.md`'s "It does not create the PR... PR creation, review, and merge
stay human-owned"; `release.md`'s "PR creation and merge strategy are not owned by this rule"). The
agreed target gives `ship-it` **authorized** PR creation — the human still approves and merges.

Proposed shape, mirrored from `release.md`'s already-reviewed pattern (discover policy → draft →
human approval → act → validate), so this is a bounded, precedented addition:

1. Once Milestone PR readiness's three conditions pass, discover the project's PR-target/base-branch
   convention the same way `release.md` discovers release policy (explicit repo convention first,
   then inferred history, then ask if ambiguous).
2. Draft a PR description at PR altitude, referencing the milestone (the existing "milestone-PR
   reference convention" `milestone-completion.md` already states as an observed contract — this
   makes it something `ship-it` itself produces instead of only being aware of).
3. Present title, base/head branches, and body together; require explicit human approval before
   creating anything — the same two-step "may I start" / "is this exact content right" split
   `release.md` already uses.
4. Create the PR through the discovered mechanism; re-fetch and validate the result (number, base,
   head, title, body) instead of trusting the creation command's exit code.

**Open**: this exact procedure has not itself been reviewed the way `release.md` was — it is
proposed for Step 3's review, not pre-approved by virtue of being written down here.

---

## 4. Behavior deltas

**Preserved, moved verbatim.** `lab-it`'s investigation discipline and plan-synthesis method;
`document-it`'s entire guide-writing grammar, template, review checklist, and maintenance procedure
(content unchanged, only file location and owning skill change); `implement-it`'s Gate 1/Gate 2
state machine, commit-boundary derivation, existing verification lifecycle, issue-closure procedure,
and branch-readiness/next-issue-recommendation logic; `ship-it`'s milestone PR-readiness conditions
(pending the Step 5 fourth-condition decision), closure gate, and release-policy
discovery/drafting/publish/validation; the two-gate-never-collapsed invariant; closure always opt-in;
the existing discoverable-configuration-vs-fixed-structure distinction (finding #20, untouched by
this migration); Git/GitHub as intentional core substrate.

**Clarified, not changed.** Gate 1/Gate 2 are now explicitly `implement-it`'s own gates, not
ambiguously "`ship-it`'s"; file extension does not decide `document-it`-vs-`lab-it` ownership —
`plan.md` stays `lab-it`'s; milestone PR-readiness stays "a report, not a mutation" for the readiness
conditions themselves, distinguished from the new PR-*creation* mutation that follows a positive
report; a specific-issue request ending after that issue's lifecycle (already true — `sequencing.md`
already forbids chaining into the next issue) is now stated as the explicit boundary between
`implement-it` and `ship-it`/human authorization for milestone delivery.

**New behavior** (agreed target for this migration, not an extraction of already-existing,
undocumented practice — stated plainly per the audit's own caution, decision-brief topic 1):
`review-it` as an independently callable skill; Gate 1's substantive checklist (§3.1); `ship-it`'s
authorized PR creation (§3.5); the recovery-contract additions (§3.2); Markdown as a first-class,
equally-maintained `document-it` output alongside Artifact (§3.3).

**Proposed, still requiring a decision** (not silently approved by this plan): canonical
issue-definition durable storage location and lifecycle (§3.2); the verification-policy reuse rule
and whether the two new full-suite boundaries are mandatory-always or discovered-per-project (§3.4);
`document-it`'s Markdown-fallback default location/naming (§3.3); `review-it`'s per-item checklist
wording, beyond the agreed category list (§3.1); the worktree-provenance signal and the
approval-staleness re-confirmation trigger's exact wording (§3.2); `ship-it`'s new PR-creation
procedure, proposed but not yet reviewed on its own (§3.5).

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
  and approved this plan, including the open decisions in §4.
- **Result to present.** This document, plus the material-decisions list (§7).

### Step 2 — Extract `document-it`, narrow `lab-it`

- **Outcome/boundaries.** `document-it` exists as a fully self-contained skill (§2.1); `lab-it`
  no longer routes to guide-workflow files; §3.3's reviewed decisions are implemented here, since
  this is `document-it`'s own domain.
- **Affected files.** New: `document-it/SKILL.md`, `README.md`, `rules/doc-style.md`,
  `rules/template.html`, `rules/review.md`, `rules/maintenance.md`. Modified: `lab-it/SKILL.md`,
  `lab-it/README.md`. Unaffected: `lab-it/rules/plan-synthesis.md`.
- **Preserved vs. changed.** Guide grammar, template, review checklist, and maintenance procedure
  move verbatim. Deliberate additions: the Markdown-fallback and format-appropriate-review decisions
  from §3.3, once resolved.
- **Dependencies.** §3.3's open items resolved first (or resolved as part of this step's own
  review, before merge — not deferred past this step).
- **Acceptance criteria.** `document-it` activates on "document/update/review a guide" without
  invoking `lab-it` except for its stated investigation-reuse step; no reference to
  `doc-style.md`/`template.html`/guide `review.md`/`maintenance.md` remains under `lab-it/`; a
  repo-wide search confirms no external file still points at the old paths.
- **Validation (static).** Walk through "document existing architecture," "update an existing
  guide," and "review a guide" against `document-it`'s new files only.
- **Result to present.** Diff of new `document-it` files and narrowed `lab-it` files, plus
  confirmation that no `plan-it`/`ship-it` file needed updating (verified — none references the
  moved files).

### Step 3 — Extract `implement-it`, narrow `ship-it`

- **Outcome/boundaries.** `implement-it` exists and handles single-issue and milestone-mode
  implementation identically to current `ship-it`, using only moved files; `ship-it` is narrowed to
  milestone delivery and gains the proposed PR-creation procedure (§3.5); every cross-reference in
  §2.2's table is updated in this same pass.
- **Affected files.** New: `implement-it/SKILL.md`, `README.md`, `rules/review-gates.md`,
  `commit-boundaries.md`, `verification.md`, `issue-closure.md`, `sequencing.md`. Modified:
  `ship-it/SKILL.md`, `README.md`, `rules/milestone-completion.md` (PR creation), `rules/release.md`
  (cross-reference reconciliation only); `plan-it/SKILL.md`, `rules/discovered-work.md`,
  `rules/review.md`, `rules/issue-conventions.md`, `rules/sequencing.md`, `README.md` (handoff
  pointers only — no owned-content change).
- **Preserved vs. changed.** Gate mechanics, commit derivation, existing verification lifecycle,
  issue closure, branch readiness, and next-issue recommendation move verbatim. Deliberate: `ship-it`
  gains PR creation (§3.5, not yet reviewed on its own — implemented here as a proposal for this
  step's review, not pre-approved). `review-it` is **not** wired into Gate 1 yet — that's Step 4;
  Gate 1's text in this step notes the pending integration explicitly, so the transition state is
  never ambiguous.
- **Dependencies.** Step 2 complete (kept sequential so only one mixed-ownership state exists at a
  time, even though the two domains are independent).
- **Acceptance criteria.** `implement-it` reproduces current `ship-it` behavior for "implement issue
  #N" end to end; `ship-it` additionally handles an authorized PR-creation request once PR readiness
  passes; no file anywhere still says "`ship-it`" for branch readiness, Gate 1/2, commits,
  verification, or issue closure; `release.md`'s "not owned by this rule" statement no longer
  conflicts with `milestone-completion.md`.
- **Validation (static).** Single-issue implementation walkthrough; milestone-mode walkthrough
  (branch readiness → issues → empty ready set → hand off to `ship-it`); the new PR-creation flow
  through to a human-merge stop.
- **Result to present.** Diff of new `implement-it` files, narrowed `ship-it` files, the proposed
  PR-creation procedure text, and every cross-reference update from §2.2's table, for review.

### Step 4 — Establish `review-it`, integrate before Gate 1

- **Outcome/boundaries.** `review-it` exists as a standalone skill, callable independently of
  `implement-it`; `implement-it/rules/review-gates.md`'s Gate 1 consumes its result.
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
- **Affected files.** `implement-it/rules/verification.md`, `rules/review-gates.md`,
  `rules/issue-closure.md`; `plan-it/rules/sequencing.md`, `rules/issue-conventions.md` (whichever
  owns the approved canonical-definition-location decision); `ship-it/rules/milestone-completion.md`
  and `rules/release.md` (partial-mutation re-query; PR-readiness's condition count, if a CI-based
  fourth condition is approved — every "three conditions" reference in that file updated together).
- **Preserved vs. changed.** This step is entirely deliberate change — every edit traces to §3.2 or
  §3.4 above; nothing here is a pure move.
- **Dependencies.** Steps 2-4 complete (files must exist at their new locations); the specific open
  decisions in §3.2 and §3.4 resolved before their corresponding edits — this step cannot silently
  fill them in.
- **Acceptance criteria.** A worktree-provenance check exists and is exercised by a scenario with
  pre-existing uncommitted changes; partial-mutation re-query exists for both `plan-it`'s issue
  batches and `ship-it`'s milestone/release mutations; the canonical-issue-definition location is
  stated, consistent with `plan.md`'s own default-location pattern; any new PR-readiness condition
  doesn't contradict "report, not mutation."
- **Validation (static).** Interrupted-worktree resume; interrupted issue-batch-creation resume;
  approval-then-material-change resume; PR readiness against an open PR with red CI.
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
investigation without documentation and an approved `plan.md` handoff; guide creation/update in both
supported formats; single-issue and branching milestone dependency flows; standalone review and
finding/correction/re-review; interrupted planning and implementation; milestone PR creation through
human merge and authorized release. Step 6's `useOrbit` exercise and portability check are
**execution**, not static walkthroughs — planned only, per that step's own scope, not performed by
this plan.

## 7. Material decisions still needed

1. Canonical issue-definition durable storage: location, creation/update timing, approval
   relationship, mapping to created issues, retirement (§3.2, finding #21).
2. Verification-policy reuse rule and whether the milestone-entry/PR-readiness-CI boundaries are
   mandatory-always or discovered-per-project (§3.4) — this changes an existing unconditional
   requirement and is not treated as approved by writing it here.
3. `document-it`'s Markdown-fallback default location/naming convention, and whether
   format-appropriate review needs any further split beyond the shared file with conditional items
   (§3.3).
4. `review-it`'s per-item checklist wording, beyond the agreed category list (§3.1) — authored and
   reviewed at Step 4, not fixed by this plan.
5. The exact worktree-provenance signal and the approval-staleness re-confirmation trigger's wording
   (§3.2).
6. `ship-it`'s proposed PR-creation procedure (§3.5) — precedented by `release.md`'s pattern, but
   not itself reviewed yet.
7. `laravel-inertia-stack`'s unresolved precedence rule for conflicting Boost-skill guidance
   (finding #7) — out of scope for this migration; flagged only so it isn't lost, not addressed by
   any step above.

---

## Verification of this planning pass

- `git status --porcelain` before writing: only `control-room-responsibilities.md`,
  `skills-audit.md`, `subagents.md` untracked; `plan.md` did not exist.
- Only `plan.md` was created by this task. No skill file, `README.md`, `roadmap.md`, or `docs/`
  file was edited. Nothing was staged, committed, pushed, or changed on GitHub.
