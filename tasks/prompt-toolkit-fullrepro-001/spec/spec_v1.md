<!-- INTERNAL
task_id: prompt-toolkit-fullrepro-001
spec_version: v1
delta: Initial Stage 2 behavioral specification. Scope is limited to public, stable prompt_toolkit behavior for Document/Buffer, key bindings, completion, validation, formatted text, styles, layout controls, and application/input-output abstractions. Terminal-driver byte streams, private helpers, contrib servers, progress bars, dialogs, widgets, and exact render snapshots are excluded.
source_boundary: candidate_selection.md; source_audit.json; source_pointer.md; filter_notes.md; README.rst; pyproject.toml; docs/pages/getting_started.rst; docs/pages/asking_for_input.rst; docs/pages/printing_text.rst; docs/pages/full_screen_apps.rst; docs/pages/advanced_topics/key_bindings.rst; docs/pages/advanced_topics/styling.rst; docs/pages/advanced_topics/unit_testing.rst; examples under examples/prompts, examples/print-text, and examples/full-screen; public exports and docstrings under src/prompt_toolkit/__init__.py, application, buffer.py, completion, document.py, filters, formatted_text, input, key_binding, layout, output, shortcuts/prompt.py, styles, validation.py; public behavioral tests under tests/test_document.py, tests/test_buffer.py, tests/test_completion.py, tests/test_key_binding.py, tests/test_formatted_text.py, tests/test_style.py, tests/test_layout.py, tests/test_cli.py, tests/test_print_formatted_text.py, tests/test_filter.py, tests/test_shortcuts.py.
-->
# prompt_toolkit Specification

## Product Overview

`prompt_toolkit` is a Python library for building interactive command-line prompts and full-screen terminal applications. It provides composable data structures for editable text, completion, validation, key bindings, formatted text, styling, layouts, and application input/output abstraction.

The core design promise is that UI behavior is driven by explicit objects instead of process-wide mutable state. A program builds a `Document`, `Buffer`, `Completer`, `Validator`, `KeyBindings`, `Layout`, and `Application`, then observes results through returned text, public state objects, events, and application return values.

## Scope

This specification covers the stable public behavior for:

- editable text state through `prompt_toolkit.document.Document` and `prompt_toolkit.buffer.Buffer`
- completion through `Completion`, `Completer`, `CompleteEvent`, `WordCompleter`, `PathCompleter`, `NestedCompleter`, `FuzzyCompleter`, `FuzzyWordCompleter`, wrappers, and merge helpers
- validation through `Validator`, `ValidationError`, and validator wrappers
- key binding registration and processing through `KeyBindings`, `Binding`, `KeyProcessor`, `KeyPress`, `KeyPressEvent`, conditional/dynamic key bindings, and merged key bindings
- formatted text through `HTML`, `ANSI`, `FormattedText`, `PygmentsTokens`, `Template`, and conversion/fragment utilities
- style parsing, style lookup, style merging, color depth, and style transformations
- layout composition through `Layout`, containers, controls, dimensions, focus, and invalid-layout errors
- `Application`, `PromptSession`, `prompt`, current application/session helpers, `Input`, `PipeInput`, `DummyInput`, `Output`, `DummyOutput`, and app-session based I/O injection

## Installable Surface

The distribution name is `prompt_toolkit`. It is imported with an underscore:

```python
import prompt_toolkit
from prompt_toolkit import Application, PromptSession, prompt, choice, print_formatted_text, HTML, ANSI
```

The top-level package must expose `Application`, `prompt`, `choice`, `PromptSession`, `print_formatted_text`, `HTML`, `ANSI`, `__version__`, and `VERSION`.

The covered public import paths are:

- `prompt_toolkit.application`: `Application`, `AppSession`, `get_app_session`, `create_app_session`, `create_app_session_from_tty`, `get_app`, `get_app_or_none`, `set_app`, `DummyApplication`, `run_in_terminal`, `in_terminal`
- `prompt_toolkit.buffer`: `Buffer`, `CompletionState`, `EditReadOnlyBuffer`, `indent`, `unindent`, `reshape_text`
- `prompt_toolkit.completion`: `Completion`, `Completer`, `CompleteEvent`, `WordCompleter`, `PathCompleter`, `ExecutableCompleter`, `NestedCompleter`, `FuzzyCompleter`, `FuzzyWordCompleter`, `ThreadedCompleter`, `DummyCompleter`, `DynamicCompleter`, `ConditionalCompleter`, `DeduplicateCompleter`, `merge_completers`, `get_common_complete_suffix`
- `prompt_toolkit.document`: `Document`
- `prompt_toolkit.filters`: `Filter`, `Condition`, `Always`, `Never`, `to_filter`, `is_true`, and documented app-state filters such as `has_focus`, `has_completions`, `has_selection`, `is_done`, `is_read_only`, `is_multiline`, `in_editing_mode`, `emacs_mode`, `vi_mode`, and related Vi/Emacs mode filters
- `prompt_toolkit.formatted_text`: `HTML`, `ANSI`, `FormattedText`, `PygmentsTokens`, `Template`, `to_formatted_text`, `is_formatted_text`, `merge_formatted_text`, `fragment_list_len`, `fragment_list_width`, `fragment_list_to_text`, `split_lines`, `to_plain_text`
- `prompt_toolkit.input`: `Input`, `PipeInput`, `DummyInput`, `create_input`, `create_pipe_input`
- `prompt_toolkit.key_binding`: `KeyBindings`, `KeyBindingsBase`, `ConditionalKeyBindings`, `DynamicKeyBindings`, `merge_key_bindings`, `KeyPress`, `KeyPressEvent`
- `prompt_toolkit.layout`: `Layout`, `InvalidLayoutError`, `walk`, `Dimension`, `D`, `to_dimension`, `is_dimension`, `sum_layout_dimensions`, `max_layout_dimensions`, `Container`, `HSplit`, `VSplit`, `FloatContainer`, `Float`, `Window`, `ConditionalContainer`, `DynamicContainer`, `ScrollablePane`, `BufferControl`, `SearchBufferControl`, `FormattedTextControl`, `UIControl`, `UIContent`, `WindowAlign`, `HorizontalAlign`, `VerticalAlign`, `ScrollOffsets`, `ColorColumn`, margins, and completion menus
- `prompt_toolkit.output`: `Output`, `DummyOutput`, `ColorDepth`, `create_output`
- `prompt_toolkit.shortcuts`: `PromptSession`, `prompt`, `confirm`, `create_confirm_session`, `CompleteStyle`, `choice`, `print_formatted_text`, `print_container`, `clear`, `set_title`, `clear_title`
- `prompt_toolkit.styles`: `Attrs`, `DEFAULT_ATTRS`, `BaseStyle`, `Style`, `Priority`, `merge_styles`, `parse_color`, `DummyStyle`, `DynamicStyle`, `default_ui_style`, `default_pygments_style`, `style_from_pygments_cls`, `style_from_pygments_dict`, `pygments_token_to_classname`, `StyleTransformation` and documented transformation classes
- `prompt_toolkit.validation`: `Validator`, `ValidationError`, `ThreadedValidator`, `DummyValidator`, `ConditionalValidator`, `DynamicValidator`

No command-line executable is part of the covered surface.

## Product State Model

The central user-visible state has three projections:

- Text projection: a `Document` is an immutable snapshot of text, cursor position, and optional selection; a `Buffer` is the mutable editing state that publishes its current `Document`.
- Interaction projection: key bindings, completion, validation, history navigation, and prompt/app accept handlers transform or inspect the current buffer and application.
- Presentation projection: formatted text, styles, controls, containers, layout focus, and application input/output determine what is displayed and where input is routed.

The projections must agree through these invariants:

- A `Buffer.document` read must return a `Document` with the same `text`, `cursor_position`, and selection state as the buffer at that moment.
- Assigning a `Document` to `Buffer.document` must update buffer text and cursor together; observers must not see a cursor position that is out of range for the new text.
- A `BufferControl` created for a buffer must render and focus the same buffer state that key bindings and validators inspect.
- A `Completion.start_position` must be interpreted relative to the document cursor and must replace text between that relative position and the cursor when applied.
- A `Validator` must receive a `Document`, and a validation failure must be stored or raised with a cursor position in that document's coordinate system.
- A `Layout` focus change to a `Buffer`, `Window`, or `UIControl` must route focused key bindings and focus filters to the corresponding control.
- Formatted text fragments and style strings must remain separate: formatted text supplies `(style, text)` fragments, and a `Style` resolves the style strings into attributes.
- `Application.run()` and `PromptSession.prompt()` must return only after the application exits or raises the configured interrupt/end-of-file exception.

## Public API

### Document and Buffer

`Document(text: str = "", cursor_position: int | None = None, selection: SelectionState | None = None)` represents an immutable text snapshot. When `cursor_position` is `None`, the cursor must default to the end of `text`. It must raise `AssertionError` when a provided cursor position is greater than the text length. Text and cursor properties must be read-only.

`Document` must expose:

- `text`, `cursor_position`, `selection`
- `current_char`, `char_before_cursor`, `text_before_cursor`, `text_after_cursor`
- `current_line_before_cursor`, `current_line_after_cursor`, `current_line`, `lines`, `line_count`
- `cursor_position_row`, `cursor_position_col`, `on_first_line`, `on_last_line`, `is_cursor_at_the_end`, `is_cursor_at_the_end_of_line`
- search and word helpers such as `find`, `find_all`, `find_backwards`, `get_word_before_cursor`, `get_word_under_cursor`, current/previous/next word boundary helpers, bracket matching helpers, and relative cursor movement helpers
- selection helpers such as `selection_range`, `selection_ranges`, `cut_selection`, and `paste_clipboard_data`

Line indexes are zero-based. `lines` must split on `"\n"` and must include an empty final line when the text ends with a trailing newline. `translate_index_to_position(index)` must return a zero-based `(row, column)`. `translate_row_col_to_index(row, col)` must clamp negative row or column values to zero and return an absolute text index for the nearest represented location.

Search helpers must return relative positions from the cursor when searching from the cursor and absolute positions for `find_all`. They must return `None` or an empty list when no match exists. Character accessors at text boundaries must return `""` instead of raising.

`Buffer(...)` is the mutable editing state. The constructor must accept public options for `completer`, `auto_suggest`, `history`, `validator`, `name`, `document`, `accept_handler`, read-only/multiline/filter options, completion/validation options, max completions, temp file options, and event callbacks. A new buffer must start with empty text and cursor position `0` when no document is supplied.

`Buffer.text` assignment must keep `cursor_position <= len(text)`. Editing methods such as `insert_text`, `delete`, `delete_before_cursor`, `newline`, `join_next_line`, cursor movement, line transforms, selection cut/copy/paste, completion selection, undo/redo, and history movement must update `document` consistently. Methods that delete text must return the deleted text, and must return `""` when there is nothing to delete. Cursor movement beyond document boundaries must stop at the nearest valid position.

When `read_only` evaluates true, direct text mutation and `set_document(..., bypass_readonly=False)` must raise `EditReadOnlyBuffer`. `set_document(..., bypass_readonly=True)` must update the state anyway.

`Buffer.validate(set_cursor: bool = False)` must return `True` when there is no validator or validation succeeds. It must return `False` when the validator raises `ValidationError`, store that error on the buffer, mark validation invalid, and, when `set_cursor=True`, move the cursor to the error position.

### Completion

`Completion(text: str, start_position: int = 0, display=None, display_meta=None, style: str = "", selected_style: str = "")` describes one possible insertion. `start_position` must be zero or negative. `display` defaults to `text` and is converted to formatted text. `display_text` and `display_meta_text` must return plain text.

`CompleteEvent(text_inserted: bool = False, completion_requested: bool = False)` describes why completion was requested. It must raise `AssertionError` when both flags are true.

`Completer.get_completions(document, complete_event)` must yield `Completion` objects. The default async method must yield the same completions as the synchronous generator unless a subclass overrides it. `DummyCompleter` must yield no completions. `ThreadedCompleter` must preserve the wrapped completer's synchronous results and expose asynchronous completion from a worker thread. `DynamicCompleter` must call its provider and behave like `DummyCompleter` when the provider returns `None`. `ConditionalCompleter` must yield wrapped completions only when its filter evaluates true. `merge_completers([...])` must yield each completer's completions in order.

`WordCompleter(words, ignore_case=False, display_dict=None, meta_dict=None, WORD=False, sentence=False, match_middle=False, pattern=None)` must complete the word before the cursor by default. It must use the full text before the cursor when `sentence=True`. It must raise `AssertionError` when `WORD=True` and `sentence=True` are combined. It must call `words()` at completion time when `words` is callable. It must preserve the word order supplied by the caller. It must use `start_position=-len(matched_input)` for yielded completions.

`PathCompleter(only_directories=False, get_paths=None, file_filter=None, min_input_len=0, expanduser=False)` must complete filesystem names from the current directory by default. It must return no completions when the input length is below `min_input_len`. It must not expand `~` unless `expanduser=True`. It must silently return no completions for filesystem access errors. Directories must be displayed with a trailing slash while the inserted completion text remains the unmatched suffix.

`NestedCompleter.from_nested_dict(data)` must accept nested dictionaries, sets as shorthand for keys with no children, `None` for terminal choices, and `Completer` instances as subtree handlers. Before the first space it must behave like a `WordCompleter` over the top-level keys. After a recognized first term and whitespace it must delegate completion to the nested completer for the remaining text. Unknown first terms must return no completions.

`FuzzyCompleter(completer, WORD=False, pattern=None, enable_fuzzy=True)` must wrap another completer. When fuzzy mode is enabled it must match the characters before the cursor as an ordered subsequence of the inner completion text, case-insensitively, and sort matches by earliest start and then shortest match. When fuzzy mode is disabled it must return the wrapped completer's completions. A non-`None` custom pattern must start with `^` or raise `AssertionError`. `FuzzyWordCompleter` must behave like `WordCompleter` wrapped in `FuzzyCompleter`.

### Validation

`ValidationError(cursor_position: int = 0, message: str = "")` must store both attributes and use the message as the exception message.

`Validator.validate(document)` must raise `ValidationError` to reject a document and return `None` to accept it. `Validator.validate_async(document)` must perform the same validation by default. `Validator.from_callable(validate_func, error_message="Invalid input", move_cursor_to_end=False)` must call `validate_func(document.text)`. It must accept the document when the callable returns true. It must raise `ValidationError` with the configured message and cursor `0` when false, or cursor `len(document.text)` when `move_cursor_to_end=True`.

`DummyValidator` must accept every document. `ConditionalValidator` must call the wrapped validator only when its filter is true. `DynamicValidator` must call the validator returned by its provider and must accept every document when the provider returns `None`. `ThreadedValidator` must preserve synchronous validation and expose asynchronous validation from a worker thread.

### Key Bindings

`KeyBindings()` stores `Binding` objects. `add(*keys, filter=True, eager=False, is_global=False, save_before=lambda e: True, record_in_macro=True)` must return a decorator that registers the handler and returns the original handler. Keys must accept `Keys` enum values, documented key-name strings, one-character strings, and aliases such as `c-h`/`backspace`, `c-m`/`enter`, `c-i`/`tab`, and `c-space`/`c-@`. Invalid key names must raise `ValueError`.

Bindings must support multi-key sequences, filters, eager matching, coroutine handlers, global bindings, and macro-recording flags. `remove(handler)` or `remove(*keys)` must remove a binding and must raise `ValueError` when no matching binding exists.

`KeyProcessor(key_bindings)` receives `KeyPress` objects through `feed` or `feed_multiple`; `process_keys()` must process queued keys until no eligible keys remain. Exact active matches must call the latest registered matching binding. If a key sequence is a prefix of a longer active binding, processing must wait for more keys unless an exact eager binding exists or a flush occurs. Unknown keys must be ignored after allowing any shorter suffix match to run. Handler events must expose `app`, `current_buffer`, `key_sequence`, `previous_key_sequence`, `arg`, and related public state.

`ConditionalKeyBindings` must make the wrapped bindings active only when its filter is true. `DynamicKeyBindings` must delegate to the bindings returned by its provider and behave like an empty binding set when the provider returns `None`. `merge_key_bindings([...])` must preserve binding order across the provided collections.

### Formatted Text

Formatted text inputs are accepted as plain strings, `HTML`, `ANSI`, `FormattedText`, `PygmentsTokens`, lists of `(style, text)` fragments, and callables returning those forms. `to_formatted_text(value, style="")` must return a `FormattedText` fragment list. Applying a non-empty `style` must prefix or combine that style with the converted fragments without changing the plain text. Unsupported inputs must raise `ValueError`.

`HTML(text)` must parse simple HTML-like tags into class-based style strings. Nested tags must combine class names in nesting order. `fg` and `bg` attributes must become foreground and background style strings, and inherited background/foreground attributes must apply to nested text. Attribute values containing spaces must raise `ValueError`.

`ANSI(text)` must parse common ANSI SGR sequences into formatted fragments. It must support reset, foreground/background ANSI colors, 256-color foreground/background, true-color foreground/background, bold, italic, underline, blink, reverse, hidden, dim, and zero-width escape markers. Unknown or malformed escape bytes inside interpolation must be made printable as replacement text instead of leaking raw control parsing state.

`FormattedText(fragments)` must preserve the fragment sequence. `PygmentsTokens(tokens)` must convert Pygments token tuples into `class:pygments...` style strings where dotted token names expand through the style system. `Template(...).format(...)` must accept positional and keyword formatted-text arguments, interpolate them while preserving surrounding literal text, and produce plain text equal to the template text with arguments substituted. `fragment_list_len` must return the number of visible characters in a fragment list. `fragment_list_width` must return the total display-cell width of all fragments. `fragment_list_to_text` and `to_plain_text` must return text with style information removed. `split_lines` must split formatted fragments on newline boundaries while preserving styles.

`print_formatted_text(*values, sep=" ", end="\n", file=None, style=None, color_depth=None, output=None, include_default_pygments_style=True)` must print plain and formatted text using prompt_toolkit styling. It must accept a regular file-like object or an `Output`. It must not require callers to inspect terminal escape bytes for correctness.

### Styles

`Style(style_rules)` must accept a list of `(class_names, style_string)` rules. `Style.from_dict(style_dict, priority=Priority.DICT_KEY_ORDER)` must create a style from an ordered mapping. Later rules must override earlier rules. Class-name order in a selector must not affect matching. Inline style fragments that occur later in a style string must override earlier class-derived attributes.

`BaseStyle.get_attrs_for_style_str(style_str, default=DEFAULT_ATTRS)` and `Style.get_attrs_for_style_str(...)` must resolve a style string into an `Attrs` value. The returned `Attrs` must expose `color`, `bgcolor`, `bold`, `underline`, `strike`, `italic`, `blink`, `reverse`, `hidden`, and `dim` fields. `DEFAULT_ATTRS` must use empty colors and false boolean attributes. When a field is not set by a style rule, resolution must inherit from the supplied default.

Style strings must support foreground colors (`#rgb`, `#rrggbb`, `fg:...`, ANSI color names, named colors), background colors (`bg:...`), `bold`, `italic`, `underline`, `strike`, `blink`, `reverse`, `hidden`, `dim`, and `no...` negations. `roman`, `sans`, `mono`, and `border:...` must be ignored for compatibility. `parse_color` must return normalized colors for valid colors and raise `ValueError` for invalid color strings.

Dotted class names must expand from left to right. For example, `class:a.b.c` must apply matching rules for `a`, `a.b`, and `a.b.c`. Multiple classes must be accepted as repeated `class:` fragments or comma-separated names.

`merge_styles([...])` must produce a style where later styles override earlier styles. `DummyStyle` must always return the provided default attributes. `DynamicStyle` must delegate to the current style returned by its provider and use dummy styling when the provider returns `None`.

`ColorDepth` must expose `DEPTH_1_BIT`, `DEPTH_4_BIT`, `DEPTH_8_BIT`, `DEPTH_24_BIT` and aliases `MONOCHROME`, `ANSI_COLORS_ONLY`, `DEFAULT`, `TRUE_COLOR`. `ColorDepth.from_env()` must return one-bit depth when `NO_COLOR` is set, return the named value when `PROMPT_TOOLKIT_COLOR_DEPTH` is a valid enum value, and return `None` otherwise.

### Layout Controls

`Dimension(min=0, max=None, preferred=None, weight=1)` and `D(...)` describe layout dimensions. A dimension must raise `ValueError` when `max < min`. `to_dimension` must accept integers and dimensions, and must raise `ValueError` for unsupported values. Sum/max helpers must combine dimensions for layout calculations.

`UIContent(get_line, line_count, cursor_position=None, menu_position=None, show_cursor=True)` must provide line fragments by index and line count. `FormattedTextControl(text="", focusable=False, key_bindings=None, show_cursor=True, modal=False, get_cursor_position=None)` must convert its text source to UI content, report preferred width as the longest visible line, and report preferred height as the number of lines. `BufferControl(buffer=None, input_processors=None, lexer=None, key_bindings=None, focusable=True, search_buffer_control=None, preview_search=False, include_default_input_processors=True, ...)` must expose the associated buffer state as UI content.

`Window(content=None, width=None, height=None, style="", wrap_lines=True, dont_extend_width=False, dont_extend_height=False, align=WindowAlign.LEFT, char=None, get_line_prefix=None, scroll_offsets=None, allow_scroll_beyond_bottom=False, always_hide_cursor=False, cursorline=False, cursorcolumn=False, colorcolumns=None, right_margins=None, left_margins=None)` wraps a `UIControl` as a container. `HSplit`, `VSplit`, `FloatContainer`, `Float`, `ConditionalContainer`, `DynamicContainer`, and `ScrollablePane` compose containers and controls into a tree.

`Layout(container, focused_element=None)` must wrap a container tree, expose all windows and controls, and track current and previous focus. It must raise `InvalidLayoutError` when the container tree has no focusable control. `focus(value)` must accept a `Window`, focusable `UIControl`, `Buffer`, or buffer name present in the layout. It must raise `ValueError` when the target is not present or not focusable. `focus_last()` must return focus to the previous control when available.

`to_container` and `to_window` must accept real containers and widgets implementing `__pt_container__`; they must raise `ValueError` for unsupported objects.

### Application, Prompt, and I/O

`Application(layout=None, style=None, include_default_pygments_style=True, style_transformation=None, key_bindings=None, clipboard=None, full_screen=False, color_depth=None, mouse_support=False, enable_page_navigation_bindings=None, paste_mode=False, editing_mode=EditingMode.EMACS, erase_when_done=False, reverse_vi_search_direction=False, min_redraw_interval=None, max_render_postpone_time=0.01, refresh_interval=None, terminal_size_polling_interval=0.5, cursor=None, on_reset=None, on_invalidate=None, before_render=None, after_render=None, input=None, output=None)` glues layout, bindings, style, clipboard, and I/O together. When `layout` is `None`, it must create a dummy layout. When `style_transformation` is `None`, it must use a no-op transformation. `run()` must block until `exit()` sets a result or exception. `run_async()` must provide the asynchronous form. `exit(result=None, exception=None, style="")` must end a running application; it must raise `Exception` when the application is not running or the return value is already set.

`PromptSession` must create a reusable prompt application with persistent history and shared default/search buffers. Its constructor and `prompt()` method must accept prompt text, multiline/wrapping/password options, editing mode, completion, validation, history, clipboard, auto suggestion, styles, right prompt, bottom toolbar, placeholder, key bindings, input, output, and configured interrupt/end-of-file exception types. The default interrupt exception type is `KeyboardInterrupt`; the default end-of-file exception type is `EOFError`. Values passed to `prompt()` must override the session defaults for that call. `prompt()` must return the accepted text. It must raise the configured interrupt exception for the prompt interrupt binding and the configured EOF exception for the end-of-file binding.

The top-level `prompt(...)` function must behave like creating a `PromptSession` for one input call and returning the accepted text. `CompleteStyle` must expose `COLUMN`, `MULTI_COLUMN`, and `READLINE_LIKE`.

`create_pipe_input()` must return a context manager yielding a `PipeInput`. `PipeInput.send_text(text)` and `send_bytes(data)` must feed input to applications using that input. `DummyOutput` must implement the `Output` interface without rendering visible output, making it suitable for tests and non-rendering workflows. `create_app_session(input=None, output=None)` must install default input/output for applications and formatted printing inside its context. `get_app()` must return the current application when one is active. `get_app_or_none()` must return `None` when no real app is active.

## Error Semantics

- `Document(...)` must raise `AssertionError` when `cursor_position > len(text)`.
- `Buffer` editing must raise `EditReadOnlyBuffer` when the buffer is read-only and the operation would mutate text or document state without bypass.
- `Buffer.validate(set_cursor=False)` must catch `ValidationError`, store it, and return `False`; direct validator calls must propagate `ValidationError`.
- `ValidationError` must carry `cursor_position` and `message`.
- `Validator.from_callable(...)` must raise `ValidationError` with the configured message when the callable returns false.
- `CompleteEvent(...)` must raise `AssertionError` when both flags are true.
- `Completion(...)` must raise `AssertionError` when `start_position` is positive.
- `WordCompleter(...)` must raise `AssertionError` when `WORD` and `sentence` are both true.
- `FuzzyCompleter(...)` must raise `AssertionError` when a custom pattern is supplied and does not start with `^`.
- `PathCompleter` must return no completions, not raise, for filesystem `OSError` while listing candidate paths.
- `KeyBindings.add(...)` must raise `ValueError` for invalid key names. `KeyBindings.remove(...)` must raise `ValueError` when no binding matches.
- `to_filter(value)` must raise `TypeError` for values that are neither booleans nor `Filter` instances.
- `HTML(...)` conversion must raise `ValueError` when `fg` or `bg` attribute values contain spaces.
- `to_formatted_text(value)` must raise `ValueError` for unsupported formatted text values.
- `parse_color(value)` must raise `ValueError` for invalid color strings.
- `Dimension(...)` must raise `ValueError` when maximum is smaller than minimum. `to_dimension(value)` must raise `ValueError` for unsupported values.
- `Layout(...)` must raise `InvalidLayoutError` when no focusable control exists. `Layout.focus(...)` must raise `ValueError` when the requested focus target is absent or not focusable.
- `to_container(value)` and `to_window(value)` must raise `ValueError` for unsupported objects.
- `Application.exit(...)` must raise `Exception` when called while the application is not running or after a result has already been set.
- `PromptSession.prompt()` must raise the configured interrupt exception for an interrupt and the configured EOF exception for end of input; by default these are `KeyboardInterrupt` and `EOFError`.

## Cross-View Invariants

- `Buffer.text` and `Buffer.document.text` must always return the same text after each public buffer operation.
- `Buffer.cursor_position` and `Buffer.document.cursor_position` must always return the same integer after each public buffer operation.
- A `Document` returned by a buffer must return line, word, and cursor projections that correspond to the buffer text at the time the document was read.
- Applying a `Completion` through a buffer must update the buffer text exactly as described by the completion's `start_position` and `text`, and the resulting document must expose the inserted text.
- A completion menu, completion toolbar, or other completion view must derive display text from `Completion.display` and insertion text from `Completion.text`; display formatting must not alter inserted buffer text.
- A validator attached to a buffer or prompt must validate the same document text that the prompt returns after acceptance.
- A `ValidationError.cursor_position` stored on a buffer must refer to the same coordinate system as `Buffer.document.cursor_position`.
- A key binding handler that mutates `event.current_buffer` must change the same buffer that the focused `BufferControl` exposes through the layout.
- `Layout.has_focus(buffer)`, `Layout.has_focus(control)`, and `Layout.has_focus(window)` must agree for a focused buffer control and its wrapping window.
- A formatted text object converted with `to_formatted_text` must preserve `to_plain_text` across `HTML`, `ANSI`, `FormattedText`, `PygmentsTokens`, and `Template` inputs.
- A style applied through a container or control must affect style resolution while leaving formatted fragment text unchanged.
- An application or prompt run with a `PipeInput` and `DummyOutput` must produce the same accepted text and buffer state as the same key sequence on real I/O, excluding terminal rendering side effects.

## Representative Workflows

### Prompt With Completion and Validation

```python
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.input import create_pipe_input
from prompt_toolkit.output import DummyOutput
from prompt_toolkit.validation import Validator

validator = Validator.from_callable(
    lambda text: text in {"start", "stop"},
    error_message="Choose start or stop",
)

with create_pipe_input() as inp:
    inp.send_text("start\n")
    session = PromptSession(
        completer=WordCompleter(["start", "stop"]),
        validator=validator,
        input=inp,
        output=DummyOutput(),
    )
    result = session.prompt("> ")

assert result == "start"
assert session.default_buffer.document.text == "start"
```

### Full-Screen Layout With a Buffer and Exit Binding

```python
from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl

buffer = Buffer()
kb = KeyBindings()

@kb.add("c-q")
def _(event):
    event.app.exit(result=event.current_buffer.text)

layout = Layout(
    VSplit([
        Window(BufferControl(buffer=buffer)),
        Window(width=1, char="|"),
        Window(FormattedTextControl("status")),
    ])
)

app = Application(layout=layout, key_bindings=kb, full_screen=True)
```

The application must route typed text to `buffer` while its control is focused. Pressing `c-q` must exit with the current buffer text.

### Formatted Text and Styles

```python
from prompt_toolkit import HTML
from prompt_toolkit.formatted_text import to_formatted_text, to_plain_text
from prompt_toolkit.styles import Style

text = to_formatted_text(HTML("<b>Hello</b> <ansired>world</ansired>"))
style = Style.from_dict({"b": "bold", "ansired": "ansired"})

assert to_plain_text(text) == "Hello world"
assert style.get_attrs_for_style_str("class:b").bold is True
```

Formatted conversion must preserve plain text. Style lookup must resolve class names independently from the text content.

## Non-Goals

- Exact terminal escape sequences, byte-for-byte VT100 output, CPR handling, raw/cooked terminal mode behavior, and platform terminal-driver details are not part of this specification.
- Snapshot-exact rendering, exact screen cell placement, and exact stdout escape strings are not required beyond public return values, state changes, and plain-text/fragment semantics.
- Private helpers, private modules, private attributes, cache internals, parser internals, renderer internals, and test-only helpers are not part of the covered contract.
- Dialog shortcuts, progress bars, contrib SSH/Telnet servers, regular-language contrib helpers, clipboard backends requiring optional third-party packages, Pygments lexer internals, and widget-specific visual polish are outside this scope.
- Performance characteristics, memory usage, background task scheduling order, and redraw throttling internals are outside this scope except where public methods must return, raise, or preserve state as specified.
- Exact exception message strings are not required unless the message is explicitly supplied by the caller and stored on a public exception object.

## Evaluation Notes

Evaluation checks observable behavior through public imports and documented workflows. It focuses on text state, cursor projections, buffer editing, completion outputs, validation outcomes, key binding dispatch, formatted-text conversion, style resolution, layout focus, and prompt/application behavior with controllable input and dummy output.

Scoring treats the specification as the contract. Implementations are expected to pass tests that use public APIs and assert returned values, raised exception classes, public object state, and cross-view invariants. Tests are not intended to require private module structure, exact rendering snapshots, byte-for-byte terminal output, network services, or platform-specific terminal behavior.
