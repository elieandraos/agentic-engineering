---
name: document-it
description: "Creates, maintains, and reviews evidence-backed technical documentation in Markdown. Covers architecture, infrastructure, operations, engineering practices, configuration, integrations, costs, approved designs and product behavior. Reuses verified understanding and approved decisions; routes missing or stale evidence to lab-it. Not for debugging, diff review, making unresolved decisions, synthesizing plan.md, or generating API specifications."
---

# document-it

## What this skill does

This skill creates, maintains, and reviews purpose-driven technical documentation in Markdown, from
already-available, sufficient, and current understanding. It is independently callable: a
documentation request does not require a fresh investigation to begin.

| User intention                                    | Result                                         |
| ------------------------------------------------- | ---------------------------------------------- |
| Document a technical system or approved design    | A new Markdown document                        |
| Reconcile a document with verified current reality | The same document, updated at its existing path |
| Evaluate whether a document serves its purpose    | A findings report, not a rewrite               |

## Evidence: reuse first, route to `lab-it` only when needed

Before writing or updating anything, establish whether currently available understanding is
sufficient and current:

- **Sufficient, current evidence already exists** — from this conversation, a recent
  investigation, or evidence directly verifiable against the real system right now. Use it
  directly. Don't repeat a full investigation just because a documentation workflow is starting.
- **Evidence is missing or stale.** Route the relevant investigation through `lab-it`'s canonical
  investigation method (its "Shared investigation and decision discipline") rather than
  duplicating that method here. Once `lab-it` returns verified findings, resume the documentation
  workflow.

This distinction determines the entry point, not the destination: the result is always a document,
or a review of one — never a `plan.md`. An approved `plan.md` stays `lab-it`'s output regardless of
which skill performed the underlying investigation; file extension does not decide ownership.

## Purpose and scope

Establish what the reader needs to understand, operate, extend, look up or decide, and who
will use the document. Architecture explains; operations instruct; technical references and
integrations deepen understanding or support lookup; costs justify spending; product-behavior
documents state rules precisely. These are examples, not mandatory modes or templates. A document
can combine purposes where useful.

Evidence includes verified code and runtime behavior, configuration, provider documentation,
approved decisions and explicit assumptions. A system need not be implemented yet: describe
approved designs as approved, estimates as estimates, and pending verification as pending.
Never invent rationale, turn a proposal into a verified fact, or decide an open product question.

For connected documentation, identify the primary overview and the authoritative home of
each detailed subject. Keep primary documents self-contained at their intended level;
link to supporting detail instead of repeating it. Match effort to importance and intended
use: operationally critical material needs stronger verification; supporting references
need accuracy and usable coverage, not endless editorial polish.

## Document a technical system or approved design

Triggered by a user request for new documentation. An existing document on the same subject does
not block an explicit request for another; that is the user's deliberate choice, not an error.
`rules/authoring.md` owns the procedure, including when the evidence recap needs confirmation
before writing.

## Update an existing document

Triggered when a document needs reconciling with verified current reality — a stale technical
claim, a stale evidence reference, changed configuration or runtime behavior, or a prior
documentation defect, not only a changed implementation. `rules/maintenance.md` owns the procedure,
from locating the target to the final review pass.

## Review a document

Triggered when the user asks whether a document is complete, accurate, or still fit for its
purpose. A standalone review reports findings only and changes nothing. `rules/review.md` owns the
evaluation; authoring and maintenance also call it before they finish.

## Ownership and handoff

This skill owns:

- creating new technical documentation in Markdown;
- maintaining and reconciling existing documentation with verified current reality;
- reviewing documentation for fitness for purpose.

This skill does not own:

- investigation from scratch when understanding is missing or stale (→ `lab-it`);
- architecture or product decisions reached with the user, or `plan.md` synthesis (→ `lab-it` —
  file extension does not decide ownership: an approved `plan.md` stays `lab-it`'s even though it is
  a `.md` file);
- generating API specifications from code;
- application implementation;
- debugging or diff review;
- feature classification and issue decomposition;
- GitHub issue mutation;
- delivery sequencing;
- Git workflow.

## Rule routing

These are loaded only when their workflow needs them — none is a universal prerequisite:

- new documentation → `rules/authoring.md`
- updating existing documentation → `rules/maintenance.md`
- writing guidance for both → `rules/doc-style.md`
- evaluation and findings → `rules/review.md`

## Output-specific non-negotiables

- Explain at the depth the purpose requires. Architecture documents explain why and how the design
  works, not method bodies. Operational documents may include exact commands, ordered procedures,
  safeguards and verification. References and integrations may include configuration, interface
  contracts and endpoints when the reader needs them.
- Ground material technical claims in concrete evidence or enforcement references when an
  identifiable mechanism exists; never force a misleading one.
- Don't copy an exhaustive specification that is authoritative and discoverable elsewhere — link to
  it. No implementation walkthroughs that don't serve the reader, and no unnecessary duplicated
  explanations across sections or connected documents.
- Not every document needs a limitations section. When limitations or deferred work materially
  affect understanding, state the reason rather than adding a generic TODO list.
- Writing and reviewing are separate steps. Authoring and maintenance are complete only after a
  `rules/review.md` pass and the correction of its material findings.
