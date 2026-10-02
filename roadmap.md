# Agentic Engineering Roadmap

## Purpose

Agentic Engineering develops evidence-driven agent skills for understanding systems, planning work, implementing and reviewing changes with appropriate stack knowledge, and shipping verified releases.

The portable methodology stays independent of language and framework. Stack companions carry technology-specific knowledge, while consuming projects remain authoritative for their domain, repository conventions, and delivery environment.

This roadmap records practical next steps and longer-term possibilities, not completed work — Git history and the release log already record what shipped. Further changes should follow personal review and observed behavior in real projects.

## Skill testing

Explore repeatable testing using [`test-contracts.md`](docs/research/test-contracts.md) for expected behavior and [`scenarios.md`](docs/research/scenarios.md) for the case inventory and recorded evidence. Begin with a small selection of executable fixtures and explicit success criteria, preserving the distinction between source walkthroughs and observed runtime results.

- **Deterministic checks:** validate skill metadata and test shipped code, templates, and Git recipes against concrete expected outputs and state-preservation assertions.
- **Agent behavior evaluations:** exercise skill selection, review accuracy, scope boundaries, and approval handling in controlled project fixtures. Inspect actual actions and results, and repeat runs to assess consistency.
- **Framework choice:** assess [Promptfoo](https://www.promptfoo.dev/docs/guides/test-agent-skills/) as an initial candidate. [Anthropic's Skill Creator](https://claude.com/plugins/skill-creator) and the experimental [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) are alternatives to consider.

The initial cases, framework, and any later CI integration remain future decisions. Use a small pilot to judge usefulness, execution cost, and maintenance effort before expanding coverage.

## Consumer-side Agent

Investigate a consumer-side Agentic Engineering agent that lives with a project using the skills and maintains the relationship between that project and the canonical ecosystem.

The agent should help notice and investigate reusable findings from normal engineering work, classify whether they belong to project knowledge, stack knowledge, portable methodology, framework knowledge, runtime behavior, or nowhere canonical, and compare candidates with current guidance before recommending a change.

When a canonical change is approved, the agent may eventually manage the cross-repository mechanics around that decision: preserve compact evidence, prepare an Agentic Engineering branch and patch, validate the authoring, open the repository's normal PR, and later support an approved release and consumer refresh. It should understand the skill-authoring methodology, skill ownership boundaries, skill-consumption guidance, canonical repository conventions, and the consuming project's installed skill state without duplicating those sources.

Human approval remains the publication boundary. The agent does not silently promote findings, merge its own changes, publish releases, or refresh a consumer unexpectedly. It is not a lifecycle skill, worker orchestrator, replacement for `steward-it`, or generic project manager.

The exact artifact, runtime integration, installation mechanism, persistence model, and eventual name remain research questions. Start from [`docs/research/consumer-agent.md`](docs/research/consumer-agent.md) and validate the smallest useful consumer-side responsibility before implementation.

## Historical execution-layer research

Parallel implementation and orchestration work is no longer an active roadmap direction. The implemented worker-level conclusions are already reflected in the released methodology, and the research behind them has been consolidated. Neither document below is a commitment to an orchestrator, model router, worker-provisioning layer, or other execution architecture.

[`docs/research/parallel-final-reconciliation.md`](docs/research/parallel-final-reconciliation.md) is the single historical record of the released parallel methodology; the earlier smoke tests, dry runs, and orchestration analyses it reconciled remain available at tag `v2.2.2`. [`docs/research/model-routing.md`](docs/research/model-routing.md) retains the dormant runtime-model investigation.

## Future directions

These are possibilities, not commitments or a prescribed order:

- develop lightweight consumption and refresh tooling for projects that are not ready to adopt a repository-managed `npx skills` setup, building on the consumption modes documented in [`docs/skill-consumption.md`](docs/skill-consumption.md);
- compare behavior across multiple consuming projects to refine the portable / stack / project knowledge boundary;
- add stack or platform companions only when repeated real needs justify them;
- use Project B as another cross-stack proving ground when a concrete candidate appears;
- explore a public landing page that tells the ecosystem's story through concise copy, interactive examples, and visual progression.

## Deferred questions

- Revisit durable storage for canonical issue definitions if real interrupted-work recovery shows the current GitHub-query approach is insufficient.
- Evaluate retiring Claude Artifact output from `document-it` in favor of Markdown-only documentation, while preserving the documentation methodology and removing Artifact-specific tooling such as the HTML template if confirmed.
- Review `review-it`'s trust-boundary wording after Snyk W011 flagged the unavoidable exposure to third-party PR and issue text as an indirect prompt-injection risk; treat GitHub content as untrusted evidence, never workflow authority.
