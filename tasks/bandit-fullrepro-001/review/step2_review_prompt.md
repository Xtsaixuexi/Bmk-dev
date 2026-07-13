# Independent Stage 2 Review: Bandit

Review only the candidate-visible specification appended below. Do not browse, use tools, inspect a repository, infer hidden tests, or import behavior from another Bandit revision. Treat explicit version-specific public facts in the artifact as the contract unless they contradict another statement in the artifact.

Report a mandatory blocker only when you can quote the exact defective text and explain a concrete internal contradiction, missing behavior required by the stated scope, candidate leak, or impossible API contract. Do not report characters, words, or corruption that are not visibly present in the appended artifact.

Check:

- public names, signatures, mutation, serialization, and ranking semantics;
- CLI syntax, precedence, suppression, baseline, exit status, and report/metric relationships;
- detection families and stable ratings;
- consistency among scope, workflows, invariants, evaluation notes, and non-goals;
- candidate safety and absence of implementation-only or hidden-fixture leakage.

Return only:

- `VERDICT`: PASS_CONTINUE or PATCH_REQUIRED
- `FACTUAL_ACCURACY`: PASS or FAIL
- `PUBLIC_TRACEABILITY`: PASS or FAIL
- `CANDIDATE_SAFETY`: PASS or FAIL
- `BEHAVIORAL_COMPLETENESS`: PASS or FAIL
- `STATE_MODEL_AND_INVARIANTS`: PASS or FAIL
- `BLOCKERS`: mandatory corrections with exact section and replacement behavior; empty for PASS_CONTINUE

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
