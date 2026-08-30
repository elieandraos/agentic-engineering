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

An Action must never resolve its own state by calling `request()`, `Auth::user()`, or any other
HTTP-layer global inside `handle()`. The controller resolves the current user, a route-bound model, or
any other value it has access to, and passes it into the Action as a plain, already-resolved argument
(a `User`, a `Model`, a scalar, a validated array — never a live request or auth facade call). An action
built this way can also run unchanged from a console command, job, or listener, none of which have an
HTTP request to resolve state from.

## Data payload convention

- Name the validated-array parameter `$attributes` — not `$data`, `$input`, or `$payload`.
- Add a `@param array{...}` PHPDoc shape on `handle()`, derived from the corresponding Form Request's
  `rules()` and its actual validated shape — not from a fixed rule-to-type table. Presence and
  nullability are separate axes:
  - **Key presence** — whether the key is guaranteed to appear in the array at all — comes from
    `required`, `present`, and `sometimes`. A `sometimes` rule, or a rule only conditionally applied
    (`Rule::when()`, `exclude_unless`, and similar), makes the key optional (`?`) in the shape regardless
    of nullability.
  - **Nullability** — whether the value itself may be `null` when the key is present — comes from
    `nullable`. It is independent of presence: a required, nullable field is always present but may be
    `null` (`key: string|null`); an optional, non-nullable field may be absent but is never `null` when
    it is present (`key?: string`).
  - **Type** each key from its actual validation rule, not a blanket mapping to `string`: `integer` →
    `int`; `boolean` → `bool`; `array`/`array:...` → `array` (refine the shape further when the array's
    own structure is known); `numeric`/`decimal` → `int|float`, or the project's actual numeric type; a
    backed-enum rule (`new Enum(...)`) → that enum's backing type, or the enum class itself when the
    Action consumes the enum instance directly; `string`, `date`, and other string-shaped rules →
    `string`.

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

## Keep external side effects out of the transaction; dispatch them with `afterCommit()`

`DB::transaction()` may contain whatever reads, locks, and writes the atomic unit of work actually
needs — a transaction is not limited to a single write. What it must not contain is a side effect
external to the database: sending mail, dispatching a queued job, calling another service. Those run
outside the transaction, chained with `->afterCommit()` so Laravel defers them until the transaction
actually commits.

```php
$order = DB::transaction(function () use ($attributes): Order {
    $order = Order::query()->create($attributes);
    $order->lineItems()->createMany($attributes['line_items']);

    return $order;
});

SendOrderConfirmation::dispatch($order)->afterCommit();
```

`afterCommit()` queues the dispatch to run once the outermost transaction it was chained within
commits — not immediately, and not at all if that transaction rolls back. It has no effect on the
transaction itself and cannot retroactively undo a commit that already happened; it only controls when
the dispatch fires relative to that commit.

| Scenario | Behavior without `afterCommit()` (dispatched synchronously, inside the transaction) | Behavior with `afterCommit()` |
|---|---|---|
| DB write succeeds, then the dispatched job/mail throws | The exception can trigger a rollback of the just-written data, discarding a persisted record to unwind a failure in an unrelated side effect | The write already committed before the dispatch could run; the side effect firing or failing afterward cannot affect it |
| DB write fails | The dispatch never runs — correct either way | The dispatch never runs — correct either way |

## Testing

See `testing-strategy.md` for what an Action test asserts and where it lives.
