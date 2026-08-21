# Issue & Structural Review

Run after canonical issue definitions are drafted, and again after any revision — before the final approval pass. Six categories, plus post-mutation validation every time this skill actually touches GitHub — at initial creation and on any later mutation.

Three of these categories are easy to conflate but check entirely different things — keep them distinct rather than treating any one as covering the others:

- **Canonical structural integrity** — validates the canonical issue *definitions* against each other (unique titles, acyclic dependencies, no duplicated bodies, etc.). Says nothing about what the user is shown, and says nothing about whether any individual issue's content is any good.
- **Rendered manifest integrity** — validates that the *rendered* final compact manifest — the summary table the user actually reads and approves — faithfully contains the canonical set: same issues, same count, same order, nothing added, nothing dropped, nothing duplicated. A canonical definition can be perfectly valid while its rendering silently drops or duplicates a row; only this check catches that, because it inspects the actual table output, not the data it was generated from. It says nothing about the *content* inside any one issue — a manifest row can be perfectly present and still point at a body full of broken references.
- **Issue-body content integrity** — validates that each individual rendered issue *body* — the full Context/Tasks/Acceptance Criteria/Tests text, not just its title and row in the manifest — is correct, self-contained, and developer-ready. A canonical definition can pass structural integrity, and its title can pass manifest integrity, while its body still cites `plan.md` instead of explaining anything, uses `#N` for a decision number instead of a real reference, or drops a checkbox. This is the only one of the three that reads inside the body text.

## Issue quality

- Does each issue represent one coherent capability/change, not a random bundle of unrelated files?
- Is an issue too broad because it actually bundles multiple independently valuable outcomes? Split it.
- Is an issue so small it's really a task that belongs inside another issue? Fold it in.
- Do important architectural/product guarantees appear as acceptance criteria, rather than being collapsed into a vague "add tests" bullet? (See `SKILL.md`'s "Acceptance criteria vs. task checklists".)
- Are non-goals stated explicitly wherever accidental scope expansion is likely (e.g. "no free-text field", "no second leadership copy")?
- Are tests described by the behavior/guarantee they prove when that matters, not just "add tests for X"?
- Does the issue preserve a deliberate distinction the plan already made (e.g. "same event, two audiences, two classes") instead of flattening it for convenience?
- Extensibility claims validated against every actual integration seam — see "Extensibility-claim validation" below.

Apply proportionally — a one-file frontend wiring issue doesn't need a wall of acceptance criteria; a shared-infrastructure or multi-audience issue usually does.

## Extensibility-claim validation

When an issue or its acceptance criteria claims a future model/resource can join a capability through a minimal, enumerated set of changes (e.g. "add one model + one registry entry"), verify that claim against every actual integration seam the capability has — not just the one seam its author happened to be thinking about. Walk them explicitly:

- Backend registration (a config array, a service-provider call, an enum case)
- Any contract/interface the model must implement
- Frontend presentation/registry (a kind→icon/label map, a switch statement keyed on the same kind string)
- Routing/navigation (a new route, a nav-item entry)
- Authorization (a policy class/ability the fan-out or dispatch logic checks)
- Anything else the shared infrastructure actually touches per adopter

If the claim omits a seam that's genuinely required, correct it before the issue is finalized — widen the claim to name every seam, or split an omitted seam into its own task/issue if it's substantive enough to be its own unit of work. Don't let an acceptance criterion under-claim the integration surface just because the shared-infrastructure issue only implemented some of the seams itself. Cite a source reference for the claim where one exists (the interface, the registry file, the frontend map) — the same way a security row cites its enforcement location.

## Dependency quality

- Is each dependency an actual implementation prerequisite, not just a preferred execution order?
- Can root/infrastructure issues land and be tested independently, with no dependency of their own?
- Does every frontend issue depend on the specific backend capability it actually consumes — not just "depends on everything backend"?
- Do shared-infrastructure issues precede every integration issue that needs them?
- Are dependency references acyclic, and do they all point to issues that actually exist in the canonical set?
- Are nominal cleanup issues (renames, tenancy fixes) left independent when they genuinely are — don't invent a dependency just because they landed in the same milestone?

## Canonical structural integrity

Validate the canonical issue definitions against each other — never the rendered preview text — before any final manifest or `gh issue create` call:

- Expected issue count equals the canonical issue count.
- Sequence numbers/IDs are unique.
- Titles are unique.
- Exactly one canonical body exists per issue.
- No issue's Tasks or Acceptance Criteria contain content belonging to another issue.
- No canonical body is duplicated.
- Every dependency reference points to an existing canonical issue.
- Announced backend/frontend batch counts match the canonical definitions (applies to planned feature work sequenced per `rules/sequencing.md`'s batching convention; a standalone discovered-work issue sequenced per that file's discovered-work carve-out has no such batch to check).
- Issue order matches the intended dependency-safe sequence (every dependency points backward, never forward).

> Run this validation against the canonical issue definitions, never against previously rendered preview text. A preview is a one-way rendering of the canonical set, not a record to re-derive it from — reconstructing from a prior render is exactly what produced duplicated headings and misplaced acceptance criteria while drafting Phase 21.

This category says nothing about whether the manifest you're about to show the user actually reflects these definitions — that's a separate check, immediately below.

## Rendered manifest integrity

Canonical structural integrity checks the definitions. This checks the **rendered artifact** — the final compact manifest the user is about to see and approve — against those same definitions. Run it immediately before presenting the final compact manifest, every time that manifest is (re-)shown, including after any revision. A manifest that hasn't passed this check is not ready to be shown.

Rendering is a generative step, not a mechanical copy — a row can be silently dropped, duplicated, retitled, or reordered in the act of producing the table, with nothing else in this workflow catching it. Treat a freshly rendered manifest as unverified until it's been diffed against the canonical set; don't rely on having "just written it correctly" or on a visual skim.

Before presenting the final compact manifest, mechanically verify, by comparing the rendered rows against the current canonical issue definitions:

- Canonical issue count == rendered manifest row count.
- Every canonical sequence number appears in the manifest exactly once.
- Every canonical title appears in the manifest exactly once.
- No rendered row exists that is not in the canonical set.
- Rendered order matches canonical order.
- No canonical issue is missing from the manifest.
- No issue is duplicated in the manifest.

This check is generic by construction: it re-derives its expected set from whatever the canonical definitions currently are, for any feature and any issue count — never hard-code a specific issue, title, or count into the check itself.

**If the check fails:** do not present the manifest. Treat the failure as a structural-integrity failure — report exactly which row(s) diverged (missing / duplicated / reordered / retitled), regenerate the render from the canonical definitions, and re-run this check before showing anything to the user. The manifest remains a one-way rendering of the canonical definitions; never "fix" a failure by hand-editing the rendered table to match — regenerate it from the canonical set instead.

## Issue-body content integrity

Canonical structural integrity checks the definitions; rendered manifest integrity checks the summary table. This checks the **actual body text of every issue** — the thing a developer opens and reads, months from now, quite possibly without this conversation, `plan.md`, or this skill available to them. See `SKILL.md`'s "GitHub issues must stand alone" for the underlying principle.

Run this validation twice, on every rendered issue body:

1. **When issue bodies are first rendered for substantive content review** (`SKILL.md` workflow step 9) — so problems surface while the user is reviewing scope, not after.
2. **Immediately before that body is used in `gh issue create` or `gh issue edit`** — a revision made after step 1's check could have reintroduced a problem, so the check must run again right at the point of truth, not be trusted to still hold from earlier.

For every issue body, verify each of the following. Where useful, cite the specific line/field that fails — this check is meant to produce an actionable diff, not a pass/fail verdict.

**No false GitHub references**
- No `#N` where `N` is a plan.md decision number, a canonical planning sequence number, or any other non-GitHub numbering scheme (`decision #7`, `LOCKED #9`, `issue 5` meaning "canonical issue 5").
- Every `#N` that *does* appear resolves to a real GitHub issue in this milestone's set, and is a genuine dependency or a genuine pointer to another real issue — not an accidental collision with plan-decision numbering.

**No load-bearing plan.md references**
- No `§N.N` (or similar) section citation used as a stand-in for explanation.
- If a `§` citation appears at all, the sentence it's attached to is already fully understandable without it — the citation is decoration, not the load-bearing part.

**No other planning-only leakage**
- No unresolved placeholders (e.g. a literal `<issue5>` or `TBD` that should have been substituted).
- No references to "the previous draft", "the planning conversation", "resolved above", "per our discussion", or any other phrase that assumes the reader was present for planning.
- No canonical-only terminology (a phrase that only makes sense with the canonical issue list open) survives unexplained.

**Context is self-contained**
- Context explains *why* this issue exists and what problem/change motivates it, in its own words — not solely by citing a decision, section, or prior document.
- The outcome, the architectural/product constraints that matter, in-scope/out-of-scope, and relevant dependencies are all addressable from the issue body alone.
- Apply the test from `SKILL.md`/`rules/issue-conventions.md`: could a developer who never saw the planning conversation open this issue tomorrow and understand what they're supposed to deliver and why? If no, this check fails.
- Where this issue depends on another (`Depends on #N`) and understanding *this* issue's own outcome or user/system behavior genuinely requires knowing what that dependency does, the body briefly summarizes that relied-upon behavior in its own words — not just the `#N` link on its own. Apply the test from `SKILL.md`'s "A GitHub dependency is not an excuse to skip explaining what it provides": could a developer understand this issue's own outcome and user/system behavior without opening the dependency? If no, this check fails. This does not require restating the dependency's Context, Tasks, or Acceptance Criteria, and does not apply when the dependency is a pure implementation prerequisite the reader doesn't need to understand to grasp this issue's own scope (e.g. "depends on the migration landing first").
- For a Discovered-work issue (`rules/discovered-work.md`), confirmed facts and open hypotheses/unknowns stay visibly distinct in Context — no unresolved mechanism is phrased as if it were an established fact. If the mechanism is still open, an investigation/instrumentation Task naming what's left to determine is a legitimate substitute for a settled root cause, not a gap (`rules/issue-conventions.md`'s "Discovered-work issues").

**Tasks are literal checkboxes**
- Every `## Tasks` line is `- [ ] ...` in the actual body text about to be posted — not a plain `- ...` bullet, not a prose paragraph.

**Acceptance Criteria are real guarantees**
- Acceptance Criteria bullets state guarantees (business rules, authorization boundaries, tenancy invariants, runtime behavior, observable outcomes, meaningful non-goals) — not a restatement of a Tasks line with different wording.
- Every guarantee a real invariant discovered during planning (e.g. "an Admin can never reset an Owner's 2FA") is present somewhere in Acceptance Criteria — not lost between the canonical definition and the rendered body.

**Tests, when present, stay at the behavior level**
- A `## Tests` section exists only where it earns its place — multiple authorization cases, multiple audiences, a tenancy boundary, a recovery/edge-case matrix — not by default.
- No method names, no assertion-by-assertion recipes, no implementation walkthroughs.

This check is generic by construction — it re-derives what to look for from whatever the canonical definitions currently say, for any feature and any issue count. Never hard-code a specific issue number, title, or phrase into the check itself.

**If the check fails on any issue:** do not create or update that issue on GitHub. Report the exact issue and the exact field/bullet that failed. Revise the *canonical definition* (never patch the rendered text directly), render that issue's body again, and re-run this check before proceeding — the same discipline as the other two integrity checks.

## Post-mutation validation

Every GitHub mutation this skill performs — creating an issue, editing an issue's body, changing an issue's title/labels/milestone/assignee, creating a milestone, creating a label — ends with two things, every time, no exceptions: a **compact change summary**, and a **post-mutation validation pass**. This applies whenever this skill touches GitHub, not only during the initial batch-creation moment at the end of a planning pass — a later request to fix, reword, retitle, relabel, or re-milestone an already-created issue gets exactly the same discipline.

Never trust a `gh` command's exit code (or its own echoed output) as proof the change is correct. Re-fetch the mutated state from GitHub with a separate read (`gh api`/`gh issue view`) and check it against what was actually intended — the exit code proves the request was accepted, not that the result is right.

Validate per mutation *episode* — one batch of related `gh` calls issued together for one user-approved change — not per individual API call. Updating 8 issue bodies in one pass gets one validation pass and one summary covering all 8, not eight separate ones.

### What to validate, by mutation type

- **Issue(s) created** — created count matches the canonical/approved count; every issue carries the milestone and approved labels; every issue is assigned as specified (default `@me`); titles match the canonical definitions exactly; every dependency reference inside a created body is a real GitHub issue number, with no leftover canonical/planning-only reference.
- **Issue body updated** — re-run **issue-body content integrity** (above) against the *live* body fetched back from GitHub, not the text that was sent — no false `#N` references, no load-bearing `§` citations, no other planning-only leakage, Tasks checkboxes still literal, content matches what was approved.
- **Issue metadata changed** (title/labels/milestone/assignee) — re-fetch and confirm the new value is actually set; confirm nothing else on the issue moved that shouldn't have (e.g. an `--add-label` call didn't silently drop an existing label; an unrelated field wasn't touched).
- **Milestone or label created** — re-fetch and confirm name/color/number match what was proposed and approved; if a description was proposed and approved (`rules/issue-conventions.md`'s "Milestone descriptions"), confirm its text matches too — an approved description is part of what was agreed, not an optional extra that can silently drift or go missing.

### Compact change summary

Report immediately after validation, compact — never a full re-render of bodies or a wall of raw `gh` output:

```
<mutation type> — <N> issue(s)/item(s)
#<n> <title> — <one-line description of what changed>
#<n> <title> — <one-line description of what changed>
...
Validation: <pass/fail, per applicable check category>
```

The summary reports the validation's result; it never substitutes for actually running the validation.

### If validation fails

Do not report success. State exactly which issue and which field failed. If GitHub is now left in a state that doesn't match what was approved, say so explicitly and state whether a follow-up mutation is needed to correct it — never leave a failed mutation unflagged.
