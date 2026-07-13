| test_nodeid | layer | spec_section | status | notes |
|---|---|---|---|---|
| `test/test_cache.py::test_modulepickling_change_cache_dir` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_cache.py::test_modulepickling_simulate_deleted_cache` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_cache.py::test_cache_limit` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_cache.py::test_cache_last_used_update[False-False]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_cache.py::test_cache_last_used_update[False-True]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_cache.py::test_cache_last_used_update[True-False]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_cache.py::test_inactive_cache` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_cache.py::test_permission_error` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_simple` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_change_and_undo` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_positions` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_if_simple` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_func_with_for_and_comment` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_one_statement_func` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_for_on_one_line` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_open_parentheses` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_open_parentheses_at_end` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_backslash` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_full_copy` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_wrong_whitespace` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_issues_with_error_leaves` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_unfinished_nodes` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_nested_if_and_scopes` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_word_before_def` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_classes_with_error_leaves` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_totally_wrong_whitespace` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_node_insertion` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_whitespace_at_end` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_endless_while_loop` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_in_class_movements` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_in_parentheses_newlines` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_indentation_issue` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_endmarker_newline` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_newlines_at_end` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_end_newline_with_decorator` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_invalid_to_valid_nodes` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_if_removal_and_reappearence` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_diff_parser.py::test_add_error_indentation` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_dump_tree.py::test_dump_parser_tree[None-Module([Lambda([Keyword('lambda', (1, 0)), Param([Name('x', (1, 7), prefix=' '), Operator(',', (1, 8)), ]), Param([Name('y', (1, 10), prefix=' '), ]), Operator(':', (1, 11)), PythonNode('arith_expr', [Name('x', (1, 13), prefix=' '), Operator('+', (1, 15), prefix=' '), Name('y', (1, 17), prefix=' '), ]), ]), EndMarker('', (1, 18)), ])]` | integration | Cross-View Invariants + Representative Workflow | covered | reference-passing upstream behavior |
| `test/test_dump_tree.py::test_dump_parser_tree[0-Module([\nLambda([\nKeyword('lambda', (1, 0)),\nParam([\nName('x', (1, 7), prefix=' '),\nOperator(',', (1, 8)),\n]),\nParam([\nName('y', (1, 10), prefix=' '),\n]),\nOperator(':', (1, 11)),\nPythonNode('arith_expr', [\nName('x', (1, 13), prefix=' '),\nOperator('+', (1, 15), prefix=' '),\nName('y', (1, 17), prefix=' '),\n]),\n]),\nEndMarker('', (1, 18)),\n])]` | integration | Cross-View Invariants + Representative Workflow | covered | reference-passing upstream behavior |
| `test/test_dump_tree.py::test_dump_parser_tree[4-Module([\n    Lambda([\n        Keyword('lambda', (1, 0)),\n        Param([\n            Name('x', (1, 7), prefix=' '),\n            Operator(',', (1, 8)),\n        ]),\n        Param([\n            Name('y', (1, 10), prefix=' '),\n        ]),\n        Operator(':', (1, 11)),\n        PythonNode('arith_expr', [\n            Name('x', (1, 13), prefix=' '),\n            Operator('+', (1, 15), prefix=' '),\n            Name('y', (1, 17), prefix=' '),\n        ]),\n    ]),\n    EndMarker('', (1, 18)),\n])]` | integration | Cross-View Invariants + Representative Workflow | covered | reference-passing upstream behavior |
| `test/test_dump_tree.py::test_dump_parser_tree_not_top_level_module[node0-Function([\n    Keyword('def', (1, 0)),\n    Name('foo', (1, 4), prefix=' '),\n    PythonNode('parameters', [\n        Operator('(', (1, 7)),\n        Param([\n            Name('x', (1, 8)),\n            Operator(',', (1, 9)),\n        ]),\n        Param([\n            Name('y', (1, 11), prefix=' '),\n        ]),\n        Operator(')', (1, 12)),\n    ]),\n    Operator(':', (1, 13)),\n    ReturnStmt([\n        Keyword('return', (1, 15), prefix=' '),\n        PythonNode('arith_expr', [\n            Name('x', (1, 22), prefix=' '),\n            Operator('+', (1, 24), prefix=' '),\n            Name('y', (1, 26), prefix=' '),\n        ]),\n    ]),\n])-def foo(x, y): return x + y]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_dump_tree.py::test_dump_parser_tree_not_top_level_module[node1-Keyword('def', (1, 0))-def]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_dump_tree.py::test_dump_parser_tree_not_top_level_module[node2-ErrorLeaf('error_type', 'error_code', (1, 1), prefix=' ')- error_code]` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_dump_tree.py::test_dump_parser_tree_invalid_args` | integration | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_dump_tree.py::test_eval_dump_recovers_parent` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_error_recovery.py::test_with_stmt` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_error_recovery.py::test_one_line_function[3.6]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_error_recovery.py::test_one_line_function[3.7]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_error_recovery.py::test_one_line_function[3.8]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_error_recovery.py::test_if_else` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_error_recovery.py::test_if_stmt` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_error_recovery.py::test_invalid_token` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_error_recovery.py::test_invalid_token_in_fstr` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_error_recovery.py::test_dedent_issues1` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_error_recovery.py::test_dedent_issues2` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_error_recovery.py::test_dedent_issues3` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_file_python_errors.py::test_on_itself[3.6]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_file_python_errors.py::test_on_itself[3.7]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_file_python_errors.py::test_on_itself[3.8]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_fstring.py::test_valid[f"{1}"]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_fstring.py::test_valid[f"""{1}"""]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_fstring.py::test_valid[f"{foo} {bar}"]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_fstring.py::test_invalid[f"}"]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_fstring.py::test_invalid[f"{"]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_fstring.py::test_invalid[f"""}"""]` | atomic | Error Semantics | covered | reference-passing upstream behavior |
| `test/test_fstring.py::test_tokenize_start_pos[f"}{"-positions0]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_fstring.py::test_tokenize_start_pos[f" :{ 1 : } "-positions1]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_fstring.py::test_tokenize_start_pos[f"""\n {\nfoo\n }"""-positions2]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_fstring.py::test_roundtrip[f'''s{\n   str.uppe\n'''\n]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_fstring.py::test_roundtrip[f"foo]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_fstring.py::test_roundtrip[f"""foo]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_get_code.py::test_basic_parsing` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_get_code.py::test_operators` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_get_code.py::test_get_code` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_get_code.py::test_end_newlines` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_get_code.py::test_carriage_return_at_end[\r-types0]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_get_code.py::test_carriage_return_at_end[\n\r-types1]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_get_code.py::test_full_code_round_trip[ ]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_get_code.py::test_full_code_round_trip[    F"""]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_get_code.py::test_full_code_round_trip[    F"""\n]` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_grammar.py::test_non_unicode` | atomic | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_load_grammar.py::test_load_inexisting_grammar` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_load_grammar.py::test_load_grammar_uses_older_syntax` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_load_grammar.py::test_load_grammar_doesnt_warn[3.6]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_load_grammar.py::test_load_grammar_doesnt_warn[3.7]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_load_grammar.py::test_load_grammar_doesnt_warn[3.8]` | integration | Cross-View Invariants | covered | reference-passing upstream behavior |
| `test/test_load_grammar.py::test_parse_version[2-result0]` | integration | Cross-View Invariants + Public API Behavior | covered | reference-passing upstream behavior |
| `test/test_load_grammar.py::test_parse_version[3-result1]` | integration | Cross-View Invariants + Public API Behavior | covered | reference-passing upstream behavior |
| `test/test_load_grammar.py::test_parse_version[1.1-result2]` | integration | Cross-View Invariants + Public API Behavior | covered | reference-passing upstream behavior |

Total: 90 | kept (covered): 90 | spec_gap: 0 | source-only: 0 | excluded: 1896 | final scoreable: 90
