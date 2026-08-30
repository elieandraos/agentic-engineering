# Actions Pattern

## Purpose

Business logic and mutations live in an **Action**, not the controller or the Form Request. See
`resource-controller-blueprint.md` for how an Action fits between the Form Request and the Resource in
the full controller composition — this file owns only the Action's own shape.

## Naming and location

- Place actions in `app/Actions/{Domain}/` — for example `app/Actions/Orders/`.
- Name each action `{Verb}{Model}Action` — for example `CreateOrderAction`, `UpdateOrderAction`,
  `ArchiveOrderAction`.
- The action's entry method is always named `handle()`.

## Action structure

```php
final class CreateOrderAction
{
    /**
     * @param  array{customer_id: int, notes?: string|null}  $attributes
     */
    public function handle(User $user, array $attributes): Order
    {
        return DB::transaction(function () use ($user, $attributes): Order {
            return Order::query()->create([
                ...$attributes,
                'created_by' => $user->id,
            ]);
        });
    }
}
```

## No HTTP concerns inside an Action

Never pass `Auth::user()`, `request()`, or any other HTTP-layer concern into an action. Resolve those in
the controller and pass plain values instead. An action that receives only plain arguments can also run
unchanged from a console command, job, or listener.

## Data payload convention

- Name the validated-array parameter `$attributes` — not `$data`, `$input`, or `$payload`.
- Add a `@param array{...}` PHPDoc shape on `handle()`, derived directly from the corresponding Form
  Request's `rules()`:
  - a `required` rule becomes a required key (no `?`);
  - a `nullable` rule becomes an optional key (`?`), typed `|null`;
  - rule-to-type mapping: `integer` maps to `int`; every other rule (`string`, `date`, an enum rule) maps
    to `string`.

## Reusing an Action from another Action

Inject it via the constructor — Laravel resolves the dependency automatically:

```php
final class CreateOrderAction
{
    public function __construct(private readonly AssignDefaultPricingAction $assignPricing) {}

    public function handle(User $user, array $attributes): Order
    {
        $order = DB::transaction(fn (): Order => Order::query()->create([
            ...$attributes,
            'created_by' => $user->id,
        ]));

        $this->assignPricing->handle($order);

        return $order;
    }
}
```

## Keep the transaction pure; dispatch side effects with `afterCommit()`

`DB::transaction()` should contain database writes only. Never send mail or dispatch a job from inside
it — chain `->afterCommit()` so Laravel defers the dispatch until the transaction actually commits.

```php
$order = DB::transaction(fn (): Order => Order::query()->create([...$attributes]));

SendOrderConfirmation::dispatch($order)->afterCommit();
```

| Scenario | Behavior without `afterCommit()` |
|---|---|
| DB write succeeds, dispatch throws | Transaction rolls back — the record is lost even though the write itself succeeded |
| DB write fails | Correct either way — nothing was dispatched |
| DB write succeeds, side effect fires, a later statement in the same request then fails | The side effect already fired for a record that no longer exists |

## Testing

See `testing-strategy.md` for what an Action test asserts and where it lives.
