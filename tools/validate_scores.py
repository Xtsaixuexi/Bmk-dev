#!/usr/bin/env python3
"""Validate Bmk-dev task metadata, score reports, and score_summary.csv."""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path


def norm(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def pct(value: float) -> float:
    return round(value * 100, 2)


def load_report_scores(path: Path) -> tuple[float, float, float]:
    report = json.loads(path.read_text(encoding="utf-8"))
    unit = pct(float(report["unit_score"]["score"]))
    system = pct(float(report["system_score"]["score"]))
    gap = pct(float(report.get("unit_system_gap", report["unit_score"]["score"] - report["system_score"]["score"])))
    return unit, system, gap


def score_report_path(task_dir: Path, solution: str) -> Path | None:
    score_dir = task_dir / "doc" / "score_reports"
    if solution == "reference":
        path = score_dir / "score_report_reference_unit_system_v1.json"
        return path if path.exists() else None
    stem = norm(solution)
    matches = sorted(score_dir.glob(f"score_report_{stem}_unit_system_v1.json"))
    return matches[0] if matches else None


def add_issue(bucket: list[dict], level: str, message: str, **extra) -> None:
    bucket.append({"level": level, "message": message, **extra})


def validate(root: Path) -> dict:
    errors: list[dict] = []
    warnings: list[dict] = []

    manifest_path = root / "MANIFEST.json"
    summary_path = root / "score_summary.csv"
    matrix_path = root / "code_agent_execution_matrix.csv"

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    rows = list(csv.DictReader(summary_path.open(encoding="utf-8")))
    matrix_rows = list(csv.DictReader(matrix_path.open(encoding="utf-8"))) if matrix_path.exists() else []

    tasks = {task["display_name"]: task for task in manifest.get("tasks", [])}
    task_ids = {task["id"]: task for task in manifest.get("tasks", [])}

    for task in manifest.get("tasks", []):
        task_dir = root / "task" / task["id"]
        for label in ("prd", "rubric", "requirement_map"):
            rel = task.get("paths", {}).get(label)
            if rel and not (root / rel).exists():
                add_issue(errors, "error", f"manifest path missing: {label}", task=task["display_name"], path=rel)

        rubric_path = task_dir / "rubric.json"
        reqmap_path = task_dir / "doc" / "requirement_map.md"
        if rubric_path.exists() and reqmap_path.exists():
            rubric = json.loads(rubric_path.read_text(encoding="utf-8"))
            reqmap = reqmap_path.read_text(encoding="utf-8")
            missing_refs = sorted({ref for case in rubric for ref in case.get("requirement_refs", []) if ref not in reqmap})
            if missing_refs:
                add_issue(errors, "error", "rubric requirement_refs missing from requirement_map", task=task["display_name"], refs=missing_refs)

            layers = {case.get("layer") for case in rubric}
            if not {"unit", "system"}.issubset(layers):
                add_issue(errors, "error", "rubric must include both unit and system cases", task=task["display_name"], layers=sorted(layers))

            for case in rubric:
                if case.get("layer") == "system" and not case.get("system_dimension"):
                    add_issue(errors, "error", "system case missing system_dimension", task=task["display_name"], case_id=case.get("id"))

    for row in rows:
        task_name = row["task"]
        solution = row["solution"]
        status = norm(row["status"])
        task = tasks.get(task_name)
        if task is None:
            add_issue(errors, "error", "score_summary task not in MANIFEST", task=task_name, solution=solution)
            continue

        if status == "non_core_bare_model":
            task_scores = task.get("auxiliary_scores", {})
            if norm(solution) not in {norm(key) for key in task_scores}:
                add_issue(errors, "error", "non-core bare model row missing from MANIFEST auxiliary_scores", task=task_name, solution=solution)

        task_dir = root / "task" / task["id"]
        report_path = score_report_path(task_dir, solution)
        if report_path is None:
            add_issue(warnings, "warning", "score_summary row has no matching score_report file", task=task_name, solution=solution)
            continue

        unit, system, gap = load_report_scores(report_path)
        row_unit = round(float(row["unit_score"]), 2)
        row_system = round(float(row["system_score"]), 2)
        row_gap = round(float(row["gap_pp"]), 2)
        if (row_unit, row_system, row_gap) != (unit, system, gap):
            add_issue(
                errors,
                "error",
                "score_summary does not match score_report",
                task=task_name,
                solution=solution,
                summary=[row_unit, row_system, row_gap],
                report=[unit, system, gap],
                report_path=str(report_path.relative_to(root)),
            )

    summary_keys = {(row["task"], norm(row["solution"])) for row in rows}
    for task in manifest.get("tasks", []):
        display = task["display_name"]
        for score_group, required_status in (("scores", None), ("auxiliary_scores", "non_core_bare_model")):
            for solution_key, score in task.get(score_group, {}).items():
                solution_norm = norm(solution_key)
                if (display, solution_norm) not in summary_keys:
                    add_issue(warnings, "warning", "MANIFEST score missing from score_summary", task=display, solution=solution_key)
                if required_status and norm(str(score.get("status", ""))) != required_status:
                    add_issue(errors, "error", "MANIFEST auxiliary score has wrong status", task=display, solution=solution_key, status=score.get("status"))

    for row in matrix_rows:
        status = norm(row.get("status", ""))
        if status not in {"scored", "partially_scored"}:
            continue
        score_solution = row.get("score_solution", "")
        for item in [part.strip() for part in score_solution.split(";") if part.strip()]:
            item_norm = norm(item)
            if not any(item_norm in solution_norm or solution_norm in item_norm for _, solution_norm in summary_keys):
                add_issue(warnings, "warning", "matrix scored solution not found in score_summary", agent=row.get("agent"), solution=item)

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "counts": {
            "manifest_tasks": len(task_ids),
            "score_summary_rows": len(rows),
            "matrix_rows": len(matrix_rows),
            "errors": len(errors),
            "warnings": len(warnings),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root")
    args = parser.parse_args()

    result = validate(Path(args.root).resolve())
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
