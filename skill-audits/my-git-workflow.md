# my-git-workflow — Skill Dossier

Status: Current
Scope: `my-git-workflow` as it stands at `agentic-engineering@main`
Purpose: Deep-dive supporting analysis of the current skill — architecture, rationale, boundaries,
evidence, and open questions.

## 1. Purpose and status

This is a supporting deep-dive document for the `my-git-workflow` skill, not the skill itself. The
skill's own files — `SKILL.md`, `README.md`, and `rules/*.md` — remain the operational source of
truth. Where anything here appears to disagree with them, the skill files win and this document is
stale, not the other way around.

This document exists to inspect what the skill files don't inspect themselves: why the seven rules
are divided the way they are, where each one's boundary actually sits, what the human-decision model
protects, how the verification ladder holds together, what evidence justifies specific methodology
choices, and which questions are genuinely still open. A maintainer should be able to read this
alongside the skill files and understand not just what the skill says to do, but why it's built this
way.

This is a dossier, not a history book. It describes the skill as it currently stands. An earlier
draft of the methodology, or the project the methodology was extracted from, is mentioned only when
it explains why a current rule exists — never as a chronological account of how the skill got here.

## 2. What the skill is

`my-git-workflow` is the delivery stage of the Agentic Engineering pipeline. It:

- starts only from an approved, dependency-ready GitHub issue — it never decides what work should
  exist;
- is intentionally Git/GitHub-centered: Git and GitHub are core substrate for this methodology, not
  an abstraction layer meant to be swapped for something else;
- covers everything from implementation review through verified delivery, and the milestone/release
  lifecycle that follows a merge;
- does not own application-stack behavior, framework conventions, or any implementation knowledge —
  that comes from whatever stack-specific skills are loaded alongside it.

## 3. Pipeline position

```
my-architecture-laboratory  →  my-feature-planning  →  my-git-workflow
   (understand reality)         (approved work)          (verified delivery,
                                                            milestone/release lifecycle)
```

`my-feature-planning` hands off exactly one thing: an approved, drafted, reviewed GitHub issue (or a
validated Discovered-work finding that has gone through the same drafting/review pipeline). Planning
states its own boundary outright — its "responsibility ends at issue creation" — and everything from
implementation onward, including commit structure and the release/milestone lifecycle, is explicitly
out of its scope and explicitly in `my-git-workflow`'s.

That boundary is bidirectional and unusually well matched, not just asserted from one side:
`my-feature-planning`'s issue-conventions rule states that milestone closure "is not decided here,
and never at planning time," and names `my-git-workflow`'s `rules/milestone-completion.md` as the
file that owns the gate built on top of the classification planning does define.

## 4. Current end-to-end lifecycle

Two paths exist, chosen by which kind of milestone the approved issue belongs to. Both share the
same implement → verify → Gate 1 → commit plan → Gate 2 → build → verify spine; they diverge on what
happens before it (branch readiness) and after it (what a validated closure triggers next).

```
approved, dependency-ready issue  (handed off by my-feature-planning)
│
├── Backlog / hotfix
│     → work on the repository trunk branch (a checkout mismatch is surfaced to the human,
│        never silently worked around or switched — no feature branch, no branch decision)
│     → implement
│     → VERIFY — full-project suite, pre-Gate-1 (lint/format/static + full regression)
│     → GATE 1 — implementation review
│     → derive commit plan
│     → GATE 2 — commit-plan review
│     → build semantic commits  (VERIFY — narrowest reliable scope per commit)
│     → VERIFY — full regression suite, completed-issue boundary
│     → ask: close the issue?  →  closing recipe + post-mutation validation
│     → recompute ready set within Backlog → next-work recommendation
│     → done — no PR, no milestone-level gate, no release trigger
│
└── Milestone issue
      → inspect current branch — not yet the milestone's shared branch?
          → recommend a branch name derived from the milestone's nature, ask before
             creating/switching
      → implement issue
      → VERIFY — full-project suite, pre-Gate-1 (lint/format/static + full regression)
      → GATE 1 — implementation review
      → derive commit plan
      → GATE 2 — commit-plan review
      → build semantic commits  (VERIFY — narrowest reliable scope per commit;
          VERIFY — isolation, escalation only, when an intermediate committed state's
          own correctness must itself be proven)
      → VERIFY — full regression suite, completed-issue boundary
      → ask: close the issue?  →  closing recipe + post-mutation validation
      → recompute the milestone's dependency-ready set → recommend next issue
      → repeat for every issue in the milestone
      → ready set reaches zero
      → Milestone PR readiness: every issue closed + human confirms final manual testing
          done + that testing found nothing further
      → follow-up work found during manual testing?
           ├─ yes → discovered-work intake → new issue, attached to the still-open
           │         milestone → continue milestone, re-run this gate once that issue closes
           └─ no  → report: milestone PR-ready (a report, not a mutation)
                    → human creates, reviews, and merges the milestone-linked PR
                    → human confirms the merge
                    → STOP — one bundled human authorization:
                        "close the milestone and start the release?"
                    → two independent branches, neither gates the other
                         ├── MILESTONE CLOSURE
                         │     → verify eligibility (delivery/phase, zero open issues,
                         │        authorization actually covers closure — all checked fresh)
                         │     → close (no second approval — already authorized above)
                         │     → re-fetch, confirm state is closed
                         └── RELEASE
                               → discover release policy
                               → understand the release, draft notes at release altitude
                               → GATE — human approves exact version/tag target/title/body
                               → publish
                               → re-fetch, validate
```

**Backlog/hotfix ends at the closing recipe.** No PR, no milestone-level gate, no release trigger —
none of the milestone branch's machinery applies to it.

### What each checkpoint actually proves

The diagram names six kinds of checkpoint — two review gates, three verification moments, and one
authorization — that are easy to gloss as interchangeable "checks." They are not: each answers a
different question, against different evidence, and licenses a different transition.

**Gate 1 — implementation review.** *Event:* implementation is reported complete, and the
pre-Gate-1 full-project verification has run — appropriate project-wide formatting/lint/static
checks, and the full regression suite appropriate to the project. *Question it answers:* is the
implementation itself ready to be turned into durable semantic history? *Evidence:* the
verification results and any meaningful unknowns, visible to the human before they answer.
*Transition:* approval authorizes moving on to commit-plan derivation — nothing more. Gate 1 does
not approve commit structure; no commit boundary has even been proposed yet at this point.

**Gate 2 — commit-plan review.** *Event:* a commit plan has been derived from the reviewed diff.
*Question it answers:* is this the right engineering history for the implementation? *Evidence:*
the proposed grouping and order, shown before anything is written — commit boundaries are
engineering decisions in their own right; tests travel with the decision they verify when
appropriate; ordering must keep every intermediate state coherent and must account for
activation/configuration ordering hazards (`rules/verification.md`'s ordering note). *Transition:*
approval authorizes writing the commits. Gate 2 does not re-approve the implementation — that
question was already closed at Gate 1.

**Per-commit verification.** While building the approved commit plan, verify each commit at the
narrowest reliable scope that proves it — a principle that applies across every kind of check the
project's tooling offers, not tests alone: targeted/relevant tests, formatting, linting, static
analysis, and any other project-specific quality check, scoped down wherever the tooling can
reliably do it. Where the tooling has no reliable way to scope a given check, that check falls back
to its broader, project-wide mode for that commit — the target is the narrowest scope that's
actually reliable, not the narrowest scope regardless of whether the tooling can back it.

**Pre-Gate-1 verification vs. completed-issue verification.** These are the diagram's two
full-project verification moments, and they can run the identical command without being duplicates
of each other: pre-Gate-1 proves the complete implementation working tree is ready, before any
commit history exists to review or split; the completed-issue pass proves the final assembled
semantic history — however many commits it became, in whatever order — still reconstructs that same
correct result once the commits actually exist. They are intentionally distinct proofs of two
different objects, a working tree versus a commit history, and skipping either because the other
already ran green loses a real check.

**Isolation verification.** A deliberate escalation, not the default posture for every multi-commit
issue — most issues verify each commit at its own narrowest reliable scope and never reach for this.
It's used specifically when the correctness of an intermediate *committed* state itself needs to be
proven — reconstructed-after-the-fact history, or commit order that's itself load-bearing for
correctness — rather than assumed from how the working tree behaved during implementation. At a high
level, it works by committing a semantic group, temporarily setting aside everything not yet
committed, running the project's full verification against exactly that committed state, then
restoring the rest and repeating for the next commit. The exact mechanics live in
`rules/verification.md`; this dossier only needs the reader to know when and why the escalation
exists, not how to execute it.

**Post-merge authorization.** *Event:* the human confirms the milestone PR merged. *Question it
answers:* should post-merge progression begin at all — for both the milestone-closure branch and
the release branch. *Evidence:* the human's single explicit acceptance, typically phrased as one
bundled question ("close the milestone and start the release?"). *Transition:* it opens two
independent branches at once, neither gating the other — the workflow's home project has typically
closed the milestone first and drafted the release second, but that's a recorded habit, not an
enforced order, and running the two in the opposite order, or interleaved, is equally valid. The
milestone-closure branch then verifies its own eligibility (delivery/phase, zero open issues,
authorization actually covering closure, all checked fresh) and closes without asking a second
time — the bundled authorization already is the approval for closure. The release branch separately
requires its own later approval of the exact release content (version, tag target, title, body),
because that content doesn't exist yet at the moment the bundled authorization is given — a merged
PR, and the authorization itself, approve *proceeding*, not any particular version or wording. There
is no second milestone-closure approval; there is a second, necessarily later, release-content
approval.

## 5. Rule architecture

| Rule | Owns | Consulted | Key dependencies | Explicitly does not own |
|---|---|---|---|---|
| `review-gates.md` | The approval-boundary procedure — Gate 1, Gate 2, and the standing "genuine unknown" escalation. | Once implementation is ready to report (Gate 1); again once a commit plan is ready (Gate 2). | Reports verification results (`verification.md`) and commit-plan content (`commit-boundaries.md`) rather than deciding them. | Verification scope, commit-splitting logic, sequencing choice. |
| `commit-boundaries.md` | Commit-decomposition semantics: the coherence test, the derivation procedure, message content, `Refs #N`, test placement, correction-folding. | While inspecting the diff and building the commit plan, after Gate 1. | `verification.md` for the negative-proof mechanism behind an intentionally inert commit. | Verification execution/scope, the review-gate procedure, issue closure. |
| `verification.md` | Verification scope at each lifecycle boundary (full / narrowest-reliable / isolation-escalation), the regression-baseline model, activation-risk commit ordering. | While implementing, and while building/ordering commits. | Layers activation-safety ordering on top of `commit-boundaries.md`'s dependency ordering. | Commit boundaries, gate reporting. |
| `issue-closure.md` | Whether/when to ask about closing, the four-part closure recipe, post-mutation validation. | After the completed-issue full-suite pass, once commits exist. | `milestone-completion.md`'s "When manual testing finds something" for what a later finding does instead of reopening. | Deciding closure beyond the ask, issue creation, issue reopening. |
| `sequencing.md` | Branch readiness before an issue starts (trunk vs. shared milestone branch); recomputing and reporting the dependency-ready set after a validated closure. | Before implementing an approved issue; again after every validated closure. | Consumes `my-feature-planning`'s milestone classification and dependency representation, never redefines them. | Dependency-graph design, milestone PR-readiness/closure, starting the next issue. |
| `release.md` | The post-merge authorization gate (shared with milestone closure), release-policy discovery, drafting at release altitude, the content-approval gate, publishing, post-publication validation. | Once a PR carrying committed work has merged. | Its step 0 authorization is the same one `milestone-completion.md`'s closure gate consumes. | Issue closure, PR creation/merge, milestone closure, invented deployment/rollback/changelog machinery. |
| `milestone-completion.md` | Milestone PR readiness (a factual gate); the closure gate (eligibility, not a second approval); the closure mutation and its validation; the milestone-PR reference convention. | PR readiness once `sequencing.md` reports an empty ready set; closure once the post-merge authorization has been given. | Consumes `release.md`'s step 0 authorization and `my-feature-planning`'s milestone classification/description. | Milestone scope/naming, PR creation/review/merge, release drafting/publication. |

**Why seven rules, and not more or fewer.** The decomposition tracks genuinely distinct questions —
approval procedure, commit semantics, verification scope, closure, sequencing, release, and milestone
completion — and no two files claim authority over the same question. Every place two rules touch the
same topic divides it by *which question is being asked*, not by *which artifact is touched*:
verification *timing* belongs to `verification.md` alone; test *placement* (which commit) belongs to
`commit-boundaries.md`; commit *ordering* splits cleanly by *reason* (structural dependency vs.
activation safety) rather than being duplicated. No rule's stated boundary claims something another
file actually owns, and no responsibility is claimed by two files at once.

No merge, split, retirement, or move is warranted by current evidence for any of the seven rules.
That conclusion held through the architecture review that first examined it, and through two later
rounds of methodology correction that changed real content inside several rules — including a
substantive change to how milestone closure and release relate to each other (§6) — neither of which
needed a new rule file or a restructured one.

## 6. Human decision model

Eight distinct decision points exist across the lifecycle. None is redundant with another, and none
should be collapsed:

1. **Genuine-unknown escalation** (standing, not a fixed checkpoint) — fires wherever a
   product/architecture decision is missing, evidence contradicts an assumption, or a choice has no
   clearly better answer. Protects against silently resolving something that was never actually
   decided.
2. **Gate 1 — implementation review** — "is the implementation/approach correct," before any commit
   history exists.
3. **Gate 2 — commit-plan review** — "is *this* historical decomposition acceptable," independent of
   Gate 1: the same diff can be split several defensible ways, and approving the implementation does
   not pre-approve any particular split.
4. **Issue-closure ask** — "is this issue done enough to mark closed" — independent of Gates 1/2,
   since commits can be correct and well-split while closure is still legitimately deferred (e.g.
   pending manual QA).
5. **Sequencing choice** (only when genuinely comparable ready issues exist) — "which unit of work
   next," using what the closure just unblocked.
6. **Milestone PR readiness** — not a human approval at all, but a *factual* gate: every issue
   closed, manual testing actually done (confirmed by asking, never inferred), and that testing found
   nothing further. Passing it produces a report ("the branch looks ready"), not a mutation — PR
   creation itself stays entirely human-owned from there.
7. **Post-merge continuation authorization** — one human acceptance, right after the human confirms
   the PR merged, that authorizes *both* the milestone-closure branch and the release branch to
   proceed. This is deliberately singular: a bundled question like "close the milestone and start the
   release?" covers both branches at once, rather than asking the same thing twice in two different
   files.
8. **Release-content approval** — "is this exact version/title/body approved for publication." This
   is a separate, later gate from #7, because the concrete content being approved didn't exist yet at
   authorization time. A merged PR is not this approval, and the post-merge authorization in #7 is
   not this approval either.

The one gate worth calling out explicitly because it changed: **milestone closure is not its own
approval gate.** An earlier draft of this methodology had the closure gate asking for a second,
separate "are you sure you want to close the milestone" approval after #7's authorization had already
been given — a redundant re-ask of the same question. The current rule instead treats #7's
authorization as the approval for closure, and confines the closure gate's own job to verifying that
the authorization actually covers closure and that the milestone is actually eligible (delivery/phase,
zero open issues, checked fresh), then acting. If either check fails, the rule reports what's missing
and stops — it does not ask again unprompted, the same discipline `issue-closure.md` already uses for
a declined close.

## 7. Branch and Git/GitHub model

- **Backlog/hotfix work runs directly on the repository's trunk branch** — never a newly created
  feature branch, and there is no branch *decision* to make for it. Which branch a given repository
  actually treats as trunk is discovered from the repository, not assumed to be a fixed name
  (commonly `main`, sometimes something else). If the checked-out branch isn't trunk when this work
  begins, the mismatch is surfaced to the human — never silently worked around, and never silently
  switched.
- **Milestone work shares exactly one branch** across every issue in the milestone — implementation
  does not get a fresh branch per issue. If the wrong branch is checked out, the rule recommends one
  derived from the milestone's actual nature (its area, or the kind of change it bundles) and asks
  before creating or switching — it never does either silently.
- **Branch naming is derived from what the milestone actually is**, never matched against a fixed
  prefix taxonomy. Illustrative shapes — an area-scoped prefix for a cross-cutting rework, a
  capability-scoped prefix for a new feature — exist to show the reasoning, not as a list to
  pattern-match against. When a milestone's nature doesn't suggest an obvious name, the rule asks
  rather than guesses.
- **A milestone's PR is expected to reference the milestone it integrates** — a confirmed observed
  convention, stated explicitly as a contract this workflow is aware of, not something any rule
  checks or enforces.
- **PR content, creation, review, and merge stay entirely human-owned** throughout. The workflow's
  role stops at reporting when a branch looks ready; picking the mechanism a PR gets created,
  reviewed, and merged with is never this skill's decision.

The throughline: every Git/GitHub behavioral detail this skill states is either a discovered fact
about the specific repository (trunk branch name, release mechanism) or an observed convention from
the project this methodology was extracted from, presented as evidence for the reasoning rather than
a fixed rule to match. Nothing here is a universal Git abstraction invented in the absence of
evidence.

## 8. Issue / milestone / release model

**Why issues close before the milestone's PR merges.** Every issue in a milestone closes
individually, on the shared branch, once its own implementation and verification are done — this is
confirmed and intentional, and can happen well before that branch is ever proposed as a PR. Closure
marks that an issue's own work is verified, not that its commits have reached the trunk branch. The
milestone-level gates exist precisely to confirm the aggregate state of all that already-closed work
later, once it actually does move toward a PR and a release.

**What issue closure actually means.** A committed, verified, human-approved decision that this
issue's scope is done — checked-off tasks, a durable closing comment (summary, verification numbers,
commit SHAs), and post-mutation validation that the close, the comment, and the checkbox state all
actually landed. It says nothing about the milestone the issue belongs to.

**What happens when manual testing discovers new work.** A bug or gap found during a milestone's
final manual-testing pass goes through the same Discovered-work intake `my-feature-planning` already
defines for any unexpected finding — no special case invented here. The result is a **new issue**,
explicitly noting it was found during or after the original (already-closed) issue's work, attached
to the still-open milestone.

**Why the default is a new issue, not reopening the original.** Closing the original issue was
already an explicit, approved decision. A later finding doesn't retroactively undo that decision — it
is new information, not proof the earlier one was wrong. Issue reopening is deliberately unowned by
either skill, which is a coherent state precisely because the default path never needs it: a
manual-testing finding becomes a new issue, referencing the original, every time.

**What milestone PR readiness proves, and doesn't.** It proves the shared branch is a reasonable PR
candidate — every issue closed, manual testing actually done and clean. It doesn't create the PR, and
it doesn't mean a release was cut.

**What milestone closure proves, and doesn't.** It proves a delivery/phase milestone is factually
eligible to close *right now* — not Backlog, zero open issues, and the post-merge authorization
already covers it. It doesn't mean a release for that work has published, or ever will on any
particular timeline — the two branches don't gate each other (§4, §6).

**What release publication proves, and doesn't.** It proves a specific version actually published
correctly, re-fetched and validated field-by-field against what was approved. It doesn't by itself
confirm every issue the milestone needed is closed — a Backlog issue discovered along the way and
filed elsewhere can leave the milestone with open work even after a clean release.

**Why none of those should be conflated.** Each proves something narrower than "the milestone is
done," and the workflow says so explicitly and repeatedly at every boundary: zero open issues ≠
milestone complete; release validated ≠ milestone complete; PR readiness ≠ the milestone is done.
This is a deliberate, repeated pattern — an explicit "does not imply" statement at nearly every
adjacent gate — not incidental repetition.

## 9. Verification model

The ladder, in the order a single issue actually passes through it:

```
implementation complete
  → full-project verification (lint/format/static + full regression suite) — before Gate 1
Gate 1 approved → build semantic commits
  → narrowest reliable verification per commit (tests, formatting, linting, static analysis alike)
  → isolation verification only when an intermediate committed state itself needs its own proof
all commits assembled
  → full regression suite once more, at the completed-issue boundary
```

The two full-suite moments — pre-Gate-1 and completed-issue — are not duplicates of each other even
though they can run the identical command: the first proves the completed working tree as one whole,
before any commit history exists to review or split; the second proves the *final assembled
history* — however many commits it became, in whatever order — reconstructs that same correct result
once the semantic commits actually exist. Skipping either because the other already ran green loses a
real check.

Per-commit verification defaults to the narrowest scope that reliably proves that one commit — across
every check the project's tooling offers, not tests alone — falling back to a broader/project-wide
mode only where the tooling genuinely can't scope narrower. Isolation verification (commit → stash the
rest → verify in isolation → pop → repeat) is a deliberate, expensive escalation reserved for when an
intermediate committed state's own correctness is itself load-bearing — semantic history reconstructed
after the fact, or commit order that's itself required for correctness — never the default for every
multi-commit issue.

**Regression-baseline model.** A project's full-project lint/format/static-analysis output is not
required to already be at zero violations before this workflow can run. Pre-existing, unrelated
violations are tolerated debt; the standard is that *this work* introduces no new failures, not that
the whole project becomes clean because this issue touched it. This applies specifically to
lint/format/static checks — the regression **test** suite is never given this leniency: a test passes
or fails regardless of the codebase's history, so the full-suite signal stays exactly as strict
everywhere it runs. How a given project actually distinguishes "pre-existing" from "newly introduced"
for its own tooling is discovered per project, the same way the tools themselves are — never assumed
in advance.

**Dependency ordering vs. activation ordering — deliberately left unresolved.** Commits are ordered
by structural dependency; activation-safety ordering (don't flip a feature gate before what it
activates is already present) layers on top of that same sequence. No real work has yet produced a
case where the two orderings actually disagree. That's recorded as an observed non-conflict, not a
claim that they never can — and no precedence rule is invented for a conflict that hasn't happened.
Should one actually arise, it's exactly the kind of genuine unresolved decision `review-gates.md`'s
"when to stop and ask" exists to surface, not something to guess at now.

## 10. Cross-skill contracts

| Assumption `my-git-workflow` makes about `my-feature-planning` | Classification | What actually backs it |
|---|---|---|
| An approved, dependency-ready issue is the input; planning's job ends at creation | Genuine contract, bidirectional | Planning states outright that its "responsibility ends at issue creation," matching `my-git-workflow`'s own framing exactly. |
| Milestone classification (Backlog/catch-all vs. delivery/phase) is planning's | Genuine contract, bidirectional | Planning's issue-conventions rule defines the distinction and explicitly names `milestone-completion.md` as the file owning the closure gate built on top of it. |
| Dependency representation (e.g. `Depends on #N`) is planning's | Genuine contract, matched | Planning's own conventions define the syntax; `sequencing.md` only reads and evaluates the resulting graph, never redesigning or inventing one. |
| Milestone scope/description, when one exists, is planning's | Consumed convention | `milestone-completion.md` treats an existing description as the scope contract for judging whether a later finding belongs in the still-open milestone — it doesn't draft, redraft, or reinterpret it. |
| A manual-testing finding's intake is planning's (Discovered-work) | Genuine contract, matched | `milestone-completion.md` hands a finding straight to that intake rather than defining its own investigation process; planning's own stated boundary confirms it owns exactly this. |
| Issue reopening | Deliberately unowned by both | Neither skill claims it. This is coherent, not a gap: the default path for a later finding is always a new issue referencing the original, so reopening is never actually needed in the normal case. |

Four of these are unusually explicit, bidirectional contracts — each skill names the other correctly,
a real strength of this pipeline rather than a coincidence. The one deliberately unowned item
(reopening) stays that way because the workflow's own default behavior makes ownership unnecessary,
not because it was overlooked.

## 11. Empirical evidence behind the current methodology

Some of this skill's rules are direct extractions from repeated real observation; others are
explicit, deliberate decisions the human maintainer made and stated outright, independent of how many
times something had actually been observed. Both are legitimate sources for a rule — the distinction
matters for how confidently a future maintainer should generalize from it. The reader does not need
any of what follows to understand the current skill; it exists to show the methodology isn't
theoretical.

**Grounded in repeated observation:**

- A milestone's shared branch, one per milestone rather than per issue, held across enough real
  milestones — not just one — to confirm as an actual convention rather than a single milestone's
  happenstance.
- Issues closing on the shared branch well before that branch is ever proposed as a PR was observed
  across a full milestone's worth of issues, not inferred from a single case.
- Backlog/hotfix work bypassing branch decisions and PR creation entirely was observed across a run
  of hotfix issues worked directly on the trunk branch.
- The release mechanism (a tag plus a published hosted release) was extracted from inspecting a
  project's actual prior release history, not assumed from a template — including a concrete
  before/after where a first notes draft written at implementation altitude was revised to release
  altitude before approval.

**Grounded in explicit human decision, not repeated observation:**

- The regression-baseline model (pre-existing lint/static debt tolerated, new failures block)
  reflects an explicit clarification of what standard this workflow should hold a project to — not a
  pattern read off historical lint output.
- The milestone-completion lifecycle itself is a deliberate, forward-looking decision: the project
  this methodology came from had, in its actual history, left every milestone open regardless of
  issue count, including ones where every issue was already closed. That history is evidence of a
  *different, unstated* set of assumptions at the time, not a convention this skill preserves. The
  completion lifecycle was added as an explicit forward-looking decision instead: closure requires
  the post-merge authorization and factual eligibility, not just zero open issues, and no existing
  milestone was retroactively closed because the rule now exists.
- The single bundled post-merge authorization (one acceptance covering both milestone closure and
  release, rather than two separate asks) came from an explicit clarification of the actual observed
  conversational pattern — the human proposes both in one question and expects one acceptance to
  cover both — not from counting repeated instances of it happening.

A future maintainer reusing this methodology on a different project should treat the first group as
strong prior evidence worth trusting by default, and the second group as intentional design choices
that may or may not fit a different project's own constraints — the regression-baseline standard in
particular is explicitly framed as a choice about what standard to hold a project to, not an
immutable methodology law.

## 12. Authoring observations

Reusable authoring observations extracted from this skill are consolidated in
`skill-audits/skill-authoring-methodology.md`. This dossier retains only the skill-specific evidence,
architecture, assessment, boundaries, and open questions; §11 above contains the empirical evidence
relevant to this skill.

## 13. Known boundaries and open questions

Genuinely unresolved by current evidence — not carried forward out of habit:

- **PR creation, review, and merge mechanics remain entirely human-owned and unformalized.**
  Title/description conventions, review procedure, and merge strategy (merge commit vs. squash vs.
  rebase) have no rule here; this skill picks up again once the human reports the outcome.
- **Release cadence for Backlog/hotfix work is not yet extracted.** `release.md`'s trigger is the
  milestone-PR-merge path specifically; hotfix work committed directly to trunk with no PR has no
  defined release cadence, because no real evidence exists yet to extract one from.
- **Deployment triggers are outside this skill entirely.** Nothing here invents deployment, rollback,
  or CD-trigger behavior beyond whatever a project's own discovered release mechanism already does.
- **Dependency-order vs. activation-order precedence remains unresolved.** No real work has produced
  a case where the two orderings actually conflict, so no precedence rule exists — deliberately, per
  §9, not as an oversight.
- **A milestone's PR later being rejected or materially revised, after some of its issues already
  closed, is unowned on both sides.** The intentional pre-merge-closure design means those issues are
  already closed by the time such a rejection could happen; neither this skill nor
  `my-feature-planning` currently owns walking that back. This is narrower than it might sound — it
  requires a PR rejection *after* closure, not merely a finding surfacing late (that case is already
  resolved: see §8's "default is a new issue").

Not carried forward as open, because current evidence resolves them: whether pre-existing lint/static
debt should block this workflow (resolved — tolerated, §9); whether a milestone's post-closure/
pre-merge gap was an oversight (resolved — intentional, with a defined default for the ordinary case,
§8); whether milestone closure needs its own separate approval (resolved — no, §6); and an earlier
one-sided assumption that issue reopening belonged to `my-feature-planning` (resolved by softening the
claim rather than assigning explicit ownership to either side, §10).

## 14. Current assessment

**Methodology maturity.** High for the paths with real repeated evidence (milestone branching,
issue-before-PR closure, Backlog/hotfix bypass, release-mechanism discovery); intentionally
provisional for paths still marked as not-yet-designed (PR mechanics, hotfix release cadence,
deployment). The skill is explicit about which is which rather than filling gaps with invented
machinery.

**Architectural coherence.** Strong. Seven rules divide genuinely distinct questions with no
duplicated authority and no rule claiming a boundary another file actually owns. Two rounds of real
methodology correction — including a substantive change to how milestone closure and release relate
to each other — were absorbed entirely inside existing rule files, with no new rule needed and none
split or merged.

**Authoring quality.** Rules read as self-sufficient statements of methodology, evidence-supported
rather than evidence-dependent. Origin-project detail appears only where it demonstrates a rule, not
as required context. Cross-references between files are accurate and current.

**Portability of presentation.** Good. Nearly every operationally significant detail is stated as
"discover this from the project" rather than assumed — release mechanism, trunk-branch naming,
verification tooling, dependency-representation syntax. The remaining project-specific texture
(illustrative branch prefixes, a description of one real release run) is explicitly marked as
illustrative, not policy.

**Remaining risks/unknowns.** The genuinely open items in §13 are narrow and well-scoped, not
structural gaps — none threatens the coherence of the seven-rule architecture, and each is honestly
marked unresolved rather than silently assumed one way or the other.
