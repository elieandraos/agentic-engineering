# Skill audit scenarios

Reusable scenario specifications and the results observed during the 2026-09-08 audit. This is an evidence record for future regression testing, not a claim that an automated skill test suite already exists.

**Audited source:** [`86107d1f3f310c5ae19d5ea8e8f8388d6738918a`](https://github.com/elieandraos/agentic-engineering/commit/86107d1f3f310c5ae19d5ea8e8f8388d6738918a) on `main`. This is the post-v2.0.0 roadmap/plan closeout state. Skill runtime files are unchanged from the published v2.0.0 content. Results below describe this pinned source, not whichever commit is current when this document is read.

**Change boundary:** this audit adds only `scenarios.md`. It does not fix or alter any skill, template, README, roadmap, installation, consumer project, tag, or release. The authorized commit/push of this document is a repository mutation; the audit scenarios themselves did not mutate Git or GitHub.

## Scope and evidence

Inspected all 57 files under the seven `skills/` directories, including entrypoints, READMEs, rules, blueprints, and shipped PHP/HTML templates. Also inspected root `README.md`, `roadmap.md`, and both files under `docs/`: 61 source files in total. The architecture dossiers under `artifacts/` were not a separate full-audit scope.

Independent read-only passes covered planning/documentation, implementation/review, delivery, the Laravel companion, and installation. The coordinating pass reconciled their findings, re-read the material source passages, and independently repeated the HTML-script failures.

| Method | Cases | What was actually done | What it does not prove |
| --- | ---: | --- | --- |
| Measured | 2 | Description lengths and bounded relative-link resolution checked programmatically against fetched source. | Full loader acceptance, complete semantic validation, or external link availability. |
| Executed JavaScript | 5 | The exact shipped HTML script executed in V8 with a minimal DOM stub; concrete output/errors inspected. | Browser layout, real Artifact publication, or model compliance. |
| Source trace | 40 | Concrete fixtures walked through the written contracts or code; relevant external mechanics checked against primary sources. | Actual Git command execution, Laravel integration, CLI installation, or end-to-end skill invocation. |

**Result vocabulary:** `Aligned` means the checked output or source path agrees with the stated expectation at that method's evidence level. `Defect` means a concrete contradiction, incorrect recipe, or executed failure was found for the fixture. `Gap` means the written handoff/recovery path leaves a material case unspecified. These labels are not interchangeable with live test passes/failures.

There are 47 scenario records: 27 aligned, 18 defect cases, and 2 gaps. Multiple cases can expose one underlying issue, and several are explicitly low-priority extension cases. This is not an 18-bug severity score. Of the five executed JavaScript cases, three failed their expectations and two passed.

No installed skill was invoked in a consuming project, and no Claude Code/Artifact workflow was run end to end. PHP/Laravel execution was unavailable. External Boost-installed skills were not inspected. The CLI source comparison is pinned to `vercel-labs/skills` v1.5.24, commit `1682051d48c34f5eb135e6475c1a965dce05e820`; Laravel technical cross-checks used official Laravel 13 source/documentation. No compatibility across every historical framework or CLI version is claimed.

## Findings to address first

| Priority | Scenario IDs | Concrete issue |
| --- | --- | --- |
| High | IMP-05, IMP-07 | Literal Git recipes can include unrelated staged work or restore/drop an unrelated older stash. |
| High | DOC-03, DOC-04 | Artifact highlighting removes code content from ordinary quoted HTTPS URL examples. |
| Normal | IMP-06, IMP-08 | Reconstruction does not reach an earlier owning commit; isolation does not explicitly restore staged selection. |
| Normal | STACK-01, STACK-02, STACK-03 | Customer-ID casting defeats validation; accepted ascending date sorting falls back to descending; required/nullability guidance is incorrect. |
| Normal | META-01, CONS-01, CONS-02 | review-it description exceeds the format limit; selective install omits required siblings; lockfile integrity assurance is overstated. |
| Clarify | REV-05, SHIP-07 | Issue-free standalone review corrections and recovery without a historical release proposal need a stated path. |
| Low / bounded | DOC-05, DOC-08, STACK-04, STACK-08, CONS-03, CONS-04 | Unsupported-language edge case, mobile CSS cascade, factory naming, infrastructure-handler collision, explicit source refs, and Windows link qualification. |

Priority is this audit's assessment of consequence for the stated fixture. It is not a newly enforced delivery gate. Generic preservation rules may lead an experienced agent to adapt an unsafe recipe, but that does not make the literal recipe correct.

## Scenario records

### Format and repository references

#### META-01 — Skill descriptor limits

**Method:** Measured. **Result:** Defect. **Priority:** Normal.

**Fixture:** The seven SKILL.md entrypoints at the audited commit.

**Request/action:** Measure each description and compare it with the Agent Skills format.

**Expected:** Each description is nonempty and at most 1,024 characters; names match their directories.

**Observed at this evidence level:** review-it has 1,219 description characters, exceeding the limit by 195. The other six are within the limit. This establishes a format violation, not an observed loader rejection.

**Evidence:** [skills/review-it/SKILL.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/review-it/SKILL.md#L1-L4); [Agent Skills specification](https://agentskills.io/specification).

#### META-02 — Relative source links

**Method:** Measured. **Result:** Aligned.

**Fixture:** Fetched repository tree and all files in the audit scope.

**Request/action:** Resolve explicit relative Markdown file links outside fenced examples against the pinned tree.

**Expected:** Every path matched by this bounded check resolves.

**Observed at this evidence level:** No unresolved file target was found by that check. It did not establish external URL availability, anchor validity, implicit prose-reference completeness, or selective-install dependency availability.

**Evidence:** [docs/skill-authoring-methodology.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/docs/skill-authoring-methodology.md).

### Investigation

#### LAB-01 — Investigation may end with an answer

**Method:** Source trace. **Result:** Aligned.

**Fixture:** The user asks how authentication works. The relevant code is accessible and sufficient; no guide or plan was requested.

**Request/action:** Explain the existing authentication architecture.

**Expected:** Inspect evidence, give a supported explanation, and finish without manufacturing a publication or planning task.

**Observed at this evidence level:** lab-it permits an investigation to end with a verified answer. Its routing does not force document-it or plan.md synthesis.

**Evidence:** [skills/lab-it/SKILL.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/lab-it/SKILL.md#L29-L71).

### Documentation and Artifact template

#### DOC-01 — New Markdown guide from current evidence

**Method:** Source trace. **Result:** Aligned.

**Fixture:** Current findings are available; the user explicitly requests Markdown. Artifact capability and graphical rendering are unavailable. No recap approval has yet been given.

**Request/action:** Create a guide from these findings as Markdown.

**Expected:** Reuse current evidence, use docs/ for the new file, and follow the recap/approval procedure. Do not ask the already-settled format question or require an Artifact tool.

**Observed at this evidence level:** The written path supports Markdown and plain fenced diagrams. It retains a recap approval checkpoint unless already satisfied; no file was actually created in this scenario.

**Evidence:** [skills/document-it/SKILL.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/document-it/SKILL.md#L67-L122); [skills/document-it/rules/doc-style.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/document-it/rules/doc-style.md).

#### DOC-02 — Explicit update to one member of a paired guide

**Method:** Source trace. **Result:** Aligned.

**Fixture:** A Markdown/Artifact pair exists. The Markdown file is architecture.md at the repository root. Artifact updating is unavailable; its last known contents are readable. The user explicitly chooses a Markdown-only update.

**Request/action:** Update the Markdown guide and leave the Artifact for later.

**Expected:** Preserve the existing Markdown path, update dependent claims in the chosen output, and report the Artifact's divergence accurately.

**Observed at this evidence level:** Identity, maintenance, and review rules preserve the out-of-docs/ path and honor the explicit single-format exception. If the Artifact is also unreadable, coverage of it must be reported as unavailable rather than asserted.

**Evidence:** [skills/document-it/SKILL.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/document-it/SKILL.md#L103-L161); [skills/document-it/rules/maintenance.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/document-it/rules/maintenance.md); [skills/document-it/rules/review.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/document-it/rules/review.md).

#### DOC-03 — TypeScript URL survives highlighting

**Method:** Executed JavaScript. **Result:** Defect. **Priority:** High.

**Fixture:** One ts block contains: const url = "https://example.com"; followed by const mode = "safe"; on the next line.

**Request/action:** Execute the unmodified shipped highlighter against a minimal DOM stub.

**Expected:** Adding highlighting must preserve every source character and leave no internal placeholder.

**Observed at this evidence level:** The emitted HTML loses the URL suffix `//example.com";` and contains an unresolved control-character placeholder. The comment pass treats the URL as a comment before the string pass, creating a nested placeholder that the single restore pass does not fully restore.

**Evidence:** [skills/document-it/rules/template.html](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/document-it/rules/template.html#L305-L345).

#### DOC-04 — PHP URL survives highlighting

**Method:** Executed JavaScript. **Result:** Defect. **Priority:** High.

**Fixture:** One php block contains: $url = "https://example.com"; followed by $mode = "safe"; on the next line.

**Request/action:** Execute the same shipped highlighter.

**Expected:** The formatted block retains the complete PHP source.

**Observed at this evidence level:** The same URL-content loss and unresolved placeholder occur. A paired Markdown guide could retain correct code while the Artifact output loses it.

**Evidence:** [skills/document-it/rules/template.html](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/document-it/rules/template.html#L305-L345).

#### DOC-05 — Unsupported language cannot abort later blocks

**Method:** Executed JavaScript. **Result:** Defect. **Priority:** Low.

**Fixture:** A block has data-lang="constructor", followed by a normal ts block.

**Request/action:** Execute the shipped script over both blocks.

**Expected:** The first block falls back to escaped plain text; the next block still highlights.

**Observed at this evidence level:** Inherited object properties pass the supported-language lookup. The script throws TypeError: kws.join is not a function; neither block's innerHTML is assigned. This is an unusual language-label edge case, not a normal guide input.

**Evidence:** [skills/document-it/rules/template.html](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/document-it/rules/template.html#L261-L353).

#### DOC-06 — Ordinary unsupported language fallback

**Method:** Executed JavaScript. **Result:** Aligned.

**Fixture:** A python block contains if x < 2: followed by print("safe").

**Request/action:** Execute the shipped script.

**Expected:** Escape HTML characters and retain the source as plain text without throwing.

**Observed at this evidence level:** The output contains &lt; for the comparison and preserves the snippet; no exception or leftover placeholder occurs.

**Evidence:** [skills/document-it/rules/template.html](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/document-it/rules/template.html#L284-L290).

#### DOC-07 — JSON URL control case

**Method:** Executed JavaScript. **Result:** Aligned.

**Fixture:** A json block contains {"url":"https://example.com","ok":true}.

**Request/action:** Execute the shipped script.

**Expected:** Highlight keys, strings, and the Boolean while preserving the source.

**Observed at this evidence level:** The JSON path preserves the URL and other source characters. The demonstrated URL bug is in the ts/php path, not every language.

**Evidence:** [skills/document-it/rules/template.html](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/document-it/rules/template.html#L284-L345).

#### DOC-08 — Mobile navigation cascade

**Method:** Source trace. **Result:** Defect. **Priority:** Low.

**Fixture:** Viewport width is 800px or 375px; the generated guide has several navigation entries.

**Request/action:** Resolve the applicable .nav declarations, then later verify scrolling in a browser.

**Expected:** The mobile rule's intended static position and removed right border should take effect.

**Observed at this evidence level:** The later base .nav declaration has the same specificity and overrides position: static and border-right: none. The later mobile rule changes only height. The source-resolved position remains sticky; visual severity was not browser-tested.

**Evidence:** [skills/document-it/rules/template.html](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/document-it/rules/template.html#L94-L98).

### Planning and interrupted work

#### PLAN-01 — Interrupted issue batch with recoverable approval

**Method:** Source trace. **Result:** Aligned.

**Fixture:** Three complete issue definitions were approved. GitHub creation timed out after two matching issues were created; the full definitions and their approval evidence remain available.

**Request/action:** Continue the interrupted creation batch.

**Expected:** Query GitHub first, reconcile actual content/identity, reuse the matching issue numbers, and create only the missing member after normal checks.

**Observed at this evidence level:** The batch recovery procedure separates already-created members from missing work and forbids blind retry or duplicate creation.

**Evidence:** [skills/plan-it/rules/sequencing.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/plan-it/rules/sequencing.md#L121-L154).

#### PLAN-02 — Existing issue is not proof of approval

**Method:** Source trace. **Result:** Aligned.

**Fixture:** Two live GitHub issues match recovered definitions, but the earlier approval evidence and the third complete definition are unavailable.

**Request/action:** Resume the planning session.

**Expected:** Recover what the issues actually establish, treat unapproved recovered definitions as drafts, and obtain missing decisions through normal review.

**Observed at this evidence level:** The rules do not infer approval from existence or formatting. Missing durable planning storage leads to an honest stop rather than invented authorization; storage remains deliberately deferred.

**Evidence:** [skills/plan-it/rules/sequencing.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/plan-it/rules/sequencing.md#L121-L154); [skills/plan-it/rules/issue-conventions.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/plan-it/rules/issue-conventions.md#L15-L21); [skills/plan-it/rules/review.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/plan-it/rules/review.md).

#### PLAN-03 — Approved target versus stale premise

**Method:** Source trace. **Result:** Aligned.

**Fixture:** An approved plan contains a locked architectural target, an outdated factual premise, and an unresolved security choice. Current implementation still differs from the intended target.

**Request/action:** Turn the plan into issues using current code evidence.

**Expected:** Preserve the intended target, recheck stale facts, and surface the unresolved security decision before drafting work that depends on it.

**Observed at this evidence level:** The plan-input and reconciliation rules distinguish implementation drift from a changed approved decision and do not silently convert an open decision into a settled fact.

**Evidence:** [skills/plan-it/rules/plan-md-input.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/plan-it/rules/plan-md-input.md#L19-L36); [skills/plan-it/rules/design-reconciliation.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/plan-it/rules/design-reconciliation.md).

### Implementation, Git state, and verification

#### IMP-01 — Issue created elsewhere, optional stack

**Method:** Source trace. **Result:** Aligned.

**Fixture:** A GitHub issue was authored without plan-it but satisfies its conventions and review bar. The user approved implementation. The project has established framework conventions but no custom stack companion.

**Request/action:** Implement the issue.

**Expected:** Accept equivalent issue evidence; inspect and follow project guidance; do not require a custom stack or a prior plan-it session.

**Observed at this evidence level:** The ordinary entry contract accepts this issue. Project instructions and applicable tooling guidance still apply when no companion is installed.

**Evidence:** [skills/implement-it/SKILL.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/SKILL.md#L62-L84).

#### IMP-02 — Review evidence and human gates remain distinct

**Method:** Source trace. **Result:** Aligned.

**Fixture:** Implementation is verified and review-it is clean. Initially only permission to implement exists. In a continuation variant, complete actual Gate 1 and Gate 2 approvals for unchanged work are available.

**Request/action:** Continue toward commits and authorized publication.

**Expected:** First variant: report at Gate 1 and wait for its approval before commit planning. Continuation: preserve applicable completed approvals; refresh only when material changes invalidate them.

**Observed at this evidence level:** The gate and validity rules distinguish initial implementation permission, review evidence, commit-plan approval, and push authorization. A clean review does not itself approve Gate 1.

**Evidence:** [skills/implement-it/rules/review-gates.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/review-gates.md).

#### IMP-03 — Milestone branching retains the human pause

**Method:** Source trace. **Result:** Aligned.

**Fixture:** Issue A is completed. Issues B and C are both dependency-ready.

**Request/action:** Continue the milestone workflow.

**Expected:** Recompute readiness, recommend the next issue with a reason, and pause for the user's selection/review boundary.

**Observed at this evidence level:** The written sequencing retains the intentional issue-by-issue pause. This audit does not treat that agreed human stop as an autonomy defect.

**Evidence:** [skills/implement-it/rules/sequencing.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/sequencing.md#L100-L148).

#### IMP-04 — Unknown worktree ownership

**Method:** Source trace. **Result:** Aligned.

**Fixture:** The starting worktree contains edits that resemble the issue but may belong to the user; their origin is not established.

**Request/action:** Begin implementing or verifying the issue.

**Expected:** Preserve the existing content, seek reliable provenance, and ask only when unresolved origin materially affects safe continuation.

**Observed at this evidence level:** The general preservation rule rejects recency and scope resemblance as ownership proof. The specific reset/stash recipes below do not fully carry this invariant through.

**Evidence:** [skills/implement-it/rules/verification.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/verification.md#L91-L112).

#### IMP-05 — Soft reset must not commit unrelated staged work

**Method:** Source trace. **Result:** Defect. **Priority:** High.

**Fixture:** An unpublished commit must be reconstructed into semantic groups. Unrelated user change U is already staged; the removed commit contains groups A and B.

**Request/action:** Follow the documented reset/add/commit reconstruction recipe.

**Expected:** Only the selected semantic group enters each new commit; U and its staged state remain outside task commits.

**Observed at this evidence level:** git reset --soft HEAD~1 preserves the index. Selective git add does not remove U or other already-staged groups. A plain git commit can include them. The literal recipe omits index control needed to satisfy its own grouping/preservation contract.

**Evidence:** [skills/implement-it/rules/commit-boundaries.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/commit-boundaries.md#L149-L166); [skills/implement-it/rules/verification.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/verification.md#L91-L112); [Git reset reference](https://git-scm.com/docs/git-reset).

#### IMP-06 — Correction belongs to an earlier commit

**Method:** Source trace. **Result:** Defect. **Priority:** Normal.

**Fixture:** History is base → A → B, all unpublished. A needs a correction for its own correctness; there are no unrelated changes.

**Request/action:** Fold the correction into its semantic owner using the documented recipe.

**Expected:** Reconstruct A with its correction, then preserve B as the appropriate subsequent semantic commit.

**Observed at this evidence level:** The hard-coded HEAD~1 reset leaves A in history. A new commit after it can contain B plus the correction, leaving A defective. This fails the stated objective even in a clean worktree.

**Evidence:** [skills/implement-it/rules/commit-boundaries.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/commit-boundaries.md#L45-L62); [skills/implement-it/rules/commit-boundaries.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/commit-boundaries.md#L149-L166); [Git reset reference](https://git-scm.com/docs/git-reset).

#### IMP-07 — Isolation with no new stash

**Method:** Source trace. **Result:** Defect. **Priority:** High.

**Fixture:** The final semantic commit leaves a clean worktree. An unrelated older user stash already exists.

**Request/action:** Follow the isolation loop's stash push, verify, stash pop sequence.

**Expected:** Do not restore or drop any unrelated stash; restoration must refer to a stash actually created for this isolation step.

**Observed at this evidence level:** On the clean tree, stash push creates no new entry. The unqualified stash pop selects the older entry and can apply/drop it. The recipe lacks a creation/identity check; a general preserve-work instruction does not repair this literal command sequence.

**Evidence:** [skills/implement-it/rules/verification.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/verification.md#L315-L335); [Git stash reference](https://git-scm.com/docs/git-stash).

#### IMP-08 — Isolation preserves staged selection

**Method:** Source trace. **Result:** Defect. **Priority:** Normal.

**Fixture:** Remaining work contains both staged and unstaged changes; the stash applies without conflict and stash.index has its default false value.

**Request/action:** Hide remaining work during isolation, then restore it.

**Expected:** Recover both file contents and the original staged/unstaged selection.

**Observed at this evidence level:** Plain git stash pop does not request index restoration. Contents can return with their previous staged selection lost. Restoration failure/conflict handling also needs an explicit preservation path; no failure was executed in this audit.

**Evidence:** [skills/implement-it/rules/verification.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/verification.md#L315-L326); [Git stash reference](https://git-scm.com/docs/git-stash).

#### IMP-09 — Full-suite reuse follows final content

**Method:** Source trace. **Result:** Aligned.

**Fixture:** A complete pre-Gate-1 run has identifiable evidence. Compare unchanged final content, a formatter/hook edit after that run, and a final isolation run with nothing left stashed.

**Request/action:** Satisfy completed-issue verification.

**Expected:** Reuse only with proven final-content equivalence, equivalent inputs/environment, and no unresolved limitation. Accept a qualifying actual final-state run; reject a superseded or materially changed run.

**Observed at this evidence level:** The owning reuse rule covers both legitimate sources and invalidates reuse after relevant content/environment changes. A cache success alone is not evidence of actual complete execution.

**Evidence:** [skills/implement-it/rules/verification.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/verification.md); [skills/implement-it/rules/review-gates.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/review-gates.md).

### Implementation review

#### REV-01 — Real comparison base and complete worktree scope

**Method:** Source trace. **Result:** Aligned.

**Fixture:** A feature branch targets another feature branch, tracks its own remote counterpart, and has staged, unstaged, and untracked changes.

**Request/action:** Review the branch and current worktree.

**Expected:** Resolve the actual requested/PR integration base, ordinarily compare from its merge-base, and account for all requested worktree content without staging it.

**Observed at this evidence level:** The rule does not treat the tracking counterpart as the merge target. An explicit alternative comparison takes precedence and must be labeled accurately.

**Evidence:** [skills/review-it/rules/scope.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/review-it/rules/scope.md).

#### REV-02 — Authorized change can still be insecure

**Method:** Source trace. **Result:** Aligned.

**Fixture:** The user authorized a broader feature. The implementation contains a concretely evidenced security defect. No custom stack companion is installed, but project conventions are available.

**Request/action:** Review the authorized implementation.

**Expected:** Do not flag the authorized feature merely for scope expansion; still inspect correctness, security, data integrity, and project-backed framework conventions.

**Observed at this evidence level:** The authorization exemption is limited to accidental scope expansion. Missing a companion skips only checks dependent on that companion's rules, not ordinary engineering review.

**Evidence:** [skills/review-it/rules/checklist.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/review-it/rules/checklist.md); [skills/review-it/rules/scope.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/review-it/rules/scope.md).

#### REV-03 — Unavailable diagnostics remain a limitation

**Method:** Source trace. **Result:** Aligned.

**Fixture:** A suspected defect cannot safely be exercised: the diagnostic is unavailable or would cause unauthorized changes.

**Request/action:** Complete the review report.

**Expected:** Use available concrete evidence; distinguish a confirmed finding from a concern requiring missing evidence. Never imply a test ran or the unresolved surface is clean.

**Observed at this evidence level:** review-it reports limitations. implement-it must obtain missing material evidence and retry, or surface the blocked decision before proceeding through Gate 1.

**Evidence:** [skills/review-it/rules/verification.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/review-it/rules/verification.md#L9-L35); [skills/implement-it/rules/review-gates.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/review-gates.md#L77-L92).

#### REV-04 — Review identity changes without a new HEAD

**Method:** Source trace. **Result:** Aligned.

**Fixture:** After a clean review, edit a dirty file without committing, or keep the same head SHA but change the comparison base. Then request a scoped re-review.

**Request/action:** Decide whether the earlier clean result still applies.

**Expected:** Invalidate the affected result, identify actual content and comparison, and state only the surface rechecked.

**Observed at this evidence level:** The report contract records dirty-content identity and branch comparison identity, and requires scoped coverage alongside identity. A head SHA alone does not preserve the old assurance.

**Evidence:** [skills/review-it/rules/verification.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/review-it/rules/verification.md#L41-L88).

#### REV-05 — Standalone finding with no issue

**Method:** Source trace. **Result:** Gap.

**Fixture:** review-it finds a confirmed defect in a standalone PR/worktree. No issue exists, and this is not a ship-it milestone-CI correction. The user authorizes the fix.

**Request/action:** Hand the finding to implement-it.

**Expected:** Explain the valid implementation entry route and any prerequisite instead of implying the handoff is already complete.

**Observed at this evidence level:** review-it sends all corrections to implement-it, but ordinary implementation requires an issue; its explicit no-issue exception is a ship-it delivery correction. The standalone case has no express matching route. This does not prove the system cannot fix it: the user may choose issue planning or explicitly override the default contract.

**Evidence:** [skills/review-it/SKILL.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/review-it/SKILL.md#L15-L33); [skills/review-it/SKILL.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/review-it/SKILL.md#L61-L66); [skills/implement-it/SKILL.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/SKILL.md#L62-L100).

### Milestone delivery and release

#### SHIP-01 — Ready milestone PR with existing approval

**Method:** Source trace. **Result:** Aligned.

**Fixture:** Zero open issues are freshly confirmed; manual testing is confirmed; no follow-up is needed. The exact PR title, head, base, and body are already approved.

**Request/action:** Create the milestone PR.

**Expected:** Check for an existing match, preserve applicable proposal approval, create only if absent, and re-fetch the result.

**Observed at this evidence level:** The procedure distinguishes PR fields from release fields and supports recovery without duplicate creation or a demonstrated need to reapprove identical content.

**Evidence:** [skills/ship-it/rules/milestone-completion.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/rules/milestone-completion.md#L136-L146); [skills/ship-it/rules/milestone-completion.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/rules/milestone-completion.md#L199-L248).

#### SHIP-02 — Closed-issue CI correction versus new scope

**Method:** Source trace. **Result:** Aligned.

**Fixture:** An open milestone PR fails CI. The correction belongs to a closed issue's approved scope and is explicitly authorized. A later finding requires genuinely new behavior.

**Request/action:** Correct the CI failure and resume delivery.

**Expected:** ship-it investigates/explains/secures authorization; implement-it fixes through review, gates, commits, verification, and authorized push. New scope follows planning intake.

**Observed at this evidence level:** The closed-issue correction needs no reopened/new issue. Delivery resumes after the actual CI rerun is green; the correction authorization does not silently cover new scope.

**Evidence:** [skills/ship-it/rules/milestone-completion.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/rules/milestone-completion.md#L277-L312); [skills/implement-it/SKILL.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/SKILL.md#L86-L100); [skills/plan-it/rules/discovered-work.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/plan-it/rules/discovered-work.md).

#### SHIP-03 — All open issues blocked

**Method:** Source trace. **Result:** Aligned.

**Fixture:** A milestone has open issues, all blocked, with an empty ready set.

**Request/action:** Assess the next milestone action.

**Expected:** Report blockers and do not declare delivery readiness.

**Observed at this evidence level:** Both the implementation handoff and ship-it entry distinguish zero open issues from zero ready issues.

**Evidence:** [skills/implement-it/rules/sequencing.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/sequencing.md#L100-L115); [skills/ship-it/SKILL.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/SKILL.md#L24-L33).

#### SHIP-04 — Fresh post-merge closure and release

**Method:** Source trace. **Result:** Aligned.

**Fixture:** Fresh session: the user confirms PR 100 merged and asks to close milestone 4 and publish v1.2.0. Exact release target/title/body are not yet approved.

**Request/action:** Continue post-merge delivery.

**Expected:** Recognize the supplied merge confirmation and post-merge authorization; re-query milestone state. Prepare the missing concrete release proposal before its publication boundary.

**Observed at this evidence level:** Closure and release are independent branches. Closure can proceed when its own conditions hold; the broad request does not invent exact release content approval.

**Evidence:** [skills/ship-it/rules/milestone-completion.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/rules/milestone-completion.md#L348-L386); [skills/ship-it/rules/release.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/rules/release.md#L44-L65); [skills/ship-it/rules/release.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/rules/release.md#L158-L184).

#### SHIP-05 — Tag/release timeout with proposal available

**Method:** Source trace. **Result:** Aligned.

**Fixture:** Creation times out. The exact approved release proposal is available. A matching tag, partial release, or complete release may already exist.

**Request/action:** Resume publication.

**Expected:** Query authoritative state first, compare actual version/target/title/body/publication status, and perform only missing authorized steps.

**Observed at this evidence level:** The partial-outcome handling forbids assuming timeout means nothing happened and avoids recreating correct artifacts.

**Evidence:** [skills/ship-it/rules/release.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/rules/release.md#L177-L228).

#### SHIP-06 — Consumer release policy controls

**Method:** Source trace. **Result:** Aligned.

**Fixture:** The project states branch/version/release conventions that differ from familiar defaults.

**Request/action:** Prepare delivery.

**Expected:** Use explicit project policy first and established history only as fallback; ask about genuine conflicts.

**Observed at this evidence level:** The rules do not impose main, a tag prefix, or a guessed release mechanism. Git/GitHub remains an intentional ecosystem dependency.

**Evidence:** [skills/ship-it/rules/release.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/rules/release.md#L67-L98); [skills/ship-it/rules/milestone-completion.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/rules/milestone-completion.md#L207-L211).

#### SHIP-07 — Recovered release without historical proposal

**Method:** Source trace. **Result:** Gap.

**Fixture:** A tag/release already exists after an interruption, but the original exact proposal or approval evidence is unavailable.

**Request/action:** Describe and recover publication state.

**Expected:** Distinguish observed remote state from historical approval evidence; do not invent approval, duplicate, or silently overwrite existing artifacts.

**Observed at this evidence level:** Release recovery references the approved step-4 proposal without the explicit missing-evidence branch already present for PR recovery. A new complete proposal and approval can still provide a valid path; this is a reporting/recovery gap, not proof of unsafe publication.

**Evidence:** [skills/ship-it/rules/release.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/rules/release.md#L177-L184); [skills/ship-it/rules/release.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/rules/release.md#L224-L228); [skills/ship-it/rules/milestone-completion.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/ship-it/rules/milestone-completion.md#L218-L235).

### Laravel/Inertia companion

#### STACK-01 — Reject malformed customer identifiers

**Method:** Source trace. **Result:** Defect. **Priority:** Normal.

**Fixture:** Customer 12 exists. Submit customer_id as the string 12garbage, or as JSON number 12.9, to the worked StoreOrderRequest.

**Request/action:** Validate and create an order using the blueprint.

**Expected:** Reject the invalid integer identifier rather than associate the order with a truncated/cast ID.

**Observed at this evidence level:** prepareForValidation calls integer(), which uses a PHP integer cast. Each input becomes 12 before integer/exists validation. The declared rules can therefore accept the changed identifier. This is validation loss and possible wrong association, not a demonstrated authorization bypass.

**Evidence:** [skills/laravel-inertia-stack/blueprints/resource-controller.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/blueprints/resource-controller.md#L38-L56); [Laravel reference](https://github.com/laravel/framework/blob/13.x/src/Illuminate/Support/Traits/InteractsWithData.php#L281-L291); [PHP integer conversion](https://www.php.net/manual/en/language.types.integer.php#language.types.integer.casting).

#### STACK-02 — Accepted created_at ascending sort

**Method:** Source trace. **Result:** Defect. **Priority:** Normal.

**Fixture:** The worked endpoint has orders dated January and February.

**Request/action:** Request ?sort=created_at&direction=asc.

**Expected:** The accepted query should return January before February.

**Observed at this evidence level:** Validation accepts created_at, but OrderSort implements total() and default(), with no createdAt(). QuerySorter falls back to created_at desc, producing the reverse of the requested order.

**Evidence:** [skills/laravel-inertia-stack/blueprints/filters-and-sorting.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/blueprints/filters-and-sorting.md#L83-L112); [skills/laravel-inertia-stack/templates/app/Sorts/QuerySorter.php](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/templates/app/Sorts/QuerySorter.php#L45-L51).

#### STACK-03 — Present but nullable input

**Method:** Source trace. **Result:** Defect. **Priority:** Normal.

**Fixture:** The user must supply a notes key and is allowed to clear it to null. Follow the actions rule's claim about a required, nullable field.

**Request/action:** Validate notes: null with required, nullable, string.

**Expected:** The recipe should model mandatory presence with an allowed null value.

**Observed at this evidence level:** Laravel required rejects null; nullable does not override it. The stated combination rejects the clearing request. present plus nullable expresses the described key-presence requirement.

**Evidence:** [skills/laravel-inertia-stack/rules/actions.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/rules/actions.md#L68-L74); [Laravel reference](https://laravel.com/framework/docs/13.x/validation#rule-required); [Laravel reference](https://github.com/laravel/framework/blob/13.x/src/Illuminate/Validation/Concerns/ValidatesAttributes.php#L2168-L2180).

#### STACK-04 — Factory relationship name differs from model name

**Method:** Source trace. **Result:** Defect. **Priority:** Low.

**Fixture:** Employee has division(): BelongsTo targeting Department; no department() relationship exists.

**Request/action:** Use Employee::factory()->for($department)->create() based on the rule's inference explanation.

**Expected:** Use the established division relationship, explicitly naming it when required.

**Observed at this evidence level:** Factory::for() infers a camel-cased related model basename, not the belongsTo return type. It looks for department(), so the example requires for($department, 'division'). Conventional matching names conceal the error.

**Evidence:** [skills/laravel-inertia-stack/rules/factories-and-seeders.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/rules/factories-and-seeders.md#L84-L90); [Laravel reference](https://github.com/laravel/framework/blob/13.x/src/Illuminate/Database/Eloquent/Factories/Factory.php#L759-L766).

#### STACK-05 — Sorter input validation rejects arrays and malicious values

**Method:** Source trace. **Result:** Aligned.

**Fixture:** Use the worked IndexOrderRequest with missing/null direction, array-valued sort/direction, or malicious column/direction strings.

**Request/action:** Trace normalization, validation, and sorter entry.

**Expected:** Missing direction defaults coherently; invalid arrays/strings fail before SQL or dynamic dispatch.

**Observed at this evidence level:** The shown whitelist rejects the hostile/array cases and missing/null direction becomes asc. No SQL injection in this endpoint was demonstrated. The separate accepted created_at defect remains.

**Evidence:** [skills/laravel-inertia-stack/blueprints/filters-and-sorting.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/blueprints/filters-and-sorting.md); [skills/laravel-inertia-stack/templates/app/Sorts/QuerySorter.php](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/templates/app/Sorts/QuerySorter.php).

#### STACK-06 — Single-action and child-resource authorization

**Method:** Source trace. **Result:** Aligned.

**Fixture:** Use the blueprint's authorized __invoke controller and a child resource policy receiving a parent model under Laravel 13.

**Request/action:** Trace middleware attribute discovery and policy argument handling.

**Expected:** Authorization executes before the controller body with the intended class/parent arguments.

**Observed at this evidence level:** Official Laravel source supports the demonstrated attributes and argument handling. No technical flaw was found in these two paths; no application route was executed.

**Evidence:** [skills/laravel-inertia-stack/rules/authorization.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/rules/authorization.md); [skills/laravel-inertia-stack/blueprints/resource-controller.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/blueprints/resource-controller.md).

#### STACK-07 — Resource and flash assertion wiring

**Method:** Source trace. **Result:** Aligned.

**Fixture:** Use the TestingServiceProvider resource assertions and Inertia flash assertions with their documented shapes.

**Request/action:** Trace expected and actual serialization against the adapter behavior.

**Expected:** Compare compatible serialized values and read the adapter's actual flash-session key.

**Observed at this evidence level:** The source paths agree. The limitation of tests comparing production resources with themselves is already documented; this is not proof that application values are correct.

**Evidence:** [skills/laravel-inertia-stack/templates/app/Providers/TestingServiceProvider.php](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/templates/app/Providers/TestingServiceProvider.php); [skills/laravel-inertia-stack/rules/test-ownership.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/rules/test-ownership.md).

#### STACK-08 — Dynamic handler collides with infrastructure method

**Method:** Source trace. **Result:** Defect. **Priority:** Low.

**Fixture:** A future caller bypasses the shown HTTP whitelist and directly passes sort column apply or default; a filter caller admits key apply.

**Request/action:** Trace generic QuerySorter/QueryFilter dispatch.

**Expected:** Treat unsupported handler names as unsupported rather than invoking an infrastructure method with the wrong argument type.

**Observed at this evidence level:** method_exists also matches infrastructure methods, which expect a Builder rather than the dispatched value/direction. A type error follows for these fixtures. The current worked request rejects these names, so this is an extension edge case, not an established remotely reachable vulnerability.

**Evidence:** [skills/laravel-inertia-stack/templates/app/Sorts/QuerySorter.php](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/templates/app/Sorts/QuerySorter.php#L45-L51); [skills/laravel-inertia-stack/templates/app/Filters/QueryFilter.php](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/laravel-inertia-stack/templates/app/Filters/QueryFilter.php).

### Installation and consumption

#### CONS-01 — Fresh selective implement-it install

**Method:** Source trace. **Result:** Defect. **Priority:** Normal.

**Fixture:** A fresh project has none of this repository's skills and follows implement-it/README.md's single-skill installation command.

**Request/action:** Install only implement-it, then follow its ordinary entry and pre-Gate-1 review requirements.

**Expected:** The installation guidance must provide or state the dependencies required for the advertised workflow.

**Observed at this evidence level:** The CLI selects/copies the requested skill only. plan-it's referenced issue/review contracts and the required review-it capability are absent; sibling links do not auto-install dependencies. This was checked against CLI source, not by installing into a project.

**Evidence:** [skills/implement-it/README.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/README.md#L49-L53); [skills/implement-it/SKILL.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/SKILL.md#L64-L68); [skills/implement-it/rules/review-gates.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/skills/implement-it/rules/review-gates.md#L26-L38); [Skills CLI source](https://github.com/vercel-labs/skills/blob/1682051d48c34f5eb135e6475c1a965dce05e820/src/add.ts#L1296-L1316); [Skills CLI source](https://github.com/vercel-labs/skills/blob/1682051d48c34f5eb135e6475c1a965dce05e820/src/installer.ts#L358-L360).

#### CONS-02 — Lockfile after local skill edits

**Method:** Source trace. **Result:** Defect. **Priority:** Normal.

**Fixture:** A project installed the skills, then someone edited its managed review-gates.md without changing skills-lock.json.

**Request/action:** Decide whether the existing lock proves installed content has not drifted.

**Expected:** A claim of current file integrity requires comparing the actual installed content with trusted recorded content.

**Observed at this evidence level:** The lock records a source hash at install/update time; it remains unchanged after the local edit. Its existence does not prove current destination files match. The consumption document overstates this assurance.

**Evidence:** [docs/skill-consumption.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/docs/skill-consumption.md#L104-L114); [Skills CLI source](https://github.com/vercel-labs/skills/blob/1682051d48c34f5eb135e6475c1a965dce05e820/src/add.ts#L1911-L1932); [Skills CLI source](https://github.com/vercel-labs/skills/blob/1682051d48c34f5eb135e6475c1a965dce05e820/src/local-lock.ts#L189-L196).

#### CONS-03 — Explicit source ref survives refresh

**Method:** Source trace. **Result:** Defect. **Priority:** Low.

**Fixture:** Use a GitHub tree URL with an explicit tag ref, rather than an unqualified owner/repository source.

**Request/action:** Trace installation lock recording and later refresh.

**Expected:** Describe default-branch behavior for unqualified sources without incorrectly applying it to an explicitly retained ref.

**Observed at this evidence level:** The inspected CLI parses, records, and reuses the explicit ref. The consumption document's blanket GitHub/default-branch statement is too broad; its ordinary unqualified examples remain accurate.

**Evidence:** [docs/skill-consumption.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/docs/skill-consumption.md#L110-L114); [Skills CLI source](https://github.com/vercel-labs/skills/blob/1682051d48c34f5eb135e6475c1a965dce05e820/src/source-parser.ts#L351-L370); [Skills CLI source](https://github.com/vercel-labs/skills/blob/1682051d48c34f5eb135e6475c1a965dce05e820/src/update.ts#L845-L868).

#### CONS-04 — Windows links versus POSIX links

**Method:** Source trace. **Result:** Defect. **Priority:** Low.

**Fixture:** Compare installer behavior on POSIX and Windows.

**Request/action:** Assess the consumption document's claim that installed links are always relative and portable across clone locations.

**Expected:** Qualify the claim by platform and actual link mechanism.

**Observed at this evidence level:** The inspected installer uses relative symlinks on POSIX but absolute-target junctions on Windows. The shown POSIX layout is valid; no Windows installation or clone was executed.

**Evidence:** [docs/skill-consumption.md](https://github.com/elieandraos/agentic-engineering/blob/86107d1f3f310c5ae19d5ea8e8f8388d6738918a/docs/skill-consumption.md#L93-L102); [Skills CLI source](https://github.com/vercel-labs/skills/blob/1682051d48c34f5eb135e6475c1a965dce05e820/src/installer.ts#L251-L258).

## Repeating the executed template cases

The following in-memory harness captures the method used here. Pass the audited template's complete HTML text as `templateHtml`. It extracts and executes the unmodified shipped script, supplies only the DOM methods that script uses, and records output/errors. It does not render a page or publish an Artifact. Only use this execution harness with deliberately selected, trusted repository code.

```js
function exerciseTemplate(templateHtml) {
  const script = templateHtml.match(/<script>([\s\S]*?)<\/script>/)[1];
  const cases = [
    {
      id: "DOC-03",
      blocks: [{
        lang: "ts",
        src: 'const url = "https://example.com";\nconst mode = "safe";'
      }]
    },
    {
      id: "DOC-04",
      blocks: [{
        lang: "php",
        src: '$url = "https://example.com";\n$mode = "safe";'
      }]
    },
    {
      id: "DOC-05",
      blocks: [
        { lang: "constructor", src: "x < y" },
        { lang: "ts", src: "const ok = true;" }
      ]
    },
    {
      id: "DOC-06",
      blocks: [{
        lang: "python",
        src: 'if x < 2:\n    print("safe")'
      }]
    },
    {
      id: "DOC-07",
      blocks: [{
        lang: "json",
        src: '{"url":"https://example.com","ok":true}'
      }]
    }
  ];

  return cases.map(testCase => {
    const nodes = testCase.blocks.map(block => ({
      textContent: block.src,
      innerHTML: ""
    }));
    const pres = nodes.map((node, index) => ({
      getAttribute: () => testCase.blocks[index].lang,
      querySelector: () => node
    }));
    let error = null;
    try {
      new Function("document", script)({
        querySelectorAll: () => pres
      });
    } catch (caught) {
      error = String(caught);
    }
    return {
      id: testCase.id,
      error,
      blocks: testCase.blocks.map((block, index) => ({
        ...block,
        html: nodes[index].innerHTML,
        unrestored: /[\u0000\u0002]/.test(nodes[index].innerHTML)
      }))
    };
  });
}
```

For regression assertions, require no exception, no unresolved stash marker, all blocks processed, and source-text preservation after removing only the highlighter's generated spans and decoding its HTML escaping. Unsupported languages should remain escaped plain text. The present harness returns observations; it is not an installed assertion runner.

Actual output from the coordinating pass is retained below. Control characters are JSON-escaped, not embedded as raw null bytes. The runner's IDs are mapped to the stable scenario IDs.

```json
[
  {
    "blocks": [
      {
        "html": "<span class=\"tok-keyword\">const</span> url = <span class=\"tok-string\">\"https:\u00000\u0002\nconst mode = \"</span>safe\";",
        "lang": "ts",
        "src": "const url = \"https://example.com\";\nconst mode = \"safe\";",
        "unrestored": true
      }
    ],
    "error": null,
    "id": "DOC-03"
  },
  {
    "blocks": [
      {
        "html": "<span class=\"tok-var\">$url</span> = <span class=\"tok-string\">\"https:\u00000\u0002\n$mode = \"</span>safe\";",
        "lang": "php",
        "src": "$url = \"https://example.com\";\n$mode = \"safe\";",
        "unrestored": true
      }
    ],
    "error": null,
    "id": "DOC-04"
  },
  {
    "blocks": [
      {
        "html": "",
        "lang": "constructor",
        "src": "x < y",
        "unrestored": false
      },
      {
        "html": "",
        "lang": "ts",
        "src": "const ok = true;",
        "unrestored": false
      }
    ],
    "error": "TypeError: kws.join is not a function",
    "id": "DOC-05"
  },
  {
    "blocks": [
      {
        "html": "if x &lt; 2:\n    print(\"safe\")",
        "lang": "python",
        "src": "if x < 2:\n    print(\"safe\")",
        "unrestored": false
      }
    ],
    "error": null,
    "id": "DOC-06"
  },
  {
    "blocks": [
      {
        "html": "{<span class=\"tok-attr\">\"url\"</span>:<span class=\"tok-string\">\"https://example.com\"</span>,<span class=\"tok-attr\">\"ok\"</span>:<span class=\"tok-keyword\">true</span>}",
        "lang": "json",
        "src": "{\"url\":\"https://example.com\",\"ok\":true}",
        "unrestored": false
      }
    ],
    "error": null,
    "id": "DOC-07"
  }
]
```

## Entry-point size observations

These measurements cover only SKILL.md, not conditionally loaded rule files. Rough tokens use characters divided by four and are not tokenizer measurements. Size by itself is not a runtime failure.

| Skill | Description characters | SKILL.md characters | Rough SKILL.md tokens |
| --- | ---: | ---: | ---: |
| document-it | 553 | 13742 | 3436 |
| implement-it | 839 | 10042 | 2511 |
| lab-it | 641 | 7497 | 1875 |
| laravel-inertia-stack | 373 | 4164 | 1041 |
| plan-it | 716 | 6542 | 1636 |
| review-it | 1219 | 6305 | 1577 |
| ship-it | 923 | 5919 | 1480 |

## Turning these cases into future tests

Keep scenario IDs stable. Preserve this baseline result when a fix lands; add the new tested commit, environment/model, method, evidence, and result rather than rewriting an old source trace as a live pass.

1. **Deterministic fixtures first:** template source preservation, description/schema checks, sorting/validation examples, and Git state-preservation recipes can have concrete assertions. Any future Git fixture should use a disposable repository with before/after content, index, stash identity, and history assertions; do not run reconstruction experiments in a working project.
2. **Skill behavior next:** start a fresh session with the selected skill/version and a controlled project fixture. Supply the exact request and approval state from the case. Retain tool calls, user pauses, findings, final reports, and actual mutations. Judge the observable actions and evidence, not whether the response repeats expected phrases.
3. **Keep authorization explicit:** fixtures must distinguish permission to implement from completed Gate 1 approval, Gate 2 approval, push permission, and exact publication approval. Supply later human responses deliberately when a case reaches those points.
4. **Real-environment follow-up:** separately exercise one complete issue lifecycle, a non-Laravel project without a companion, an actual Markdown/Artifact pair, and the installed Laravel/Boost composition. Those runs are not already completed by this document and are not newly imposed as a publication gate.

Known deferred topics remain deferred: durable issue-definition storage and the custom-stack/Boost precedence question were not resolved here. The intentional Git/GitHub dependency and manual pause between milestone issues were not classified as defects.

## Follow-up validation: IMP-05–08 corrections (2026-09-09)

This section records a bounded correction pass against the four `implement-it` defects/gaps the
2026-09-08 audit above flagged in the "Findings to address first" table: IMP-05, IMP-06, IMP-07, and
IMP-08. It supplements, and does not replace, those original records — their pinned source,
observations, and counts above are unchanged.

**What changed:** `skills/implement-it/rules/commit-boundaries.md`'s "Review corrections fold into
their semantic commit" section replaced the hard-coded `git reset --soft HEAD~1` recipe with a
procedure that determines the actual owning unpublished commit, confirms the full affected range is
unpublished, protects unrelated worktree content before rewriting, and rebuilds each semantic commit
from the combined index with a staged-diff check before every commit (patch-level staging via `git
add -p` / `git restore --staged` for a file whose content spans more than one semantic group).
`skills/implement-it/rules/verification.md` gained a new "Preserving unrelated worktree content
during a Git rewrite" procedure — a qualified stash-identity-verify-restore sequence, used by both
that reconstruction and the isolation-verification technique — replacing the previous unqualified
`git stash push -u` / `git stash pop` pair in the isolation loop.

**Tested state:** the corrected rule text as it exists in this working tree, built on top of pinned
commit `07bb5bfaf7ca1ac8be1280902095d2f52c712cb1` on `main` (this pass's own changes land as ordinary
new commits after it, per the same non-rewrite boundary described below).

**Method:** executed Git-mechanics verification only — disposable Git repositories created and
discarded outside this project (under a session scratch directory, not committed here), each running
the literal `git` commands the old and new rule text specify, with results inspected via `git log`,
`git show`, `git diff --staged`, `git status --porcelain`, and `git stash list`. This is the same
"Executed" evidence tier the original audit used for the HTML-script cases, applied here to Git
commands instead. **`implement-it` itself was not invoked in a live agent session** for this
follow-up — no agent carried out a request end to end through the skill's own activation, gates, or
reporting; only the underlying Git recipes were exercised directly. That remains an open item for the
"Real-environment follow-up" list above, not something this record claims to have done.

**Fixtures, steps, and results:**

- **IMP-05 (IMP-05 High).** Repo with commit `base`, then one unpublished commit combining groups A
  (`a.txt`) and B (`b.txt`), then unrelated file `u.txt` staged on top. *Original recipe:* `git reset
  --soft HEAD~1` staged all three files; `git add a.txt && git commit` committed all three (A, B, and
  U together) into one commit, because plain `git add` cannot narrow a commit below what is already
  staged — confirmed by inspecting `git show --stat` of the resulting commit. *Corrected recipe:* `U`
  was set aside via the qualified stash procedure before the reset; `git restore --staged` /
  targeted `git add` plus a `git diff --staged --stat` check before each commit produced two commits
  containing exactly `a.txt` and exactly `b.txt`; `U` was restored afterward in its original staged
  state (verified via `git show :u.txt` and `git status --porcelain`) and never appeared in either
  commit. Result: defect reproduced, corrected procedure verified on the same fixture shape.
- **IMP-06 (Normal).** Repo with `base → A (a.txt) → B (b.txt)`, all unpublished; a correction to
  `a.txt` made as an uncommitted edit while `HEAD` is `B`. *Original recipe:* `git reset --soft
  HEAD~1` reached only `B`'s parent (which happens to be `A` in this two-commit fixture) but the
  literal "selectively add and commit" step folded the correction into one commit sitting after the
  unchanged `A` commit; `git show <A>:a.txt` still returned the pre-correction content — `A` itself
  stayed defective. *Corrected recipe:* the owning commit `O` (`A`) was identified explicitly, `git
  reset --soft O~1` was used instead of a fixed `HEAD~1`, and the combined index was split back into
  a reconstructed `A` (correction folded in) and an intact `B`; `git show <new-A>:a.txt` returned the
  corrected content and `git show HEAD:b.txt` returned `B`'s unchanged content. Result: defect
  reproduced, corrected procedure verified on the same fixture shape.
- **IMP-07 (High).** Repo with an older unrelated stash created first, then a final semantic commit
  leaving a clean working tree. *Original recipe:* `git stash push -u` on the clean tree created no
  new entry ("No local changes to save"); the subsequent unqualified `git stash pop` nonetheless
  applied and dropped the older, unrelated stash, materializing `old.txt` into the tree. *Corrected
  procedure:* checking `git status --porcelain` first and skipping stashing entirely on a clean tree
  left the older stash untouched (`git stash list` unchanged, working tree still clean). Result:
  defect reproduced, corrected procedure verified on the same fixture shape.
- **IMP-08 (Normal).** Repo with `mixed.txt` partially staged (one staged hunk, one unstaged hunk)
  and an untracked `new_untracked.txt` present together. *Original recipe:* plain `git stash push -u`
  / `git stash pop` (no `--index`) restored file content but collapsed the staged hunk back to
  unstaged — `git diff --staged` was empty after the pop where it should not have been. *Corrected
  procedure:* `git stash push -u` followed by `git stash apply --index <recorded stash>` reproduced
  the exact pre-isolation `git diff --staged` and `git diff` output for `mixed.txt` and the exact
  untracked file content, confirmed before the entry was dropped. Result: defect reproduced,
  corrected procedure verified on the same fixture shape.
- **Restoration-failure handling (supports IMP-07/IMP-08's recovery-data requirement).** A qualified
  stash entry was created over an unstaged edit, then an independent conflicting commit was made to
  the same line before restoration was attempted. `git stash apply --index` reported a merge conflict
  (`Auto-merging`, `CONFLICT (content)`), left the working tree with an honest `UU` conflict marker,
  and — matching `git stash apply`'s own default behavior — did not drop the stash entry
  (`git stash list` still showed it afterward). This confirms the corrected procedure's "do not drop
  on conflict, report the specific problem" step is backed by `git stash apply`'s actual behavior, not
  merely asserted.

**Limitations:** all fixtures used small, single- or two-file repositories with no submodules, LFS
content, or binary files; behavior on those is unverified. The IMP-06 fixture is the minimal
two-commit case the original finding described; a longer unpublished range was not separately
exercised, though the corrected procedure's owning-commit-range logic does not depend on the range
length. `implement-it`'s own reporting and gate behavior around this procedure (how it would present
the reconstruction plan, or ask before rewriting) was not exercised — only the underlying Git
mechanics were.

## Follow-up correction: combined reconstruction, stash identity, verification policy (2026-09-09b)

This section records a second, bounded correction against commit
[`d6220f07c327cc0b5cc5632857aa509511a9fede`](https://github.com/elieandraos/agentic-engineering/commit/d6220f07c327cc0b5cc5632857aa509511a9fede)
— the first IMP-05–08 correction pass above. Control Room review of that commit found three
remaining defects, all in the same two rule files. This section supplements, and does not replace,
either the original 2026-09-08 audit or the first follow-up validation above; their pinned source,
observations, counts, and results are unchanged.

**What each defect was, and what changed:**

1. **The reconstruction procedure's own "protect unrelated content" step used an unqualified sweep
   that also hid an uncommitted task correction, not only genuinely unrelated work.** Because that
   step protected everything indiscriminately and restored it only after every commit was already
   rebuilt, a correction belonging to the commit being reconstructed was unavailable at the one step
   that needed it — reconstructing that commit without it, silently.
   `skills/implement-it/rules/commit-boundaries.md`'s "Something already committed, correction needed
   before push" now captures the correction as a zero-context patch file *before* anything is
   protected (`git diff -U0 --staged -- <path> > correction.patch`), reverse-applies it out of the
   working tree (`git apply --unidiff-zero -R`) so only genuinely unrelated content remains to be
   stashed, then reapplies the same patch (`git apply --unidiff-zero --index`) immediately after the
   reset to the owning commit's parent — exactly the step that needs it. The correction's content
   never leaves git tooling; it is never retyped or reconstructed from memory.
2. **The qualified stash-preservation procedure tracked an entry by its `stash@{n}` position and
   message, both of which can drift or repeat.**
   `skills/implement-it/rules/verification.md`'s "Preserving unrelated worktree content during a Git
   rewrite" now records the entry's commit SHA immediately on creation (`git rev-parse stash@{0}`)
   and uses that SHA as the entry's identity throughout. `apply` accepts the bare SHA directly; `drop`
   does not — the procedure now resolves the SHA to its current `stash@{n}` selector
   (`git stash list --format='%gd %H'`, matched by SHA) immediately before every drop, and stops
   without dropping anything if no current entry matches the recorded SHA.
3. **The reconstruction procedure's per-commit verification had been reworded from a mandatory
   requirement to a conditional one** ("...when that commit's own standalone correctness needs
   proving"), softening the previous pass's own restatement of the pre-existing policy. Step 7 of the
   reconstruction procedure now states the requirement unconditionally again — every commit the
   reconstruction produces is verified in isolation before the next is built — while leaving
   `rules/verification.md`'s general "a deliberate escalation, not the default" framing for ordinary,
   non-reconstruction commit building untouched; that section already lists post-hoc history
   reconstruction as one of the cases the escalation is reserved for, so this is a restatement of an
   existing, unweakened trigger, not a new policy.

**Tested state:** the corrected rule text as it exists in this working tree, built on top of
`d6220f07c327cc0b5cc5632857aa509511a9fede` on `main` (this pass's own changes land as ordinary new
commits after it, under the same non-rewrite boundary as the first pass).

**Method:** executed Git-mechanics verification only, in disposable repositories created and
discarded under a session scratch directory, never inside this project. `implement-it` itself was not
invoked in a live agent session for this follow-up either — the same limitation the first follow-up
record states applies here too.

**What the first follow-up's fixtures established, and what they did not:** the first follow-up
validated IMP-05 (unrelated staged work excluded) and IMP-06 (owning-commit-range reconstruction)
*separately* — no fixture combined an uncommitted correction with simultaneous unrelated staged work,
and the stash-identity check used single-entry, non-conflicting scenarios (a clean tree with an older
stash for IMP-07; a single mixed-staging entry for IMP-08). Combining a live correction with unrelated
work, and exercising stash identity under repeated-message/shifting-position conditions, are new
coverage added by this pass, not a re-run of the same ground.

**Fixtures, steps, and results:**

- **Defect 1 — combined fixture, non-shared files.** `base → A (a.txt) → B (b.txt)`, all unpublished;
  an uncommitted correction to `a.txt` (belonging to `A`) coexists with unrelated staged `u.txt`.
  *Reproduced the defect* first: applying the prior (`d6220f0`) procedure's single indiscriminate
  stash step hid both the correction and `u.txt` together; the correction was restored only after `A`
  and `B` were already rebuilt, leaving reconstructed `A` at `git show HEAD~1:a.txt` →
  `"A original content"` (uncorrected) with the fix sitting as a leftover unstaged diff on top of
  `B`. *Corrected procedure:* capture-patch → reverse-apply → stash `u.txt` alone → reset to `O~1` →
  reapply the patch → rebuild. Reconstructed `A` (`git show HEAD~1:a.txt`) returned
  `"A corrected content"`; `B` (`git show HEAD:b.txt`) returned `"B content"` unchanged; `u.txt`,
  restored via its recorded SHA, matched its original content and its original staged state
  (`A  u.txt`), and never appeared in either commit's diff.
- **Defect 1 — shared-file variant.** Same history shape, but the correction (line 1) and unrelated
  work (line 3) land in the *same* file, `shared.txt`, both initially unstaged, plus a second,
  wholly-unrelated staged file `u2.txt`. `git add -p` isolated the correction's hunk; `git diff -U0
  --staged` captured it; a first reverse-apply attempt without `--unidiff-zero` failed
  (`error: patch does not apply` — git rejects zero-context patches by default as a fuzz-match
  safeguard) and `--unidiff-zero` was required for both the reversal and the later reapplication.
  After reversal, `shared.txt` held only the unrelated line-3 change; both `shared.txt`'s unrelated
  hunk and `u2.txt` were then protected in one ordinary qualified-procedure stash. Reconstructed `A`
  (`git show HEAD~1:shared.txt`) held all three lines with only line 1 corrected
  (`CORRECTION-l1/l2/l3`); after restoration, `shared.txt`'s working tree showed the corrected,
  committed line 1 plus the unrelated line-3 change auto-merged back on top as an unstaged diff
  (matching its original unstaged state), and `u2.txt` returned staged, matching its original staged
  state.
- **Defect 1 — degenerate case (no unrelated content).** Same procedure run with no `U` at all: after
  the reverse-apply, the working tree was already clean, so the qualified stash-protection step's own
  clean-tree check (from the first pass) correctly created no entry, and none was restored at the
  end. Reconstruction still completed correctly.
- **Defect 1 — genuine conflict.** The correction's captured patch was reverse-applied against a tree
  where an unrelated edit had *overwritten the same line* (not merely sat nearby). The reversal failed
  cleanly (`error: patch failed` / `patch does not apply`); the working tree was left completely
  unmodified and the captured patch file remained on disk — confirming the "stop, do not guess, both
  the patch and the working tree remain the recovery data" behavior is backed by `git apply`'s actual
  all-or-nothing-per-file failure behavior, not merely asserted.
- **Defect 2 — SHA-vs-selector acceptance.** Confirmed directly: `git stash apply <SHA>` succeeded
  against a stash no longer at `stash@{0}`; `git stash drop <SHA>` on the same entry failed with
  `error: '<sha>' is not a stash reference`. This is the concrete basis for the corrected procedure's
  "apply accepts a bare SHA; drop does not, resolve first" instruction.
- **Defect 2 — identical messages, changing positions.** Two stash entries pushed with the *same*
  message (`"isolation-step"`) over different files, then a third, differently-named stash pushed
  afterward to shift positions further (final order: `stash@{0}`=third, `stash@{1}`=second
  same-message entry, `stash@{2}`=first same-message entry). Resolving each recorded SHA via
  `git stash list --format='%gd %H'` correctly identified each entry's true current position
  (`stash@{2}` and `stash@{1}` respectively) despite the identical messages and the shift. Applying
  and dropping the *first* entry by its resolved selector restored only that entry's own file content;
  the second same-message entry and the unrelated third entry were confirmed unaffected and still
  present (`git stash list` showed exactly two remaining entries, matching their recorded SHAs)
  afterward.
- **Defect 2 — unresolved identity.** A SHA that was never actually pushed (a fabricated value) was
  looked up against a live stash list; the matching lookup returned empty, cleanly and
  unambiguously distinguishing "not found" from a wrong guess — matching the corrected procedure's
  "stop and report, don't drop anything" instruction for this case. The real, unrelated entry present
  in the list was confirmed untouched by the failed lookup.
- **Defect 3 — composition with the mandatory per-commit isolation step.** In the non-shared combined
  fixture above, after committing reconstructed `A`, a second, concurrent qualified-stash entry (a
  distinct SHA, a distinct message) was created to isolate `A` for verification while the
  still-unrestored `U`-protecting entry from Defect 1's fix remained in the stash list at the same
  time. Both entries' SHAs were resolved and acted on independently and correctly — the isolation
  entry was applied, verified, and dropped without disturbing `U`'s entry, and `U`'s entry was later
  applied, verified, and dropped without any trace of the isolation entry's own content. This confirms
  the mandatory-isolation restatement composes cleanly with Defect 1/2's fixes rather than requiring
  a special case.

**Limitations:** the same file-scale, submodule, LFS, and binary-content limitations as the first
follow-up apply here. The shared-file variant used a 3-line file with a single-line correction hunk
and a single-line unrelated hunk on non-adjacent lines once zero-context patches were used; a
correction and unrelated content on directly adjacent lines within the same hunk boundary were not
separately exercised, and would likely surface as the same genuine-conflict path already validated
above rather than a silent misattribution, but that specific adjacency was not tested. `implement-it`
itself was not invoked in a live agent session for this pass either — only the underlying Git
mechanics were exercised, the same distinction the first follow-up record draws.

**Correction to the above limitation, superseded by the next section:** the claim that an untested
adjacent change "would likely surface as the same genuine-conflict path... rather than a silent
misattribution" was wrong, and is corrected, not merely extended, by the third follow-up below. Built
and executed against the exact adjacent, identical-text case that assumption described, the
zero-context reverse-apply this section validated did not conflict — it succeeded, silently, against
the wrong occurrence. The assumption was untested speculation about behavior this pass had not
actually run; the third follow-up runs it and reports what actually happened, per this document's own
"Turning these cases into future tests" guidance not to let a historical trace be quietly
reinterpreted as still-current fact.

## Follow-up correction: patch-capture attribution, index preservation, scratch-artifact location (2026-09-09c)

This section records a third, bounded correction against commit
[`caad9d3f89f273403b67b619dee4ab922c4a4a6b`](https://github.com/elieandraos/agentic-engineering/commit/caad9d3f89f273403b67b619dee4ab922c4a4a6b)
— the second IMP-05–08 follow-up above. Control Room accepted that pass's stable stash-SHA handling
and restored mandatory isolation verification for reconstruction (both preserved, unchanged, by this
pass). It found the patch-capture/removal sequence itself still unsound: three further reproduced
failures, all within the same two rule files. This section supplements, and does not replace, the
2026-09-08 audit or either earlier follow-up; their pinned source, observations, counts, and results
are unchanged except for the one correction stated immediately above.

**What each defect was, and what changed:**

1. **`git add -p` followed by a whole-path `git restore --staged <path>` cannot isolate a task
   correction from an unrelated hunk already staged in the same file** — `add -p` only ever shows the
   *unstaged* remainder, so if the correction is unstaged and unrelated content is already staged,
   selecting the correction's hunk leaves both staged together, and unstaging the whole path
   afterward discards the fact that the unrelated hunk had been staged at all. `commit-boundaries.md`
   replaces this with a capture procedure that never mutates the real index to find out what's
   already staged: it compares the real index's current blob for the path against `HEAD` and, when
   that blob cleanly represents either the correction or the unrelated content on its own, uses it
   directly (`git show :<path>`) — no staging or unstaging touches the real repository at all. Only
   when *nothing* is staged for that path does it interactively isolate the correction, and even then
   it does so against a private index copy (`GIT_INDEX_FILE=<scratch>/index git read-tree HEAD`,
   then `git add -p` against that copy), never the real one.
2. **A blanket zero-context patch reversal can silently apply against the wrong occurrence of
   identical-looking content, without ever reporting a conflict.** Reproduced with the exact fixture
   given: committed `"start\nsame\nmarker\nsame\nend\n"`, a staged correction turning line 4 into
   `"fixed"`, and an unstaged, adjacent insertion of a second, identical `"fixed"` line. The prior
   pass's `git apply --unidiff-zero -R` reverted line 4 (matched by raw line-number proximity, since
   zero context gives it nothing else to go on) instead of line 5, where the correction had actually
   ended up once the unrelated insertion shifted it down — producing
   `"start\nsame\nmarker\nsame\nfixed\nend\n"` with no error, no conflict, and no indication anything
   was wrong. `commit-boundaries.md` replaces zero-context patch application entirely with a real
   three-way merge (`git merge-file`), which is structurally aware of *which* content came from
   *which* side rather than pattern-matching lines, and — on this exact fixture — reports a genuine
   conflict (exit 1, `<<<<<<<`/`=======`/`>>>>>>>` markers) instead of guessing. The rule additionally
   requires a round-trip verification independent of the merge's own exit code: replaying the split
   pieces back together must reconstruct the original combined content exactly, or the split is not
   trusted regardless of what the merge command reported.
3. **A correction patch or any other capture artifact placed inside the repository worktree is
   exactly the kind of untracked content `git stash -u` removes** — the prior passes' patch files
   were written with no stated location, leaving this open. `commit-boundaries.md` now opens the
   reconstruction procedure by requiring an explicit, uniquely-named scratch directory *outside* the
   worktree (e.g. `mktemp -d`) for every recovery artifact the procedure creates, preserved until
   reconstruction is verified complete and removed only then — never on a failure.

A further defect, found only while executing the *combined* fixture rather than the capture step in
isolation, is also fixed here: restoring unrelated content that shares a file with the correction
cannot rely on `git stash apply`'s own restoration once the correction has been folded into a
reconstructed commit, because the file's committed content — the base the stash's own three-way merge
was taken against — has changed. `commit-boundaries.md` excludes such a path from the general
stash-based protection step and instead restores it with the same `git merge-file` technique, applied
against the path's new, reconstructed content rather than its old committed state.

**Tested state:** the corrected rule text as it exists in this working tree, built on top of
`caad9d3f89f273403b67b619dee4ab922c4a4a6b` on `main` (this pass's own changes land as ordinary new
commits after it, under the same non-rewrite boundary as the earlier passes).

**Method:** executed Git-mechanics verification only, in disposable repositories created and
discarded under a session scratch directory, never inside this project. `implement-it` itself was not
invoked in a live agent session for this follow-up — the same limitation the earlier follow-up records
state applies here too; nothing below should be read as a claim that the skill's own reporting, gates,
or human-facing behavior around this procedure were exercised.

**Fixtures, steps, and results:**

- **Defect 1 — full reconstruction and restoration, not just capture.** `base → A (f.txt) → B
  (b.txt)`, all unpublished; `f.txt` carries an already-staged unrelated hunk (`beta` →
  `UNRELATED-beta`) and a separate, unstaged correction hunk (`gamma` → `CORRECTION-gamma`), belonging
  to `A`. Capture: the real index's blob for `f.txt` was recognized as the unrelated hunk (not the
  correction), used directly (`git show :f.txt`); the correction was extracted via `git merge-file`
  (exit 0) and round-trip-verified (exact match) without ever staging, unstaging, or otherwise
  touching the real index. `f.txt` was reset to `head` content (excluding it from the general stash
  step); reconstruction produced `A` (`git show HEAD~1:f.txt`) containing the correction with the
  unrelated hunk absent, and `B` (`git show HEAD:b.txt`) unchanged. Restoration:
  a first attempt using the prior pass's ordinary `git stash apply --index` against `f.txt`'s
  protected content **failed outright** (`error: patch failed`, `error: conflicts in index`) because
  `f.txt`'s committed content had changed since the stash was taken — this is the further defect
  described above, caught only by running restoration all the way through rather than stopping at
  capture. The corrected procedure — `git merge-file` against the *new* reconstructed content, then
  staging the result because the unrelated content had originally been staged — produced
  `"alpha\nUNRELATED-beta\nmiddle1\nmiddle2\nCORRECTION-gamma\n"`, staged (`M  f.txt`), exactly
  matching both the correction and the unrelated content's original staged state.
- **Defect 2 — the exact adversarial fixture, old vs. new, with real commit history.** `base → A
  (f.txt) → B (b.txt)`; `f.txt`'s index held exactly the intended correction
  (`"start\nsame\nmarker\nfixed\nend\n"`); the working tree additionally carried the unrelated,
  adjacent, identical-text insertion (`"start\nsame\nmarker\nfixed\nfixed\nend\n"`). The prior pass's
  procedure, run faithfully against this fixture (correction already fully staged, so no `add -p`
  step applies), reproduced the reported silent corruption exactly:
  `"start\nsame\nmarker\nsame\nfixed\nend\n"`, with `git apply` reporting success. The corrected
  procedure's `git merge-file` extraction attempt on the same fixture returned exit 1 with explicit
  conflict markers; per the rule, this halts the procedure entirely — confirmed nothing in the real
  repository was touched (working tree still showed the original mixed state, no commits, no reset,
  no stash created) and all four captured artifacts (`head`, `known`, `combined`, the conflicted
  `other`) remained present in the scratch directory.
- **Defect 2 — non-adjacent case still succeeds cleanly (no regression).** The same `git merge-file`
  extraction, run against a variant with the correction and unrelated hunk separated by two unchanged
  lines, returned exit 0 with the exact expected content, and the round-trip check matched exactly —
  confirming the honest-conflict behavior is specific to genuine ambiguity, not a blanket refusal to
  merge adjacent-but-independent changes.
- **Defect 2 — round-trip check has real teeth.** A deliberately wrong "extracted" piece was fed
  through the round-trip reconstruction; it did not match the saved original combined content (and,
  separately, `git merge-file` itself flagged it as conflicting when the wrong piece was structurally
  incompatible) — confirming the verification step would catch a bad split rather than rubber-stamping
  whatever the merge command returned.
- **Defect 3 — scratch location survives `git stash -u`.** A file written to a `mktemp -d` directory
  outside a test repository's worktree was confirmed unaffected by `git stash push -u` run inside that
  repository — content and location unchanged — and was removed only after this was confirmed, not
  before.
- **Regression check — prior passes' combined and shared-file cases re-run under the new procedure.**
  The second follow-up's `base → A (shared.txt) → B (b.txt)` fixture — correction and unrelated
  content on non-adjacent lines of the same file, neither originally staged, plus a wholly separate
  staged unrelated file `u2.txt` — was rebuilt and run end to end under this pass's corrected
  procedure: private-index `add -p` isolated the correction without touching the real index;
  `git merge-file` extraction and round-trip verification both succeeded; the shared file was excluded
  from the general stash and restored via the new merge-based technique (unstaged, matching its
  original state); `u2.txt` was protected and restored via the unchanged, SHA-tracked qualified-stash
  procedure. Final state: reconstructed `A` held the correction alone
  (`git show HEAD~1:shared.txt` → `"CORRECTION-l1\nl2\nl3\n"`), `B` was unchanged, `shared.txt`'s
  working tree showed the correction committed plus the unrelated hunk restored unstaged, and `u2.txt`
  was restored staged — the same correct outcome the second follow-up validated, now produced by a
  mechanism proven not to fail on the case that mechanism previously could not have handled (a
  shared-file unrelated hunk surviving history rewriting).

**Limitations:** the same file-scale, submodule, LFS, and binary-content limitations as the earlier
follow-ups apply. The private-index capture path (nothing staged for the touched path at all) was
exercised only for a non-adjacent hunk pair, reusing the second follow-up's fixture; it was not
separately run against an adjacent or identical-text pair the way Defect 2's fixture exercises the
already-staged case — based on `git add -p`'s own hunk-splitting behavior this would likely surface as
an unsplittable-hunk stop rather than a silent misattribution, but, per the correction recorded above,
that expectation is now explicitly flagged as untested rather than asserted as established. A
correction spanning more than one file, with different capture branches applying to different files
in the same reconstruction, was not exercised — each branch was validated individually and in the
combined fixtures, but not in combination with a second, differently-shaped file in the same pass.
`implement-it` itself was not invoked in a live agent session for this pass either — only the
underlying Git mechanics were exercised, the same distinction the earlier follow-up records draw.

**Confirmation of the above limitation, by the next section:** the fourth follow-up below did exercise
the private-index capture path against the exact adjacent, identical-text pair this limitation flagged
as untested — and it surfaced exactly the predicted unsplittable-hunk stop (`git add -p` itself
reported "Sorry, cannot split this hunk"), not a silent misattribution. Unlike the correction recorded
after the second follow-up, this expectation held up under test.

## Follow-up correction: correction-vs-unrelated attribution in a three-way split (2026-09-09d)

This section records a fourth, bounded correction against commit
[`8ff0bd8e84bb3dfdb6f3aa29b2c1287b7002913d`](https://github.com/elieandraos/agentic-engineering/commit/8ff0bd8e84bb3dfdb6f3aa29b2c1287b7002913d)
— the third IMP-05–08 follow-up above. Control Room accepted that pass's SHA-based stash identity,
external scratch location, conflict handling, mandatory per-reconstructed-commit isolation
verification, and preserved Gate 1/2 and semantic-ownership rules (all unchanged, still, by this
pass). It found the third pass's own patch-capture replacement still unsound in one further way. This
section supplements, and does not replace, the 2026-09-08 audit or the three earlier follow-ups; their
pinned source, observations, counts, and results are unchanged except for the one confirmation stated
immediately above.

**What the defect was, and what changed:** the third pass's capture procedure recognized the real
index's current blob for a path as *either* "the correction" *or* "unrelated content," then extracted
whichever piece it didn't already have by subtracting the known piece from the combined working tree
and treating the remainder as automatically homogeneous. When a path carries *three* separately
changed regions — an unrelated hunk already staged, a second unrelated hunk still unstaged, and the
correction itself also unstaged — the real index correctly reads as "unrelated" (it holds only the
first hunk), but the remainder (combined minus that known unrelated hunk) is *not* homogeneous: it
contains the correction *and* the second, unstaged unrelated hunk together. The prior procedure
extracted that whole remainder and labeled it "the correction." The round-trip check the third pass
added still passed, because round-trip only confirms that the two pieces recombine to reproduce the
original content exactly — it says nothing about whether the pieces are correctly attributed, and a
mislabeled-but-complete piece round-trips exactly as cleanly as a correctly-labeled one.
`commit-boundaries.md`'s capture procedure is restructured so the correction is never derived by
subtraction: step 4 now interactively isolates the correction's own hunk(s) via `git add -p` against a
`HEAD`-seeded private index — the same technique the third pass already used only when nothing was
staged — applied uniformly regardless of what the real index already holds, so every hunk that differs
from `HEAD` for that path is individually reviewed and selected, never lumped into "whatever's left."
Step 5 then extracts only the unrelated-only complement (never the correction) via the same
`git merge-file` mechanism, and step 6 adds an explicit classification check — comparing the extracted
unrelated content against `HEAD` and the real index — that stops before any mutation whenever the
staged/unstaged shape of the unrelated content can't be represented by the single stage-or-unstage
restoration this recipe supports, rather than silently picking one. The round-trip check's own
description is corrected to state plainly what it proves — content recombination — and what it does
not — semantic ownership.

**Tested state:** the corrected rule text as it exists in this working tree, built on top of
`8ff0bd8e84bb3dfdb6f3aa29b2c1287b7002913d` on `main` (this pass's own changes land as ordinary new
commits after it, under the same non-rewrite boundary as the earlier passes).

**Method:** executed Git-mechanics verification only, in disposable repositories created and
discarded under a session scratch directory, never inside this project. `implement-it` itself was not
invoked in a live agent session for this follow-up — the same limitation every earlier follow-up
record states applies here too.

**Fixtures, steps, and results:**

- **The reported three-hunk defect, reproduced against the prior (third-pass) procedure.** One file,
  one commit history (`base → A → B`): an unrelated hunk already staged, a second unrelated hunk
  unstaged, and the correction (belonging to `A`) also unstaged. The prior procedure's real-index
  recognition correctly read the staged content as unrelated, then extracted "the rest" via
  `git merge-file` — exit 0, and the round-trip check passed exactly, while the extracted "correction"
  visibly contained the second, unstaged unrelated hunk's own marker text alongside the actual
  correction. This reproduces the report precisely: a passing round-trip on a wrongly-attributed
  split.
- **The same fixture under the corrected procedure.** Step 4's interactive selection, run against the
  full diff between a `HEAD`-seeded private index and the real combined working tree, presented all
  three changed regions as separate, individually selectable hunks (confirmed via `git add -p`'s own
  hunk count and content); selecting only the correction's hunk produced a private-index blob
  identical to `HEAD` except for that one change — no trace of either unrelated hunk. Step 5's
  extraction and round-trip both passed, correctly, against this now-accurate correction. Step 6's
  classification then compared the extracted unrelated content (both hunks combined) against the real
  index (holding only the first) and against `HEAD` — matching neither — and **stopped**, before
  clearing the path, creating any stash, or resetting anything. `git status`, `git log`, and
  `git stash list` afterward were unchanged from the fixture's starting state.
- **The mixed-index case: both the correction and unrelated content staged together, nothing further
  unstaged.** One file, correction and unrelated changes on different lines, both already staged in
  the same real-index blob. Step 4's interactive selection against the `HEAD`-seeded private index
  presented both regions as separate hunks despite both being staged together in the real index;
  selecting only the correction's hunk produced a clean, correction-only blob, confirming the
  technique isolates correctly even when the ambiguity originates in the real index rather than the
  working tree. Step 5 extracted the unrelated content cleanly (exit 0, round-trip exact). Step 6's
  classification compared it against the real index (which holds *both* changes) and against `HEAD`
  (which holds neither) — matching neither — and **stopped**, correctly identifying "an index
  containing both correction and unrelated changes" as an unsupported split, with the repository
  state unchanged.
- **Retained: successful end-to-end non-adjacent shared-file case.** The second follow-up's
  `base → A (shared.txt) → B (b.txt)` fixture — correction and unrelated content on non-adjacent
  lines of the same file, neither originally staged, plus a wholly separate staged unrelated file
  — was rebuilt and run completely under the corrected procedure: interactive selection isolated the
  correction cleanly; extraction and round-trip both passed; step 6's classification correctly
  resolved to "nothing was ever staged, restore unstaged" (not a stop, since this fixture has no
  staged/unstaged split to fail on); the shared file was excluded from the general stash and restored
  via the merge technique against the reconstructed content; the separate file was protected and
  restored via the unchanged, SHA-tracked qualified-stash procedure. Final state matched the second
  and third follow-ups' validated outcome exactly: `git show HEAD~1:shared.txt` held the correction
  alone, `B` was unchanged, the shared file's unrelated hunk was restored unstaged, and the separate
  file was restored staged.
- **Retained: the exact repeated-text fixture stops safely.** The second follow-up's adversarial
  fixture (`"start\nsame\nmarker\nsame\nend\n"` committed; the correction changing line 4 to `"fixed"`
  staged; an unstaged, adjacent insertion of a second, identical `"fixed"` line) was run against the
  corrected procedure's step 4. `git add -p` against the `HEAD`-seeded private index reported, on its
  own, "Sorry, cannot split this hunk" for the combined `-same`/`+fixed`/`+fixed` change — a stop
  intrinsic to the tooling, not merely asserted by this rule's own language, though the rule's
  language independently covers the case (identical candidate edits with no content-based way to
  choose between them) in case a future git version's splitter behaves differently. Declining the
  hunk and confirming repository state afterward showed no commits, no reset, and no stash — the same
  clean, unchanged state as the third follow-up's finding for this fixture, now reached through the
  new capture mechanism rather than the retired patch-based one.

**Limitations:** the same file-scale, submodule, LFS, and binary-content limitations as the earlier
follow-ups apply. The three-hunk and mixed-index fixtures used non-adjacent, non-identical hunks
(separated by enough unchanged context for `git merge-file` to extract cleanly once the correction was
known); a three-way split where the *unrelated* portions are themselves adjacent to, or textually
identical with, each other or the correction was not separately exercised — step 4's stop conditions
are expected to cover it on the same grounds validated for the two-way adversarial case, but that
specific three-way overlap was not run. A path where the correction spans more than one file, with a
mix of the four classification outcomes (no unrelated content, staged-only, unstaged-only, unsupported
mix) occurring simultaneously across those files in one reconstruction, was not exercised.
`implement-it` itself was not invoked in a live agent session for this pass either — only the
underlying Git mechanics were exercised, the same distinction every earlier follow-up record draws.

## Follow-up correction: document-it Artifact-template highlighter and mobile nav (2026-09-09e)

This section records a bounded correction pass against the three `document-it` `rules/template.html`
defects the audit above recorded as DOC-03/DOC-04 (High), DOC-05 (Low), and DOC-08 (Low). It
supplements, and does not replace, those original records — their pinned source, method, and
observations above are unchanged. Only `skills/document-it/rules/template.html` and this file were
touched; DOC-06 and DOC-07's Aligned results were re-run as regression checks, not changed.

**Starting source:** pinned commit `0087a07b83ebc02d75401f347afdf1107c11b660` on `main`.

**What changed, in `rules/template.html`:**

- The `<script>` highlighter's `//`-comment pass for `php`/`ts` previously ran as its own regex
  pass *before* the generic quoted-string pass, so a `//` occurring inside a quoted string (e.g. a
  URL) was matched and stashed as a comment first, stranding the string's closing quote inside that
  stash entry. The now-quote-less string regex then matched forward past the stash placeholder to
  the *next* real quote in the source, wrapping the earlier placeholder inside its own stash entry —
  a nested placeholder the single final restore pass (a one-shot, non-recursive `.replace`) cannot
  reach, leaking raw `\u0000`/`\u0002` characters into the rendered HTML and silently reclassifying
  part of the string as a comment. Fix: for `php`/`ts` only, comments and strings are now matched in
  one combined regex pass (`//[^\n]*` alternated with the three string forms), so whichever
  construct's start character is encountered first in left-to-right scanning — `//` or a quote —
  consumes to its own natural end before the other pass ever sees that text. `vue`/`json`/`http`
  (which have no comment syntax here) keep the prior string-only pass unchanged.
- The supported-language guard `if (!SUPPORTED[lang])` did a plain property lookup on a `{}` object
  literal, so a `data-lang` value that names an inherited `Object.prototype` member (e.g.
  `"constructor"`) resolved truthy and fell through into the enhanced-highlighting path meant only
  for the five real supported languages; `KEYWORDS['constructor']` is likewise inherited and not an
  array, so `kws.join(...)` threw, and the uncaught exception aborted the `for` loop over all
  `<pre>` blocks partway through — every block after the offending one, not just that one, was left
  un-highlighted. Fix: the guard now uses
  `Object.prototype.hasOwnProperty.call(SUPPORTED, lang)`, which is true only for `SUPPORTED`'s own
  five keys, so any inherited-property label (or a missing `data-lang`) takes the plain-text
  fallback instead of the enhanced path.
- `.nav`'s mobile-width overrides (`position: static`, `border-right: none`, `border-bottom: ...`)
  were declared inside a `@media (max-width: 880px)` block positioned *before* the base `.nav { ...
  }` rule. Because both selectors are the plain class `.nav` (identical specificity), the later base
  rule's `position: sticky` and `border-right: 1px solid var(--border)` won the cascade at every
  width, including ≤880px — only a second, separate mobile block after the base rule (setting just
  `height: auto`) actually took effect. Fix: the base `.nav` rule now keeps its original desktop
  declarations unchanged, and a single mobile override block — `position: static`, `height: auto`,
  `border-right: none`, `border-bottom: 1px solid var(--border)` — was moved to directly follow it,
  so it now wins the cascade at ≤880px as originally intended; the `.shell` mobile override
  (unaffected by this bug, since no later `.shell` rule competes with it) was left in place.

**Method:** two independent checks, kept separate as the task requires:

1. **JavaScript/DOM-stub execution (Node, no browser).** The same in-memory harness documented under
   "Repeating the executed template cases" above — it extracts the shipped `<script>` verbatim from
   `template.html` and runs it via `new Function("document", script)` against a minimal
   `getAttribute`/`querySelector`/`textContent`/`innerHTML` stub, with no real DOM, no
   `document-it` invocation, and no Artifact publish. It was first run unmodified against
   `template.html` as it existed at the pinned starting commit to reproduce DOC-03/04/05, then run
   again against the corrected file in this working tree, extended with new fixtures for the
   validation items this task called for: escaped quotes, a comment marker inside a string, a quote
   inside a `//` comment (both `ts` and `php`), HTML-sensitive characters (`<`, `>`, `&`) alongside a
   comment and a string, a missing (`null`) `data-lang`, and one representative snippet for each of
   the five supported languages (`php`, `ts`, `vue`, `json`, `http`). Every case additionally
   round-trips the produced HTML back to source — stripping the generated `<span class="...">` tags
   and reversing `escapeHtml`'s three entity substitutions — and asserts the result equals the
   original fixture text exactly. This is a stronger check than reading a DOM stub's unchanged input
   `textContent` back: it decodes the actual highlighter *output* and verifies no character was
   dropped, duplicated, or left as an unresolved placeholder.
2. **CSS cascade — source inspection only, with a stated tool limitation.** The Chrome browser
   extension (`claude-in-chrome`) reported "not connected" when queried for a tab context in this
   session, and no headless browser (Playwright, Puppeteer) was available locally without a network
   package install, which was out of scope for this bounded correction. The `.nav`/`.shell` cascade
   at 375px, 800px, and desktop widths was therefore verified by manual source inspection: enumerating
   every rule that can set a `.nav` property, in file order, confirming all such selectors share the
   same specificity (a single class selector), and resolving each property to whichever declaration
   is later in source order and applicable at the given width — the standard cascade tie-break CSS
   applies when specificity is equal. **This is a source-inspection result, not a browser-rendered or
   computed-style result**, and should be re-verified against actual computed styles (e.g. via
   `getComputedStyle` in a connected browser tab) before being treated as a full substitute for visual
   confirmation.

**Reproductions (against the unmodified pinned template):**

- DOC-03 (`ts`, `const url = "https://example.com";\nconst mode = "safe";`): no thrown error;
  output `<span class="tok-keyword">const</span> url = <span
  class="tok-string">"https:\u00000\u0002\nconst mode = "</span>safe";` — an unresolved
  `\u0000`/`\u0002` placeholder pair present, and decoding the spans back to source yields
  `const url = "https:\u00000\u0002\nconst mode = "safe";`, not the original text. Matches the
  DOC-03 record above exactly.
- DOC-04 (`php`, `$url = "https://example.com";\n$mode = "safe";`): same shape of failure —
  `<span class="tok-var">$url</span> = <span class="tok-string">"https:\u00000\u0002\n$mode =
  "</span>safe";`, unresolved placeholder present. Matches the DOC-04 record above exactly.
- DOC-05 (`data-lang="constructor"` block followed by an ordinary `ts` block): threw `TypeError:
  kws.join is not a function`; both blocks' `innerHTML` remained empty (`""`), including the
  well-formed `ts` block after it. Matches the DOC-05 record above exactly.

**Corrected results (against `rules/template.html` in this working tree):**

- DOC-03: `<span class="tok-keyword">const</span> url = <span
  class="tok-string">"https://example.com"</span>;\n<span class="tok-keyword">const</span> mode =
  <span class="tok-string">"safe"</span>;` — no error, no unresolved placeholder, decodes back to
  the exact original source.
- DOC-04: `<span class="tok-var">$url</span> = <span
  class="tok-string">"https://example.com"</span>;\n<span class="tok-var">$mode</span> = <span
  class="tok-string">"safe"</span>;` — same result shape, source fully preserved.
- DOC-05: `constructor` block falls back to `x &lt; y` (escaped plain text, no throw); the
  following `ts` block still highlights normally (`<span class="tok-keyword">const</span> ok =
  true;`) — no longer aborted by the earlier block.
- DOC-06 (regression, python fallback) and DOC-07 (regression, JSON) re-run unchanged from their
  original Aligned results: no error, no unresolved placeholder, source preserved.
- New checks — escaped quotes, a comment marker inside a string, and a quote inside a `//` comment
  (`ts` and `php`) — all produced no error, no unresolved placeholder, and an exact source
  round-trip; a `"http://foo"` string followed by a real trailing `// comment` correctly separated
  the two (string tagged `tok-string`, comment tagged `tok-comment`, nothing swallowed either way).
  HTML-sensitive characters (`<`, `>`, `&`) round-tripped correctly through both the plain-text
  fallback and the enhanced path. The `null`/missing-`data-lang` fixture fell back to escaped plain
  text with no error. One representative snippet per supported language (`php`, `ts`, `vue`, `json`,
  `http`) each highlighted without error and round-tripped to its exact source text.
- `git diff --check` against the changed file reported no whitespace errors (clean exit).

**Limitations:** the JavaScript checks are Node `new Function` execution of the shipped script
against a minimal object stub, as defined in "Repeating the executed template cases" above — not a
live `document-it` invocation, not a rendered page, and not a published Artifact; DOM APIs beyond
`getAttribute`/`querySelector`/`textContent`/`innerHTML` were never exercised. The CSS mobile-nav
check is source inspection, explicitly not browser-rendered or computed-style verification, because
the Chrome extension was unavailable and no headless browser was installed for this bounded pass —
treat the DOC-08 fix as unverified in an actual browser until that gap is closed. Fixtures remain
small, hand-written snippets, not a fuzz corpus or the full breadth of each language's syntax; no
attempt was made to exercise nested-quote edge cases beyond one level (e.g. a `php` `#[...]`
attribute containing an unterminated string), since that interaction predates this pass and was not
part of the recorded DOC-03/04/05/08 defects.

## Follow-up correction: document-it Artifact-template PHP attribute ordering (2026-09-09f)

This section records a bounded correction pass against a fourth `rules/template.html` highlighter
defect, reported directly (not from a prior audit pass): the PHP `#[...]` attribute regex still ran
as its own pass *before* the DOC-03/04 combined comment/string pass added in the prior follow-up
above, so `#[...]`-shaped text inside a real `//` comment or a real quoted string was matched and
stashed as an attribute before that surrounding construct was protected — reproducing the same
nested-placeholder failure mode DOC-03/04 fixed, now triggered by the attribute pass instead of the
old separate comment pass. It supplements, and does not replace, the prior two follow-up records —
DOC-03/04/05/08's fixes and checks above are unchanged and were re-run as regressions. Only
`skills/document-it/rules/template.html` and this file were touched.

**Starting source:** commit `23ea271` on `main` (the prior follow-up's own commit).

**Fixtures (both requested regressions, IDs DOC-09/DOC-10, plus a combined and two preservation
checks):**

- DOC-09 — `#[...]`-shaped text inside a real comment: `php`, `// See #[Example] before changing
  this.`
- DOC-10 — `#[...]`-shaped text inside a real string: `php`, `$example = "#[Example]";`
- CHECK-attribute-comment-string-combined — both lines together in one block, exactly as reported:
  `// See #[Example] before changing this.\n$example = "#[Example]";`
- CHECK-attribute-genuine — a real attribute must still highlight as one unit:
  `#[Route('/users')]\nfinal class UserController\n{\n}`
- CHECK-attribute-nested-brackets — the existing one-level-nested-bracket case
  (`#[Authorize('x', [A::class, 'b'])]\nfunction f() {}`) must still resolve as a single attribute
  match, not stop early at the array's own closing bracket.

**What changed, in `rules/template.html`:** the standalone `if (lang === 'php') { ... #[...] ...
}` pass was removed, and its pattern was added as a third alternative — ahead of the `//` and
string alternatives, php-only — to the same combined regex the prior follow-up introduced for
comments and strings. The classification callback now checks the match's first character (`#` for
an attribute, `//` for a comment, otherwise a string) instead of just the first two. Leftmost-match
scanning then guarantees the same property this fixed for comments and strings: whichever
construct's start character is encountered first in the source consumes to its own natural end, so
`#[...]`-shaped text inside a comment or string can no longer be read as a real attribute, and (as
before) a `//` inside a string still can't be read as a comment. Runtime comments were tightened to
one or two lines pointing here for the mechanism; this record carries the defect history instead of
the script.

**Method:** the same DOM-stub harness used in the two prior follow-ups (`new Function("document",
script)` against a minimal `getAttribute`/`querySelector`/`textContent`/`innerHTML` stub extracted
from the shipped `<script>` — no real DOM, no `document-it` invocation, no Artifact publish), first
run unmodified against the template as committed at `23ea271` to reproduce the defect, then run
again against the corrected file in this working tree together with every fixture from the prior two
follow-ups (DOC-03 through DOC-10 plus all `CHECK-*` cases) as a full regression pass. Every case
round-trips the produced HTML back to source (strip the generated spans, reverse `escapeHtml`'s
entity substitutions) and asserts exact equality with the original fixture text — the same
stronger-than-`textContent` check used previously.

**Reproduction (against `23ea271`, unmodified):**

- DOC-09: no thrown error; output
  `<span class="tok-comment">// See ` + NUL + `0` + STX + ` before changing this.</span>` — the
  attribute's own `<span class="tok-comment">#[Example]</span>` stash entry never gets substituted
  back in; decoding yields `// See ` + NUL + `0` + STX + ` before changing this.`, not the original
  text. (NUL/STX here are the same U+0000/U+0002 marker characters DOC-03/04 identified, written out
  rather than embedded literally in this file.)
- DOC-10: same failure shape —
  `<span class="tok-var">$example</span> = <span class="tok-string">"` + NUL + `0` + STX +
  `"</span>;`, unresolved marker present, `#[Example]` lost from the visible/decoded text.
- CHECK-attribute-comment-string-combined (both lines together): both failures occur in the same
  block, one unresolved marker per line, confirming the interaction reproduces when the two lines
  share a single highlighter pass exactly as reported.
- CHECK-attribute-genuine and CHECK-attribute-nested-brackets both already passed at this commit —
  the defect is specific to `#[...]`-shaped text appearing inside a comment or string, not to
  genuine attribute recognition, which the fix must not regress.

**Corrected results (against `rules/template.html` in this working tree):**

- DOC-09: `<span class="tok-comment">// See #[Example] before changing this.</span>` — no error, no
  unresolved marker, decodes back to the exact original source.
- DOC-10: `<span class="tok-var">$example</span> = <span class="tok-string">"#[Example]"</span>;` —
  same result shape, source fully preserved.
- CHECK-attribute-comment-string-combined: both lines correct in one pass, matching the two
  single-line results above.
- CHECK-attribute-genuine: `<span class="tok-comment">#[Route('/users')]</span>` followed by the
  `final class UserController` declaration highlighting normally — genuine attribute recognition
  preserved.
- CHECK-attribute-nested-brackets: `<span class="tok-comment">#[Authorize('x', [A::class,
  'b'])]</span>` resolves as one match through the nested `[...]`, exactly as before this pass.
- Full regression: every DOC-03 through DOC-10 fixture and every `CHECK-*` fixture from this and the
  prior follow-up passed together in one run (23 cases, no error, no unresolved marker, exact
  round-trip on every non-empty result).
- `git diff --check` against the changed file reported no whitespace errors (clean exit).

**Limitations:** same as the prior follow-up — DOM-stub Node execution, not a live `document-it`
invocation, rendered page, or published Artifact; the CSS mobile-nav (DOC-08) verification remains
source inspection only, unchanged by this pass since no browser tooling became available in the
interim. Fixtures are still hand-written, not a fuzz corpus; attribute recognition inside a
`` ` ``-delimited template-literal string, and an attribute immediately adjacent to (rather than
inside) a string or comment with no separating whitespace, were not separately exercised.

## Follow-up correction: review-it description metadata, context-consumption measurement (2026-09-09g)

This section records a bounded correction against the META-01 defect the 2026-09-08 audit above
recorded: `skills/review-it/SKILL.md`'s frontmatter `description` exceeded the Agent Skills
specification's 1,024-character limit. It supplements, and does not replace, that original
record — META-01's pinned source, method, and observation above are unchanged. This same pass also
produced [`docs/skill-context.md`](docs/skill-context.md), the new dated home for context-consumption
measurements referenced from each skill's `README.md`, and reconciled `artifacts/implement-it.md`
and `artifacts/document-it.md` against the approved Git-repair and Artifact-template corrections
recorded in the follow-up sections above; those changes are not repeated here in detail.

**What changed:** the description was rewritten from **1,219 to 966 characters**. The ten-category
checklist enumeration and the "every finding is verified... distinguished from an unresolved
limitation" clause were removed — that detail already lives in the skill's body and in
`rules/checklist.md`/`rules/verification.md` — while the purpose statement, the three discovery
triggers (review implemented code, review a branch or PR, verify a correction before it's relied
on), standalone and invoked availability (callable standalone with no prior `implement-it` session
or `plan-it`-authored issue required; also callable by `implement-it` before Gate 1 and during an
authorized delivery correction), and the reports-only ownership boundary (never fixes application
code, never mutates GitHub or other live/production state, every correction returns to
`implement-it`; does not own guide, issue/plan-synthesis, investigation, or commit-plan review) are
all preserved, checked by direct comparison against the original 1,219-character text.

**Method:** the same programmatic measurement META-01 used — extracting the frontmatter
`description` field with a regular expression and measuring its length — re-run against the
corrected file (966 characters, within the 1,024 limit) and against all seven `SKILL.md` files'
frontmatter, confirming each has exactly `name` and `description` (no new metadata fields,
invocation controls, or dependencies were introduced or found), each `name` matches its directory,
and that `review-it` was the only one that had ever exceeded the limit. Markdown link resolution was
programmatically re-checked for every file this pass touched (`docs/skill-context.md`, the seven
skill `README.md` files, `skills/review-it/SKILL.md`, and `artifacts/implement-it.md` /
`artifacts/document-it.md`), and `git diff --check` reported no whitespace errors against the full
changed set.

**Result:** META-01 is corrected; `review-it`'s description is now 966 characters, with its meaning
and discovery triggers intact by direct comparison against the original text. This does not reopen
or alter the original audit's counts (27 aligned, 18 defect, 2 gaps) — this is one follow-up
correction to one already-recorded defect, the same pattern as the IMP-05–08 and `document-it`
template follow-ups above.

**Limitations:** this pass measured description length and link resolution programmatically; it did
not invoke any Agent Skills loader or a live coding-agent session to confirm the corrected
frontmatter actually parses and activates correctly at runtime — that remains the same category of
gap the original audit's "Measured" method rows already disclose.
