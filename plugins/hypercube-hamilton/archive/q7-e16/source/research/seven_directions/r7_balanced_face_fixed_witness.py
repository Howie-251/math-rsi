"""Construct and check exactly one prescribed 59-edge input; no family search."""
import json
from pathlib import Path


def edge(x, y):
    return tuple(sorted((x, y)))


def face(b, chains, switch_directions):
    forbidden = {0, 3}
    for d, e, f in chains:
        forbidden.update((d, d ^ e, d ^ e ^ f))
    matching = {edge(x, x ^ b) for x in range(64) if not x & b}
    for x in forbidden:
        matching.remove(edge(x, x ^ b))
    for d, e, f in chains:
        matching.update((edge(d, d ^ e), edge((d ^ e) ^ b, (d ^ e ^ f) ^ b)))
    used = set(forbidden)
    switches = []
    for q in switch_directions:
        pairs = ((x, x ^ q) for x in range(64) if not x & b and x < (x ^ q))
        x, y = next((x, y) for x, y in pairs if x not in used and y not in used)
        matching.remove(edge(x, x ^ b))
        matching.remove(edge(y, y ^ b))
        matching.update((edge(x, y), edge(x ^ b, y ^ b)))
        used.update((x, y))
        switches.append([q, x, y])
    covered = [v for xy in matching for v in xy]
    assert len(covered) == len(set(covered))
    return {
        "base_mask": b, "chains_d_e_f": chains,
        "square_switches_q_x_y": switches,
        "edges": sorted(matching),
        "holes_before_bridges": sorted(set(range(64)) - set(covered)),
        "direction_counts": [sum(x ^ y == 1 << i for x, y in matching) for i in range(6)],
    }


def build():
    a = face(32, [(12, 1, 2), (24, 1, 2)], [4, 8, 16])
    b = face(16, [(6, 8, 2)], [1, 2, 4, 8, 32])
    matching = a["edges"] + [(x + 64, y + 64) for x, y in b["edges"]] + [(0, 64), (3, 67)]
    covered = [v for xy in matching for v in xy]
    assert len(matching) == 59
    assert len(covered) == len(set(covered)) == 118
    assert all((x ^ y).bit_count() == 1 for x, y in matching)
    holes = sorted(set(range(128)) - set(covered))
    evens = [x for x in holes if x.bit_count() % 2 == 0]
    odds = [x for x in holes if x.bit_count() % 2 == 1]
    assert evens == [15, 27, 80, 83, 86]
    assert odds == [32, 35, 44, 56, 76]
    assert all((x ^ y).bit_count() != 1 for x in holes for y in holes)
    counts = [sum(x ^ y == 1 << i for x, y in matching) for i in range(7)]
    assert counts[6] == 2 and min(counts[:6]) > 2
    assert all(t >= 2 for t in a["direction_counts"] + b["direction_counts"])
    # The only two-edge direction is 6; ports 0,3 differ in coordinates 0,1.
    # T needs a missing separating direction; U/V/W need a single one.
    assert all(a["direction_counts"][i] >= 2 and b["direction_counts"][i] >= 2 for i in [0, 1])
    plus_even = [x for x in evens if x & 4]
    plus_odd = [x for x in odds if x & 4]
    assert plus_even == [15, 86] and plus_odd == [44, 76]
    return {
        "scope": "one prescribed fixed input; deterministic local square choices, no family search",
        "A_local": a, "B_local": b, "M": sorted(matching),
        "holes": holes, "even_holes": evens, "odd_holes": odds,
        "direction_counts": counts, "m": 2, "unique_two_edge_direction": 6,
        "maximal_short_matching": True,
        "balanced_cut": {"coordinate": 2, "bit": 1,
                         "even_holes": plus_even, "odd_holes": plus_odd,
                         "complement_even_holes": [x for x in evens if not x & 4],
                         "complement_odd_holes": [x for x in odds if not x & 4]},
        "T_U_V_W_exclusion": "Only j=6 has two edges; D_j={0,1}; both j-faces have at least two prescribed edges in each separating direction.",
        "E8_augmentation_exclusion": "Independent ten-hole set makes this 59-edge short matching maximal; no strict short supermatching, hence none with at least 60 edges.",
    }


if __name__ == "__main__":
    result = build()
    path = Path(__file__).with_name("R7_BALANCED_FACE_SPLICE_WITNESS.json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("direction_counts", "even_holes", "odd_holes", "balanced_cut")}, ensure_ascii=False))
