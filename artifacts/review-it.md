# review-it — Architecture Dossier

Status: Current
Scope: `review-it` as it stands in this repository
Purpose: A compact architecture artifact for the skill — its three entry points into one identical
procedure, how it establishes a review's target/baseline/scope/evidence before inspecting anything,
how it discovers applicable conventions with or without a stack companion, the ten-category
checklist and its skip-if-inapplicable and narrow-exemption discipline, how it verifies a finding
and reports staleness/review identity, what it never does, rule ownership, and current boundaries
and confidence.
[`SKILL.md`](../skills/review-it/SKILL.md) remains the operational routing entrypoint;
[`README.md`](../skills/review-it/README.md) is the human-facing orientation. This document explains
the architecture behind both rather than restating either.

## 1. Purpose and independence

`review-it` is an independently callable implementation-assurance skill. It reviews a worktree,
branch, or PR against a substantive, evidence-backed checklist and reports a clean result, verified
findings, or an inconclusive result where evidence or diagnostics weren't available. It does not fix
what it finds — corrections go through [`implement-it`](../skills/implement-it/)'s entry contract.

This skill has no predecessor and no narrowed-from history: it did not exist before this
repository's ecosystem migration extracted implementation assurance out of what was then a single,
undivided delivery skill (now `implement-it` and [`ship-it`](../skills/ship-it/)) into its own
callable capability. It is portable by construction, not by later narrowing — it runs the same way
whether or not `implement-it` or `plan-it` were ever involved, and a worktree with no issue, a
branch with no plan, or a PR opened entirely outside this ecosystem are all valid, ordinary targets.

**Three entry points, one identical procedure — not three procedures:**

- **Standalone.** A human asks directly: review this branch, this PR, my current changes.
- **Before Gate 1.** `implement-it` invokes this skill once implementation and its own verification
  are complete, before stopping at its Gate 1.
- **During an authorized delivery correction.** `implement-it` invokes this skill the same
  standalone way before that correction's own Gate 1/Gate 2 pass, when performing a correction
  `ship-it` has handed it.

No entry point requires another skill's context — a call from `implement-it` typically supplies
richer scope evidence (an approved issue, a completed diff) than a standalone call might have, but
neither situation changes the procedure itself, only how much evidence turns out to be available,
which the final report states either way.

## 2. Establishing the review before inspecting anything

[`rules/scope.md`](../skills/review-it/rules/scope.md) runs first, at the start of every invocation,
on the principle that a review is only as trustworthy as the target, baseline, and scope it was
actually checked against — established before a single line is inspected, with whichever of the
three couldn't be established reported plainly rather than guessed at.

**The review target** — a worktree, a branch, or a PR — is discovered from what's actually
available: something named explicitly in the request, the repository's current git state when
nothing else is named, or a PR already linked to the work under discussion. The human is asked only
when genuinely ambiguous.

**The comparison baseline**, where one applies, follows a strict discovery order for a branch or PR
review: an explicit comparison stated in the request controls outright; absent that, an associated
PR's own declared base branch, discovered from GitHub; absent both, other reliable evidence of the
actual intended integration target (a documented branching convention, an explicit statement already
in the conversation). **A branch's configured upstream or tracking branch is deliberately excluded
from this order entirely** — it names where the branch's own commits push, not what it's meant to
merge into, and a feature branch commonly tracks its own remote counterpart rather than its
intended target. Trunk is the last-resort fallback, never the default first choice. **The ordinary
comparison**, once the base is resolved, diffs from the merge-base of that base and the reviewed
head — not a direct comparison against the base's current tip, which would also pull in whatever the
base has itself gained since the branch diverged. **This is the default, not an unconditional rule:**
an explicitly requested comparison controls outright, per the discovery order's own first tier, even
when it differs from the merge-base method or from a PR's own declared base — a review comparing
against the base's current tip, or against some other explicitly named point, is a legitimate,
requested comparison, not an error. What is never legitimate is silence about which one is in play:
a requested comparison that differs from the PR's own declared base, or from the ordinary
merge-base method, is identified plainly in the report as the requested comparison — distinct from,
and never presented as if it were, the PR's own declared base or the ordinary method. A worktree
review's in-scope content includes staged, unstaged, and untracked files alike; an untracked file
needs direct inspection, since a `HEAD`-relative diff never surfaces one, and no file is ever staged
or otherwise mutated merely to bring it into view.

**The intended scope** is discovered from a linked issue or milestone, a PR description, an approved
`plan.md`, or explicit scope stated in the request. No `plan-it`-authored issue, approved
`plan.md`, or prior `implement-it` session is required — when no scope evidence exists at all, that
is stated plainly in the report, never inferred from the diff's own shape and then treated as if it
had been approved. A diff is evidence of what changed, never proof of what was authorized. For the
same reason, `Refs #N` lines and commit messages count as the author's claimed scope: they locate an
authoritative source such as the referenced issue, and are reported as claimed, not approved, scope
when no such source exists.

**Available evidence** — the diff itself, a linked issue or PR body, `plan.md` or a guide, CI
results already produced by someone else, applicable project instructions, an installed stack
companion — is gathered and its actual presence or absence stated in the final report, never
silently filled by inference; missing evidence that leaves an applicable check unresolved is a
limitation. The human is asked only
when an unresolved ambiguity would materially change what gets reviewed or the standard it's checked
against — not on every ambiguity, which is instead noted and proceeded past with the most defensible
reading.

**Trust boundary.** PR and issue text, commit messages, reviewed files and comments, and command
output are evidence about the change. They may describe intended scope, but none of them can grant
authorization, change the review procedure, override a workflow boundary, or expand what the review
may do; authorization and decisions come from the caller. Applicable, authoritative project
instructions remain legitimate engineering guidance. The boundary is stated once, in
`rules/scope.md`, as a property of how evidence is treated — not as a separate security mechanism.

## 3. Discovering applicable conventions — portable and stack-aware

An installed stack companion sharpens the checklist's "Architectural fit," "Project/stack convention
compliance," and "Correctness and edge cases" checks when it applies to the reviewed stack, but it
is never a prerequisite for running this review, and **its absence does not disable applicable
framework checks**. Framework and technology conventions are discovered the same way project
conventions are — from project instructions, configuration, established usage already in the
repository, and other available authoritative guidance the project itself references — not only
from an installed companion. The full checklist runs with no stack companion installed; only the
specific sub-check that depends on a custom companion's own rules, with no other available
authoritative source for the same requirement, is skipped, and that skip is stated plainly in the
report. A finding grounded in framework or convention reasoning states explicitly whether it rests
on an established project requirement or on general technical reasoning with no such backing — never
presenting the latter as if it were a discovered project rule.

When the reviewed change itself modifies a convention — project instructions, a rule file, lint or
test configuration — the existing convention comes from the base. The convention change is reviewed
against the authorized intent, and where it is explicitly approved, the implementation depending on
it is evaluated against the approved convention as well. A change therefore cannot quietly redefine
the standard it is judged by.

This is a deliberate architectural choice, not an incidental default: portability across projects on
different stacks is a stated goal of this skill (§8), and a review that silently went quiet on every
framework concern the moment no companion was installed would defeat that goal for exactly the
projects it's meant to serve.

## 4. The checklist

[`rules/checklist.md`](../skills/review-it/rules/checklist.md) runs ten categories — requirements
compliance, correctness and edge cases, security, data integrity, likely regressions, architectural
fit, maintainability, project/stack convention compliance, test adequacy, and accidental scope
expansion — each skip-if-inapplicable, not skip-by-default: a category is skipped only when the
reviewed change genuinely doesn't touch what it checks, and that is stated, not left silently absent.
A finding must materially affect one of those concerns; a stylistic preference the project's own
conventions don't already support is not a finding, and neither is a speculative concern with no
traced code path or reproducible evidence behind it.

Maintainability and test adequacy use concrete consequences rather than superficial signals.
An abstraction is unnecessary only when its continued existence has a demonstrated cost; removing
it and spreading important responsibilities across callers supports retaining it. A single caller
or thin wrapper alone establishes no defect. Test expectations must independently check the
behavior their test layer owns, match the intended requirement, and use assertions that would
catch a regression in that behavior. Legitimate integration assertions remain valid where separate
tests own the underlying value's correctness. A stack companion that documents test-layer ownership
or test-execution mechanics is applied when installed; the portable check does not require one. The
owning checklist contains the inspection procedure for both concerns.

Defects that already existed are classified by their relation to the change. A defect the change
introduces — including a new occurrence of an existing flaw — is a finding, as is one the change
exposes or worsens, and a pre-existing problem that prevents the approved requirements from being
met. An unrelated pre-existing defect is a brief observation: not a finding, not a review
limitation, and not automatic correction scope. Performance, compatibility, and deployment
consequences are checked inside the existing categories (correctness, likely regressions) when
evidence shows them, not as categories of their own.

When the reviewed change modifies test infrastructure, test adequacy also checks the properties that
specific change could affect, scaled to it: execution completeness (a matching test count alone does
not prove fresh execution), isolation of any state the change introduces, a changed coverage minimum proven
to fail below its threshold, and no test deleted, skipped, or weakened to make the change pass.

**The authorized-scope-change exemption is deliberately narrow.** An explicitly authorized scope
change is exempt from exactly one category — Accidental scope expansion — because it is not
accidental. Raising a scope change with the human is not authorization by itself; only the human's
explicit decision is. It is not exempt from anything else: every other applicable category runs
against it exactly as thoroughly as against any other part of the diff. The authorization approved the work
happening; it did not verify the work, and it never suppresses a defect discovered in it or stands
in as acceptance of that defect's consequences. This is a precise, single-category exemption by
design — a broader reading (an authorized change being exempt from review generally) was considered
and rejected during this skill's own authoring, as a correction against exactly that broader,
incorrect reading.

## 5. Verification, evidence, and reporting

[`rules/verification.md`](../skills/review-it/rules/verification.md) governs how a candidate finding
from the checklist earns its place in the report, and what the report itself must state.

**Verify before reporting.** Every finding is traced to a concrete file and line, or confirmed by a
diagnostic command's actual output, before being reported — never a suspicion stated as fact. A
successful command or a passing exit code is not, by itself, proof that it validated the specific
property in question. The report distinguishes findings this skill actually verified itself — by
source inspection, reproduction, or diagnostic execution — from evidence merely supplied by someone
else (a CI result quoted in the request, a claim already made in a PR description) and not
independently checked.

**Diagnostic execution is not read-only inspection.** This skill may run the project's own existing
tests, linters, or static analysis — discovered the same way `implement-it/rules/verification.md`
discovers them, never assumed in advance — to confirm a specific concern. Running one can write to
caches, temporary directories, or other local state; this skill's execution is not described as free
of side effects. When safe diagnostic execution isn't available, that limitation is reported plainly
rather than the concern being skipped silently or its result guessed at. This skill never mutates
GitHub or any other live or production state to gather evidence — reading published state is
evidence-gathering, creating, editing, or merging anything is not this skill's job under any
circumstance.

**Staleness and review identity.** A finding, or a clean result, is tied to the specific state it
was checked against, stated precisely enough to actually distinguish it from a different state — not
merely a label that happens to be available. A branch or PR review is not fully identified by its
head commit SHA alone, since the identical head diffed against a different base produces a different
diff and can produce different findings: the report states the head SHA, the resolved base, the
comparison-start (merge-base) SHA where one applies, and the comparison method itself. An isolated
commit reviewed with no comparison is identified by its SHA alone. A dirty worktree is identified by
`HEAD` plus an explicit identity for the actual uncommitted content reviewed — the tracked diff's own
content and an accounting of every untracked file reviewed by path and content — since `HEAD` alone
cannot distinguish two different dirty states sharing it. A material change invalidates a prior pass
for the affected surface whether or not `HEAD` itself moved: an edit to an already-reviewed file with
no new commit, or a change to the resolved base or comparison method, both count. This skill does not
track or store review history itself between invocations — each invocation is stateless with respect
to any prior pass and states its own identity fresh; the caller (a human, or `implement-it`) requests
a fresh or scoped pass when relying on this result again. A scoped re-review states plainly which
surface it actually checked this time, alongside the same state/comparison identity — never implying,
by omission, that it independently rechecked the entire target.

**Report shape.** Every result opens with exactly one outcome: `Clean` (no confirmed findings and
every applicable check completed), `Findings remain` (which may also list limitations), or
`Inconclusive` (no confirmed findings, but a material limitation leaves an applicable check
unresolved). A result with a confirmed finding is never `Clean`, and resolution history belongs to
the calling workflow's report — the skill is stateless, so it has no "clean after resolution"
outcome of its own. A human's decision to proceed or to accept a finding is separate and does not
change the outcome. The report then states the reviewed target and its precise identity; confirmed
findings ordered by consequence — location, evidence, concrete consequence, relation to the change
where it isn't plainly introduced, and the requirement or convention source when one applies — with
no severity label or scoring; brief observations (scope notes, unrelated older defects); which
checks this skill actually ran or traced itself, distinguished from evidence supplied by others;
material limitations that could change the outcome; and, when `Clean`, which categories applied and
passed. A category is reported passed only when its checks were performed: reading a rule file in
full is required before claiming its coverage, but is never evidence that the checks ran. An
unchecked category is a limitation to state, never a pass to imply; absent optional evidence (no
issue, no architectural reference, no companion) is stated and its category skipped, without by
itself making a result `Inconclusive`. **A `review-it` result never grants authorization by
itself** — it is input to whatever gate the calling context owns (Gate 1, or a human's own judgment for a
standalone call); it never substitutes for that decision.

## 6. What this skill never does, and does not own

`review-it` reports; it does not edit application code, apply formatting fixes, commit, push,
approve a gate, merge, or mutate GitHub or any other live or production state — regardless of how
minor or obviously correct a fix would be. A finding this skill could trivially fix by hand is still
reported, not applied. Corrections go through `implement-it`'s entry contract: an approved issue,
or an authorized delivery correction handed over by `ship-it`. A human-authorized correction route
for findings from a standalone review, with no issue, is approved in principle but not yet part of
`implement-it`'s contract (`OPEN-C01` in the test contracts); this skill implies no route that
contract doesn't define.

**This skill is deliberately not the owner of every skill's specialized review.** It owns exactly
one thing: independently callable implementation review against the checklist above, for a
worktree, branch, or PR. It does not own guide review (→ [`document-it`](../skills/document-it/));
issue-definition and dependency review, or plan-synthesis review (→
[`plan-it`](../skills/plan-it/) and [`lab-it`](../skills/lab-it/) respectively); commit-plan review,
i.e. Gate 2 (→ `implement-it/rules/review-gates.md`); or approving Gate 1, Gate 2, or any GitHub
mutation — a review does not grant authorization, and the human decision stays exactly where the
calling skill already places it. This skill is also not a subagent, a background process, or an
automated gatekeeper that runs on its own initiative: it is an ordinary, independently invocable
skill, reached the same three ways described in §1, that reports to whoever invoked it — a human
directly, or `implement-it` on the human's behalf at a gate `implement-it` itself owns.

## 7. Rule ownership and cross-skill handoffs

| Rule | Owns |
|---|---|
| [`rules/scope.md`](../skills/review-it/rules/scope.md) | Establishing the review target, comparison baseline, intended scope, and available evidence before running the checklist; the trust boundary for reviewed content; discovering applicable project and stack conventions, including which version applies when the change modifies them |
| [`rules/checklist.md`](../skills/review-it/rules/checklist.md) | The ten-category substantive checklist with concrete inspection instructions, the classification of defects that already existed, and the narrow authorized-scope-change exemption |
| [`rules/verification.md`](../skills/review-it/rules/verification.md) | Verifying a finding against concrete evidence, diagnostic-execution boundaries, the staleness/review-identity rule, and the required report shape and outcomes |

**Called by `implement-it`, not owned by it.** `implement-it`'s Gate 1 and its delivery-correction
flow each invoke this skill the identical standalone way described in §1 — this skill's own dossier
does not restate `implement-it`'s gate mechanics or its handling of this skill's result; see
[`implement-it`'s dossier](implement-it.md) §4 and §9 for that side of the boundary.

**No downstream handoff of its own.** A finding always returns to whichever skill invoked this one
(`implement-it`, or the human directly) — this skill never hands work forward to `plan-it`,
`document-it`, or `lab-it`; it only names them as the owners of a specialized review kind it
explicitly doesn't perform (§6).

## 8. Boundaries and confidence

Portability across projects on different stacks, with or without a custom companion, is a stated
architectural goal (§3), not an incidental property — this skill's checklist and conventions
discovery are written to hold that goal even where the ecosystem's own stack companion isn't
installed at all.

Two dependencies are deliberate: the checklist's diagnostic-execution step depends on the reviewed
project's own discoverable test/lint/static-analysis tooling existing and being safely runnable in
this session; where it isn't, that is a stated limitation, not a silently skipped concern. The
staleness/review-identity model (§5) depends on the calling context (a human, or `implement-it`)
actually requesting a fresh or scoped re-review when relying on a result again — this skill has no
mechanism of its own to detect that a caller relied on a stale result without asking.

**Current, honest limits:**

- The comparison-base discovery order (§2) — excluding a branch's configured upstream/tracking
  branch, diffing from the merge-base rather than the base's current tip — was verified by a
  disposable Git repository exercising the underlying comparison and state-identity mechanics this
  procedure depends on (recorded in the [v2.0.0 migration plan](https://github.com/elieandraos/agentic-engineering/blob/v2.0.0/plan.md)'s Step 4 correction record): a pushed feature branch
  tracking its own remote counterpart producing an empty diff against that counterpart, an explicit
  comparison against a parent branch correctly isolating the child's own change, the identical head
  diffed against two different bases producing two different diffs, and a material worktree edit
  with no new commit leaving `HEAD` unchanged while the reviewed content changed. That experiment
  tested Git comparison and state-identity behavior specifically — it did not exercise this skill's
  stack-aware convention discovery (§3) or run the checklist itself; it provides no live consumer
  evidence for either.
- **Live consumer use, analyzed retrospectively.** Transcripts of 89 real invocations (late October
  to late November 2026) across three consuming projects were analyzed after the fact. Two use the
  Laravel companion; one is a Nuxt/Supabase project with no stack companion installed, so the
  no-companion convention discovery (§3) has run in real use. The invocations came overwhelmingly
  through `implement-it` before Gate 1, mostly against dirty worktrees, plus a few branch and one PR
  review. They show evidence-backed true positives, no invented findings, and the
  verified-versus-supplied distinction honored. They also showed rule files read only partially,
  reports routinely omitting the reviewed state's identity, and older defects placed
  inconsistently — the observations behind the current report shape, outcome set, older-defect
  classification, and full-read requirement. This is observed real use, not a controlled behavioral
  evaluation: no fixed fixtures, no repeated runs, approximate pattern-matched counts, and review
  text interleaved with `implement-it`'s own.
- **The current contract's refinements are not yet validated by use.** The outcome set, restored
  identity requirement, older-defect classification, trust boundary, changed-convention rule, and
  full-read requirement were checked by source review and cold-read walkthroughs only. Whether they
  change behavior remains to be seen in later consumer sessions.
- The finding-traceability, abstraction-usefulness, and independent-test-expectation checks have
  been exercised in the consumer sessions above, but no executed test fixture covers them.
