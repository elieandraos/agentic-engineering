# Creating new technical documentation

This file owns the procedure for a new document, triggered from `SKILL.md`'s "Document a technical
system or approved design." Updating an existing document belongs to `rules/maintenance.md`.

## 1. Establish evidence and purpose

Confirm the subject, the intended audience, the purpose and the scope. Reuse current evidence —
implementation, configuration, schema, tests, runtime behavior, provider documentation, approved
decisions or cost assumptions — and route missing or stale evidence through `lab-it`, per
`SKILL.md`.

Identify the central idea or the reader task the document serves. For architecture, this is the
architectural center of gravity; for an operational document, the task the reader must carry out
safely; for a product-behavior document, the rules and states the reader must apply. For connected
documentation, identify which document owns each subject and which existing documents already
reference it.

## 2. Recap, and confirm when confirmation is still needed

Write the recap directly as chat output, not as a file. Keep it bullet-driven and honest about
gaps. Cover whichever of these the subject actually has, with concrete evidence references where
useful: the problem or goal, the central idea, the main components or steps, ownership and
boundaries, runtime behavior, the data model, integration seams, configuration, costs, rules and
states, security, testing, decisions, and remaining gaps. Distinguish verified behavior from
approved plans and estimates. Don't invent a data model, lifecycle, security boundary, or
integration seam the subject doesn't have just to fill out the list.

Decide whether the recap needs the user's confirmation before writing:

- **Confirm** when the understanding, the scope, or a material decision behind the document has
  not been confirmed. Stop and wait. A correction here is real signal about what the document must
  get right.
- **Reuse an applicable existing approval** when the user has already approved the substance — in
  this conversation or another identifiable context — and has explicitly authorized writing the
  document. An approval is applicable only when it covers this recap's understanding, scope, and
  material decisions. Present the recap as the basis you are writing from and proceed. Don't ask
  for the same approval twice.
- **Stop again** when the recap diverges materially from what was approved, or when writing
  surfaces a new unresolved decision. Return that decision to the user, or to `lab-it` when it
  needs fresh investigation or an architecture decision.

In every other case, including an unclear one, confirm.

## 3. Write the document

Write only after the recap is confirmed or an applicable existing approval is reused.

- Decide the structure from the confirmed purpose and central idea, not a fixed section
  inventory. `rules/doc-style.md` owns the writing guidance.
- Save a new document under the consuming repository's `docs/` directory, unless the user or the
  project's own convention names another location. Create the directory if it doesn't exist. If
  the location can't be written, explain the limitation, ask how to proceed, and never report the
  document as saved.
- Run `rules/review.md` against the saved document. Correct the material findings it reports, then
  verify the corrected claims against the same evidence. Stop and return to the user when a
  correction requires an unresolved decision.
- Report the document's path, any material findings you corrected, and any finding left open with
  its reason.
