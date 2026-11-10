# audit-it

Audit how an existing system behaves today — data access, security, and background work — and
report verified findings with the smallest useful corrections, never a fix applied during the audit.

## When to use it

- You need to know whether current behavior holds up: tenant isolation, record lifecycle, query
  cost, authorization, data exposure, or queued-job reliability.
- A system or subsystem is approaching launch, and its data access, security, or background work
  needs an evidence-backed check.
- A business rule is enforced by several workflows or computed in several places, and you need to
  know whether they agree.
- Earlier audit findings need re-checking after fixes.

Not for reviewing a proposed change — that stays with [`review-it`](../review-it/). Not for
deciding what the system should become — that stays with [`lab-it`](../lab-it/). `audit-it` is a
tool, not a pipeline stage: it runs at any point, on any codebase, with no prior plan or issue.

## Boring prompts

```shell
"Audit tenant isolation across the order pages, exports, and jobs."
"Audit the billing module for security and data-integrity risks."
"Check whether the upload jobs survive retries and worker restarts."
"Re-audit last week's database findings."
```

## Audit modules

Only the modules whose surfaces are in scope load; one audit can combine several.

- **Database** — who can reach which records on every path, record lifecycle and integrity,
  concurrent writes, N+1 growth, and query cost on realistic data.
- **Security** — entry-point authorization, input trust, sensitive data leaving the server, files
  and external input, and configuration and dependencies. It starts from real entry points, not
  from the presence of policies, validation, or settings.
- **Background work** — what retries, interruptions, commit ordering, and stale state do to queued
  jobs, notifications, batches, and scheduled tasks.

Business-rule consistency is not a module. Contradictions surface during investigation, so the
check belongs to every audit: it compares what each workflow permits, prohibits, and assumes, and
whether every implementation and consumer of a rule agrees at its boundaries. A contradiction ends
as confirmed, an intentional exception backed by requirements, project instructions, or a
recorded product decision, unreachable, or an open product decision handed to `lab-it`.

## What normally happens

1. Establish the target, the surfaces in scope, and the guarantees the system is expected to keep,
   including recorded product decisions. Behavior those decisions approve is not a defect.
2. Trace the normal entry points and consumers, then verify material leads with the smallest
   reproduction — writes and load tests only in a disposable local environment. Test runs that
   share files or databases don't overlap in one checkout.
3. Classify each result as reproduced, established by source inspection, or unverified, and keep
   what an invalid fixture proves apart from what a normal user action can reach.
4. Read the closest tests and name why each finding escaped them.
5. Report findings by risk — impact, reachability, realistic likelihood, recoverability, and the
   cost of the correction — each with a correction and the test or measurement that would prove
   it, along with the checks that passed and what remains unverified.

An audit is independent unless you ask it to verify earlier findings: it judges the current system
on its own evidence and doesn't inherit earlier findings or scores, whether or not it runs in the
same session. A re-audit collects earlier findings and decisions from previous reports, tracker
issues, milestones, and plans, then marks each one fixed, open, regressed, an accepted risk, or
intentional. An accepted risk stays a finding with its deduction but isn't presented again as new
or as a blocker unless new evidence changes its assessment.

Each applicable module gets its own score out of 100, so a strong database score can't hide weak
background work; there is no combined score, and a finding counts once. Only verified findings
cost points. A category the evidence can't support, such as one whose checks couldn't run, is
marked unassessed rather than given full points, and a total is withheld when too little evidence
supports it. Launch blockers — findings
whose risk isn't acceptable for launch under the project's guarantees — are listed first and beside
each score, because no score offsets an open blocker. A focused audit, including a re-audit that
only searches changed code, shows its normalized score with the points that applied and is never
compared with a full audit's score.

## Ownership

Owns diagnostic audits of current behavior: findings, evidence, priorities, scores, and proposed
corrections. Choosing a new business rule or architecture belongs to [`lab-it`](../lab-it/);
approved corrections proceed through [`plan-it`](../plan-it/) and
[`implement-it`](../implement-it/); reviewing them belongs to [`review-it`](../review-it/). An
audit never changes application code, repositories, trackers, or live environments.

Not yet covered: comprehensive production readiness — CI/CD, deployment, rollback, backups, and
monitoring — and performance outside the database, such as external calls, storage, CPU, and
memory.

## Install

```shell
npx skills add elieandraos/agentic-engineering --skill audit-it
```

See [`SKILL.md`](SKILL.md) for the complete operational contract.
