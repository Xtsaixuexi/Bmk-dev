# Bandit Public Surface Audit

## Scope Decision

The candidate contract covers Bandit's documented command-line scanner, configuration and suppression behavior, structured findings and report projections, and plugin-author API. Internal manager orchestration, raw extension-loader registries, meta-AST storage, visitor/tester implementation, and formatter helper internals are excluded.

## Installable Surface

- Console commands: `bandit`, `bandit-config-generator`, and `bandit-baseline`.
- Module command: `python -m bandit`.
- Top-level plugin imports: `bandit.Issue`, `bandit.Cwe`, `bandit.checks`, `bandit.takes_config`, `bandit.test_id`, `bandit.accepts_baseline`, `bandit.UNDEFINED`, `bandit.LOW`, `bandit.MEDIUM`, and `bandit.HIGH`.
- Context type available to plugins as `bandit.context.Context`.

## Public Object Signatures

```python
Issue(
    severity,
    cwe=0,
    confidence="UNDEFINED",
    text="",
    ident=None,
    lineno=None,
    test_id="",
    col_offset=-1,
    end_col_offset=0,
)

Issue.filter(severity, confidence)
Issue.get_code(max_lines=3, tabbed=False)
Issue.as_dict(with_code=True, max_lines=3)
Issue.from_dict(data, with_code=True)

Cwe(id=0)
Cwe.link()
Cwe.as_dict()
Cwe.as_jsons()
Cwe.from_dict(data)

checks(*node_types)
takes_config(function_or_name)
test_id(id_value)
accepts_baseline(formatter)
```

The ranking order is `UNDEFINED < LOW < MEDIUM < HIGH`. `Issue.filter()` returns true only when both the issue severity and confidence meet or exceed the requested thresholds.

Plugin contexts expose `call_args`, `call_args_count`, `call_function_name`, `call_function_name_qual`, `call_keywords`, `node`, `statement`, `string_val`, `bytes_val`, `string_val_as_escaped_bytes`, `function_def_defaults_qual`, `file_data`, `filename`, `import_aliases`, `get_call_arg_value(name)`, `get_call_arg_at_position(index)`, `get_lineno_for_call_arg(name)`, `check_call_arg_value(name, values=None)`, `is_module_being_imported(name)`, `is_module_imported_exact(name)`, and `is_module_imported_like(name)`.

## CLI Surface

The scanner accepts files, directories with `--recursive`, and `-` for standard input. Public options include config/profile selection, test include/skip IDs, severity and confidence thresholds, context line count, file/vulnerability aggregation, report format, custom message templates, output file, exclusions, baseline, INI path, `--ignore-nosec`, `--exit-zero`, quiet/verbose/debug modes, and version.

Supported report format names are `csv`, `custom`, `html`, `json`, `sarif`, `screen`, `txt`, `xml`, and `yaml`. JSON baselines are accepted by `--baseline`.

## Configuration and Suppression

- Recursive scans automatically consider a `.bandit` INI file with a `[bandit]` section.
- `--ini` explicitly selects an INI file.
- `--configfile` selects YAML or TOML; TOML settings live under `[tool.bandit]`.
- Config supports `targets`, include `tests`, `skips`, and exclusions; plugin-specific sections override plugin defaults.
- YAML/TOML profile `tests`/`skips` are extended by selected CLI or INI test values.
- Explicit CLI `--tests`/`--skip` values replace corresponding INI defaults; INI values apply when the CLI value is absent.
- Explicit CLI targets replace INI targets; INI targets are used when no target argument is supplied.
- `--ini` and `--configfile` are usable together. Explicit CLI options override INI defaults, while the YAML/TOML file supplies plugin/profile configuration.
- When both include and skip sets are present, only included tests not in the skip set run. The same ID in both sets is an error.
- `# nosec` suppresses all findings associated with that line. `# nosec B101,B602` and full test names suppress only the named checks. `--ignore-nosec` disables suppression.

## Structured Finding Projection

JSON output has top-level `errors`, `generated_at`, `metrics`, and `results`. Each result exposes filename, test name/ID, issue severity/confidence/text/CWE, line number/range, column offsets, code context, and documentation link. Metrics contain per-file and `_totals` counts by severity/confidence plus LOC, nosec, and skipped-test counts.

Reference probes establish:

- no findings: exit 0 and an empty `results` list;
- reportable findings: exit 1 unless `--exit-zero` is used;
- a syntax-error-only file: exit 0, no findings, and an entry in `errors`;
- `# nosec` changes nosec/skipped metrics and suppresses only the affected line/checks;
- severity/confidence thresholds filter `results`, while metrics retain counts for discovered unsuppressed findings before those thresholds;
- default thresholds are `UNDEFINED/all`; one to three short `-l`/`-i` repetitions select LOW through HIGH, and additional repetitions fail nonzero;
- `--number` defaults to 3 and controls report code-context length;
- timestamps and absolute path prefixes are variable and must not be exact-match evaluation targets.

## Detection Families In Scope

The contract includes representative documented checks across all plugin families:

| IDs | Observable trigger family |
|---|---|
| B101-B108 | assertions, `exec`, permissive chmod, wildcard bind, hardcoded passwords, hardcoded temporary paths |
| B110, B112, B113 | swallowed exceptions and HTTP requests without an effective timeout |
| B201, B202 | Flask debug mode and unsafe tar extraction |
| B301-B307, B310-B312, B323-B324 | unsafe deserialization, weak crypto/hash/cipher use, `mktemp`, `eval`, risky URL open, non-cryptographic random, Telnet, unverified SSL contexts |
| B401-B409, B411-B415 | risky imports for Telnet/FTP/pickle/subprocess/XML/XMLRPC/CGI/PyCrypto/IPMI |
| B501-B509 | disabled certificate checks, insecure SSL defaults/protocols, weak key sizes, unsafe YAML, Paramiko host-key trust, and weak SNMP |
| B601-B615 | shell/process/SQL/wildcard injection, Django SQL APIs, insecure logging listener, bidirectional source controls, unsafe PyTorch loading, and unpinned Hugging Face downloads |
| B701-B704 | Jinja2/Mako autoescaping and unsafe Django/MarkupSafe marking |

Representative stable ratings include B101 LOW/HIGH, B102 MEDIUM/HIGH, B104 MEDIUM/MEDIUM, B105-B107 LOW/MEDIUM, B108 MEDIUM/MEDIUM, B110 and B112 LOW/HIGH, B201 HIGH/MEDIUM, B301-B303 MEDIUM/HIGH, B404 LOW/HIGH, B501 HIGH/HIGH, B506 MEDIUM/HIGH, B507 HIGH/MEDIUM, B603 LOW/HIGH, B604 MEDIUM/LOW, B606 LOW/MEDIUM, B607 LOW/HIGH, B609 HIGH/MEDIUM, B612 MEDIUM/HIGH, B613 HIGH/MEDIUM, B614-B615 MEDIUM/HIGH, and B701-B704 as documented by each check. Some checks vary severity/confidence based on whether the argument is a literal or can be statically determined.

## Excluded Surfaces

- Private visitor, AST-map, manager, metrics-storage, extension-loader, and tester internals.
- Exact internal exception messages and logger diagnostics.
- Exact report whitespace, HTML templates, timestamps, absolute prefixes, or dictionary ordering beyond a format's documented schema.
- Third-party plugin discovery implementation and Stevedore object shapes.
- SARIF implementation internals beyond valid public report production.
