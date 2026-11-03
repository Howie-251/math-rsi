#!/usr/bin/env python3
"""One literal source, stop at the first vertex not contained in a triangle."""
import itertools
import json
import time
from pathlib import Path

started = time.process_time()
here = Path(__file__).resolve().parent
project = here.parents[3]
source = project / "research/ddp/breadth_20261027_wave6/cyclic_cover369/base41.edges"
rows = [list(map(int, line.split())) for line in source.read_text().splitlines()]
n, m = rows[0]
assert (n, m) == (41, 82) and len(rows[1:]) == m
adj = [set() for _ in range(n)]
for u, v in rows[1:]:
    adj[u].add(v)
    adj[v].add(u)
checked = []
failure = None
for u in range(n):
    ns = sorted(adj[u])
    pairs = [(v, w) for v, w in itertools.combinations(ns, 2) if w in adj[v]]
    checked.append({"vertex": u, "neighbors": ns, "neighbor_edges": pairs})
    if not pairs:
        failure = u
        break
assert failure is not None, "Unexpected pass: do not silently add the next test."
result = {
    "status": "REJECTED_AT_FIRST_TRIANGLE_FREE_VERTEX",
    "source": str(source.relative_to(project)),
    "order": n,
    "edges": m,
    "vertices_checked_before_stop": len(checked),
    "first_failure": failure,
    "checked_prefix": checked,
    "nb3_ordered_pairs_checked": 0,
    "bfs_runs": 0,
    "lift_graphs_generated": 0,
    "other_controllers_checked": 0,
    "self_fiber_capacity_F5": {"upper_bound": 17, "required": 125},
    "self_fiber_capacity_F4": {"upper_bound": 13, "required": 64},
    "cpu_seconds": time.process_time() - started,
}
(here / "RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, separators=(",", ":")))
