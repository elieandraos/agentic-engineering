# Eloquent Attributes

Conventions for computed model attributes. `laravel-best-practices` already covers local scopes via
the `#[Scope]` attribute — see "Local scopes" below for the one narrow addition this file makes to
that baseline.

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

`Illuminate\Database\Eloquent\Casts\Attribute` supports `make()`, `get()`, and `set()` for accessors
and mutators. Confirm the project's installed Laravel version supports the API before relying on it.

## Local scopes

Defining a local scope with the `#[Scope]` attribute is already `laravel-best-practices`'s standard
guidance; this file does not restate that mechanic. It requires a Laravel version that provides
`Illuminate\Database\Eloquent\Attributes\Scope` — confirm this class exists in the project's installed
`laravel/framework` version before relying on it.
