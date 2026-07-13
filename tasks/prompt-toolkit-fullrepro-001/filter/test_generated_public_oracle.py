from __future__ import annotations

import pytest

from prompt_toolkit import ANSI, HTML, Application, PromptSession, choice, print_formatted_text, prompt
from prompt_toolkit.application import create_app_session, get_app_or_none
from prompt_toolkit.buffer import Buffer, EditReadOnlyBuffer
from prompt_toolkit.completion import CompleteEvent, Completion, FuzzyCompleter, WordCompleter
from prompt_toolkit.document import Document
from prompt_toolkit.formatted_text import Template, to_formatted_text, to_plain_text
from prompt_toolkit.input import create_pipe_input
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.layout import Layout, VSplit, Window, to_container, to_window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.dimension import Dimension
from prompt_toolkit.output import ColorDepth, DummyOutput
from prompt_toolkit.styles import Style, parse_color
from prompt_toolkit.validation import ConditionalValidator, DummyValidator, DynamicValidator, ValidationError, Validator


def test_public_import_surface_smoke():
    assert Application is not None
    assert PromptSession is not None
    assert HTML("<b>x</b>")
    assert ANSI("\x1b[31mx")


def test_public_subpackage_import_surface_smoke():
    from prompt_toolkit.completion import PathCompleter
    from prompt_toolkit.formatted_text import FormattedText
    from prompt_toolkit.layout import HSplit
    from prompt_toolkit.styles import Attrs

    assert PathCompleter is not None
    assert FormattedText([("", "x")])
    assert HSplit is not None
    assert Attrs is not None


def test_top_level_shortcut_symbols_are_importable():
    assert prompt is not None
    assert choice is not None
    assert print_formatted_text is not None


def test_color_depth_public_aliases_and_invalid_env(monkeypatch):
    assert ColorDepth.TRUE_COLOR == ColorDepth.DEPTH_24_BIT
    monkeypatch.delenv("NO_COLOR", raising=False)
    monkeypatch.setenv("PROMPT_TOOLKIT_COLOR_DEPTH", "not-valid")
    assert ColorDepth.from_env() is None
    monkeypatch.setenv("NO_COLOR", "1")
    assert ColorDepth.from_env() == ColorDepth.DEPTH_1_BIT


def test_document_cursor_position_out_of_range_raises():
    with pytest.raises(AssertionError):
        Document("abc", cursor_position=4)


def test_buffer_read_only_rejects_text_edits_and_bypass_allows_document_set():
    buf = Buffer(read_only=True)
    with pytest.raises(EditReadOnlyBuffer):
        buf.insert_text("x")
    buf.set_document(Document("forced", 3), bypass_readonly=True)
    assert buf.document.text == "forced"
    assert buf.document.cursor_position == 3


def test_buffer_validate_stores_validation_error_and_moves_cursor():
    validator = Validator.from_callable(
        lambda text: text.isdigit(), error_message="digits only", move_cursor_to_end=True
    )
    buf = Buffer(document=Document("abc", 1), validator=validator)
    assert buf.validate(set_cursor=True) is False
    assert isinstance(buf.validation_error, ValidationError)
    assert buf.validation_error.cursor_position == 3
    assert buf.cursor_position == 3


def test_validator_from_callable_success_and_failure_positions():
    validator = Validator.from_callable(lambda text: text == "ok", error_message="bad")
    validator.validate(Document("ok"))
    with pytest.raises(ValidationError) as excinfo:
        validator.validate(Document("nope"))
    assert excinfo.value.cursor_position == 0
    assert excinfo.value.message == "bad"


def test_dummy_conditional_and_dynamic_validators_use_public_fallbacks():
    DummyValidator().validate(Document("anything"))
    failing = Validator.from_callable(lambda text: False, error_message="no")
    ConditionalValidator(failing, filter=False).validate(Document("anything"))
    DynamicValidator(lambda: None).validate(Document("anything"))


def test_dynamic_validator_delegates_to_current_validator():
    validator = DynamicValidator(
        lambda: Validator.from_callable(lambda text: text == "ok", error_message="bad")
    )
    validator.validate(Document("ok"))
    with pytest.raises(ValidationError):
        validator.validate(Document("bad"))


def test_buffer_apply_completion_keeps_document_projection_consistent():
    buf = Buffer(document=Document("hello wor", len("hello wor")))
    buf.apply_completion(Completion("world", start_position=-3))
    assert buf.text == "hello world"
    assert buf.document.text == "hello world"
    assert buf.cursor_position == len("hello world")


def test_completion_error_preconditions_are_enforced():
    with pytest.raises(AssertionError):
        Completion("x", start_position=1)
    with pytest.raises(AssertionError):
        CompleteEvent(text_inserted=True, completion_requested=True)
    with pytest.raises(AssertionError):
        WordCompleter(["x"], WORD=True, sentence=True)
    with pytest.raises(AssertionError):
        FuzzyCompleter(WordCompleter(["x"]), pattern="not-anchored")


def test_style_and_layout_error_preconditions_are_enforced():
    with pytest.raises(ValueError):
        parse_color("not a color")
    with pytest.raises(ValueError):
        Dimension(min=5, max=3)


def test_key_binding_invalid_keys_and_missing_remove_raise_value_error():
    kb = KeyBindings()
    with pytest.raises(ValueError):
        kb.add("not-a-real-key")
    def handler(event):
        return None
    with pytest.raises(ValueError):
        kb.remove(handler)


def test_html_attribute_validation_and_plain_text_preservation():
    with pytest.raises(ValueError):
        to_formatted_text(HTML('<tag fg="bad value">x</tag>'))
    formatted = to_formatted_text(HTML("<b>Hello</b> <ansired>world</ansired>"))
    assert to_plain_text(formatted) == "Hello world"


def test_to_formatted_text_rejects_unsupported_values():
    with pytest.raises(ValueError):
        to_formatted_text(object())


def test_formatted_text_control_creates_content_from_public_fragments():
    control = FormattedTextControl([("class:title", "hello"), ("", "\nworld")])
    content = control.create_content(width=20, height=5)
    assert content.line_count == 2
    assert to_plain_text(content.get_line(0)) == "hello"
    assert to_plain_text(content.get_line(1)) == "world"


def test_layout_focus_accepts_buffer_and_keeps_control_window_agreement():
    buf = Buffer()
    control = BufferControl(buffer=buf)
    left = Window(control)
    right = Window(FormattedTextControl("status"))
    layout = Layout(VSplit([left, right]))
    layout.focus(buf)
    assert layout.has_focus(buf)
    assert layout.has_focus(control)
    assert layout.has_focus(left)


def test_layout_focus_last_returns_previous_control():
    first = BufferControl(buffer=Buffer())
    second = BufferControl(buffer=Buffer())
    layout = Layout(VSplit([Window(first), Window(second)]))
    layout.focus(first)
    layout.focus(second)
    layout.focus_last()
    assert layout.has_focus(first)


def test_to_container_and_to_window_reject_unsupported_objects():
    with pytest.raises(ValueError):
        to_container(object())
    with pytest.raises(ValueError):
        to_window(object())


def test_prompt_session_pipe_input_dummy_output_returns_buffer_text():
    with create_pipe_input() as inp:
        inp.send_text("start\r")
        session = PromptSession(
            input=inp,
            output=DummyOutput(),
            completer=WordCompleter(["start", "stop"]),
            validator=Validator.from_callable(lambda text: text in {"start", "stop"}),
        )
        result = session.prompt("> ")
    assert result == "start"
    assert session.default_buffer.document.text == "start"


def test_prompt_session_accept_default_workflow_reuses_session():
    with create_pipe_input() as inp:
        session = PromptSession(input=inp, output=DummyOutput())
        assert session.prompt(default="first", accept_default=True) == "first"
        assert session.prompt(default="second", accept_default=True) == "second"


def test_top_level_prompt_with_pipe_input_returns_text():
    with create_pipe_input() as inp:
        inp.send_text("hello\r")
        with create_app_session(input=inp, output=DummyOutput()):
            assert prompt("> ") == "hello"


def test_prompt_session_custom_eof_exception_type_is_raised():
    class Done(Exception):
        pass

    with create_pipe_input() as inp:
        inp.send_text("\x04\r")
        session = PromptSession(input=inp, output=DummyOutput(), eof_exception=Done)
        with pytest.raises(Done):
            session.prompt("> ")


def test_app_session_context_installs_dummy_output_defaults():
    with create_app_session(output=DummyOutput()):
        assert get_app_or_none() is None


def test_style_lookup_does_not_change_formatted_plain_text():
    fragments = to_formatted_text(HTML("<b>Hello</b> <ansired>world</ansired>"))
    style = Style.from_dict({"b": "bold", "ansired": "ansired"})
    assert to_plain_text(fragments) == "Hello world"
    assert style.get_attrs_for_style_str("class:b").bold is True


def test_template_formatted_text_style_workflow_preserves_plain_text():
    fragments = Template("Result: {}").format(HTML("<b>ok</b>"))
    style = Style.from_dict({"b": "bold"})
    assert to_plain_text(fragments) == "Result: ok"
    assert style.get_attrs_for_style_str("class:b").bold is True


def test_formatted_text_style_workflow_combines_classes_and_inline_style():
    fragments = to_formatted_text([("class:left class:right", "value")])
    style = Style([("left", "ansired"), ("right", "bold")])
    attrs = style.get_attrs_for_style_str(fragments[0][0] + " underline")
    assert to_plain_text(fragments) == "value"
    assert attrs.bold is True
    assert attrs.underline is True


def test_full_screen_layout_workflow_objects_share_buffer():
    buffer = Buffer()
    kb = KeyBindings()

    @kb.add("c-q")
    def _(event):
        event.app.exit(result=event.current_buffer.text)

    control = BufferControl(buffer=buffer)
    layout = Layout(VSplit([Window(control), Window(width=1, char="|")]))
    app = Application(layout=layout, key_bindings=kb, full_screen=True, output=DummyOutput())
    buffer.insert_text("ready")
    assert app.layout.has_focus(control)
    assert app.layout.current_buffer.text == "ready"


def test_full_screen_layout_workflow_can_focus_second_buffer():
    first = Buffer()
    second = Buffer()
    first_control = BufferControl(buffer=first)
    second_control = BufferControl(buffer=second)
    app = Application(
        layout=Layout(VSplit([Window(first_control), Window(second_control)])),
        full_screen=True,
        output=DummyOutput(),
    )
    app.layout.focus(second)
    second.insert_text("selected")
    assert app.layout.has_focus(second_control)
    assert app.layout.current_buffer.text == "selected"


def test_full_screen_layout_workflow_includes_status_control():
    buffer = Buffer()
    status = FormattedTextControl("status")
    app = Application(
        layout=Layout(VSplit([Window(BufferControl(buffer=buffer)), Window(status)])),
        full_screen=True,
        output=DummyOutput(),
    )
    assert app.full_screen is True
    assert to_plain_text(status.create_content(width=20, height=1).get_line(0)) == "status"


def test_application_default_layout_and_exit_error_semantics():
    app = Application(output=DummyOutput())
    assert app.layout is not None
    with pytest.raises(Exception):
        app.exit(result="done")
