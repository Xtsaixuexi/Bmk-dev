# MiniDotenv Source Repository Mapping

Source repository: `theskumar/python-dotenv`

GitHub: https://github.com/theskumar/python-dotenv

## Why This Repository

`python-dotenv` is a mature Python project for reading `.env` files and loading configuration into process environments. It has real parsing rules, environment override semantics, interpolation behavior, path discovery, and file mutation helpers. These features are small enough to abstract into a compact benchmark while still producing meaningful system-level interactions.

## Abstraction Boundary

MiniDotenv keeps the core configuration-loading behavior:

- `.env` parsing
- quoted and unquoted values
- comments and `export` prefixes
- `${VAR}` and `${VAR:-default}` interpolation
- `dotenv_values` and `load_dotenv`
- override behavior against `os.environ`
- upward path discovery
- `get_key`, `set_key`, and `unset_key`

MiniDotenv excludes the full original project surface:

- Click CLI integration
- IPython extension
- `dotenv run` process execution
- full Bash-compatible parsing
- multiline edge cases
- platform-specific filesystem details
- exact warning/logger text

## Benchmark Intent

The task is designed to expose unit/system gaps. A candidate may parse simple key-value lines correctly but still fail when parsing, interpolation, override rules, file mutation, path discovery, and repeated environment operations interact.
