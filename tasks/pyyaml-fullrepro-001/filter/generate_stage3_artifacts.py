#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


TASK_ID = "pyyaml-fullrepro-001"
WIP = Path(__file__).resolve().parents[1]
FILTER = WIP / "filter"
SPEC = WIP / "spec" / "spec_v1.md"
SOURCE_REPO = Path("/root/autodl-tmp/new-e2e/yaml__pyyaml")
COMMIT = "34a9bf82357f4952d8f194a5a31f1c39743652d0"


def read_headings() -> set[str]:
    headings = set()
    for line in SPEC.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^#{2,3}\s+(.+?)\s*$", line)
        if match:
            headings.add(match.group(1))
    return headings


HEADINGS = read_headings()


def split_sections(value: str) -> list[str]:
    if value == "-":
        return []
    return [part.strip() for part in value.split("+")]


def taxonomy_key(nodeid: str) -> str:
    nodeid = re.sub(r"\[.*\]$", "", nodeid)
    parts = nodeid.split("::")
    stem = Path(parts[0]).stem
    if len(parts) > 2:
        return f"{stem}::" + ".".join(parts[1:])
    return "::".join([stem, *parts[1:]])


def func_name(nodeid: str) -> str:
    return nodeid.split("::", 2)[1]


def classify_test_yaml(func: str, nodeid: str) -> tuple[str, str, str, str]:
    excluded = {
        "test_canonical_scanner": (
            "atomic",
            "excluded",
            "test-added yaml.canonical_scan helper is not part of the public PyYAML API",
        ),
        "test_canonical_parser": (
            "atomic",
            "excluded",
            "test-added yaml.canonical_parse helper is not part of the public PyYAML API",
        ),
        "test_canonical_error": (
            "atomic",
            "excluded",
            "test-added canonical loader error protocol is not a public PyYAML behavior",
        ),
        "test_scanner": (
            "atomic",
            "excluded",
            "dummy gate: scanner smoke test has no behavioral assertion beyond no exception",
        ),
        "test_structure": (
            "atomic",
            "source-only",
            "asserts a legacy .structure fixture through Loader.check_event/get_event helpers absent from the spec",
        ),
        "test_sort_keys": (
            "atomic",
            "source-only",
            "asserts exact dump transcript text rather than semantic sorted/preserved mapping behavior",
        ),
        "test_implicit_resolver": (
            "atomic",
            "source-only",
            "YAML 1.1 schema aggregate also asserts exact safe_dump scalar spellings outside the spec",
        ),
        "test_subclass_blacklist_types": (
            "atomic",
            "source-only",
            "depends on overriding FullLoader.get_state_keys_blacklist, an implementation hook not specified as public",
        ),
    }
    if func in excluded:
        layer, status, note = excluded[func]
        return layer, "-", status, note

    direct = {
        "test_marks": (
            "atomic",
            "Error Semantics",
            "Mark.get_snippet and source mark snippet behavior",
        ),
        "test_stream_error": (
            "atomic",
            "Loading + Error Semantics",
            "reader rejects invalid byte/text streams with a YAML error",
        ),
        "test_tokens": (
            "atomic",
            "Tokens, Events, And Nodes",
            "scan returns the documented public token class sequence for YAML examples",
        ),
        "test_parser": (
            "integration",
            "Product State Model + Tokens, Events, And Nodes + Cross-View Invariants",
            "parse event stream matches the same YAML document expressed in canonical form",
        ),
        "test_parser_on_canonical": (
            "atomic",
            "Tokens, Events, And Nodes",
            "canonical YAML parses into the expected public event classes and attributes",
        ),
        "test_composer": (
            "integration",
            "Product State Model + Tokens, Events, And Nodes + Cross-View Invariants",
            "compose_all nodes preserve canonical node kinds, tags, and scalar values",
        ),
        "test_constructor": (
            "integration",
            "Product State Model + Constructors, Representers, Resolvers, And YAMLObject + Cross-View Invariants",
            "custom Loader constructor helpers construct data equivalent to canonical nodes",
        ),
        "test_loader_error": (
            "atomic",
            "Loading + Error Semantics",
            "malformed or unsupported YAML raises a YAMLError during load_all iteration",
        ),
        "test_loader_error_string": (
            "atomic",
            "Loading + Error Semantics",
            "malformed or unsupported YAML bytes raise a YAMLError during load_all iteration",
        ),
        "test_loader_error_single": (
            "atomic",
            "Loading + Error Semantics",
            "single-document load raises YAMLError for invalid single-document streams",
        ),
        "test_emitter_error": (
            "atomic",
            "Dumping + Error Semantics",
            "invalid public event streams passed to emit raise YAMLError",
        ),
        "test_dumper_error": (
            "atomic",
            "Dumping + Error Semantics",
            "unsupported dumping/serialization operations raise PyYAML errors",
        ),
        "test_emitter_on_data": (
            "system_e2e",
            "Product State Model + Tokens, Events, And Nodes + Cross-View Invariants + Representative Workflows",
            "parse, emit, and reparse preserve event classes and observable event data",
        ),
        "test_emitter_on_canonical": (
            "system_e2e",
            "Product State Model + Tokens, Events, And Nodes + Cross-View Invariants + Representative Workflows",
            "emit preserves public event data for canonical YAML streams",
        ),
        "test_emitter_styles": (
            "integration",
            "Product State Model + Dumping + Tokens, Events, And Nodes + Cross-View Invariants",
            "public event style and flow_style inputs remain parseable into equivalent events",
        ),
        "test_constructor_types": (
            "integration",
            "Loading + YAML Type Mapping + Constructors, Representers, Resolvers, And YAMLObject",
            "load_all constructs documented safe, full, custom, and unsafe Python tag values",
        ),
        "test_representer_types": (
            "integration",
            "Dumping + Constructors, Representers, Resolvers, And YAMLObject + Cross-View Invariants + Representative Workflows",
            "custom representers and dump/load round trips preserve constructed public values",
        ),
        "test_recursive": (
            "system_e2e",
            "Product State Model + Loading + Dumping + Cross-View Invariants + Representative Workflows",
            "recursive Python-specific object graphs dump and unsafe_load back into stable YAML",
        ),
        "test_unicode_input": (
            "atomic",
            "Loading",
            "full_load accepts text, bytes, BOM, and file-like Unicode streams",
        ),
        "test_unicode_input_errors": (
            "atomic",
            "Loading + Error Semantics",
            "full_load rejects byte streams with invalid or conflicting encodings",
        ),
        "test_unicode_output": (
            "atomic",
            "Dumping",
            "dump return and stream write types follow encoding and allow_unicode options",
        ),
        "test_file_output": (
            "integration",
            "Dumping",
            "dump writes equivalent text or bytes to text and binary streams with encoding options",
        ),
        "test_unicode_transfer": (
            "system_e2e",
            "Product State Model + Tokens, Events, And Nodes + Dumping + Cross-View Invariants + Representative Workflows",
            "parse and emit transfer Unicode streams through text and byte output paths",
        ),
        "test_path_resolver_loader": (
            "integration",
            "Product State Model + Constructors, Representers, Resolvers, And YAMLObject + Cross-View Invariants + Representative Workflows",
            "path resolver changes composed node tags at documented paths",
        ),
        "test_path_resolver_dumper": (
            "integration",
            "Product State Model + Constructors, Representers, Resolvers, And YAMLObject + Cross-View Invariants + Representative Workflows",
            "path resolver and serialize_all preserve node tags across dumper and loader views",
        ),
        "test_multi_constructor": (
            "integration",
            "Constructors, Representers, Resolvers, And YAMLObject",
            "multi-constructor fallback and tag-prefix registrations construct expected values",
        ),
    }
    if func not in direct:
        raise KeyError(f"unclassified test_yaml function: {func} ({nodeid})")
    layer, section, note = direct[func]
    return layer, section, "covered", note


def classify(nodeid: str) -> tuple[str, str, str, str]:
    path = nodeid.split("::", 1)[0]
    func = func_name(nodeid)

    if path == "tests/legacy_tests/test_yaml_ext.py":
        return (
            "integration",
            "-",
            "excluded",
            "original extension wrapper imports private yaml._yaml and is optional/not collectable under scorer isolation",
        )

    if path == "tests/test_merge.py":
        return (
            "atomic",
            "-",
            "source-only",
            "directly calls Loader.flatten_mapping and inspects MappingNode.value; merge semantics are covered elsewhere through public load",
        )

    if path == "tests/test_dump_load.py":
        if func == "test_dump":
            return "atomic", "Installable Surface + Dumping", "covered", "dump returns non-empty YAML for a simple public value"
        if func == "test_load_no_loader":
            return "atomic", "Installable Surface + Loading + Error Semantics", "covered", "load without required Loader raises TypeError"
        if func == "test_load_safeloader":
            return "atomic", "Installable Surface + Loading", "covered", "load with SafeLoader constructs a simple sequence"
        raise KeyError(f"unclassified test_dump_load function: {func}")

    if path == "tests/legacy_tests/test_yaml.py":
        return classify_test_yaml(func, nodeid)

    raise KeyError(f"unclassified path: {path}")


def validate_sections(rows: list[dict[str, str]]) -> None:
    missing = set()
    for row in rows:
        if row["status"] != "covered":
            continue
        for section in split_sections(row["spec_section"]):
            if section not in HEADINGS:
                missing.add(section)
    if missing:
        raise SystemExit(f"spec_section values do not match spec headings: {sorted(missing)}")


def write_lines(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    FILTER.mkdir(parents=True, exist_ok=True)
    nodeids = [line.strip() for line in (FILTER / "all_nodeids.txt").read_text(encoding="utf-8").splitlines() if line.strip()]
    rows = []
    for nodeid in nodeids:
        layer, section, status, note = classify(nodeid)
        rows.append(
            {
                "test_nodeid": nodeid,
                "layer": layer,
                "spec_section": section,
                "status": status,
                "notes": note,
            }
        )

    validate_sections(rows)
    counts = Counter(row["status"] for row in rows)
    kept = [row for row in rows if row["status"] == "covered"]
    by_layer = Counter(row["layer"] for row in kept)
    by_file = Counter(row["test_nodeid"].split("::", 1)[0] for row in rows)
    excluded_by_file = Counter(row["test_nodeid"].split("::", 1)[0] for row in rows if row["status"] != "covered")

    if len(rows) != 2616:
        raise SystemExit(f"expected 2616 rows, got {len(rows)}")
    if len(kept) < 50:
        raise SystemExit(f"oracle floor failed: only {len(kept)} kept")
    if not by_layer:
        raise SystemExit("taxonomy layer count is empty")

    map_lines = [
        f"# Spec Test Map: {TASK_ID}",
        "",
        "oracle_source: upstream_filtered_reference_passed",
        "source_file: upstream pytest suite",
        "authority: github_alignment/raw_main/skills/test-filter/SKILL.md",
        "coverage_floor: total oracle >= 50 and every behavior spec section has covered rows",
        "",
        "| test_nodeid | layer | spec_section | status | notes |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        map_lines.append(
            f"| `{row['test_nodeid']}` | {row['layer']} | {row['spec_section']} | {row['status']} | {row['notes']} |"
        )
    map_lines.extend(
        [
            "",
            (
                f"Total: {len(rows)} | kept (covered): {counts['covered']} | spec_gap: {counts['spec_gap']} | "
                f"source-only: {counts['source-only']} | excluded: {counts['excluded']} | final scoreable: {counts['covered']}"
            ),
        ]
    )
    write_lines(FILTER / "spec_test_map.md", map_lines)
    write_lines(WIP / "spec_test_map.md", map_lines)

    kept_nodeids = [row["test_nodeid"] for row in kept]
    write_lines(FILTER / "kept_nodeids.txt", kept_nodeids)
    write_lines(FILTER / "kept_upstream.txt", kept_nodeids)
    write_lines(WIP / "kept_nodeids.txt", kept_nodeids)

    tax_lines = [
        json.dumps({"taxonomy_key": taxonomy_key(row["test_nodeid"]), "layer": row["layer"]}, sort_keys=True)
        for row in kept
    ]
    write_lines(FILTER / "taxonomy.jsonl", tax_lines)
    write_lines(WIP / "taxonomy.jsonl", tax_lines)

    candidate_lines = [
        f"# Candidate Filter Map: {TASK_ID}",
        "",
        "| test_nodeid | layer | spec_section | status | reason |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        candidate_lines.append(
            f"| `{row['test_nodeid']}` | {row['layer']} | {row['spec_section']} | {row['status']} | {row['notes']} |"
        )
    candidate_lines.append("")
    candidate_lines.append(
        f"Total: {len(rows)} | covered: {counts['covered']} | source-only: {counts['source-only']} | excluded: {counts['excluded']}"
    )
    write_lines(FILTER / "candidate_filter_map.md", candidate_lines)

    audit_lines = [
        f"# Rewrite Audit: {TASK_ID}",
        "",
        "## Summary",
        "",
        f"- collected nodeids processed: {len(rows)}",
        f"- original files observed: {len(by_file)}",
        f"- kept upstream nodeids: {counts['covered']}",
        f"- source-only exclusions: {counts['source-only']}",
        f"- mechanical/protocol exclusions: {counts['excluded']}",
        "- rewritten upstream tests: 0",
        "- Track B trigger: not triggered; retained upstream oracle is above the 50-test global floor and covers all behavior sections.",
        "",
        "## File Decisions",
        "",
        "| file | nodeids | decision | rationale |",
        "|---|---:|---|---|",
    ]
    for file_name, total in sorted(by_file.items()):
        excluded_total = excluded_by_file[file_name]
        kept_total = total - excluded_total
        if file_name == "tests/legacy_tests/test_yaml_ext.py":
            decision = "discard original file"
            rationale = "private yaml._yaml import and optional C-extension wrapper; not retained under scorer isolation"
        elif file_name == "tests/test_merge.py":
            decision = "discard original file"
            rationale = "asserts internal Loader.flatten_mapping/MappingNode.value behavior; public merge behavior covered by legacy constructor data"
        elif file_name == "tests/test_dump_load.py":
            decision = "retain"
            rationale = "all nodeids use public top-level load/dump behavior"
        else:
            decision = "retain with node-level filtering"
            rationale = f"kept {kept_total}; excluded {excluded_total} canonical-helper, no-assertion, exact-format, and implementation-hook rows"
        audit_lines.append(f"| `{file_name}` | {total} | {decision} | {rationale} |")
    write_lines(FILTER / "rewrite_audit.md", audit_lines)

    rewritten = [
        '"""No rewritten upstream tests were needed for the final oracle.',
        "",
        "Original upstream nodeids retained in kept_upstream.txt use public PyYAML APIs.",
        "Original nodeids requiring private imports, implementation hooks, or exact transcript",
        "assertions were excluded instead of rewritten because Track A retained enough",
        "coverage to satisfy the Stage 3 floor.",
        '"""',
    ]
    write_lines(FILTER / "rewritten_upstream_tests.py", rewritten)

    section_counts: dict[str, int] = defaultdict(int)
    for row in kept:
        for section in split_sections(row["spec_section"]):
            section_counts[section] += 1

    behavior_sections = [
        "Installable Surface",
        "Product State Model",
        "Loading",
        "YAML Type Mapping",
        "Dumping",
        "Tokens, Events, And Nodes",
        "Constructors, Representers, Resolvers, And YAMLObject",
        "Error Semantics",
        "Cross-View Invariants",
        "Representative Workflows",
    ]
    below = []
    for section in behavior_sections:
        floor = 5 if section == "Cross-View Invariants" else 3
        if section_counts[section] < floor:
            below.append({"section": section, "count": section_counts[section], "floor": floor})

    validation = {
        "task_id": TASK_ID,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "total_nodeids_processed": len(rows),
        "kept": counts["covered"],
        "source_only": counts["source-only"],
        "excluded": counts["excluded"],
        "layers": dict(sorted(by_layer.items())),
        "coverage_sections": {section: section_counts[section] for section in behavior_sections},
        "coverage_below_minimum_sections": below,
        "track_b_triggered": False,
        "scorer_isolation": {
            "score_harness": "harness/score_pytest_original.py",
            "package_import": "yaml",
            "remove_paths": ["yaml"],
            "reference_solution_dir": str(SOURCE_REPO / "lib"),
        },
    }
    (FILTER / "filter_validation.json").write_text(json.dumps(validation, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    validation_lines = [
        f"# Filter Validation: {TASK_ID}",
        "",
        f"- processed nodeids: {len(rows)}",
        f"- final scoreable oracle: {counts['covered']}",
        f"- source-only: {counts['source-only']}",
        f"- excluded: {counts['excluded']}",
        f"- layers: {dict(sorted(by_layer.items()))}",
        "- Track B: not triggered; Track A retained enough public behavioral coverage.",
        "- scorer isolation: `score_pytest_original.py --remove-path yaml` with reference solution dir `/root/autodl-tmp/new-e2e/yaml__pyyaml/lib`.",
        "",
        "## Coverage Floor",
        "",
        "| spec section | covered rows | floor | status |",
        "|---|---:|---:|---|",
    ]
    for section in behavior_sections:
        floor = 5 if section == "Cross-View Invariants" else 3
        status = "PASS" if section_counts[section] >= floor else "FAIL"
        validation_lines.append(f"| {section} | {section_counts[section]} | {floor} | {status} |")
    validation_lines.append("")
    validation_lines.append("Non-behavior sections (`Product Overview`, `Scope`, `Non-Goals`, `Evaluation Notes`) are not scored as coverage targets.")
    write_lines(FILTER / "filter_validation.md", validation_lines)

    score_csv = ["layer,total"]
    for layer, total in sorted(by_layer.items()):
        score_csv.append(f"{layer},{total}")
    write_lines(FILTER / "test_taxonomy_score.csv", score_csv)
    write_lines(WIP / "test_taxonomy_score.csv", score_csv)

    print(json.dumps(validation, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
