# Rewrite Audit: pyyaml-fullrepro-001

## Summary

- collected nodeids processed: 2616
- original files observed: 4
- kept upstream nodeids: 889
- source-only exclusions: 39
- mechanical/protocol exclusions: 1688
- rewritten upstream tests: 0
- Track B trigger: not triggered; retained upstream oracle is above the 50-test global floor and covers all behavior sections.

## File Decisions

| file | nodeids | decision | rationale |
|---|---:|---|---|
| `tests/legacy_tests/test_yaml.py` | 1280 | retain with node-level filtering | kept 886; excluded 394 canonical-helper, no-assertion, exact-format, and implementation-hook rows |
| `tests/legacy_tests/test_yaml_ext.py` | 1325 | discard original file | private yaml._yaml import and optional C-extension wrapper; not retained under scorer isolation |
| `tests/test_dump_load.py` | 3 | retain | all nodeids use public top-level load/dump behavior |
| `tests/test_merge.py` | 8 | discard original file | asserts internal Loader.flatten_mapping/MappingNode.value behavior; public merge behavior covered by legacy constructor data |
