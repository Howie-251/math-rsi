#!/usr/bin/env python3
"""Check the two transcriptions against each other; not a classification run."""
import json
import os
from pathlib import Path
import resource
import time
import networkx as nx

resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
if hasattr(os, "sched_getaffinity"):
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
start = time.process_time()
base = Path(__file__).parent


def levi(config):
    blocks = config["blocks"]
    assert len(blocks) == 10 and all(len(set(b)) == 3 for b in blocks)
    assert all(sum(p in b for b in blocks) == 3 for p in range(10))
    pairs = [tuple(sorted((b[i], b[j]))) for b in blocks
             for i in range(3) for j in range(i+1, 3)]
    assert len(set(pairs)) == 30
    g = nx.Graph()
    g.add_nodes_from((p, {"side": 0}) for p in range(10))
    g.add_nodes_from((10+b, {"side": 1}) for b in range(10))
    g.add_edges_from((p, 10+b) for b, block in enumerate(blocks) for p in block)
    return g


def iso(a, b):
    matcher = nx.algorithms.isomorphism.GraphMatcher(
        a, b, node_match=lambda x, y: x["side"] == y["side"])
    return dict(matcher.mapping) if matcher.is_isomorphic() else None


data = {name: json.loads((base/f"10_3_{name}.json").read_text())["configurations"]
        for name in ("grunbaum", "orbiter")}
graphs = {name: [levi(c) for c in cs] for name, cs in data.items()}
duplicates = {}
for name, gs in graphs.items():
    duplicates[name] = [[i+1, j+1] for i in range(10) for j in range(i+1, 10)
                        if iso(gs[i], gs[j]) is not None]
matches = []
for i, a in enumerate(graphs["orbiter"], 1):
    for j, b in enumerate(graphs["grunbaum"], 1):
        mapping = iso(a, b)
        if mapping is not None:
            matches.append({"orbiter_number": i, "grunbaum_number": j,
                            "point_map": [mapping[x] for x in range(10)],
                            "block_map": [mapping[10+x]-10 for x in range(10)]})
assert not any(duplicates.values())
assert len(matches) == 10
assert len({m["orbiter_number"] for m in matches}) == 10
assert len({m["grunbaum_number"] for m in matches}) == 10
out = {"scope": "Two-color Levi isomorphism check of two supplied ten-example tables; no completeness enumeration",
       "cpu_limit_seconds": 10, "cpu_cores": 1,
       "configuration_axioms_verified": True,
       "within_catalog_duplicates": duplicates, "bijection_verified": True,
       "orbiter_to_grunbaum": matches, "cpu_seconds": time.process_time()-start}
(base/"verification.json").write_text(json.dumps(out, indent=2)+"\n")
print(json.dumps({"cpu_seconds": out["cpu_seconds"], "bijection":
                  [[m["orbiter_number"],m["grunbaum_number"]] for m in matches]}, indent=2))
