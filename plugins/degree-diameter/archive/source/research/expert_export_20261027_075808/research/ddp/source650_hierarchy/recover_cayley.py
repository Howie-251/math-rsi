"""Recover and exactly verify the labelled 650 construction; no graph search."""
import csv
import json
import time
from collections import Counter
from pathlib import Path

started = time.process_time()
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
source = ROOT / "research/ddp/m1_degree5_transfer/rithwik650_source.edges"
data = list(map(int, source.read_text().split()))
n, edge_count = data[:2]
original = {tuple(sorted(e)) for e in zip(data[2::2], data[3::2])}
assert (n, edge_count, len(original)) == (650, 1625, 1625)
adj = [set() for _ in range(n)]
for u, v in original:
    adj[u].add(v)
    adj[v].add(u)

q, m, action = 25, 20, 2
power = [pow(action, k, q) for k in range(m)]
assert len(set(power)) == 20 and pow(action, m, q) == 1
S = [(v % q, v // q) for v in sorted(adj[0]) if v < 500]
assert S == [(21, 9), (1, 10), (10, 10), (17, 11)]


def multiply(g, h):
    x, k = g
    y, ell = h
    return ((x + power[k] * y) % q, (k + ell) % m)


def inverse(g):
    x, k = g
    return (-power[-k % m] * x % q, -k % m)


def leaf(x, k):
    return x + q * k


def block(x, b):
    return 500 + 5 * x + b


def head(x):
    return 625 + x


leaf_edges = set()
tree_edges = set()
for x in range(q):
    for k in range(m):
        u = leaf(x, k)
        for s in S:
            y, ell = multiply((x, k), s)
            leaf_edges.add(tuple(sorted((u, leaf(y, ell)))))
        tree_edges.add(tuple(sorted((u, block(x, k % 5)))))
    for b in range(5):
        tree_edges.add((block(x, b), head(x)))
reconstructed = leaf_edges | tree_edges
assert len(leaf_edges) == 1000 and len(tree_edges) == 625
assert reconstructed == original
with (HERE / "algebraic_reconstruction.edges").open("w") as f:
    f.write("650 1625\n")
    for u, v in sorted(reconstructed):
        f.write(f"{u} {v}\n")

compressed = json.loads((HERE / "compressed_graph.json").read_text())
for b in compressed["blocks"]:
    x, y = divmod(b["block"], 5)
    assert b["center_v1"] == block(x, y)
    assert b["ports_v0"] == [leaf(x, y + 5 * p) for p in range(4)]
for g in compressed["groups"]:
    x = g["group"]
    assert g["center_v2"] == head(x)
    assert g["blocks"] == list(range(5 * x, 5 * x + 5))


def left_action(u, v):
    perm = []
    for vertex in range(n):
        if vertex < 500:
            x, k = vertex % 25, vertex // 25
            perm.append(leaf((u + power[v] * x) % 25, (v + k) % 20))
        elif vertex < 625:
            x, b = divmod(vertex - 500, 5)
            perm.append(block((u + power[v] * x) % 25, (v + b) % 5))
        else:
            x = vertex - 625
            perm.append(head((u + power[v] * x) % 25))
    assert sorted(perm) == list(range(n))
    return perm


action_checks = []
for name, g in [("a", (1, 0)), ("d", (0, 1))]:
    perm = left_action(*g)
    mapped = {tuple(sorted((perm[u], perm[v]))) for u, v in original}
    assert mapped == original
    action_checks.append({"name": name, "element": list(g), "all_original_edges_preserved": True})

# The proven group formulas give all 500 actions; checking the two generators
# on the input verifies that the recovered labelling realizes these actions.
P = [(x, k) for x in range(25) for k in range(0, 20, 4)]
block_orbit = {block(x, k % 5) for x, k in P}
assert len(block_orbit) == 125
leaf_orbits = [{leaf(x, (k + c) % 20) for x, k in P} for c in range(4)]
assert all(len(o) == 125 for o in leaf_orbits)
assert set.union(*leaf_orbits) == set(range(500))
assert all({v // 25 % 4 for v in o} == {c} for c, o in enumerate(leaf_orbits))

pair_counts = Counter()
for u, v in leaf_edges:
    x, y = u % 25, v % 25
    assert x != y
    pair_counts[tuple(sorted((x, y)))] += 1
assert len(pair_counts) == 300
for (x, y), count in pair_counts.items():
    assert count == (5 if (y - x) % 5 == 0 else 3)

damage_path = ROOT / "research/ddp/m1_matching_joint/source650_diagnosis/diagnosis.edge_damage.tsv"
damage = {}
with damage_path.open() as f:
    for row in csv.DictReader(f, delimiter="\t"):
        damage[tuple(sorted((int(row["u"]), int(row["v"]))))] = int(row["bad_pairs"])
generators = []
for s in S:
    v = leaf(*s)
    generators.append({"element": list(s), "original_neighbor_of_leaf_zero": v,
                       "inverse": list(inverse(s)), "involution": inverse(s) == s,
                       "source_single_edge_damage": damage[(0, v)]})

result = {
    "status": "EXACT_LABELLED_ALGEBRAIC_RECONSTRUCTION",
    "group": {"translation_modulus": 25, "quotient_modulus": 20, "action": 2,
              "multiplication": "(x,k)(y,l)=(x+2^k*y mod25,k+l mod20)"},
    "generators": generators,
    "H": "(0,5j), j=0..3",
    "K": "(0,k), k=0..19",
    "labels": {"leaf": "x+25*k", "block": "500+5*x+(k mod5)", "head": "625+x"},
    "vertices": n, "leaf_edges": len(leaf_edges), "tree_edges": len(tree_edges),
    "all_1625_original_edges_exactly_reconstructed": True,
    "all_compressed_groups_blocks_and_ports_exactly_matched": True,
    "verified_automorphism_generators": action_checks,
    "proven_automorphism_subgroup_order": 500,
    "full_automorphism_group_recomputed": False,
    "normal_subgroup_P": "(x,4j), x in Z25,j in Z5; isomorphic C25 semidirect C5",
    "P_regular_on_125_blocks": True,
    "P_leaf_orbits": {"count": 4, "size_each": 125, "invariant": "k mod4"},
    "group_pair_multiplicity_histogram": dict(sorted(Counter(pair_counts.values()).items())),
    "five_edge_group_pairs": "exactly distinct x,y with x=y mod5",
    "cpu_seconds": time.process_time() - started,
    "scope": "One exact reconstruction and two explicit permutation checks; no isomorphism search or new candidate."
}
(HERE / "algebraic_reconstruction.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
