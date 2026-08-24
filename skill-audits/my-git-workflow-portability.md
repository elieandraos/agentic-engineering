# My Git Workflow Portability Audit

## Audit metadata

- Phase D supporting audit.
- Target skill: `my-git-workflow`.
- Audit date: 2026-08-24.
- Canonical skill commit analyzed: `4b759ccb9d90e8a6c3db11fc603842d4bee1741e`.
- Consumer snapshot (`useOrbit/.claude/skills/my-git-workflow/`) was not refreshed during this audit.
- This document records analysis only; no skill changes were made as part of the audit.

---

## Audit method

This section documents the reusable procedure that produced the findings below, so the same method
can be applied to other Agentic Engineering skills in a later pass. It is a general audit method, not
a transcript of the specific questions asked to produce this particular audit.

### Scope

Inspect the complete target skill, not just files a prior pass already flagged:

- `SKILL.md` — the skill's own description of what it does, when it triggers, and what it owns.
- `README.md` — the skill's narrative self-description, read independently of `SKILL.md` since the
  two can drift (one staying portable while the other accumulates project narrative).
- Every file under `rules/`, `references/`, and any templates or worked examples the skill ships.
- Cross-skill references and dependencies — where this skill assumes another skill exists, defines a
  term, or owns a boundary.
- Relevant originating-project evidence, read directly, whenever the skill makes a concrete claim
  about that project (an issue's shape, a repository's release history, a file's current contents) —
  not taken on the skill's word alone when the claim materially affects portability.

A prior audit having already cleared a file is not a reason to skip it — re-read every file fresh,
because defects can hide outside the file a previous pass was scoped to (a stack-specific term can
leak into a *different* rule file than the one already fixed).

### Evidence inspection

For every concrete project reference found:

- Follow the citation to its actual source rather than trusting the skill's paraphrase of it.
- Verify issue numbers, URLs, file paths, class/method names, commands, and historical claims against
  the originating repository where that repository is available for inspection.
- Distinguish a *current* source (something a reader could still go look at) from a *historical*
  source (something true only at extraction time, which may since have changed or been removed).
- Inspect external dependencies (a CLI, an API, a platform convention) closely enough to know whether
  they affect the skill's actual behavior, not just whether they're mentioned.
- Do not accept the skill's own description of a reference at face value when that reference's
  accuracy materially affects whether the skill is portable — check the underlying source.

### Reference classification

Classify each significant concrete reference into exactly one of:

1. **Portable methodology** — the rule itself is stack/project independent.
2. **Useful empirical evidence** — a real historical example that helps explain or validate a rule
   and is worth retaining.
3. **Project-specific rule** — a convention that only makes sense in the originating project.
4. **Project-specific example** — an example retainable only if clearly framed as originating-project
   evidence rather than as the rule itself.
5. **Stack/tooling fact** — a concrete implementation mechanism that should be isolated from the
   surrounding methodology, not asserted as if it were universal.
6. **External dependency** — capability owned outside the skill (and outside Agentic Engineering
   generally) that the skill assumes without redefining.
7. **Stale or misleading material** — a claim no longer true, or one likely to mislead a new reader.
8. **Unnecessary noise** — a concrete detail that does not materially improve the methodology either
   way.

"Concrete" is not itself a defect. The classification determines the right treatment, not whether the
reference survives.

### Self-contained reader test

Apply this question to each meaningful reference:

> Can a developer who has never seen the originating project understand the rule completely without
> knowing its project history, issue structure, architecture, naming, or conventions?

If yes, state why the reference is harmless or actively useful as-is.

If no, identify precisely what contextual dependency remains, and judge whether that dependency is
legitimate (e.g., the skill explicitly and deliberately assumes a named platform) or should be
removed, reworded, or separated from the portable rule it's currently fused to.

### Example treatment

Do not remove a concrete example merely because it originated in one project. For each example,
determine whether it should:

- remain, explicitly labeled as empirical evidence from the originating project;
- be generalized, so the specific fact is replaced by the general pattern it was an instance of;
- be rewritten as a synthetic, stack-agnostic teaching example;
- be separated — kept as evidence, but structurally distinguished from the portable rule it currently
  sits inside;
- be replaced, because it is stale or actively misleading; or
- be removed outright, because it adds no reusable teaching value even as labeled evidence.

The default posture favors retention with clearer framing over deletion — historical evidence is what
grounds a methodology skill in something real rather than a guess, and losing it is a real cost.

### Boundary analysis

Across the skill as a whole, distinguish:

- reusable rule from the empirical evidence used to support it;
- methodology (what to do, and why) from implementation (how one specific project happened to do it);
- reusable knowledge from a project's own convention;
- a stack fact from the portable principle it happens to be evidence for;
- a capability the skill genuinely owns from an external dependency it merely assumes and builds on
  top of.

### Quality checks

Independently of the classification pass, scan the whole skill for:

- hidden project coupling (a rule that silently only works given one project's history or state);
- hidden stack/tooling coupling (a rule that silently only works given one toolchain);
- stale references (a citation to something that has since changed, moved, or been removed);
- contradictory guidance (two rules, or a rule and its own evidence, pointing different ways);
- duplicated responsibility (two files or two skills quietly claiming the same ground);
- unexplained external dependencies (a tool or platform assumed without ever being named as such);
- examples that require originating-project context to parse at all;
- rules that cannot be understood independently of a sibling file or another skill, where that
  dependency isn't itself declared.

### Output method

Produce, in this order:

1. Executive verdict.
2. File-by-file audit.
3. A concrete reference inventory (table: file, reference, classification, whether it's needed for
   understanding, current treatment, recommended treatment).
4. Strong examples worth preserving, with the framing that keeps them from becoming hidden
   dependencies.
5. Problematic references, named specifically.
6. Structural implications — whether the evidence justifies a consistent structural convention (e.g.,
   a labeled "evidence" section), assessed rather than assumed.
7. Readiness conclusion — what, concretely, must change before the skill is a clean, reusable,
   self-contained methodology.

Keep observed facts (what the text says, what the source confirms), classification judgments (which
of the eight categories a reference falls into and why), and open questions (things this pass could
not resolve, e.g. because the originating source wasn't checkable) visibly distinct from each other
throughout — a reader should be able to tell which of the three they're looking at without inferring
it from tone.

Do not introduce a numeric score as part of this method. A prior score, if one already exists for the
skill from a different process, is a separate artifact this method does not reproduce or update — this
method's job is to state what a score would mean in concrete, actionable terms, not to produce a new
one.

The purpose of the whole method is a single question: can a developer or team reuse this skill without
prior knowledge of the project it was extracted from? Every step above exists to answer that question
with evidence rather than impression.

---

## Audit findings

The section below is the complete, unedited audit report produced by applying the method above to
`my-git-workflow` at commit `4b759ccb9d90e8a6c3db11fc603842d4bee1741e`. It is reproduced in full, with
its own verdict, findings, and conclusions preserved exactly as originally written — including where
its judgments are specific to this one audit pass rather than restatements of the general method above.

---

# Portability/Readability Audit — `my-git-workflow` (canonical, `main` @ `4b759cc`)

Analysis only. No files modified.

---

### 1. Executive verdict

**Portable with targeted cleanup needed** — narrower than before, but not zero.

The `verification.md` refinement from the prior pass holds up: re-reading it fresh, all three previously-embedded stack citations (Pest/Pint commands, `skipUnlessFortifyHas()`) are now correctly boxed under `release.md`'s "What this repository's evidence shows" pattern, and the surrounding rule prose reads as genuinely stack-agnostic. That file is no longer a problem.

But auditing the *whole* skill fresh (not just the file Phase C already flagged) turns up three more instances of the same underlying pattern — smaller, more isolated, but real:

1. `rules/review-gates.md` still names "Pint" directly inside Gate 1's generic reporting instruction — unboxed, missed by every prior Phase C iteration because they were reading with `verification.md` as the lens.
2. `rules/milestone-completion.md`'s definition of "what counts as a delivery/phase milestone" is worded so that a project-specific naming convention (`Phase NN — {Feature Name}`) reads as part of the definition itself, not clearly as an example of it.
3. `rules/sequencing.md` has one ambiguous "this project" reference that isn't wrong, but isn't self-locating either.

None of these require a rewrite. Each is a sentence-level fix, same class of problem `verification.md` had, same fix pattern already proven twice in this skill. The skill does not say "here's how useOrbit did X, therefore this is the rule" anywhere I found — every rule is stated generically first, with evidence following, essentially everywhere. The gaps are places where a *specific term* leaked into general prose without its own box, not places where the *reasoning* is project-bound.

---

### 2. File-by-file audit

#### `SKILL.md`
**Verdict:** Portable, one soft spot.
- **Project-specific references:** `#288/#287/#120/#289`, PR `#298`, `v0.17.0`, "Phase 22" — all inside a single parenthetical clause per mention: `(see rules/commit-boundaries.md for the v0.1 evidence: ...)`. Consistently bracketed as *evidence for* a rule already stated in generic terms immediately before it. This is the cleanest citation style in the file.
- **Stack/tooling references:** the frontmatter's "Always load ALONGSIDE this project's implementation skills (my-laravel-patterns, laravel-best-practices, pest-testing, my-phpstorm-conventions, inertia-vue-development, fortify-development, wayfinder-development, etc. as the code demands)" names five Laravel-stack skills concretely. Correctly scoped by "this project's" and "etc. as the code demands," but never states outright that a different-stack consumer loads *their own* equivalent list — implied, not said.
- **External dependencies:** GitHub issues/PRs/milestones assumed throughout — but this is declared in the skill's own first sentence ("moving an already-approved GitHub issue..."), so it's a stated scope boundary, not a hidden leak.
- **Historical examples:** the "Left for later versions" section's branch-naming discussion (`feature/organization-owner-provisioning`) is a model of correct self-labeling — "That's one data point, not a pattern... Do not generalize."
- **Problematic references:** none rise to blocking; the implementation-skills list is the only soft spot.
- **Recommended treatment:** leave as-is, or add one clause making the stack-substitution explicit ("...as the code demands — a project on a different stack loads its own equivalent implementation skills here").

#### `README.md`
**Verdict:** Portable, heavier narrative weight than `SKILL.md` but same discipline.
- **Project-specific references:** the issue-shape table (`#288/#287/#120/#289`), PR `#298`, `v0.17.0`, "Phase 22 — Authentication & 2FA," `SecurityTest.php`, "Fortify TOTP," `organizations:provision`. Every instance is introduced with "the evidence," "extracted from," or "this repository's own..." — rule-then-evidence order is consistent, never evidence-then-implied-rule.
- **Notably already-generic:** the "Verification, at the right scope" section (lines 95–107) never names Pest/Pint/Fortify/Artisan at all — it describes the stash-based technique in fully generic terms (`git stash push -u`, "run the full suite") and cites only the issue numbers and `SecurityTest.php` as evidence. This section was *not* touched in the prior `verification.md` pass and didn't need to be — worth noting as a positive data point, not a gap.
- **Stack/tooling references:** minimal — "Fortify TOTP," `organizations:provision` appear once, inside the release-altitude drafting example, explicitly framed as "the evidence for the gap between 'technically accurate' and 'release-level.'" That's the rule's whole point (implementation language reads wrong at release altitude) — the Laravel-specific terms are the *bad example* the rule warns against, so their presence is load-bearing, not a leak.
- **External dependencies:** `gh` mentioned once ("A `gh` command's exit code is not proof"), generic usage.
- **Historical examples:** the same branch-naming self-labeling as `SKILL.md`, restated.
- **Problematic references:** none found requiring change.
- **Recommended treatment:** no change needed.

#### `rules/commit-boundaries.md`
**Verdict:** Portable core, evidence used correctly throughout.
- **Project-specific references:** `#288/#287/#120/#289/#291`, plus class names in the worked commit-message example (`ResetTwoFactorAuthenticationAction`, `organizations:reset-owner-two-factor`) and `OrganizationPolicy`.
- **Self-contained reader test:** Passes. The evidence table (line 15–20) states shapes and commit counts as data, with the general rule ("Neither shape is the default... the diff decides") stated independently of the table. The full example commit message (lines 92–100) is understandable purely as a *shape* — title, body, `Refs #N` trailer — without knowing what a "2FA reset" or `ResetTwoFactorAuthenticationAction` is.
- **Stack/tooling references:** one incidental "turn the Fortify feature on" inside a quoted example commit-message fragment — evidence, not instruction.
- **Problematic references:** none.
- **Recommended treatment:** no change.

#### `rules/issue-closure.md`
**Verdict:** Portable, strongest evidentiary discipline in the skill.
- **Project-specific references:** `#288/#287/#120` (closure recipe evidence), `#289` (explicitly marked as *not* evidence for closure, since it hadn't gone through closure yet at extraction time — a genuinely strong piece of methodological self-awareness: "Only cite an issue as evidence for a workflow rule once that part of its lifecycle has actually occurred").
- **External dependencies:** `gh issue view/edit/comment/close` — used as literal commands throughout the four-part recipe. This is GitHub CLI syntax embedded directly into procedural steps, not boxed as "evidence" — but see the dependency discussion below: this is arguably correct, since `gh` *is* the mechanism, not an example of one, for a skill whose whole premise is a GitHub issue.
- **Self-contained reader test:** Passes for the recipe's shape (check tasks → comment → close → validate). A reader without `gh` installed would need to substitute their own tracker's API, but the *procedure* — persist, mutate, re-fetch, confirm — is fully transferable, and "check off completed Tasks" etc. isn't Laravel- or useOrbit-specific.
- **Recommended treatment:** no change to content; see the structural recommendation (§6) on naming `gh`/GitHub as an explicit dependency once, skill-wide, rather than per-file.

#### `rules/milestone-completion.md`
**Verdict:** Portable with one definitional wording issue.
- **Problematic reference (new finding):** line 39–40 — `"A delivery/phase milestone represents a bounded body of work intended to ship as a release — this project's `Phase NN — {Feature Name}` convention (`my-feature-planning`'s `rules/issue-conventions.md`)."` The em-dash clause reads ambiguously: is the naming convention illustrating the definition, or is it part of the definition (i.e., does a milestone have to be literally named `Phase NN — Feature Name` to qualify)? A reader unfamiliar with useOrbit could reasonably conclude the rule only applies to milestones following that literal syntax, which isn't the intent — the actual test is the general clause before the dash.
- **Project-specific references:** the "Forward-looking only" section's claim that "this project's full milestone history... showed every milestone ever created left open" is clearly framed as *why this rule was deliberately decided rather than extracted* — a genuinely useful piece of context (explains why this one rule departs from the skill's otherwise "extract from evidence" method) and already well self-labeled.
- **External dependencies:** `gh api repos/{owner}/{repo}/milestones/{number}` commands, `gh issue list --milestone "Phase 23" --state open` (placeholder example, harmless).
- **Historical examples:** the "every milestone was left open" finding is a strong, well-used piece of evidence — it's cited to justify *why* the rule departs from the skill's own norm, not to justify the rule's content.
- **Recommended treatment:** reword the "What counts as a delivery/phase milestone" definition so the general clause stands alone as the test, and the naming convention is clearly marked as this project's example of it (same fix shape as `verification.md`, one sentence).

#### `rules/release.md`
**Verdict:** Genuinely clean — the model file, confirmed on a full re-read.
- **Project-specific references:** all under two explicit `### What this repository's evidence shows` headings (policy discovery: tags/GitHub Releases/no automation; publish mechanism: the exact `git tag`/`gh release create` sequence), plus a shape-classification table (`v0.13.0 — Carriers`, `v0.11.1 — Tags Infrastructure`, etc.) explicitly introduced as "this repository's own history is the evidence for that range, not a hypothetical."
- **Self-contained reader test:** Passes cleanly. Every numbered step states the portable rule first ("discover... do not assume...", "never derive version importance from commit/file/line count") with the repository's actual answer boxed separately and explicitly disclaimed ("not a rule to carry into a project whose evidence points somewhere else," "an adapter fact for this repository, not a template to reuse verbatim").
- **Recommended treatment:** none — this is the file the other six should be measured against, and now `verification.md` matches it.

#### `rules/review-gates.md`
**Verdict:** Portable with one leaked term (new finding).
- **Problematic reference (new finding):** line 12 — `"Report what changed and how it was verified — files touched, a short description of the approach, the test/Pint results — and wait."` "Pint" is a Laravel-specific formatter named directly inside Gate 1's generic reporting checklist, with no box, no evidence label, and no cross-reference to `verification.md`. This is exactly the class of problem `verification.md` had — a stack term stated as if it were universal — just smaller (one word) and in a different file, which is why three passes of Phase C (all scoped by their own account to `verification.md`) never caught it.
- **Self-contained reader test:** Fails narrowly here — a reader unfamiliar with Laravel would not know what "Pint results" means, though they could infer "some formatting-tool output" from context. Everything else in the file passes.
- **Project-specific references:** `#289` (Gate 2 sequencing example), `#287` (the 13-route-groups/8-files architecture-contradiction example) — both are genuinely strong, self-contained illustrations of the abstract point they're attached to (see §4).
- **Minor noise:** `gatherMiddleware()` (line 60) — a specific Laravel `Router` method cited parenthetically as evidence of "investigated with evidence." Understandable without knowing the method (the surrounding clause already says what it's for: "resolving real route middleware"), so it doesn't block comprehension — borderline unnecessary specificity, not a blocker.
- **Recommended treatment:** change "the test/Pint results" to "the test/formatting results" (matching `verification.md`'s now-generic phrasing), optionally cross-referencing `rules/verification.md` for what those tools are in this project's evidence.

#### `rules/sequencing.md`
**Verdict:** Portable, one wording ambiguity.
- **Problematic reference (new finding):** line 11 — `"(this project writes them as plain prose — 'Depends on #120', 'Depends on #290, #120' — not a structured field; read the issue body, don't assume a schema)"`. The *rule* is already fully generalized ("don't assume a schema" — i.e., read whatever format is actually there). The issue is purely the phrase "this project," which is ambiguous between "the originating project this skill was extracted from" and "your own project" (a new reader's first read is more likely the latter, which is backwards — it would suggest their project already uses this format, when the point is the opposite: check, don't assume).
- **Project-specific references:** `#120/#289/#290/#121` in the "three simultaneously-ready issues" example — a clean, self-contained illustration of "closing one issue surfaces several ready ones with different blockers," understandable with zero project context.
- **External dependencies:** `gh issue list --milestone "<name>" --state open` — templated with a placeholder, not project-specific.
- **Recommended treatment:** reword to something like "(one project's evidence: issues here wrote dependencies as plain prose... — a different project's issues may use a different format; read whatever's actually there, never assume a schema)," matching the "this repository's evidence shows... not a rule to carry into a project whose evidence points somewhere else" framing used elsewhere.

---

### 3. Reference inventory

| File | Reference | Type | Needed for understanding? | Current treatment | Recommended treatment |
|---|---|---|---|---|---|
| `SKILL.md` | `#288/#287/#120/#289`, PR `#298`, `v0.17.0` (frontmatter) | Useful empirical evidence | No — rule stated first each time | Parenthetical `(see rules/x.md for the v0.1 evidence: ...)` | Keep as-is |
| `SKILL.md` | `my-laravel-patterns, pest-testing, fortify-development, wayfinder-development, inertia-vue-development` | Stack/tooling fact | Partially — implies but doesn't state stack-substitution | Scoped by "this project's implementation skills... etc." | Add one clause making substitution explicit |
| `SKILL.md` | GitHub issues/PRs/milestones (throughout) | External dependency | Yes, but declared in skill's own name/opening line | Assumed, not itemized | Acceptable as-is; see §6 |
| `SKILL.md` | `feature/organization-owner-provisioning` branch name | Project-specific example, correctly labeled | No | Explicit "one data point, not a pattern" disclaimer | Keep as-is |
| `README.md` | Issue-shape table (`#288/#287/#120/#289`) | Useful empirical evidence | No | Standalone table, rule stated independently | Keep as-is |
| `README.md` | `SecurityTest.php`, "Fortify TOTP", `organizations:provision` | Project-specific example (release-altitude section is the bad example the rule warns against) | No | Explicitly framed as evidence for the gap being illustrated | Keep as-is |
| `rules/commit-boundaries.md` | Evidence table + `#120/#289` shape descriptions | Useful empirical evidence | No | Table + prose, rule independent of table | Keep as-is |
| `rules/commit-boundaries.md` | `ResetTwoFactorAuthenticationAction`, `organizations:reset-owner-two-factor`, `OrganizationPolicy` | Project-specific example | No — illustrates message *shape* only | Full worked example, self-contained | Keep as-is |
| `rules/issue-closure.md` | `#288/#287/#120` (recipe evidence), `#289` (explicitly excluded as evidence) | Useful empirical evidence + methodology about evidence | No | Explicit "only cite once that lifecycle stage occurred" rule | Keep as-is — strongest file in the skill on this axis |
| `rules/issue-closure.md` | `gh issue view/edit/comment/close ...` | External dependency | Only if not using `gh`/GitHub | Literal commands, unboxed | Acceptable — `gh` is the mechanism, not an example; see §6 |
| `rules/milestone-completion.md` | `Phase NN — {Feature Name}` convention | **Project-specific rule presented as part of a definition** | **No — blocks understanding of what the rule generalizes to** | Inline em-dash clause, ambiguous | **Reword: separate general definition from this project's naming example** |
| `rules/milestone-completion.md` | "every milestone ever created left open" | Useful empirical evidence (explains why this rule is *decided*, not *extracted*) | No | Explicit "Forward-looking only" section | Keep as-is |
| `rules/milestone-completion.md` | `gh api repos/{owner}/{repo}/milestones/{number} ...` | External dependency | Only if not using `gh` | Literal, with fallback hedge ("or whatever mechanism the installed `gh` version actually offers") | Keep as-is — already hedged |
| `rules/release.md` | Release-policy discovery + publish-mechanism boxes | Stack/tooling fact, correctly isolated | No | `### What this repository's evidence shows`, twice, explicit disclaimers | Keep as-is — the model |
| `rules/release.md` | `v0.13.0 — Carriers`, `v0.11.1 — Tags Infrastructure`, etc. (shape table) | Useful empirical evidence | No | Explicit "evidence for that range, not a hypothetical" | Keep as-is |
| `rules/review-gates.md` | `"the test/Pint results"` | **Stack/tooling fact embedded unboxed in general prose** | **No — blocks understanding for a non-Laravel reader** | Bare mention, no box, no cross-reference | **Reword to "the test/formatting results"** |
| `rules/review-gates.md` | `#287` 13-route-groups/8-files example; `#289` sequencing example | Useful empirical evidence | No | Self-contained illustrations of the abstract point | Keep as-is |
| `rules/review-gates.md` | `gatherMiddleware()` | Unnecessary noise (minor) | No, but adds no value either | Parenthetical named-method citation | Optional: drop the method name, keep "resolving real route middleware" |
| `rules/sequencing.md` | `"this project writes them as plain prose"` | **Project-specific example, ambiguously framed** | **Rule itself is fine; phrase risks misreading** | Inline parenthetical, no "evidence" framing | **Reword to "one project's evidence: ..." matching release.md's pattern** |
| `rules/sequencing.md` | `#120/#289/#290/#121` (ready-set example) | Useful empirical evidence | No | Self-contained illustration | Keep as-is |
| `rules/sequencing.md` | `gh issue list --milestone "<name>" --state open` | External dependency | Only if not using `gh` | Literal, templated placeholder | Keep as-is |
| `rules/verification.md` | Pest/Pint commands, `skipUnlessFortifyHas()`, `SecurityTest.php`/`SecurityController` | Stack/tooling fact, now correctly isolated | No | Three `### What this repository's evidence shows` boxes (this pass's prior fix) | Keep as-is |

---

### 4. Strong examples worth preserving

- **`rules/commit-boundaries.md`'s four-issue evidence table** (`#288`→1 commit, `#287`→1, `#120`→3, `#289`→4). Teaches the actual rule ("file count ≠ commit count, the diff decides") better than prose alone could, because the counter-intuitive pairing (a 21-file issue as one commit; a 2-file issue as three) is the whole point. Framing already correct: present as evidence, not instruction.
- **`rules/review-gates.md`'s #287 "13 route groups across 8 files, not the 3 expected" example.** This is the single best-taught concept in the skill: "implementation reveals a contradiction with approved architecture" is an abstract, easy-to-skip warning on its own; the concrete mismatch between planned scope and discovered scope makes it visceral and memorable without requiring any useOrbit knowledge — a reader just needs "the plan said X, reality said Y, that's a stop." Keep, exactly as framed.
- **`rules/issue-closure.md`'s "only cite an issue as evidence once that lifecycle stage occurred" rule**, illustrated by explicitly *excluding* `#289` from being cited as closure evidence. This is a methodology-about-methodology statement — it teaches evidentiary discipline by demonstrating it, and it's the clearest self-aware moment in the whole skill. Preserve verbatim.
- **`rules/release.md`'s release-shape table** (`v0.13.0 — Carriers`, `v0.11.1 — Tags Infrastructure`, etc.). Demonstrates the "release size isn't a versioning rule" point with real range across six different shapes — a hypothetical list would be far less convincing. Already framed correctly ("this repository's own history is the evidence for that range, not a hypothetical").
- **`rules/verification.md`'s three now-boxed evidence sections** (post-refinement). The `#120` Fortify/`SecurityTest.php` ordering story in particular is a strong, concrete failure-mode illustration — a reader who's never touched Fortify still gets the general mechanism (a gate silently hides tests; flipping the gate exposes them against code that may not be ready) because the general paragraph now stands fully on its own before the evidence box explains what actually happened in this project.

For all of the above: the framing that makes them work is **rule stated in full generality first, evidence following as a labeled "here's what this looked like" clause** — never the reverse.

---

### 5. Problematic examples/references

Three, all newly identified or refined by this pass (no others found on full re-read):

1. **`rules/review-gates.md:12`** — `"the test/Pint results"`. Blocks comprehension for a non-Laravel reader; no box, no cross-reference. Highest-priority fix — same defect class as the one just resolved in `verification.md`, just missed because Phase C's iterations were scoped to that file.
2. **`rules/milestone-completion.md:39-40`** — the `Phase NN — {Feature Name}` convention embedded in the definition of "what counts as a delivery/phase milestone." Risks a reader concluding the naming syntax is required rather than illustrative.
3. **`rules/sequencing.md:11-13`** — `"this project writes them as plain prose"`. The underlying rule is fine; the phrase risks being misread as describing the reader's own project rather than the originating one.

None of these are "materially mixed" in the sense of a rule whose *reasoning* depends on useOrbit — all three are terminology/labeling slips in otherwise-sound generic rules.

---

### 6. Structural recommendation

**Assessment, not implementation:** the evidence does not justify a skill-wide mechanical restructuring (e.g., mandating a `### What this repository's evidence shows` heading in every file, or splitting into `methodology/` vs. `evidence/` subdirectories).

Reasoning: two files (`release.md`, and now `verification.md`) already use the explicit heading pattern, and it works well there specifically because those files mix *procedural steps* with *concrete commands* — the box gives the reader a clean place to skip. The other five rule files rely on inline prose separation (rule-clause, then an evidence-clause introduced by "e.g.," a table, or a citation), and on this full re-read that pattern holds up almost everywhere — only three sentence-level instances leaked a term or blurred a definition. Retrofitting headings onto files that don't currently have a boxing problem would add ceremony without fixing anything.

**What the evidence does support:**
- Apply the exact same three fixes already used twice in this skill (`verification.md`, informally elsewhere) to the three flagged spots — no new pattern needed, just wider application of the existing one.
- A single, one-time explicit statement of external dependencies (`GitHub` + `gh` CLI) somewhere prominent — `SKILL.md`'s "What this skill owns" section, or a new short "Assumes" line — rather than per-file. This isn't fixing a defect (the `gh` usage is coherent and intentional throughout), it's closing the disclosure gap Phase C already named and left open ("`gh`/GitHub as a first-class, named dependency distinct from Boost or the `Artifact` tool... names this gap but does not close it"). Low cost, addresses a real gap.

---

### 7. Readiness conclusion

What the Phase C 7.3 score concretely means, after this deeper pass: **six of seven rule files plus both top-level files were already sound**, and the one flagged file (`verification.md`) has since been fixed using a pattern the skill had already proven on itself (`release.md`). This pass found that pattern needed applying in two more places and one wording fix — smaller in scope than the original `verification.md` gap, spread across two files instead of concentrated in one, and undiscovered by three prior iterations precisely because they were reading with `verification.md` as the lens rather than auditing the skill fresh.

**Before `my-git-workflow` is a clean, self-contained reusable methodology skill, three sentence-level edits remain:**
1. `rules/review-gates.md:12` — de-name "Pint."
2. `rules/milestone-completion.md:39-40` — separate the general milestone definition from the project's naming-convention example.
3. `rules/sequencing.md:11-13` — reframe "this project writes them as plain prose" as originating-project evidence, not an ambient fact.

Optional, not blocking: an explicit one-line "assumes GitHub + `gh` CLI" dependency statement, and trimming `gatherMiddleware()` from `review-gates.md`'s parenthetical.

No file needs a rewrite, no example needs deletion, and no new structural convention needs inventing — the skill's own established "rule first, evidence second, boxed when the evidence is a command" pattern is sufficient; it just needs to be applied to the three spots that still slipped past it.
