# Spec Test Map: prompt-toolkit-fullrepro-001

filter/oracle_source: upstream_plus_generated
upstream_collected: 156
upstream_covered: 68
generated_covered: 32
final_scoreable: 100

## Section Coverage

| spec_section | covered_count |
|---|---:|
| Application, Prompt, and I/O | 3 |
| Completion | 18 |
| Cross-View Invariants | 5 |
| Document and Buffer | 13 |
| Error Semantics | 8 |
| Formatted Text | 16 |
| Formatted Text and Styles | 3 |
| Full-Screen Layout With a Buffer and Exit Binding | 3 |
| Installable Surface | 3 |
| Key Bindings | 6 |
| Layout Controls | 3 |
| Product State Model | 5 |
| Prompt With Completion and Validation | 3 |
| Styles | 7 |
| Validation | 4 |

Non-behavior documentation headings (`Product Overview`, `Scope`, `Non-Goals`, `Evaluation Notes`) are reviewed for traceability but are not assigned executable oracle quotas.

## Map

| test_nodeid | source | layer | spec_section | status | notes |
|---|---|---|---|---|---|
| `tests/test_async_generator.py::test_generator_to_async_generator` | upstream | atomic | - | source-only | eventloop async-generator helpers are outside the candidate spec scope |
| `tests/test_buffer.py::test_initial` | upstream | integration | Product State Model | covered | buffer state reflected through document projection |
| `tests/test_buffer.py::test_insert_text` | upstream | integration | Product State Model | covered | buffer state reflected through document projection |
| `tests/test_buffer.py::test_cursor_movement` | upstream | integration | Product State Model | covered | buffer state reflected through document projection |
| `tests/test_buffer.py::test_backspace` | upstream | atomic | Document and Buffer | covered | public buffer editing and cursor behavior |
| `tests/test_buffer.py::test_cursor_up` | upstream | atomic | Document and Buffer | covered | public buffer editing and cursor behavior |
| `tests/test_buffer.py::test_cursor_down` | upstream | atomic | Document and Buffer | covered | public buffer editing and cursor behavior |
| `tests/test_buffer.py::test_join_next_line` | upstream | atomic | Cross-View Invariants | covered | buffer text/cursor/document agreement after edit operation |
| `tests/test_buffer.py::test_newline` | upstream | atomic | Cross-View Invariants | covered | buffer text/cursor/document agreement after edit operation |
| `tests/test_buffer.py::test_swap_characters_before_cursor` | upstream | atomic | Cross-View Invariants | covered | buffer text/cursor/document agreement after edit operation |
| `tests/test_cli.py::test_simple_text_input` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_cursor_movements` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_kill_multiple_words_and_paste` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_interrupts` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_yank` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_quoted_insert` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_transformations` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_other_bindings` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_controlx_controlx` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_history_bindings` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_reverse_search` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_arguments` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_arguments_for_all_commands` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_kill_ring` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_selection` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_insert_comment` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_record_macro` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_emacs_nested_macro` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_prefix_meta` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_bracketed_paste` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_cursor_movements` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_operators` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_text_objects` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_digraphs` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_block_editing` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_block_editing_empty_lines` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_visual_line_copy` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_visual_empty_line` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_character_delete_after_cursor` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_character_delete_before_cursor` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_character_paste` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_temp_navigation_mode` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_vi_macros` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_cli.py::test_accept_default` | upstream | atomic | - | excluded | module-level imports terminal parser/named-command helpers and asserts exact key-sequence terminal behavior; public PromptSession coverage is generated separately |
| `tests/test_completion.py::test_pathcompleter_completes_in_current_directory` | upstream | integration | Completion | covered | PathCompleter public filesystem completion behavior |
| `tests/test_completion.py::test_pathcompleter_completes_files_in_current_directory` | upstream | integration | Completion | covered | PathCompleter public filesystem completion behavior |
| `tests/test_completion.py::test_pathcompleter_completes_files_in_absolute_directory` | upstream | integration | Completion | covered | PathCompleter public filesystem completion behavior |
| `tests/test_completion.py::test_pathcompleter_completes_directories_with_only_directories` | upstream | integration | Completion | covered | PathCompleter public filesystem completion behavior |
| `tests/test_completion.py::test_pathcompleter_respects_completions_under_min_input_len` | upstream | integration | Completion | covered | PathCompleter public filesystem completion behavior |
| `tests/test_completion.py::test_pathcompleter_does_not_expanduser_by_default` | upstream | integration | Completion | covered | PathCompleter public filesystem completion behavior |
| `tests/test_completion.py::test_pathcompleter_can_expanduser` | upstream | integration | Completion | covered | PathCompleter public filesystem completion behavior |
| `tests/test_completion.py::test_pathcompleter_can_apply_file_filter` | upstream | integration | Completion | covered | PathCompleter public filesystem completion behavior |
| `tests/test_completion.py::test_pathcompleter_get_paths_constrains_path` | upstream | integration | Completion | covered | PathCompleter public filesystem completion behavior |
| `tests/test_completion.py::test_word_completer_static_word_list` | upstream | atomic | Completion | covered | WordCompleter public completion behavior |
| `tests/test_completion.py::test_word_completer_ignore_case` | upstream | atomic | Completion | covered | WordCompleter public completion behavior |
| `tests/test_completion.py::test_word_completer_match_middle` | upstream | atomic | Completion | covered | WordCompleter public completion behavior |
| `tests/test_completion.py::test_word_completer_sentence` | upstream | atomic | Completion | covered | WordCompleter public completion behavior |
| `tests/test_completion.py::test_word_completer_dynamic_word_list` | upstream | atomic | Completion | covered | WordCompleter public completion behavior |
| `tests/test_completion.py::test_word_completer_pattern` | upstream | atomic | Completion | covered | WordCompleter public completion behavior |
| `tests/test_completion.py::test_fuzzy_completer` | upstream | integration | Completion | covered | completer wrapper/delegation behavior |
| `tests/test_completion.py::test_nested_completer` | upstream | integration | Completion | covered | completer wrapper/delegation behavior |
| `tests/test_completion.py::test_deduplicate_completer` | upstream | integration | Completion | covered | completer wrapper/delegation behavior |
| `tests/test_document.py::test_current_char` | upstream | atomic | Document and Buffer | covered | document public text/line/word projection behavior |
| `tests/test_document.py::test_text_before_cursor` | upstream | atomic | Document and Buffer | covered | document public text/line/word projection behavior |
| `tests/test_document.py::test_text_after_cursor` | upstream | atomic | Document and Buffer | covered | document public text/line/word projection behavior |
| `tests/test_document.py::test_lines` | upstream | atomic | Document and Buffer | covered | document public text/line/word projection behavior |
| `tests/test_document.py::test_line_count` | upstream | atomic | Document and Buffer | covered | document public text/line/word projection behavior |
| `tests/test_document.py::test_current_line_before_cursor` | upstream | atomic | Document and Buffer | covered | document public text/line/word projection behavior |
| `tests/test_document.py::test_current_line_after_cursor` | upstream | atomic | Document and Buffer | covered | document public text/line/word projection behavior |
| `tests/test_document.py::test_current_line` | upstream | atomic | Document and Buffer | covered | document public text/line/word projection behavior |
| `tests/test_document.py::test_cursor_position` | upstream | atomic | Product State Model | covered | document cursor projection behavior |
| `tests/test_document.py::test_translate_index_to_position` | upstream | atomic | Product State Model | covered | document cursor projection behavior |
| `tests/test_document.py::test_is_cursor_at_the_end` | upstream | atomic | Document and Buffer | covered | document public text/line/word projection behavior |
| `tests/test_document.py::test_get_word_before_cursor_with_whitespace_and_pattern` | upstream | atomic | Document and Buffer | covered | document public text/line/word projection behavior |
| `tests/test_filter.py::test_never` | upstream | atomic | - | excluded | module-level private imports _AndList/_OrList create cleanroom collection risk |
| `tests/test_filter.py::test_always` | upstream | atomic | - | excluded | module-level private imports _AndList/_OrList create cleanroom collection risk |
| `tests/test_filter.py::test_invert` | upstream | atomic | - | excluded | module-level private imports _AndList/_OrList create cleanroom collection risk |
| `tests/test_filter.py::test_or` | upstream | atomic | - | excluded | module-level private imports _AndList/_OrList create cleanroom collection risk |
| `tests/test_filter.py::test_and` | upstream | atomic | - | excluded | module-level private imports _AndList/_OrList create cleanroom collection risk |
| `tests/test_filter.py::test_nested_and` | upstream | atomic | - | excluded | module-level private imports _AndList/_OrList create cleanroom collection risk |
| `tests/test_filter.py::test_nested_or` | upstream | atomic | - | excluded | module-level private imports _AndList/_OrList create cleanroom collection risk |
| `tests/test_filter.py::test_to_filter` | upstream | atomic | - | excluded | module-level private imports _AndList/_OrList create cleanroom collection risk |
| `tests/test_filter.py::test_filter_cache_regression_1` | upstream | atomic | - | excluded | module-level private imports _AndList/_OrList create cleanroom collection risk |
| `tests/test_filter.py::test_filter_cache_regression_2` | upstream | atomic | - | excluded | module-level private imports _AndList/_OrList create cleanroom collection risk |
| `tests/test_filter.py::test_filter_remove_duplicates` | upstream | atomic | - | excluded | module-level private imports _AndList/_OrList create cleanroom collection risk |
| `tests/test_formatted_text.py::test_basic_html` | upstream | atomic | Formatted Text | covered | HTML formatted-text conversion behavior |
| `tests/test_formatted_text.py::test_html_with_fg_bg` | upstream | atomic | Formatted Text | covered | HTML formatted-text conversion behavior |
| `tests/test_formatted_text.py::test_ansi_formatting` | upstream | atomic | Formatted Text | covered | ANSI formatted-text conversion behavior |
| `tests/test_formatted_text.py::test_ansi_dim` | upstream | atomic | Formatted Text | covered | ANSI formatted-text conversion behavior |
| `tests/test_formatted_text.py::test_ansi_256_color` | upstream | atomic | Formatted Text | covered | ANSI formatted-text conversion behavior |
| `tests/test_formatted_text.py::test_ansi_true_color` | upstream | atomic | Formatted Text | covered | ANSI formatted-text conversion behavior |
| `tests/test_formatted_text.py::test_ansi_interpolation` | upstream | atomic | Formatted Text | covered | ANSI formatted-text conversion behavior |
| `tests/test_formatted_text.py::test_interpolation` | upstream | integration | Formatted Text | covered | formatted-text wrapper/interpolation behavior |
| `tests/test_formatted_text.py::test_html_interpolation` | upstream | atomic | Formatted Text | covered | HTML formatted-text conversion behavior |
| `tests/test_formatted_text.py::test_merge_formatted_text` | upstream | integration | Formatted Text | covered | formatted-text wrapper/interpolation behavior |
| `tests/test_formatted_text.py::test_pygments_tokens` | upstream | integration | Formatted Text | covered | formatted-text wrapper/interpolation behavior |
| `tests/test_formatted_text.py::test_split_lines` | upstream | atomic | Formatted Text | covered | formatted fragment utility behavior |
| `tests/test_formatted_text.py::test_split_lines_2` | upstream | atomic | Formatted Text | covered | formatted fragment utility behavior |
| `tests/test_formatted_text.py::test_split_lines_3` | upstream | atomic | Formatted Text | covered | formatted fragment utility behavior |
| `tests/test_formatted_text.py::test_split_lines_4` | upstream | atomic | Formatted Text | covered | formatted fragment utility behavior |
| `tests/test_history.py::test_in_memory_history` | upstream | atomic | - | source-only | history classes and threaded history behavior are outside the narrowed spec scope |
| `tests/test_history.py::test_file_history` | upstream | atomic | - | source-only | history classes and threaded history behavior are outside the narrowed spec scope |
| `tests/test_history.py::test_threaded_file_history` | upstream | atomic | - | source-only | history classes and threaded history behavior are outside the narrowed spec scope |
| `tests/test_history.py::test_threaded_in_memory_history` | upstream | atomic | - | source-only | history classes and threaded history behavior are outside the narrowed spec scope |
| `tests/test_inputstream.py::test_control_keys` | upstream | atomic | - | excluded | terminal parser internals and VT100 sequence exactness are non-goals |
| `tests/test_inputstream.py::test_arrows` | upstream | atomic | - | excluded | terminal parser internals and VT100 sequence exactness are non-goals |
| `tests/test_inputstream.py::test_escape` | upstream | atomic | - | excluded | terminal parser internals and VT100 sequence exactness are non-goals |
| `tests/test_inputstream.py::test_special_double_keys` | upstream | atomic | - | excluded | terminal parser internals and VT100 sequence exactness are non-goals |
| `tests/test_inputstream.py::test_flush_1` | upstream | atomic | - | excluded | terminal parser internals and VT100 sequence exactness are non-goals |
| `tests/test_inputstream.py::test_flush_2` | upstream | atomic | - | excluded | terminal parser internals and VT100 sequence exactness are non-goals |
| `tests/test_inputstream.py::test_meta_arrows` | upstream | atomic | - | excluded | terminal parser internals and VT100 sequence exactness are non-goals |
| `tests/test_inputstream.py::test_control_square_close` | upstream | atomic | - | excluded | terminal parser internals and VT100 sequence exactness are non-goals |
| `tests/test_inputstream.py::test_invalid` | upstream | atomic | - | excluded | terminal parser internals and VT100 sequence exactness are non-goals |
| `tests/test_inputstream.py::test_cpr_response` | upstream | atomic | - | excluded | terminal parser internals and VT100 sequence exactness are non-goals |
| `tests/test_inputstream.py::test_cpr_response_2` | upstream | atomic | - | excluded | terminal parser internals and VT100 sequence exactness are non-goals |
| `tests/test_key_binding.py::test_remove_bindings` | upstream | atomic | Key Bindings | covered | KeyBindings registration/removal behavior |
| `tests/test_key_binding.py::test_feed_simple` | upstream | integration | Key Bindings | covered | KeyProcessor dispatches public KeyPress sequences through KeyBindings |
| `tests/test_key_binding.py::test_feed_several` | upstream | integration | Key Bindings | covered | KeyProcessor dispatches public KeyPress sequences through KeyBindings |
| `tests/test_key_binding.py::test_control_square_closed_any` | upstream | atomic | Key Bindings | covered | KeyBindings registration/removal behavior |
| `tests/test_key_binding.py::test_common_prefix` | upstream | integration | Key Bindings | covered | KeyProcessor dispatches public KeyPress sequences through KeyBindings |
| `tests/test_key_binding.py::test_previous_key_sequence` | upstream | integration | Key Bindings | covered | KeyProcessor dispatches public KeyPress sequences through KeyBindings |
| `tests/test_layout.py::test_layout_class` | upstream | integration | Layout Controls | covered | layout focus tracks windows and controls |
| `tests/test_layout.py::test_create_invalid_layout` | upstream | atomic | Error Semantics | covered | Layout raises InvalidLayoutError for no focusable control |
| `tests/test_memory_leaks.py::test_prompt_session_memory_leak` | upstream | atomic | - | source-only | GC/memory lifetime behavior is outside the public behavioral contract |
| `tests/test_print_formatted_text.py::test_print_formatted_text` | upstream | atomic | - | source-only | asserts terminal escape output and platform skip helper behavior excluded by non-goals |
| `tests/test_print_formatted_text.py::test_print_formatted_text_backslash_r` | upstream | atomic | - | source-only | asserts terminal escape output and platform skip helper behavior excluded by non-goals |
| `tests/test_print_formatted_text.py::test_formatted_text_with_style` | upstream | atomic | - | source-only | asserts terminal escape output and platform skip helper behavior excluded by non-goals |
| `tests/test_print_formatted_text.py::test_html_with_style` | upstream | atomic | - | source-only | asserts terminal escape output and platform skip helper behavior excluded by non-goals |
| `tests/test_print_formatted_text.py::test_print_formatted_text_with_dim` | upstream | atomic | - | source-only | asserts terminal escape output and platform skip helper behavior excluded by non-goals |
| `tests/test_regular_languages.py::test_simple_match` | upstream | atomic | - | source-only | contrib regular language APIs are outside the narrowed spec scope |
| `tests/test_regular_languages.py::test_variable_varname` | upstream | atomic | - | source-only | contrib regular language APIs are outside the narrowed spec scope |
| `tests/test_regular_languages.py::test_prefix` | upstream | atomic | - | source-only | contrib regular language APIs are outside the narrowed spec scope |
| `tests/test_regular_languages.py::test_completer` | upstream | atomic | - | source-only | contrib regular language APIs are outside the narrowed spec scope |
| `tests/test_shortcuts.py::test_split_multiline_prompt` | upstream | atomic | - | excluded | private _split_multiline_prompt and widget visual/print-container behavior are outside scope |
| `tests/test_shortcuts.py::test_print_container` | upstream | atomic | - | excluded | private _split_multiline_prompt and widget visual/print-container behavior are outside scope |
| `tests/test_style.py::test_style_from_dict` | upstream | atomic | Styles | covered | Style rule/class resolution behavior |
| `tests/test_style.py::test_class_combinations_1` | upstream | atomic | Styles | covered | Style rule/class resolution behavior |
| `tests/test_style.py::test_class_combinations_2` | upstream | atomic | Styles | covered | Style rule/class resolution behavior |
| `tests/test_style.py::test_substyles` | upstream | atomic | Styles | covered | Style rule/class resolution behavior |
| `tests/test_style.py::test_swap_light_and_dark_style_transformation` | upstream | atomic | Styles | covered | style transformation public attrs behavior |
| `tests/test_style_transformation.py::test_adjust_brightness_style_transformation` | upstream | atomic | Styles | covered | style transformation public attrs behavior |
| `tests/test_utils.py::test_using_weights` | upstream | atomic | - | source-only | utility weighting helper is outside the covered public surface |
| `tests/test_vt100_output.py::test_get_closest_ansi_color` | upstream | atomic | - | excluded | private VT100 output helpers and color table internals are non-goals |
| `tests/test_vt100_output.py::test_256_colors` | upstream | atomic | - | excluded | private VT100 output helpers and color table internals are non-goals |
| `tests/test_widgets.py::test_default_button` | upstream | atomic | - | source-only | widget visual polish is explicitly outside scope |
| `tests/test_widgets.py::test_custom_button` | upstream | atomic | - | source-only | widget visual polish is explicitly outside scope |
| `tests/test_yank_nth_arg.py::test_empty_history` | upstream | atomic | - | source-only | history-specific yank argument behavior is not specified in the narrowed public contract |
| `tests/test_yank_nth_arg.py::test_simple_search` | upstream | atomic | - | source-only | history-specific yank argument behavior is not specified in the narrowed public contract |
| `tests/test_yank_nth_arg.py::test_simple_search_with_quotes` | upstream | atomic | - | source-only | history-specific yank argument behavior is not specified in the narrowed public contract |
| `tests/test_yank_nth_arg.py::test_simple_search_with_arg` | upstream | atomic | - | source-only | history-specific yank argument behavior is not specified in the narrowed public contract |
| `tests/test_yank_nth_arg.py::test_simple_search_with_arg_out_of_bounds` | upstream | atomic | - | source-only | history-specific yank argument behavior is not specified in the narrowed public contract |
| `tests/test_yank_nth_arg.py::test_repeated_search` | upstream | atomic | - | source-only | history-specific yank argument behavior is not specified in the narrowed public contract |
| `tests/test_yank_nth_arg.py::test_repeated_search_with_wraparound` | upstream | atomic | - | source-only | history-specific yank argument behavior is not specified in the narrowed public contract |
| `tests/test_yank_nth_arg.py::test_yank_nth_arg` | upstream | atomic | - | source-only | history-specific yank argument behavior is not specified in the narrowed public contract |
| `tests/test_yank_nth_arg.py::test_repeated_yank_nth_arg` | upstream | atomic | - | source-only | history-specific yank argument behavior is not specified in the narrowed public contract |
| `tests/test_yank_nth_arg.py::test_yank_nth_arg_with_arg` | upstream | atomic | - | source-only | history-specific yank argument behavior is not specified in the narrowed public contract |
| `filter/test_generated_public_oracle.py::test_public_import_surface_smoke` | generated | atomic | Installable Surface | covered | generated public import smoke for documented top-level surface |
| `filter/test_generated_public_oracle.py::test_public_subpackage_import_surface_smoke` | generated | atomic | Installable Surface | covered | generated public import smoke for documented subpackage surface |
| `filter/test_generated_public_oracle.py::test_top_level_shortcut_symbols_are_importable` | generated | atomic | Installable Surface | covered | generated top-level shortcut import smoke |
| `filter/test_generated_public_oracle.py::test_color_depth_public_aliases_and_invalid_env` | generated | atomic | Styles | covered | generated ColorDepth alias and environment behavior |
| `filter/test_generated_public_oracle.py::test_document_cursor_position_out_of_range_raises` | generated | atomic | Error Semantics | covered | generated public error check for Document cursor precondition |
| `filter/test_generated_public_oracle.py::test_buffer_read_only_rejects_text_edits_and_bypass_allows_document_set` | generated | integration | Error Semantics | covered | generated read-only Buffer error and bypass behavior |
| `filter/test_generated_public_oracle.py::test_buffer_validate_stores_validation_error_and_moves_cursor` | generated | integration | Validation | covered | generated Buffer/Validator validation-state agreement |
| `filter/test_generated_public_oracle.py::test_validator_from_callable_success_and_failure_positions` | generated | atomic | Validation | covered | generated Validator.from_callable behavior |
| `filter/test_generated_public_oracle.py::test_dummy_conditional_and_dynamic_validators_use_public_fallbacks` | generated | atomic | Validation | covered | generated validator wrapper fallback behavior |
| `filter/test_generated_public_oracle.py::test_dynamic_validator_delegates_to_current_validator` | generated | atomic | Validation | covered | generated DynamicValidator delegation behavior |
| `filter/test_generated_public_oracle.py::test_buffer_apply_completion_keeps_document_projection_consistent` | generated | integration | Cross-View Invariants | covered | generated Buffer/Completion/Document agreement |
| `filter/test_generated_public_oracle.py::test_completion_error_preconditions_are_enforced` | generated | atomic | Error Semantics | covered | generated completion constructor/precondition errors |
| `filter/test_generated_public_oracle.py::test_style_and_layout_error_preconditions_are_enforced` | generated | atomic | Error Semantics | covered | generated style and dimension precondition errors |
| `filter/test_generated_public_oracle.py::test_key_binding_invalid_keys_and_missing_remove_raise_value_error` | generated | atomic | Error Semantics | covered | generated key binding invalid-key and missing-handler errors |
| `filter/test_generated_public_oracle.py::test_html_attribute_validation_and_plain_text_preservation` | generated | integration | Formatted Text | covered | generated HTML error and plain-text preservation behavior |
| `filter/test_generated_public_oracle.py::test_to_formatted_text_rejects_unsupported_values` | generated | atomic | Error Semantics | covered | generated formatted-text unsupported value error |
| `filter/test_generated_public_oracle.py::test_formatted_text_control_creates_content_from_public_fragments` | generated | integration | Layout Controls | covered | generated FormattedTextControl content behavior |
| `filter/test_generated_public_oracle.py::test_layout_focus_accepts_buffer_and_keeps_control_window_agreement` | generated | system_e2e | Cross-View Invariants | covered | generated layout focus agreement across buffer/control/window views |
| `filter/test_generated_public_oracle.py::test_layout_focus_last_returns_previous_control` | generated | integration | Layout Controls | covered | generated Layout previous-focus behavior |
| `filter/test_generated_public_oracle.py::test_to_container_and_to_window_reject_unsupported_objects` | generated | atomic | Error Semantics | covered | generated layout conversion error behavior |
| `filter/test_generated_public_oracle.py::test_prompt_session_pipe_input_dummy_output_returns_buffer_text` | generated | system_e2e | Prompt With Completion and Validation | covered | generated PromptSession workflow with PipeInput, DummyOutput, completion, and validation |
| `filter/test_generated_public_oracle.py::test_prompt_session_accept_default_workflow_reuses_session` | generated | system_e2e | Prompt With Completion and Validation | covered | generated PromptSession accept_default reuse workflow |
| `filter/test_generated_public_oracle.py::test_top_level_prompt_with_pipe_input_returns_text` | generated | system_e2e | Prompt With Completion and Validation | covered | generated top-level prompt workflow with AppSession I/O |
| `filter/test_generated_public_oracle.py::test_prompt_session_custom_eof_exception_type_is_raised` | generated | system_e2e | Application, Prompt, and I/O | covered | generated PromptSession configured EOF exception behavior |
| `filter/test_generated_public_oracle.py::test_app_session_context_installs_dummy_output_defaults` | generated | integration | Application, Prompt, and I/O | covered | generated AppSession I/O context behavior |
| `filter/test_generated_public_oracle.py::test_style_lookup_does_not_change_formatted_plain_text` | generated | integration | Formatted Text and Styles | covered | generated formatted text plus style representative workflow |
| `filter/test_generated_public_oracle.py::test_template_formatted_text_style_workflow_preserves_plain_text` | generated | integration | Formatted Text and Styles | covered | generated Template/HTML/Style representative workflow |
| `filter/test_generated_public_oracle.py::test_formatted_text_style_workflow_combines_classes_and_inline_style` | generated | integration | Formatted Text and Styles | covered | generated class and inline style workflow |
| `filter/test_generated_public_oracle.py::test_full_screen_layout_workflow_objects_share_buffer` | generated | system_e2e | Full-Screen Layout With a Buffer and Exit Binding | covered | generated full-screen layout workflow object agreement |
| `filter/test_generated_public_oracle.py::test_full_screen_layout_workflow_can_focus_second_buffer` | generated | system_e2e | Full-Screen Layout With a Buffer and Exit Binding | covered | generated full-screen layout focus workflow |
| `filter/test_generated_public_oracle.py::test_full_screen_layout_workflow_includes_status_control` | generated | system_e2e | Full-Screen Layout With a Buffer and Exit Binding | covered | generated full-screen layout status control workflow |
| `filter/test_generated_public_oracle.py::test_application_default_layout_and_exit_error_semantics` | generated | atomic | Application, Prompt, and I/O | covered | generated Application default layout and exit error behavior |

Total: 156 upstream + 32 generated | kept (covered): 100 | spec_gap: 0 | source-only: 28 | excluded: 60 | final scoreable: 100
