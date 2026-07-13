| test_nodeid | layer | spec_section | status | notes |
|---|---|---|---|---|
| `tests/test_cli.py::test_cli_main_empty` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_parser_empty` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_main_help` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_valid_args` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_invalid_choice` | system_e2e | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_invalid_args` | system_e2e | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_invalid_infile` | system_e2e | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_invalid_outfile` | system_e2e | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_stdout` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_script` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_encoding_stdout[encoding_utf8.sql-utf-8]` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_encoding_stdout[encoding_gbk.sql-gbk]` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_encoding_output_file[encoding_utf8.sql-utf-8]` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_encoding_output_file[encoding_gbk.sql-gbk]` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_encoding_stdin[encoding_utf8.sql-utf-8]` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_encoding_stdin[encoding_gbk.sql-gbk]` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_encoding` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_cli_multiple_files_with_inplace` | system_e2e | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_cli_multiple_files_without_inplace_fails` | system_e2e | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_cli_inplace_with_stdin_fails` | system_e2e | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_cli_outfile_with_multiple_files_fails` | system_e2e | Error Semantics + Representative Workflow | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_cli_single_file_inplace` | system_e2e | Cross-View Invariants + Representative Workflow | covered | reference-passing upstream behavior |
| `tests/test_cli.py::test_cli_error_handling_continues` | system_e2e | Error Semantics + Representative Workflow | covered | reference-passing upstream behavior |
| `tests/test_dos_prevention.py::TestDoSPrevention::test_large_tuple_list_performance` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_dos_prevention.py::TestDoSPrevention::test_deeply_nested_groups_limited` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_dos_prevention.py::TestDoSPrevention::test_very_large_token_list_limited` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_dos_prevention.py::TestDoSPrevention::test_nested_paren_within_cap_under_1s` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_dos_prevention.py::TestDoSPrevention::test_nested_case_within_cap_under_1s` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_dos_prevention.py::TestDoSPrevention::test_normal_sql_still_works` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_dos_prevention.py::TestDoSPrevention::test_reasonable_tuple_list_works` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_keywordcase` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_keywordcase_invalid_option` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_identifiercase` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_identifiercase_invalid_option` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_identifiercase_quotes` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_strip_comments_single` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_strip_comments_invalid_option` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_strip_comments_multi` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_strip_comments_preserves_linebreak` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_strip_comments_preserves_whitespace` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_strip_comments_preserves_hint` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_strip_ws` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_strip_ws_invalid_option` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_preserve_ws` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormat::test_notransform_of_quoted_crlf` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormatReindentAligned::test_basic` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormatReindentAligned::test_joins` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormatReindentAligned::test_case_statement` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormatReindentAligned::test_case_statement_with_between` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormatReindentAligned::test_group_by` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormatReindentAligned::test_group_by_subquery` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormatReindentAligned::test_window_functions` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestSpacesAroundOperators::test_basic` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestSpacesAroundOperators::test_bools` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestSpacesAroundOperators::test_nested` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestSpacesAroundOperators::test_wildcard_vs_mult` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormatReindent::test_option` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormatReindent::test_stmts` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormatReindent::test_keywords` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_format.py::TestFormatReindent::test_keywords_between` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_parenthesis` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_assignment[foo := 1;]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_assignment[foo := 1]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_typed_literal[x > DATE '2020-01-01']` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_typed_literal[x > TIMESTAMP '2020-01-01 00:00:00']` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_compare_expr[select a from b where c < d + e-Identifier-Identifier]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_compare_expr[select a from b where c < d + interval '1 day'-Identifier-TypedLiteral]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_compare_expr[select a from b where c < d + interval '6' month-Identifier-TypedLiteral]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifiers` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_simple_identifiers[1 as f]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_simple_identifiers[foo as f]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_simple_identifiers[foo f]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_group_identifier_list[foo, bar]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_group_identifier_list[sum(a), sum(b)]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_group_identifier_list[sum(a) as x, b as y]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifier_wildcard` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifier_name_wildcard` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifier_invalid` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifier_invalid_in_middle` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifer_as[foo as (select *)]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifer_as[foo as(select *)]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifier_as_invalid` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifier_function` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_operation[foo+100]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_operation[foo + 100]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_operation[foo*100]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifier_list` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifier_list_subquery` | atomic | Cross-View Invariants + Public API Behavior | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifier_list_case` | atomic | Cross-View Invariants + Public API Behavior | covered | reference-passing upstream behavior |
| `tests/test_grouping.py::test_grouping_identifier_list_other` | atomic | Cross-View Invariants + Public API Behavior | covered | reference-passing upstream behavior |

Total: 90 | kept (covered): 90 | spec_gap: 0 | source-only: 0 | excluded: 400 | final scoreable: 90
