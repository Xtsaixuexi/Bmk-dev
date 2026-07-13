# Bandit Public Reference Probes

Generated: 2026-07-10 UTC

- Clean Python file: exit 0; JSON `errors=[]`; JSON `results=[]`.
- File importing subprocess, using assert, and calling `subprocess.Popen(..., shell=True)`: exit 1; findings B404 LOW/HIGH, B101 LOW/HIGH, and B602 HIGH/HIGH.
- `# nosec B101` suppresses B101 only; bare `# nosec` suppresses all findings on its line; unrelated import findings remain and retain exit 1.
- Syntax-error-only file: exit 0; JSON `results=[]`; JSON `errors` contains the filename and parse-error reason.
- JSON top-level keys: `errors`, `generated_at`, `metrics`, `results`.
- JSON result keys observed: `code`, `col_offset`, `end_col_offset`, `filename`, `issue_confidence`, `issue_cwe`, `issue_severity`, `issue_text`, `line_number`, `line_range`, `more_info`, `test_id`, `test_name`.
- With `--severity-level high`, the result list retained only the HIGH finding while metrics still counted the LOW findings discovered in the same file. Metrics are therefore pre-threshold counts, not a histogram of the filtered result list.
- Supplying B101 in both `--tests` and `--skip` exited 2 before scanning and reported a non-exclusive include/exclude set.
- With no explicit targets, `--ini options.ini` used its target list. An explicit target replaced the INI target.
- Explicit CLI `--tests B602` replaced the INI `tests=B101`; the INI skip list still applied because CLI did not replace it.
- Supplying both `--ini` and `--configfile` was valid. The YAML include B602 combined with the INI include B101 and produced both findings.
- INI `number=1` limited each JSON `code` snippet to one source line. The CLI default is 3.
- No threshold option maps to `UNDEFINED/all`. Four repeated `-l` flags exited nonzero; traceback text is not contractual.
- The short/count and named severity forms are mutually exclusive, as are the corresponding confidence forms.
- Repeating `-t` is valid and the last occurrence controls the CLI include value (`-t B101 -t B602` selected only B602 in the CLI layer).
- A sole directory target without `-r` was warned about and skipped; the resulting empty JSON scan exited 0.

Probe fixtures are stored under `new-work/parallel-results/lane-1/bandit-stage2-probes/`. Variable timestamps, environment-specific absolute paths, and internal diagnostic wording are not contractual.
