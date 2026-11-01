"""Replay a real-H limitation of one-center monotone repair; not a non-B example."""
from itertools import combinations
import json
from pathlib import Path


def instance(k):
    assert k >= 4
    n = k * k
    G = frozenset(range(k))
    P = G
    C = [frozenset(range(k + j * (k - 1),
                         k + (j + 1) * (k - 1)))
         for j in range(k)]
    B = frozenset(range(n)) - P
    edges = {G}
    for g in G:
        edges.add(frozenset({g}) | C[g])
        for y in B:
            edges.add((G - {g}) | {y})
    matching = [frozenset({j}) | C[j] for j in range(k)]
    anchor = {2, min(C[2])}
    for u, v in combinations(range(n), 2):
        e = anchor | {u, v}
        for w in range(n):
            if len(e) == k:
                break
            e.add(w)
        edges.add(frozenset(e))
    return n, G, P, C, B, matching, edges


def replay(k):
    n, G, P, C, B, matching, edges = instance(k)
    assert all(len(e) == k for e in edges)
    assert len(matching) == k
    assert all(not (x & y) for x, y in combinations(matching, 2))
    pairs = set().union(*(set(combinations(sorted(e), 2)) for e in edges))
    assert len(pairs) == n * (n - 1) // 2
    bad_source = [e for e in edges if e <= P or e <= B]
    assert bad_source == [G]
    assert all(e & G for e in edges)
    final_red = (P - {0, 1}) | {min(C[0]), min(C[1])}
    final_blue = frozenset(range(n)) - final_red
    assert not [e for e in edges if e <= final_red or e <= final_blue]
    # For any g, R empty leaves F_g blue.  For every nonempty R,
    # each selected y makes the *actual original edge* E_{g,y} red.
    for g in G:
        assert frozenset({g}) | C[g] in edges
        assert all((G - {g}) | {y} in edges for y in B)
    bound = k ** 3 - k ** 2 + k + 1 + n * (n - 1) // 2
    assert len(edges) <= bound
    return {"k": k, "n": n, "M": len(edges), "M_bound": bound,
            "pair_cover": True, "unique_bad_source": True,
            "tau_equal_k_via_disjoint_edges_and_transversal_G": k,
            "explicit_proper_four_flip_coloring": True,
            "all_G_centers_monotone_repair_blocked": True}


if __name__ == "__main__":
    result = {"status": "PASS", "scope": "actual colorable H, k=4..10; not non-B",
              "rows": [replay(k) for k in range(4, 11)]}
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
