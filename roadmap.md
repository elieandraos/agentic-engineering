# Agentic Engineering Roadmap

## Purpose

Agentic Engineering develops evidence-driven agent skills for understanding systems, planning work, implementing and reviewing changes with appropriate stack knowledge, and shipping verified releases.

The portable methodology stays independent of language and framework. Stack companions carry technology-specific knowledge, while consuming projects remain authoritative for their domain, repository conventions, and delivery environment.

This roadmap records practical next steps and longer-term possibilities. Further changes should follow personal review and observed behavior in real projects.

## Skill testing

Explore repeatable testing using [`test-contracts.md`](test-contracts.md) for expected behavior and [`scenarios.md`](scenarios.md) for the case inventory and recorded evidence. Begin with a small selection of executable fixtures and explicit success criteria, preserving the distinction between source walkthroughs and observed runtime results.

- **Deterministic checks:** validate skill metadata and test shipped code, templates, and Git recipes against concrete expected outputs and state-preservation assertions.
- **Agent behavior evaluations:** exercise skill selection, review accuracy, scope boundaries, and approval handling in controlled project fixtures. Inspect actual actions and results, and repeat runs to assess consistency.
- **Framework choice:** assess [Promptfoo](https://www.promptfoo.dev/docs/guides/test-agent-skills/) as an initial candidate. [Anthropic's Skill Creator](https://claude.com/plugins/skill-creator) and the experimental [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) are alternatives to consider.

The initial cases, framework, and any later CI integration remain future decisions. Use a small pilot to judge usefulness, execution cost, and maintenance effort before expanding coverage.

## Future directions

These are possibilities, not commitments or a prescribed order:

- develop lightweight consumption and refresh tooling for projects that are not ready to adopt a repository-managed `npx skills` setup, building on the consumption modes documented in [`docs/skill-consumption.md`](docs/skill-consumption.md);
- compare behavior across multiple consuming projects to refine the portable / stack / project knowledge boundary;
- add stack or platform companions only when repeated real needs justify them;
- evaluate a rewrite of `laravel-inertia-stack` against the current Laravel Boost skill structure and current Vue/Inertia skill ecosystem, with the goal of reducing overlap, tightening progressive disclosure, and keeping only evidence-backed companion rules;
- use Project B as another cross-stack proving ground when a concrete candidate appears;
- explore a public landing page that tells the ecosystem's story through concise copy, interactive examples, and visual progression.

## Deferred questions

- Clarify precedence between `laravel-inertia-stack` and Laravel Boost guidance if a concrete disagreement appears. The v2.0.0 audit identified missing conflict handling, not an established conflict.
- Revisit durable storage for canonical issue definitions if real interrupted-work recovery shows the current GitHub-query approach is insufficient.
- Evaluate retiring Claude Artifact output from `document-it` in favor of Markdown-only documentation, while preserving the documentation methodology and removing Artifact-specific tooling such as the HTML template if confirmed.
- Review `review-it`'s trust-boundary wording after Snyk W011 flagged the unavoidable exposure to third-party PR and issue text as an indirect prompt-injection risk; treat GitHub content as untrusted evidence, never workflow authority.
