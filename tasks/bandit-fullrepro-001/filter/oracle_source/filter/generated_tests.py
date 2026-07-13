from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

import bandit


def run_bandit(args, *, cwd=None, input_text=None):
    return subprocess.run(
        [sys.executable, "-m", "bandit", *args],
        cwd=cwd,
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def scan_source(tmp_path, source, *extra):
    target = tmp_path / "target.py"
    target.write_text(source, encoding="utf-8")
    process = run_bandit(["-f", "json", *extra, str(target)])
    report = json.loads(process.stdout)
    return process, report, target


def result_ids(report):
    return [item["test_id"] for item in report["results"]]


def test_ranking_constants_are_strings():
    assert (bandit.UNDEFINED, bandit.LOW, bandit.MEDIUM, bandit.HIGH) == (
        "UNDEFINED",
        "LOW",
        "MEDIUM",
        "HIGH",
    )


@pytest.mark.parametrize("cwe_id", [0, 79, 605])
def test_cwe_dictionary_and_link(cwe_id):
    cwe = bandit.Cwe(cwe_id)
    if cwe_id == 0:
        assert cwe.link() == ""
        assert cwe.as_dict() == {}
    else:
        link = f"https://cwe.mitre.org/data/definitions/{cwe_id}.html"
        assert cwe.link() == link
        assert cwe.as_dict() == {"id": cwe_id, "link": link}


def test_cwe_from_dict_mutates_and_returns_none():
    cwe = bandit.Cwe(79)
    assert cwe.from_dict({"id": 22}) is None
    assert cwe == bandit.Cwe(22)
    assert cwe.from_dict({}) is None
    assert cwe == bandit.Cwe(0)


def test_cwe_string_and_json_string():
    cwe = bandit.Cwe(79)
    assert str(cwe) == f"CWE-79 ({cwe.link()})"
    assert cwe.as_jsons() == str(cwe.as_dict())


@pytest.mark.parametrize(
    "severity,confidence,minimum_severity,minimum_confidence,expected",
    [
        (bandit.HIGH, bandit.HIGH, bandit.MEDIUM, bandit.MEDIUM, True),
        (bandit.LOW, bandit.HIGH, bandit.MEDIUM, bandit.LOW, False),
        (bandit.HIGH, bandit.LOW, bandit.LOW, bandit.MEDIUM, False),
        (bandit.UNDEFINED, bandit.UNDEFINED, bandit.UNDEFINED, bandit.UNDEFINED, True),
    ],
)
def test_issue_filter_uses_both_rankings(
    severity, confidence, minimum_severity, minimum_confidence, expected
):
    finding = bandit.Issue(severity, confidence=confidence)
    assert finding.filter(minimum_severity, minimum_confidence) is expected


def populated_issue():
    finding = bandit.Issue(
        bandit.MEDIUM,
        cwe=79,
        confidence=bandit.HIGH,
        text="unsafe output",
        lineno=3,
        test_id="B999",
        col_offset=4,
        end_col_offset=12,
    )
    finding.fname = "sample.py"
    finding.test = "sample_check"
    finding.linerange = [3]
    return finding


def test_issue_as_dict_schema_without_code():
    data = populated_issue().as_dict(with_code=False)
    assert set(data) == {
        "filename",
        "test_name",
        "test_id",
        "issue_severity",
        "issue_cwe",
        "issue_confidence",
        "issue_text",
        "line_number",
        "line_range",
        "col_offset",
        "end_col_offset",
    }
    assert data["issue_cwe"]["id"] == 79
    assert data["test_id"] == "B999"


def test_issue_from_dict_mutates_and_defaults_columns():
    data = populated_issue().as_dict(with_code=False)
    data["code"] = "3 unsafe_output(value)\n"
    data.pop("col_offset")
    data.pop("end_col_offset")
    finding = bandit.Issue(bandit.LOW)
    assert finding.from_dict(data) is None
    assert finding.fname == "sample.py"
    assert finding.test == "sample_check"
    assert finding.cwe == bandit.Cwe(79)
    assert finding.col_offset == 0
    assert finding.end_col_offset == 0


def test_issue_equality_ignores_location_but_not_identity_fields():
    left = populated_issue()
    right = populated_issue()
    right.lineno = 300
    right.col_offset = 0
    assert left == right
    right.test_id = "B998"
    assert left != right


def test_issue_get_code_respects_line_limit(tmp_path):
    target = tmp_path / "code.py"
    target.write_text("one\ntwo\nthree\nfour\n", encoding="utf-8")
    finding = bandit.Issue(bandit.LOW, lineno=3)
    finding.fname = str(target)
    finding.linerange = [3]
    assert finding.get_code(max_lines=1) == "3 three\n"
    assert len(finding.get_code(max_lines=3).splitlines()) == 3


@pytest.mark.parametrize(
    "decorator,args",
    [
        (bandit.checks, ("Call",)),
        (bandit.test_id, ("B999",)),
        (bandit.takes_config, ("sample",)),
        (bandit.accepts_baseline, ()),
    ],
)
def test_public_decorators_preserve_callable_behavior(decorator, args):
    def sample(value=3):
        return value + 1

    decorated = decorator(*args)(sample) if args else decorator(sample)
    assert callable(decorated)
    assert decorated(4) == 5


DETECTION_CASES = [
    ("B101", "def check(value):\n    assert value\n"),
    ("B102", "exec('value = 1')\n"),
    ("B103", "import os\nos.chmod('data', 0o777)\n"),
    ("B104", "import socket\ns = socket.socket()\ns.bind(('0.0.0.0', 8080))\n"),
    ("B105", "password = 'secret-value'\n"),
    ("B106", "connect(password='secret-value')\n"),
    ("B107", "def connect(password='secret-value'):\n    return password\n"),
    ("B108", "temporary_name = '/tmp/application-state'\n"),
    ("B110", "try:\n    run()\nexcept Exception:\n    pass\n"),
    ("B112", "for item in items:\n    try:\n        run(item)\n    except Exception:\n        continue\n"),
    ("B113", "import requests\nrequests.get('https://example.invalid')\n"),
    ("B201", "from flask import Flask\napp = Flask(__name__)\napp.run(debug=True)\n"),
    ("B202", "import tarfile\ntarfile.open('archive.tar').extractall('.')\n"),
    ("B301", "import pickle\npickle.loads(payload)\n"),
    ("B307", "eval(user_text)\n"),
    ("B310", "import urllib.request\nurllib.request.urlopen(user_url)\n"),
    ("B311", "import random\nrandom.random()\n"),
    ("B312", "import telnetlib\ntelnetlib.Telnet(host)\n"),
    ("B323", "import ssl\nssl._create_unverified_context()\n"),
    ("B324", "import hashlib\nhashlib.md5(payload).hexdigest()\n"),
    ("B401", "import telnetlib\n"),
    ("B403", "import pickle\n"),
    ("B404", "import subprocess\n"),
    ("B405", "import xml.etree.ElementTree\n"),
    ("B415", "from pyghmi.ipmi import command\n"),
    ("B501", "import requests\nrequests.get(url, verify=False)\n"),
    ("B506", "import yaml\nyaml.load(document)\n"),
    (
        "B507",
        "import paramiko\nclient = paramiko.SSHClient()\n"
        "client.set_missing_host_key_policy(paramiko.AutoAddPolicy())\n",
    ),
    ("B602", "import subprocess\nsubprocess.Popen(command, shell=True)\n"),
    ("B603", "import subprocess\nsubprocess.Popen(['/bin/ls', '-l'])\n"),
    ("B605", "import os\nos.system(command)\n"),
    ("B607", "import subprocess\nsubprocess.Popen(['git', 'status'])\n"),
    ("B608", "query = \"SELECT * FROM users WHERE id = '%s'\" % user_id\n"),
    ("B609", "import subprocess\nsubprocess.Popen('/bin/chmod *', shell=True)\n"),
    ("B612", "import logging.config\nlogging.config.listen()\n"),
    ("B614", "import torch\ntorch.load(model_path)\n"),
    (
        "B615",
        "from transformers import AutoModel\nAutoModel.from_pretrained('organization/model')\n",
    ),
    ("B701", "import jinja2\njinja2.Environment(autoescape=False)\n"),
    ("B703", "from django.utils.safestring import mark_safe\nmark_safe(user_text)\n"),
    ("B704", "import markupsafe\nmarkupsafe.Markup(user_text)\n"),
]


@pytest.mark.parametrize(
    "expected_id,source", DETECTION_CASES, ids=[case[0] for case in DETECTION_CASES]
)
def test_detection_family_reports_expected_id(tmp_path, expected_id, source):
    process, report, _ = scan_source(tmp_path, source)
    assert process.returncode == 1
    ids = result_ids(report)
    if expected_id == "B324":
        assert {"B303", "B324"}.intersection(ids)
    else:
        assert expected_id in ids


def test_clean_scan_has_empty_results_and_zero_exit(tmp_path):
    process, report, _ = scan_source(tmp_path, "value = 1\n")
    assert process.returncode == 0
    assert report["results"] == []
    assert report["errors"] == []


def test_finding_scan_has_one_exit_and_exit_zero_override(tmp_path):
    process, report, target = scan_source(tmp_path, "assert value\n", "--tests", "B101")
    assert process.returncode == 1
    assert result_ids(report) == ["B101"]
    override = run_bandit(["-f", "json", "--exit-zero", "--tests", "B101", str(target)])
    assert override.returncode == 0
    assert result_ids(json.loads(override.stdout)) == ["B101"]


def test_syntax_error_is_reported_but_not_a_finding(tmp_path):
    process, report, _ = scan_source(tmp_path, "def broken(:\n    pass\n")
    assert process.returncode == 0
    assert report["results"] == []
    assert len(report["errors"]) == 1


def test_stdin_scan_uses_same_json_projection(tmp_path):
    process = run_bandit(
        ["-f", "json", "--tests", "B101", "-"],
        cwd=tmp_path,
        input_text="assert value\n",
    )
    report = json.loads(process.stdout)
    assert process.returncode == 1
    assert isinstance(report["results"][0]["filename"], str)
    assert report["results"][0]["filename"]
    assert report["results"][0]["test_id"] == "B101"


def test_directory_requires_recursive_flag_for_python_files(tmp_path):
    source_dir = tmp_path / "source"
    source_dir.mkdir()
    (source_dir / "bad.py").write_text("assert value\n", encoding="utf-8")
    skipped = run_bandit(["-f", "json", str(source_dir)])
    assert skipped.returncode == 0
    assert json.loads(skipped.stdout)["results"] == []
    scanned = run_bandit(["-r", "-f", "json", "--tests", "B101", str(source_dir)])
    assert scanned.returncode == 1
    assert result_ids(json.loads(scanned.stdout)) == ["B101"]


def test_recursive_exclusion_removes_matching_subtree(tmp_path):
    root = tmp_path / "tree"
    included = root / "included"
    excluded = root / "excluded"
    included.mkdir(parents=True)
    excluded.mkdir()
    (included / "one.py").write_text("assert one\n", encoding="utf-8")
    (excluded / "two.py").write_text("assert two\n", encoding="utf-8")
    process = run_bandit(
        ["-r", "-f", "json", "--tests", "B101", "-x", str(excluded), str(root)]
    )
    report = json.loads(process.stdout)
    assert process.returncode == 1
    assert len(report["results"]) == 1
    assert report["results"][0]["filename"].endswith("included/one.py")


def test_bare_nosec_and_ignore_nosec(tmp_path):
    source = "assert value  # nosec\n"
    suppressed, report, target = scan_source(tmp_path, source, "--tests", "B101")
    assert suppressed.returncode == 0
    assert report["results"] == []
    ignored = run_bandit(
        ["-f", "json", "--tests", "B101", "--ignore-nosec", str(target)]
    )
    assert ignored.returncode == 1
    assert result_ids(json.loads(ignored.stdout)) == ["B101"]


def test_named_nosec_suppresses_only_named_check(tmp_path):
    source = "import subprocess\nassert subprocess  # nosec B101\n"
    process, report, _ = scan_source(tmp_path, source)
    assert process.returncode == 1
    assert "B101" not in result_ids(report)
    assert "B404" in result_ids(report)
    assert report["metrics"]["_totals"]["skipped_tests"] >= 1


def test_threshold_filters_results_but_not_metrics(tmp_path):
    source = "import subprocess\nsubprocess.Popen(command, shell=True)\n"
    process, report, _ = scan_source(tmp_path, source, "--severity-level", "high")
    assert process.returncode == 1
    assert all(item["issue_severity"] == "HIGH" for item in report["results"])
    assert report["metrics"]["_totals"]["SEVERITY.LOW"] >= 1


def test_overlapping_include_and_skip_is_invocation_error(tmp_path):
    target = tmp_path / "target.py"
    target.write_text("assert value\n", encoding="utf-8")
    process = run_bandit(
        ["-f", "json", "--tests", "B101", "--skip", "B101", str(target)]
    )
    assert process.returncode != 0


def test_repeated_tests_option_uses_last_value(tmp_path):
    source = "assert value\nexec('x = 1')\n"
    process, report, _ = scan_source(
        tmp_path, source, "--tests", "B101", "--tests", "B102"
    )
    assert process.returncode == 1
    assert result_ids(report) == ["B102"]


def test_ini_defaults_are_replaced_by_explicit_cli_tests(tmp_path):
    target = tmp_path / "target.py"
    target.write_text("assert value\nexec('x = 1')\n", encoding="utf-8")
    ini = tmp_path / "options.ini"
    ini.write_text("[bandit]\ntests = B101\n", encoding="utf-8")
    process = run_bandit(
        ["-f", "json", "--ini", str(ini), "--tests", "B102", str(target)]
    )
    assert process.returncode == 1
    assert result_ids(json.loads(process.stdout)) == ["B102"]


def test_ini_targets_apply_when_cli_target_is_absent(tmp_path):
    target = tmp_path / "target.py"
    target.write_text("assert value\n", encoding="utf-8")
    ini = tmp_path / "options.ini"
    ini.write_text(
        f"[bandit]\ntargets = {target}\ntests = B101\n", encoding="utf-8"
    )
    process = run_bandit(["-f", "json", "--ini", str(ini)])
    assert process.returncode == 1
    assert result_ids(json.loads(process.stdout)) == ["B101"]


def test_yaml_profile_is_extended_by_selected_cli_tests(tmp_path):
    target = tmp_path / "target.py"
    target.write_text("assert value\nexec('x = 1')\n", encoding="utf-8")
    config = tmp_path / "bandit.yaml"
    config.write_text("tests:\n  - B101\n", encoding="utf-8")
    process = run_bandit(
        [
            "-f",
            "json",
            "--configfile",
            str(config),
            "--tests",
            "B102",
            str(target),
        ]
    )
    assert process.returncode == 1
    assert set(result_ids(json.loads(process.stdout))) == {"B101", "B102"}


def test_number_controls_json_code_context(tmp_path):
    source = "first = 1\nsecond = 2\nassert second\nfourth = 4\n"
    process, report, _ = scan_source(
        tmp_path, source, "--tests", "B101", "--number", "1"
    )
    assert process.returncode == 1
    assert report["results"][0]["code"].splitlines() == ["3 assert second"]


@pytest.mark.parametrize("format_name", ["csv", "yaml", "xml", "sarif", "txt"])
def test_supported_report_formats_emit_findings(tmp_path, format_name):
    target = tmp_path / "target.py"
    target.write_text("assert value\n", encoding="utf-8")
    process = run_bandit(["-f", format_name, "--tests", "B101", str(target)])
    assert process.returncode == 1
    assert "B101" in process.stdout


def test_output_file_receives_json_report(tmp_path):
    target = tmp_path / "target.py"
    target.write_text("assert value\n", encoding="utf-8")
    output = tmp_path / "report.json"
    process = run_bandit(
        ["-f", "json", "-o", str(output), "--tests", "B101", str(target)]
    )
    assert process.returncode == 1
    assert result_ids(json.loads(output.read_text(encoding="utf-8"))) == ["B101"]


def test_aggregate_mode_changes_result_order(tmp_path):
    root = tmp_path / "src"
    root.mkdir()
    (root / "a.py").write_text("exec('x = 1')\n", encoding="utf-8")
    (root / "z.py").write_text("assert value\n", encoding="utf-8")
    by_file = run_bandit(["-r", "-f", "json", "-a", "file", str(root)])
    by_vuln = run_bandit(["-r", "-f", "json", "-a", "vuln", str(root)])
    file_results = json.loads(by_file.stdout)["results"]
    vuln_results = json.loads(by_vuln.stdout)["results"]
    assert [item["filename"] for item in file_results] == sorted(
        item["filename"] for item in file_results
    )
    assert [item["test_name"] for item in vuln_results] == sorted(
        item["test_name"] for item in vuln_results
    )


def test_baseline_removes_matching_finding_and_changes_exit(tmp_path):
    target = tmp_path / "target.py"
    target.write_text("assert value\n", encoding="utf-8")
    baseline_run = run_bandit(["-f", "json", "--tests", "B101", str(target)])
    baseline = tmp_path / "baseline.json"
    baseline.write_text(baseline_run.stdout, encoding="utf-8")
    matched = run_bandit(
        ["-f", "json", "--tests", "B101", "--baseline", str(baseline), str(target)]
    )
    matched_report = json.loads(matched.stdout)
    assert matched.returncode == 0
    assert matched_report["results"] == []
    assert matched_report["metrics"]["_totals"]["SEVERITY.LOW"] == 1


def test_baseline_json_candidates_for_duplicate_new_signature(tmp_path):
    target = tmp_path / "target.py"
    target.write_text("assert value\n", encoding="utf-8")
    baseline_run = run_bandit(["-f", "json", "--tests", "B101", str(target)])
    baseline = tmp_path / "baseline.json"
    baseline.write_text(baseline_run.stdout, encoding="utf-8")
    target.write_text("exec('x = 1')\nexec('y = 2')\n", encoding="utf-8")
    current = run_bandit(["-f", "json", "--baseline", str(baseline), str(target)])
    report = json.loads(current.stdout)
    assert current.returncode == 1
    b102 = [item for item in report["results"] if item["test_id"] == "B102"]
    assert len(b102) == 2
    assert all(len(item["candidates"]) == 2 for item in b102)


def test_non_baseline_aware_format_is_invocation_error(tmp_path):
    target = tmp_path / "target.py"
    target.write_text("assert value\n", encoding="utf-8")
    baseline_run = run_bandit(["-f", "json", "--tests", "B101", str(target)])
    baseline = tmp_path / "baseline.json"
    baseline.write_text(baseline_run.stdout, encoding="utf-8")
    process = run_bandit(["-f", "yaml", "--baseline", str(baseline), str(target)])
    assert process.returncode != 0


def test_json_result_cwe_link_and_location_fields(tmp_path):
    process, report, _ = scan_source(tmp_path, "assert value\n", "--tests", "B101")
    assert process.returncode == 1
    result = report["results"][0]
    assert result["issue_cwe"]["link"].endswith(
        f"/{result['issue_cwe']['id']}.html"
    )
    assert result["line_number"] == 1
    assert result["line_range"] == [1]
    assert isinstance(result["col_offset"], int)
    assert isinstance(result["end_col_offset"], int)
