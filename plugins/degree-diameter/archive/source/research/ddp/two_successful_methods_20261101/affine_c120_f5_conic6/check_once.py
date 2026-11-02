#!/usr/bin/env python3
"""New controller triangle gate only; no BFS or fiber graph is built."""
import itertools
import json
import resource
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "research/ddp/m1_sources/graph_6_3_n120.txt"


def save(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + "\n")


def main():
    assert (HERE / "PRED.json").exists()
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    start = time.process_time()
    edges = []
    for line in SOURCE.read_text().splitlines():
        if line.strip() and not line.lstrip().startswith("#"):
            a, b = map(int, line.split())
            edges.append((a, b))
    assert all(0 <= a < b < 120 for a, b in edges)
    assert len(set(edges)) == len(edges) == 360
    adj = [set() for _ in range(120)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    assert {len(row) for row in adj} == {6}
    triangles = [
        (a, b, c)
        for a in range(120)
        for b in sorted(adj[a])
        if a < b
        for c in sorted(adj[a] & adj[b])
        if b < c
    ]
    counts = [0] * 120
    for triangle in triangles:
        for a in triangle:
            counts[a] += 1
    free = [a for a, count in enumerate(counts) if count == 0]
    hist = dict(sorted(Counter(counts).items()))
    save("CONTROLLER_TRIANGLE_PROFILE.json", {
        "source": str(SOURCE.relative_to(ROOT)),
        "simple": True,
        "vertices": 120,
        "edges": 360,
        "degree_histogram": {6: 120},
        "triangle_count": len(triangles),
        "vertex_triangle_count_histogram": hist,
        "vertex_triangle_counts": counts,
        "triangles": triangles,
        "triangle_free_vertices": free,
        "port_neighbors": [sorted(row) for row in adj],
        "BFS_runs": 0,
        "source_provenance_and_D3_inherited": True,
    })
    witness = None
    if free:
        a = free[0]
        neighbors = sorted(adj[a])
        witness = {
            "vertex": a,
            "sorted_neighbors": neighbors,
            "all15_neighbor_pairs": [
                {"pair": [b, c], "is_controller_edge": c in adj[b]}
                for b, c in itertools.combinations(neighbors, 2)
            ],
            "same_fiber_closed_walk_lengths_at_most3": [0, 2],
            "two_step_closed_words": [[a, b, a] for b in neighbors],
            "fiber_size": 125,
            "same_fiber_R3_upper": 25,
            "unreachable_same_fiber_targets_at_least": 100,
            "affine_offsets": "Cancel under true reverse inverse relation",
        }
        assert all(not row["is_controller_edge"] for row in witness["all15_neighbor_pairs"])
        save("TRIANGLE_FREE_WITNESS.json", witness)
    status = ("FIXED_CONTROLLER_FULL_PORT_LINE_D3_EXCLUDED_BY_TRIANGLE_FREE_VERTEX"
              if free else "TRIANGLE_GATE_SURVIVES_QUOTIENT_INTERFACE_REQUIRED")
    result = {
        "status": status,
        "simple": True,
        "controller_n": 120,
        "controller_edges": 360,
        "controller_degree_histogram": {6: 120},
        "actual_triangle_count": len(triangles),
        "actual_vertex_triangle_histogram": hist,
        "triangle_free_vertex_count": len(free),
        "first_triangle_free_vertex": free[0] if free else None,
        "same_fiber_R3_upper_at_witness": 25 if free else None,
        "same_fiber_size": 125,
        "CPU_seconds": time.process_time() - start,
        "CPU_budget_seconds": 30,
        "workers": 1,
        "new_fiber_graphs": 0,
        "BFS_runs": 0,
        "source_fetches": 0,
        "Lean_runs": 0,
        "SAT_calls": 0,
        "MIP_calls": 0,
        "quotient_domain_enumerations": 0,
        "accepted_count_change": 0,
        "scope": "Fixed literal Michel120 controller, F5^3 full fibers, one full5point affine line per incident edge, no within-fiber edges, invertible affine maps with true reverse inverses and transported endpoint port lines. Arbitrary edge maps and offsets are included.",
        "not_excluded": "Changed controller, changed adjacency rule, added within-fiber edges, other fiber relations. These were not tried or scheduled.",
    }
    save("RESULT.json", result)
    save("TERMINAL.json", {
        "status": status,
        "running": False,
        "active_handles": [],
        "next": "Stop this fixed controller/full-line/no-intrafiber rule; no automatic followup." if free else "Return first gate; quotient interface remains unexecuted.",
        "graphs_added": 0,
        "solver_calls": 0,
    })
    print(json.dumps(result))


if __name__ == "__main__":
    main()
