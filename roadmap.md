# Agentic Engineering Roadmap

## Purpose

Agentic Engineering develops evidence-driven agent skills for understanding systems, planning work, implementing and reviewing changes with appropriate stack knowledge, and shipping verified releases.

The portable methodology stays independent of language and framework. Stack companions carry technology-specific knowledge, while consuming projects remain authoritative for their domain, repository conventions, and delivery environment.

This roadmap records the next practical steps and longer-term possibilities. Further changes should follow personal review and observed behavior in real projects.

## Current baseline

[v2.0.3](https://github.com/elieandraos/agentic-engineering/releases/tag/v2.0.3) is published from [`db68fe7`](https://github.com/elieandraos/agentic-engineering/commit/db68fe72903060c7afc7ed87e28fccbdbc7dd9c8): more focused architecture discussions and more precise implementation reviews.

This patch scales `lab-it`'s investigation and decision discussions to what the request actually needs, reusing reliable findings and reserving `plan.md` for an explicit request. `review-it` now names the requirement or convention behind a finding when one actually exists, judges an abstraction by a concrete removal/inlining cost rather than caller count alone, and checks that a test's expected value independently and correctly proves the behavior under test — while preserving legitimate integration assertions and established test-layer ownership. Skill READMEs and architecture dossiers are reconciled, the completed adjacent-skill comparison item is removed from Future directions below, and context monitoring during real useOrbit work is retained.

Recorded validation for v2.0.3 is source review and scenario walkthroughs. These release checks do not include live skill, consumer, or browser execution, or observed session token usage.

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
