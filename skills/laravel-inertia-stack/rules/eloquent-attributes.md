# Eloquent Attributes

Conventions for model responsibilities, computed attributes and local scopes. `laravel-best-practices`
already covers the `#[Scope]` attribute's own mechanics.

## Model responsibilities

Keep Eloquent models focused on persistence, relationships, casts, scopes and attributes.
Prefer a focused support class for a reusable business calculation that needs external
context, such as a business date or organization setting. Keep that context explicit
rather than resolving it implicitly in an accessor. Avoid model forwarding methods
and concerns that merely delegate to another class without adding meaningful behavior
or reuse. Domain methods that naturally belong to a model remain valid. Do not extract
simple model-local behavior solely to satisfy a layering preference.

Actions retain ownership of business mutations and transactions; support classes can
supply the reusable calculation without performing the mutation.

## Computed attributes

Expose a derived model property as an `Attribute` accessor when the value is naturally consumed as a
model attribute, especially when several consumers need the same derived value. Prefer a protected
accessor returning `Attribute` over a public helper method that represents the same property.

```php
use Illuminate\Database\Eloquent\Casts\Attribute;

final class Client extends Model
{
    protected function fullName(): Attribute
    {
        return Attribute::make(
            get: fn () => $this->client_type === ClientType::Company
                ? $this->company_name
                : trim("{$this->first_name} {$this->last_name}"),
        );
    }
}
```

Consume the derived value through Eloquent's attribute interface, using the snake-cased property name:

```php
$client->full_name;
```

Reserve an accessor for a derived property, not as a generic replacement for domain behavior. A
reusable operation with behavior or side effects stays a method or an Action, not an Eloquent
attribute.

## Local scopes

Which scope style a new scope uses depends on the project's established position:

- **No established position** — define the scope with the `#[Scope]` attribute, not the
  `scope`-prefixed method-name convention.
- **The project consistently uses `scope`-prefixed methods** — match that style for compatibility.
- **The project has explicitly adopted an incremental migration to `#[Scope]`** (recorded in its
  project instructions or rules) — new scopes use the attribute, including on a model whose existing
  scopes still use the prefix. Convert existing scopes only when the task includes that migration.

```php
// The attribute style
#[Scope]
protected function filter(Builder $query, QueryFilter $filters): Builder
{
    return $filters->apply($query);
}

// The scope-prefixed style
public function scopeFilter(Builder $query, QueryFilter $filters): Builder
{
    return $filters->apply($query);
}
```

Both styles are called the same way (`Order::query()->filter($filters)`), so a migration does not change
callers.
