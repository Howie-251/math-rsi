"""Exact seven-type, three-edge multigraph calculation; no hypergraph search."""
from itertools import combinations, combinations_with_replacement, permutations
from math import comb
from pathlib import Path
import json

EDGES = tuple(combinations(range(5), 2))
INDEX = {e: i for i, e in enumerate(EDGES)}
PERMS = tuple(permutations(range(5)))


def canonical(vector):
    images = []
    for p in PERMS:
        w = [0] * 10
        for (i, j), m in zip(EDGES, vector):
            w[INDEX[tuple(sorted((p[i], p[j])))]] = m
        images.append(tuple(w))
    return min(images)


def count(vector):
    family = [set() for _ in range(5)]
    degree = [0] * 5
    point = 0
    for (i, j), m in zip(EDGES, vector):
        degree[i] += m
        degree[j] += m
        for _ in range(m):
            family[i].add(point)
            family[j].add(point)
            point += 1
    for i in range(5):
        for _ in range(4 - degree[i]):
            family[i].add(point)
            point += 1
    assert point == 17 and all(len(a) == 4 for a in family)
    direct = sum(all(set(c) & a for a in family)
                 for c in combinations(range(point), 4))
    ie = 0
    for mask in range(32):
        union = set().union(*(family[i] for i in range(5) if mask >> i & 1))
        left = point - len(union)
        ie += (-1) ** mask.bit_count() * (comb(left, 4) if left >= 4 else 0)
    assert direct == ie
    return {"vector": vector, "degrees": degree, "union_size": point,
            "C4_direct": direct, "C4_IE": ie,
            "graph_edges": [list(e) for e, m in zip(EDGES, vector) for _ in range(m)]}


def main():
    orbits = {}
    labelled = 0
    for multiset in combinations_with_replacement(range(10), 3):
        v = [0] * 10
        for e in multiset:
            v[e] += 1
        rep = canonical(v)
        orbits[rep] = orbits.get(rep, 0) + 1
        labelled += 1
    assert labelled == comb(12, 3) == 220 and len(orbits) == 7
    results = [dict(count(v), orbit_size=orbits[v]) for v in sorted(orbits)]
    assert sum(r["orbit_size"] for r in results) == 220
    result = {"domain": "loopless multigraph on five labels with exactly three indexed edges",
              "edge_order": EDGES, "labelled_count": labelled, "orbit_count": 7,
              "minimum_C4": min(r["C4_IE"] for r in results),
              "results": results, "status": "PASS"}
    assert result["minimum_C4"] > 108
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("status", "labelled_count", "orbit_count", "minimum_C4")}))
    for r in results:
        print(r["graph_edges"], r["C4_IE"], "orbit", r["orbit_size"])


if __name__ == "__main__":
    main()
