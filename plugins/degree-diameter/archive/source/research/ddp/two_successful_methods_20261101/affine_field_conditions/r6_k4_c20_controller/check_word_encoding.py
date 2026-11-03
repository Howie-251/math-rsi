#!/usr/bin/env python3
"""Audit 600 symbolic walks, without building any graph or repeating the search."""
import csv
import json
from pathlib import Path
import time

start = time.process_time()
here = Path(__file__).resolve().parent
rows = list(csv.DictReader((here / "WORD_COEFFICIENTS.tsv").open(), delimiter="\t"))
edge_order = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
seen = set()
groups = [[0] * 4 for _ in range(4)]
for row in rows:
    root, target = int(row["root_base"]), int(row["target_base"])
    ports = tuple(int(row[f"p{k}"]) for k in (1, 2, 3))
    assert ports[0] != ports[1] and ports[1] != ports[2]
    assert (root, ports) not in seen
    seen.add((root, ports))
    current = root
    coefficient = dict.fromkeys(edge_order, 0)
    for p in ports:
        other = current ^ (p % 3 + 1)
        if p >= 3:
            coefficient[tuple(sorted((current, other)))] += 1 if current < other else -1
        current = other
    assert current == target
    assert [coefficient[e] for e in edge_order] == [int(row[f"c{a}{b}"]) for a, b in edge_order]
    groups[root][target] += 1
assert len(rows) == len(seen) == 600
assert all(sum(group) == 150 for group in groups)
result = {"status": "PASS_SYMBOLIC_WORD_ENCODING", "rows_checked": 600,
          "word_counts_by_root_target_base": groups,
          "second_parameter_search": False, "graph_generated": False,
          "BFS_calls": 0, "CPU_seconds": time.process_time() - start}
(here / "WORD_ENCODING_CHECK.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
