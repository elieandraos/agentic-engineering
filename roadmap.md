# Agentic Engineering Roadmap

## Purpose

Agentic Engineering develops evidence-driven agent skills for understanding systems, planning work, implementing and reviewing changes with appropriate stack knowledge, and shipping verified releases.

The portable methodology stays independent of language and framework. Stack companions carry technology-specific knowledge, while consuming projects remain authoritative for their domain, repository conventions, and delivery environment.

This roadmap records the next practical steps and longer-term possibilities. Further changes should follow personal review and observed behavior in real projects.

## Current baseline

[v2.0.2](https://github.com/elieandraos/agentic-engineering/releases/tag/v2.0.2) is published from [`c9d73ea`](https://github.com/elieandraos/agentic-engineering/commit/c9d73eae5d459f5f0ea62d55d82e5368c46acdb3): **Lab. Plan. Implement. Review. Ship — with the right stack.** `document-it` is an independently available companion.

This patch separates conditional guidance in `document-it`, `implement-it`, `ship-it`, and `plan-it` into focused supporting files, with responsibilities, approvals, and verification requirements preserved through source review. The simplified [context guide](docs/skill-context.md) uses a [measurement script](scripts/measure_skill_context.py) and explicit workflow definitions for repeatable breakdowns. [Test contracts](test-contracts.md) retain expected behavior and a framework-independent testing strategy.

Recorded validation for v2.0.2 includes source comparisons, static routing walkthroughs, focused measurement-script checks, and independent arithmetic. These release checks do not include live skill or consumer execution, or observed session token usage; workflow totals remain modeled estimates.

The v2.0.0 migration is complete. Its [migration plan is preserved at v2.0.0](https://github.com/elieandraos/agentic-engineering/blob/v2.0.0/plan.md) and in Git history.

## Next steps

1. **Personal review of all skills.** Read the six portable skills and `laravel-inertia-stack`, including their supporting rules, blueprints, and templates. Gather the maintainer's own observations on clarity, responsibilities, approvals, and practical workflow. Apply agreed feedback through focused, reviewable corrections before adoption.
2. **Install the updated skills in useOrbit.** Manually select all six portable skills so existing installations are refreshed and `document-it`, `implement-it`, and `review-it` are added. Retain the applicable stack companion and unrelated installed skills. Installation follows the [consumption guidance](docs/skill-consumption.md); it does not by itself establish successful runtime behavior.
3. **Use the skills in real work and refine them.** Apply the relevant skills to normal useOrbit development. Capture concrete friction, missing guidance, or unexpected behavior with enough context to reproduce it; correct the owning skill and publish follow-up changes as needed. Formal consumer and portability exercises remain optional follow-up work.

## Future directions

These are possibilities, not commitments or a prescribed order:

- consider an optional `steward-it` companion once real use clarifies the need: collect skill observations, retain approved findings, and propose deliberate canonical updates; define its scope from that evidence before choosing an implementation or packaging approach;
- compare adjacent skills from mature public ecosystems—starting with Matt Pocock’s—to identify useful methods, intentional differences, and concrete gaps without copying their structure blindly;
- develop lightweight consumption and refresh tooling for projects that are not ready to adopt a repository-managed `npx skills` setup, building on the consumption modes documented in [`docs/skill-consumption.md`](docs/skill-consumption.md);
- use Project B as a possible later cross-stack proving ground;
- compare behavior across multiple consuming projects to refine the portable / stack / project knowledge boundary;
- add stack or platform companions only when repeated real needs justify them.

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
