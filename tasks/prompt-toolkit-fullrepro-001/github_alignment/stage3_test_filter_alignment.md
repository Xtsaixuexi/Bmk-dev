# Stage 3 Test Filter Alignment

## Workflow Inputs

- Stage skill read: `github_alignment/raw_main/skills/test-filter/SKILL.md`
- Coordinator skill read: `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`
- Source repo: `/root/autodl-tmp/new-e2e/prompt-toolkit__python-prompt-toolkit`
- Candidate spec: `spec.md`
- Pipeline entry state: `S3_FILTER_IN_PROGRESS`

## Required Outputs

| artifact | status |
|---|---|
| `filter/rewrite_audit.md` | present |
| `filter/spec_test_map.md` | present |
| `filter/kept_nodeids.txt` | present |
| `filter/taxonomy.jsonl` | present |
| `filter/test_taxonomy_score.csv` | present |
| `filter/reference_validation.md` | present |
| `filter/dummy_score.json` | present |
| `filter/filter_validation.md` | present |
| root `kept_nodeids.txt` | present |
| root `taxonomy.jsonl` | present |
| root `spec_test_map.md` | present |
| root `reference_validation.md` | present |
| root `filter_validation.md` | present |

## Filtering Alignment

PASS. Every covered test has a concrete `spec_section` mapping in `filter/spec_test_map.md`. Rows that could not be mapped to the narrowed public spec were marked `source-only` or `excluded` rather than retained.

The retained/generated oracle covers the requested public stable behavior areas:

- `Document` and `Buffer`
- completion
- validation
- key bindings
- formatted text
- style lookup and transformations
- layout focus and controls
- `PromptSession`, `PipeInput`, `DummyOutput`, and app-session I/O injection

The filter excludes the requested non-goals:

- terminal byte stream exactness
- snapshot exact rendering
- private renderer/parser internals
- contrib servers, dialogs, progress, widget visual polish
- platform-specific terminal behavior
- test helper fixture behavior

## Count Alignment

| metric | count |
|---|---:|
| upstream collected | 156 |
| upstream covered | 68 |
| generated covered | 32 |
| source-only | 28 |
| excluded | 60 |
| final scoreable oracle | 100 |

Taxonomy is non-empty in all required layers:

| layer | covered |
|---|---:|
| atomic | 59 |
| integration | 33 |
| system_e2e | 8 |

## Validation Alignment

PASS.

- Upstream retained scorer reference gate: 68 passed / 68 total
- Generated reference pytest gate: 32 passed / 32 total
- Upstream retained scorer dummy gate: 0 passed / 68 total
- Generated dummy pytest gate: 0 passed; collection failed on dummy public import

The upstream scorer used `--remove-path src/prompt_toolkit` and a provenance check for `prompt_toolkit`. The generated tests are wip-local pytest tests, so they were validated with direct pytest reference/dummy gates.

## Pipeline Exit

Stage 3 is ready to leave `S3_FILTER_IN_PROGRESS` for `S3_FILTER_DONE_PENDING_REVIEW`.
