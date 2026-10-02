# Consumer-Side Agentic Engineering Agent

What you're describing is **not another lifecycle skill** and not a worker orchestrator. It is a **consumer-side Agentic Engineering agent** whose job is to maintain the relationship between a real project and the Agentic Engineering ecosystem.

The distinction is important.

## 1. What the Agent is

The Agent lives with the consuming project and is available during normal engineering work.

Its core purpose:

> **Notice, investigate, and manage reusable engineering knowledge discovered while using Agentic Engineering in a real project.**

The project is where the evidence appears. The Agent is the bridge that can carry good evidence back into the canonical Agentic Engineering repository.

The mental model is:

```
                        CONSUMING PROJECT
                              │
                    normal engineering work
                              │
                    "this feels reusable"
                              │
                              ▼
                         THE AGENT
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
       inspect             classify            compare
       code/tests          ownership            existing
       history             evidence             guidance
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
                    "candidate for ecosystem?"
                              │
                    ┌─────────┴─────────┐
                    │                   │
                   no                  yes
                    │                   │
                 project             Agentic
                 knowledge          Engineering
                                      repo
                                        │
                         branch → evidence → change
                                        │
                                     review
                                        │
                                       PR
                                        │
                                     release
                                        │
                              refresh consumers
```

The important thing is that **the Agent does not replace the existing skills**. It uses them.

---

# 2. Its responsibilities

I'd define seven responsibilities.

### A. Detect candidate findings

The Agent can be invoked explicitly when you say things like:

> “Could this be part of the Laravel stack?”

> “This feels like a reusable pattern.”

> “Is this something we should put into Agentic Engineering?”

It can also eventually notice something during a session and say:

> “This looks like a possible reusable stack finding. Want me to investigate it?”

But **detection must never imply promotion**.

A surprising implementation is not automatically a skill rule.

---

### B. Investigate the finding

The Agent reconstructs enough evidence to answer:

> What actually happened?

It can inspect:

- current implementation;
- tests;
- project rules;
- installed skills and versions;
- existing canonical guidance;
- relevant repository history;
- runtime/tool evidence when available;
- previous retained evidence.

It can invoke or compose existing capabilities where appropriate.

For example:

```
Finding
  ↓
"Could this be a Laravel rule?"
  ↓
inspect current code
  ↓
inspect laravel-inertia-stack
  ↓
inspect authoring methodology
  ↓
inspect prior evidence
```

This is where **`steward-it` can still participate**, but only when its actual responsibility is relevant.

The distinction remains:

```
steward-it
→ "Why was this session difficult / inefficient / off course?"

Agent
→ "Does this observation belong in the reusable ecosystem, and what should happen next?"
```

That's clean.

---

### C. Classify ownership

The Agent should explicitly classify the observation before proposing a change.

For example:

```
project knowledge
stack knowledge
portable methodology
skill behavior
prompt problem
execution mistake
runtime/tool limitation
framework knowledge
not reusable
```

And then:

> **Who owns this knowledge?**

Maybe it belongs in:

- `laravel-inertia-stack`;
- `review-it`;
- `lab-it`;
- authoring methodology;
- skill consumption guidance;
- project rules;
- nowhere.

This is important because otherwise this Agent becomes a **“put everything into the skill” machine**.

---

### D. Evaluate whether it deserves canonical guidance

The Agent should know the **skill-authoring methodology** and apply it.

It should ask:

> Is this reusable?

> Is it non-obvious?

> Is the guidance currently missing or too narrow?

> Is there enough evidence?

> Is the proposed rule the smallest useful abstraction?

> Is there an existing rule we should refine instead of creating a new one?

> Is this actually framework knowledge that the skills should not own?

This is the part we just exercised with #407.

The Agent's output might be:

```
Candidate: MODIFY

Owner:
laravel-inertia-stack / request-normalization.md

Evidence:
strong

Reason:
Existing rule already covers query-state restoration,
but its enum-focused example failed to communicate the
same boundary for scalar IDs.

Smallest change:
broaden the existing rule and add one neutral ID example.
```

That should feel like **our current reasoning, operationalized**.

---

# 3. It knows the Agentic Engineering ecosystem

This is where those documentation pieces you mentioned become important.

The Agent should be aware of three different knowledge layers.

### The authoring methodology

How reusable guidance is created and evolved.

It knows things like:

```
observed behavior
→ evidence
→ classification
→ reusable rule
→ correct owner
→ activation scope
→ example
→ validation
→ PR
→ release
```

### The skill ecosystem

It knows what each existing skill owns.

For example:

```
lab-it
plan-it
implement-it
review-it
ship-it
steward-it
laravel-inertia-stack
...
```

So it can ask:

> “Am I putting this in the correct place?”

### Skill consumption

It also knows how the **consumer project** installs and refreshes the ecosystem.

That means it can understand:

```
installed version
lock state
refresh mechanism
skill directories
consumer verification
```

So after a release it can potentially complete:

```
release v2.2.3
        ↓
refresh useOrbit
        ↓
verify installed skills
        ↓
report result
```

That is a fundamentally different responsibility from the lifecycle skills.

---

# 4. The Agent can manage the cross-repository workflow

This is the part we've done manually enough times that I think it deserves to become explicit.

Once a finding is approved for canonical promotion, the Agent can own the mechanical bridge:

```
consumer project
      ↓
prepare evidence
      ↓
Agentic Engineering repo
      ↓
create branch
      ↓
apply approved skill change
      ↓
validate
      ↓
commit
      ↓
push
      ↓
open PR
```

Then, **after human approval**:

```
merge
  ↓
tag
  ↓
release
  ↓
refresh consuming project
  ↓
verify
```

The Agent therefore understands both repositories:

### Consumer repository

```
current stack
installed skills
refresh command
project-specific conventions
```

### Canonical repository

```
skill authoring
PR conventions
branch conventions
release conventions
no-trailer policy
research/evidence structure
```

That knowledge should be **configuration/data**, not hard-coded assumptions.

---

# 5. Human approval remains central

This Agent should be powerful but not self-authorizing.

I'd make these explicit boundaries:

### The Agent may investigate automatically.

### The Agent may recommend promotion.

### The Agent may prepare a patch.

### The Agent may prepare a branch and PR after you authorize that action.

### The Agent must not silently:

- change canonical skills;
- merge its own PR;
- publish a release;
- turn a project observation into canonical doctrine;
- rewrite history;
- refresh the consumer unexpectedly.

So:

```
Agent:
"I think this belongs in laravel-inertia-stack."

Human:
"Yes."

Agent:
"Here's the patch and PR."

Human:
"Merge."

Agent:
"Okay, release?"

Human:
"Yes."

Agent:
"Refresh useOrbit?"
```

That feels right.

---

# 6. It should also know how to resume this work

This is another important difference from a normal skill.

The Agent may discover:

> “This finding is not ready yet.”

So it should be able to retain a **small evidence record** and come back later.

For example:

```
Finding #407
status: candidate
owner: laravel-inertia-stack
candidate changes:
  - query-state
  - option projections
evidence: sufficient
PR: #15
release: pending
```

Then later:

> “Finish the Agentic Engineering update for the finding we discussed.”

It can inspect the current remote state and resume.

That means the Agent becomes a **long-lived relationship manager**, while the skills remain task-oriented.

---

# 7. What the Agent is NOT

This is worth locking down early.

### Not an orchestrator

It does not coordinate worker A/B/C during normal feature delivery.

### Not `steward-it`

It does not primarily diagnose slow, difficult, or broken sessions.

### Not `lab-it`

It can use Lab-style investigation, but it doesn't replace Lab's product/architecture investigation responsibility.

### Not `ship-it`

It may eventually invoke the release workflow, but it doesn't redefine release methodology.

### Not a generic project manager

No backlog babysitting, sprint management, reminders, or “what should we build today?” behavior.

### Not an autonomous Agentic Engineering maintainer

Human approval remains the publication boundary.

---

# 8. Where I think it should live

This is the interesting architectural question.

I **would not put it inside `skills/` as another normal skill**.

That would blur the exact boundary we're trying to establish.

Instead, I see:

```
agentic-engineering/
├── skills/
│   ├── lab-it/
│   ├── plan-it/
│   ├── implement-it/
│   ├── review-it/
│   ├── ship-it/
│   ├── steward-it/
│   └── laravel-inertia-stack/
│
├── docs/
│   ├── skill-authoring-methodology.md
│   ├── skill-consumption.md
│   └── ...
│
└── ??? agent distribution ???
```

The Agent is a **consumer companion**, so I would investigate an artifact such as:

```
agents/
└── <eventual-agent-name>.md
```

which a consuming project installs alongside its skills:

```
consumer/
├── .agents/skills/
│   └── ...
└── .claude/agents/
    └── <agent>.md
```

The exact installation mechanism is something I'd research rather than lock now, because **skills and Claude agents are different runtime primitives**.

That's one of the places where I would deliberately avoid designing ahead of the evidence.

---

# 9. The Agent's knowledge should remain layered

I think this is especially important for portability.

The Agent should not contain:

> “useOrbit does X.”

Instead:

```
Agent definition
    ↓
portable responsibilities
    +
Agentic Engineering knowledge
    +
consumer project configuration
    +
runtime capability
```

So the consumer can provide something like:

```yaml
agentic_engineering:
  repository: elieandraos/agentic-engineering
  branch: main
  installed_version: v2.2.3
  refresh_command: npm run skills:refresh
  canonical_workflow: ...
```

while project-specific things live in the project.

That preserves your boundary:

> **methodology ≠ stack ≠ project ≠ runtime**

which has become one of the most important architectural ideas in this whole system.

---

# 10. The lifecycle I'd give the Agent

Eventually I'd want its mental model to look something like:

```
OBSERVE
   ↓
INVESTIGATE
   ↓
CLASSIFY
   ↓
EVALUATE
   ↓
PROPOSE
   ↓
HUMAN APPROVAL
   ↓
AUTHOR
   ↓
VALIDATE
   ↓
OPEN PR
   ↓
HUMAN REVIEW
   ↓
MERGE
   ↓
RELEASE
   ↓
REFRESH CONSUMERS
   ↓
VERIFY
```

But importantly, **not every invocation goes through the whole thing**.

You might just ask:

> “Is this a stack finding?”

and stop at `EVALUATE`.

Or:

> “Prepare the Agentic patch.”

and start at `AUTHOR`.

Or:

> “Release the approved v2.2.3 PR and refresh useOrbit.”

and start at `RELEASE`.

So this is more like a **stateful capability around the ecosystem** than another rigid workflow.

---

## And I think this finally explains why the old “orchestrator” idea felt slightly wrong

We kept trying to answer:

> **Who coordinates the workers?**

But the repeated real-world need was actually:

> **Who coordinates the relationship between a project consuming Agentic Engineering and the canonical system that evolves it?**

That's the Agent.

The worker runtime doesn't really need another boss.

**The ecosystem needs a caretaker that lives at the edge where real engineering happens.**

That's a much more interesting architecture, and unlike the original Control Room idea, we've already accumulated repeated evidence for almost every part of it. The next step should be a small **Agent definition/research pass**, not implementation.
