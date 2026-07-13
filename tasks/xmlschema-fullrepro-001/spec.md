<!-- INTERNAL
task_id: xmlschema-fullrepro-001
spec_version: v1
delta: initial public-packet draft for remaining e2e project batch
source_boundary: README, public package exports, public module/class/function names, selected upstream behavioral tests
-->

# xmlschema Specification

## Product Overview

This document describes the public behavior of `xmlschema`. The package should provide the documented user-facing Python surface and reproduce observable behavior for the feature areas listed below.

Project overview:

```text
*********
xmlschema
*********

   :target: https://pypi.python.org/pypi/xmlschema/
   :target: https://pypi.python.org/pypi/xmlschema/
   :target: https://pypi.python.org/pypi/xmlschema/
   :alt: MIT License
   :target: https://lbesson.mit-license.org/
   :target: https://pypi.python.org/pypi/xmlschema/

.. xmlschema-introduction-start

The *xmlschema* library is an implementation of `XML Schema <http://www.w3.org/2001/XMLSchema>`_
for Python.

This library arises from the needs of a solid Python layer for processing XML
Schema based files for
`MaX (Materials design at the Exascale) <http://www.max-centre.eu>`_  European project.
A significant problem is the encoding and the decoding of the XML data files
produced by different simulation software.
Another important requirement is the XML data validation, in order to put the
produced data under control. The lack of a suitable alternative for Python in
the schema-based decoding of XML data has led to build this library. Obviously
this library can be useful for other cases related to XML Schema based processing,
not only for the original scope.

The full `xmlschema documentation is available on "Read the Docs" <http://xmlschema.readthedocs.io/en/latest/>`_.


Features
========

This library includes the following features:

* Full XSD 1.0 and XSD 1.1 support
* Building of XML schema objects from XSD files
* Validation of XML instances against XSD schemas
* Decoding of XML data into Python data and to JSON
* Encoding of Python data and JSON to XML
* Data decoding and encoding ruled by converter classes
* An XPath based API for finding schema's elements and attributes
* Support of XSD validation modes *strict*/*lax*/*skip*
* XML attacks protection using an XMLParser that forbids entities
* Access control on resources addressed by an URL or filesystem path
* Downloading XSD files from a remote URL and storing them for offline use
* XML data bindings based on DataElement class
* Static code generation with Jinja2 templates


Installation
============

You can install the library with *pip* in a Python environment::

    pip install xmlschema

The library uses the Python's ElementTree XML library and requires
`elementpath <https://github.com/brunato/elementpath>`_ additional package.
The base schemas of the XSD standards are included in the package for working
offline and to speed-up the building of schema instances
```

## Scope

The covered scope is the public Python API and command/user workflows for these behavior areas: get converter, get loglevel, json2xml command 01, json2xml command 02, json2xml command 03, json2xml command 04, validate command 01, validate command 02, validate command 03, validate command 04, validate command 05, validate command 06, fetch namespaces function, fetch resource function, fetch schema function, fetch schema locations function, fid with name attr, get nsmap, get xmlns, iterfind parser, iterparse argument, iterparse argument for html, iterparse argument with lxml, iterparse argument with parser instance, arguments with wrong types, cdata mapping, columnar converter, data element converter.

Out of scope: private modules, private attributes, repository maintenance scripts, network access, exact internal cache structures, and implementation-specific repr/message wording unless explicitly documented as public behavior.

## Installable Surface

The package provides an importable `xmlschema` package from the solution root. The package should be importable without depending on another installed distribution of the same library.

Public export names and public module members observed from the package surface include:

- `xmlschema.translation`
- `xmlschema.limits`
- `xmlschema.XMLSchemaException`
- `xmlschema.XMLResourceError`
- `xmlschema.XMLSchemaNamespaceError`
- `xmlschema.fetch_resource`
- `xmlschema.fetch_namespaces`
- `xmlschema.fetch_schema_locations`
- `xmlschema.fetch_schema`
- `xmlschema.XMLResource`
- `xmlschema.ElementPathMixin`
- `xmlschema.ElementSelector`
- `xmlschema.ElementPathSelector`
- `xmlschema.ElementData`
- `xmlschema.XMLSchemaConverter`
- `xmlschema.UnorderedConverter`
- `xmlschema.ParkerConverter`
- `xmlschema.BadgerFishConverter`
- `xmlschema.AbderaConverter`
- `xmlschema.JsonMLConverter`
- `xmlschema.ColumnarConverter`
- `xmlschema.GDataConverter`
- `xmlschema.DataElement`
- `xmlschema.DataElementConverter`
- `xmlschema.DataBindingConverter`
- `xmlschema.validate`
- `xmlschema.is_valid`
- `xmlschema.iter_errors`
- `xmlschema.iter_decode`
- `xmlschema.to_dict`
- `xmlschema.to_json`
- `xmlschema.to_etree`
- `xmlschema.from_json`
- `xmlschema.XmlDocument`
- `xmlschema.download_schemas`
- `xmlschema.SchemaLoader`
- `xmlschema.LocationSchemaLoader`
- `xmlschema.SafeSchemaLoader`
- `xmlschema.etree_tostring`
- `xmlschema.normalize_url`
- `xmlschema.normalize_locations`
- `xmlschema.XMLSchemaValidatorError`
- `xmlschema.XMLSchemaParseError`
- `xmlschema.XMLSchemaNotBuiltError`
- `xmlschema.XMLSchemaModelError`
- `xmlschema.XMLSchemaModelDepthError`
- `xmlschema.XMLSchemaValidationError`
- `xmlschema.XMLSchemaDecodeError`
- `xmlschema.XMLSchemaEncodeError`
- `xmlschema.XMLSchemaChildrenValidationError`
- `xmlschema.XMLSchemaStopValidation`
- `xmlschema.XMLSchemaIncludeWarning`
- `xmlschema.XMLSchemaImportWarning`
- `xmlschema.XMLSchemaTypeTableWarning`
- `xmlschema.XMLSchemaAssertPathWarning`
- `xmlschema.XsdGlobals`
- `xmlschema.XMLSchemaBase`
- `xmlschema.XMLSchema`
- `xmlschema.XMLSchema10`
- `xmlschema.XMLSchema11`
- `xmlschema.XsdComponent`
- `xmlschema.XsdType`
- `xmlschema.XsdElement`
- `xmlschema.XsdAttribute`
- `xmlschema.arguments.Argument`
- `xmlschema.arguments.Option`
- `xmlschema.arguments.validate_type`
- `xmlschema.arguments.validate_subclass`
- `xmlschema.arguments.validate_choice`
- `xmlschema.arguments.validate_minimum`
- `xmlschema.arguments.validate_instance`
- `xmlschema.arguments.BooleanOption`
- `xmlschema.arguments.StringOption`
- `xmlschema.arguments.NillableStringOption`
- `xmlschema.arguments.PositiveIntOption`
- `xmlschema.arguments.NonNegIntOption`
- `xmlschema.arguments.SourceArgument`
- `xmlschema.arguments.BaseUrlOption`
- `xmlschema.arguments.AllowOption`
- `xmlschema.arguments.DefuseOption`

## Public API Behavior

- Public constructors, functions, classes, exceptions, and constants must be importable from the paths shown above when those paths are part of the documented package surface.
- Functions and methods should accept the documented Python value types, preserve caller-visible return types, and raise the documented exception classes for invalid inputs.
- Mutable public objects should expose stable user-visible state through public methods, properties, iteration, conversion, or rendering APIs rather than through private fields.
- Public options, presets, flags, and mode selectors must affect output consistently across API calls and command-style workflows.

## Parsing, Validation, Rendering, and Conversion Behavior

- Text parsers should accept documented input strings, preserve meaningful whitespace and token boundaries where the public API exposes them, and reject malformed input with the package's public errors.
- Validators should distinguish valid and invalid inputs through public result values, exceptions, iterators, or CLI exit behavior as appropriate for the package.
- Renderers and converters should produce deterministic user-visible output for the same input and configuration. Formatting differences that are part of the public output contract must be reproduced.
- Public plugin, preset, extension, or rule registration APIs should update the same behavior observed by normal parse/render/validate calls.

## Command and Workflow Behavior

- CLI or command-style entry points should parse documented arguments, read files or standard input where supported, write user-visible output to the appropriate stream, and return documented success/failure status.
- File-based workflows should keep path handling, encoding, and error behavior consistent with the Python API view of the same underlying data.
- Import hooks, interactive helpers, or runtime integration points that are public must compose with the core package behavior rather than bypassing it.

## Error Semantics

- Invalid inputs should fail with the package's public exception classes or documented CLI status codes.
- Unknown names, unsupported formats, malformed documents, and invalid configuration should be distinguished when the public API exposes separate error types or outcomes.
- Exact exception message wording is not part of the public contract unless it is itself documented user-facing behavior.

## Cross-View Invariants

- API calls and CLI workflows must agree on whether the same input is accepted or rejected.
- Parser output consumed by renderer/converter APIs should round-trip user-visible content according to documented behavior.
- Configuration passed at construction time and configuration passed at call time should resolve with documented precedence.
- Public serialization, representation, or token views should describe the same logical data observed through direct API access.
- Errors raised during direct API use and errors surfaced through command workflows should describe the same invalid condition.
- Repeated calls with the same input and public configuration should be deterministic unless the API explicitly documents time-, environment-, or randomness-dependent behavior.

## Representative Workflow

A typical implementation should allow a caller to import `xmlschema`, construct or configure the main public object, process an input document/value/string through the documented API, inspect the returned Python object or rendered text, and receive the same observable result when the equivalent command/file workflow is supported.

## Non-Goals

The library contract does not include private helper modules, private test utilities, release automation, packaging metadata, repository-only files, unexposed network integrations, or internal caching and data-structure choices.

## Evaluation Notes

Evaluation runs a filtered subset of upstream pytest nodeids against the candidate package in an isolated oracle worktree. The retained tests are mapped to this specification and are intended to measure public import surface, atomic behavior, cross-component integration, and end-to-end workflows. Candidates receive this specification only; source code, tests, retained nodeids, taxonomy, private scoring artifacts, and prior attempts are not part of the candidate packet.
