"""Small exact checks for the critical-small-transversal interface.

No H search: reuse one frozen actual H and enumerate only subsets of its nine
blue points.  The blue-minimal lemma in REPORT is proved independently on paper.
"""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
source = HERE.parent / "CRITICAL_SMALL_BLOCKERS_PILOT.json"
raw = json.loads(source.read_text())
vertices = set(raw["actual_H"]["points"])
edges = [frozenset(e) for e in raw["actual_H"]["edges"]]
red = set(raw["found"]["initial_red"])
blue = vertices - red
G = frozenset([6, 8, 15, 19, 21])
degree = Counter(v for e in edges for v in e)
assert len(vertices) == 24 and len(edges) == len(set(edges)) == 35
assert all(len(e) == 5 for e in edges) and min(degree.values()) == 7
assert all(any({x, y} <= e for e in edges) for x, y in combinations(vertices, 2))
assert [e for e in edges if e <= red or e <= blue] == [G]
assert sum(degree[g] for g in G) == 35
centers = []
for g in sorted(G):
    positives = [e - {g} for e in edges if e != G and g in e and e - {g} <= blue]
    negatives = [e & blue for e in edges if g not in e]
    assert all(negatives)
    small = [B for B in negatives if len(B) <= 3]
    singleton_points = set().union(*(B for B in small if len(B) == 1))
    best = None
    for size in range(len(blue) + 1):
        hits = [frozenset(F) for F in combinations(sorted(blue), size)
                if all(set(F) & B for B in small)]
        if hits:
            best = hits
            break
    assert best is not None
    occurrence = Counter(v for A in positives for v in A)
    occurrence.update(v for B in negatives for v in B)
    ignored = {x: sum(g in e and x in e and e - {g} not in positives for e in edges)
               for x in blue}
    assert all(occurrence[x] == degree[x] - ignored[x] for x in blue)
    violations = [x for x in sorted(blue) if occurrence[x] > 7]
    centers.append({
        "g": g, "positive_count": len(positives),
        "small_negative_count_indexed": len(small),
        "small_negative_tau": len(next(iter(best))),
        "minimum_transversal_count": len(best),
        "minimum_transversal_example": sorted(best[0]),
        "singleton_points": sorted(singleton_points),
        "blue_point_data": {str(x): {"degree": degree[x], "signed_occurrence": occurrence[x],
                                      "ignored_g_edges": ignored[x]} for x in sorted(blue)},
        "signed_occurrence_above_seven": violations,
    })

# Verify the arithmetic consequence of the private-edge packing inequality.
# For n=24, M=35, total degree excess over 7 is seven. All G points are red.
# If b>=14, the floor-free upper bound already contradicts 4b incidences.
packing = []
for b in range(1, 20):
    # 12b <= 4*(30+7a+7) - (5+a)*b, where a=19-b.
    a = 19 - b
    rhs = 4 * (30 + 7*a + 7) - (5+a)*b
    packing.append({"blue_count": b, "needed_three_times_private_incidence": 12*b,
                    "upper_bound": rhs, "excluded": rhs < 12*b})
assert all(row["excluded"] for row in packing if row["blue_count"] >= 14)

result = {
    "scope": "One fixed actual colorable pair-covering H; no criticality or optimal initial color claimed.",
    "source": str(source.relative_to(HERE.parents[5])),
    "initial_red": sorted(red), "initial_blue": sorted(blue), "G": sorted(G),
    "centers": centers,
    "blue_minimal_packing_bound_check": packing,
    "status": "PASS",
}
(HERE / "CHECK.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": "PASS", "centers": [
    {k: c[k] for k in ("g", "positive_count", "small_negative_tau", "signed_occurrence_above_seven")}
    for c in centers]}, indent=2))
