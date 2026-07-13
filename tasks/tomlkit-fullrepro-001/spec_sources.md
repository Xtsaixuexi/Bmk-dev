# Spec Sources

## Public Documentation

- `/root/autodl-tmp/e2e/tomlkit/README.md`
- `/root/autodl-tmp/e2e/tomlkit/docs/index.rst`
- `/root/autodl-tmp/e2e/tomlkit/docs/quickstart.rst`
- `/root/autodl-tmp/e2e/tomlkit/docs/api.rst`

## Public Source Boundary

- `/root/autodl-tmp/e2e/tomlkit/tomlkit/__init__.py`
- `/root/autodl-tmp/e2e/tomlkit/tomlkit/api.py`
- `/root/autodl-tmp/e2e/tomlkit/tomlkit/toml_document.py`
- `/root/autodl-tmp/e2e/tomlkit/tomlkit/toml_file.py`
- `/root/autodl-tmp/e2e/tomlkit/tomlkit/items.py`
- `/root/autodl-tmp/e2e/tomlkit/tomlkit/exceptions.py`

## Boundary Notes

- Source code is used only to identify public exports, signatures, docstrings, and behavior exposed through documented classes.
- Candidate-visible spec must not reveal source layout, hidden tests, node ids, taxonomy, reference results, review files, or candidate score data.
- Tests importing private helpers are tracked as Stage 3 filter risk and are not used to expand the public API surface by themselves.
