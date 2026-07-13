# Spec Validation: cleo-fullrepro-001

## Files Validated

- `spec/spec_v1.md`
- `spec/spec_v1_candidate.md`
- `spec.md`

## Candidate Packet Check

- `spec/spec_v1_candidate.md` and root `spec.md` are byte-identical.
- Candidate-visible files do not include the internal header.
- Candidate-visible files do not include source checkout paths, task audit paths, test file paths, benchmark task metadata, kept-nodeid lists, or taxonomy artifacts.

## Public API Surface Considered

Primary documented entry points:

- `cleo.application.Application`
- `cleo.commands.command.Command`
- `cleo.helpers.argument`, `cleo.helpers.option`, and `cleo.helpers.tokenize`
- `cleo.io.inputs.Argument`, `Option`, `Definition`, `Input`, `ArgvInput`, and `StringInput`
- `cleo.io.outputs.Output`, `BufferedOutput`, `NullOutput`, `StreamOutput`, `SectionOutput`, `Verbosity`, and `Type`
- `cleo.io.io.IO`, `cleo.io.buffered_io.BufferedIO`, and `cleo.io.null_io.NullIO`
- `cleo.testers.CommandTester` and `cleo.testers.ApplicationTester`

Additional public import paths and extension points considered:

- built-in commands for help, list, and completions
- command loaders, including `CommandLoader` and `FactoryCommandLoader`
- formatter, style, and style-stack classes
- public UI helpers for tables, questions, choices, confirmations, progress, and styling
- console events and event dispatching
- public exception classes exposed from `cleo.exceptions`

## Eleven-Point Validation

1. Traceability to public docs and day-one knowledge: pass. Included behaviors come from README usage, public documentation, public import paths, and public behaviors exercised through tests.
2. Internal names or undocumented module paths: pass with note. The spec names modules that are documented, imported by users, or used as extension surfaces, and avoids private helper structure.
3. Invariants in behavioral language: pass. Definition, input, execution, and output projections are tied together through observable `must` relationships.
4. Non-goals listed: pass.
5. Hidden fixture shape assumptions: pass. Evaluation Notes describe public behaviors and explicitly exclude fixture-only helper names and exact terminal snapshots.
6. Behavioral statements use concrete verbs: pass. Candidate-visible requirements are written as public API behavior, returned values, raised errors, and observable output/state effects.
7. Conditional behavior states conditions explicitly: pass. Conditions are scoped with `when`, `if`, command contexts, or named input/output modes.
8. Failure paths included: pass. Missing command, invalid option, missing argument, validation failure, user error rendering, exception propagation, and status-code behavior are covered.
9. Product State Model before per-subsystem sections: pass. The spec defines definition, input, execution, and output projections before detailed API sections.
10. Escape hatches avoided: pass. The spec names supported public classes and user-visible behaviors while avoiding exact byte snapshots where they are not semantically stable.
11. Priority/override rules: pass with conservative handling. The spec covers observable behavior for quiet/verbosity/decorated output, default command behavior, alias/shortcut lookup, and tester execution without over-specifying private precedence internals.

## Residual Risk

- Cleo has rich terminal formatting and completion behavior. The spec intentionally checks semantic content, status codes, and public API state rather than exact ANSI bytes, cursor movement, or shell script text.
- Some public UI helper behavior is broad. The spec keeps it at documented, user-observable granularity and leaves private rendering internals to Stage 3 filtering.
