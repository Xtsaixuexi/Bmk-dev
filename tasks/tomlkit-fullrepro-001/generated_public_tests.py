from __future__ import annotations

import io
import os

from datetime import date as py_date
from datetime import datetime as py_datetime
from datetime import time as py_time
from pathlib import Path

import pytest

from tomlkit import aot
from tomlkit import array
from tomlkit import boolean
from tomlkit import comment
from tomlkit import date
from tomlkit import datetime
from tomlkit import document
from tomlkit import dump
from tomlkit import dumps
from tomlkit import float_
from tomlkit import inline_table
from tomlkit import integer
from tomlkit import item
from tomlkit import key
from tomlkit import key_value
from tomlkit import load
from tomlkit import loads
from tomlkit import nl
from tomlkit import parse
from tomlkit import register_encoder
from tomlkit import string
from tomlkit import table
from tomlkit import time
from tomlkit import unregister_encoder
from tomlkit import value
from tomlkit import ws
from tomlkit.exceptions import ConvertError
from tomlkit.exceptions import EmptyKeyError
from tomlkit.exceptions import EmptyTableNameError
from tomlkit.exceptions import InvalidCharInStringError
from tomlkit.exceptions import InvalidDateError
from tomlkit.exceptions import InvalidDateTimeError
from tomlkit.exceptions import InvalidNumberError
from tomlkit.exceptions import InvalidStringError
from tomlkit.exceptions import InvalidTimeError
from tomlkit.exceptions import InvalidUnicodeValueError
from tomlkit.exceptions import KeyAlreadyPresent
from tomlkit.exceptions import NonExistentKey
from tomlkit.exceptions import ParseError
from tomlkit.exceptions import TOMLKitError
from tomlkit.exceptions import UnexpectedCharError
from tomlkit.exceptions import UnexpectedEofError
from tomlkit.toml_document import TOMLDocument
from tomlkit.toml_file import TOMLFile


def test_parse_and_dumps_preserve_comments_and_inline_comment():
    content = '# title\n[tool.demo]\nname = "demo"  # package\n'
    doc = parse(content)
    assert isinstance(doc, TOMLDocument)
    assert doc["tool"]["demo"]["name"] == "demo"
    assert dumps(doc) == content


def test_loads_alias_and_load_file_like_match_parse():
    content = "a = 1\nb = true\n"
    assert loads(content).unwrap() == parse(content).unwrap()
    assert load(io.StringIO(content)).unwrap() == {"a": 1, "b": True}


def test_parse_accepts_bytes_input():
    doc = parse(b'a = "b"\n')
    assert doc["a"] == "b"
    assert dumps(doc) == 'a = "b"\n'


def test_dump_writes_same_text_as_dumps():
    buf = io.StringIO()
    data = {"b": 2, "a": 1}
    dump(data, buf, sort_keys=True)
    assert buf.getvalue() == dumps(data, sort_keys=True)
    assert buf.getvalue().splitlines() == ["a = 1", "b = 2"]


def test_dumps_rejects_unsupported_non_mapping():
    with pytest.raises(TypeError):
        dumps(object())  # type: ignore[arg-type]


def test_document_add_comment_newline_and_table():
    doc = document()
    doc.add(comment("heading"))
    doc.add(nl())
    t = table()
    t["x"] = 1
    doc["tool"] = t
    text = dumps(doc)
    assert text.startswith("# heading\n\n")
    assert "[tool]" in text
    assert "x = 1" in text


def test_document_mapping_update_pop_and_unwrap():
    doc = document()
    doc["a"] = 1
    doc.update({"b": {"c": 2}})
    assert "a" in doc
    assert doc.pop("a") == 1
    assert doc.unwrap() == {"b": {"c": 2}}


def test_document_delete_removes_rendered_entry():
    doc = parse("a = 1\nb = 2\n")
    del doc["a"]
    assert doc.unwrap() == {"b": 2}
    assert "a = 1" not in dumps(doc)


def test_editing_parsed_table_preserves_unrelated_comment():
    doc = parse("# keep\n[tool]\na = 1\n")
    doc["tool"]["b"] = 2
    text = dumps(doc)
    assert "# keep" in text
    assert "a = 1" in text
    assert "b = 2" in text


def test_table_update_and_comment_rendering():
    t = table()
    t.update({"x": 1})
    t["y"] = 2
    t["y"].comment("why")
    text = t.as_string()
    assert "x = 1" in text
    assert "y = 2" in text
    assert "# why" in text
    assert t.unwrap() == {"x": 1, "y": 2}


def test_super_table_renders_child_table_header():
    doc = document()
    parent = table(True)
    child = table()
    child["x"] = 1
    parent.append("child", child)
    doc["parent"] = parent
    assert dumps(doc) == "[parent.child]\nx = 1\n"


def test_inline_table_editing_keeps_valid_separators():
    it = inline_table()
    it["x"] = 1
    it["y"] = 2
    assert it.as_string() == "{x = 1, y = 2}"
    del it["x"]
    assert it.as_string() == "{y = 2}"


def test_array_default_append_insert_and_unwrap():
    arr = array()
    arr.append(1)
    arr.insert(0, "zero")
    assert arr.unwrap() == ["zero", 1]
    assert arr.as_string() == '["zero",1]'


def test_array_parse_multiline_add_line():
    arr = array("[\n]")
    arr.multiline(True)
    arr.add_line(1, 2, comment="numbers")
    text = arr.as_string()
    assert "1" in text and "2" in text
    assert "# numbers" in text


def test_array_rejects_non_array_literal():
    with pytest.raises(ValueError):
        array("1")


def test_aot_append_dict_and_render_in_document():
    doc = document()
    products = aot()
    products.append({"name": "Hammer", "sku": 738594937})
    doc["products"] = products
    text = dumps(doc)
    assert "[[products]]" in text
    assert 'name = "Hammer"' in text
    assert products.unwrap() == [{"name": "Hammer", "sku": 738594937}]


def test_integer_and_float_items_behave_like_numbers():
    assert integer("2") + 3 == 5
    assert float_("1.5") * 2 == 3.0
    assert integer(7).as_string() == "7"


def test_boolean_helper_accepts_bool_and_toml_strings():
    assert boolean(True) is True or boolean(True) == True
    assert boolean("true") == True
    assert boolean("false") == False
    assert boolean("true").as_string() == "true"


def test_basic_literal_and_multiline_string_helpers():
    assert string("hello").as_string() == '"hello"'
    assert string("C:\\temp", literal=True).as_string() == "'C:\\temp'"
    assert string("a\nb", multiline=True).as_string().startswith('"""')


def test_string_escape_false_preserves_valid_content():
    assert string("abc", escape=False).as_string() == '"abc"'


def test_date_time_datetime_helpers_unwrap_to_python_types():
    assert date("1979-05-27").unwrap() == py_date(1979, 5, 27)
    assert time("12:34:56").unwrap() == py_time(12, 34, 56)
    assert datetime("1979-05-27T07:32:00").unwrap() == py_datetime(1979, 5, 27, 7, 32)


def test_temporal_helpers_reject_wrong_temporal_kind():
    with pytest.raises(ValueError):
        date("12:34:56")
    with pytest.raises(ValueError):
        time("1979-05-27")
    with pytest.raises(ValueError):
        datetime("1979-05-27")


def test_key_single_and_dotted_rendering():
    assert key("plain").as_string() == "plain"
    assert key(["tool", "demo"]).as_string() == "tool.demo"
    assert key(["only"]).as_string() == "only"


def test_value_parses_scalars_and_arrays():
    assert value("1").unwrap() == 1
    assert value("true").unwrap() is True
    assert value("[1, 2]").unwrap() == [1, 2]


def test_value_rejects_trailing_characters():
    with pytest.raises(UnexpectedCharError):
        value("1 junk")


def test_key_value_parses_pair():
    k, v = key_value("tool.demo = 42")
    assert k.as_string().strip() == "tool.demo"
    assert v.unwrap() == 42


def test_comment_multiline_renders_each_line_as_comment():
    c = comment("one\n\ntwo")
    assert c.as_string() == "# one\n#\n# two\n"


def test_whitespace_and_newline_items_render_layout():
    assert ws("   ").as_string() == "   "
    assert nl().as_string() == "\n"


def test_item_converts_plain_mapping_and_list():
    converted = item({"a": [1, "x"]})
    assert converted.unwrap() == {"a": [1, "x"]}
    assert "a = [1, \"x\"]" in converted.as_string()


def test_item_converts_tuple_to_array():
    converted = item({"coords": (1, 2)})
    assert converted.unwrap() == {"coords": [1, 2]}


def test_item_sort_keys_orders_mapping_output():
    assert item({"b": 2, "a": 1}, _sort_keys=True).as_string().splitlines() == [
        "a = 1",
        "b = 2",
    ]


def test_item_unsupported_value_raises_convert_error():
    with pytest.raises(ConvertError):
        item(object())


def test_custom_encoder_decorator_and_unregister():
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    @register_encoder
    def encode_point(obj, _parent=None, _sort_keys=False):
        if isinstance(obj, Point):
            t = table()
            t["x"] = obj.x
            t["y"] = obj.y
            return t
        raise ConvertError("not a point")

    try:
        rendered = item({"point": Point(1, 2)}).as_string()
        assert "[point]" in rendered
        assert "x = 1" in rendered
        assert "y = 2" in rendered
    finally:
        unregister_encoder(encode_point)

    with pytest.raises(ConvertError):
        item(Point(1, 2))


def test_unregister_missing_encoder_is_noop():
    def encoder(obj):
        raise ConvertError("no")

    assert unregister_encoder(encoder) is None


def test_toml_file_preserves_lf_line_endings(tmp_path: Path):
    path = tmp_path / "pyproject.toml"
    path.write_bytes(b"a = 1\nb = 2\n")
    tf = TOMLFile(path)
    doc = tf.read()
    doc["b"] = 3
    tf.write(doc)
    assert path.read_bytes() == b"a = 1\nb = 3\n"


def test_toml_file_preserves_crlf_line_endings(tmp_path: Path):
    path = tmp_path / "pyproject.toml"
    path.write_bytes(b"a = 1\r\nb = 2\r\n")
    tf = TOMLFile(path)
    doc = tf.read()
    doc["b"] = 3
    tf.write(doc)
    assert path.read_bytes() == b"a = 1\r\nb = 3\r\n"


def test_toml_file_keeps_mixed_line_endings(tmp_path: Path):
    path = tmp_path / "pyproject.toml"
    path.write_bytes(b"a = 1\r\nb = 2\n")
    tf = TOMLFile(path)
    tf.write(tf.read())
    assert path.read_bytes() == b"a = 1\r\nb = 2\n"


def test_parse_error_exposes_line_and_column():
    with pytest.raises(ParseError) as excinfo:
        parse("[x]\na @ 1\n")
    assert excinfo.value.line == 2
    assert excinfo.value.col >= 1


@pytest.mark.parametrize(
    ("src", "exc_type"),
    [
        ("a = 1.2.3", InvalidNumberError),
        ("a = 1979-99-99", InvalidDateError),
        ("a = 25:00:00", InvalidTimeError),
        ("a = 1979-05-27T25:00:00", InvalidDateTimeError),
        ('a = "bad\\u12_3"', InvalidUnicodeValueError),
        ("[]", EmptyTableNameError),
    ],
)
def test_parse_raises_public_exception_categories(src, exc_type):
    with pytest.raises(exc_type):
        parse(src)


def test_unexpected_eof_is_public_parse_error():
    with pytest.raises(UnexpectedEofError):
        parse('a = "unterminated')


def test_exception_classes_share_public_base_classes():
    assert issubclass(ParseError, ValueError)
    assert issubclass(ParseError, TOMLKitError)
    assert issubclass(NonExistentKey, KeyError)
    assert issubclass(KeyAlreadyPresent, TOMLKitError)


def test_duplicate_key_raises_key_already_present():
    doc = document()
    doc.add("a", 1)
    with pytest.raises(KeyAlreadyPresent):
        doc.add("a", 2)


def test_missing_key_item_raises_nonexistent_key():
    doc = document()
    with pytest.raises(NonExistentKey):
        doc.item("missing")


def test_inline_table_inside_nested_array_round_trips():
    data = {"foo": [[{"a": 1}]]}
    text = dumps(data)
    assert text == "foo = [[{a = 1}]]\n"
    assert loads(text).unwrap() == data


def test_out_of_order_table_data_is_preserved():
    doc = parse("[a.b]\nx = 1\n[a]\ny = 2\n")
    assert doc["a"]["b"]["x"] == 1
    assert doc["a"]["y"] == 2
    assert doc.unwrap() == {"a": {"b": {"x": 1}, "y": 2}}


def test_replacing_value_with_table_keeps_following_dotted_sibling():
    doc = parse("a.b = 1\na.c = 2\n")
    doc["a"]["b"] = {"nested": True}
    text = dumps(doc)
    assert "nested = true" in text
    assert "c = 2" in text


def test_copy_is_independently_editable():
    original = parse("a = 1\n")
    copied = original.copy()
    copied["a"] = 2
    assert original["a"] == 1
    assert copied["a"] == 2
