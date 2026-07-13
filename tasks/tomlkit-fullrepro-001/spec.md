<!-- INTERNAL
task_id: tomlkit-fullrepro-001
spec_version: v1
delta: standardized current-main task packet
source_boundary: public documentation, public API surface, and existing task artifacts
-->

# TOML Kit Specification

## Product Overview

TOML Kit is a style-preserving TOML library for Python. It parses TOML text into editable document objects, preserves comments, whitespace, indentation, line endings, quote style, table ordering, and other formatting details, and serializes documents back to TOML after reads or edits. It can also build TOML documents from Python data and helper-created TOML items.

The core contract is the relationship between TOML text, a mutable TOML document, item objects, and the string or file output produced from that document.

## Scope

This specification covers normal public TOML Kit usage:

- top-level imports from `tomlkit`;
- parsing and loading TOML from strings, bytes, and file-like objects;
- dumping mappings, documents, tables, and item containers to strings and writable streams;
- creating new TOML documents and items with public helper functions;
- dictionary-like document and table editing;
- list-like array and array-of-table editing;
- inline table, table, key, comment, whitespace, date, time, datetime, number, boolean, and string item behavior;
- `TOMLFile` read/write behavior;
- custom encoder registration;
- public exception classes and parse-error line/column attributes.

This specification does not require matching private implementation storage, parser helper functions, private utility functions, exact `repr()` output, exact exception message wording, or tests that directly import private modules.

## Installable Surface

The package name is `tomlkit`. Public imports include:

```python
import tomlkit
from tomlkit import parse, loads, load, dumps, dump
from tomlkit import document, table, inline_table, aot, array
from tomlkit import item, key, key_value, value
from tomlkit import string, integer, float_, boolean, date, time, datetime
from tomlkit import comment, ws, nl
from tomlkit import register_encoder, unregister_encoder, TOMLDocument
from tomlkit.toml_file import TOMLFile
```

Documented public modules include `tomlkit`, `tomlkit.toml_document`, `tomlkit.toml_file`, `tomlkit.items`, and `tomlkit.exceptions`.

## Quick Start

Parse TOML text, read values with mapping syntax, edit the document, and serialize it:

```python
from tomlkit import dumps, parse

content = """[table]
foo = "bar"  # String
"""
doc = parse(content)

assert doc["table"]["foo"] == "bar"
assert dumps(doc) == content

doc["table"]["baz"] = 13
assert "baz = 13" in dumps(doc)
```

Build a new document from scratch:

```python
from tomlkit import comment, document, nl, table

doc = document()
doc.add(comment("This is a TOML document."))
doc.add(nl())
doc.add("title", "TOML Example")

owner = table()
owner.add("name", "Tom")
doc.add("owner", owner)
```

## Parsing And Loading

`parse(string: str | bytes) -> TOMLDocument` parses TOML text or bytes into a `TOMLDocument`. `loads(string)` is an alias for `parse`. `load(fp)` reads text or bytes from a file-like object and parses the result.

Parsed documents behave like mutable mappings. Top-level keys, tables, inline tables, arrays, and arrays of tables are accessible with dictionary-style indexing. Scalar TOML values compare and behave like the corresponding Python values while retaining TOML rendering behavior.

Parsing preserves the original layout of a document. If a parsed document is serialized without modification, `dumps(doc)` returns the original TOML text for ordinary supported documents, including comments, blank lines, indentation, inline comments, quote styles, and table ordering.

TOML Kit supports TOML 1.x syntax needed by normal TOML documents: strings, integers, floats, booleans, dates, times, datetimes, arrays, inline tables, standard tables, arrays of tables, dotted keys, quoted keys, comments, and whitespace. Invalid TOML raises a subclass of `ParseError`.

## Dumping And Serialization

`dumps(data, sort_keys=False) -> str` serializes a TOML document, table, inline table, container-like object, or mapping to TOML text.

- A parsed `TOMLDocument` or table-like item serializes with its preserved layout.
- A plain mapping is converted into a TOML document representation.
- Nested dictionaries become tables or inline containers according to the item-building rules.
- Lists become arrays, and lists of dictionaries may become arrays of tables where appropriate.
- `sort_keys=True` serializes mapping keys in sorted order for newly encoded mappings and table containers.
- A mapping-like object with an `as_string()` method may be serialized through that method.
- Passing an unsupported non-mapping object raises `TypeError`.

`dump(data, fp, *, sort_keys=False) -> None` writes `dumps(data, sort_keys=sort_keys)` to a writable text stream.

Every public item implements `as_string() -> str`, returning its TOML representation. Every public item implements `unwrap()`, returning the corresponding plain Python value: dictionaries for tables/documents, lists for arrays and arrays of tables, strings for string items, numbers for number items, booleans for boolean items, dates/times/datetimes for temporal items, and `None` for comments or whitespace-like null items.

## TOMLDocument

`document() -> TOMLDocument` creates an empty document. `parse`, `loads`, and `load` return `TOMLDocument` instances.

A `TOMLDocument` behaves like an ordered mutable mapping with TOML-aware rendering:

- `doc[key]` reads an item or unwrapped value by key.
- `doc[key] = value` inserts or replaces a value, converting ordinary Python values into TOML items.
- `del doc[key]`, `pop`, and `remove` delete keys.
- `add(key, value)` / `append(key, value)` append keys and items while preserving TOML formatting.
- Passing a comment or newline item to `add` appends it as layout rather than as a key/value pair.
- `update`, `keys`, `values`, `items`, membership tests, and iteration follow standard mapping expectations.
- `unwrap()` returns a plain nested Python dictionary/list/value representation.
- `as_string()` renders the document as TOML text.
- Copying or deep-copying a document produces an independently editable document with the same observable content.

When a document was parsed from text, editing should preserve surrounding comments, indentation, line endings, and sibling order as much as possible. Adding a key to an existing table renders that key in the table. Adding a new table renders a table header in a natural location. Removing a table or key removes its rendered TOML entry without corrupting the remaining document.

For out-of-order table fragments and sub-tables of arrays of tables, the data model is preserved. Serialization may normalize the physical placement of a sub-table into the owning array element; the data must remain accessible through the same public mapping path.

## Tables And Inline Tables

`table(is_super_table: bool | None = None) -> Table` creates an empty standard table. A table behaves like a mutable mapping and renders as TOML table content when attached to a document. A table can be updated with dictionaries, assigned with `table["key"] = value`, and extended with `append` or `add`.

`inline_table() -> InlineTable` creates an inline table. Inline tables behave like mutable mappings and render inside braces, such as `{x = 1, y = 2}`. Editing an inline table preserves valid comma separation and does not leave trailing or doubled separators after insertion or deletion.

Tables and inline tables expose:

- `as_string()` for TOML rendering;
- `unwrap()` for plain dictionaries;
- `is_table()` / `is_inline_table()` indicators;
- `comment(text)` to attach a trailing comment;
- `indent(n)` where indentation is relevant to rendering.

`table(True)` creates a super table used for nested table construction. Super tables group child tables without always rendering their own header when the rendered TOML only needs the child table header.

## Arrays And Arrays Of Tables

`array(raw="[]") -> Array` parses a TOML array literal and returns an editable array item. The default creates an empty array. The input must be an array literal; otherwise `ValueError` is raised.

Arrays behave like mutable Python lists:

- `append`, `extend`, `insert`, `remove`, indexing, iteration, membership, and length follow list expectations;
- ordinary Python values are converted to TOML items when inserted;
- `as_string()` renders a TOML array;
- `unwrap()` returns a plain list;
- `multiline(True)` renders the array as multiline;
- `add_line(*items, indent="    ", comment=None, add_comma=True, newline=True)` appends a formatted line to a multiline array.

`aot() -> AoT` creates an array of tables. It behaves like a list of table-like mappings and renders as repeated `[[name]]` sections when attached to a document. Appending dictionaries converts them into table elements. `unwrap()` returns a list of dictionaries.

## Scalar Item Helpers

TOML Kit scalar helpers create item objects that behave like Python scalar values and retain TOML rendering:

```python
integer(raw: str | int) -> Integer
float_(raw: str | float) -> Float
boolean(raw: str | bool) -> Bool
string(raw: str, *, literal=False, multiline=False, escape=True) -> String
date(raw: str) -> Date
time(raw: str) -> Time
datetime(raw: str) -> DateTime
```

`integer` and `float_` accept strings or native numbers and render TOML numeric values. Integer items behave like `int`; float items behave like `float`, including normal arithmetic and comparison behavior inherited from Python numeric types.

`boolean` accepts `True`, `False`, `"true"`, or `"false"` and renders TOML booleans. Boolean items compare like booleans.

`string` creates TOML string items. By default it creates a single-line basic string. `literal=True` chooses literal quoting, `multiline=True` chooses multiline quoting, and both flags together choose multiline literal quoting. For basic strings, escaping is applied by default. With `escape=False`, the caller is responsible for providing content that is valid for the selected string type. Invalid strings raise `InvalidStringError`.

`date`, `time`, and `datetime` parse RFC 3339-style TOML date/time/datetime strings and return items that behave like `datetime.date`, `datetime.time`, and `datetime.datetime`. Passing a string of the wrong temporal kind raises `ValueError`.

Every scalar item supports `as_string()`, `unwrap()`, `comment(text)`, and `indent(n)`. Date/time/datetime items preserve their original TOML spelling where relevant for rendering while unwrapping to Python temporal values.

## Keys, Values, Comments, And Whitespace

`key(k)` creates a TOML key object. A string creates a single key. An iterable of strings creates a dotted key; an iterable with one element creates a single key. Keys render with `as_string()` and preserve quoting/escaping needed for TOML validity.

`value(raw)` parses a single TOML value literal and returns an item. The entire input must be consumed; extra trailing characters raise a parse error. `key_value(src)` parses a TOML key/value pair and returns `(Key, Item)`.

`comment(text)` creates a comment item. A single-line input renders as a `#` comment. A multiline input renders each line as a TOML comment line, with empty lines rendered as bare `#`.

`ws(src)` creates fixed whitespace. `nl()` creates a newline item. Whitespace and newline items are layout items; when added to a document they affect rendering rather than adding data keys.

## Item Conversion

`item(value, _sort_keys=False)` converts Python values into TOML items:

- dictionaries and mappings become tables;
- lists and tuples become arrays, except arrays of dictionaries may become arrays of tables where appropriate;
- strings, integers, floats, booleans, dates, times, datetimes, comments, whitespace, arrays, tables, inline tables, and existing TOML items are converted or returned as TOML items;
- unsupported values raise `ConvertError` unless a registered custom encoder handles them.

When `_sort_keys=True`, mapping keys are rendered in sorted order during conversion.

## Custom Encoders

`register_encoder(encoder)` registers a custom encoder function and returns the same function, allowing decorator use. Encoders are consulted when `item()` cannot convert an object through built-in rules. An encoder receives the object and may accept TOML Kit's parent/sort keyword arguments; it should return a TOML item or raise `ConvertError` to let other encoders try.

`unregister_encoder(encoder)` removes a registered encoder if present. Removing an encoder that is not currently registered has no effect.

Custom encoders apply to nested values as well as top-level values when conversion reaches an unsupported object.

## TOMLFile

`TOMLFile(path)` represents a TOML file at a filesystem path.

`read() -> TOMLDocument` opens the file as UTF-8, reads it without newline translation, records the file's line-ending style, normalizes CRLF to LF in memory when the file is consistently CRLF, and returns a parsed `TOMLDocument`.

`write(data: TOMLDocument) -> None` serializes the document and writes UTF-8 TOML text to the same path. If a previous `read()` observed consistent LF or CRLF line endings, `write()` preserves that line-ending style. Mixed line endings are not normalized. If no file was read first, the default platform line separator is used.

## Exceptions

Public exception classes are available from `tomlkit.exceptions`; conversion exceptions are also visible through item conversion APIs. Important classes include:

- `TOMLKitError`
- `ParseError`
- `MixedArrayTypesError`
- `InvalidNumberError`
- `InvalidDateTimeError`
- `InvalidDateError`
- `InvalidTimeError`
- `InvalidNumberOrDateError`
- `InvalidUnicodeValueError`
- `UnexpectedCharError`
- `EmptyKeyError`
- `EmptyTableNameError`
- `InvalidCharInStringError`
- `UnexpectedEofError`
- `NonExistentKey`
- `KeyAlreadyPresent`
- `InvalidControlChar`
- `InvalidStringError`
- `ConvertError`

`ParseError` is a `ValueError` and exposes integer `line` and `col` properties. Parser-specific subclasses identify common syntax categories such as invalid numbers, invalid dates, invalid strings, empty keys, unexpected characters, unexpected end of file, and mixed array types. Tests and applications should rely on exception class and parse position, not exact message wording.

`NonExistentKey` is raised for missing TOML keys in APIs that distinguish missing keys from normal mapping defaults. `KeyAlreadyPresent` is raised when an operation would duplicate a key in a context where duplicate TOML keys are invalid.

## Error Semantics

Invalid TOML input and unsupported conversions should fail with the public exception classes exposed by `tomlkit.exceptions`. Parse errors report source position through public line and column attributes where available. Conversion errors from custom encoders and item conversion are reported through public exception categories. Exact exception message wording is not part of the public contract.

## Cross-View Invariants

1. Parsing a valid TOML document and immediately dumping it preserves the document's observable text layout for ordinary supported documents.
2. A value read through mapping syntax and the same value observed after `unwrap()` represent the same TOML fact.
3. Editing a parsed document changes the relevant data while preserving unrelated comments, whitespace, and table ordering.
4. A document built with helper item constructors and a document parsed from equivalent TOML serialize to compatible TOML and unwrap to equivalent Python data.
5. `dump(data, fp)` writes the same TOML text that `dumps(data)` would return with the same `sort_keys` option.
6. `TOMLFile.read()` followed by `TOMLFile.write()` preserves the file's line-ending convention when it is consistently LF or consistently CRLF.
7. Arrays, tables, inline tables, and arrays of tables expose Python container behavior and TOML rendering for the same underlying values.
8. Scalar TOML items behave like their Python scalar counterparts for equality, comparison, and basic operations while retaining TOML-specific `as_string()` behavior.
9. `item(x).unwrap()` returns data equivalent to `x` for supported plain Python values, modulo TOML-specific conversions such as tuples becoming arrays.
10. Parse errors report the public exception category and source position consistently across `parse`, `loads`, `load`, `value`, and `key_value`.

## Representative Workflows

### Parse, edit, and preserve style

```python
from tomlkit import dumps, parse

doc = parse("""# Project
[tool.demo]
name = "demo"  # package name
""")

doc["tool"]["demo"]["version"] = "1.0"
text = dumps(doc)

assert "# Project" in text
assert 'name = "demo"  # package name' in text
assert 'version = "1.0"' in text
```

### Build a document with tables and arrays

```python
from tomlkit import aot, document, table

doc = document()
doc["title"] = "Example"

owner = table()
owner["name"] = "Tom"
doc["owner"] = owner

products = aot()
products.append({"name": "Hammer", "sku": 738594937})
doc["products"] = products
```

### Use a custom encoder

```python
from tomlkit import item, register_encoder, table, unregister_encoder
from tomlkit.exceptions import ConvertError

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

@register_encoder
def encode_point(obj, _parent=None, _sort_keys=False):
    if isinstance(obj, Point):
        t = table()
        t["x"] = obj.x
        t["y"] = obj.y
        return t
    raise ConvertError("not a point")

encoded = item({"point": Point(1, 2)})
unregister_encoder(encode_point)
```

## Non-Goals

TOML Kit does not promise that a reimplementation will expose the same private parser classes, private utility functions, internal container structures, proxy class names, object `repr()` strings, or exact exception message text. It also does not require preserving the physical source location of every out-of-order sub-table when serialization normalizes placement while preserving data.

TOML standard conformance is relevant where it affects public TOML Kit behavior, but a task that only checks a large external TOML compliance corpus without exercising style preservation, editable documents, item helpers, or public exception categories is outside this reconstruction scope.

## Evaluation Notes

Evaluation checks public behavior through imports, parsing, serialization, document editing, item helpers, file read/write, custom encoders, and public exception classes. Tests may compare serialized TOML text when the formatting is part of TOML Kit's documented style-preservation behavior. Tests should not require private imports, private attributes, internal parser helper names, exact `repr()` output, exact exception messages, or prior source layout.

Scoring distinguishes atomic API behavior from integration behavior and full workflows. A correct implementation should maintain consistency between parsed documents, mapping access, item unwrapping, serialization, and file output.
