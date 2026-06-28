# MiniDotenv Unit/System Requirement Map

Date: 2026-06-28

Public packet: `prd.md`
Rubric: `rubric.json`

Current rubric size: 30 executable cases, including 12 unit cases and 18 system cases.

## Public Requirements

| ID | Capability | Public packet section | Observable behavior |
| --- | --- | --- | --- |
| `REQ-api-shape` | Public functions | Public API | Required functions are importable from `minidotenv.py` |
| `REQ-source-selection` | File and stream inputs | Input Sources | `dotenv_path` takes precedence over `stream`; missing sources are handled safely |
| `REQ-parse-basic` | Basic bindings | Dotenv File Format | `KEY=value`, `KEY=`, and bare `KEY` parse to expected values |
| `REQ-parse-comments-export` | Comments and export prefix | Dotenv File Format | Empty lines, comments, inline comments, and `export` are handled |
| `REQ-key-validation` | Key syntax | Dotenv File Format, Error Behavior | Invalid keys are skipped or rejected without corrupting state |
| `REQ-quote-single` | Single-quoted values | Values, Quotes, And Comments | Single quotes preserve literal text and supported escapes |
| `REQ-quote-double` | Double-quoted values | Values, Quotes, And Comments | Double quotes decode supported escapes |
| `REQ-inline-comments` | Inline comments | Values, Quotes, And Comments | Unquoted values stop before whitespace-introduced comments |
| `REQ-interpolate-basic` | `${NAME}` interpolation | Variable Interpolation | Values can reference earlier bindings or environment values |
| `REQ-interpolate-default` | `${NAME:-default}` interpolation | Variable Interpolation | Defaults are used for undefined variables |
| `REQ-interpolate-order` | Forward-reference behavior | Variable Interpolation | Variables only see earlier file bindings, not later bindings |
| `REQ-load-no-override` | Preserve existing environment | Environment Loading | `load_dotenv(..., override=False)` does not replace existing environment keys |
| `REQ-load-override` | Override existing environment | Environment Loading | `load_dotenv(..., override=True)` replaces existing environment keys |
| `REQ-load-none-skip` | Skip `None` values | Environment Loading | Bare keys are not written to `os.environ` |
| `REQ-find-dotenv` | Upward path discovery | Path Discovery | `find_dotenv` searches current and parent directories |
| `REQ-get-key` | Read one key | File Mutation Helpers | `get_key` returns a parsed value without modifying the file |
| `REQ-set-key` | Add or replace one key | File Mutation Helpers | `set_key` updates or appends a binding deterministically |
| `REQ-unset-key` | Remove one key | File Mutation Helpers | `unset_key` removes a binding and preserves unrelated lines |
| `REQ-mutation-atomicity` | Failed mutation recovery | File Mutation Helpers, Error Behavior | Failed mutations do not partially rewrite the file |
| `REQ-malformed-recovery` | Malformed-line recovery | Error Behavior And Recovery | Malformed lines do not stop later valid bindings |
| `REQ-no-state-leak` | Repeated-call isolation | Global Invariants | Parsing/loading one source does not leak hidden state into later calls |
| `REQ-unit-eval` | Unit testing definition | Evaluation Style | Unit cases test one feature module at a time |
| `REQ-system-eval` | System testing definition | Evaluation Style | System cases combine parser, interpolation, env state, discovery, mutation, and recovery |

## Unit Coverage

| Test | Feature | Requirement refs | Public basis |
| --- | --- | --- | --- |
| `MDU001` | API shape | `REQ-api-shape` | Required functions are importable and callable |
| `MDU002` | source selection | `REQ-source-selection`, `REQ-parse-basic` | `dotenv_path` takes precedence over `stream` |
| `MDU003` | basic parsing | `REQ-parse-basic` | String, empty string, and bare `None` bindings |
| `MDU004` | comments/export | `REQ-parse-comments-export`, `REQ-inline-comments` | Comments, blank lines, export prefix, inline comments |
| `MDU005` | quotes | `REQ-quote-single`, `REQ-quote-double` | Quote removal and supported escapes |
| `MDU006` | interpolation | `REQ-interpolate-basic`, `REQ-interpolate-default` | Earlier bindings and default values expand |
| `MDU007` | interpolation order | `REQ-interpolate-order` | Later bindings are not visible to earlier lines |
| `MDU008` | environment loading | `REQ-load-no-override`, `REQ-load-override`, `REQ-load-none-skip` | Override modes and bare-key skipping |
| `MDU009` | path discovery | `REQ-find-dotenv` | Upward `.env` search from nested cwd |
| `MDU010` | mutation helpers | `REQ-get-key`, `REQ-set-key`, `REQ-unset-key` | Set, get, unset one file |
| `MDU011` | replacement | `REQ-set-key` | Replace first matching key without duplication |
| `MDU012` | malformed recovery | `REQ-malformed-recovery`, `REQ-key-validation` | Bad lines do not block later valid lines |

## System Coverage

| Test | system_dimension | Crossed modules | Requirement refs | Public basis |
| --- | --- | --- | --- | --- |
| `MDS001` | `cross_feature_dataflow` | parse -> interpolate -> load | `REQ-parse-basic`, `REQ-interpolate-basic`, `REQ-load-override` | Parsed bindings feed interpolation and environment loading |
| `MDS002` | `state_accumulation` | set -> load -> get | `REQ-set-key`, `REQ-get-key`, `REQ-load-override` | File mutation affects later parse/load results |
| `MDS003` | `global_invariant` | values -> env check -> load | `REQ-source-selection`, `REQ-no-state-leak`, `REQ-load-override` | Read-only parsing and loading stay distinct |
| `MDS004` | `error_atomicity` | invalid set -> unchanged parse | `REQ-key-validation`, `REQ-mutation-atomicity`, `REQ-parse-basic` | Failed mutation does not corrupt file state |
| `MDS005` | `operation_order_sensitivity` | env/file conflict -> override mode | `REQ-interpolate-basic`, `REQ-load-no-override`, `REQ-load-override` | Override mode changes interpolation and final env |
| `MDS006` | `boundary_crossing` | find -> load -> interpolate | `REQ-find-dotenv`, `REQ-interpolate-basic`, `REQ-load-no-override` | Discovery, interpolation, and environment priority compose |
| `MDS007` | `durability_reload` | unset -> get -> parse | `REQ-unset-key`, `REQ-get-key`, `REQ-no-state-leak` | File edits persist across later reads |
| `MDS008` | `error_atomicity` | malformed parse -> set -> parse | `REQ-malformed-recovery`, `REQ-set-key`, `REQ-parse-basic` | Malformed lines do not poison later mutation |
| `MDS009` | `state_accumulation` | replace -> interpolate -> dedup | `REQ-set-key`, `REQ-interpolate-basic`, `REQ-no-state-leak` | Replacing a key changes later interpolation without duplicate state |
| `MDS010` | `global_invariant` | missing file across helpers | `REQ-source-selection`, `REQ-get-key`, `REQ-unset-key` | Missing sources are safe and deterministic |
| `MDS011` | `boundary_crossing` | quote -> comment -> interpolate | `REQ-quote-single`, `REQ-quote-double`, `REQ-inline-comments`, `REQ-interpolate-basic` | Quote and comment parsing feed interpolation |
| `MDS012` | `operation_order_sensitivity` | set file -> file-vs-stream parse | `REQ-source-selection`, `REQ-set-key`, `REQ-parse-basic` | Mutated file takes precedence over stream input |
| `MDS013` | `boundary_crossing` | implicit find -> parse -> load -> cwd switch | `REQ-find-dotenv`, `REQ-source-selection`, `REQ-no-state-leak`, `REQ-load-override` | Implicit source discovery composes with read-only parsing and later loading |
| `MDS014` | `state_accumulation` | export replace -> append -> duplicate unset -> load | `REQ-set-key`, `REQ-unset-key`, `REQ-parse-comments-export`, `REQ-load-override` | Multiple persisted mutations determine later parse and environment state |
| `MDS015` | `error_atomicity` | failed mutation -> unchanged file -> valid mutation | `REQ-key-validation`, `REQ-mutation-atomicity`, `REQ-malformed-recovery`, `REQ-set-key`, `REQ-unset-key` | Failed operations preserve file state and do not block later valid edits |
| `MDS016` | `global_invariant` | interpolate=False parse -> load -> later interpolate=True parse | `REQ-interpolate-basic`, `REQ-source-selection`, `REQ-load-override`, `REQ-no-state-leak` | Literal interpolation mode is preserved through parsing and loading without poisoning later calls |
| `MDS017` | `durability_reload` | quote_mode always -> get -> parse -> file preservation | `REQ-set-key`, `REQ-quote-single`, `REQ-get-key`, `REQ-parse-basic` | Escaped quoted writes survive later helper reads and parsing |
| `MDS018` | `no_state_leak` | stream parse -> second stream parse -> file parse | `REQ-no-state-leak`, `REQ-interpolate-basic`, `REQ-interpolate-order`, `REQ-source-selection` | Repeated stream/file parses do not share hidden bindings |

## Reference Verification

| Run | Unit | System | Gap pp | Evidence role | Report |
| --- | ---: | ---: | ---: | --- | --- |
| Reference | 100.00% | 100.00% | 0.00 | reference_pass | `score_report_reference_unit_system_v1.json` |
| Codex subagent 001 | 100.00% | 100.00% | 0.00 | candidate_reviewed | `score_report_codex_subagent_001_unit_system_v1.json` |
| Mini-SWE-Agent DeepSeek chat 001 | 100.00% | 100.00% | 0.00 | candidate_reviewed | `score_report_mini_swe_agent_deepseek_chat_001_unit_system_v1.json` |

## Current Gap Status

MiniDotenv is closed-loop executable: the public PRD, rubric, reference, and scorer all run successfully. However, the currently available executable code-agent candidates do not produce a unit-system gap. The task should remain `needs code-agent gap`, not `core strong`, until a fresh code-agent run has unit > system with at least a 15pp gap.

## Fairness Notes

- Tests must not require exact logger or warning text.
- Tests must not inspect private parser tokens or original `python-dotenv` internal classes.
- Tests must not require Click CLI, IPython magic, or `dotenv run` process execution.
- Tests should avoid full Bash compatibility and complex multiline edge cases unless the PRD is expanded first.
