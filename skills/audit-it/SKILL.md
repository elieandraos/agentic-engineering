---
name: audit-it
description: "Audit an existing system for security, data integrity, performance, and test gaps. Use for a database audit, tenant isolation review, query and index assessment, or launch-readiness audit of data access. Trace current behavior, verify material findings, and recommend the smallest useful correction. Use review-it for implementation review of a proposed change and lab-it for architecture decisions."
---

# audit-it

## Scope and routing

Audit the current behavior of a system or subsystem. Establish the target revision or
environment, the surfaces in scope, and the expected guarantees from project instructions,
requirements, and the request. Reuse relevant prior evidence when it still applies. Ask only
when an unresolved question would materially change the scope or the standard for a finding.

For database work, load [Database audit](rules/database.md). Use the project's actual database
engine, access layer, and runtime paths to select checks and tools.

## Investigate and verify

1. Trace the normal entry points to the operation and its downstream consumers. Compare the
   implementation, schema or configuration, relevant tests, and available runtime evidence.
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
material areas that remain unverified. If the evidence supports no findings, report that result
within the audited scope.

## Ownership and handoff

Finish with findings and proposed corrections. Use `lab-it` if remediation requires a product or
architecture decision. Approved work can proceed through `plan-it` and `implement-it` as
appropriate. Keep the audit diagnostic and leave application, repository, tracker, and live
environment changes to separately authorized work.
