"""Arithmetic verification of one fixed xor-3 transport; no search or solver.

Python standard library only. The fixed B edges are copied from the previous
prescribed-input probe. A is their image under local x -> x xor 3.
"""
import argparse
import json
from pathlib import Path

B_EDGES = [(1, 5), (2, 18), (4, 6), (7, 39), (8, 10), (9, 13),
           (11, 27), (14, 15), (16, 48), (17, 21), (19, 51), (22, 23),
           (24, 26), (25, 29), (28, 30), (32, 34), (33, 37), (35, 43),
           (36, 38), (41, 57), (42, 46), (44, 45), (49, 53), (50, 58),
           (52, 54), (56, 60), (62, 63)]
ANCHORS = {0, 3}


def counts(edges, dimensions):
    return [sum((u ^ v) == 1 << k for u, v in edges) for k in range(dimensions)]


def build():
    a_edges = sorted(tuple(sorted((u ^ 3, v ^ 3))) for u, v in B_EDGES)
    b_edges = sorted(B_EDGES)
    result = {"construction": "fixed B copied; A=B xor 3; no search",
              "search_calls": 0, "faces": {}, "margin_gates": []}
    hole_sets = {}
    for name, edges in (("A", a_edges), ("B", b_edges)):
        endpoints = [x for e in edges for x in e]
        assert len(edges) == 27 and len(set(endpoints)) == len(endpoints) == 54
        assert all((u ^ v).bit_count() == 1 for u, v in edges)
        internal_free = set(range(64)) - set(endpoints)
        assert ANCHORS <= internal_free
        holes = internal_free - ANCHORS
        odd = {x for x in holes if x.bit_count() % 2}
        even = holes - odd
        hole_sets[name] = holes
        assert len(odd) == 5 and len(even) == 3
        assert not any((u ^ v).bit_count() == 1 for u in holes for v in holes)
        anchor_to_odd = [(d, z) for d in sorted(ANCHORS) for z in sorted(odd)
                         if (d ^ z).bit_count() == 1]
        assert not anchor_to_odd
        result["faces"][name] = {"edges": edges, "local_odd_holes": sorted(odd),
            "local_even_holes": sorted(even), "internal_matching_free": sorted(internal_free),
            "direction_counts": counts(edges, 6), "f": 5,
            "anchor_to_odd_hole_edges": anchor_to_odd}
        for d in sorted(ANCHORS):
            for k in range(6):
                ox = sum((x >> k & 1) != (d >> k & 1) for x in odd)
                ex = sum((x >> k & 1) != (d >> k & 1) for x in even)
                result["margin_gates"].append({"response_face": name, "anchor": d,
                    "coordinate": k, "odd_in_opposite_half": ox,
                    "even_in_opposite_half": ex, "delta": ox - ex,
                    "gate_pass": ox - ex in (0, 1)})
    assert result["faces"]["A"]["local_odd_holes"] == [28, 44, 52, 56, 62]
    assert result["faces"]["A"]["local_even_holes"] == [15, 23, 43]
    assert hole_sets["A"] == {x ^ 3 for x in hole_sets["B"]}
    assert not hole_sets["A"] & hole_sets["B"]
    # Transport must preserve every old partner and each edge direction.
    partner_a = {x: y for u, v in a_edges for x, y in ((u, v), (v, u))}
    partner_b = {x: y for u, v in b_edges for x, y in ((u, v), (v, u))}
    assert all(partner_a[x ^ 3] == (y ^ 3) for x, y in partner_b.items())
    assert {x ^ 3 for x in ANCHORS} == ANCHORS
    edges = a_edges + [(u + 64, v + 64) for u, v in b_edges] + [(0, 64), (3, 67)]
    edges.sort()
    endpoints = [x for e in edges for x in e]
    holes = set(range(128)) - set(endpoints)
    assert holes == hole_sets["A"] | {x + 64 for x in hole_sets["B"]}
    assert len(edges) == 56 and len(set(endpoints)) == len(endpoints) == 112
    assert all((u ^ v).bit_count() == 1 for u, v in edges)
    hole_edges = [(u, v) for u in sorted(holes) for v in sorted(holes)
                  if u < v and (u ^ v).bit_count() == 1]
    assert not hole_edges
    direction_counts = counts(edges, 7)
    assert direction_counts == [8, 14, 16, 4, 6, 6, 2]
    assert all(min(f["direction_counts"]) >= 2 for f in result["faces"].values())
    assert not any(g["gate_pass"] for g in result["margin_gates"])
    even_holes = {x for x in holes if x.bit_count() % 2 == 0}
    odd_holes = holes - even_holes
    internal_common_free = (set(range(64)) - set(partner_a)) & (
        set(range(64)) - set(partner_b))
    assert internal_common_free == ANCHORS
    result.update({"status": "FIXED_JOINT_RESIDUAL_WITNESS_VERIFIED",
        "edges": edges, "edge_count": 56, "direction_counts": direction_counts,
        "minimum_positive_direction_count": 2, "two_edge_directions": [6],
        "holes": sorted(holes), "hole_count": len(holes),
        "global_even_holes": sorted(even_holes), "global_odd_holes": sorted(odd_holes),
        "global_hole_bit1_marginals_even_odd": [
            [sum(x >> k & 1 for x in even_holes), sum(x >> k & 1 for x in odd_holes)]
            for k in range(7)],
        "hole_edges": hole_edges, "inclusion_maximal": True,
        "common_local_global_holes": sorted(hole_sets["A"] & hole_sets["B"]),
        "common_local_internal_free": sorted(internal_common_free),
        "xor3_all_partner_relations_preserved": True,
        "all_24_margin_gates_fail": True,
        "F7_source_cut_four_free_f5_unavailable": True,
        "F_two_face_four_free_f5_unavailable": True,
        "scope": "joint residual of the specifically listed criteria; not an R7 counterexample"})
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = build()
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
        print(json.dumps({k: result[k] for k in ("status", "edge_count", "direction_counts")},
                         ensure_ascii=False))
    else:
        print(payload, end="")
