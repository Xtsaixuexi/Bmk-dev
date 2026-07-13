| test_nodeid | layer | spec_section | status | notes |
|---|---|---|---|---|
| `tests/messages/test_catalog.py::test_message_python_format` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_catalog.py::test_message_python_brace_format` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_catalog.py::test_message_translator_comments` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_catalog.py::test_message_clone_message_object` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_catalog.py::test_catalog_add_returns_message_instance` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_catalog.py::test_catalog_two_messages_with_same_singular` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_catalog.py::test_catalog_duplicate_auto_comment` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_catalog.py::test_catalog_duplicate_user_comment` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_catalog.py::test_catalog_duplicate_location` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_catalog.py::test_catalog_update_message_updates_comments` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test_2_num_plurals_checkers` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test_python_format_invalid[foo %s-foo]` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test_python_format_invalid[msgid1-msgstr1]` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test_python_format_invalid[msgid2-msgstr2]` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test_python_format_valid[foo-foo]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test_python_format_valid[foo-foo %s]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test_python_format_valid[foo %s-]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test__validate_format_invalid[%s %(foo)s-%s %(foo)s-format string mixes positional and named placeholders]` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test__validate_format_invalid[foo %s-foo-placeholders are incompatible]` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test__validate_format_invalid[%s-%(foo)s-the format strings are of different kinds]` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test__validate_format_valid[foo-foo]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test__validate_format_valid[foo-foo %s]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_checkers.py::test__validate_format_valid[%s foo-foo %s]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_simple_extract` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_various_calls` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_message_with_line_comment` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_message_with_multiline_comment` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_ignore_function_definitions` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_misplaced_comments` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_jsx_extraction[False]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_jsx_extraction[True]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_dotted_keyword_extract` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_template_string_standard_usage` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_template_string_tag_usage` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_inside_template_string` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_inside_template_string_with_linebreaks` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_js_extract.py::test_inside_nested_template_string` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_jslexer.py::test_unquote` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_jslexer.py::test_dollar_in_identifier` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_jslexer.py::test_dotted_name` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_jslexer.py::test_dotted_name_end` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_jslexer.py::test_template_string` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_jslexer.py::test_jsx` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_mofile.py::test_basics` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_unescape` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_unescape_of_quoted_newline` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_denormalize_on_msgstr_without_empty_first_line` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_extract_locations_valid_location_comment[\u2068file1.po\u2069-locations0]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_extract_locations_valid_location_comment[file1.po \u2068file 2.po\u2069 file3.po-locations1]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_extract_locations_valid_location_comment[file1.po:1 \u2068file 2.po\u2069:2 file3.po:3-locations2]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_extract_locations_invalid_location_comment[\u2068file 1.po]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_extract_locations_invalid_location_comment[file 1.po\u2069]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_extract_locations_invalid_location_comment[\u2069file 1.po\u2068]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_enclose_filename_if_necessary_no_change[file.po]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_enclose_filename_if_necessary_no_change[file_a.po]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_enclose_filename_if_necessary_no_change[file-a.po]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_enclose_filename_if_necessary_enclosed[file a.po]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_enclose_filename_if_necessary_enclosed[file\ta.po]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_iterable_of_mismatching_strings[1]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_iterable_of_mismatching_strings[-1]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_issue_1087` | atomic | Cross-View Invariants + Public API Behavior + Representative Workflow | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_issue_1134[False-msgid "foo"]` | atomic | Cross-View Invariants + Public API Behavior + Representative Workflow | covered | reference-passing upstream behavior |
| `tests/messages/test_pofile.py::test_issue_1134[False-msgid "foo"\nmsgid_plural "foos"]` | atomic | Cross-View Invariants + Public API Behavior + Representative Workflow | covered | reference-passing upstream behavior |

Total: 63 | kept (covered): 63 | spec_gap: 0 | source-only: 0 | excluded: 533 | final scoreable: 63
