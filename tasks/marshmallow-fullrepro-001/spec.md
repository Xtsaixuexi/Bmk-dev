<!-- INTERNAL
task_id: marshmallow-fullrepro-001
spec_version: v1
delta: standardized current-main task packet
source_boundary: public documentation, public API surface, and existing task artifacts
-->

# Marshmallow Specification

## Product Overview

marshmallow helps you describe the shape of your application data once and reuse that description when sending data out, accepting data in, validating user input, and building application objects. You define a `Schema` with field attributes, add validators and hooks where needed, and then call `dump`, `load`, `validate`, `dumps`, or `loads` depending on the direction of the workflow.

A schema is the shared contract for these operations. The same field declaration controls which keys are produced, which keys are accepted, how values are converted, how nested objects are represented, and how validation errors are reported.

## Scope

The API described here is the part of marshmallow needed to define schemas, convert data, validate input, report errors, and extend those behaviors in normal application code. It includes:

- the top-level `marshmallow` imports used to define schemas and handle errors;
- `Schema`, `Schema.Meta` options, schema construction options, `dump`, `dumps`, `load`, `loads`, `validate`, `from_dict`, and public extension hooks;
- the `marshmallow.fields` namespace, including base field options, common scalar fields, collection fields, nested fields, computed fields, constants, enum, URL/email/IP/UUID, and custom field extension;
- the `marshmallow.validate` class-based validators and custom callable validators;
- pre/post load and dump decorators, field validator decorators, and schema validator decorators;
- `ValidationError` and other public exception classes;
- class registry behavior needed by string-named nested schemas;
- `marshmallow.orderedset.OrderedSet` for ordered field-name collections;
- the experimental typed `Context` helper;
- selected public utility helpers where they are part of documented user workflows.

This specification does not cover third-party integrations, historical compatibility APIs, private attributes, private helper functions, exact implementation storage, or exact wording of error messages.

## Installable Surface

The package name is `marshmallow`. The main public import styles are:

```python
import marshmallow
from marshmallow import Schema, SchemaOpts, ValidationError, fields, validate
from marshmallow import EXCLUDE, INCLUDE, RAISE, missing
from marshmallow import pre_load, post_load, pre_dump, post_dump
from marshmallow import validates, validates_schema
from marshmallow.experimental.context import Context
```

Documented submodules include `marshmallow.fields`, `marshmallow.validate`, `marshmallow.decorators`, `marshmallow.exceptions`, `marshmallow.class_registry`, `marshmallow.utils`, and `marshmallow.experimental.context`.

## Quick Start

Define a schema by assigning field instances to class attributes. Use `dump` when you have Python objects or mappings and want native serialized data. Use `load` when you have input data and want validated Python values. Use `post_load` when loaded dictionaries should become application objects.

```python
from marshmallow import Schema, ValidationError, fields, post_load, validate

class UserSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    age = fields.Integer(validate=validate.Range(min=0))

    @post_load
    def make_user(self, data, **kwargs):
        return data

schema = UserSchema()
outgoing = schema.dump({"name": "Ada", "email": "ada@example.com", "age": 37})
incoming = schema.load({"name": "Ada", "email": "ada@example.com", "age": 37})
try:
    schema.load({"name": "Ada", "email": "not-an-email"})
except ValidationError as err:
    errors = err.messages
```

## Public API

### Top-Level Names

`Schema` is the base class for declaring serialization and deserialization contracts. `SchemaOpts` represents defaults derived from `Schema.Meta` options and is importable as part of the public API, but users normally configure options through `class Meta` rather than constructing `SchemaOpts` directly.

`fields` is the public namespace for field classes. `validate` is the public namespace for validator classes.

`ValidationError` is raised when data cannot be deserialized or validated. `EXCLUDE`, `INCLUDE`, and `RAISE` are the allowed unknown-field policies. `missing` is a sentinel meaning that a value is absent; it is distinct from `None`.

`pre_load`, `post_load`, `pre_dump`, `post_dump`, `validates`, and `validates_schema` are decorators used on `Schema` methods.

### Schema Declaration

A schema is declared by subclassing `Schema` and assigning field instances as class attributes:

```python
class UserSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email()
    created_at = fields.DateTime(dump_only=True)
```

Each declared field becomes a named part of the schema. Field names are used as Python-side result keys unless a field uses `attribute` or `data_key` to change object access or external data keys.

Schemas can also be generated at runtime:

```python
UserSchema = Schema.from_dict({"name": fields.String(), "email": fields.Email()})
```

`Schema.from_dict(fields, *, name="GeneratedSchema")` returns a `Schema` subclass with the provided field mapping.

### Schema Construction

`Schema` accepts keyword-only configuration:

```python
Schema(
    *,
    only=None,
    exclude=(),
    many=None,
    load_only=(),
    dump_only=(),
    partial=None,
    unknown=None,
)
```

`only` limits the active fields. `exclude` removes fields from the active set. Both accept collections of field names, and nested fields may be addressed with dotted paths such as `"author.email"`. Passing a plain string where a collection of field names is required raises `StringNotCollectionError`.

`many` sets the default collection mode for `dump`, `dumps`, `load`, `loads`, and `validate`. A per-call `many` argument overrides the instance default.

`load_only` fields are accepted during loading and omitted from dump output. `dump_only` fields appear during dumping and are ignored during loading.

`partial` controls required-field behavior during loading. `partial=True` ignores missing required fields throughout the schema. A collection of field names ignores missing required checks only for those fields. Dotted field names apply to nested schemas.

`unknown` controls keys in input data that do not match any load field. `RAISE` reports them as errors, `EXCLUDE` drops them, and `INCLUDE` keeps them in deserialized output. A constructor value overrides `Meta.unknown`; a per-call value overrides both.

### Schema Meta Options

A schema may define `class Meta` for default behavior. Publicly relevant options include:

- `fields`: a field-name collection limiting declared or generated fields;
- `exclude`: a field-name collection removed from the schema;
- `dateformat`, `datetimeformat`, and `timeformat`: default formats for date/time fields;
- `render_module`: module used by `dumps` and `loads`, defaulting to a JSON-compatible module;
- `index_errors`: when true, collection errors are keyed by item index;
- `load_only` and `dump_only`: default field-name sets for load-only and dump-only behavior;
- `unknown`: default unknown-field policy;
- `register`: whether the schema class participates in string-name registry lookup for nested fields;
- `ordered`: whether serialized mapping output preserves declaration order using an ordered mapping type;
- `include`: extra fields to include with declared fields.

Schema classes may set `set_class` to a set-like class used for ordered field-name collections such as `only`, `exclude`, `load_only`, and `dump_only`. The default preserves declared field ordering. A compatible custom `set_class` must support construction from an iterable, membership checks, iteration in insertion order, and normal mutable-set operations used to add or discard field names.

### Schema Methods

`dump(obj, *, many=None)` serializes an object or collection to Python data structures. It does not run load-time validators for performance. Missing dump values are omitted unless a field supplies `dump_default`.

`dumps(obj, *args, many=None, **kwargs)` serializes with `dump` and then encodes the result with the schema render module's `dumps` function. Extra positional and keyword arguments are passed to that JSON encoder.

`load(data, *, many=None, partial=None, unknown=None)` deserializes and validates mapping data. On success it returns Python data structures keyed by field name or field `attribute`. On failure it raises `ValidationError` containing all collected errors and any partial valid data.

`loads(s, *args, many=None, partial=None, unknown=None, **kwargs)` decodes a string with the schema render module's `loads` function and then calls `load`. Extra arguments are passed to the decoder.

`validate(data, *, many=None, partial=None)` validates input data and returns an error dictionary. It returns an empty dictionary on success instead of raising.

`handle_error(error, data, *, many, **kwargs)` is called when loading raises `ValidationError`. Override it to translate, log, or re-raise errors.

`get_attribute(obj, attr, default)` defines how dump retrieves values from objects. The default behavior supports attribute and mapping access.

`on_bind_field(field_name, field_obj)` runs when a field is bound to a schema and can be overridden to customize public field behavior.

### Base Field Options

All field classes share the base field contract:

```python
fields.Field(
    *,
    load_default=missing,
    dump_default=missing,
    data_key=None,
    attribute=None,
    validate=None,
    required=False,
    allow_none=False,
    load_only=False,
    dump_only=False,
    error_messages=None,
    metadata=None,
)
```

`load_default` supplies a value when an input key is missing during load. `dump_default` supplies a value when the source object lacks the value during dump. A default may be a value or a callable.

`data_key` is the external key used in serialized output and input data. `attribute` is the Python-side attribute/key used to access or place values. These are independent: `data_key` affects the wire/data representation, while `attribute` affects object access and loaded output paths.

`required=True` makes missing input invalid unless `partial` suppresses that required check. `allow_none=True` allows `None` as a valid value; otherwise `None` is invalid unless a field explicitly treats it differently.

`validate` accepts one callable validator or a collection of validators. Validators run during deserialization, not serialization. A validator must raise `ValidationError` to signal invalid data.

`error_messages` customizes error messages by error key. `metadata` stores arbitrary public metadata on the field; metadata does not itself change serialization semantics.

### Field Types

`fields.Raw` applies no conversion. `fields.String` and alias `fields.Str` handle strings. `fields.Integer` and alias `fields.Int` handle integers; `strict=True` accepts only integer types rather than any value castable to `int`. `fields.Float`, `fields.Decimal`, `fields.Number`, `fields.Boolean` and alias `fields.Bool` handle numeric and boolean data. `fields.Decimal` returns `Decimal` objects by default and can serialize as a string when `as_string=True`.

`fields.DateTime`, `fields.NaiveDateTime`, `fields.AwareDateTime`, `fields.Date`, `fields.Time`, and `fields.TimeDelta` format and parse temporal values. `DateTime` supports named formats such as `"iso"`, `"rfc"`, `"timestamp"`, and `"timestamp_ms"`, or a date format string. Naive and aware variants enforce timezone expectations during deserialization according to their documented constructor options.

`fields.UUID`, `fields.Url`/`fields.URL`, `fields.Email`, `fields.IP`, `fields.IPv4`, `fields.IPv6`, `fields.IPInterface`, `fields.IPv4Interface`, and `fields.IPv6Interface` format and validate those external data forms.

`fields.Enum(enum, *, by_value=False, **kwargs)` serializes and deserializes enum members by name by default. With `by_value=True`, it uses raw enum values. With a field class or instance passed as `by_value`, that field is used for the value representation.

`fields.Method(serialize, *, deserialize=None, **kwargs)` gets dump values from a method on the schema. `serialize` is the schema method name and that method receives the object being serialized. If `deserialize` is provided, the named schema method converts loaded input values.

`fields.Function(serialize=None, *, deserialize=None, **kwargs)` gets dump values from a callable. The serialize callable receives the object being serialized. The deserialize callable receives the input value. If no serialize callable is provided, the field is load-only; if no deserialize callable is provided, load passes the value through.

`fields.Constant(constant, **kwargs)` serializes and deserializes to a fixed constant value. Use `dump_only` or `load_only` to restrict it to one direction.

### Collection and Nested Fields

`fields.List(inner, **kwargs)` applies an inner field to each list element and does not turn scalar inputs into single-item lists.

`fields.Tuple(tuple_fields, **kwargs)` applies a fixed sequence of fields to a tuple-like value with the same arity.

`fields.Mapping(keys=None, values=None, **kwargs)` and `fields.Dict` validate mapping keys and values when key/value fields are supplied. If omitted, mapping contents are not recursively validated by those arguments.

`fields.Nested(nested, *, only=None, exclude=(), many=False, unknown=None, **kwargs)` embeds another schema. `nested` may be a schema class, schema instance, class name string, `"self"`, or callable returning a schema. The string `"self"` means the schema currently being declared, which supports self-referential relationships. A callable defers schema resolution so two schemas may refer to each other. `only` and `exclude` limit nested fields. A parent schema can address nested fields with dotted `only`, `exclude`, and `partial` paths. A nested field used inside `fields.List` represents a collection of nested objects.

`fields.Pluck(nested, field_name, *, many=False, **kwargs)` is a nested field that represents only one field of the nested schema. On dump it produces the plucked value instead of the full nested object. On load it wraps the incoming value under `field_name` and loads that nested shape, so a plucked scalar can become nested data such as `{field_name: value}`. With `many=True`, a flat list of plucked values corresponds to a list of nested objects carrying that field.

### Custom Fields

A custom field subclasses `fields.Field` and implements `_serialize(value, attr, obj, **kwargs)` and/or `_deserialize(value, attr, data, **kwargs)`. `_serialize` returns the external representation for dump. `_deserialize` returns the Python representation for load. A custom field raises `ValidationError` for invalid input.

### Validators

A validator is a callable that receives a value and raises `ValidationError` on failure. Field validators run during deserialization.

`validate.Range(min=None, max=None, min_inclusive=True, max_inclusive=True, error=None)` checks numeric bounds. Missing lower or upper bound means that side is unbounded.

`validate.Length(min=None, max=None, equal=None, error=None)` checks `len(value)`. If `equal` is supplied, exact length is checked instead of min/max.

`validate.OneOf(choices, labels=None, error=None)` accepts values in `choices`. Its `options(valuegetter=str)` helper yields value/label pairs for UI-like choices. `validate.NoneOf(iterable, error=None)` rejects values in an iterable. `validate.ContainsOnly(choices, labels=None, error=None)` accepts sequences whose every member is in `choices`, and empty input is valid. `validate.ContainsNoneOf(iterable, error=None)` rejects sequences containing any forbidden member.

`validate.Equal(comparable, error=None)` checks equality. `validate.Regexp(regex, flags=0, error=None)` uses regular-expression matching from the beginning of a string. `validate.Predicate(method, error=None, **kwargs)` calls a named method on the value and succeeds when the result is truthy. `validate.URL(...)` and `validate.Email(...)` validate URL and email strings. `validate.And(*validators)` runs multiple validators and combines their errors.

### Decorators and Hooks

`@pre_load(fn=None, *, pass_collection=False)` registers a method that receives data before deserialization and returns replacement data. `@post_load(fn=None, *, pass_collection=False, pass_original=False)` registers a method that receives deserialized data and returns replacement data. `post_load` is the normal way to construct application objects from loaded dictionaries.

`@pre_dump(fn=None, *, pass_collection=False)` registers a method that receives an object before serialization and returns a replacement object. `@post_dump(fn=None, *, pass_collection=False, pass_original=False)` registers a method that receives serialized data and returns replacement data.

By default, hook methods process one item at a time when `many=True`; `pass_collection=True` passes the whole collection. Hook methods receive lifecycle keyword arguments such as `many`; load hooks receive `partial`, and schema validators receive `partial`, `many`, and `unknown` as applicable. When `pass_original=True`, post hooks and schema validators also receive the original input for comparison.

`@validates(*field_names)` registers a schema method as a field validator for one or more fields. The method receives the field value and a `data_key` keyword argument.

`@validates_schema(fn=None, *, pass_collection=False, pass_original=False, skip_on_field_errors=True)` registers a schema-level validator. With the default `skip_on_field_errors=True`, the method is not called for data that already produced field-level errors; set it to false when the schema-level check should still run. It raises `ValidationError` to add schema-level errors, either under `_schema` or under explicit field keys when a mapping of messages is raised.

### Exceptions and Errors

`ValidationError(message, field_name="_schema", data=None, valid_data=None, **kwargs)` is the primary validation exception. `message` may be a string, list, or mapping. The exception exposes `messages`, `field_name`, `data`, and `valid_data`. `normalized_messages()` returns messages in the public normalized shape used by schema loading and validation.

For a single object, field errors are keyed by field/data key and schema-level errors use `_schema`. A field normally maps to a list of messages; a custom error message may itself be a mapping when the user supplied structured message data. For collection loads with indexed errors enabled, the outer keys are invalid item indexes. Nested schemas produce nested error dictionaries. `normalized_messages()` returns this public normalized shape whether the original error message was a string, list, or mapping. `ValidationError.valid_data` contains values that were successfully deserialized before the error was raised.

`MarshmallowError` is the base marshmallow exception. `RegistryError` is raised when a schema class cannot be resolved from the registry. `StringNotCollectionError` is raised when a string is supplied where a collection of field names is required.

### Class Registry

`marshmallow.class_registry.register(classname, cls)` registers a schema class by name. `marshmallow.class_registry.get_class(classname, all=False)` retrieves a registered class; with `all=True`, it returns all matching classes. This registry supports `fields.Nested` declarations that refer to schemas by class name string.

### OrderedSet

`marshmallow.orderedset.OrderedSet` is importable as an insertion-ordered mutable set. It is useful anywhere a schema or extension wants set semantics while preserving field declaration order, including `Schema.set_class`.

`OrderedSet(iterable=None)` creates an empty ordered set or one populated from the iterable in first-seen order. Repeated values appear once. It supports `len`, membership tests with `in`, forward iteration in insertion order, reversed iteration in reverse insertion order, `add(value)`, `discard(value)`, and `pop(last=True)`. `pop()` removes and returns the newest item by default; with `last=False`, it removes and returns the oldest item. Popping an empty ordered set raises `KeyError`.

Equality with another `OrderedSet` is order-sensitive. Equality with a normal set-like object uses ordinary set membership equality. Standard mutable-set operations such as union, intersection, and difference should behave consistently with Python's set protocol while preserving the ordered-set iteration contract for `OrderedSet` results.

### Experimental Context

`Context[T](context)` is a typed context manager. Within the context block, `Context[T].get(default=...)` returns the active context value. The context can be read from custom fields, hook methods, and validators. Accessing context outside an active block returns the provided default when one is supplied.

### Utility Helpers

`marshmallow.utils` contains public helpers used by advanced users and extensions, including collection predicates, aware datetime detection, timestamp conversion helpers, `ensure_text_type`, `get_value`, `set_value`, `pluck`, `callable_or_raise`, and `timedelta_to_microseconds`. These helpers should behave as their names and API documentation describe, but the core schema behavior should not depend on private utility implementation details.

## Behavioral Sections

### Serialization With Dump and Dumps

`dump` returns native Python data composed from active dump fields. A single object produces a mapping. With `many=True`, an iterable collection produces a list of mappings. `load_only` fields are omitted. Missing values are omitted unless a `dump_default` supplies a value. `data_key` controls the external key in the output, while `attribute` controls where the value is read from the source object.

`only` and `exclude` affect which fields appear. Dotted paths affect nested schemas. Nested fields serialize nested objects using the nested schema, and plucked fields serialize a selected nested value. Computed `Method` and `Function` fields produce values from schema methods or callables.

`dumps` returns a JSON string by encoding the result of `dump` through the schema render module.

### Deserialization With Load and Loads

`load` accepts a mapping or, with `many=True`, a collection of mappings. It applies active load fields, converts values, applies defaults, runs validators, applies hooks, handles unknown fields, and returns Python data. `dump_only` fields are ignored during loading. `load_only` fields may appear in loaded output.

If input is invalid, `load` raises `ValidationError` after collecting available errors. Unknown fields follow the active unknown policy. `loads` decodes a string through the schema render module and then applies `load`.

### Validate

`validate` applies load-time validation and returns the normalized error dictionary instead of returning loaded data or raising for ordinary validation errors. An empty dictionary means the input is valid under the active schema options.

### Required, Missing, Defaults, and Nulls

A missing non-required field without `load_default` is omitted from loaded output. A missing field with `load_default` contributes that default. A missing required field is an error unless suppressed by `partial`. `None` is accepted only when `allow_none=True` or when a field's own public behavior allows it.

### Unknown Fields

`RAISE` reports unknown input keys as errors. `EXCLUDE` drops them. `INCLUDE` keeps them in loaded output. Unknown handling applies during loading, including nested schema loading when a nested unknown policy is active.

### Hooks and Object Construction

Pre-load hooks can normalize input data before fields see it. Post-load hooks can transform loaded dictionaries into application objects. Pre-dump hooks can normalize source objects before field extraction. Post-dump hooks can transform serialized dictionaries before they are returned or JSON-encoded. Hook return values replace the data for the next phase.

### Error Handling

Errors from field conversion, validators, schema validators, nested schemas, unknown fields, required fields, and custom fields are collected into the public error shape. `handle_error` is called before a load error is raised, giving schema subclasses a public extension point.

## Error Semantics

- Invalid deserialization and validation raise or return `ValidationError` information; serialization does not run normal validators.
- A field validator or custom field signals invalid input by raising `ValidationError`.
- A `ValidationError` raised from a field is associated with that field. A schema-level `ValidationError` is associated with `_schema` unless it supplies field-specific messages.
- Collection errors may be indexed by item position when `index_errors` is enabled.
- Nested schema errors retain nested structure.
- `RegistryError` indicates that a string-named schema cannot be resolved.
- `StringNotCollectionError` indicates that a string was supplied where marshmallow requires a collection of field names.

## Cross-View Invariants

1. A schema's declared field set is the common source for `dump`, `load`, and `validate`: fields removed by `only` or `exclude` disappear from every active view unless a direction flag excludes them only from one direction.
2. The external key selected by `data_key` is shared by dump output and load input, while the Python-side `attribute` affects object access and loaded placement; the two choices remain independent.
3. A `load_only` field can affect `load` and `validate` but is absent from `dump` and `dumps`; a `dump_only` field can affect `dump` and `dumps` but is ignored by `load`, `loads`, and `validate`.
4. Collection mode is a cross-method outer-shape rule: `dump` and `load` return lists, `dumps` and `loads` encode/decode those list shapes, and validation errors can be grouped by item index.
5. A `partial` load changes the missing-required view of the data without changing conversion and validation for present values, and dotted partial paths carry that rule into nested schemas.
6. Unknown-field policy changes only the fate of undeclared input keys; declared fields keep their normal conversion, validation, default, and direction behavior under all three policies.
7. Nested schemas preserve projection rules across views: dotted `only` and `exclude` affect both nested dump shape and nested load/validation expectations for the same named path.
8. `validate` and a failed `load` report compatible normalized error shapes for the same invalid input, while successful `load` returns converted data instead of an error mapping.
9. `dumps` and `loads` are JSON-facing views of `dump` and `load`; they use the same schema contract and differ only by the render module's encoding or decoding step.
10. Hook return values are observable across phases: a pre-load change affects field loading, a post-load change affects the returned object, a pre-dump change affects field dumping, and a post-dump change affects the final serialized mapping or JSON string.

## Representative Workflows

### Serializing and Loading a User

```python
from dataclasses import dataclass
import datetime as dt
from marshmallow import Schema, fields, post_load, validate

@dataclass
class User:
    name: str
    email: str
    age: int
    created_at: dt.datetime | None = None

class UserSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    age = fields.Integer(validate=validate.Range(min=0))
    created_at = fields.DateTime(dump_only=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

schema = UserSchema()
serialized = schema.dump(User("Ada", "ada@example.com", 37, dt.datetime(2024, 1, 1)))
loaded = schema.load({"name": "Ada", "email": "ada@example.com", "age": 37})
errors = schema.validate({"name": "Ada", "email": "not-an-email", "age": -1})
```

The dump result is a mapping with declared dump fields. The load result is a `User` because `post_load` returns one. The validation result is an error mapping for the invalid fields.

### Nested Relationships and Projections

```python
class AuthorSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)

class BookSchema(Schema):
    title = fields.String(required=True)
    author = fields.Nested(AuthorSchema, only=("id", "name"))
    coauthors = fields.List(fields.Nested(AuthorSchema, exclude=("id",)))
```

The nested schema controls the shape of `author`; the list field applies the nested schema to each coauthor. `only` and `exclude` restrict nested projections without changing the top-level schema.

### Custom Field Extension

```python
from marshmallow import ValidationError, fields

class PinCode(fields.Field[list[int]]):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        return "".join(str(digit) for digit in value)

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return [int(char) for char in value]
        except ValueError as error:
            raise ValidationError("Pin codes must contain only digits.") from error
```

A custom field controls its own external and Python representations while still participating in schema defaults, direction flags, validators, and error collection.

## Non-Goals

- Private or underscore-prefixed methods, attributes, caches, maps, and metaclass storage are not part of this specification.
- Exact error message wording is not specified. The public error shape and exception types are specified.
- Historical APIs removed or deprecated before the current public surface are not required.
- Third-party extensions and integrations are not included.
- Performance characteristics and implementation strategies are not specified.
- The specification does not require a particular internal module layout beyond public import compatibility.

## Evaluation Notes

A complete implementation should preserve the behavior described in this document across simple schemas, nested schemas, computed fields, validators, lifecycle hooks, error reporting, JSON wrappers, and extension points. The checks for this API are behavioral: they use public imports and public method calls, and they do not require private attributes, private storage layouts, exact internal algorithms, or exact wording of error messages.
