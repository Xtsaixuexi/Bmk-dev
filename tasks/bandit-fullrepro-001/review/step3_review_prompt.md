# Independent Stage 3 Oracle Review: Bandit

Review only the appended candidate specification and oracle artifacts. Do not browse, use tools, inspect a repository, infer hidden tests, or import behavior from another revision.

Check:

- every scoreable assertion is public, behavioral, and derivable from a cited specification section;
- no private imports, internal object shapes, exact human diagnostic prose, source-tree fixture dependence, network execution, or candidate-visible leakage appears;
- generated inputs may contain source snippets, but assertions must test documented IDs, schemas, state projections, or errors rather than hidden implementation details;
- parameterized detection cases provide meaningful independent nodeids rather than duplicate padding;
- `spec_test_map`, taxonomy, quota, reference gate, dummy gate, and provenance totals are mutually consistent;
- atomic/integration/system_e2e classifications are reasonable;
- reference success and dummy failure establish a nontrivial offline oracle;
- the oracle is ready to advance to candidate evaluation.

Return only:

- `VERDICT`: PASS_CONTINUE or PATCH_REQUIRED
- `PUBLIC_BEHAVIOR_ONLY`: PASS or FAIL
- `SPEC_TRACEABILITY`: PASS or FAIL
- `ORACLE_NONTRIVIALITY`: PASS or FAIL
- `TAXONOMY_AND_ACCOUNTING`: PASS or FAIL
- `OFFLINE_DETERMINISM`: PASS or FAIL
- `CANDIDATE_SAFETY`: PASS or FAIL
- `ADVANCE_TO_STAGE4`: YES or NO
- `BLOCKERS`: exact mandatory corrections; empty for PASS_CONTINUE

---
# Bandit Specification

## Product Overview
Bandit scans Python source code for common security issues. It accepts files, directories (scanned recursively), and `-` to read from stdin. Findings are emitted in multiple formats: screen/text, CSV, custom, HTML, JSON, SARIF, XML, and YAML.

## Scope
This specification defines the public, observable behavior of Bandit as a command-line tool and Python library. It covers:

- Supported input targets and output formats
- CLI argument syntax, configuration file handling, and test selection
- Suppression of findings via inline `# nosec` comments
- Exit code semantics
- Structure and content of the JSON report
- The stable public Python API: classes, functions, decorators, and constants
- The set of built-in detection families and their stable severity/confidence ratings
- Error collection and reporting
- Invariants that hold across different views (CLI, JSON, library)

Internal architecture, exact wording of diagnostic messages, absolute filesystem paths, timestamps, and third-party loader internals are **out of scope**.

## Product State Model
A scan has three public projections over the same result state:

1. The scan request combines targets, exclusions, configuration, selected test IDs, suppression comments, severity/confidence thresholds, and an optional baseline.
2. The finding view contains the surviving issues plus file parse/access errors and scan metrics. Findings are identified by test ID, location, severity, confidence, text, and optional CWE.
3. Report formatters and the process exit status project that finding view for people and automation.

Configuration-provided and command-line `tests`/`skips` values must describe one effective test set under the precedence rules below. Exclusions and `# nosec` determine the discovered unsuppressed set; severity/confidence thresholds and an optional baseline determine the reportable set. JSON `results` is that post-threshold, post-baseline reportable set. Metrics preserve counts for the discovered unsuppressed set before threshold and baseline filtering. A parse error must appear as an error rather than a security finding. The exit status reflects the same reportable set represented by `results` unless `--exit-zero` overrides it.

## Installable Surface
Bandit is distributed as a Python package. The scoped scanner surface provides:

- The `bandit` command-line entry point and `python -m bandit`.
- The public library modules `bandit` and `bandit.context`, importable with the names and symbols listed in the Public API section.

The distribution also installs the auxiliary `bandit-config-generator` and `bandit-baseline` commands. Their detailed command behavior is outside this scanner contract.

## Public API

### Constants
```python
from bandit import UNDEFINED, LOW, MEDIUM, HIGH
```
These constants are the strings `"UNDEFINED"`, `"LOW"`, `"MEDIUM"`, and `"HIGH"`, respectively. Their ranking is `UNDEFINED < LOW < MEDIUM < HIGH`; comparisons use that ordering rather than numeric values.

### `Issue`
Represents a single finding.

**Constructor**
```python
Issue(severity, cwe=0, confidence=UNDEFINED, text="", ident=None,
      lineno=None, test_id="", col_offset=-1, end_col_offset=0)
```
Defaults are as shown.

**Methods**

- `Issue.filter(severity, confidence)` -> `bool`  
  Returns `True` if the issue's severity **and** confidence are both at least as high as the given thresholds (using the ranking above). Both dimensions must meet their threshold.

- `Issue.get_code(max_lines=3, tabbed=False)` -> `str`  
  Returns a code snippet around the line where the issue occurred.

- `Issue.as_dict(with_code=True, max_lines=3)` -> `dict`  
  Serialises the issue to a dictionary with `filename`, `test_name`, `test_id`, `issue_severity`, `issue_cwe`, `issue_confidence`, `issue_text`, `line_number`, `line_range`, `col_offset`, and `end_col_offset`. If `with_code` is `True`, a `code` snippet is also included. Documentation metadata such as `more_info` is added by report formatters and is not produced by this method.

- `Issue.from_dict(data, with_code=True)` -> `None`  
  Mutates the existing issue from a structured issue dictionary and returns `None`. The input must provide `code`, `filename`, `issue_severity`, `issue_cwe`, `issue_confidence`, `issue_text`, `test_name`, `test_id`, `line_number`, and `line_range`; missing required keys raise `KeyError`. `col_offset` and `end_col_offset` are optional and default to 0. The accepted `with_code` parameter does not change deserialisation behavior. Consequently, this method is not a direct inverse of `as_dict(with_code=False)`; callers must supply `code` before deserialising such a dictionary.

Each issue initializes public `fname` (filename) and `test` (test name) attributes to empty strings. Scanning or `from_dict()` populates those attributes. Two issues compare equal when their text, severity, CWE, confidence, `fname`, `test`, and test ID match. Exact `str(issue)` formatting is not part of the compatibility contract.

### `Cwe`
Manages a Common Weakness Enumeration identifier.

**Constructor**
```python
Cwe(id=0)
```

**Methods**

- `Cwe.link()` -> `str`  
  If `id` is non-zero, returns `https://cwe.mitre.org/data/definitions/<id>.html`; otherwise returns the empty string.

- `Cwe.as_dict()` -> `dict`  
  For a non-zero CWE returns `{'id': <id>, 'link': <link>}`; for CWE 0 returns an empty dict.

- `Cwe.as_jsons()` -> `str`  
  Returns the string representation of `as_dict()`.

- `Cwe.from_dict(data)` -> `None`  
  Mutates the current object from an `id` field, resets a missing ID to 0, and returns `None`.

CWEs compare by numeric ID. `str(Cwe(0))` returns the empty string; a nonzero value returns `CWE-<id> (<link>)`.

### Decorators
```python
from bandit import checks, takes_config, test_id, accepts_baseline
```

- `checks(*node_types)` marks a function as a check that runs for AST nodes of the given types.
- `takes_config(function_or_name)` indicates that the decorated check accepts configuration, optionally binding a specific configuration key.
- `test_id(id_value)` assigns a stable identifier such as `"B101"` to a check.
- `accepts_baseline(formatter)` marks a formatter as able to present baseline-aware results.

### Plugin Context (`bandit.context`)
When writing a plugin, the `context` object provides:

- `call_args`, `call_args_count`, `call_function_name`, `call_function_name_qual`, and `call_keywords` describe the current call.
- `node`, `statement`, `string_val`, `bytes_val`, `string_val_as_escaped_bytes`, `function_def_defaults_qual`, `file_data`, `filename`, and `import_aliases` expose the documented current-source view.
- `get_call_arg_value(name)`, `get_call_arg_at_position(index)`, `get_lineno_for_call_arg(name)`, and `check_call_arg_value(name, values=None)` query call arguments.
- `is_module_being_imported(name)`, `is_module_imported_exact(name)`, and `is_module_imported_like(name)` query imports.

Plugin functions **must** return either an `Issue` instance or nothing (`None`) if no problem is found.

## CLI and Configuration

### Invocation
```bash
bandit [options] [target ...]
```
Targets are files or `-` for stdin. Directories are traversed when `--recursive` is set. A directory target supplied without `--recursive` is skipped with a warning; it is not an invocation error. If no files or findings remain, the scan completes with exit code 0.

### Frequently Used Options
- `-r`, `--recursive` - recursively discover and scan matching files under each target directory.
- `-f FORMAT`, `--format FORMAT` - output format (`screen`, `txt`, `csv`, `custom`, `html`, `json`, `sarif`, `xml`, or `yaml`).
- `-o FILE`, `--output FILE` - write report to FILE.
- `-n N`, `--number N` - number of lines of context to show.
- `-t TESTS`, `--tests TESTS` - comma-separated list of test IDs to include. If the option is repeated, the last occurrence supplies the CLI value.
- `-s SKIPS`, `--skip SKIPS` - comma-separated test IDs to skip. If the option is repeated, the last occurrence supplies the CLI value.
- Repeated count flags `-l` or its no-value long form `--level` select LOW, MEDIUM, then HIGH minimum severity; the distinct `--severity-level {all,low,medium,high}` option takes a named value.
- Repeated count flags `-i` or its no-value long form `--confidence` select LOW, MEDIUM, then HIGH minimum confidence; the distinct `--confidence-level {all,low,medium,high}` option takes a named value.
- `-a {file,vuln}`, `--aggregate {file,vuln}` - select filename or vulnerability/test-name ordering or grouping in supported report formats; the default is `file`.
- `-x PATHS`, `--exclude PATHS` - comma-separated path patterns to exclude. Each value is normalized first: if it names an existing directory, that value is replaced by the directory followed by `/*`. A discovered file is then excluded when its scan path matches the normalized value using Unix-style `fnmatch` wildcards or contains that normalized value as a literal substring. Directory normalization replaces the original value; it does not retain the unexpanded directory string as an additional substring rule.
- `--ini INI` - path to an INI-format configuration file.
- `--configfile FILE` - path to a YAML or TOML configuration file.
- `--baseline FILE` - path to a JSON baseline for suppressing known findings.
- `--ignore-nosec` - ignore `# nosec` comments entirely.
- `--exit-zero` - always exit with code 0, even when findings are present.
- `-q`, `--quiet` - only show output for errors and findings.
- `-v`, `--verbose` - display extra information.
- `-d`, `--debug` - emit debug messages.
- `--version` - show version number and exit.

With no severity or confidence option, the minimum for each dimension is `UNDEFINED` (equivalent to the long-option value `all`). One, two, or three short flags select LOW, MEDIUM, or HIGH. More than three repetitions are invalid and must exit nonzero; traceback or diagnostic text is not fixed.

The short/count severity option (`-l`/`--level`) and `--severity-level` are mutually exclusive. The short/count confidence option (`-i`/`--confidence`) and `--confidence-level` are likewise mutually exclusive. Supplying both forms in either pair is an invocation error before scanning.

`--number` controls the maximum code-context lines attached to each issue by report formats that include source context, including the JSON `code` field. Its default is 3. The CLI passes the configured value into issue serialization while producing reports. The library methods' independent `max_lines=3` defaults apply when library callers omit that argument; changing CLI arguments does not mutate the library default.

### Configuration File Loading
- When `--ini` is absent, Bandit performs a configuration-only recursive search of each directory target for `.bandit` before Python file discovery, regardless of whether `--recursive` is set. This config search is independent of the later rule that skips Python-file traversal for directory targets without `--recursive`. Exactly one discovered file is loaded; discovering more than one is an invocation error. File targets do not cause a parent-directory search. The file's `[bandit]` section supports `targets`, `exclude`, `tests`, and `skips`; plugin-specific options belong in an explicitly selected YAML or TOML config.
- `--ini` explicitly selects an INI file.
- `--configfile` selects a YAML or TOML file. When using TOML, the configuration must reside under `[tool.bandit]`.
- INI target paths are used only when no target argument is supplied. Explicit target arguments replace the INI target list.
- `--ini` and `--configfile` are not mutually exclusive. Explicit CLI values override the corresponding INI defaults; an explicit `--configfile` selects the YAML/TOML plugin configuration while non-conflicting INI options still apply.
- YAML/TOML `exclude_dirs` initializes the base exclusion patterns. Bandit then selects one additional exclusion value: explicit CLI `--exclude` if present, otherwise the INI `exclude` value if present. The selected comma-separated patterns extend the base list. Repeating `--exclude` is valid and the last CLI occurrence is the selected value.

### Test List Composition
1. YAML/TOML `tests` and `skips`, when a config file is active, initialize the base profile include and exclude sets. Without such values, the corresponding base set is empty.
2. Separately for includes and skips, Bandit has one CLI/INI option slot: an explicit CLI `--tests` or `--skip` value wins; otherwise the corresponding explicit or automatically loaded INI value occupies that slot; otherwise it is empty. INI is not a second base set. This selection still occurs when a YAML/TOML config is active.
3. IDs from the selected CLI/INI slot extend the corresponding YAML/TOML base set. Thus explicit CLI values replace INI defaults in the slot, while whichever value occupies the slot extends rather than replaces YAML/TOML profile sets.
4. The active tests are the effective include set minus the effective skip set. With no include set, every discovered check not skipped is active.
5. It is an error for a test ID to appear in both effective sets; Bandit must terminate before scanning.

### Baseline Filtering

`--baseline FILE` accepts a JSON report previously produced by Bandit and reads its `results` array as baseline issues. An unreadable baseline file is an invocation error. A baseline may be used only with a formatter marked by `accepts_baseline`; the built-in baseline-aware formats are `custom`, `html`, `json`, `screen`, and `txt`. Using another built-in format (`csv`, `sarif`, `xml`, or `yaml`) is an invocation error that exits nonzero before scanning.

Threshold filtering is applied to current findings before baseline comparison. A current issue matches a baseline issue when their text, severity, CWE, confidence, filename, test name, and test ID are equal; line numbers and column positions are not matching fields. Matching current issues are omitted from the reportable result set. If no baseline issue has a current issue's equality signature, that current issue is unmatched. When two or more current issues share the same unmatched signature, a baseline-aware report may attach all of those current issues as candidates because source movement makes their individual line-based identity unreliable. Baseline JSON `results` entries therefore represent unmatched current issues and retain the normal finding fields; they do not represent stale baseline-only entries. JSON must add a `candidates` list containing all equal current finding objects whenever more than one current issue shares the unmatched signature; it omits the field for a single candidate.

Baseline filtering does not alter metrics: severity/confidence metrics continue to describe all discovered, unsuppressed findings before thresholds and baseline comparison. It does affect the normal finding-based exit status: no unmatched reportable issues yields exit 0, while unmatched issues yield exit 1 unless `--exit-zero` is supplied.

## Scanning and Suppression

- Each target file is parsed as Python source.
- All registered checks (built-in and user-provided) are executed against the AST.
- Lines containing `# nosec` suppress **all** findings that would otherwise be reported on that line.
- The form `# nosec B101,B602` (or test names matching registered IDs) suppresses only the named checks.
- Suppression is per-line and only affects findings whose line number falls on that line.
- The flag `--ignore-nosec` overrides all `# nosec` suppression; findings are reported as if the comments did not exist.
- Files that are syntactically invalid are **not** silently discarded; the parse error is recorded in the `errors` list of the report. A file containing only a syntax error and no reportable findings causes an exit code of 0 because the `results` array is empty. This holds with or without `--exit-zero`; that option additionally forces 0 when findings are present.

## Finding and Report Model

The JSON report produced by Bandit contains four top-level keys:

- `"errors"` - a list of error objects (parse errors, file-access errors, etc.).
- `"generated_at"` - an ISO-8601 timestamp string (variable per invocation).
- `"metrics"` - aggregate statistics for the entire scan and per-file breakdowns.
  - `"_totals"` contains counts of discovered, unsuppressed findings before severity/confidence report thresholds, grouped by severity (`SEVERITY.HIGH`, `.MEDIUM`, `.LOW`, `.UNDEFINED`) and confidence (`CONFIDENCE.HIGH`, `.MEDIUM`, `.LOW`, `.UNDEFINED`). Findings suppressed by an effective `# nosec` are excluded from these severity/confidence counts. The totals also include `loc` (lines of code), `nosec` (blanket suppressions), and `skipped_tests` (named-test suppressions).
  - Per-file entries repeat the same structure under the filename key.
- `"results"` - the reportable finding list after effective `# nosec` suppression, severity/confidence thresholds, and optional baseline matching, with each finding containing:
  - `filename` - path to the scanned file; its absolute or relative prefix is environment-dependent.
  - `test_id` - the stable test ID (e.g., `"B101"`).
  - `test_name` - human-readable name of the check.
  - `issue_severity` - severity string (`"UNDEFINED"`, `"LOW"`, `"MEDIUM"`, `"HIGH"`).
  - `issue_confidence` - confidence string.
  - `issue_text` - human-readable description of the problem.
  - `issue_cwe` - an object representing the CWE mapping. For a non-zero CWE, it contains `id` (int) and `link` (URL string). For CWE 0, it is an empty object `{}`.
  - `line_number` - the line where the issue was found.
  - `line_range` - a list of affected source line numbers.
  - `col_offset`, `end_col_offset` - column positions.
  - `code` - relevant source code snippet (included when requested, e.g., via `with_code` equivalent in JSON output).
  - `more_info` - a documentation URL for the specific test.

## Detection Families
The scoped built-in checks must report the documented ID for these observable source patterns. Issue text must identify the security concern, but exact prose is not fixed by this specification.

| IDs | Observable trigger family |
|---|---|
| B101-B108 | assertions, `exec`, permissive chmod, wildcard bind, hardcoded password values, and hardcoded temporary paths |
| B110, B112, B113 | `except` bodies that only pass/continue and requests/httpx calls without an effective timeout |
| B201, B202 | Flask debug mode and `tarfile.extractall` calls without a demonstrably safe filter |
| B301-B308, B310-B319, B321, B323-B324 | unsafe deserialization, weak cipher/hash use, `mktemp`, `eval`, unsafe marking, risky URL open, non-cryptographic random, Telnet/FTP calls, XML parsing, and unverified SSL contexts |
| B401-B409, B411-B413, B415 | risky imports involving Telnet, FTP, serialization, subprocess, XML/XMLRPC, CGI, PyCrypto, and IPMI |
| B501-B509 | disabled certificate checks, insecure SSL defaults/protocols, weak key sizes, unsafe YAML loading, Paramiko auto-trust, and weak SNMP settings |
| B601-B615 | Paramiko/shell/process/SQL/wildcard injection, Django SQL APIs, insecure logging listeners, bidirectional source controls, unsafe PyTorch loading, and unpinned Hugging Face downloads |
| B701-B704 | unsafe Jinja2/Mako autoescaping and unsafe Django/MarkupSafe marking |

Stable representative ratings are B101 LOW/HIGH, B102 MEDIUM/HIGH, B104 MEDIUM/MEDIUM, B105-B107 LOW/MEDIUM, B108 MEDIUM/MEDIUM, B110 and B112 LOW/HIGH, B201 HIGH/MEDIUM, B301-B303 MEDIUM/HIGH, B404 LOW/HIGH, B501 HIGH/HIGH, B506 MEDIUM/HIGH, B507 HIGH/MEDIUM, B603 LOW/HIGH, B604 MEDIUM/LOW, B606 LOW/MEDIUM, B607 LOW/HIGH, B609 HIGH/MEDIUM, B612 MEDIUM/HIGH, B613 HIGH/MEDIUM, and B614-B615 MEDIUM/HIGH. Ratings not listed here are required to use one of the four public ranking constants, but their exact pair is not fixed by this scoped contract.

## Error Semantics
- **Parse errors** (syntax errors) are collected in the `"errors"` array of the structured output. They are **not** treated as findings.
- If a scan yields no reportable findings after thresholds and optional baseline filtering (i.e., the `"results"` array is empty), Bandit exits with code `0`, regardless of the presence of parse errors.
- If at least one reportable finding is present in `"results"`, Bandit normally exits with code `1`.
- The `--exit-zero` flag overrides the above: the tool always exits with code `0`, even when findings exist.
- Configuration and invocation errors, including overlapping include/skip sets, must produce a non-zero exit before a successful scan report is completed. Exact diagnostic wording is not fixed.

## Cross-View Invariants
The following statements **must** hold for any valid Bandit scan, whether observed through the CLI, JSON output, or library calls.

1. **Exit code without `--exit-zero`**  
   Unless `--exit-zero` is supplied, the process exit code must be `0` if and only if the post-threshold, post-baseline reportable set is empty, which is the same condition as an empty `"results"` array. Syntax-error-only files do not change this condition.

2. **Suppression fidelity**  
   For every source comment containing bare `# nosec` when `--ignore-nosec` is not set, **no** finding from that line must appear in output. When specific test IDs are listed (e.g., `# nosec B101`), only those checks are suppressed; other applicable checks on the same line must still report findings.

3. **CWE link correctness**  
   If a finding carries a non-zero CWE ID, the `issue_cwe.link` field must be `https://cwe.mitre.org/data/definitions/<id>.html`. If the CWE ID is `0`, the `issue_cwe` field must be an empty object (`{}`).

4. **Include/skip disjointness**  
   After merging command-line and configuration-provided include and skip lists, the intersection of the two sets must be empty. If any test ID appears in both, Bandit must raise an error and terminate before scanning.

5. **Test ID stability**  
   Every `test_id` present in a finding must exactly match an ID registered by a built-in or user-provided plugin. The built-in IDs are those listed in the Detection Families section.

6. **Metrics consistency**  
   Severity and confidence counts in `metrics._totals` must describe discovered, unsuppressed findings before report thresholds. Each item in `results` is represented in matching metric categories, but not every metric-counted finding must remain in `results`. Metric totals can exceed the result count when severity or confidence thresholds hide findings or baseline filtering removes matched findings.

## Representative Workflows

1. **Basic directory scan with JSON output**  
   ```bash
   bandit -r my_project/ -f json -o report.json
   ```
   Recursively scans `my_project`, outputs a JSON report to `report.json`, exits 0 if no findings.

2. **Filter by severity and use exit-zero for CI**  
   ```bash
   bandit -r src/ --severity-level medium --exit-zero
   ```
   Reports only issues of MEDIUM severity or higher, always exits 0.

3. **Exclude tests and ignore `nosec`**  
   ```bash
   bandit -r . -s B101,B603 --ignore-nosec
   ```
   Skips `B101` and `B603`, and overrides any `# nosec` comments, reporting all findings.

4. **Combine config file and CLI test lists**  
   With a YAML config containing `tests: [B101, B102]` and `skips: [B201]`, and CLI `-t B301 -s B603`, the effective include set is `{B101,B102,B301}` and the effective skip set is `{B201,B603}`. Supplying the same ID in both sets is an error rather than a subtraction shortcut. For INI, explicit CLI `-t` and `-s` replace the corresponding INI values before profile composition.

5. **Suppress specific checks inline**  
   ```python
   password = "secret"  # nosec B105
   eval(user_input)     # nosec
   ```
   The `# nosec B105` on the first line suppresses B105 but not a different applicable check on that line. The bare `# nosec` on the second line suppresses all findings on that line.

6. **Scan from stdin**  
   ```bash
   cat snippet.py | bandit -
   ```
   Reads code from standard input and checks it.

## Non-Goals
The following are **explicitly out of scope** for this specification:

- Internal implementation details: manager, visitor, AST traversal, plugin loader, Stevedore integration.
- Storage format for extension managers.
- Exact text of error or warning messages.
- The exact whitespace, template strings, absolute file system paths, or generated timestamps appearing in output.
- Behaviour of third-party plugin repositories or services.
- Performance or scalability guarantees.
- Any configuration merge logic beyond what is described in the CLI and Configuration section.

## Evaluation Notes
Compatibility tests exercise Bandit's public behavior by:

- Exercising each detection family with both positive and negative test cases, checking that the expected severity/confidence pair is emitted (where deterministic) and that the CWE link is correct.
- Confirming that `# nosec` comments (bare and with a list) suppress the correct checks, and that `--ignore-nosec` disables all suppression.
- Testing exit codes: zero findings -> 0; one or more findings -> 1; `--exit-zero` -> always 0, even with findings; syntax-error-only scans -> 0.
- Inspecting a generated JSON report to ensure the top-level keys are present, results obey thresholds, and metrics retain the pre-threshold discovered counts.
- Using the public Python API to construct, filter, serialise, and deserialise `Issue` and `Cwe` objects, verifying the documented ranking and methods.
- Providing configuration files with overlapping include/skip sets and asserting that Bandit raises an error.
- Scanning a directory while excluding patterns and verifying that only matching files are covered.

These checks use temporary source trees and public interfaces only. They do not require network services or third-party plugin repositories.
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
    assert expected_id in result_ids(report)


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
    assert report["results"][0]["filename"] == "<stdin>"
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
# Bandit Oracle Spec-Test Map

oracle_source: merged_public_rewrite_and_generated

| test_nodeid | source | layer | spec_section | status | notes |
|---|---|---|---|---|---|
| `filter/rewritten_upstream_tests.py::test_issue_constructor_and_public_attributes` | upstream_rewrite | atomic | Public API - Issue | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_issue_as_dict_without_code` | upstream_rewrite | atomic | Public API - Issue | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_issue_filter_severity_ranking` | upstream_rewrite | atomic | Public API - Issue; Public API - Constants | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_issue_filter_confidence_ranking` | upstream_rewrite | atomic | Public API - Issue; Public API - Constants | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_issue_equality_fields_and_location_independence` | upstream_rewrite | atomic | Public API - Issue | covered | public observable assertion; reference and dummy gated |
| `filter/rewritten_upstream_tests.py::test_issue_get_code_from_public_filename` | upstream_rewrite | atomic | Public API - Issue | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_ranking_constants_are_strings` | generated | atomic | Public API - Constants | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_cwe_dictionary_and_link[0]` | generated | atomic | Public API - Cwe; Cross-View Invariants - CWE link correctness | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_cwe_dictionary_and_link[79]` | generated | atomic | Public API - Cwe; Cross-View Invariants - CWE link correctness | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_cwe_dictionary_and_link[605]` | generated | atomic | Public API - Cwe; Cross-View Invariants - CWE link correctness | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_cwe_from_dict_mutates_and_returns_none` | generated | atomic | Public API - Cwe; Cross-View Invariants - CWE link correctness | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_cwe_string_and_json_string` | generated | atomic | Public API - Cwe; Cross-View Invariants - CWE link correctness | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_issue_filter_uses_both_rankings[HIGH-HIGH-MEDIUM-MEDIUM-True]` | generated | atomic | Public API - Issue; Public API - Constants | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_issue_filter_uses_both_rankings[LOW-HIGH-MEDIUM-LOW-False]` | generated | atomic | Public API - Issue; Public API - Constants | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_issue_filter_uses_both_rankings[HIGH-LOW-LOW-MEDIUM-False]` | generated | atomic | Public API - Issue; Public API - Constants | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_issue_filter_uses_both_rankings[UNDEFINED-UNDEFINED-UNDEFINED-UNDEFINED-True]` | generated | atomic | Public API - Issue; Public API - Constants | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_issue_as_dict_schema_without_code` | generated | atomic | Public API - Issue | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_issue_from_dict_mutates_and_defaults_columns` | generated | atomic | Public API - Issue | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_issue_equality_ignores_location_but_not_identity_fields` | generated | atomic | Public API - Issue | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_issue_get_code_respects_line_limit` | generated | atomic | Public API - Issue | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_public_decorators_preserve_callable_behavior[checks-args0]` | generated | atomic | Public API - Decorators | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_public_decorators_preserve_callable_behavior[test_id-args1]` | generated | atomic | Public API - Decorators | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_public_decorators_preserve_callable_behavior[takes_config-args2]` | generated | atomic | Public API - Decorators | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_public_decorators_preserve_callable_behavior[accepts_baseline-args3]` | generated | atomic | Public API - Decorators | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B101]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B102]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B103]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B104]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B105]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B106]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B107]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B108]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B110]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B112]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B113]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B201]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B202]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B301]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B307]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B310]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B311]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B312]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B323]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B324]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B401]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B403]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B404]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B405]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B415]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B501]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B506]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B507]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B602]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B603]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B605]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B607]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B608]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B609]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B612]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B614]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B615]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B701]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B703]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_detection_family_reports_expected_id[B704]` | generated | atomic | Detection Families; Scanning and Suppression | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_clean_scan_has_empty_results_and_zero_exit` | generated | integration | Finding and Report Model; Error Semantics; CLI and Configuration - Invocation; Representative Workflows | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_finding_scan_has_one_exit_and_exit_zero_override` | generated | integration | Error Semantics; Cross-View Invariants - Exit code; Product State Model; Representative Workflows | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_syntax_error_is_reported_but_not_a_finding` | generated | integration | Error Semantics; Finding and Report Model | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_stdin_scan_uses_same_json_projection` | generated | integration | CLI and Configuration - Invocation; Representative Workflows | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_directory_requires_recursive_flag_for_python_files` | generated | system_e2e | CLI and Configuration - Invocation; Product State Model; Representative Workflows | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_recursive_exclusion_removes_matching_subtree` | generated | system_e2e | CLI and Configuration - Frequently Used Options; Representative Workflows | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_bare_nosec_and_ignore_nosec` | generated | system_e2e | Scanning and Suppression; Cross-View Invariants - Suppression fidelity; Product State Model | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_named_nosec_suppresses_only_named_check` | generated | system_e2e | Scanning and Suppression; Cross-View Invariants - Suppression fidelity; Product State Model | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_threshold_filters_results_but_not_metrics` | generated | system_e2e | Finding and Report Model; Cross-View Invariants - Metrics consistency; Product State Model | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_overlapping_include_and_skip_is_invocation_error` | generated | integration | CLI and Configuration - Test List Composition; Error Semantics | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_repeated_tests_option_uses_last_value` | generated | integration | CLI and Configuration - Frequently Used Options; CLI and Configuration - Test List Composition | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_ini_defaults_are_replaced_by_explicit_cli_tests` | generated | system_e2e | CLI and Configuration - Configuration File Loading; CLI and Configuration - Test List Composition; Representative Workflows | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_ini_targets_apply_when_cli_target_is_absent` | generated | integration | CLI and Configuration - Configuration File Loading; CLI and Configuration - Test List Composition; Representative Workflows | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_yaml_profile_is_extended_by_selected_cli_tests` | generated | system_e2e | CLI and Configuration - Configuration File Loading; CLI and Configuration - Test List Composition; Representative Workflows | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_number_controls_json_code_context` | generated | integration | CLI and Configuration - Frequently Used Options; Finding and Report Model | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_supported_report_formats_emit_findings[csv]` | generated | integration | Installable Surface; Finding and Report Model | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_supported_report_formats_emit_findings[yaml]` | generated | integration | Installable Surface; Finding and Report Model | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_supported_report_formats_emit_findings[xml]` | generated | integration | Installable Surface; Finding and Report Model | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_supported_report_formats_emit_findings[sarif]` | generated | integration | Installable Surface; Finding and Report Model | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_supported_report_formats_emit_findings[txt]` | generated | integration | Installable Surface; Finding and Report Model | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_output_file_receives_json_report` | generated | integration | CLI and Configuration - Frequently Used Options; Finding and Report Model | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_aggregate_mode_changes_result_order` | generated | system_e2e | CLI and Configuration - Frequently Used Options; Finding and Report Model | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_baseline_removes_matching_finding_and_changes_exit` | generated | system_e2e | CLI and Configuration - Baseline Filtering; Cross-View Invariants - Metrics consistency; Product State Model; Representative Workflows | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_baseline_json_candidates_for_duplicate_new_signature` | generated | system_e2e | CLI and Configuration - Baseline Filtering; Cross-View Invariants - Metrics consistency; Product State Model; Representative Workflows | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_non_baseline_aware_format_is_invocation_error` | generated | system_e2e | CLI and Configuration - Baseline Filtering; Cross-View Invariants - Metrics consistency; Product State Model; Representative Workflows | covered | public observable assertion; reference and dummy gated |
| `filter/generated_tests.py::test_json_result_cwe_link_and_location_fields` | generated | atomic | Public API - Cwe; Cross-View Invariants - CWE link correctness | covered | public observable assertion; reference and dummy gated |

Total: 90 | kept (covered): 90 | spec_gap: 0 | source-only: 0 | excluded: 0 | final scoreable: 90
{"layer": "system_e2e", "taxonomy_key": "generated_tests::test_aggregate_mode_changes_result_order"}
{"layer": "system_e2e", "taxonomy_key": "generated_tests::test_bare_nosec_and_ignore_nosec"}
{"layer": "system_e2e", "taxonomy_key": "generated_tests::test_baseline_json_candidates_for_duplicate_new_signature"}
{"layer": "system_e2e", "taxonomy_key": "generated_tests::test_baseline_removes_matching_finding_and_changes_exit"}
{"layer": "integration", "taxonomy_key": "generated_tests::test_clean_scan_has_empty_results_and_zero_exit"}
{"layer": "atomic", "taxonomy_key": "generated_tests::test_cwe_dictionary_and_link"}
{"layer": "atomic", "taxonomy_key": "generated_tests::test_cwe_from_dict_mutates_and_returns_none"}
{"layer": "atomic", "taxonomy_key": "generated_tests::test_cwe_string_and_json_string"}
{"layer": "atomic", "taxonomy_key": "generated_tests::test_detection_family_reports_expected_id"}
{"layer": "system_e2e", "taxonomy_key": "generated_tests::test_directory_requires_recursive_flag_for_python_files"}
{"layer": "integration", "taxonomy_key": "generated_tests::test_finding_scan_has_one_exit_and_exit_zero_override"}
{"layer": "system_e2e", "taxonomy_key": "generated_tests::test_ini_defaults_are_replaced_by_explicit_cli_tests"}
{"layer": "integration", "taxonomy_key": "generated_tests::test_ini_targets_apply_when_cli_target_is_absent"}
{"layer": "atomic", "taxonomy_key": "generated_tests::test_issue_as_dict_schema_without_code"}
{"layer": "atomic", "taxonomy_key": "generated_tests::test_issue_equality_ignores_location_but_not_identity_fields"}
{"layer": "atomic", "taxonomy_key": "generated_tests::test_issue_filter_uses_both_rankings"}
{"layer": "atomic", "taxonomy_key": "generated_tests::test_issue_from_dict_mutates_and_defaults_columns"}
{"layer": "atomic", "taxonomy_key": "generated_tests::test_issue_get_code_respects_line_limit"}
{"layer": "atomic", "taxonomy_key": "generated_tests::test_json_result_cwe_link_and_location_fields"}
{"layer": "system_e2e", "taxonomy_key": "generated_tests::test_named_nosec_suppresses_only_named_check"}
{"layer": "system_e2e", "taxonomy_key": "generated_tests::test_non_baseline_aware_format_is_invocation_error"}
{"layer": "integration", "taxonomy_key": "generated_tests::test_number_controls_json_code_context"}
{"layer": "integration", "taxonomy_key": "generated_tests::test_output_file_receives_json_report"}
{"layer": "integration", "taxonomy_key": "generated_tests::test_overlapping_include_and_skip_is_invocation_error"}
{"layer": "atomic", "taxonomy_key": "generated_tests::test_public_decorators_preserve_callable_behavior"}
{"layer": "atomic", "taxonomy_key": "generated_tests::test_ranking_constants_are_strings"}
{"layer": "system_e2e", "taxonomy_key": "generated_tests::test_recursive_exclusion_removes_matching_subtree"}
{"layer": "integration", "taxonomy_key": "generated_tests::test_repeated_tests_option_uses_last_value"}
{"layer": "integration", "taxonomy_key": "generated_tests::test_stdin_scan_uses_same_json_projection"}
{"layer": "integration", "taxonomy_key": "generated_tests::test_supported_report_formats_emit_findings"}
{"layer": "integration", "taxonomy_key": "generated_tests::test_syntax_error_is_reported_but_not_a_finding"}
{"layer": "system_e2e", "taxonomy_key": "generated_tests::test_threshold_filters_results_but_not_metrics"}
{"layer": "system_e2e", "taxonomy_key": "generated_tests::test_yaml_profile_is_extended_by_selected_cli_tests"}
{"layer": "atomic", "taxonomy_key": "rewritten_upstream_tests::test_issue_as_dict_without_code"}
{"layer": "atomic", "taxonomy_key": "rewritten_upstream_tests::test_issue_constructor_and_public_attributes"}
{"layer": "atomic", "taxonomy_key": "rewritten_upstream_tests::test_issue_equality_fields_and_location_independence"}
{"layer": "atomic", "taxonomy_key": "rewritten_upstream_tests::test_issue_filter_confidence_ranking"}
{"layer": "atomic", "taxonomy_key": "rewritten_upstream_tests::test_issue_filter_severity_ranking"}
{"layer": "atomic", "taxonomy_key": "rewritten_upstream_tests::test_issue_get_code_from_public_filename"}
# Bandit Oracle Coverage Quota

Total scoreable nodeids: 90 (global floor: 50)

## Taxonomy

- atomic: 65
- integration: 14
- system_e2e: 11

## Spec Behavior Coverage

- CLI and Configuration - Baseline Filtering: 3
- CLI and Configuration - Configuration File Loading: 3
- CLI and Configuration - Frequently Used Options: 5
- CLI and Configuration - Invocation: 3
- CLI and Configuration - Test List Composition: 5
- Cross-View Invariants - CWE link correctness: 6
- Cross-View Invariants - Exit code: 1
- Cross-View Invariants - Metrics consistency: 4
- Cross-View Invariants - Suppression fidelity: 2
- Detection Families: 40
- Error Semantics: 4
- Finding and Report Model: 11
- Installable Surface: 5
- Product State Model: 8
- Public API - Constants: 7
- Public API - Cwe: 6
- Public API - Decorators: 4
- Public API - Issue: 14
- Representative Workflows: 11
- Scanning and Suppression: 42

Non-behavioral framing sections (Scope, Non-Goals, Evaluation Notes) do not receive standalone tests. Plugin Context is exercised indirectly by the scanner detection families; its raw constructor shape is intentionally not asserted.
# Bandit Filter Notes

## Oracle Composition

- Upstream public rewrites: 6 nodeids from `Issue` behavior.
- Generated public oracle: 84 nodeids.
- Final scoreable oracle: 90 nodeids.
- Reference gate: 100% pass.
- Dummy gate: 0% pass (all 90 tests failed the NotImplemented dummy).

## Filtering Decision

The upstream suite is saturated with bidirectional `bandit.core` manager, config,
metrics, formatter, extension-loader, source-tree fixture, and exact-output dependencies.
`filter/rewrite_audit.md` and `filter/candidate_filter_map.md` account for all 24 files
and 264 test functions. Six `Issue` tests were safely rewritten through top-level public
imports; Track B supplies the remaining behavior coverage.

## Fairness Boundaries

- No private import or private assertion is scoreable.
- No exact human diagnostic wording is scoreable.
- Detection assertions require public test IDs, not exact issue prose.
- Variable timestamps and path prefixes are not exact-matched.
- CLI tests use `python -m bandit` so candidate provenance can be isolated.
# Bandit Stage 3 Gate Summary

Date: 2026-07-12 UTC

- Oracle source: six rewritten public upstream tests plus generated public tests.
- Collected scoreable nodeids: 90.
- Reference direct run: 90 passed, 0 failed.
- Official grouped scorer: 90 passed, 0 failed, pass rate 1.0.
- Taxonomy: 65 atomic, 14 integration, 11 system_e2e, 0 unknown.
- Dummy gate: 90 failed, 0 passed.
- Official scorer isolation: `--remove-path bandit`.
- Import provenance: `/root/autodl-tmp/new-e2e/PyCQA__bandit/bandit/__init__.py`.
- Public-import scan of scoreable files: no `bandit.core`, `bandit.cli`, or `bandit.formatters` imports.
- Global oracle floor: 90 >= 50.
- Branch coverage artifacts: `filter/coverage.json` and `filter/coverage_gaps.txt`.
- Variable timestamps, absolute path prefixes, exact human diagnostic prose, private fields, manager/visitor state, and extension-loader shapes are not asserted.

The first official scorer attempt was invalid before test execution because its run directory was nested under the source copy. The valid result above used the minimal `filter/oracle_source` and external run directory `/root/autodl-tmp/Bmk-Lizhiqian/scorer-runs/bandit-reference-v1`.
