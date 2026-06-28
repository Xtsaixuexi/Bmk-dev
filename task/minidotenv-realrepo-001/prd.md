# MiniDotenv Public Product Packet

## Overview

Build `minidotenv.py`, a dependency-free Python module that implements a compact subset of `.env` parsing, interpolation, environment loading, path discovery, and file mutation helpers. It is inspired by `python-dotenv` and should behave like a small deterministic configuration loader suitable for automated testing.

The submitted module must be importable from the solution directory:

```python
from minidotenv import dotenv_values, load_dotenv, find_dotenv, get_key, set_key, unset_key
```

Use only the Python standard library.

## Feature Set

The product has seven feature modules:

1. Public API functions.
2. `.env` line parsing.
3. Quoting and escape handling.
4. Variable interpolation.
5. Environment loading with override control.
6. Path discovery and stream input.
7. File mutation helpers.

These modules are intentionally state-dependent. Parsed bindings feed interpolation; interpolation may use earlier parsed values and the process environment; loading writes selected parsed values into `os.environ`; path discovery selects which file to load; file mutation helpers change later parse and load results; and malformed lines should not corrupt later valid bindings.

## Global Invariants

The following invariants define system correctness:

- `dotenv_values` must not modify `os.environ`.
- `load_dotenv` must only write parsed variables with non-`None` values.
- Existing environment variables are preserved when `override=False` and replaced when `override=True`.
- Variable interpolation must be deterministic and must distinguish file-local values from existing environment values according to the override mode.
- File mutation helpers must preserve unrelated lines and comments where practical.
- Failed or malformed operations must not corrupt the original `.env` file.
- Repeated calls must not leak hidden parser state between files or streams.
- Output dictionaries and file listing behavior must be deterministic in file order unless a helper specifies otherwise.

## Public API

The module must expose these functions:

```python
dotenv_values(dotenv_path=None, stream=None, interpolate=True, override=True)
load_dotenv(dotenv_path=None, stream=None, override=False, interpolate=True)
find_dotenv(filename=".env", usecwd=True)
get_key(dotenv_path, key)
set_key(dotenv_path, key, value, quote_mode="always")
unset_key(dotenv_path, key)
```

Return values should be simple Python values suitable for tests:

- `dotenv_values` returns a `dict` mapping keys to strings or `None`; if the selected file does not exist, it returns `{}`.
- `load_dotenv` returns `True` if it read a file or stream and `False` if no input source exists.
- `find_dotenv` returns the matching path as a string, or an empty string if not found.
- `get_key` returns the string value for a present key, or `None` if absent.
- `set_key` returns `True` on success and `False` on validation or file-read failure.
- `unset_key` returns `True` if a key was removed and `False` if the key was not present or the file does not exist.

## Input Sources

`dotenv_path` is a filesystem path to a `.env` file.

`stream` is a text stream such as `io.StringIO`.

If both `dotenv_path` and `stream` are provided, `dotenv_path` takes precedence.

If neither is provided, `dotenv_values` and `load_dotenv` use `find_dotenv()`.

## Dotenv File Format

The parser reads UTF-8 text line by line.

Supported line forms:

```text
KEY=value
KEY=
KEY
export KEY=value
# comment
```

Rules:

- Empty lines and full-line comments are ignored.
- Leading and trailing whitespace around keys, `=`, and values is ignored unless inside quotes.
- `export` before a binding is accepted and ignored.
- Valid keys match `[A-Za-z_][A-Za-z0-9_]*`.
- `KEY=` maps to an empty string.
- A bare `KEY` line maps to `None`.
- Malformed lines are skipped and must not stop later valid lines from being parsed.

## Values, Quotes, And Comments

Unquoted values end before an inline comment marker introduced by whitespace and `#`.

Single-quoted values preserve literal text except for `\\` and `\'` escapes.

Double-quoted values support common escapes: `\n`, `\t`, `\r`, `\"`, and `\\`.

Surrounding quotes are removed in parsed values.

## Variable Interpolation

When `interpolate=True`, values may reference variables using:

```text
${NAME}
${NAME:-default}
```

Bare `$NAME` expansion is not required.

Interpolation uses values parsed earlier in the same file and values from `os.environ`.

When resolving conflicts between a file value and an existing environment value:

- with `override=True`, the file value takes precedence;
- with `override=False`, the existing environment value takes precedence.

Undefined `${NAME}` expands to an empty string.

Undefined `${NAME:-default}` expands to `default`.

A variable only sees bindings parsed before the current line, not later lines.

## Environment Loading

`load_dotenv` parses the selected source and writes variables into `os.environ`.

Bindings with value `None` are not written.

When `override=False`, existing keys in `os.environ` are not changed.

When `override=True`, parsed values replace existing keys.

The function must not modify unrelated environment variables.

## Path Discovery

`find_dotenv(filename=".env", usecwd=True)` searches from the current working directory upward through parent directories until it finds `filename`.

If no file is found, it returns an empty string.

For this benchmark, `usecwd=False` may behave the same as `usecwd=True`.

## File Mutation Helpers

`get_key(path, key)` returns the parsed value for `key` without modifying the file. It uses the same interpolation behavior as `dotenv_values(path)` for the selected key.

`set_key(path, key, value, quote_mode="always")` adds or replaces a binding in an existing file. If the file does not exist, `set_key` returns `False` and does not create it.

For this benchmark:

- `quote_mode="always"` writes `KEY='value'`.
- `quote_mode="never"` writes `KEY=value`.
- existing comments and unrelated bindings should remain in their original order;
- replacing an existing key should update the first matching binding, including `export KEY=...` bindings, and leave unrelated lines intact;
- adding a new key appends it at the end of the file.

`unset_key(path, key)` removes the first matching binding for `key` and preserves unrelated lines.

If a mutation fails because the key is invalid, the file does not exist, or the file cannot be read, it must return `False` and must not partially rewrite the original file.

## Error Behavior And Recovery

Exact warning text is not public API.

Malformed lines are skipped during parsing.

Invalid keys passed to mutation helpers should fail without modifying the file.

Missing files should not crash `dotenv_values`, `load_dotenv`, `get_key`, or `unset_key`.

## Non-Goals

Do not implement full Bash parsing.

Do not implement command substitution, arithmetic expansion, multiline values, IPython integration, Click-based CLI commands, or `dotenv run` process execution.

Do not implement full POSIX parameter expansion beyond `${NAME}` and `${NAME:-default}`.

Do not preserve file permissions, symlink behavior, or platform-specific path edge cases.

## Evaluation Style

Evaluation will use unit cases for isolated parser, interpolation, loading, discovery, and mutation behavior.

System cases will combine parsing, interpolation, environment state, path discovery, mutation helpers, malformed-line recovery, and repeated calls to check end-to-end consistency.
