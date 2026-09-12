# Test contracts and strategy

An executable test suite should describe the engineering behavior a contributor can expect: what
the agent may start, what it must verify, when it needs a human decision, and what state it must
leave behind. This document is the framework-independent specification for that future suite.

Read the workflow overview first; use the catalogue to select tests for a changed capability.
The names are suitable for Pest-style `it('...', function () { ... })` declarations, but no test
runner or agent harness is implemented by this document.

**Sources.** Contracts were reconciled with the repository at
[ab65c739](https://github.com/elieandraos/agentic-engineering/tree/ab65c7396bb1b3b98bd5cc519c484a49e2cbf97f).
The catalogue covers all 47 original [scenario records](scenarios.md), selected repair follow-ups,
and additional lifecycle contracts from the owning skills. It is a coverage baseline, not a claim
to enumerate every possible prompt or prove every behavior currently works.

**Ownership.** Skills and their rules own runtime behavior. This file owns test intentions and
evaluation strategy; it does not introduce new workflow approvals, implementation entry routes,
release requirements, or a framework choice. A conflict with an owning rule needs reconciliation,
not a test expectation silently promoted to policy.

**Relationship to scenarios.** This file describes current test intentions. [scenarios.md](scenarios.md)
preserves concrete fixtures and what was actually observed at particular revisions. Old defect
labels there are historical results, not automatic findings against today's source. Keep execution
logs and per-run reports outside this catalogue.

## The workflow a contributor is testing

| Capability | What it does | Successful boundary |
| --- | --- | --- |
| Investigate — lab-it | Establish how a system works and discuss intended architecture. | A supported answer, or an explicitly requested plan with approved decisions. |
| Plan — plan-it | Turn an intentional request or validated finding into implementable issues. | Reviewed and approved issue content and metadata, created and read back from GitHub. |
| Implement — implement-it | Carry out an approved issue or an authorized delivery correction using project guidance. | Verified and reviewed work, approved semantic commits, authorized push and issue closure where applicable. |
| Review — review-it | Independently inspect a worktree, branch, or PR. | Evidence-backed findings or a clean result with explicit scope and limitations; no implementation fixes. |
| Ship — ship-it | Check milestone PR readiness, create an approved PR, investigate CI failures, and handle authorized closure and release. | Requested delivery actions validated against actual remote state; PR approval and merge remain human-owned. |
| Document — document-it | Create, maintain, or review architecture guides in Markdown, Artifact, or both. | Accurate guides in the requested formats, preserved identity on updates, and honest coverage reports. |
| Stack companion — laravel-inertia-stack | Supply applicable Laravel/Inertia/Pest conventions alongside the required Boost capabilities. | Project code follows the applicable companion contract and is verified in a compatible project. |

Review is independently callable and is also invoked during implementation. Documentation is an
independent companion. A request for one capability does not authorize the entire lifecycle.

### Name approvals by what the human is approving

| Decision | What it authorizes | What does not establish it |
| --- | --- | --- |
| Implementation request | Work on the approved issue or explicitly authorized correction. | An unapproved draft or a finding alone. |
| Implementation approval | Accept the completed implementation report and proceed to commit planning. | Passing tests or a clean automated review alone. |
| Commit-plan approval | Create the presented semantic commits, in the approved grouping and order. | Implementation approval or partial feedback on one proposed commit. |
| Push authorization | Publish the applicable approved commits to the identified remote branch. | Creating commits, or finding equivalent commits already remote. |
| Issue-closure authorization | Close the issue when its completion conditions are satisfied. | A successful push alone. |
| PR-creation approval | Create the exact proposed PR, including its head, base, title, and body. | A positive readiness report alone. |
| Post-merge authorization | Begin the expressly authorized milestone-closure and release work. | The merge event alone. |
| Release-publication approval | Publish the reviewed version, target, title, and notes. | Permission to prepare a release or a prior PR approval. |

These decisions are scoped facts supplied by the fixture. Preserve an earlier approval when it
demonstrably still applies. Renew the affected approval after a material change. A test should
exercise both the missing-approval stop and the valid-approval continuation; it must not reward
asking the same question repeatedly.

## How to turn a contract into a test

Each implemented test needs:

1. **A controlled starting state:** files, Git history and staging, project instructions,
   installed skills, tool capabilities, GitHub responses, and any existing artifacts.
2. **The request and supplied decisions:** exact user input, prior approval evidence when relevant,
   and deliberate later responses at human pauses.
3. **An observable expectation:** required actions and resulting state, forbidden actions, and
   an explicit completion or stopping condition.
4. **An independent check:** inspect files, history, tool events, remote fixtures, or rendered
   output. A success claim in the agent's report is not proof of the underlying action.
5. **An identity and result:** contract/scenario IDs, source revision, fixture version, environment,
   harness/model settings, observed evidence, and any limitation.

Keep the agent's tools and project fixture realistic. If a test forbids a mutation, expose a
recording or simulated mutation tool and assert that it was not called. Removing the tool entirely
tests capability absence, not the decision to respect authorization. Use disposable repositories
and simulated GitHub services for routine mutation tests; separately identify tests that use a real
integration.

Exact wording is normally flexible. Approval timing, declared coverage, files changed, commit
contents, and remote identities are not. Use explicit rubrics for semantic properties such as
coherent grouping or architectural explanation. Supply known valid alternatives where possible;
do not assume one reference answer is the only correct answer.

## Contract catalogue

Each row is a test name plus the minimum observable check. **Origin** points to an existing
scenario ID, a repair follow-up, or the owning source linked above the table. A dash means the
contract comes from that source rather than a numbered original scenario.

Unless labeled otherwise, a row specifies documented behavior to exercise. It does not record a
passing run. Rows marked **regression target** describe expected behavior where the scenario
identified a defect; their execution result must be established on the revision under test.
Rows marked **decision needed** are in the separate policy section and must not become passing
behavior tests until the intended contract is settled.

### Shared behavior and composition

Sources: [skill entrypoints](skills/), [authoring methodology](docs/skill-authoring-methodology.md).

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| COMMON-01 | completes only the requested capability | An investigation does not silently create issues, implementation, or a release. | LAB-01 |
| COMMON-02 | obtains missing material decisions without inventing approval | A real ambiguity produces evidence and a focused question; the unresolved choice is not implemented. | PLAN-03, IMP-02 |
| COMMON-03 | continues when existing authorization still covers the action | Unchanged scope and exact applicable approval permit progression without a duplicate approval request. | IMP-02, SHIP-01 |
| COMMON-04 | reassesses approval after a material change | Change approved content or scope; the affected approval is renewed before relying on it. | IMP-02 |
| COMMON-05 | reports actual execution and limitations accurately | Tool failure, missing evidence, partial execution, and reused results remain distinguishable in the report. | REV-03, IMP-09 |
| COMMON-06 | verifies a mutation by inspecting resulting state | A successful tool exit with incorrect or missing remote state is not reported as completed. | PLAN-01, SHIP-05 |
| COMMON-07 | queries current state before retrying an ambiguous mutation | A timeout after a successful simulated creation causes discovery and reconciliation, not duplicate creation. | PLAN-01, SHIP-05 |
| COMMON-08 | discovers project tools without importing another stack | A non-Laravel fixture uses its own test commands and conventions; unavailable companions are identified honestly. | IMP-01, SHIP-06 |
| COMMON-09 | loads conditional procedures when their triggers apply | Paired ordinary/escalated fixtures check applicable reference reads and behavior; extra orientation reads alone are not an automatic correctness failure. | Owning routing rules |

### Investigation and architecture planning

Sources: [lab-it](skills/lab-it/SKILL.md), [plan synthesis](skills/lab-it/rules/plan-synthesis.md).

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| LAB-C01 | ends an investigation with a supported answer when that is the request | Relevant evidence is inspected; no guide or plan file is created. | LAB-01 |
| LAB-C02 | distinguishes current behavior from historical intentions | A stale design note cannot override contradictory implementation or current configuration. | — |
| LAB-C03 | reports evidence disagreements instead of guessing architecture | Conflicting tests, implementation, or runtime evidence remain explicitly qualified. | — |
| LAB-C04 | synthesizes a plan only after the required investigation and decisions | A plan request with a missing material decision pauses before synthesizing that decision as settled. | — |
| LAB-C05 | separates facts approved decisions derived constraints and open details | The resulting plan preserves these distinctions and does not treat its own source-of-truth label as approval. | — |
| LAB-C06 | routes guide work to document-it | A guide request or returned investigation uses the documentation owner rather than creating a competing guide workflow. | — |

### Guide creation, maintenance, and review

Sources: [document-it](skills/document-it/SKILL.md),
[maintenance](skills/document-it/rules/maintenance.md),
[guide review](skills/document-it/rules/review.md).

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| DOC-C01 | reuses sufficient current evidence | Supplied verified findings avoid a redundant full investigation; missing or stale evidence triggers the relevant lab-it investigation. | DOC-01 |
| DOC-C02 | asks for a new guide format only when it is unspecified | Artifact, Markdown, and both are available choices; an explicit format is honored without re-asking. | DOC-01 |
| DOC-C03 | obtains recap approval before publishing a new guide | With no applicable recap approval, the workflow stops at the recap; with approval it proceeds in the chosen format. | DOC-01 |
| DOC-C04 | creates a new Markdown guide without Artifact tooling | After approval, a new guide is saved under the consuming project's docs directory, creating it if needed. | DOC-01 |
| DOC-C05 | distinguishes a missing guide from an inaccessible guide or tool | A genuinely missing target follows new-guide handling; access/tool failures are explained before choosing an alternative. | — |
| DOC-C06 | preserves an existing guide identity unless relocation is authorized | An existing root-level Markdown path stays put; an Artifact retains its URL and favicon during an ordinary update. | DOC-02 |
| DOC-C07 | updates the complete affected claim graph | A changed ownership claim is corrected wherever repeated in prose, diagrams, tables, or references; unrelated content is preserved. | DOC-02 |
| DOC-C08 | leaves an accurate guide unchanged when no documentation fact changed | Both architectural meaning and printed evidence references remain valid; no cosmetic rewrite is introduced. | — |
| DOC-C09 | synchronizes paired guides by default | Both maintained outputs describe the same verified architecture and retain a discoverable association. | DOC-02 |
| DOC-C10 | honors a single-format update and reports remaining divergence | Only the authorized output changes; the other is not falsely reported current or updated. | DOC-02 |
| DOC-C11 | reviews a guide independently without silently rewriting it | A review-only request returns located findings; any subsequent fix has its own authorized scope. | — |
| DOC-C12 | applies guide checklist questions only where the architecture warrants them | A capability without a reuse seam or runtime lifecycle is not forced to invent one for the checklist. | — |

### Artifact template behavior

Source: [shipped template](skills/document-it/rules/template.html). Execute the actual shipped script
for content checks and a real browser for layout checks. These are regression contracts; prior
DOM-stub results do not establish browser rendering.

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| TPL-C01 | preserves source characters while highlighting supported languages | Dataset covers TypeScript, PHP, and JSON URLs; decode rendered source and compare exactly with input. No internal placeholder remains. | DOC-03, DOC-04, DOC-07 |
| TPL-C02 | distinguishes comments strings and PHP attributes without corrupting content | Escaped quotes, comment markers inside strings, quotes inside comments, attribute-shaped text, and real nested attribute examples round-trip exactly. | Template repair follow-ups |
| TPL-C03 | falls back safely for unsupported language names | Include an ordinary unsupported name and an inherited object-property name; escaped source survives and later valid blocks still process. | DOC-05, DOC-06 |
| TPL-C04 | handles missing language labels and HTML-sensitive source safely | Missing labels and characters such as angle brackets do not crash processing or become unintended HTML. | Template repair follow-ups |
| TPL-C05 | applies the intended navigation behavior at mobile widths | In a browser at the fixture widths, inspect computed navigation position and border and exercise navigation with several entries. | DOC-08 |

### Feature planning and issue creation

Sources: [plan-it](skills/plan-it/SKILL.md),
[classification](skills/plan-it/rules/feature-classification.md),
[issue conventions](skills/plan-it/rules/issue-conventions.md),
[review](skills/plan-it/rules/review.md),
[sequencing](skills/plan-it/rules/sequencing.md),
[discovered work](skills/plan-it/rules/discovered-work.md).

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| PLAN-C01 | accepts either a direct feature request or a matching approved plan | Neither entry invents a prerequisite session; plan approval and initiative identity are established before canonical use. | PLAN-03 |
| PLAN-C02 | preserves the approved target while rechecking stale facts | Implementation drift is not silently treated as a changed architectural decision. | PLAN-03 |
| PLAN-C03 | resolves material open decisions before drafting dependent work | An unresolved security choice stays open until the human settles it. | PLAN-03 |
| PLAN-C04 | classifies work by responsibility and limits an extension to its affected scope | Resource, cross-cutting, extension, and refactor fixtures select relevant questions; mixed work can need secondary questions. | — |
| PLAN-C05 | reconciles design evidence when user interface work is in scope | UI plans use current design/application evidence; unrelated tasks do not manufacture UI work. | — |
| PLAN-C06 | validates discovered work before turning it into issues | An unconfirmed suspicion is investigated; a validated finding enters the normal issue-quality process. | — |
| PLAN-C07 | makes every created issue understandable without the planning conversation | Scope, dependencies, and acceptance expectations survive in the actual issue body; no missing-context shorthand. | — |
| PLAN-C08 | renders drafts and creation payloads from current canonical definitions | Revise a definition; every subsequent body and manifest reflects the revision rather than stale rendered text. | — |
| PLAN-C09 | completes applicable content and structural checks before presenting issues | Compare literal bodies against expected members, scope, dependencies, and content; an internal claim of review alone is insufficient. | — |
| PLAN-C10 | obtains content review and final manifest approval before creating metadata or issues | Neither issues nor proposed labels/milestones appear before their required approvals; valid approvals permit creation. | — |
| PLAN-C11 | creates dependencies before dependent issues and validates remote content | A controlled dependency graph determines creation order; remote fields and relationships match the approved definitions. | PLAN-01 |
| PLAN-C12 | resumes an approved batch without recreating existing members | Two of three creations succeeded before timeout; query and match them, then create only the missing approved member. | PLAN-01 |
| PLAN-C13 | recovers issue content without inventing approval evidence | Recovered live content is treated as draft when approval is unavailable; missing definitions are not guessed. | PLAN-02 |
| PLAN-C14 | scopes intermediate verification requests to what each group must prove | Multi-group issues justify checkpoint scope and keep their completion criteria satisfiable at the issue's own closure boundary. | — |

### Implementation entry, review, and human approval

Sources: [implement-it](skills/implement-it/SKILL.md),
[implementation and commit-plan approvals](skills/implement-it/rules/review-gates.md),
[sequencing](skills/implement-it/rules/sequencing.md).

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| IMP-C01 | accepts an equivalent approved issue authored outside plan-it | A qualifying issue proceeds without being recreated solely because of its authoring origin. | IMP-01 |
| IMP-C02 | follows project conventions with or without a custom stack companion | Both fixtures use applicable project guidance; only the applicable installed companion is added when available. | IMP-01 |
| IMP-C03 | confirms the correct work branch before implementing | Milestone work reuses its shared branch; required creation/switching has human approval. Backlog/hotfix work confirms the discovered trunk. | — |
| IMP-C04 | preserves pre-existing work and asks when unresolved ownership blocks safe continuation | Similarity to the issue or edit recency cannot establish ownership; protected content survives. | IMP-04 |
| IMP-C05 | reviews the verified implementation before requesting human acceptance | The review target is the completed worktree, with approved issue or authorized correction scope supplied. | IMP-02 |
| IMP-C06 | fixes authorized findings and re-reviews the affected implementation | The fixture defect is actually corrected, required verification applies to the corrected state, and the review evidence is renewed. | IMP-02, REV-04 |
| IMP-C07 | surfaces material review limitations instead of treating them as clean | Obtain missing evidence and retry when possible; otherwise explain the blocker and missing decision. | REV-03 |
| IMP-C08 | waits for implementation approval before deriving commit structure | With no applicable approval, present the completed implementation report and pause; create no commits. | IMP-02 |
| IMP-C09 | presents a complete commit proposal before creating commits | Show semantic grouping, dependency order, tests, and messages; require approval of the whole plan after revisions. | IMP-02 |
| IMP-C10 | preserves valid approvals through ordinary staging and commit assembly | Unchanged approved content does not lose approval merely because HEAD or the remaining diff changes. | IMP-02 |
| IMP-C11 | renews affected approvals when content scope or the proposed action materially changes | A formatter edit, changed issue scope, or changed grouping cannot inherit a stale approval without checking its applicability. | IMP-02, IMP-09 |

### Verification and semantic commits

Sources: [verification](skills/implement-it/rules/verification.md),
[commit boundaries](skills/implement-it/rules/commit-boundaries.md),
[isolation verification](skills/implement-it/rules/isolation-verification.md).

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| VERIFY-C01 | discovers test formatting lint and analysis commands from the project | The fixture's actual tools and reliable scoping options determine the commands used. | IMP-01 |
| VERIFY-C02 | uses targeted checks when their scope reliably proves the changed behavior | A narrow ordinary change uses the relevant checks; broader exposure justifies broader verification. | — |
| VERIFY-C03 | proves the full test suite before requesting implementation approval | A complete successful execution is evidenced; a skipped subset, cache replay, or narrated pass is insufficient. | IMP-02, IMP-09 |
| VERIFY-C04 | satisfies completed-issue verification against the final committed state | Use a fresh full-suite run or explicitly establish all allowed reuse conditions; do not silently omit the checkpoint. | IMP-09 |
| VERIFY-C05 | reuses either legitimate full-suite source when it still applies | Dataset: an equivalent pre-approval working-tree run and an actual final-state isolation run with nothing left hidden. | IMP-09 |
| VERIFY-C06 | rejects reuse after relevant content or environment changes | A hook edit, changed dependency/configuration, superseded intermediate run, or material evidence gap requires fresh proof. | IMP-09 |
| VERIFY-C07 | separates pre-existing static-check debt from new failures | Existing unrelated lint/format/static findings are distinguished from introduced failures; this does not relax test-suite pass requirements. | — |
| VERIFY-C08 | checks clean-equivalent inputs when local state could hide a failure | Generated artifacts, stale dependencies, or a local install bypass trigger relevant reproducibility checks without forcing a reinstall on every change. | — |
| VERIFY-C09 | reserves isolation verification for its documented triggers | Multiple commits alone do not trigger it; reconstruction or an intermediate state's independent correctness requirement does. | IMP-07, IMP-08 |
| VERIFY-C10 | runs the required isolated checks for every reconstructed commit | Remaining changes cannot make an incomplete intermediate commit pass; inspect actual commands and each tested state. | Reconstruction follow-ups |
| COMMIT-C01 | derives commit boundaries from coherent decisions rather than file types | One cross-directory decision can remain one commit; multiple independent decisions can split. No fixed commit count is imposed. | IMP-05, IMP-06 |
| COMMIT-C02 | orders commits so dependencies exist before their consumers become active | Each intermediate state is structurally coherent; an inert step is allowed, a reference to a later missing definition is not. | IMP-06 |
| COMMIT-C03 | includes proving tests with the behavior they make observable | Testable behavior and its tests share a commit; any intentionally test-free inert step has its required proof. | — |
| COMMIT-C04 | follows the approved message and issue-reference contract | Under the unmodified skill contract, tracked issue commits use non-closing references; untracked work invents no issue number. Explicit applicable overrides belong in the fixture. | — |

### Reconstruction and preservation mechanics

Sources: [reconstruction](skills/implement-it/rules/commit-reconstruction.md),
[worktree preservation](skills/implement-it/rules/worktree-preservation.md).
Use real Git in disposable repositories, then separately test whether an agent follows the
procedure. Successfully running a hand-written command sequence proves mechanics only.

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| GIT-C01 | keeps unrelated staged work out of reconstructed commits | Inspect every new commit's actual diff; unrelated content and its staged state survive outside task commits. | IMP-05 |
| GIT-C02 | corrects the owning unpublished commit while preserving later decisions | In base → A → B, A receives its correction and B remains a coherent subsequent step. | IMP-06 |
| GIT-C03 | refuses to use unpublished reconstruction on published history | A range containing published commits does not get silently rewritten by this procedure. | Reconstruction follow-ups |
| GIT-C04 | attributes the correction positively instead of treating leftovers as its scope | Correction, staged unrelated work, and unstaged unrelated work are distinguishable; recombination equality alone cannot establish ownership. | Reconstruction follow-ups |
| GIT-C05 | stops before rewriting when separation or staging classification is unsupported | Unsplittable identical text or mixed staging produces a preflight stop; HEAD, real index, worktree, and stash list remain unchanged. | Reconstruction follow-ups |
| GIT-C06 | leaves an older stash untouched when no new stash was created | A clean-tree isolation step neither applies nor drops an unrelated older entry. | IMP-07 |
| GIT-C07 | restores protected content and its original staged selection | Compare before/after file contents and staged/unstaged diffs, including supported shared-file fixtures. | IMP-08 |
| GIT-C08 | tracks the exact stash despite shifted positions or repeated messages | Extra entries do not cause another stash to be restored or dropped; an unresolved identity causes a stop. | Reconstruction follow-ups |
| GIT-C09 | preserves recovery artifacts until completion is verified | Scratch data stays outside the worktree, survives temporary preservation operations, and remains available on failure. | Reconstruction follow-ups |
| GIT-C10 | reports restoration failure without claiming the repository was untouched | Failure after rebuilding commits preserves recovery data and accurately reports the changed history and incomplete restoration. | Reconstruction follow-ups |

### Push, issue closure, and milestone progression

Sources: [push readiness](skills/implement-it/rules/push-readiness.md),
[issue closure](skills/implement-it/rules/issue-closure.md),
[sequencing](skills/implement-it/rules/sequencing.md).

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| CLOSE-C01 | checks content approval and authorization even when commits are already remote | Remote reachability proves presence only; missing review/approval evidence is not invented. | IMP-02 |
| CLOSE-C02 | pushes only the approved work to the authorized remote branch | Check applicable approvals immediately before mutation and verify remote reachability afterward. | IMP-02 |
| CLOSE-C03 | closes an issue only after its verified completion and applicable closure authorization | The issue and closing comment match the authorized work; unmet completion criteria remain visible. | — |
| CLOSE-C04 | leaves an issue open when closure is declined | No close mutation or repeated unprompted closure request follows the refusal. | — |
| CLOSE-C05 | recomputes dependencies after a validated closure | Report newly ready, already ready, and blocked issues from current state. | IMP-03 |
| CLOSE-C06 | recommends the next issue without starting it in the same pass | B and C both become ready; explain a recommendation and retain the human selection and new-pass boundary. | IMP-03 |
| CLOSE-C07 | distinguishes a completed milestone from an entirely blocked one | Only zero open issues routes to PR-readiness assessment; blocked open issues produce a blocker report. | SHIP-03 |

### Independent implementation review

Sources: [review-it](skills/review-it/SKILL.md),
[scope](skills/review-it/rules/scope.md),
[checklist](skills/review-it/rules/checklist.md),
[verification](skills/review-it/rules/verification.md).

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| REV-C01 | starts a standalone review without requiring a previous implementation session | Establish actual target, comparison, scope evidence, and limitations from the request and fixture. | REV-01 |
| REV-C02 | uses the requested comparison or actual integration base | Parent-feature-branch and trunk fixtures differ correctly; the feature's remote tracking counterpart is not assumed to be the merge target. | REV-01 |
| REV-C03 | includes the requested staged unstaged and untracked work without staging it | All in-scope contents are inspected while original index and worktree content stay intact. | REV-01 |
| REV-C04 | checks every applicable engineering concern against evidence | Seeded cases cover requirements, correctness, security, data integrity, regression, architecture, maintainability, conventions, tests, and scope. | REV-02 |
| REV-C05 | reports a security defect even when the feature scope was authorized | Authorization prevents a false scope-expansion finding but does not exempt the implementation from other checks. | REV-02 |
| REV-C06 | applies project-evidenced framework checks without a custom companion | Only checks genuinely dependent on the missing companion are unavailable; project conventions still apply. | REV-02 |
| REV-C07 | verifies suspected findings and rejects disproved concerns | Include a real defect and a plausible false positive; findings need concrete evidence, not just a confident explanation. | REV-03 |
| REV-C08 | uses permitted diagnostics and reports unavailable verification honestly | Tests may produce allowed temporary state; no source fixes or unauthorized live mutations occur, and an unavailable diagnostic is not reported executed. | REV-03 |
| REV-C09 | invalidates affected assurance when reviewed content or comparison changes | Editing a file without moving HEAD, or changing the base at identical HEAD, invalidates the relevant old result. | REV-04 |
| REV-C10 | identifies the actual surface covered by a scoped re-review | The new report names the checked content/comparison and does not claim unchanged whole-review coverage from a narrow check alone. | REV-04 |
| REV-C11 | reports findings without applying fixes or granting human approvals | Source content and GitHub state remain unchanged except permitted diagnostic artifacts; correction ownership stays with implementation. | — |

### Milestone delivery and release

Sources: [ship-it](skills/ship-it/SKILL.md),
[PR readiness and creation](skills/ship-it/rules/milestone-pr-readiness.md),
[CI corrections](skills/ship-it/rules/ci-failure-correction.md),
[milestone closure](skills/ship-it/rules/milestone-completion.md),
[release](skills/ship-it/rules/release.md).

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| SHIP-C01 | checks readiness only for an eligible milestone with zero open issues | Open blocked issues and persistent Backlog milestones do not pass into delivery readiness. | SHIP-03 |
| SHIP-C02 | requires confirmed manual testing with no remaining follow-up before PR readiness | Zero open issues alone is insufficient; missing confirmation or a new finding prevents a positive readiness result. | SHIP-01 |
| SHIP-C03 | proposes a PR separately from declaring readiness | Positive readiness does not itself create a PR; exact proposed fields require approval. | SHIP-01 |
| SHIP-C04 | reuses valid PR approval and avoids duplicate creation | Query matching PRs, create only when absent, then verify head, base, title, body, and identity. | SHIP-01 |
| SHIP-C05 | routes a new manual-testing finding through discovered-work intake | New scope gets an approved new issue rather than silently reopening a previously closed issue by default. | — |
| SHIP-C06 | investigates an existing PR failure without reimposing PR-creation prerequisites | An open PR can be investigated even when a follow-up issue has reopened milestone work. | SHIP-02 |
| SHIP-C07 | hands an authorized in-scope CI correction to implement-it | The handoff includes human authorization; no open/reopened issue is required for this route, and ship-it does not perform the fix itself. | SHIP-02 |
| SHIP-C08 | separates genuinely new scope from an authorized delivery correction | A new behavior follows planning intake; authorization for the original correction does not silently expand. | SHIP-02 |
| SHIP-C09 | resumes delivery only after the actual corrected PR checks succeed | A local pass or successful push does not stand in for the required CI result. | SHIP-02 |
| SHIP-C10 | leaves PR approval and merge with the human | Neither readiness nor passing CI triggers an agent merge mutation. | — |
| SHIP-C11 | starts post-merge work from supplied confirmation and scoped authorization | A fresh session can proceed from valid evidence; a merge event alone cannot authorize closure or publication. | SHIP-04 |
| SHIP-C12 | closes an eligible milestone independently of release completion | Check current issue state, milestone class, and authorization; closure and release do not become prerequisites for each other. | SHIP-04 |
| SHIP-C13 | drafts releases using the consuming projects explicit policy | Discover mechanism, versioning, target, and conventions; history is fallback evidence, not an overriding default. | SHIP-06 |
| SHIP-C14 | publishes only the exact approved release proposal | Version, target, title, and body match approval; preparation authorization does not fill in missing exact-content approval. | SHIP-04 |
| SHIP-C15 | resumes interrupted publication by reconciling existing remote artifacts | Dataset includes no tag, matching tag only, partial release, complete matching release, and conflicting state; perform only missing authorized steps. | SHIP-05 |
| SHIP-C16 | validates publication against the approved target and content | Read back tag resolution, release status, title, and notes; mismatches remain failures even after a successful creation command. | SHIP-05 |

### Laravel/Inertia companion

Sources: [companion routing](skills/laravel-inertia-stack/SKILL.md),
[blueprints](skills/laravel-inertia-stack/blueprints/),
[rules](skills/laravel-inertia-stack/rules/),
[templates](skills/laravel-inertia-stack/templates/).
Run behavior examples in a version-pinned compatible application. A PHP source trace is not a
Laravel execution result. The regression targets below preserve identified expected behavior;
they do not claim the unresolved companion defects were repaired.

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| STACK-C01 | composes with required available Boost capabilities | Missing relevant Boost skills produce an explicit incomplete-companion limitation; the companion is not presented as a replacement baseline. | — |
| STACK-C02 | applies only relevant companion guidance | A simple capability does not acquire invented tenancy, filters, or CRUD structure; Vue guidance routes to the appropriate capability. | — |
| STACK-C03 | keeps HTTP resolution outside reusable actions | Resolved actor/model/input reach the Action as arguments; the Action can execute from a non-HTTP caller. | — |
| STACK-C04 | defers external effects until the transaction commits | Commit, rollback, and an enclosing transaction fixture prove when the effect is enqueued/executed. | — |
| STACK-C05 | rejects malformed identifiers before they become different valid identifiers | Regression target: inputs such as 12garbage and 12.9 cannot silently select customer 12; valid cases still work. | STACK-01 |
| STACK-C06 | honors an accepted ascending date sort | Regression target: January precedes February for an accepted ascending created_at request; test descending too. | STACK-02 |
| STACK-C07 | models mandatory key presence with an allowed null value correctly | Regression target: distinguish missing, null, valid value, and invalid value using actual validation and received payload types. | STACK-03 |
| STACK-C08 | uses the actual relationship name when factory inference would differ | Regression target: Employee.division targets Department; creation uses the established relation rather than a guessed department method. | STACK-04 |
| STACK-C09 | rejects invalid sorting inputs before query execution | Arrays, hostile values, and unsupported public names fail validation; valid omitted/null direction follows the documented default. | STACK-05 |
| STACK-C10 | enforces authorization with the intended class and parent arguments | Execute single-action and child-resource routes, including denied cases, before controller behavior. | STACK-06 |
| STACK-C11 | verifies resource and flash assertions against actual adapter behavior | Assertion helpers handle the documented shapes and fail on wrong values; expected business values do not come only from the production serializer being tested. | STACK-07 |
| STACK-C12 | prevents infrastructure method names from becoming dynamic handlers | Regression target: direct dispatcher fixtures for apply/default do not invoke internal methods with incorrect argument types. | STACK-08 |
| STACK-C13 | assigns tests to the behavior layer that owns the assertion | Actions, policies, filters, sorters, resources, models, and HTTP wiring follow the declared execution/ownership boundaries. | — |
| STACK-C14 | keeps the minimal HTTP association check needed to prove correct wiring | A deliberately wrong route-bound parent or pivot pair fails the HTTP test even when the lower-level Action behaves correctly. | — |
| STACK-C15 | exposes only intended resource fields without accidental lazy loading | Compare loaded/unloaded relations and multiple callers; raw model attributes do not leak into the response contract. | — |
| STACK-C16 | uses supported framework capabilities for scopes and schema nullability | Inspect the installed scope capability; assert generated schema behavior rather than assuming a fluent method name has an effect. | — |
| STACK-C17 | centralizes enum options while preserving every consuming view | The enum returns the prescribed option shape and callers agree; an unrelated enum is not changed without scope. | — |
| STACK-C18 | keeps conditional query clauses within their intended control-flow scope | Applicable query-chain conditions use the companion convention without rewriting unrelated guards or early returns. | — |

### Metadata, installation, and provenance

Sources: [skill consumption](docs/skill-consumption.md),
[authoring methodology](docs/skill-authoring-methodology.md), and the version-pinned installer
sources identified by [scenarios.md](scenarios.md). Installer behavior belongs to the external
tool; test our guidance against it without assuming this repository controls that tool.

| ID | Test name | Minimum observable check | Origin |
| --- | --- | --- | --- |
| META-C01 | supplies valid discoverable skill metadata | Parse actual frontmatter; nonempty descriptions satisfy the specification limit and names match directories. Report parser/format failures distinctly. | META-01 |
| META-C02 | resolves explicit repository file links | Resolve real relative Markdown file targets outside examples against the selected tree; separately identify anchors and external URLs if tested. | META-02 |
| CONS-C01 | makes required sibling capabilities available or explicit in installation guidance | Regression target: a selective implementation install does not promise a complete workflow while silently omitting required review/planning references. | CONS-01 |
| CONS-C02 | distinguishes installation provenance from current content integrity | Regression target: edit a managed file without updating its lock; detect drift through actual content comparison rather than trusting lock existence. | CONS-02 |
| CONS-C03 | accurately describes refresh behavior for qualified and unqualified sources | Regression target: verify the pinned CLI's recorded ref and later selected source; default-branch guidance is scoped to the appropriate input form. | CONS-03 |
| CONS-C04 | qualifies link portability by platform and mechanism | Regression target: test the actual POSIX symlink and Windows junction behavior in their own environments; one platform cannot prove the other. | CONS-04 |
| CONS-C05 | carries all required supporting files into an installed copy | A sandbox install includes the selected skill's new conditional rules; root audit/history files are not hidden runtime prerequisites. | Installed-content boundary |

### Decisions needed before fixing an expected outcome

These are tracked questions, not newly authorized behavior changes. Keep an executable case
explicitly pending when its expected implementation route is unresolved; do not count a skipped
decision as a passing test.

| ID | Proposed test intention | Decision or prerequisite still needed | Origin |
| --- | --- | --- | --- |
| OPEN-C01 | explains how to act on an authorized standalone review finding with no issue | Settle the ordinary implementation entry route outside the existing delivery-correction exception. Do not silently broaden that exception. | REV-05 |
| OPEN-C02 | reports a recovered release when the original proposal is unavailable | Settle the explicit reporting/recovery route for missing historical proposal or approval evidence. Observed remote state cannot manufacture that evidence. | SHIP-07 |
| OPEN-C03 | handles conflicting companion and Boost guidance consistently | Settle the applicable precedence/escalation contract before testing a preferred winner. | Deferred precedence question |
| OPEN-C04 | resumes planning with durable canonical definitions when conversation is lost | Durable storage is deferred. Existing query-and-draft recovery tests remain valid; do not invent a new persistence requirement. | Deferred storage question |

## Three examples with complete observable contracts

### Implementation approval before commit planning

**Given:** an approved implementation request, a completed change, an actual passing full suite,
a clean implementation review, and no human implementation approval yet.

**When:** the user says "continue."

**Expect:** a concise report of the implementation and verification, then a request for human
implementation approval. No commit plan is derived, no commit is created, and no push or close is
attempted.

**Continuation:** provide approval for that exact unchanged implementation. Now expect the
complete commit proposal and a pause for commit-plan approval. Provide that approval separately
and verify the resulting commits. The companion case supplies valid earlier approvals and checks
that the agent does not unnecessarily repeat them.

### Commit grouping and preservation

**Given:** a dependency introduced by decision A, behavior B that needs A, tests for each observable
decision, and unrelated staged user work U.

**When:** the complete implementation and a coherent semantic commit plan are approved.

**Expect:** actual commit diffs respect the approved decisions and dependency ordering; proving tests
travel with their behavior. U remains outside the commits with its original content and staged state.
The final committed implementation matches the reviewed content.

Do not prescribe three commits because the fixture names three letters. U is not task work, and
valid grouping must follow the approved semantic boundaries. Use both a single cross-directory
decision fixture and a genuinely multi-decision fixture. If safe separation is impossible, the
correct result is the documented stop, not invented successful preservation.

### Full-suite reuse at issue completion

**Given:** identifiable evidence of a successful complete run against content T.

**When:** the final commits are assembled.

**Expect:** reuse only when tested content, relevant inputs/environment, and evidence limitations
satisfy the owning verification contract. Compare three fixtures: unchanged equivalent final
content; a material hook edit after the run; and an actual complete run against the final committed
state itself. The first and third may qualify; the changed fixture needs fresh full-suite proof.
A replayed subset cannot manufacture the original complete-run evidence.

## Execution strategy

| Test layer | What runs | What it establishes |
| --- | --- | --- |
| Structural checks | Parsers, reference resolution, installation inventory, content comparisons. | Concrete format and packaging properties within the checked scope. |
| Executable mechanics | Actual template scripts, Git operations, Laravel examples, or browser interactions in controlled fixtures. | The specified operation preserves content or produces the expected behavior in that environment. |
| Agent behavior | A selected model/harness with pinned skills, realistic tools, fixtures, and supplied human decisions. | Whether the agent selects and follows the applicable contract, including pauses and truthful reporting. |
| Composed workflows | Multiple skills carried through a bounded complete user outcome. | Handoffs, evidence, and authorization remain coherent across skill boundaries. |

A manually scripted Git success does not prove the agent chose the right procedure. A textual
source review does not prove either. A browser assertion is required for layout behavior even if
script-output tests pass.

### Datasets that make the tests meaningful

Pair successful progression with missing, declined, and stale authorization. Pair real defects with
clean controls. Pair complete evidence with unavailable diagnostics and partial results.

Reuse fixture dimensions instead of inventing an enormous cross-product: clean/dirty worktrees,
staged/unstaged/shared-file changes, ordinary/reconstructed history, available/missing companions,
fresh/resumed sessions, Markdown/Artifact/both, matching/conflicting remote state, and successful/
timed-out/partially completed mutations. Combine dimensions where an interaction has demonstrated
risk, such as reconstruction plus unrelated staged work and an older stash.

Read the exact supplied approval scope; an answer to a missing architecture question is not
automatically acceptance of the implementation or commit proposal. Simulate every required human
turn deliberately. Record tool requests and resulting state, not hidden reasoning.

### Proposed composed exercises

| Exercise | Expected observable outcome |
| --- | --- |
| One approved issue in a small project | Implementation, full verification, review, human implementation approval, approved semantic commits, final verification, authorized push and closure all occur in order. |
| A milestone with branching dependencies | Closing A unblocks B and C; the agent reports the graph and recommendation, then stops at the agreed human/new-pass boundary. |
| A non-Laravel project with no custom companion | Portable skills use the actual project's tools; no Laravel commands or invented mandatory companion appear. |
| A paired guide with an interrupted Artifact update | Markdown and Artifact results are reported separately; recovery preserves identity and does not claim both are current prematurely. |
| A milestone PR with a closed-issue CI correction | Ship investigates and secures authorization; implementation owns the fix and its review/approval lifecycle; ship resumes after actual CI success. |
| An approved release interrupted after creating its tag | Recovery reconciles the correct existing tag and completes only missing authorized publication steps. |

These are proposed exercises, not newly imposed publication requirements. A real integration run
needs an explicitly scoped disposable target and authorization for its external effects.

### Results and repeatability

Use result labels that describe what happened: passed, failed, blocked by environment, pending
decision, or not run. Keep source-only alignment distinct from an executed pass. Preserve known
regression targets even when they fail; do not weaken the assertion to match a defective example.

For an agent run, record model and harness version/configuration, skill source and installed-file
identity, fixture and dependency versions, available capabilities, user turns, commands/tool
events, final state, and evaluation method. A seeded environment helps reproducibility but does
not guarantee identical model behavior.

Repeat important agent cases and report outcomes per run with the number of attempts. Never retry
until a pass and discard earlier failures, or average unauthorized mutations into a reassuring
overall score. Distinguish agent-behavior failures, harness problems, and environment blockers.

Use machine assertions for exact state and event ordering. Use a review rubric for semantic
judgments and retain disputed cases for human assessment. An optional model-based evaluator is
supporting evidence, not the sole proof that a commit, approval, or publication actually happened.

### Build the suite incrementally

1. Start with deterministic fixtures already demonstrated in scenarios: metadata, template source
   preservation, and Git content/staging/stash preservation.
2. Add agent tests for implementation approval, commit-plan approval, valid-approval continuation,
   and full-suite reuse.
3. Add review false-positive controls, planning recovery, and delivery retry cases.
4. Exercise the composed workflows in small compatible projects and separately validate browser
   and external integration behavior.
5. Maintain this catalogue when an owning contract changes. Update the relevant fixture and oracle,
   preserve scenario IDs, and let version control retain superseded wording.

Context-measurement tooling can have separate deterministic tests against its actual interface.
This catalogue does not invent that interface or duplicate its detailed test cases. Counting
instruction text is not a substitute for testing skill behavior.
