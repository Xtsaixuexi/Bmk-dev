# Rewrite Audit

Stage 3 Track A processed every collected upstream nodeid. No test source rewrites were needed: retained nodeids use public Cleo imports or standalone test fixtures, and excluded nodeids were removed at node level for private access, environment dependence, or source-only assertions.

| test_file | collected | kept | source-only | excluded | decision |
|---|---:|---:|---:|---:|---|
| `tests/commands/completion/test_completions_command.py` | 4 | 1 | 0 | 3 | partially retained after node-level filtering |
| `tests/commands/test_command.py` | 5 | 3 | 2 | 0 | partially retained after node-level filtering |
| `tests/events/test_event.py` | 2 | 2 | 0 | 0 | retained |
| `tests/events/test_event_dispatcher.py` | 7 | 7 | 0 | 0 | retained |
| `tests/fixtures/exceptions/nested1.py` | 1 | 0 | 0 | 1 | discarded after filtering |
| `tests/fixtures/exceptions/nested2.py` | 1 | 0 | 0 | 1 | discarded after filtering |
| `tests/fixtures/exceptions/raiser_with_suppressed_context.py` | 1 | 0 | 0 | 1 | discarded after filtering |
| `tests/fixtures/exceptions/recursion.py` | 1 | 0 | 0 | 1 | discarded after filtering |
| `tests/fixtures/exceptions/simple.py` | 1 | 0 | 0 | 1 | discarded after filtering |
| `tests/formatters/test_formatter.py` | 13 | 0 | 13 | 0 | discarded after filtering |
| `tests/io/inputs/test_argument.py` | 5 | 3 | 2 | 0 | partially retained after node-level filtering |
| `tests/io/inputs/test_argv_input.py` | 19 | 18 | 0 | 1 | partially retained after node-level filtering |
| `tests/io/inputs/test_option.py` | 15 | 15 | 0 | 0 | retained |
| `tests/io/outputs/test_section_output.py` | 8 | 0 | 8 | 0 | discarded after filtering |
| `tests/io/outputs/test_stream_output.py` | 2 | 0 | 0 | 2 | discarded after filtering |
| `tests/loaders/test_factory_command_loader.py` | 4 | 4 | 0 | 0 | retained |
| `tests/test_application.py` | 31 | 18 | 12 | 1 | partially retained after node-level filtering |
| `tests/test_color.py` | 7 | 0 | 0 | 7 | discarded after filtering |
| `tests/test_helpers.py` | 2 | 2 | 0 | 0 | retained |
| `tests/test_terminal.py` | 9 | 0 | 0 | 9 | discarded after filtering |
| `tests/test_utils.py` | 34 | 0 | 0 | 34 | discarded after filtering |
| `tests/testers/test_application_tester.py` | 2 | 2 | 0 | 0 | retained |
| `tests/testers/test_command_tester.py` | 2 | 2 | 0 | 0 | retained |
| `tests/ui/exception_trace/helpers.py` | 3 | 0 | 0 | 3 | discarded after filtering |
| `tests/ui/exception_trace/test_frame.py` | 2 | 0 | 2 | 0 | discarded after filtering |
| `tests/ui/exception_trace/test_inspector.py` | 3 | 0 | 3 | 0 | discarded after filtering |
| `tests/ui/test_choice_question.py` | 1 | 0 | 1 | 0 | discarded after filtering |
| `tests/ui/test_confirmation_question.py` | 7 | 7 | 0 | 0 | retained |
| `tests/ui/test_exception_trace.py` | 13 | 0 | 13 | 0 | discarded after filtering |
| `tests/ui/test_progress_bar.py` | 25 | 1 | 24 | 0 | partially retained after node-level filtering |
| `tests/ui/test_progress_indicator.py` | 2 | 0 | 2 | 0 | discarded after filtering |
| `tests/ui/test_question.py` | 5 | 2 | 2 | 1 | partially retained after node-level filtering |
| `tests/ui/test_table.py` | 21 | 0 | 21 | 0 | discarded after filtering |

Summary: functions_in_scope=258, functions_kept=87, functions_excluded=171. Track B not triggered because Track A retained 87 scoreable nodeids with atomic, integration, and system_e2e coverage above the global floor.
