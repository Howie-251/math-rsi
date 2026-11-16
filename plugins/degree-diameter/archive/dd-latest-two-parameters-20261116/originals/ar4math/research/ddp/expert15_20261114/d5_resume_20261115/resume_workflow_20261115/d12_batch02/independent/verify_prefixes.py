#!/usr/bin/env python3
"""Independent sequential verification from raw edges and explicit pins only.

No search implementation, CSR, provider data, ball cache, or reported distance
statistics are inputs.  The accepted 42419-vertex source has D <= 5 as an
inherited premise.  Each appended vertex gets its own BFS in its own prefix.
"""

import argparse
from bisect import insort
from collections import Counter, deque
from datetime import datetime, timezone
import json
from pathlib import Path
import resource
import sys
import time


OUT = Path(__file__).resolve().parent
BATCH = OUT.parent
RUN = BATCH.parents[1]
SOURCE = RUN / "resume_workflow_20261115/d12_batch01/graph_d12_D5_n42419.edges"
ADDITIONS = BATCH / "ADDITIONS.jsonl"
AUTHOR_FINAL = BATCH / "graph_d12_D5_n42433.edges"
BASE_N, BASE_M = 42419, 246141


def read_simple_graph(path):
    with path.open("r", encoding="ascii") as stream:
        fields = stream.readline().split()
        assert len(fields) == 2, "Expected n m header"
        n, declared_m = map(int, fields)
        edges = set()
        degrees = [0] * n
        for lineno, line in enumerate(stream, 2):
            fields = line.split()
            if not fields:
                continue
            assert len(fields) == 2, (str(path), lineno)
            u, v = map(int, fields)
            assert 0 <= u < n and 0 <= v < n and u != v, (lineno, u, v)
            edge = (min(u, v), max(u, v))
            assert edge not in edges, ("duplicate undirected edge", lineno, edge)
            edges.add(edge)
            degrees[u] += 1
            degrees[v] += 1
    assert len(edges) == declared_m, (len(edges), declared_m)
    return n, edges, degrees


def degree_histogram(adjacency):
    return {str(d): count for d, count in sorted(Counter(map(len, adjacency)).items())}


def complete_bfs(adjacency, root):
    distances = [-1] * len(adjacency)
    parents = [-1] * len(adjacency)
    distances[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if distances[v] < 0:
                distances[v] = distances[u] + 1
                parents[v] = u
                queue.append(v)
    assert min(distances) == 0, "Unreachable vertex in this prefix"
    maxdist = max(distances)
    assert maxdist <= 5, (root, maxdist)
    counts = Counter(distances)
    spheres = [counts[d] for d in range(maxdist + 1)]
    endpoint = next(v for v, d in enumerate(distances) if d == maxdist)
    path = [endpoint]
    while path[-1] != root:
        path.append(parents[path[-1]])
    path.reverse()
    assert len(path) - 1 == maxdist
    assert all(v in adjacency[u] for u, v in zip(path, path[1:]))
    return {
        "root": root, "graph_order_at_bfs": len(adjacency),
        "visited_count": len(adjacency), "visited_prior_vertex_count": len(adjacency) - 1,
        "unreachable_count": 0, "maximum_distance": maxdist,
        "sphere_sizes": spheres, "farthest_vertex_count": counts[maxdist],
        "farthest_witness": {"endpoint": endpoint, "distance": maxdist, "path": path,
                             "every_path_edge_checked": True,
                             "shortestness": "This prefix's complete BFS assigns the endpoint this distance."},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--additions", type=Path, default=ADDITIONS)
    parser.add_argument("--author-final", type=Path, default=AUTHOR_FINAL)
    parser.add_argument("--output-dir", type=Path, default=OUT)
    parser.add_argument("--expected-steps", type=int, required=True)
    args = parser.parse_args()
    STEPS = args.expected_steps
    assert 0 <= STEPS <= 32
    rss_entry = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    cpu_start, wall_start = time.process_time(), time.monotonic()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Deliberately discard every ADDITIONS field except the explicit vertex and
    # pins.  The author's cover/sphere/max-degree claims do not enter checks.
    additions = []
    with args.additions.open("r", encoding="utf-8") as stream:
        for line in stream:
            if line.strip():
                row = json.loads(line)
                additions.append((row["new_vertex"], tuple(row["pins"])))
    assert len(additions) == STEPS

    n0, edges, base_degrees = read_simple_graph(args.source)
    assert (n0, len(edges)) == (BASE_N, BASE_M)
    assert max(base_degrees) <= 12
    base_edges = frozenset(edges)
    adjacency = [[] for _ in range(n0)]
    for u, v in sorted(edges):
        adjacency[u].append(v)
        adjacency[v].append(u)
    for neighbors in adjacency:
        neighbors.sort()

    prefix_results = []
    all_added_edges = set()
    for step, (new_vertex, pins) in enumerate(additions):
        step_cpu = time.process_time()
        previous_n, previous_m = len(adjacency), len(edges)
        assert new_vertex == previous_n == BASE_N + step
        assert 1 <= len(pins) == len(set(pins)) <= 12
        assert all(type(v) is int and 0 <= v < previous_n for v in pins)
        new_edges = {(v, new_vertex) for v in pins}
        assert len(new_edges) == len(pins) and not (new_edges & edges)
        before_neighbor_degrees = {v: len(adjacency[v]) for v in pins}

        # These are the only edge mutations: keep the entire prior set and
        # union exactly the specified incident edges of the new vertex.
        edges.update(new_edges)
        all_added_edges.update(new_edges)
        adjacency.append(sorted(pins))
        for v in pins:
            insort(adjacency[v], new_vertex)

        assert len(edges) == previous_m + len(pins)
        assert base_edges <= edges
        assert len(edges) == len(base_edges) + len(all_added_edges)
        assert edges == base_edges | all_added_edges
        assert set(adjacency[new_vertex]) == set(pins)
        assert len(adjacency[new_vertex]) == len(pins)
        degrees = list(map(len, adjacency))
        assert max(degrees) <= 12
        assert sum(degrees) == 2 * len(edges)
        assert all(len(adjacency[v]) == before_neighbor_degrees[v] + 1 for v in pins)

        # Run now, before constructing the next prefix.  Later shortcuts cannot
        # conceal an intermediate failure.
        bfs = complete_bfs(adjacency, new_vertex)
        prefix_results.append({
            "step": step, "status": "PASS", "n": len(adjacency), "m": len(edges),
            "simple": True, "minimum_degree": min(degrees), "maximum_degree": max(degrees),
            "all_vertex_degrees_checked": len(adjacency),
            "new_vertex": new_vertex, "new_neighborhood": sorted(pins),
            "added_edges": sorted(new_edges), "added_edge_count": len(pins),
            "retained_previous_edge_count": previous_m,
            "removed_edge_count": 0, "other_added_edge_count": 0,
            "prior_prefix_diameter_upper_bound": 5,
            "bfs_in_this_prefix": bfs,
            "diameter_upper_bound": 5,
            "diameter_exact": 5 if bfs["maximum_distance"] == 5 else None,
            "acceptance_argument": "All previous edges are retained, so previous-previous pairs inherit distance <= 5. The BFS performed in this prefix reaches every previous vertex from its new vertex within 5.",
            "cpu_seconds": time.process_time() - step_cpu,
        })

    final_n, author_edges, author_degrees = read_simple_graph(args.author_final)
    missing, extra = edges - author_edges, author_edges - edges
    comparison = {
        "status": "MATCH" if final_n == len(adjacency) and not missing and not extra else "MISMATCH",
        "path": str(args.author_final.resolve()), "author_n": final_n, "author_m": len(author_edges),
        "missing_edge_count": len(missing), "extra_edge_count": len(extra),
        "missing_examples": sorted(missing)[:10], "extra_examples": sorted(extra)[:10],
        "method": "Exact undirected edge-set comparison against reconstruction from raw 42419 source and the actual explicit pin lists.",
    }
    assert comparison["status"] == "MATCH", comparison
    assert final_n == BASE_N + STEPS and len(edges) == BASE_M + len(all_added_edges)

    result = {
        "status": "PASS", "author_batch_stop_reason": "UNKNOWN_WHOLE_CPU_LIMIT_AFTER_ACCEPTED_GRAPH",
        "uncompleted_search_status": "UNKNOWN; not a nonexistence proof; only the flushed completed prefixes are checked",
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "program": str(Path(__file__).resolve()), "python": sys.version.split()[0],
        "construction_inputs": {"source_raw_edge_file": str(args.source.resolve()),
                                "additions_file": str(args.additions.resolve()),
                                "additions_fields_used": ["new_vertex", "pins"]},
        "input_policy": "No author code, CSR, provider tables, ball/distance cache, or reported cover/sphere statistics were used. The final author edge list is read only for final edge-set comparison.",
        "source": {"n": n0, "m": len(base_edges), "simple": True,
                   "degree_histogram": {str(d): c for d, c in sorted(Counter(base_degrees).items())},
                   "maximum_degree": max(base_degrees),
                   "previously_independently_accepted_diameter_upper_bound": 5,
                   "source_old_roots_recomputed": 0,
                   "complete_concrete_source_Lean": False,
                   "formal_boundary": "Inherited accepted sourceD5; concrete 42342/42402 source Lean remains open; this checker does not discharge it."},
        "prefixes": prefix_results,
        "independently_accepted_prefix_count": len(prefix_results),
        "bfs_scope": {"new_roots_run": [r["new_vertex"] for r in prefix_results],
                      "root_count": len(prefix_results), "source_old_roots_run": 0,
                      "each_bfs_uses_its_own_prefix": True, "is_all_root_bfs": False},
        "final_graph": {"n": len(adjacency), "m": len(edges), "simple": True,
                        "maximum_degree": max(map(len, adjacency)),
                        "degree_histogram": degree_histogram(adjacency),
                        "retained_source_edge_count": len(base_edges), "added_edge_count": len(all_added_edges),
                        "removed_edge_count": 0, "diameter_upper_bound": 5, "diameter_exact": 5},
        "author_final_graph_comparison": comparison,
        "all_pairs_proof": "Start with the independently accepted source D <= 5. At each completed step, retaining all previous edges preserves old-old paths and the BFS in that exact prefix proves all new-old distances <= 5. Induction proves every prefix D <= 5. A new-root BFS distance-5 witness in every prefix proves diameter exactly 5.",
        "reproduction": {"command": f"python3 {Path(__file__).resolve()} --expected-steps {STEPS}", "threads": 1,
                         "randomness": "none", "deterministic_choices": "ascending neighbor order; smallest farthest vertex"},
        "resources": {"cpu_seconds": time.process_time() - cpu_start,
                      "wall_seconds": time.monotonic() - wall_start,
                      "cpu_cap_seconds": 8, "address_space_cap_bytes": 512*1024**2,
                      "maximum_resident_set_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                      "ru_maxrss_at_entry_kib": rss_entry,
                      "proc_VmHWM_kib": next(int(x.split()[1]) for x in Path("/proc/self/status").read_text().splitlines() if x.startswith("VmHWM:")),
                      "rss_note": "ru_maxrss is reported with its entry value; proc_VmHWM is the process-visible memory high-water. RLIMIT_AS is512MiB."},
    }
    (args.output_dir / "RESULT.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    report = [
        "Independent sequential prefix verification: PASS",
        "Inputs: raw accepted 42419-vertex edge list; new_vertex and pins from ADDITIONS.jsonl only.",
        "No author CSR/provider/ball/distance cache or reported distance statistics used.",
        "Each actual completed new root gets a BFS in its own prefix before the next insertion; zero old-source roots rerun.",
        "Every previous edge retained; specified distinct incident edges added per step; every vertex degree checked <= 12.",
        "n m new_root spheres maxdist deterministic_shortest_farthest_path",
    ]
    for row in prefix_results:
        bfs = row["bfs_in_this_prefix"]
        report.append(f"{row['n']} {row['m']} {row['new_vertex']} {bfs['sphere_sizes']} {bfs['maximum_distance']} {bfs['farthest_witness']['path']}")
    report.extend([
        "Final degree histogram: " + json.dumps(result["final_graph"]["degree_histogram"], sort_keys=True),
        "Final author edge-set comparison: MATCH; missing 0, extra 0.",
        result["all_pairs_proof"],
        "Resources: " + json.dumps(result["resources"], sort_keys=True),
        "Reproduce: " + result["reproduction"]["command"],
    ])
    (args.output_dir / "REPORT.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report))


if __name__ == "__main__":
    resource.setrlimit(resource.RLIMIT_CPU, (8, 8))
    resource.setrlimit(resource.RLIMIT_AS, (512*1024**2, 512*1024**2))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    main()
