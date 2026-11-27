# Authorization Pattern

## Use `#[Authorize]` attributes

Authorize a controller method with the `#[Authorize]` PHP attribute rather than an inline
`$this->authorize()` or `Gate::authorize()` call. This overrides Boost's inline and Form Request
`authorize()` examples: in this stack, a controller's authorization is declared on the method, where it
is visible next to the route action and runs before the method body.

```php
use Illuminate\Routing\Attributes\Controllers\Authorize;

#[Authorize('viewAny', Project::class)]
public function index(Request $request): Response { ... }

#[Authorize('create', Project::class)]
public function store(StoreProjectRequest $request, CreateProjectAction $action): RedirectResponse { ... }
```

The attribute registers Laravel's `Authorize` middleware for the route, so authorization runs before the
method body executes. Its first argument is the ability (a policy method name or a `UnitEnum`); its second
is a model class string, a route parameter name, or an array of them, or `null` for a gate-only check. The
attribute is repeatable. For its remaining options, check the installed framework's attribute class.

## `AuthorizesRequests` on the base `Controller`

When controllers authorize through the attribute, the base `Controller` does not need the
`AuthorizesRequests` trait — that trait exists to support the imperative `$this->authorize()` call.
Do not add it only for this pattern.

```php
abstract class Controller {}
```

## Authorizing `create`/`viewAny` on a child resource

`view`/`update`/`delete` authorize against an **already-bound model instance**: the route parameter
resolves to the real object before the attribute runs, and Laravel infers the policy from that object's
class automatically.

```php
#[Authorize('update', 'task')]
public function update(UpdateTaskRequest $request, Task $task, UpdateTaskAction $action): RedirectResponse { ... }
```

`create`/`viewAny` have **no instance to infer a policy from** — nothing exists yet. Passing only the
parent's route parameter (`'project'`) would authorize against the *parent's* policy, not the child's.
Name the child's policy class explicitly and pass the parent as the second element:

```php
#[Authorize('create', [Task::class, 'project'])]
public function store(StoreTaskRequest $request, Project $project, CreateTaskAction $action): RedirectResponse { ... }
```

```php
final class TaskPolicy
{
    public function create(User $user, Project $project): bool
    {
        return $project->members()->whereKey($user->id)->exists();
    }
}
```

Why the array form is required: the authorization middleware treats a string containing `\` as a
literal class name — used to resolve the policy, then stripped before the ability method is called — and
resolves any other string as a route parameter. `[Task::class, 'project']` resolves to
`["App\Models\Task", $projectInstance]`: the class-name string selects `TaskPolicy`, and the resolved
`$project` model is what actually reaches `create()`. `#[Authorize('create', Task::class)]` alone would
call `create($user)` with no parent argument at all — either an `ArgumentCountError`, or worse, a check
that never inspects which parent is involved.

## Testing

See `test-ownership.md`: the Policy test owns the permission matrix, and the HTTP test proves the gate is
wired up.
