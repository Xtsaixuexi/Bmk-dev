# Specification Sources

The PyYAML specification was derived from the pinned yaml/pyyaml checkout and its public-facing material:

- README.md and pyproject.toml
- lib/yaml/__init__.py public exports and docstrings
- public loader, dumper, constructor, representer, resolver, error, token, event, node, and cyaml modules
- public-behavior examples and selected upstream tests used only by the spec writer/filter, not exposed to the candidate

The exact pinned source boundary and file list are preserved in the internal header of spec/spec_v1.md. Candidate-visible packets exclude this audit record.
