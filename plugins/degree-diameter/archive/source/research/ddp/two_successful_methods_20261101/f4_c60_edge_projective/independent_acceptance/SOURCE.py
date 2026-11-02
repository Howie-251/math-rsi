#!/usr/bin/env python3
"""Independent all-root D3 acceptance of one literal undirected edge list."""

import json
import resource
import signal
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
GRAPH = HERE.parent / "graph_d20_D3_n3840.edges"
EXPECTED_N = 3840
EXPECTED_M = 38400
EXPECTED_DEGREE = 20
CPU_BUDGET = 30


class BudgetExpired(Exception):
    pass


def budget_alarm(signum, frame):
    raise BudgetExpired("29 CPU-second clean-stop alarm reached")


def read_adjacency(result):
    start = time.process_time()
    with GRAPH.open("r", encoding="ascii") as stream:
        header = stream.readline().split()
        if len(header) != 2:
            raise ValueError("header must contain exactly two integers: n and m")
        n, m = map(int, header)
        result.update({"header_n": n, "header_m": m})
        if (n, m) != (EXPECTED_N, EXPECTED_M):
            raise ValueError(f"unexpected header: {(n, m)}")
        adjacency = [set() for _ in range(n)]
        edge_pairs = set()
        rows = 0
        for line_number, line in enumerate(stream, start=2):
            fields = line.split()
            if len(fields) != 2:
                raise ValueError(f"line {line_number}: expected two endpoints")
            u, v = map(int, fields)
            if not (0 <= u < n and 0 <= v < n):
                raise ValueError(f"line {line_number}: endpoint outside 0..{n - 1}")
            if u == v:
                raise ValueError(f"line {line_number}: loop at {u}")
            pair = (min(u, v), max(u, v))
            if pair in edge_pairs:
                raise ValueError(f"line {line_number}: repeated unordered edge {pair}")
            edge_pairs.add(pair)
            adjacency[u].add(v)
            adjacency[v].add(u)
            rows += 1
        if rows != m or len(edge_pairs) != m:
            raise ValueError(f"literal edge count {rows} does not match declared {m}")
    degrees = [len(neighbors) for neighbors in adjacency]
    if any(degree != EXPECTED_DEGREE for degree in degrees):
        bad = next(i for i, degree in enumerate(degrees) if degree != EXPECTED_DEGREE)
        raise ValueError(f"vertex {bad} has degree {degrees[bad]}, expected {EXPECTED_DEGREE}")
    if any(u not in adjacency[v] for u, neighbors in enumerate(adjacency) for v in neighbors):
        raise ValueError("reconstructed undirected adjacency is not symmetric")
    if sum(degrees) != 2 * m:
        raise ValueError("degree sum disagrees with literal edge count")
    result.update({
        "n": n, "m": m, "literal_edge_rows": rows,
        "header_matches_actual": True, "vertex_label_range": [0, n - 1],
        "incident_vertex_count": sum(degree > 0 for degree in degrees),
        "loops": 0, "repeated_unordered_edges": 0, "simple": True,
        "undirected_edge_list": True, "reconstructed_adjacency_symmetric": True,
        "min_degree": min(degrees), "max_degree": max(degrees),
        "regular_degree": EXPECTED_DEGREE,
        "degree_histogram": dict(sorted(Counter(degrees).items())),
        "literal_structure_CPU_seconds": time.process_time() - start,
    })
    return [tuple(sorted(neighbors)) for neighbors in adjacency]


def check_all_radii(adjacency, result):
    n = len(adjacency)
    start = time.process_time()
    closed_one = []
    for root, neighbors in enumerate(adjacency):
        mask = 1 << root
        for v in neighbors:
            mask |= 1 << v
        closed_one.append(mask)
    closed_two = []
    for root, neighbors in enumerate(adjacency):
        mask = closed_one[root]
        for v in neighbors:
            mask |= closed_one[v]
        closed_two.append(mask)
    result["closed_R2_count_histogram"] = dict(sorted(Counter(
        mask.bit_count() for mask in closed_two
    ).items()))
    result["closed_R1_R2_reconstruction_CPU_seconds"] = time.process_time() - start
    del closed_one

    all_vertices = (1 << n) - 1
    start = time.process_time()
    result["root_R3_reached_counts"] = []
    result["root_array_index"] = "Array index is the exact root vertex label 0..3839"
    for root, neighbors in enumerate(adjacency):
        mask = closed_two[root]
        for v in neighbors:
            mask |= closed_two[v]
        reached = mask.bit_count()
        result["root_R3_reached_counts"].append(reached)
        result["roots_checked"] += 1
        if mask != all_vertices:
            missing = all_vertices & ~mask
            first_missing = (missing & -missing).bit_length() - 1
            result["first_counterexample"] = {
                "root": root, "target": first_missing,
                "meaning": "target cannot be reached within three literal graph edges",
            }
            result["all_root_R3_CPU_seconds"] = time.process_time() - start
            return False
    result.update({
        "all_root_R3_CPU_seconds": time.process_time() - start,
        "all_roots_checked": True,
        "all_closed_R3_equal_full_vertex_set": True,
        "connected": True,
        "connectedness_evidence": "Each of all 3840 roots reaches the entire graph within three edges",
        "all_ordered_vertex_pairs_covered": n * n,
        "ordinary_unordered_pairs_covered": n * (n - 1) // 2,
        "diameter_at_most": 3,
    })
    moore_d2 = 1 + EXPECTED_DEGREE + EXPECTED_DEGREE * (EXPECTED_DEGREE - 1)
    result["Moore_D2_bound"] = moore_d2
    result["diameter_two_excluded"] = n > moore_d2
    if not n > moore_d2:
        raise ValueError("planned Moore argument does not exclude diameter two")
    result["diameter_exact"] = 3
    return True


def main():
    cpu_start = time.process_time()
    wall_start = time.monotonic()
    resource.setrlimit(resource.RLIMIT_CPU, (CPU_BUDGET, CPU_BUDGET))
    signal.signal(signal.SIGPROF, budget_alarm)
    signal.setitimer(signal.ITIMER_PROF, 29.0)
    result = {
        "checked_UTC": datetime.now(timezone.utc).isoformat(),
        "graph_file": str(GRAPH), "checker_file": str(Path(__file__).resolve()),
        "input_scope": "Only the literal edge list; no producer parameters, routes, ranks, or caches",
        "method": "Independent exact closed R1/R2 bitsets from literal adjacency; full R3 checked for every root",
        "expected_n": EXPECTED_N, "expected_m": EXPECTED_M,
        "expected_regular_degree": EXPECTED_DEGREE,
        "worker_count": 1, "Python_standard_library_only": True,
        "CPU_budget_seconds": CPU_BUDGET,
        "status": "INCOMPLETE", "budget_exhausted": False,
        "roots_expected": EXPECTED_N, "roots_checked": 0,
        "all_roots_checked": False,
        "all_closed_R3_equal_full_vertex_set": False,
        "connected": None, "first_counterexample": None,
        "production_cache_reused": False,
        "previous_3750_or_1620_graphs_rechecked": False,
        "review_family": "same-family",
        "deterministic_evidence_disposition": "pending",
        "subjective_assessments": "provisional",
        "global_public_comparison": "pending", "novelty": "pending",
        "Lean_formalization": "pending", "global_record_claim": False,
    }
    try:
        adjacency = read_adjacency(result)
        if check_all_radii(adjacency, result):
            result["status"] = "PASS_COMPLETE_LITERAL_GRAPH_D3_ALL_3840_ROOTS"
            result["deterministic_evidence_disposition"] = "accepted"
        else:
            result["status"] = "FAIL_LITERAL_R3_COUNTEREXAMPLE"
    except BudgetExpired as error:
        result["status"] = "INCOMPLETE_CPU_BUDGET"
        result["budget_exhausted"] = True
        result["error"] = str(error)
    except (ValueError, OSError) as error:
        result["status"] = "FAIL_INPUT_OR_STRUCTURE"
        result["error"] = str(error)
    finally:
        signal.setitimer(signal.ITIMER_PROF, 0.0)
    result["CPU_seconds"] = time.process_time() - cpu_start
    result["wall_seconds"] = time.monotonic() - wall_start
    destination = HERE / "INDEPENDENT_ACCEPTANCE.json"
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary_keys = (
        "status", "n", "m", "degree_histogram", "simple",
        "reconstructed_adjacency_symmetric", "connected", "roots_checked",
        "all_roots_checked", "all_closed_R3_equal_full_vertex_set", "diameter_exact",
        "Moore_D2_bound", "closed_R2_count_histogram", "CPU_seconds", "wall_seconds",
        "budget_exhausted", "first_counterexample",
    )
    summary = {key: result.get(key) for key in summary_keys}
    summary["result_file"] = str(destination)
    (HERE / "SUMMARY.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if result["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    sys.exit(main())
