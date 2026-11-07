"""Generate one checked Q6 cycle/matching illustration; no universal theorem claim."""
import json
from pathlib import Path


def main():
    out = Path(__file__).resolve().parent
    vertices = list(range(64))
    cycle = [i ^ (i >> 1) for i in vertices]
    cycle_edges = [[cycle[i], cycle[(i + 1) % 64]] for i in vertices]
    edges = [[u, u ^ (1 << d)] for u in vertices for d in range(6)
             if u < (u ^ (1 << d))]
    selected = [0, 3, 7, 15, 31, 47, 55, 61]
    matching = [cycle_edges[i] for i in selected]
    edge_set = {tuple(e) for e in edges}
    canonical = lambda e: tuple(sorted(e))
    adjacent = lambda e: (e[0] ^ e[1]).bit_count() == 1
    assert vertices == list(range(64))
    assert len(edges) == len(edge_set) == 192
    assert all(adjacent(e) for e in edges)
    assert all(sum(v in e for e in edges) == 6 for v in vertices)
    assert len(cycle) == len(set(cycle)) == 64 and set(cycle) == set(vertices)
    assert len(cycle_edges) == 64 and all(adjacent(e) for e in cycle_edges)
    assert cycle_edges[-1] == [cycle[-1], cycle[0]]
    assert len({canonical(e) for e in cycle_edges}) == 64
    assert all(canonical(e) in edge_set for e in cycle_edges)
    matched_vertices = [v for e in matching for v in e]
    assert len(matched_vertices) == len(set(matched_vertices)) == 16
    assert all(e in cycle_edges for e in matching)
    directions = sorted({(a ^ b).bit_length() - 1 for a, b in matching})
    assert directions == list(range(6))
    data = {
        "dimension": 6,
        "scope": "One illustrative cycle containing one explicit matching; not a universal proof.",
        "vertices": vertices,
        "vertexBits": [format(v, "06b") for v in vertices],
        "edges": edges,
        "cycleVertices": cycle,
        "cycleEdges": cycle_edges,
        "matchingCycleIndices": selected,
        "matchingEdges": matching,
        "directionConvention": "Bit position 0 is the least significant bit.",
    }
    checks = {
        "status": "PASS",
        "vertices": 64, "cubeEdges": 192, "degreeAtEveryVertex": 6,
        "cycleVerticesUnique": 64, "cycleEdges": 64,
        "closingEdge": cycle_edges[-1], "allCycleEdgesAdjacent": True,
        "cycleCoversEveryVertex": True, "matchingEdges": len(matching),
        "matchingVerticesDisjoint": True, "matchingContainedInCycle": True,
        "matchingDirections": directions,
        "scope": data["scope"],
    }
    (out / "q6.json").write_text(json.dumps(data, indent=2) + "\n")
    (out / "q6-check.json").write_text(json.dumps(checks, indent=2) + "\n")
    print(json.dumps(checks))


if __name__ == "__main__":
    main()
