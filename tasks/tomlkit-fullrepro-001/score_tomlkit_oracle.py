#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path


def read_lines(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def taxonomy_key(nodeid: str) -> str:
    nodeid = re.sub(r"\[.*\]$", "", nodeid)
    parts = nodeid.split("::")
    stem = Path(parts[0]).stem
    if len(parts) > 2:
        return f"{stem}::" + ".".join(parts[1:])
    return "::".join([stem, *parts[1:]])


def load_layers(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    with path.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("keep") == "yes":
                out[row["nodeid"]] = row["layer"]
                out[row["test_id"]] = row["layer"]
    return out


def run_pytest(
    cwd: Path,
    nodeids: list[str],
    report_path: Path,
    candidate_dir: Path,
    timeout: int,
) -> dict:
    env = os.environ.copy()
    old = env.get("PYTHONPATH")
    env["PYTHONPATH"] = str(candidate_dir.resolve()) + (os.pathsep + old if old else "")
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "-q",
        "--json-report",
        "--json-report-file",
        str(report_path),
        *nodeids,
    ]
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
        check=False,
    )
    payload = {"returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}
    if report_path.exists():
        payload["json_report"] = json.loads(report_path.read_text(encoding="utf-8"))
    return payload


def copy_upstream_worktree(source_repo: Path, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(
        source_repo,
        dest,
        ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc", ".pytest_cache"),
    )
    pkg = dest / "tomlkit"
    if pkg.exists():
        shutil.rmtree(pkg)


def collect_cases(source: str, payload: dict, requested: list[str], layers: dict[str, str]) -> list[dict]:
    tests = (payload.get("json_report") or {}).get("tests") or []
    cases = []
    if not tests:
        for nodeid in requested:
            cases.append(
                {
                    "nodeid": nodeid,
                    "source": source,
                    "layer": layers.get(nodeid) or layers.get(taxonomy_key(nodeid), "unknown"),
                    "outcome": "collection_error",
                    "stdout": payload.get("stdout", ""),
                    "stderr": payload.get("stderr", ""),
                }
            )
        return cases
    seen = set()
    for test in tests:
        nodeid = test.get("nodeid", "")
        seen.add(nodeid)
        cases.append(
            {
                "nodeid": nodeid,
                "source": source,
                "layer": layers.get(nodeid) or layers.get(taxonomy_key(nodeid), "unknown"),
                "outcome": test.get("outcome", "unknown"),
                "call": test.get("call", {}),
            }
        )
    for nodeid in requested:
        if nodeid not in seen and not any(re.sub(r"\[.*\]$", "", c["nodeid"]) == nodeid for c in cases):
            cases.append(
                {
                    "nodeid": nodeid,
                    "source": source,
                    "layer": layers.get(nodeid) or layers.get(taxonomy_key(nodeid), "unknown"),
                    "outcome": "not_collected",
                }
            )
    return cases


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-repo", required=True, type=Path)
    ap.add_argument("--candidate-dir", required=True, type=Path)
    ap.add_argument("--task-dir", required=True, type=Path)
    ap.add_argument("--run-dir", required=True, type=Path)
    ap.add_argument("--json-out", required=True, type=Path)
    ap.add_argument("--timeout", type=int, default=180)
    args = ap.parse_args()

    run_dir = args.run_dir.resolve()
    run_dir.mkdir(parents=True, exist_ok=True)
    candidate_dir = args.candidate_dir.resolve()
    task_dir = args.task_dir.resolve()

    prov = subprocess.run(
        [sys.executable, "-c", "import tomlkit; print(tomlkit.__file__)"],
        cwd=run_dir,
        env={**os.environ, "PYTHONPATH": str(candidate_dir)},
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=args.timeout,
        check=False,
    )

    upstream_worktree = run_dir / "upstream_worktree"
    copy_upstream_worktree(args.source_repo.resolve(), upstream_worktree)

    upstream_nodeids = read_lines(task_dir / "filter/kept_upstream.txt")
    generated_nodeids = read_lines(task_dir / "filter/generated_nodeids.txt")
    layers = load_layers(task_dir / "filter/test_taxonomy_score.csv")

    upstream_payload = run_pytest(
        upstream_worktree,
        upstream_nodeids,
        run_dir / "upstream_report.json",
        candidate_dir,
        args.timeout,
    )
    generated_payload = run_pytest(
        task_dir,
        generated_nodeids,
        run_dir / "generated_report.json",
        candidate_dir,
        args.timeout,
    )

    cases = collect_cases("upstream", upstream_payload, upstream_nodeids, layers)
    cases += collect_cases("generated", generated_payload, generated_nodeids, layers)
    summary = Counter()
    by_layer: dict[str, Counter] = {}
    for case in cases:
        outcome = "passed" if case["outcome"] == "subtests passed" else case["outcome"]
        summary[outcome] += 1
        summary["total"] += 1
        layer = case["layer"]
        by_layer.setdefault(layer, Counter())[outcome] += 1
        by_layer[layer]["total"] += 1

    passed = summary.get("passed", 0)
    skipped = summary.get("skipped", 0)
    result = {
        "candidate_dir": str(candidate_dir),
        "import_provenance": {
            "returncode": prov.returncode,
            "stdout": prov.stdout,
            "stderr": prov.stderr,
        },
        "summary": dict(summary),
        "pass_rate_excluding_skips": passed / max(1, summary["total"] - skipped),
        "by_layer": {k: dict(v) for k, v in sorted(by_layer.items())},
        "cases": cases,
        "upstream_payload": upstream_payload,
        "generated_payload": generated_payload,
    }
    args.json_out.parent.mkdir(parents=True, exist_ok=True)
    args.json_out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["summary", "pass_rate_excluding_skips", "by_layer", "import_provenance"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
