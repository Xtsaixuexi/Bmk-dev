# Spec Sources: jsonpickle-fullrepro-001

The candidate-visible specification was derived from public jsonpickle documentation and public package surfaces at commit `4bdc0d60779b8dac952b46788b5b858223a24674`.

Public source categories used:

- project README and documentation for encode/decode, object graphs, references, handlers, and backend configuration;
- top-level public exports and documented modules for `Pickler`, `Unpickler`, `JSONBackend`, handlers, registry helpers, and public errors;
- public docstrings and reference-observed behavior used only to validate priority and override rules stated in the documentation;
- public wire-format compatibility documentation for jsonpickle tags and legacy `v1_decode` behavior.

Excluded from the candidate-visible specification: private helpers, test fixtures, optional dependency internals, exact hidden assertions, filtered nodeids, score artifacts, and source paths.
