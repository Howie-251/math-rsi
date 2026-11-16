#!/usr/bin/env python3
"""Independently reconstruct and verify the specified one-vertex extension.

Only the original text edge list is a construction input.  No author-provided
CSR, distance ball, provider table, candidate adjacency, or search code is read.
The old graph's previously accepted D <= 5 is an explicit inherited premise;
this program runs exactly one BFS, rooted at the new vertex 42402.
"""

import argparse
from collections import Counter, deque
from datetime import datetime, timezone
import json
from pathlib import Path
import resource
import sys
import time


AR = Path("/inspire/hdd/global_user/mahaitong-240108120090/ar4math")
SOURCE = AR / "research/ddp/more_graphs_20261027/h9_redei15/production/continuation/graphs/graph_d12_D5_n42402.edges"
OUT = Path(__file__).resolve().parent
ROOT_GRAPH = OUT.parent / "graph_d12_D5_n42403.edges"
OLD_N = 42402
OLD_M = 245937
NEW_VERTEX = 42402
NEIGHBORS = (979, 4045, 4563, 5711, 6513, 7312, 8156, 15138,
             21547, 29557, 37599, 41421)


def read_simple_graph(path):
    """Parse a headered undirected edge list, rejecting non-simple input."""
    with path.open("r", encoding="ascii") as stream:
        header = stream.readline().split()
        if len(header) != 2:
            raise ValueError(f"{path}: expected a two-integer n m header")
        n, declared_m = map(int, header)
        edges = set()
        degrees = [0] * n
        edge_lines = 0
        for line_no, line in enumerate(stream, start=2):
            fields = line.split()
            if not fields:
                continue
            if len(fields) != 2:
                raise ValueError(f"{path}:{line_no}: expected exactly two endpoints")
            u, v = map(int, fields)
            if not (0 <= u < n and 0 <= v < n):
                raise ValueError(f"{path}:{line_no}: endpoint outside 0..{n - 1}")
            if u == v:
                raise ValueError(f"{path}:{line_no}: loop at {u}")
            e = (min(u, v), max(u, v))
            if e in edges:
                raise ValueError(f"{path}:{line_no}: duplicate undirected edge {e}")
            edges.add(e)
            degrees[u] += 1
            degrees[v] += 1
            edge_lines += 1
    if edge_lines != declared_m:
        raise ValueError(f"{path}: header m={declared_m}, actual m={edge_lines}")
    return n, edges, degrees


def histogram(values):
    return {str(k): v for k, v in sorted(Counter(values).items())}


def compare_graph(path, expected_n, expected_edges):
    """A normal read when present; never wait for another process to write."""
    if not path.is_file():
        return {"path": str(path), "status": "ABSENT_AT_RUN", "waited": False}
    actual_n, actual_edges, unused_degrees = read_simple_graph(path)
    missing = expected_edges - actual_edges
    extra = actual_edges - expected_edges
    same = actual_n == expected_n and not missing and not extra
    return {
        "path": str(path), "status": "MATCH" if same else "MISMATCH",
        "waited": False, "n": actual_n, "m": len(actual_edges),
        "missing_edge_count": len(missing), "extra_edge_count": len(extra),
        "missing_edge_examples": sorted(missing)[:20],
        "extra_edge_examples": sorted(extra)[:20],
        "comparison": "exact undirected edge-set equality against independent raw-source reconstruction",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--output-dir", type=Path, default=OUT)
    parser.add_argument("--compare", type=Path, default=ROOT_GRAPH)
    args = parser.parse_args()
    wall_start = time.monotonic()
    cpu_start = time.process_time()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    n0, original, old_degrees = read_simple_graph(args.source)
    assert (n0, len(original)) == (OLD_N, OLD_M)
    assert max(old_degrees) <= 12
    assert len(NEIGHBORS) == len(set(NEIGHBORS)) == 12
    assert all(0 <= v < n0 for v in NEIGHBORS)

    additions = {(v, NEW_VERTEX) for v in NEIGHBORS}
    new_edges = original | additions
    n = n0 + 1
    assert NEW_VERTEX == n0
    assert len(new_edges) == OLD_M + 12
    retained = original & new_edges
    removed = original - new_edges
    actual_added = new_edges - original
    assert retained == original and not removed and actual_added == additions
    assert all(v == NEW_VERTEX and u in NEIGHBORS for u, v in actual_added)

    adjacency = [[] for _ in range(n)]
    for u, v in sorted(new_edges):
        adjacency[u].append(v)
        adjacency[v].append(u)
    for row in adjacency:
        row.sort()
    new_degrees = list(map(len, adjacency))
    assert max(new_degrees) <= 12
    assert adjacency[NEW_VERTEX] == list(NEIGHBORS)
    assert sum(new_degrees) == 2 * len(new_edges)
    assert all(new_degrees[v] == old_degrees[v] + int(v in NEIGHBORS)
               for v in range(n0))

    # Exactly one BFS, from the added vertex.  Sorting makes parent choices and
    # the selected farthest-path witness deterministic across Python versions.
    distances = [-1] * n
    parents = [-1] * n
    distances[NEW_VERTEX] = 0
    queue = deque([NEW_VERTEX])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if distances[v] == -1:
                distances[v] = distances[u] + 1
                parents[v] = u
                queue.append(v)
    unreachable = [v for v, d in enumerate(distances) if d < 0]
    assert not unreachable
    maxdist = max(distances)
    assert maxdist <= 5
    spheres = [distances.count(d) for d in range(maxdist + 1)]
    assert sum(spheres) == n
    farthest = [v for v, d in enumerate(distances) if d == maxdist]
    endpoint = min(farthest)
    reverse_path = [endpoint]
    while reverse_path[-1] != NEW_VERTEX:
        reverse_path.append(parents[reverse_path[-1]])
    witness = reverse_path[::-1]
    assert len(witness) - 1 == maxdist
    assert all((min(u, v), max(u, v)) in new_edges
               for u, v in zip(witness, witness[1:]))

    independent_graph = args.output_dir / "independent_graph.edges"
    with independent_graph.open("w", encoding="ascii", newline="\n") as stream:
        stream.write(f"{n} {len(new_edges)}\n")
        for u, v in sorted(new_edges):
            stream.write(f"{u} {v}\n")
    with (args.output_dir / "new_neighbors.txt").open("w", encoding="ascii", newline="\n") as stream:
        stream.write(f"new_vertex {NEW_VERTEX}\n")
        stream.write("neighbors " + " ".join(map(str, NEIGHBORS)) + "\n")
        for v in NEIGHBORS:
            stream.write(f"{v} old_degree={old_degrees[v]} new_degree={new_degrees[v]}\n")
    with (args.output_dir / "new_root_bfs.tsv").open("w", encoding="ascii", newline="\n") as stream:
        stream.write("vertex\tdistance_from_42402\tparent\n")
        for v in range(n):
            stream.write(f"{v}\t{distances[v]}\t{parents[v]}\n")

    comparison = compare_graph(args.compare, n, new_edges)
    assert comparison["status"] != "MISMATCH", comparison
    result = {
        "status": "PASS",
        "completed_utc": datetime.now(timezone.utc).isoformat(),
        "program": str(Path(__file__).resolve()),
        "python": sys.version.split()[0],
        "input_policy": "Only the original raw text edge list is used to construct and check the graph; no author CSR/ball/provider cache is read.",
        "source": {
            "path": str(args.source.resolve()), "n": n0, "m": len(original),
            "simple": True, "loops": 0, "duplicate_undirected_edges": 0,
            "degree_histogram": histogram(old_degrees),
            "minimum_degree": min(old_degrees), "maximum_degree": max(old_degrees),
            "inherited_accepted_diameter_upper_bound": 5,
            "old_source_roots_recomputed": 0,
            "diameter_premise": "The source graph's already accepted D <= 5 is inherited; no source all-root BFS is rerun here.",
        },
        "construction": {
            "operation": "Retain every original edge; append vertex 42402 and exactly its 12 specified incident edges.",
            "new_vertex": NEW_VERTEX, "new_neighborhood": list(NEIGHBORS),
            "added_edges": sorted(additions), "added_edge_count": len(actual_added),
            "retained_original_edge_count": len(retained), "removed_edge_count": len(removed),
            "other_added_edge_count": len(actual_added - additions),
            "neighbor_degree_changes": [{"vertex": v, "before": old_degrees[v], "after": new_degrees[v]} for v in NEIGHBORS],
        },
        "new_graph": {
            "n": n, "m": len(new_edges), "simple": True,
            "degree_histogram": histogram(new_degrees),
            "minimum_degree": min(new_degrees), "maximum_degree": max(new_degrees),
            "all_vertex_degrees_checked": n,
            "independent_edge_file": str(independent_graph.resolve()),
        },
        "new_root_bfs": {
            "roots_run": [NEW_VERTEX], "root_count": 1, "old_roots_run": 0,
            "visited_vertices": n - len(unreachable), "visited_old_vertices": n0,
            "unreachable_count": len(unreachable), "maximum_distance": maxdist,
            "sphere_sizes_by_distance_from_0": spheres,
            "sphere_sizes": {str(d): c for d, c in enumerate(spheres)},
            "farthest_vertex_count": len(farthest), "farthest_vertices": farthest,
            "deterministic_farthest_witness": {
                "endpoint": endpoint, "distance": maxdist, "path": witness,
                "every_path_edge_checked": True,
                "shortestness": "The complete BFS assigns the endpoint this distance.",
            },
            "full_distance_and_parent_table": str((args.output_dir / "new_root_bfs.tsv").resolve()),
        },
        "all_pairs_conclusion": {
            "diameter_upper_bound": 5, "diameter_exact": 5 if maxdist == 5 else None,
            "proof": "Every old-old pair retains a length <= 5 path from the accepted source because all original edges are retained. The single complete BFS from vertex 42402 reaches every old vertex within 5. These cases cover every vertex pair; the BFS witness at distance 5 also gives the matching lower bound.",
            "is_all_root_bfs": False,
            "old_root_count_not_recomputed": n0,
            "conditional_on_previously_accepted_source_D_le_5": True,
        },
        "root_graph_comparison": comparison,
        "reproduction": {
            "command": f"python3 {Path(__file__).resolve()}",
            "algorithm": "Parse raw source into a simple undirected edge set; union exactly the 12 fixed new edges; sort all adjacency lists; one FIFO BFS from 42402; choose the smallest-index farthest endpoint.",
            "randomness": "none", "threads": 1,
        },
        "resources": {
            "cpu_seconds": time.process_time() - cpu_start,
            "wall_seconds": time.monotonic() - wall_start,
            "maximum_resident_set_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        },
    }
    with (args.output_dir / "RESULT.json").open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(result, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    print(json.dumps({"status": result["status"], "n": n, "m": len(new_edges),
                      "degree_histogram": result["new_graph"]["degree_histogram"],
                      "new_root_spheres": spheres, "maxdist": maxdist,
                      "farthest_witness": witness, "root_graph_comparison": comparison,
                      "resources": result["resources"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
