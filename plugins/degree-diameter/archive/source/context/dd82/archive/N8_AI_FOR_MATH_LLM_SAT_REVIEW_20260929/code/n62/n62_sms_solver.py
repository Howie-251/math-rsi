#!/usr/bin/env python3
"""Prepare and solve graph-symmetric SAT tasks for the four open n=62 cases.

The generated formula intentionally disables the older static signature
ordering.  SMS then performs dynamic isomorphism rejection on symmetry cells
that are guaranteed to preserve both the parent template and any supplied
cube assumptions.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Sequence

from n62_all_templates_cnf import TEMPLATE_BY_NAME
from n62_graph_model import N62GraphModel
from n62_lemma_compiler import (
    BUILTIN_COVERAGE_COMPLETION,
    LemmaCompilation,
    compile_lemmas,
)


OPEN_TEMPLATES = (
    "08_triangle_pairs",
    "09_star_pairs",
    "10_path4_pairs",
    "11_path3_plus_pair",
)


def atomic_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, indent=2) + "\n")
    os.replace(temporary, path)


def parse_literal_list(text: str | None) -> list[int]:
    if not text:
        return []
    values = [int(token) for token in re.split(r"[\s,]+", text.strip()) if token]
    if any(value == 0 for value in values):
        raise ValueError("assumption literals must not contain zero")
    return values


def load_cube_literals(path: Path, node_name: str | None) -> tuple[list[int], dict]:
    data = json.loads(path.read_text())
    literals = [int(value) for value in data.get("root_literals", [])]
    selected_node = node_name
    if selected_node is None:
        max_depth_nodes = [
            name
            for name, node in data.get("nodes", {}).items()
            if node.get("status") == "TIMEOUT_MAX_DEPTH"
        ]
        if len(max_depth_nodes) == 1:
            selected_node = max_depth_nodes[0]
        elif max_depth_nodes:
            raise ValueError(
                "cube JSON has multiple max-depth nodes; pass --node explicitly"
            )
    if selected_node is not None:
        try:
            node = data["nodes"][selected_node]
        except KeyError as error:
            raise ValueError(f"unknown cube node {selected_node!r}") from error
        literals.extend(int(value) for value in node.get("extra_literals", []))
    metadata = {
        "cube_json": str(path),
        "root_id": data.get("root_id"),
        "node": selected_node,
        "source_status": (
            data.get("nodes", {}).get(selected_node, {}).get("status")
            if selected_node is not None
            else data.get("status")
        ),
    }
    return literals, metadata


def write_sms_dimacs(
    model: N62GraphModel,
    output_path: Path,
    assumptions: Sequence[int],
    lazy_distance: bool,
    lemmas: LemmaCompilation,
) -> dict:
    for literal in assumptions:
        model.edge_for_literal(literal)
    instance = model.instance
    if lazy_distance:
        clause_sources = (
            instance.degree_clauses,
            lambda: cl_coverage_clauses(instance),
            instance.fiber_cap_clauses,
            instance.saturated_fiber_clauses,
        )
        base_variable_count = (
            instance.edge_count
            + instance.counter_bit_count
            + instance.carry_count
        )
        clause_count = sum(
            1 for source in clause_sources for _ in source()
        ) + len(assumptions)
    else:
        clause_sources = (instance.clauses,)
        base_variable_count = instance.variable_count
        clause_count = instance.expected_clause_count() + len(assumptions)
    variable_count = lemmas.variable_count
    if variable_count < base_variable_count:
        raise AssertionError("lemma variable count is below the base formula")
    clause_count += len(lemmas.clauses)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="ascii") as handle:
        handle.write(f"p cnf {variable_count} {clause_count}\n")
        emitted = 0
        for source in clause_sources:
            for clause in source():
                handle.write(" ".join(map(str, clause)) + " 0\n")
                emitted += 1
        for literal in assumptions:
            handle.write(f"{literal} 0\n")
            emitted += 1
        for clause in lemmas.clauses:
            handle.write(" ".join(map(str, clause)) + " 0\n")
            emitted += 1
    if emitted != clause_count:
        raise AssertionError("DIMACS clause count mismatch")
    return {
        "variables": variable_count,
        "clauses": clause_count,
        "edge_variables": instance.edge_count,
        "witness_variables": 0 if lazy_distance else len(instance.witness_keys),
        "distance_encoding": (
            "lazy N62DistanceTwoChecker" if lazy_distance else "Tseitin witnesses"
        ),
        "static_signature_symmetry": False,
        "assumptions": list(assumptions),
        "lemmas": lemmas.metadata,
    }


def cl_coverage_clauses(instance):
    """Clauses for C--L distance-two coverage; L--L is propagated lazily."""

    for parent, children in enumerate(instance.fibers):
        for vertex in range(instance.l_size):
            if parent in instance.parents[vertex]:
                continue
            yield tuple(instance.edge_var(vertex, child) for child in children)


def find_sms_binary(explicit: Path | None) -> Path | None:
    candidates: list[Path] = []
    if explicit is not None:
        candidates.append(explicit)
    environment = os.environ.get("N62_SMS_BIN")
    if environment:
        candidates.append(Path(environment))
    discovered = shutil.which("smsg")
    if discovered:
        candidates.append(Path(discovered))
    candidates.extend(
        [
            Path(__file__).resolve().parent / "solvers/sms_n62/smsg-n62",
            Path.home() / ".local/bin/smsg-n62",
            Path.home() / ".local/bin/smsg",
            Path("third_party/sat-modulo-symmetries/build/src/smsg-n62"),
            Path("third_party/sat-modulo-symmetries/build/src/smsg"),
        ]
    )
    for candidate in candidates:
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return candidate.resolve()
    return None


def parse_sms_graph(log_path: Path, model: N62GraphModel) -> list[int] | None:
    graph_line = None
    for line in log_path.read_text(errors="replace").splitlines():
        stripped = line.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            graph_line = stripped
    if graph_line is None:
        return None
    edges = [
        (int(left), int(right))
        for left, right in re.findall(r"\((\d+),(\d+)\)", graph_line)
    ]
    return model.adjacency_from_edges(edges)


def command_for_sms(
    binary: Path,
    dimacs_path: Path,
    partition_sizes: Sequence[int],
    timeout_seconds: int,
    cutoff: int,
    frequency: int,
    lrat_output: Path | None,
) -> list[str]:
    command = [
        str(binary),
        "-v",
        "53",
        "--dimacs",
        str(dimacs_path),
        "--initial-partition",
        *map(str, partition_sizes),
        "--cutoff",
        str(cutoff),
        "--frequency",
        str(frequency),
    ]
    if timeout_seconds:
        command.extend(["--timeout", str(timeout_seconds)])
    if lrat_output is not None:
        command.extend(["--lrat-output", str(lrat_output)])
    return command


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--template", required=True, choices=tuple(sorted(TEMPLATE_BY_NAME))
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--cube-json", type=Path)
    parser.add_argument("--node")
    parser.add_argument(
        "--assumptions",
        help="additional comma- or whitespace-separated D-edge literals",
    )
    parser.add_argument("--sms-bin", type=Path)
    parser.add_argument("--lemma-file", action="append", type=Path, default=[])
    parser.add_argument(
        "--builtin-lemmas",
        default=BUILTIN_COVERAGE_COMPLETION,
        help="comma-separated built-in lemma families, or 'none'",
    )
    parser.add_argument(
        "--full-witness-cnf",
        action="store_true",
        help="use ordinary smsg and the original explicit L--L witness encoding",
    )
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--timeout-seconds", type=int, default=0)
    parser.add_argument("--cutoff", type=int, default=20_000)
    parser.add_argument("--frequency", type=int, default=30)
    parser.add_argument("--distance-frequency", type=int, default=10)
    parser.add_argument("--lrat-output", type=Path)
    args = parser.parse_args()

    if args.node and not args.cube_json:
        parser.error("--node requires --cube-json")
    if args.timeout_seconds < 0:
        parser.error("--timeout-seconds must be nonnegative")

    model = N62GraphModel(args.template)
    assumptions: list[int] = []
    cube_metadata: dict = {}
    if args.cube_json:
        cube_literals, cube_metadata = load_cube_literals(args.cube_json, args.node)
        assumptions.extend(cube_literals)
    assumptions.extend(parse_literal_list(args.assumptions))
    if len(set(map(abs, assumptions))) != len(assumptions):
        assignments: dict[int, bool] = {}
        for literal in assumptions:
            value = literal > 0
            variable = abs(literal)
            if variable in assignments and assignments[variable] != value:
                raise ValueError(f"contradictory assumption on variable {variable}")
            assignments[variable] = value
        assumptions = [variable if value else -variable for variable, value in assignments.items()]

    args.output_dir.mkdir(parents=True, exist_ok=True)
    dimacs_path = args.output_dir / f"{args.template}.sms.cnf"
    metadata_path = args.output_dir / "task.json"
    log_path = args.output_dir / "sms.log"
    result_path = args.output_dir / "result.json"
    partition_sizes = model.safe_partition_sizes(assumptions)
    lazy_distance = not args.full_witness_cnf
    instance = model.instance
    base_variable_count = (
        instance.edge_count + instance.counter_bit_count + instance.carry_count
        if lazy_distance
        else instance.variable_count
    )
    builtins = tuple(
        value.strip()
        for value in args.builtin_lemmas.split(",")
        if value.strip() and value.strip() != "none"
    )
    lemmas = compile_lemmas(
        model,
        base_variable_count,
        files=args.lemma_file,
        builtins=builtins,
    )
    formula_stats = write_sms_dimacs(
        model,
        dimacs_path,
        assumptions,
        lazy_distance=lazy_distance,
        lemmas=lemmas,
    )

    task = {
        "problem": "degree 8, diameter 2, order 62",
        "template": args.template,
        "dimacs": str(dimacs_path),
        "partition_sizes": partition_sizes,
        "partition_cells": len(partition_sizes),
        "cube": cube_metadata,
        "formula": formula_stats,
        "status": "PREPARED",
    }
    atomic_json(metadata_path, task)
    if args.prepare_only:
        print(json.dumps(task, indent=2))
        return 0

    binary = find_sms_binary(args.sms_bin)
    if binary is None:
        print(
            "SMS binary not found.  The exact task was prepared successfully; "
            "install smsg or pass --sms-bin.",
            file=sys.stderr,
        )
        return 2
    if lazy_distance and "n62" not in binary.name.lower():
        print(
            "The lazy formula requires the problem-specific smsg-n62 binary. "
            "Pass that binary, or use --full-witness-cnf with ordinary smsg.",
            file=sys.stderr,
        )
        return 2

    command = command_for_sms(
        binary,
        dimacs_path,
        partition_sizes,
        args.timeout_seconds,
        args.cutoff,
        args.frequency,
        args.lrat_output,
    )
    started = time.monotonic()
    environment = os.environ.copy()
    if lazy_distance:
        environment["N62_PARENT_MASKS"] = ",".join(map(str, model.parent_masks))
        environment["N62_PROP_FREQUENCY"] = str(max(1, args.distance_frequency))
    with log_path.open("w", encoding="utf-8") as log_handle:
        completed = subprocess.run(
            command,
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            check=False,
            env=environment,
        )
    elapsed = time.monotonic() - started
    status = {10: "SAT", 20: "UNSAT"}.get(completed.returncode, "UNKNOWN")
    result = {
        "status": status,
        "return_code": completed.returncode,
        "elapsed_seconds": elapsed,
        "command": shlex.join(command),
        "log": str(log_path),
        "template": args.template,
        "cube": cube_metadata,
    }

    if status == "SAT":
        adjacency = parse_sms_graph(log_path, model)
        if adjacency is None:
            raise RuntimeError("SMS returned SAT but no graph was found in its output")
        full_edges = model.verify(adjacency)
        edge_path = args.output_dir / "verified_graph.edges"
        edge_path.write_text("".join(f"{left} {right}\n" for left, right in full_edges))
        result["verified"] = True
        result["verified_graph"] = str(edge_path)
        result["full_edges"] = len(full_edges)
    atomic_json(result_path, result)
    print(json.dumps(result, indent=2))
    return completed.returncode if completed.returncode in (10, 20) else 1


if __name__ == "__main__":
    raise SystemExit(main())
