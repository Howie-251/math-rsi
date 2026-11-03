"""Decode the two published sparse6 constants; check their actual graph data.

No Sage execution or group identification is performed. Run from any directory.
"""
import ast
import json
from collections import Counter
from pathlib import Path

import networkx as nx


HERE = Path(__file__).resolve().parent
source = (HERE / "650-648Cayley_SageMath.txt").read_text()
results = {}
for name in ("rithwik650", "conder648"):
    line = next(s for s in source.splitlines() if s.startswith(name + " ="))
    literal = line[line.index("Graph(") + 6 : -1]
    graph = nx.from_sparse6_bytes(ast.literal_eval(literal).encode("ascii"))
    histogram, eccentricities = Counter(), Counter()
    for _, distances in nx.all_pairs_shortest_path_length(graph):
        histogram.update(distances.values())
        eccentricities[max(distances.values())] += 1
    results[name] = {
        "n": len(graph),
        "m": graph.number_of_edges(),
        "simple": not graph.is_multigraph() and nx.number_of_selfloops(graph) == 0,
        "connected": nx.is_connected(graph),
        "degree_counts": dict(Counter(dict(graph.degree()).values())),
        "diameter": max(eccentricities),
        "eccentricity_counts": dict(eccentricities),
        "ordered_distance_histogram": dict(sorted(histogram.items())),
        "root0_distance_histogram": dict(sorted(Counter(
            nx.single_source_shortest_path_length(graph, 0).values()
        ).items())),
    }
    with (HERE / (name + "_source.edges")).open("w") as out:
        out.write(f"{len(graph)} {graph.number_of_edges()}\n")
        for a, b in sorted(tuple(sorted(edge)) for edge in graph.edges()):
            out.write(f"{a} {b}\n")
(HERE / "source_graph_validation.json").write_text(
    json.dumps(results, indent=2) + "\n"
)
print(json.dumps(results, indent=2))
