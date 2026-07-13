# Spec Test Map: lark-fullrepro-001

Spec: `spec/spec_v1.md`
Collection source: `python -m pytest tests --collect-only` from the Lark source tree; node IDs are routed through `tests/__main__.py` because upstream aggregates unittest classes there.

| test_nodeid | layer | spec_section | status | notes |
|---|---|---|---|---|
| `tests/__main__.py::TestTrees::test_copy` | atomic | Tree and Token Model + Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_deepcopy` | atomic | Tree and Token Model + Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_discard` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_eq` | atomic | Tree and Token Model + Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_find_token` | atomic | Tree and Token Model + Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_incorrect_use_of_decorators` | atomic | - | source-only | asserts exact repr/message/cache naming/decorator descriptor edge not specified as public contract |
| `tests/__main__.py::TestTrees::test_inline_static` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestTrees::test_interp` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_iter_subtrees` | atomic | Tree and Token Model + Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_iter_subtrees_topdown` | atomic | Tree and Token Model + Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_merge_transformers` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_partial` | atomic | - | source-only | asserts exact repr/message/cache naming/decorator descriptor edge not specified as public contract |
| `tests/__main__.py::TestTrees::test_pickle` | atomic | - | source-only | pickle round-trip for Tree is not documented as public behavior |
| `tests/__main__.py::TestTrees::test_repr_runnable` | atomic | - | source-only | asserts exact repr/message/cache naming/decorator descriptor edge not specified as public contract |
| `tests/__main__.py::TestTrees::test_smart_decorator` | atomic | - | source-only | asserts exact repr/message/cache naming/decorator descriptor edge not specified as public contract |
| `tests/__main__.py::TestTrees::test_transform_token` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_transformer` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_transformer_variants` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_vargs` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_vargs_override` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTrees::test_vargs_set_name` | atomic | - | source-only | asserts exact repr/message/cache naming/decorator descriptor edge not specified as public contract |
| `tests/__main__.py::TestTrees::test_visitor` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestStandalone::test_contextual` | system_e2e | - | excluded | standalone tool executes generated module/subprocess-like tooling; environment-sensitive for hidden oracle |
| `tests/__main__.py::TestStandalone::test_interactive` | system_e2e | - | excluded | standalone tool executes generated module/subprocess-like tooling; environment-sensitive for hidden oracle |
| `tests/__main__.py::TestStandalone::test_postlex` | system_e2e | - | excluded | standalone tool executes generated module/subprocess-like tooling; environment-sensitive for hidden oracle |
| `tests/__main__.py::TestStandalone::test_simple` | system_e2e | - | excluded | standalone tool executes generated module/subprocess-like tooling; environment-sensitive for hidden oracle |
| `tests/__main__.py::TestStandalone::test_transformer` | system_e2e | - | excluded | standalone tool executes generated module/subprocess-like tooling; environment-sensitive for hidden oracle |
| `tests/__main__.py::TestCache::test_automatic_naming` | atomic | - | source-only | asserts exact repr/message/cache naming/decorator descriptor edge not specified as public contract |
| `tests/__main__.py::TestCache::test_cache_grammar` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCache::test_custom_lexer` | atomic | - | source-only | asserts exact repr/message/cache naming/decorator descriptor edge not specified as public contract |
| `tests/__main__.py::TestCache::test_error_message` | atomic | - | source-only | asserts exact repr/message/cache naming/decorator descriptor edge not specified as public contract |
| `tests/__main__.py::TestCache::test_imports` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCache::test_inline` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestCache::test_options` | system_e2e | Public API + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCache::test_reconstruct` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCache::test_recursive_pattern` | system_e2e | Public API + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCache::test_simple` | system_e2e | Public API + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestGrammar::test_alias_in_terminal` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_declare_rule_name` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_empty_literal` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_errors` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestGrammar::test_extend_rule` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_extend_term` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_extend_twice` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_find_grammar_errors` | atomic | - | source-only | asserts exact repr/message/cache naming/decorator descriptor edge not specified as public contract |
| `tests/__main__.py::TestGrammar::test_ignore_name` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_import_custom_sources` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestGrammar::test_import_custom_sources2` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestGrammar::test_import_custom_sources3` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestGrammar::test_inline_with_expand_single` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestGrammar::test_large_terminal` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_line_breaks` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestGrammar::test_list_grammar_imports` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestGrammar::test_override_rule` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_override_terminal` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_ranged_repeat_large` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_ranged_repeat_terms` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_symbol_eq` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_template_in_terminal` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_token_multiline_only_works_with_x_flag` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestGrammar::test_undefined_ignore` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_undefined_rule` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestGrammar::test_undefined_term` | atomic | Grammar Language + Error Semantics | covered |  |
| `tests/__main__.py::TestReconstructor::test_alias` | system_e2e | Advanced Public APIs | covered |  |
| `tests/__main__.py::TestReconstructor::test_expand_rule` | system_e2e | Advanced Public APIs | covered |  |
| `tests/__main__.py::TestReconstructor::test_json_example` | system_e2e | Advanced Public APIs | covered |  |
| `tests/__main__.py::TestReconstructor::test_keep_all_tokens` | system_e2e | Advanced Public APIs | covered |  |
| `tests/__main__.py::TestReconstructor::test_keep_tokens` | system_e2e | Advanced Public APIs | covered |  |
| `tests/__main__.py::TestReconstructor::test_starred_group` | system_e2e | Advanced Public APIs | covered |  |
| `tests/__main__.py::TestReconstructor::test_starred_rule` | system_e2e | Advanced Public APIs | covered |  |
| `tests/__main__.py::TestReconstructor::test_switch_grammar_unicode_terminal` | system_e2e | Advanced Public APIs | covered |  |
| `tests/__main__.py::TestTreeForestTransformer::test_aliases` | integration | Advanced Public APIs + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestTreeForestTransformer::test_default_ambig` | integration | Advanced Public APIs + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestTreeForestTransformer::test_default_rule` | integration | Advanced Public APIs + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestTreeForestTransformer::test_default_token` | integration | Advanced Public APIs + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestTreeForestTransformer::test_discard` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTreeForestTransformer::test_handles_ambiguity` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestTreeForestTransformer::test_identity_explicit_ambiguity` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestTreeForestTransformer::test_identity_resolve_ambiguity` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestTreeForestTransformer::test_rule_calls` | integration | Advanced Public APIs + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestTreeForestTransformer::test_token_calls` | integration | Advanced Public APIs + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestTreeForestTransformer::test_transformation` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestTreeForestTransformer::test_tree_class` | integration | Advanced Public APIs + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLexer::test_basic` | atomic | Parsing and Lexing Behavior + Tree and Token Model | covered |  |
| `tests/__main__.py::TestLexer::test_subset_lex` | atomic | Parsing and Lexing Behavior + Tree and Token Model | covered |  |
| `tests/__main__.py::TestPythonParser::test_BIN_NUMBER` | atomic | - | excluded | built-in Python grammar language details are out of scope for Lark public API reconstruction |
| `tests/__main__.py::TestPythonParser::test_DEC_NUMBER` | atomic | - | excluded | built-in Python grammar language details are out of scope for Lark public API reconstruction |
| `tests/__main__.py::TestPythonParser::test_FLOAT_NUMBER` | atomic | - | excluded | built-in Python grammar language details are out of scope for Lark public API reconstruction |
| `tests/__main__.py::TestPythonParser::test_HEX_NUMBER` | atomic | - | excluded | built-in Python grammar language details are out of scope for Lark public API reconstruction |
| `tests/__main__.py::TestPythonParser::test_IMAG_NUMBER` | atomic | - | excluded | built-in Python grammar language details are out of scope for Lark public API reconstruction |
| `tests/__main__.py::TestPythonParser::test_OCT_NUMBER` | atomic | - | excluded | built-in Python grammar language details are out of scope for Lark public API reconstruction |
| `tests/__main__.py::TestPythonParser::test_assign_expr_with_variable_named_match` | atomic | - | excluded | built-in Python grammar language details are out of scope for Lark public API reconstruction |
| `tests/__main__.py::TestPythonParser::test_assign_to_variable_named_match` | atomic | - | excluded | built-in Python grammar language details are out of scope for Lark public API reconstruction |
| `tests/__main__.py::TestPythonParser::test_invalid_match_statement` | atomic | - | excluded | built-in Python grammar language details are out of scope for Lark public API reconstruction |
| `tests/__main__.py::TestPythonParser::test_invalid_number` | atomic | - | excluded | built-in Python grammar language details are out of scope for Lark public API reconstruction |
| `tests/__main__.py::TestPythonParser::test_valid_match_statement` | atomic | - | excluded | built-in Python grammar language details are out of scope for Lark public API reconstruction |
| `tests/__main__.py::TestPythonParser::test_valid_number` | atomic | - | excluded | built-in Python grammar language details are out of scope for Lark public API reconstruction |
| `tests/__main__.py::TestTreeTemplatesConf::test_conf_call__same_tree` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesConf::test_conf_test_var__is_var` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesConf::test_conf_test_var__not_var` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesConf::test_template_match__default_conf_match_same_tree__empty_dictionary` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesConf::test_template_match__only_tree` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplateTranslator::test_translate__empty_translations__same_tree` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplateTranslator::test_translate__one_translations__same_tree` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplate::test_template_apply_vars__empty__exception` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplate::test_template_apply_vars__matching_vars__template_replaced` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplate::test_template_apply_vars__no_matching_vars__exception` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplate::test_template_match__different_tree__none` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplate::test_template_match__different_tree_no_template__none` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplate::test_template_match__no_template__empty_dictionary` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplate::test_template_match__same_tree_no_template__empty_dictionary` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplate::test_template_match__with_template__empty_dictionary` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplate::test_template_search__same_tree_as_child__empty_generator` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplate::test_template_search__same_tree_no_template__empty_generator` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplate::test_template_search__with_template__matched_result_with_parent_tree` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::TestTreeTemplatesTemplateDefaultConf::test_template_match__match_same_tree__empty_dictionary` | atomic | - | excluded | undocumented tree template helper API; not in spec scope |
| `tests/__main__.py::Testlogger::test_debug` | atomic | - | excluded | asserts logging/debug collision output and optional interegular behavior; environment/exact-output sensitive |
| `tests/__main__.py::Testlogger::test_loglevel_higher` | atomic | - | excluded | asserts logging/debug collision output and optional interegular behavior; environment/exact-output sensitive |
| `tests/__main__.py::Testlogger::test_no_regex_collision` | atomic | - | excluded | asserts logging/debug collision output and optional interegular behavior; environment/exact-output sensitive |
| `tests/__main__.py::Testlogger::test_non_debug` | atomic | - | excluded | asserts logging/debug collision output and optional interegular behavior; environment/exact-output sensitive |
| `tests/__main__.py::Testlogger::test_regex_collision` | atomic | - | excluded | asserts logging/debug collision output and optional interegular behavior; environment/exact-output sensitive |
| `tests/__main__.py::TestParsers::test_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestParsers::test_backwards_custom_lexer` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestParsers::test_big_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestParsers::test_comment_in_rule_definition` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestParsers::test_custom_input` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestParsers::test_embedded_transformer` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestParsers::test_embedded_transformer_inplace` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestParsers::test_expand1` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestParsers::test_infinite_recurse` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestParsers::test_lexer_token_limit` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestParsers::test_propagate_positions` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestParsers::test_propagate_positions2` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestParsers::test_same_ast` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestParsers::test_vargs_meta` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestParsers::test_vargs_tree` | integration | Transformers, Visitors, and Interpreters | covered |  |
| `tests/__main__.py::TestParsers::test_visit_tokens` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestParsers::test_visit_tokens2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_backslash` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_backslash2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_basic1` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_basic2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_bytes_utf8` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_default_in_treeless_mode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_dont_expand1_lists_with_multiple_items` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_dont_expand1_lists_with_multiple_items_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_dynamic_lexer_prioritization` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_empty` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_empty_end` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_empty_expand1_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_empty_expand1_list_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_empty_flatten_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_error_with_interactive_parser` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_escaped_string` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_expand1_lists_with_one_item` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_expand1_lists_with_one_item_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_float_without_lexer` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_g_regex_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_hex_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_hex_literal_range_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_ignore` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_import_errors` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_interactive_treeless_transformer` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_iter_parse` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_join_regex_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_keep_all_tokens` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_lexer_detect_newline_tokens` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_lexer_prioritization` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_line_and_column` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_line_counting` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_match_examples` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_maybe` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_maybe_placeholders` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_meddling_unused` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_multi_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_multi_start` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_on_error_without_lalr` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_parse_textslice` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_parse_textslice_fails` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_parser_interactive_parser` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_postlex_declare` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_postlex_indenter` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_prioritization` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_prioritization_sum` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_priority_vs_embedded` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_ranged_repeat_rules` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_reduce_cycle` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_regex_escaping` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_regex_quote` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_regex_width_fallback` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestEarleyBasic::test_relative_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_relative_import_of_nested_grammar` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_relative_import_preserves_leading_underscore` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_relative_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_relative_import_rules_dependencies_imported_only_once` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_relative_import_unicode` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_relative_multi_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_relative_rule_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_relative_rule_import_drop_ignore` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_relative_rule_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_relative_rule_import_subrule` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_relative_rule_import_subrule_no_conflict` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_rule_collision` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_rule_collision2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_serialize` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_serialize_with_transformer` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_special_chars` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_stack_for_ebnf` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_start` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_strict` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_stringio_unicode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_templates` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_templates_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_templates_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_templates_modifiers` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_templates_recursion` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_templates_templates` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_token_collision` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_token_collision2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_token_collision_WS` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_token_ebnf` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_token_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_token_flags2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_token_flags3` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_token_flags_collision` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_token_flags_verbose` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_token_flags_verbose_multiline` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_token_not_anon` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_twice_empty` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_unicode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_unicode2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_unicode3` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_unicode4` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_unicode_class` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestEarleyBasic::test_unicode_literal_range_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_unicode_literal_range_escape2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyBasic::test_unicode_word` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestEarleyBasic::test_utf8` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestCykBasic::test_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_backslash` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_backslash2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_basic1` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_basic2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_bytes_utf8` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestCykBasic::test_default_in_treeless_mode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_dont_expand1_lists_with_multiple_items` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_dont_expand1_lists_with_multiple_items_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_dynamic_lexer_prioritization` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_empty` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_empty_end` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_empty_expand1_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_empty_expand1_list_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_empty_flatten_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_error_with_interactive_parser` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestCykBasic::test_escaped_string` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_expand1_lists_with_one_item` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_expand1_lists_with_one_item_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_float_without_lexer` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_g_regex_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_hex_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_hex_literal_range_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_ignore` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_import_errors` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_interactive_treeless_transformer` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestCykBasic::test_iter_parse` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestCykBasic::test_join_regex_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_keep_all_tokens` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_lexer_detect_newline_tokens` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_lexer_prioritization` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_line_and_column` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestCykBasic::test_line_counting` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestCykBasic::test_match_examples` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestCykBasic::test_maybe` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_maybe_placeholders` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_meddling_unused` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_multi_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_multi_start` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_on_error_without_lalr` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestCykBasic::test_parse_textslice` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestCykBasic::test_parse_textslice_fails` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestCykBasic::test_parser_interactive_parser` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestCykBasic::test_postlex_declare` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_postlex_indenter` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_prioritization` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_prioritization_sum` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_priority_vs_embedded` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_ranged_repeat_rules` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_reduce_cycle` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_regex_escaping` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_regex_quote` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_regex_width_fallback` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestCykBasic::test_relative_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_relative_import_of_nested_grammar` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_relative_import_preserves_leading_underscore` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_relative_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_relative_import_rules_dependencies_imported_only_once` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_relative_import_unicode` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_relative_multi_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_relative_rule_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_relative_rule_import_drop_ignore` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_relative_rule_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_relative_rule_import_subrule` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_relative_rule_import_subrule_no_conflict` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_rule_collision` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_rule_collision2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_serialize` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_serialize_with_transformer` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_special_chars` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_stack_for_ebnf` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_start` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_strict` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_stringio_unicode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_templates` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_templates_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_templates_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestCykBasic::test_templates_modifiers` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_templates_recursion` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_templates_templates` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_token_collision` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_token_collision2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_token_collision_WS` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_token_ebnf` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_token_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_token_flags2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_token_flags3` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_token_flags_collision` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_token_flags_verbose` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_token_flags_verbose_multiline` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestCykBasic::test_token_not_anon` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_twice_empty` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_unicode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_unicode2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_unicode3` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_unicode4` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_unicode_class` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestCykBasic::test_unicode_literal_range_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_unicode_literal_range_escape2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestCykBasic::test_unicode_word` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestCykBasic::test_utf8` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrBasic::test_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_backslash` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_backslash2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_basic1` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_basic2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_bytes_utf8` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrBasic::test_default_in_treeless_mode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_dont_expand1_lists_with_multiple_items` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_dont_expand1_lists_with_multiple_items_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_dynamic_lexer_prioritization` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_empty` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_empty_end` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_empty_expand1_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_empty_expand1_list_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_empty_flatten_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_error_with_interactive_parser` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestLalrBasic::test_escaped_string` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_expand1_lists_with_one_item` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_expand1_lists_with_one_item_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_float_without_lexer` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_g_regex_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_hex_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_hex_literal_range_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_ignore` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_import_errors` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_interactive_treeless_transformer` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestLalrBasic::test_iter_parse` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestLalrBasic::test_join_regex_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_keep_all_tokens` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_lexer_detect_newline_tokens` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_lexer_prioritization` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_line_and_column` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrBasic::test_line_counting` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrBasic::test_match_examples` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestLalrBasic::test_maybe` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_maybe_placeholders` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_meddling_unused` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_multi_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_multi_start` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_on_error_without_lalr` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestLalrBasic::test_parse_textslice` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrBasic::test_parse_textslice_fails` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrBasic::test_parser_interactive_parser` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestLalrBasic::test_postlex_declare` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_postlex_indenter` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_prioritization` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_prioritization_sum` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_priority_vs_embedded` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_ranged_repeat_rules` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_reduce_cycle` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_regex_escaping` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_regex_quote` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_regex_width_fallback` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestLalrBasic::test_relative_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_relative_import_of_nested_grammar` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_relative_import_preserves_leading_underscore` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_relative_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_relative_import_rules_dependencies_imported_only_once` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_relative_import_unicode` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_relative_multi_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_relative_rule_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_relative_rule_import_drop_ignore` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_relative_rule_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_relative_rule_import_subrule` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_relative_rule_import_subrule_no_conflict` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_rule_collision` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_rule_collision2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_serialize` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_serialize_with_transformer` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_special_chars` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_stack_for_ebnf` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_start` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_strict` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_stringio_unicode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_templates` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_templates_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_templates_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrBasic::test_templates_modifiers` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_templates_recursion` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_templates_templates` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_token_collision` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_token_collision2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_token_collision_WS` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_token_ebnf` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_token_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_token_flags2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_token_flags3` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_token_flags_collision` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_token_flags_verbose` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_token_flags_verbose_multiline` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrBasic::test_token_not_anon` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_twice_empty` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_unicode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_unicode2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_unicode3` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_unicode4` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_unicode_class` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestLalrBasic::test_unicode_literal_range_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_unicode_literal_range_escape2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrBasic::test_unicode_word` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestLalrBasic::test_utf8` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_backslash` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_backslash2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_basic1` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_basic2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_bytes_utf8` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_default_in_treeless_mode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_dont_expand1_lists_with_multiple_items` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_dont_expand1_lists_with_multiple_items_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_dynamic_lexer_prioritization` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_empty` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_empty_end` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_empty_expand1_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_empty_expand1_list_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_empty_flatten_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_error_with_interactive_parser` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_escaped_string` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_expand1_lists_with_one_item` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_expand1_lists_with_one_item_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_float_without_lexer` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_g_regex_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_hex_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_hex_literal_range_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_ignore` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_import_errors` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_interactive_treeless_transformer` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_iter_parse` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_join_regex_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_keep_all_tokens` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_lexer_detect_newline_tokens` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_lexer_prioritization` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_line_and_column` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_line_counting` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_match_examples` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_maybe` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_maybe_placeholders` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_meddling_unused` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_multi_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_multi_start` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_on_error_without_lalr` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_parse_textslice` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_parse_textslice_fails` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_parser_interactive_parser` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_postlex_declare` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_postlex_indenter` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_prioritization` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_prioritization_sum` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_priority_vs_embedded` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_ranged_repeat_rules` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_reduce_cycle` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_regex_escaping` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_regex_quote` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_regex_width_fallback` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestEarleyDynamic::test_relative_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_relative_import_of_nested_grammar` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_relative_import_preserves_leading_underscore` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_relative_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_relative_import_rules_dependencies_imported_only_once` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_relative_import_unicode` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_relative_multi_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_relative_rule_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_relative_rule_import_drop_ignore` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_relative_rule_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_relative_rule_import_subrule` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_relative_rule_import_subrule_no_conflict` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_rule_collision` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_rule_collision2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_serialize` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_serialize_with_transformer` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_special_chars` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_stack_for_ebnf` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_start` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_strict` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_stringio_unicode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_templates` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_templates_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_templates_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_templates_modifiers` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_templates_recursion` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_templates_templates` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_token_collision` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_token_collision2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_token_collision_WS` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_token_ebnf` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_token_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_token_flags2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_token_flags3` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_token_flags_collision` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_token_flags_verbose` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_token_flags_verbose_multiline` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_token_not_anon` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_twice_empty` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_unicode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_unicode2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_unicode3` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_unicode4` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_unicode_class` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestEarleyDynamic::test_unicode_literal_range_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_unicode_literal_range_escape2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic::test_unicode_word` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestEarleyDynamic::test_utf8` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_backslash` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_backslash2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_basic1` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_basic2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_bytes_utf8` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_default_in_treeless_mode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_dont_expand1_lists_with_multiple_items` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_dont_expand1_lists_with_multiple_items_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_dynamic_lexer_prioritization` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_empty` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_empty_end` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_empty_expand1_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_empty_expand1_list_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_empty_flatten_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_error_with_interactive_parser` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_escaped_string` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_expand1_lists_with_one_item` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_expand1_lists_with_one_item_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_float_without_lexer` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_g_regex_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_hex_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_hex_literal_range_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_ignore` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_import_errors` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_interactive_treeless_transformer` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_iter_parse` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_join_regex_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_keep_all_tokens` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_lexer_detect_newline_tokens` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_lexer_prioritization` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_line_and_column` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_line_counting` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_match_examples` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_maybe` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_maybe_placeholders` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_meddling_unused` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_multi_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_multi_start` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_on_error_without_lalr` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_parse_textslice` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_parse_textslice_fails` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_parser_interactive_parser` | integration | Error Semantics + Advanced Public APIs + Parser Methods | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_postlex_declare` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_postlex_indenter` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_prioritization` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_prioritization_sum` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_priority_vs_embedded` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_ranged_repeat_rules` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_reduce_cycle` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_regex_escaping` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_regex_quote` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_regex_width_fallback` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestEarleyDynamic_complete::test_relative_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_relative_import_of_nested_grammar` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_relative_import_preserves_leading_underscore` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_relative_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_relative_import_rules_dependencies_imported_only_once` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_relative_import_unicode` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_relative_multi_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_relative_rule_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_relative_rule_import_drop_ignore` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_relative_rule_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_relative_rule_import_subrule` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_relative_rule_import_subrule_no_conflict` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_rule_collision` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_rule_collision2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_serialize` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_serialize_with_transformer` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_special_chars` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_stack_for_ebnf` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_start` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_strict` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_stringio_unicode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_templates` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_templates_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_templates_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_templates_modifiers` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_templates_recursion` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_templates_templates` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_token_collision` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_token_collision2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_token_collision_WS` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_token_ebnf` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_token_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_token_flags2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_token_flags3` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_token_flags_collision` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_token_flags_verbose` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_token_flags_verbose_multiline` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_token_not_anon` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_twice_empty` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_unicode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_unicode2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_unicode3` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_unicode4` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_unicode_class` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestEarleyDynamic_complete::test_unicode_literal_range_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_unicode_literal_range_escape2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestEarleyDynamic_complete::test_unicode_word` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestEarleyDynamic_complete::test_utf8` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrContextual::test_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_backslash` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_backslash2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_basic1` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_basic2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_bytes_utf8` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrContextual::test_default_in_treeless_mode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_dont_expand1_lists_with_multiple_items` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_dont_expand1_lists_with_multiple_items_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_dynamic_lexer_prioritization` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_empty` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_empty_end` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_empty_expand1_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_empty_expand1_list_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_empty_flatten_list` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_error_with_interactive_parser` | integration | Error Semantics + Advanced Public APIs + Parser Methods | covered |  |
| `tests/__main__.py::TestLalrContextual::test_escaped_string` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_expand1_lists_with_one_item` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_expand1_lists_with_one_item_2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_float_without_lexer` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_g_regex_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_hex_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_hex_literal_range_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_ignore` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_import_errors` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_interactive_treeless_transformer` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestLalrContextual::test_iter_parse` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestLalrContextual::test_join_regex_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_keep_all_tokens` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_lexer_detect_newline_tokens` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_lexer_prioritization` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_line_and_column` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrContextual::test_line_counting` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrContextual::test_match_examples` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestLalrContextual::test_maybe` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_maybe_placeholders` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_meddling_unused` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_multi_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_multi_start` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_on_error_without_lalr` | integration | Error Semantics + Advanced Public APIs | covered |  |
| `tests/__main__.py::TestLalrContextual::test_parse_textslice` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrContextual::test_parse_textslice_fails` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrContextual::test_parser_interactive_parser` | integration | Error Semantics + Advanced Public APIs + Parser Methods | covered |  |
| `tests/__main__.py::TestLalrContextual::test_postlex_declare` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_postlex_indenter` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_prioritization` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_prioritization_sum` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_priority_vs_embedded` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_ranged_repeat_rules` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_reduce_cycle` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_regex_escaping` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_regex_quote` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_regex_width_fallback` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestLalrContextual::test_relative_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_relative_import_of_nested_grammar` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_relative_import_preserves_leading_underscore` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_relative_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_relative_import_rules_dependencies_imported_only_once` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_relative_import_unicode` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_relative_multi_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_relative_rule_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_relative_rule_import_drop_ignore` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_relative_rule_import_rename` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_relative_rule_import_subrule` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_relative_rule_import_subrule_no_conflict` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_rule_collision` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_rule_collision2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_serialize` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_serialize_with_transformer` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_special_chars` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_stack_for_ebnf` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_start` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_strict` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_stringio_unicode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_templates` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_templates_alias` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_templates_import` | system_e2e | Public API + Advanced Public APIs + Cross-View Invariants | covered |  |
| `tests/__main__.py::TestLalrContextual::test_templates_modifiers` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_templates_recursion` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_templates_templates` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_token_collision` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_token_collision2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_token_collision_WS` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_token_ebnf` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_token_flags` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_token_flags2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_token_flags3` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_token_flags_collision` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_token_flags_verbose` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_token_flags_verbose_multiline` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrContextual::test_token_not_anon` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_twice_empty` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_unicode` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_unicode2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_unicode3` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_unicode4` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_unicode_class` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestLalrContextual::test_unicode_literal_range_escape` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_unicode_literal_range_escape2` | atomic | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestLalrContextual::test_unicode_word` | atomic | - | excluded | depends on optional regex/interegular dependency unavailable in baseline environment |
| `tests/__main__.py::TestLalrContextual::test_utf8` | integration | Tree and Token Model + Parsing and Lexing Behavior | covered |  |
| `tests/__main__.py::TestLalrCustom_new::test_alias` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_backslash` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_backslash2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_basic1` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_basic2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_bytes_utf8` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_default_in_treeless_mode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_dont_expand1_lists_with_multiple_items` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_dont_expand1_lists_with_multiple_items_2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_dynamic_lexer_prioritization` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_empty` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_empty_end` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_empty_expand1_list` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_empty_expand1_list_2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_empty_flatten_list` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_error_with_interactive_parser` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_escaped_string` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_expand1_lists_with_one_item` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_expand1_lists_with_one_item_2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_float_without_lexer` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_g_regex_flags` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_hex_escape` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_hex_literal_range_escape` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_ignore` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_import_errors` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_import_rename` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_interactive_treeless_transformer` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_iter_parse` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_join_regex_flags` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_keep_all_tokens` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_lexer_detect_newline_tokens` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_lexer_prioritization` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_line_and_column` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_line_counting` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_match_examples` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_maybe` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_maybe_placeholders` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_meddling_unused` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_multi_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_multi_start` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_on_error_without_lalr` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_parse_textslice` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_parse_textslice_fails` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_parser_interactive_parser` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_postlex_declare` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_postlex_indenter` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_prioritization` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_prioritization_sum` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_priority_vs_embedded` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_ranged_repeat_rules` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_reduce_cycle` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_regex_escaping` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_regex_quote` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_regex_width_fallback` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_relative_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_relative_import_of_nested_grammar` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_relative_import_preserves_leading_underscore` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_relative_import_rename` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_relative_import_rules_dependencies_imported_only_once` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_relative_import_unicode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_relative_multi_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_relative_rule_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_relative_rule_import_drop_ignore` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_relative_rule_import_rename` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_relative_rule_import_subrule` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_relative_rule_import_subrule_no_conflict` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_rule_collision` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_rule_collision2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_serialize` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_serialize_with_transformer` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_special_chars` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_stack_for_ebnf` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_start` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_strict` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_stringio_unicode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_templates` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_templates_alias` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_templates_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_templates_modifiers` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_templates_recursion` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_templates_templates` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_token_collision` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_token_collision2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_token_collision_WS` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_token_ebnf` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_token_flags` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_token_flags2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_token_flags3` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_token_flags_collision` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_token_flags_verbose` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_token_flags_verbose_multiline` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_token_not_anon` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_twice_empty` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_unicode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_unicode2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_unicode3` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_unicode4` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_unicode_class` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_unicode_literal_range_escape` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_unicode_literal_range_escape2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_unicode_word` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestLalrCustom_new::test_utf8` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_alias` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_backslash` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_backslash2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_basic1` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_basic2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_bytes_utf8` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_default_in_treeless_mode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_dont_expand1_lists_with_multiple_items` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_dont_expand1_lists_with_multiple_items_2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_dynamic_lexer_prioritization` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_empty` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_empty_end` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_empty_expand1_list` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_empty_expand1_list_2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_empty_flatten_list` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_error_with_interactive_parser` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_escaped_string` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_expand1_lists_with_one_item` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_expand1_lists_with_one_item_2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_float_without_lexer` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_g_regex_flags` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_hex_escape` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_hex_literal_range_escape` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_ignore` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_import_errors` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_import_rename` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_interactive_treeless_transformer` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_iter_parse` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_join_regex_flags` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_keep_all_tokens` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_lexer_detect_newline_tokens` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_lexer_prioritization` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_line_and_column` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_line_counting` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_match_examples` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_maybe` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_maybe_placeholders` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_meddling_unused` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_multi_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_multi_start` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_on_error_without_lalr` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_parse_textslice` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_parse_textslice_fails` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_parser_interactive_parser` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_postlex_declare` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_postlex_indenter` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_prioritization` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_prioritization_sum` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_priority_vs_embedded` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_ranged_repeat_rules` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_reduce_cycle` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_regex_escaping` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_regex_quote` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_regex_width_fallback` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_relative_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_relative_import_of_nested_grammar` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_relative_import_preserves_leading_underscore` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_relative_import_rename` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_relative_import_rules_dependencies_imported_only_once` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_relative_import_unicode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_relative_multi_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_relative_rule_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_relative_rule_import_drop_ignore` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_relative_rule_import_rename` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_relative_rule_import_subrule` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_relative_rule_import_subrule_no_conflict` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_rule_collision` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_rule_collision2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_serialize` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_serialize_with_transformer` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_special_chars` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_stack_for_ebnf` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_start` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_strict` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_stringio_unicode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_templates` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_templates_alias` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_templates_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_templates_modifiers` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_templates_recursion` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_templates_templates` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_token_collision` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_token_collision2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_token_collision_WS` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_token_ebnf` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_token_flags` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_token_flags2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_token_flags3` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_token_flags_collision` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_token_flags_verbose` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_token_flags_verbose_multiline` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_token_not_anon` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_twice_empty` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_unicode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_unicode2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_unicode3` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_unicode4` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_unicode_class` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_unicode_literal_range_escape` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_unicode_literal_range_escape2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_unicode_word` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestCykCustom_new::test_utf8` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_alias` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_backslash` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_backslash2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_basic1` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_basic2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_bytes_utf8` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_default_in_treeless_mode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_dont_expand1_lists_with_multiple_items` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_dont_expand1_lists_with_multiple_items_2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_dynamic_lexer_prioritization` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_empty` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_empty_end` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_empty_expand1_list` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_empty_expand1_list_2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_empty_flatten_list` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_error_with_interactive_parser` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_escaped_string` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_expand1_lists_with_one_item` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_expand1_lists_with_one_item_2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_float_without_lexer` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_g_regex_flags` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_hex_escape` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_hex_literal_range_escape` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_ignore` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_import_errors` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_import_rename` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_interactive_treeless_transformer` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_iter_parse` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_join_regex_flags` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_keep_all_tokens` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_lexer_detect_newline_tokens` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_lexer_prioritization` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_line_and_column` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_line_counting` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_match_examples` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_maybe` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_maybe_placeholders` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_meddling_unused` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_multi_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_multi_start` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_on_error_without_lalr` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_parse_textslice` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_parse_textslice_fails` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_parser_interactive_parser` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_postlex_declare` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_postlex_indenter` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_prioritization` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_prioritization_sum` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_priority_vs_embedded` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_ranged_repeat_rules` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_reduce_cycle` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_regex_escaping` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_regex_quote` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_regex_width_fallback` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_relative_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_relative_import_of_nested_grammar` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_relative_import_preserves_leading_underscore` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_relative_import_rename` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_relative_import_rules_dependencies_imported_only_once` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_relative_import_unicode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_relative_multi_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_relative_rule_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_relative_rule_import_drop_ignore` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_relative_rule_import_rename` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_relative_rule_import_subrule` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_relative_rule_import_subrule_no_conflict` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_rule_collision` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_rule_collision2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_serialize` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_serialize_with_transformer` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_special_chars` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_stack_for_ebnf` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_start` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_strict` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_stringio_unicode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_templates` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_templates_alias` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_templates_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_templates_modifiers` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_templates_recursion` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_templates_templates` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_token_collision` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_token_collision2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_token_collision_WS` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_token_ebnf` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_token_flags` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_token_flags2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_token_flags3` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_token_flags_collision` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_token_flags_verbose` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_token_flags_verbose_multiline` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_token_not_anon` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_twice_empty` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_unicode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_unicode2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_unicode3` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_unicode4` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_unicode_class` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_unicode_literal_range_escape` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_unicode_literal_range_escape2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_unicode_word` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old0::test_utf8` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_alias` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_backslash` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_backslash2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_basic1` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_basic2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_bytes_utf8` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_default_in_treeless_mode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_dont_expand1_lists_with_multiple_items` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_dont_expand1_lists_with_multiple_items_2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_dynamic_lexer_prioritization` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_empty` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_empty_end` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_empty_expand1_list` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_empty_expand1_list_2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_empty_flatten_list` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_error_with_interactive_parser` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_escaped_string` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_expand1_lists_with_one_item` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_expand1_lists_with_one_item_2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_float_without_lexer` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_g_regex_flags` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_hex_escape` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_hex_literal_range_escape` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_ignore` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_import_errors` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_import_rename` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_interactive_treeless_transformer` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_iter_parse` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_join_regex_flags` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_keep_all_tokens` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_lexer_detect_newline_tokens` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_lexer_prioritization` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_line_and_column` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_line_counting` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_match_examples` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_maybe` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_maybe_placeholders` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_meddling_unused` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_multi_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_multi_start` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_on_error_without_lalr` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_parse_textslice` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_parse_textslice_fails` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_parser_interactive_parser` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_postlex_declare` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_postlex_indenter` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_prioritization` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_prioritization_sum` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_priority_vs_embedded` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_ranged_repeat_rules` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_reduce_cycle` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_regex_escaping` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_regex_quote` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_regex_width_fallback` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_relative_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_relative_import_of_nested_grammar` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_relative_import_preserves_leading_underscore` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_relative_import_rename` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_relative_import_rules_dependencies_imported_only_once` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_relative_import_unicode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_relative_multi_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_relative_rule_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_relative_rule_import_drop_ignore` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_relative_rule_import_rename` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_relative_rule_import_subrule` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_relative_rule_import_subrule_no_conflict` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_rule_collision` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_rule_collision2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_serialize` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_serialize_with_transformer` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_special_chars` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_stack_for_ebnf` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_start` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_strict` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_stringio_unicode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_templates` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_templates_alias` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_templates_import` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_templates_modifiers` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_templates_recursion` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_templates_templates` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_token_collision` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_token_collision2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_token_collision_WS` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_token_ebnf` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_token_flags` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_token_flags2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_token_flags3` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_token_flags_collision` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_token_flags_verbose` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_token_flags_verbose_multiline` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_token_not_anon` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_twice_empty` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_unicode` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_unicode2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_unicode3` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_unicode4` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_unicode_class` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_unicode_literal_range_escape` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_unicode_literal_range_escape2` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_unicode_word` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestEarleyCustom_old1::test_utf8` | integration | - | source-only | uses custom lexer compatibility protocol not specified as public contract |
| `tests/__main__.py::TestFullEarleyBasic::test_ambiguity1` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_ambiguity2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_ambiguous_ignores` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_ambiguous_inlined_rule` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_ambiguous_intermediate_node` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_ambiguous_intermediate_node_conditionally_inlined_rule` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_ambiguous_intermediate_node_inlined_rule` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_ambiguous_intermediate_node_unnamed_token` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_ambiguous_symbol_and_intermediate_nodes` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_anon` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_consistent_derivation_order1` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_cycle` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_cycle2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_cycles` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_cycles_with_child_filter` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_earley` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_earley2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_earley3` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_earley4` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_earley_explicit_ambiguity` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_earley_repeating_empty` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_explicit_ambiguity2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_fruitflies_ambig` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_ignore_carryover_with_priority` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_many_cycles` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_multiple_start_solutions` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_multiple_start_solutions2` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_nested_ambiguous_intermediate_nodes` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_nested_ambiguous_intermediate_nodes2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_resolve_ambiguity_with_shared_node` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_resolve_ambiguity_with_shared_node2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_symbol_node_start_end_dynamic_lexer` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyBasic::test_term_ambig_resolve` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_ambiguity1` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_ambiguity2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_ambiguous_ignores` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_ambiguous_inlined_rule` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_ambiguous_intermediate_node` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_ambiguous_intermediate_node_conditionally_inlined_rule` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_ambiguous_intermediate_node_inlined_rule` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_ambiguous_intermediate_node_unnamed_token` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_ambiguous_symbol_and_intermediate_nodes` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_anon` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_consistent_derivation_order1` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_cycle` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_cycle2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_cycles` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_cycles_with_child_filter` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_earley` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_earley2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_earley3` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_earley4` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_earley_explicit_ambiguity` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_earley_repeating_empty` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_explicit_ambiguity2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_fruitflies_ambig` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_ignore_carryover_with_priority` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_many_cycles` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_multiple_start_solutions` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_multiple_start_solutions2` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_nested_ambiguous_intermediate_nodes` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_nested_ambiguous_intermediate_nodes2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_resolve_ambiguity_with_shared_node` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_resolve_ambiguity_with_shared_node2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_symbol_node_start_end_dynamic_lexer` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic::test_term_ambig_resolve` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_ambiguity1` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_ambiguity2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_ambiguous_ignores` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_ambiguous_inlined_rule` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_ambiguous_intermediate_node` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_ambiguous_intermediate_node_conditionally_inlined_rule` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_ambiguous_intermediate_node_inlined_rule` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_ambiguous_intermediate_node_unnamed_token` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_ambiguous_symbol_and_intermediate_nodes` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_anon` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_consistent_derivation_order1` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_cycle` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_cycle2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_cycles` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_cycles_with_child_filter` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_earley` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_earley2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_earley3` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_earley4` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_earley_explicit_ambiguity` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_earley_repeating_empty` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_explicit_ambiguity2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_fruitflies_ambig` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_ignore_carryover_with_priority` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_many_cycles` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_multiple_start_solutions` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction + `Lark(grammar, **options)` + Public Helper Classes and Grammar Utilities | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_multiple_start_solutions2` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction + `Lark(grammar, **options)` + Public Helper Classes and Grammar Utilities | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_nested_ambiguous_intermediate_nodes` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_nested_ambiguous_intermediate_nodes2` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_resolve_ambiguity_with_shared_node` | integration | Parsing and Lexing Behavior + Tree Construction | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_resolve_ambiguity_with_shared_node2` | integration | Parsing and Lexing Behavior + Tree Construction + Representative Workflows | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_symbol_node_start_end_dynamic_lexer` | integration | Parsing and Lexing Behavior + Tree Construction + Representative Workflows | covered |  |
| `tests/__main__.py::TestFullEarleyDynamic_complete::test_term_ambig_resolve` | system_e2e | Grammar Language + Parsing and Lexing Behavior + Tree Construction + `Lark(grammar, **options)` + Public Helper Classes and Grammar Utilities + Representative Workflows | covered |  |
| `tests/__main__.py::TestPatternMatching::test_match_on_tree` | atomic | Tree and Token Model | covered |  |
| `tests/__main__.py::TestPatternMatching::test_matches_with_bad_token_type` | atomic | Tree and Token Model | covered |  |
| `tests/__main__.py::TestPatternMatching::test_matches_with_str_positional_arg` | atomic | Tree and Token Model | covered |  |
| `tests/__main__.py::TestPatternMatching::test_matches_with_string` | atomic | Tree and Token Model | covered |  |
| `tests/__main__.py::TestPatternMatching::test_matches_with_token_kwarg_type` | atomic | Tree and Token Model | covered |  |
| `tests/__main__.py::TestPatternMatching::test_matches_with_token_positional_arg` | atomic | Tree and Token Model | covered |  |

Total: 1273 | kept (covered): 792 | spec_gap: 0 | source-only: 422 | excluded: 59 | final scoreable: 792
