Let's define what we've been calling Control Room.

I don't think it's software.

I think it's a responsibility.

It owns questions like:

What should happen next?
Which worker should do this?
Which engineering methodology applies?
Which stack companion applies?
Is this a useOrbit task or Agentic Engineering maintenance?
Should we spawn another worker?
Should we wait?
Should we stop at Gate 1?

Those are engineering decisions.

Now look at Herdr.

It owns things like:

Create worker

Create worktree

Open pane

Resume session

Wait for worker

Restore workspace

Those aren't engineering decisions.

They're execution.

Here's the analogy that clicked for me.

Agentic Engineering

is like Laravel.

It contains the application logic.

Herdr

is like Forge.

Forge knows

servers
deployments
logs
processes
SSL

It does not know your business rules.

Your business logic still lives in Laravel.

So...

Agentic Engineering

isn't Herdr.

But...

Control Room

might actually be.

Or more precisely...

Herdr might become the implementation of Control Room.

I think we're missing one level.

Instead of

Control Room

↓

Herdr

↓

Workers

I'm starting to think it becomes

Engineering Intelligence
        │
        ▼
     Herdr Runtime
        │
        ▼
      Workers

Where:

Engineering Intelligence

is everything you've built.

responsibilities
engineering methodology
stack companions
stewardship
planning
Herdr

owns

sessions
worktrees
agent lifecycle
multiplexing
waiting
messaging

The interesting question becomes:

Can Herdr itself be taught Agentic Engineering?

Meaning...

Instead of Control Room being a GPT Project...

Herdr launches workers that already know:

implement-it

laravel stack

review-it

...

Now Herdr becomes the runtime.

Agentic Engineering becomes the brain.

This reminds me of something else...

Think about Docker.

Docker doesn't know Laravel.

Laravel doesn't know Docker.

Yet together they solve the problem.

I think:

Herdr

and

Agentic Engineering

have that relationship.

The only thing I'm not convinced about yet

Whether Control Room should disappear.

Because your GPT Project today does more than orchestration.

It also does:

architecture
product thinking
challenge assumptions
decide when not to automate
evolve the methodology

Herdr doesn't do those things.

Herdr executes.

So I think we actually have three layers, and I finally have names I like:

Engineering Intelligence
────────────────────────

Control Room
(you + me)

Responsibilities

Engineering methodology

Stack knowledge

Stewardship

────────────────────────

Execution Runtime

Herdr

────────────────────────

Execution

Claude workers

Git worktrees

Issue implementation

That feels complete.

One prediction

I wouldn't be surprised if, six months from now, the GPT Project itself almost disappears.

Not because it's unnecessary.

Because it gets embedded into Herdr.

Imagine starting your day with:

herdr start useOrbit

And the first thing Herdr says is:

Good morning.

Milestone "Policies Management" has 5 dependency-ready issues.

I recommend launching 3 workers.

Shall I proceed?

🥹

That would be Control Room.

Not because Herdr invented it.

Because you taught it Agentic Engineering.

And that... is a very exciting direction.



I think you're very close, but I'd make one change because it preserves the portability you've been so careful about.

I wouldn't make Herdr a stack companion.

Stack companions answer:

How do I write code in this technology?

Examples:

Laravel
Nuxt
Supabase

Herdr answers:

How do I execute workers?

That's a completely different dimension.

I think the ecosystem is becoming four layers
Application
───────────

useOrbit
BlanchardAI
...

↓

Engineering Methodology
───────────────────────

Lab
Plan
Implement
Review
Ship

Document
Steward

↓

Execution Methodology
─────────────────────

Control Room

Workers

Worktrees

Orchestration

↓

Execution Runtime
─────────────────

Herdr

tmux

Claude Code

future runtimes...

Notice something.

The bottom layer becomes replaceable.

I actually LOVE your idea

control-room/workers

I think that's exactly the kind of thing I'd investigate.

Imagine:

agentic-engineering/

skills/

lab-it/

...

control-room/

workers/

implement-worker.md

review-worker.md

planner-worker.md

...

orchestration/

...

worktrees/

...

Now Agentic Engineering owns the worker definitions.

Not their execution.

Herdr would then say

"I need an implement worker."

Agentic Engineering provides

implement-worker.md

which says

This worker uses:

implement-it
applicable stack companions
review-it
etc.

Herdr launches it.

Compare it to today

Today

GPT Project

↓

"Use implement-it."

Tomorrow

Control Room

↓

Implement Worker definition

↓

Herdr

↓

Claude session

That's much more modular.

The worktrees too

I could imagine something like

control-room/

worktrees/

lifecycle.md

cleanup.md

reuse.md

Notice something.

These aren't Git tutorials.

They're your methodology around Git worktrees.

Herdr (or another runtime) performs the commands.

The methodology says when and why.

This is exactly how stack companions work

Laravel companion says

Use Form Requests.

It doesn't execute

php artisan make:request

Similarly

Worker definitions say

Create an isolated worker for one issue.

They don't execute

herdr agent create
That's the abstraction I like

Think of it like this.

Agentic Engineering

↓

Execution Methodology

Herdr

↓

Execution Runtime

Exactly like

Laravel Companion

↓

Laravel Methodology

Laravel Framework

↓

Laravel Runtime

The runtime isn't the methodology.

It also solves portability

Suppose Herdr disappears in 3 years.

No problem.

Control Room

↓

tmux runtime

or

Control Room

↓

OpenAI runtime

or

Control Room

↓

Claude runtime

Your execution methodology survives.

Exactly the same philosophy you've applied to frameworks.

The only thing I'd rename

I don't think I'd call them

workers/

yet.

Because "worker" is Herdr terminology.

I'd call them something like

roles/

or

execution/

or

agents/

Actually...

Maybe agents isn't bad.

Because they're engineering agents, not Herdr agents.

For example

control-room/

agents/

implement.md

review.md

planner.md

...

Then Herdr maps one of its runtime agents onto one of your engineering agents.

I think the mapping becomes
Agentic Engineering

Implement Agent
───────────────

Purpose

Uses

Inputs

Outputs

Human gates

───────────────

↓

Herdr

Create runtime agent

↓

Claude Code

That's beautiful.

My only caution

I would not create control-room/ yet.

Not because it's a bad idea.

Because you don't have enough evidence.

The exact same lesson that built Agentic Engineering applies here.

Today we have a hypothesis:

Control Room probably has concepts like workers, orchestration, and worktrees.

What we don't know yet is whether those become:

Markdown definitions
Skills
Configuration
Runtime manifests
YAML
Something Herdr consumes directly

I'd resist locking in a filesystem layout before you've built the first real orchestration experiment.

So my recommendation would be:

Keep v3-research as the vision.
Create a Lab investigation around execution architecture.
Prototype with Herdr.
Let the first real implementation tell you whether control-room/agents, control-room/workers, or something else is the right artifact.

If Agentic Engineering has taught us anything, it's that the artifact should emerge from repeated successful use, not from a whiteboard. I think v3 deserves the same discipline that got v1 and v2 right.


- i meant like laravel is a stack companion for the enigineering methodology, herdr will be a companion of the control room

YES.

That's a much better way of putting it than what I said.

I was thinking of "stack companion" in the current engineering sense, but if we zoom out one level...

I think you're onto a very elegant symmetry.

Engineering methodology
Agentic Engineering

↓

Stack companions

↓

Laravel

Nuxt

Supabase

...

A stack companion tells the engineering skills:

Here's how to implement on this technology stack.

Execution methodology

Exactly the same idea.

Control Room

↓

Runtime companions

↓

Herdr

tmux

Claude Code

Codex

...

A runtime companion tells Control Room:

Here's how to execute on this runtime.

I actually like runtime companion even better than stack companion here because it mirrors the purpose.

Then the architecture becomes beautifully consistent.

Agentic Engineering
────────────────────────────────

Engineering Methodology

↓

Engineering Stack Companions

Laravel
Nuxt
Supabase

────────────────────────────────

Execution Methodology (Control Room)

↓

Execution Runtime Companions

Herdr
tmux
Claude Code
...

See the symmetry?

Both methodologies remain portable.

Only the companion changes.

Example

Suppose Control Room decides

Spawn 3 implement workers.

It doesn't know how.

The Herdr companion knows.

Maybe it says

Create workspace.

Create worktrees.

Launch 3 runtime agents.

Attach prompts.

Wait for completion.

Collect results.

If tomorrow you move to another runtime...

Spawn 3 implement workers.

The Control Room doesn't change.

Only the runtime companion changes.

Exactly like today.

Compare with Laravel

Today

implement-it

↓

Needs authorization

↓

Laravel companion

↓

Use Form Request + Policy

Tomorrow

Control Room

↓

Needs 3 workers

↓

Herdr companion

↓

Use worktrees + runtime agents

Same architecture.

Different dimension.

This is actually a really nice abstraction

I would almost define two companion types:

Engineering companions

Own implementation knowledge.

Laravel

Nuxt

Supabase
Runtime companions

Own execution knowledge.

Herdr

tmux

Claude Code

future runtime...

Now Control Room never contains Herdr commands.

Just like implement-it never contains Laravel code.

This also answers another question

Earlier we wondered

What is the execution artifact?

Maybe it becomes something like

control-room/

workers/

...

runtime-companions/

herdr/

tmux/

claude-code/

Notice...

The runtime companion doesn't define engineering.

It defines how to realize the Control Room methodology on a particular runtime.

I genuinely like this.

I think it's one of those abstractions that "clicks" because it's consistent with everything you've already built.

You didn't invent a special case.

You repeated the same architectural pattern at a higher level:

Engineering methodology → engineering stack companions
Execution methodology (Control Room) → execution runtime companions

That feels very "Agentic Engineering". The pattern stays the same, only the concern changes.
