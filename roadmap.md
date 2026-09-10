# Agentic Engineering Roadmap

## Purpose

Agentic Engineering develops evidence-driven agent skills for understanding systems, planning work, implementing and reviewing changes with appropriate stack knowledge, and shipping verified releases.

The portable methodology stays independent of language and framework. Stack companions carry technology-specific knowledge, while consuming projects remain authoritative for their domain, repository conventions, and delivery environment.

This roadmap records the next practical steps and longer-term possibilities. Further changes should follow personal review and observed behavior in real projects.

## Current baseline

[v2.0.4](https://github.com/elieandraos/agentic-engineering/releases/tag/v2.0.4) is the next patch after v2.0.3, incorporating live useOrbit Policies implementation evidence from issues #312 and #313: a human-controlled full-suite choice at the issue boundary in `implement-it`, targeted verification retained as mandatory before Gate 1, and a portable Laravel factory rule for avoiding recursive parent factory states when `afterCreating()` creates a required child/detail record. The `implement-it` architecture dossier is reconciled with the same lifecycle.

This patch turns repeated real-work observations into focused guidance without changing the broader Agentic Engineering lifecycle. Backlog/trunk work recommends full regression verification; active phase-milestone issues may intentionally defer it after targeted verification when the human chooses. The distinction between fresh execution, TIA/impact selection, and cache/replay remains explicit, and the useOrbit-specific `--no-tia` command remains project knowledge rather than portable methodology.

The live Policies work also validated the new `review-it` Gate 1 integration and exposed reusable evidence for future stewardship: repeated verification cost on small milestone issues, a concrete factory-recursion trap, and a project-specific TIA footgun. These observations remain evidence unless and until further recurrence justifies additional canonical changes.

Recorded validation for v2.0.4 includes source review plus live useOrbit implementation/review sessions for Policies issues #312 and #313. Session-level token usage remains estimated rather than directly instrumented.

The v2.0.0 migration is complete. Its [migration plan is preserved at v2.0.0](https://github.com/elieandraos/agentic-engineering/blob/v2.0.0/plan.md) and in Git history.

## Next steps

1. **Use the skills in real work and refine them.** Apply the relevant skills to normal useOrbit development. Capture concrete friction, missing guidance, or unexpected behavior with enough context to reproduce it; correct the owning skill and publish follow-up changes as needed. Formal consumer and portability exercises remain optional follow-up work.

2. **Monitor context during real useOrbit tasks.** For representative tasks, note the skill versions, host/model, and skills or rules actually loaded where observable. Compare the measurement script's modeled workflow totals with session context readings (such as Claude Code's `/context`) at comparable checkpoints. Session totals include conversation, code, and tool output as well as skill guidance. Record unexpected or repeated loads, compaction, and missed instructions alongside task outcomes and adherence to approvals and verification. Use this evidence to decide whether clearer script reports, revised workflow models, or environment-specific context budgets would help. No universal red-zone threshold is assumed; monitoring stays lightweight and is not a publication gate.

## Future directions

These are possibilities, not commitments or a prescribed order:

- develop lightweight consumption and refresh tooling for projects that are not ready to adopt a repository-managed `npx skills` setup, building on the consumption modes documented in [`docs/skill-consumption.md`](docs/skill-consumption.md);
- use Project B as a possible later cross-stack proving ground;
- compare behavior across multiple consuming projects to refine the portable / stack / project knowledge boundary;
- add stack or platform companions only when repeated real needs justify them.

### Steward-it

Explore an explicitly human-invoked `steward-it` companion for retrospective investigation when an engineering session is unexpectedly slow, difficult, or repeatedly goes off course. It would reconstruct the session from available evidence and optional skill traces, compare intended guidance with observed behavior, classify the cause across methodology, skill, project, stack, prompt, execution, or external limitations, detect repeated patterns, and recommend deliberate improvements without changing canonical guidance automatically.

Scope, trace format, pattern detection, retention, and implementation remain future decisions. Validate the usefulness of retrospective stewardship against real sessions before making it part of the normal lifecycle.

### Skill testing

Explore repeatable testing using [`test-contracts.md`](test-contracts.md) for expected behavior and [`scenarios.md`](scenarios.md) for the case inventory and recorded evidence. Begin with a small selection of executable fixtures and explicit success criteria, preserving the distinction between source walkthroughs and observed runtime results.

- **Deterministic checks:** validate skill metadata and test shipped code, templates, and Git recipes against concrete expected outputs and state-preservation assertions.
- **Agent behavior evaluations:** exercise skill selection, review accuracy, scope boundaries, and approval handling in controlled project fixtures. Inspect actual actions and results, and repeat runs to assess consistency.
- **Framework choice:** assess [Promptfoo](https://www.promptfoo.dev/docs/guides/test-agent-skills/) as an initial candidate. [Anthropic's Skill Creator](https://claude.com/plugins/skill-creator) and the experimental [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) are alternatives to consider.

The initial cases, framework, and any later CI integration remain future decisions. Use a small pilot to judge usefulness, execution cost, and maintenance effort before expanding coverage.

### Public landing page

Explore designing and deploying a public landing page that tells the ecosystem's story through concise copy, interactive examples, and visual progression. Follow a representative mission from an initial question through Lab, Plan, Implement, Review, and Ship, with Document and stack companions available alongside the workflow.

- **Creative direction:** explore a space/universe or mission-control theme, with light gamification that helps visitors discover each capability and understand its role.
- **Motion:** consider smooth scrolling and scroll-driven animation inspired by Lenis, with clear navigation and a readable reduced-motion experience.
- **Content:** emphasize purpose, practical outcomes, and how to get started; link to the repository and documentation for implementation detail.

Visual identity, interaction design, animation tooling, hosting, domain, and deployment remain future decisions. Review a small storytelling prototype before committing to the full site.

## Deferred questions

- Clarify precedence between `laravel-inertia-stack` and Laravel Boost guidance if a concrete disagreement appears. The v2.0.0 audit identified missing conflict handling, not an established conflict.
- Revisit durable storage for canonical issue definitions if real interrupted-work recovery shows the current GitHub-query approach is insufficient.
