# Steward-it evidence

Working evidence from real Agentic Engineering use. Keep entries compact: normally one or two sentences, with a concrete commit, PR, issue, or session reference when available. Record observations, not proposed canonical fixes, until repeated evidence justifies one.

- **2026-09-10:** A `lab-it` fork delegated only to extract design evidence independently ran Plan Synthesis after inheriting the parent's full skill context, temporarily producing an unapproved `plan.md`; the parent caught and reverted it before it became authoritative. Evidence: useOrbit Policies investigation, session skill trace; resulting plan committed at `c258d30`.
- **2026-09-10:** In the same Policies planning session, `lab-it` loaded two files (~5k rough tokens), while `plan-it` loaded six supporting rule files (~15–16k rough tokens); several sections were not materially used for this schema-only pass. These are static/agent-reported estimates, not measured tokenizer usage, so retain as a context-cost baseline rather than a confirmed inefficiency.
