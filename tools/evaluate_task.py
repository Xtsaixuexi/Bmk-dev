#!/usr/bin/env python3
"""Evaluate a Bmk-dev task rubric against a candidate solution directory."""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


def score_bucket(results, layer):
    selected = [r for r in results if r["layer"] == layer]
    weight = sum(r["weight"] for r in selected)
    passed_weight = sum(r["weight"] for r in selected if r["passed"])
    cases = len(selected)
    passed_cases = sum(1 for r in selected if r["passed"])
    return {
        "weight": weight,
        "passed_weight": passed_weight,
        "score": passed_weight / weight if weight else 0.0,
        "cases": cases,
        "passed_cases": passed_cases,
    }


def run_case(case, solution_dir, timeout):
    with tempfile.TemporaryDirectory(prefix="bmk-eval-") as td:
        test_path = Path(td) / "case.py"
        test_path.write_text(case["test_code"], encoding="utf-8")
        env = os.environ.copy()
        existing_pythonpath = env.get("PYTHONPATH")
        env["PYTHONPATH"] = str(solution_dir) if not existing_pythonpath else f"{solution_dir}{os.pathsep}{existing_pythonpath}"
        proc = subprocess.run(
            [sys.executable, str(test_path)],
            cwd=solution_dir,
            text=True,
            capture_output=True,
            timeout=timeout,
            env=env,
        )
    actual = proc.stdout.rstrip("\n")
    expected = case.get("expected_output", "").rstrip("\n")
    passed = proc.returncode == 0 and actual == expected
    return {
        "id": case["id"],
        "layer": case["layer"],
        "category": case.get("category"),
        "system_dimension": case.get("system_dimension"),
        "requirement_refs": case.get("requirement_refs", []),
        "description": case.get("description", ""),
        "weight": case.get("weight", 1),
        "passed": passed,
        "returncode": proc.returncode,
        "expected_output": expected,
        "actual_output": actual,
        "stderr": proc.stderr.rstrip("\n"),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-dir", required=True)
    parser.add_argument("--solution-dir", required=True)
    parser.add_argument("--run-name", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--timeout", type=float, default=10.0)
    args = parser.parse_args()

    task_dir = Path(args.task_dir).resolve()
    solution_dir = Path(args.solution_dir).resolve()
    rubric_path = task_dir / "rubric.json"
    rubric = json.loads(rubric_path.read_text(encoding="utf-8"))

    results = []
    for case in rubric:
        try:
            result = run_case(case, solution_dir, args.timeout)
        except subprocess.TimeoutExpired as exc:
            result = {
                "id": case["id"],
                "layer": case["layer"],
                "category": case.get("category"),
                "system_dimension": case.get("system_dimension"),
                "requirement_refs": case.get("requirement_refs", []),
                "description": case.get("description", ""),
                "weight": case.get("weight", 1),
                "passed": False,
                "returncode": None,
                "expected_output": case.get("expected_output", "").rstrip("\n"),
                "actual_output": (exc.stdout or "").rstrip("\n") if isinstance(exc.stdout, str) else "",
                "stderr": "TIMEOUT",
            }
        results.append(result)

    total_weight = sum(r["weight"] for r in results)
    passed_weight = sum(r["weight"] for r in results if r["passed"])
    unit_score = score_bucket(results, "unit")
    system_score = score_bucket(results, "system")
    report = {
        "evaluator_version": "local_unit_system_v1",
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "task_dir": str(task_dir),
        "rubric_path": str(rubric_path),
        "solution_dir": str(solution_dir),
        "run_name": args.run_name,
        "total_cases": len(results),
        "passed_cases": sum(1 for r in results if r["passed"]),
        "total_weight": total_weight,
        "passed_weight": passed_weight,
        "score": passed_weight / total_weight if total_weight else 0.0,
        "unit_score": unit_score,
        "system_score": system_score,
        "unit_system_gap": unit_score["score"] - system_score["score"],
        "failed_ids": [r["id"] for r in results if not r["passed"]],
        "layers": {"unit": unit_score, "system": system_score},
        "categories": {},
        "results": results,
    }

    for r in results:
        bucket = report["categories"].setdefault(r.get("category") or "uncategorized", {"cases": 0, "passed_cases": 0, "weight": 0, "passed_weight": 0})
        bucket["cases"] += 1
        bucket["weight"] += r["weight"]
        if r["passed"]:
            bucket["passed_cases"] += 1
            bucket["passed_weight"] += r["weight"]

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({
        "run_name": args.run_name,
        "unit_score": round(unit_score["score"] * 100, 2),
        "system_score": round(system_score["score"] * 100, 2),
        "gap_pp": round(report["unit_system_gap"] * 100, 2),
        "failed_ids": report["failed_ids"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
