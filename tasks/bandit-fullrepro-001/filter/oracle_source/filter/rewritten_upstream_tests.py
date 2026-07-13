from __future__ import annotations

import bandit


def make_issue(severity=bandit.MEDIUM, confidence=bandit.MEDIUM):
    finding = bandit.Issue(severity, 605, confidence, "Test issue")
    finding.fname = "code.py"
    finding.test = "bandit_plugin"
    finding.test_id = "B999"
    finding.lineno = 1
    finding.col_offset = 8
    finding.end_col_offset = 16
    return finding


def test_issue_constructor_and_public_attributes():
    finding = make_issue()
    assert isinstance(finding, bandit.Issue)
    assert finding.fname == "code.py"
    assert finding.test == "bandit_plugin"


def test_issue_as_dict_without_code():
    data = make_issue().as_dict(with_code=False)
    assert data == {
        "filename": "code.py",
        "test_name": "bandit_plugin",
        "test_id": "B999",
        "issue_severity": "MEDIUM",
        "issue_cwe": {
            "id": 605,
            "link": "https://cwe.mitre.org/data/definitions/605.html",
        },
        "issue_confidence": "MEDIUM",
        "issue_text": "Test issue",
        "line_number": 1,
        "line_range": [],
        "col_offset": 8,
        "end_col_offset": 16,
    }


def test_issue_filter_severity_ranking():
    assert make_issue(bandit.HIGH, bandit.HIGH).filter(
        bandit.MEDIUM, bandit.UNDEFINED
    )
    assert not make_issue(bandit.LOW, bandit.HIGH).filter(
        bandit.MEDIUM, bandit.UNDEFINED
    )


def test_issue_filter_confidence_ranking():
    assert make_issue(bandit.HIGH, bandit.HIGH).filter(
        bandit.UNDEFINED, bandit.MEDIUM
    )
    assert not make_issue(bandit.HIGH, bandit.LOW).filter(
        bandit.UNDEFINED, bandit.MEDIUM
    )


def test_issue_equality_fields_and_location_independence():
    left = make_issue()
    right = make_issue()
    right.lineno = 99
    assert left == right
    right.test = "different_plugin"
    assert left != right


def test_issue_get_code_from_public_filename(tmp_path):
    source = tmp_path / "sample.py"
    source.write_text("first\nsecond\nthird\n", encoding="utf-8")
    finding = bandit.Issue(bandit.LOW, lineno=2)
    finding.fname = str(source)
    finding.linerange = [2]
    code = finding.get_code(max_lines=1)
    assert "2 second" in code
