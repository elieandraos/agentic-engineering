---
name: audit-it
description: "Audit an existing system for security, data integrity, background-work reliability, query performance, and test gaps. Use for a database or security audit, tenant isolation review, query and index assessment, queued-job reliability review, business-rule consistency check, or launch-readiness audit of data access, security, or background work. Trace current behavior, verify material findings, and recommend the smallest useful correction. Use review-it for implementation review of a proposed change and lab-it for architecture decisions."
---

# audit-it

## Scope and routing

Audit the current behavior of a system or subsystem. Establish the target revision or
environment, the surfaces in scope, and the expected guarantees from project instructions,
requirements, and the request. Reuse relevant prior evidence when it still applies. Ask only
when an unresolved question would materially change the scope or the standard for a finding.

Load each module whose surfaces are in scope. Load more than one when the audit spans them.

- Data access, tenant isolation, record lifecycle, concurrent writes, or query cost: load
  [Database audit](rules/database.md).
- Entry-point authorization, input trust, sensitive-data exposure, files, external input,
  configuration, or dependencies: load [Security audit](rules/security.md).
- Queued jobs, queued notifications or listeners, batches, scheduled tasks, or other deferred or
  retried work: load [Background-work audit](rules/background-work.md).

Use the project's actual runtime, database engine, access layer, queue, and deployment paths to
select checks and tools.

## Investigate and verify

1. Trace the normal entry points to the operation and its downstream consumers. Compare the
   implementation, schema or configuration, relevant tests, and available runtime evidence.
   When business rules govern the operation, apply
   [Business rules across workflows](#business-rules-across-workflows).
2. Verify material leads with the smallest useful reproduction. Use a safe local test environment
   and disposable synthetic data for writes, invalid fixtures, and load tests. Preserve user
   work and existing data. Keep temporary probes outside the deliverable unless requested.
3. Distinguish reproduced behavior, behavior established by source inspection, and unverified
   leads. State the conditions needed to reach each finding. A reproduction with intentionally
   invalid data establishes the effect under that condition. Establish separately whether a
   normal user action can create that data.
   When verifying a prior finding, trace the normal operations that could create the same bad
   state. If one can, reproduce it through the normal entry point and reassess the finding's
   priority.
4. For each finding, read the closest tests when a suite exists. Determine whether the gap is
   a missing test, a missing scenario, a missing assertion, or an execution gap such as a fake,
   different engine, or absent concurrency. State what the tests exercise and what they assert.
   When feasible, verify that the proposed regression test fails on current code for the
   expected reason. Distinguish tests inspected from tests run.
5. Rerun unexpected test failures under controlled conditions. Report confirmed test defects
   separately from application defects. Explain what changes between runs and how it affects
   the result.

### Business rules across workflows

Apply these checks to the domain operations in scope, in proportion to the request. Do not build
a complete domain model.

- Identify the rules and invariants that govern the operation: who may act, which states and
  references are valid, and which dates, windows, or limits apply. Use requirements, project
  instructions, implementation, and tests as sources.
- Trace the workflows that create, change, restrict, or depend on the same rules. Include
  lifecycle transitions, role differences, exceptional states, and queued or scheduled work.
- Compare what each workflow permits, prohibits, and assumes. A contradiction can exist between
  unrelated code. For example, one workflow refuses to remove a referenced record while another
  removes a comparable record and clears the references.
- When a rule has more than one implementation or consumer, check that they agree. Consider
  application-code and query versions, such as a PHP resolver and its SQL counterpart, filters,
  sorting, counts, exports, UI affordances, server enforcement, notifications, and queued
  execution. Compare their results on the same fixtures at boundary
  values such as dates, time zones, windows, and state combinations.
- Establish whether supported application behavior can reach the contradiction. Classify it as a
  confirmed contradiction, an intentional exception, an unreachable scenario, or an unresolved
  product decision. Classify an exception as intentional only when requirements or project
  instructions establish it. A test or comment that asserts the behavior shows implementation
  intent, not product approval.
- State which tests compare the implementations or workflows and which only test each one alone.

Score a confirmed contradiction in the module category that matches its impact. Report an
unresolved product decision separately, without a deduction, and hand it to `lab-it`. Do not
choose a new business rule during the audit.

## Report

Lead with the highest-impact verified findings. For each finding, give:

- **What happens and why it matters.** Explain the user or system impact in simple technical English.
- **How it can happen.** State the trigger, prerequisites, and a concrete example when the path is
  hard to picture. Cite the relevant code, test, query, or runtime result.
- **How it escaped testing.** Name the gap and the closest test, or state the limits of the evidence.
- **What to change and how to verify it.** Recommend the smallest correction that preserves the
  intended behavior. Give a regression test or measurement that would prove the correction.

Prioritize by impact, reachability, and expected workload. Separate fixes worth doing now from
improvements to revisit when evidence changes. Report meaningful checks that passed and
material areas that remain unverified. An unverified check is not a pass. If the evidence
supports no findings, report that result within the audited scope.

On re-audit, give the status of each prior finding: fixed, open, or regressed after a fix. List
new findings separately.

### Score breakdown

When a loaded module defines a rubric, report a score out of 100 for that module. Report one
score per applicable module. Do not combine module scores. Show points earned and available per
category, with the evidence and reason for each deduction. Assess deductions by impact,
reachability, and expected workload. Count each finding once, in the primary category of one
module. Reference it from other modules without a second deduction.

List launch blockers before the scores. Next to each module score, state its number of open
blockers. A high score does not offset an open blocker.

For a focused audit, label the score with its scope. Mark excluded categories as out of scope
or inapplicable. Calculate the total as 100 times earned points divided by the available points
in the remaining categories. Show the applicable points next to the total, for example
`78/100 normalized; 31/40 applicable points`. Mark a score provisional when material checks remain
unverified. If the evidence is too limited to support a meaningful total, give the supported
category scores and explain what evidence is missing.

On re-audit, compare scores only for categories whose scope and weights are unchanged. Explain
any change in scope or weights, and do not compare totals across that change.

## Ownership and handoff

Finish with findings and proposed corrections. Use `lab-it` if remediation requires a product or
architecture decision. Approved work can proceed through `plan-it` and `implement-it` as
appropriate. Keep the audit diagnostic and leave application, repository, tracker, and live
environment changes to separately authorized work.
