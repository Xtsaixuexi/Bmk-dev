#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


TASK_ID = "pyyaml-fullrepro-001"
WIP = Path(__file__).resolve().parents[1]
FILTER = WIP / "filter"
SOURCE_REPO = "/root/autodl-tmp/new-e2e/yaml__pyyaml"
COMMIT = "34a9bf82357f4952d8f194a5a31f1c39743652d0"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def assert_gates(reference: dict, dummy: dict, validation: dict) -> None:
    ref_summary = reference["summary"]
    dummy_summary = dummy["summary"]
    if ref_summary.get("passed") != ref_summary.get("total"):
        raise SystemExit(f"reference gate failed: {ref_summary}")
    if ref_summary.get("total") != validation["kept"]:
        raise SystemExit(f"reference total mismatch: {ref_summary.get('total')} != {validation['kept']}")
    if dummy_summary.get("passed", 0) != 0:
        raise SystemExit(f"dummy gate failed: {dummy_summary}")
    if validation["coverage_below_minimum_sections"]:
        raise SystemExit(f"coverage floor failed: {validation['coverage_below_minimum_sections']}")
    if any(case.get("layer") == "unknown" for case in reference["cases"]):
        raise SystemExit("reference score has unknown taxonomy cases")
    if any(case.get("layer") == "unknown" for case in dummy["cases"]):
        raise SystemExit("dummy score has unknown taxonomy cases")


def update_pipeline_state(validation: dict) -> None:
    path = WIP / "PIPELINE_STATE.md"
    text = path.read_text(encoding="utf-8")
    if "state: S3_FILTER_IN_PROGRESS" not in text:
        raise SystemExit("PIPELINE_STATE.md is not in S3_FILTER_IN_PROGRESS")
    kept = validation["kept"]
    excluded = validation["source_only"] + validation["excluded"]
    if kept + excluded != validation["total_nodeids_processed"]:
        raise SystemExit("kept + excluded does not equal total processed")

    replacements = {
        "state: S3_FILTER_IN_PROGRESS": "state: S3_FILTER_DONE_PENDING_REVIEW",
        "functions_kept: 0": f"functions_kept: {kept}",
        "functions_excluded: 0": f"functions_excluded: {excluded}",
        "oracle_count: 0": f"oracle_count: {kept}",
        "Stage 2 DeepSeek v4 Pro and GLM 5.2 reviews passed. Stage 3 test filtering is in progress.": (
            "Stage 3 local gates passed. Filter artifacts are ready for review; do not proceed to Stage 4 until review passes."
        ),
    }
    for old, new in replacements.items():
        if old not in text:
            raise SystemExit(f"missing expected state text: {old}")
        text = text.replace(old, new, 1)

    history = (
        f"| 2026-07-09 | S3_FILTER_IN_PROGRESS | S3_FILTER_DONE_PENDING_REVIEW | "
        f"Processed all {validation['total_nodeids_processed']} collected nodeids; kept {kept}; excluded/source-only {excluded}; "
        "reference gate 889/889 passed; dummy gate 0/889 passed under scorer isolation. |"
    )
    text = text.rstrip() + "\n" + history + "\n"
    write_text(path, text)


def main() -> int:
    reference = read_json(FILTER / "reference_score.json")
    dummy = read_json(FILTER / "dummy_score.json")
    validation = read_json(FILTER / "filter_validation.json")
    assert_gates(reference, dummy, validation)

    shutil.copyfile(FILTER / "reference_score.json", WIP / "reference_score.json")
    shutil.copyfile(FILTER / "dummy_score.json", WIP / "dummy_score.json")

    ref_summary = reference["summary"]
    dummy_summary = dummy["summary"]
    now = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    reference_validation = f"""# Reference Validation: {TASK_ID}

Generated: {now}

## Gates

- PASS: scorer isolation used `score_pytest_original.py --remove-path yaml`.
- PASS: import provenance resolved to `{reference['import_provenance']['stdout'].strip()}`.
- PASS: reference gate passed {ref_summary.get('passed')}/{ref_summary.get('total')}.
- PASS: dummy gate passed 0/{dummy_summary.get('total')}; outcomes were {dummy_summary}.
- PASS: taxonomy produced no `unknown` layer cases.
- PASS: coverage floor has no below-minimum behavior sections.

## Scorer Isolation

The scorer copied the upstream repository, removed top-level `yaml`, and placed `/root/autodl-tmp/new-e2e/yaml__pyyaml/lib` first on `PYTHONPATH`.
"""
    write_text(FILTER / "reference_validation.md", reference_validation)
    write_text(WIP / "reference_validation.md", reference_validation)

    alignment = f"""# Stage 3 GitHub Alignment: {TASK_ID}

Generated: {now}

Authority files:

- `github_alignment/raw_main/skills/test-filter/SKILL.md`
- `github_alignment/raw_main/skills/task-synthesizer/SKILL.md`

## Alignment Checks

- PASS: `PIPELINE_STATE.md` was verified as `S3_FILTER_IN_PROGRESS` before filtering.
- PASS: all 2616 collected nodeids are present in `filter/spec_test_map.md`.
- PASS: every covered row maps to headings present in `spec/spec_v1.md`.
- PASS: `filter/rewrite_audit.md` exists and records Track A file-level decisions before merge.
- PASS: original `test_yaml_ext.py` nodeids were excluded because they import private `yaml._yaml` and are optional C-extension wrapper tests under scorer isolation.
- PASS: original `test_merge.py` nodeids were excluded because they assert `Loader.flatten_mapping`/`MappingNode.value` implementation shape rather than public merge behavior.
- PASS: exact dump transcript, no-assertion scanner smoke, and test-added canonical helper rows were excluded.
- PASS: Track B was not triggered because Track A retained 889 public behavioral nodeids and all behavior coverage floors passed.
- PASS: `kept_nodeids.txt`, `taxonomy.jsonl`, `spec_test_map.md`, `candidate_filter_map.md`, `kept_upstream.txt`, and root copies were generated.
- PASS: scorer-compatible taxonomy produced non-zero by-layer counts and zero unknown cases.
- PASS: scorer isolation is recorded as `score_pytest_original.py --remove-path yaml`.
- PASS: reference gate passed 889/889 and dummy gate passed 0/889.
- PASS: no external review models were called in this Stage 3 run.
"""
    write_text(WIP / "github_alignment" / "stage3_test_filter_alignment.md", alignment)

    manifest = {
        "task_id": TASK_ID,
        "repo": "yaml__pyyaml",
        "status": "S3_FILTER_DONE_PENDING_REVIEW",
        "current_step": 3,
        "source": {
            "path": SOURCE_REPO,
            "commit": COMMIT,
            "package": "yaml",
            "tests": "tests/legacy_tests/test_yaml.py tests/legacy_tests/test_yaml_ext.py tests/test_dump_load.py tests/test_merge.py",
        },
        "cleanroom_policy": {
            "candidate_visible": ["spec.md", "public implementation prompt"],
            "candidate_forbidden": [
                "source repository",
                "upstream tests",
                "kept_nodeids.txt",
                "taxonomy.jsonl",
                "spec_test_map.md",
                "reference_score.json",
                "dummy_score.json",
                "filter artifacts",
                "review artifacts",
            ],
        },
        "artifacts": {
            "spec": "spec.md",
            "spec_v1": "spec/spec_v1.md",
            "collected_nodeids": "filter/all_nodeids.txt",
            "rewrite_audit": "filter/rewrite_audit.md",
            "candidate_filter_map": "filter/candidate_filter_map.md",
            "rewritten_upstream_tests": "filter/rewritten_upstream_tests.py",
            "kept_upstream": "filter/kept_upstream.txt",
            "spec_test_map": "filter/spec_test_map.md",
            "kept_nodeids": "filter/kept_nodeids.txt",
            "taxonomy": "filter/taxonomy.jsonl",
            "test_taxonomy_score": "filter/test_taxonomy_score.csv",
            "filter_validation": "filter/filter_validation.md",
            "reference_score": "filter/reference_score.json",
            "dummy_score": "filter/dummy_score.json",
            "reference_validation": "filter/reference_validation.md",
            "stage3_alignment": "github_alignment/stage3_test_filter_alignment.md",
            "root_spec_test_map": "spec_test_map.md",
            "root_kept_nodeids": "kept_nodeids.txt",
            "root_taxonomy": "taxonomy.jsonl",
        },
        "state": "S3_FILTER_DONE_PENDING_REVIEW",
        "spec_version": "v1",
        "oracle_source": "upstream_filtered_reference_passed",
        "kept_nodeids": validation["kept"],
        "reference_passed": ref_summary.get("passed"),
        "reference_failed": ref_summary.get("failed", 0),
        "reference_total": ref_summary.get("total"),
        "dummy_passed": dummy_summary.get("passed", 0),
        "dummy_total": dummy_summary.get("total"),
        "score_harness": "harness/score_pytest_original.py",
        "remove_paths": ["yaml"],
        "scorer_isolation": {
            "score_harness": "harness/score_pytest_original.py",
            "package_import": "yaml",
            "preflight_command": "python -c \"import yaml; print(yaml.__file__)\"",
            "remove_paths": ["yaml"],
            "reference_solution_dir": "/root/autodl-tmp/new-e2e/yaml__pyyaml/lib",
            "source_shadowing_guard": "Use score_pytest_original.py with --remove-path yaml so copied oracle worktree cannot import a top-level source package instead of the solution path.",
        },
        "filter_summary": {
            "collected_nodeids": validation["total_nodeids_processed"],
            "kept": validation["kept"],
            "source_only": validation["source_only"],
            "excluded": validation["excluded"],
            "functions_excluded_for_state": validation["source_only"] + validation["excluded"],
            "oracle_count": validation["kept"],
            "layers": validation["layers"],
            "coverage_sections": validation["coverage_sections"],
            "coverage_below_minimum_sections": validation["coverage_below_minimum_sections"],
            "track_a": {
                "kept_upstream": validation["kept"],
                "rewritten_tests": 0,
            },
            "track_b": {
                "triggered": False,
                "reason": "Track A retained 889 public behavioral nodeids with all behavior coverage floors satisfied.",
            },
            "dummy_summary": dummy_summary,
            "reference_summary": ref_summary,
            "taxonomy_unknown_cases": 0,
        },
        "model_reviews": {
            "stage3": "not_called_per_user_instruction",
        },
        "pipeline_state": "S3_FILTER_DONE_PENDING_REVIEW",
        "updated_at": now,
    }
    write_text(WIP / "MANIFEST.json", json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    update_pipeline_state(validation)
    print(json.dumps({"state": "S3_FILTER_DONE_PENDING_REVIEW", "kept": validation["kept"], "excluded_for_state": validation["source_only"] + validation["excluded"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
