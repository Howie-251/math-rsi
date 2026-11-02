#!/usr/bin/env python3
"""Independent terminal-graph acceptance; only literal edges and old PASS input."""

import json
import resource
import signal
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SOURCE = Path("research/ddp/refresh_20261029/f5_full_d20_D3/graph_d20_D3_n3750.edges")
PRIOR = SOURCE.with_name("INDEPENDENT_VALIDATION.json")
TERMINALS = (
    (Path("research/ddp/two_successful_methods_20261101/retained_edge_transfer/graph_d21_D3_n3900.edges"), 3900, 40500, 21),
    (Path("research/ddp/two_successful_methods_20261101/retained_edge_transfer/graph_d22_D3_n4125.edges"), 4125, 45000, 22),
)
CPU_BUDGET = 45


class BudgetExpired(Exception):
    pass


def alarm_handler(signum, frame):
    raise BudgetExpired("44 CPU-second clean-stop alarm reached")


def read_literal_graph(relative, expected_n, expected_m, degree_limit):
    """Read unordered rows independently; do not import the producer."""
    with (ROOT / relative).open("r", encoding="ascii") as stream:
        header = stream.readline().split()
        if len(header) != 2:
            raise ValueError(f"{relative}: header must contain exactly n and m")
        n, declared_m = map(int, header)
        if (n, declared_m) != (expected_n, expected_m):
            raise ValueError(f"{relative}: unexpected header {(n, declared_m)}")
        adjacency = [set() for _ in range(n)]
        edges = set()
        rows = 0
        for line_number, line in enumerate(stream, start=2):
            fields = line.split()
            if len(fields) != 2:
                raise ValueError(f"{relative}:{line_number}: expected two endpoints")
            u, v = map(int, fields)
            if not (0 <= u < n and 0 <= v < n):
                raise ValueError(f"{relative}:{line_number}: endpoint out of range")
            if u == v:
                raise ValueError(f"{relative}:{line_number}: loop at {u}")
            edge = (min(u, v), max(u, v))
            if edge in edges:
                raise ValueError(f"{relative}:{line_number}: repeated unordered edge {edge}")
            edges.add(edge)
            adjacency[u].add(v)
            adjacency[v].add(u)
            rows += 1
    if rows != declared_m or len(edges) != expected_m:
        raise ValueError(f"{relative}: {rows} literal edges disagree with header {declared_m}")
    degrees = [len(neighbors) for neighbors in adjacency]
    if max(degrees) > degree_limit:
        raise ValueError(f"{relative}: maximum degree {max(degrees)} exceeds {degree_limit}")
    if any(u not in adjacency[v] for u in range(n) for v in adjacency[u]):
        raise ValueError(f"{relative}: reconstructed adjacency is not symmetric")
    if sum(degrees) != 2 * expected_m:
        raise ValueError(f"{relative}: degree sum disagrees with edge count")
    info = {
        "file": str(relative), "n": n, "declared_m": declared_m,
        "literal_edge_rows": rows, "m": len(edges), "header_matches_actual": True,
        "vertex_labels": [0, n - 1], "simple": True, "loops": 0,
        "duplicate_unordered_edges": 0, "undirected_edge_list": True,
        "reconstructed_adjacency_symmetric": True,
        "min_degree": min(degrees), "max_degree": max(degrees),
        "degree_limit": degree_limit,
        "degree_histogram": dict(sorted(Counter(degrees).items())),
    }
    return [tuple(sorted(neighbors)) for neighbors in adjacency], edges, info


def check_new_roots(adjacency, old_n, result):
    """Exactly three BFS layers; no imported or cross-root ball cache."""
    n = len(adjacency)
    result.update({
        "new_roots_expected": n - old_n,
        "new_root_label_range": [old_n, n - 1],
        "new_roots_checked": 0, "all_new_roots_checked": False,
        "all_new_roots_reach_all_vertices_within_3": False,
        "old_roots_bfs_rerun": 0, "root_results": [],
        "first_counterexample": None,
    })
    bfs_start = time.process_time()
    for root in range(old_n, n):
        visited = bytearray(n)
        visited[root] = 1
        frontier = [root]
        layers = [1]
        for depth in range(1, 4):
            next_frontier = []
            for u in frontier:
                for v in adjacency[u]:
                    if not visited[v]:
                        visited[v] = 1
                        next_frontier.append(v)
            layers.append(len(next_frontier))
            frontier = next_frontier
        reached = sum(layers)
        root_result = {"root": root, "layers_0_to_3": layers, "reached": reached}
        result["root_results"].append(root_result)
        result["new_roots_checked"] += 1
        if reached != n:
            result["first_counterexample"] = {
                "root": root, "target": visited.index(0),
                "meaning": "target is not reachable within three literal graph edges",
            }
            result["bfs_CPU_seconds"] = time.process_time() - bfs_start
            return False
        root_result["eccentricity"] = max(i for i, count in enumerate(layers) if count)
    result["bfs_CPU_seconds"] = time.process_time() - bfs_start
    result["all_new_roots_checked"] = True
    result["all_new_roots_reach_all_vertices_within_3"] = True
    result["eccentricity_histogram_new_roots"] = dict(sorted(Counter(
        row["eccentricity"] for row in result["root_results"]
    ).items()))
    return True


def main():
    cpu_start = time.process_time()
    wall_start = time.monotonic()
    resource.setrlimit(resource.RLIMIT_CPU, (CPU_BUDGET, CPU_BUDGET))
    signal.signal(signal.SIGPROF, alarm_handler)
    signal.setitimer(signal.ITIMER_PROF, 44.0)
    output = {
        "checked_UTC": datetime.now(timezone.utc).isoformat(),
        "checker": str(Path(__file__).resolve().relative_to(ROOT)),
        "scope": "Only two terminal graphs; literal edges plus inherited old full-root D3 PASS",
        "worker_count": 1, "Python_standard_library_only": True,
        "CPU_budget_seconds": CPU_BUDGET,
        "status": "INCOMPLETE", "budget_exhausted": False,
        "production_recipe_or_cached_balls_used": False,
        "old_roots_bfs_rerun": 0,
        "review_family": "same-family",
        "deterministic_evidence_disposition": "pending",
        "subjective_assessments": "provisional",
        "global_record_claim": False, "public_maximum_degrees_21_22": "unknown",
        "novelty": "pending", "new_graph_Lean_formalizations_complete": False,
        "construction_prefixes_independently_accepted": 0,
        "terminal_graphs": [],
    }
    try:
        prior = json.loads((ROOT / PRIOR).read_text(encoding="utf-8"))
        prior_fields = ("status", "expected_n", "expected_m", "n", "m", "target_D",
                        "roots_checked", "all3750roots_checked", "target_D_passed", "graph_file")
        evidence = {key: prior[key] for key in prior_fields}
        if not (
            evidence["status"] == "PASS_COMPLETE_LITERAL_GRAPH_D3"
            and evidence["expected_n"] == evidence["n"] == 3750
            and evidence["expected_m"] == evidence["m"] == 37500
            and evidence["target_D"] == 3
            and evidence["roots_checked"] == 3750
            and evidence["all3750roots_checked"] is True
            and evidence["target_D_passed"] is True
            and Path(evidence["graph_file"]).resolve() == (ROOT / SOURCE).resolve()
        ):
            raise ValueError("existing source evidence does not provide the required complete D3 PASS")
        output["inherited_source_distance_evidence"] = {"file": str(PRIOR), **evidence}
        _, old_edges, old_info = read_literal_graph(SOURCE, 3750, 37500, 20)
        old_info["distance_recomputed"] = False
        output["old_source_literal_structure"] = old_info
        for relative, n, m, maximum_degree in TERMINALS:
            graph_start = time.process_time()
            result = {"file": str(relative), "status": "INCOMPLETE"}
            output["terminal_graphs"].append(result)
            adjacency, edges, info = read_literal_graph(relative, n, m, maximum_degree)
            result.update(info)
            missing = old_edges - edges
            result["old_edges_expected"] = len(old_edges)
            result["old_edges_retained"] = len(old_edges) - len(missing)
            result["all_old_edges_retained"] = not missing
            if missing:
                result["first_missing_old_edge"] = min(missing)
                raise ValueError(f"{relative}: old edge is missing")
            passed = check_new_roots(adjacency, 3750, result)
            result["CPU_seconds"] = time.process_time() - graph_start
            if not passed:
                result["status"] = "FAIL_NEW_ROOT_RADIUS_3"
                output["status"] = "FAIL_COUNTEREXAMPLE"
                break
            result["all_pairs_distance_at_most_3"] = True
            result["distance_proof"] = {
                "old_old": "Inherited source D3 and every literal old edge retained",
                "pairs_with_new_endpoint": "Every new root reaches all final vertices within three edges",
            }
            result["diameter_exact"] = 3 if any(
                row["layers_0_to_3"][3] for row in result["root_results"]
            ) else None
            result["status"] = "PASS_COMPLETE_LITERAL_TERMINAL_GRAPH_D3"
        else:
            output["status"] = "PASS_TWO_TERMINAL_GRAPHS_COMPLETE_DISTANCE_PROOF"
            output["terminal_graphs_independently_accepted"] = 2
            output["deterministic_evidence_disposition"] = "accepted"
    except BudgetExpired as error:
        output["status"] = "INCOMPLETE_CPU_BUDGET"
        output["budget_exhausted"] = True
        output["error"] = str(error)
    except (ValueError, OSError, KeyError) as error:
        output["status"] = "FAIL_INPUT_OR_STRUCTURE"
        output["error"] = str(error)
    finally:
        signal.setitimer(signal.ITIMER_PROF, 0.0)
    output["CPU_seconds"] = time.process_time() - cpu_start
    output["wall_seconds"] = time.monotonic() - wall_start
    destination = HERE / "INDEPENDENT_ACCEPTANCE.json"
    destination.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = {key: output[key] for key in ("status", "CPU_seconds", "wall_seconds", "budget_exhausted")}
    summary["graphs"] = [
        {key: graph.get(key) for key in ("n", "m", "degree_histogram", "old_edges_retained",
                                       "new_roots_checked", "all_new_roots_checked", "diameter_exact",
                                       "CPU_seconds", "status")}
        for graph in output["terminal_graphs"]
    ]
    summary["result_file"] = str(destination)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if output["status"].startswith("PASS_") else 1


if __name__ == "__main__":
    sys.exit(main())
