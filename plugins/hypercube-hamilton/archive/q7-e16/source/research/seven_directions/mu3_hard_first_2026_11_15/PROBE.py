"""Bounded random Q7 double-graph probe, with one ordinary matching witness."""
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
from random import Random
from time import process_time

SEED = 20261115
LIMIT = 200
CPU_LIMIT = 60
AXES = tuple(range(7))
MASK = (1 << 7) - 1
EDGES = tuple((1 << a) | (1 << b) for a, b in combinations(AXES, 2))
GATES = ("balanced_complement", "majority_root", "two_majority_roots",
         "two_minority_roots", "single_root")


def in_side(vertices, axis, side):
    return tuple(v for v in vertices if ((v >> axis) & 1) == side)


def load(vertices, axis):
    return sum((v >> axis) & 1 for v in vertices)


def oriented_cut(colors, axis, receiver_bit):
    donor = tuple(in_side(group, axis, 1 - receiver_bit) for group in colors)
    receiver = tuple(in_side(group, axis, receiver_bit) for group in colors)
    alpha = int(len(receiver[1]) > len(receiver[0]))
    return donor[alpha], donor[1-alpha], receiver[alpha], receiver[1-alpha]


def controlled_count(ab, ba, bb, k):
    counts = (
        (load(ab, k), load(ba, k), load(bb, k)),
        (len(ab) - load(ab, k), len(ba) - load(ba, k),
         len(bb) - load(bb, k)),
    )
    return all(major - minor in (1, 2) and sources >= major - minor
               and (major - minor == 1 or minor <= 1)
               for sources, major, minor in counts)


def axis_info(colors, outer, receiver_bit):
    aa, ab, ba, bb = oriented_cut(colors, outer, receiver_bit)
    inner = tuple(k for k in AXES if k != outer)
    counts = tuple(map(len, (aa, ab, ba, bb)))
    columns = [(k, load(ba, k), load(bb, k)) for k in inner]
    s = sum(c-d in (1, 2) for _, c, d in columns)
    strong_axes = [k for k, c, d in columns if (c, d) in ((2, 0), (3, 2))]
    h = (bb[0] ^ bb[1]).bit_count() if len(bb) == 2 else None
    controlled_axes = [k for k in inner if controlled_count(ab, ba, bb, k)]
    four_mono_balanced = sum(c == 2 for _, c, _ in columns) if counts == (4, 8, 4, 0) else None
    macros = []
    if counts == (5, 8, 3, 0):
        macros.append("three_mono")
    if counts == (4, 7, 4, 1):
        macros.append("R41")
    if four_mono_balanced is not None and four_mono_balanced >= 3:
        macros.append("four_mono_capacity")
    if len(ba) - len(bb) == 3 and controlled_axes:
        macros.append("controlled_count")
    if counts == (3, 6, 5, 2):
        if h == 6:
            macros.append("central_h6")
        if s >= 3:
            macros.append("central_s_ge_3")
        if s >= 2 and strong_axes:
            macros.append("central_s_ge_2_strong")
    return dict(axis=outer, receiver_bit=receiver_bit, counts=counts,
                receiver_root_distance=h, columns=columns, scarcity_s=s,
                strong_axes=strong_axes, controlled_count_axes=controlled_axes,
                four_mono_balanced=four_mono_balanced, accepted_macros=macros)


def donor_gates(r, a, ell):
    # In these central orientations r is 2 or 3. The appendix's complement
    # conditions reduce to those below.
    return (
        a in (0, 1) and ell == 4,
        a in (0, 1) and ell == 5,
        a in (0, 1) and ell == 6 and r-a in (2, 3),
        a == 2 and ell == 3,
        a == 1 and ell == 3,
    )


def test_central(colors, outer, receiver_bit):
    aa, ab, ba, bb = oriented_cut(colors, outer, receiver_bit)
    r = len(aa)
    assert tuple(map(len, (aa, ab, ba, bb))) in ((3, 6, 5, 2), (2, 5, 6, 3))
    inner = tuple(k for k in AXES if k != outer)
    tuples = Counter()
    gates = {name: Counter() for name in GATES}
    receiver_witness = None
    joint_witness = None
    for x in ab:
        y = x ^ (1 << outer)
        for k in inner:
            side = (y >> k) & 1
            ba_inside = set(in_side(ba, k, side))
            g = len(ba_inside) - len(in_side(bb, k, side))
            receiving_gap = 1 <= g <= 3
            if receiving_gap and len(ba_inside) >= g-1 and len(ba)-len(ba_inside) >= 3-g:
                tuples["receiver_only_xS"] += 1
                if receiver_witness is None:
                    returns = sorted(ba_inside)[:g-1] + sorted(set(ba)-ba_inside)[:3-g]
                    receiver_witness = dict(x=x, S=[k, side], returns=returns)
            for t in inner:
                for t_side in (0, 1):
                    tuples["xST"] += 1
                    a, b = (len(in_side(group, t, t_side)) for group in (aa, ab))
                    ell = b - int(((x >> t) & 1) == t_side) + 2 - a
                    phi = donor_gates(r, a, ell)
                    available = set(in_side(ba, t, t_side))
                    i = len(available & ba_inside)
                    j = len(available - ba_inside)
                    if not any(phi):
                        failure = "no_donor_gate"
                    elif not receiving_gap:
                        failure = "receiver_gap"
                    elif i < g-1 and j < 3-g:
                        failure = "both_capacities"
                    elif i < g-1:
                        failure = "inside_capacity"
                    elif j < 3-g:
                        failure = "outside_capacity"
                    else:
                        failure = "joint_pass"
                        if joint_witness is None:
                            returns = (sorted(available & ba_inside)[:g-1]
                                       + sorted(available - ba_inside)[:3-g])
                            joint_witness = dict(x=x, S=[k, side], T=[t, t_side],
                                                 returns=returns,
                                                 gate=GATES[phi.index(True)])
                    tuples[failure] += 1
                    for name, applies in zip(GATES, phi):
                        if applies:
                            gates[name][failure] += 1
    return dict(counts=tuples, gates=gates, receiver_witness=receiver_witness,
                joint_witness=joint_witness)


def short_matching(colors):
    holes = set(colors[0]) | set(colors[1])
    even = [v for v in range(128) if v.bit_count() % 2 == 0 and v not in holes]
    owner = {}

    def augment(v, seen):
        for k in AXES:
            w = v ^ (1 << k)
            if w in seen or w in holes:
                continue
            seen.add(w)
            if w not in owner or augment(owner[w], seen):
                owner[w] = v
                return True
        return False

    if not all(augment(v, set()) for v in even):
        return None
    matching = sorted((v, w) for w, v in owner.items())
    covered = {v for edge in matching for v in edge}
    assert len(matching) == 56 and len(covered) == 112
    assert covered == set(range(128))-holes
    assert all((v ^ w).bit_count() == 1 for v, w in matching)
    return matching


def graph_degrees(graph):
    return tuple(load(graph, k) for k in AXES)


def graph_edges(graph):
    return [tuple(k for k in AXES if (e >> k) & 1) for e in graph]


def run():
    start = process_time()
    rng = Random(SEED)
    counts = Counter()
    macro_hits = Counter()
    witness = None
    while counts["eligible_pairs"] < LIMIT and process_time() - start < CPU_LIMIT:
        counts["draws"] += 1
        g1 = sorted(rng.sample(EDGES, 7))
        g2 = sorted(rng.sample(EDGES, 7))
        d1, d2 = graph_degrees(g1), graph_degrees(g2)
        degree = tuple(a+b for a, b in zip(d1, d2))
        if min(degree) != 2 or max(degree) != 5:
            continue
        if any(d == 2 and d1[k] != 1 for k, d in enumerate(degree)):
            continue
        counts["eligible_pairs"] += 1
        colors = [(0, *g1), tuple(sorted(MASK ^ q for q in (0, *g2)))]
        assert sum(d1) + sum(d2) == 28
        delta = [load(colors[0], k) - load(colors[1], k) for k in AXES]
        assert delta == [d-8 for d in degree]
        assert min(map(abs, delta)) == 3
        assert all((v ^ w).bit_count() != 1 for v in colors[0] for w in colors[1])
        metrics = [axis_info(colors, axis, side) for axis in AXES for side in (0, 1)]
        hits = {macro for m in metrics for macro in m["accepted_macros"]}
        if hits:
            counts["old_macro"] += 1
            macro_hits.update(hits)
            continue
        central = [m for m in metrics if abs(delta[m["axis"]]) == 3]
        for row in central:
            row["five_gates"] = test_central(colors, row["axis"], row["receiver_bit"])
        if any(row["five_gates"]["receiver_witness"] is None for row in central):
            counts["receiver_failure_macro"] += 1
            macro_hits["receiver_failure"] += 1
            continue
        if any(row["five_gates"]["joint_witness"] is not None for row in central):
            counts["five_gate_pass"] += 1
            continue
        counts["outside_five_gates"] += 1
        matching = short_matching(colors)
        if matching is None:
            counts["outside_five_gates_unrealizable"] += 1
            continue
        witness = dict(g1=graph_edges(g1), g2=graph_edges(g2),
                       even_holes=colors[0], odd_holes=colors[1],
                       g1_degrees=d1, g2_degrees=d2, degree=degree,
                       delta_even_minus_odd=delta, axis_metrics=metrics,
                       matching=matching)
        break
    return dict(seed=SEED, eligible_pair_limit=LIMIT, cpu_limit=CPU_LIMIT,
                cpu_seconds=process_time()-start, counts=counts,
                macro_hits=macro_hits, witness=witness)


if __name__ == "__main__":
    result = run()
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n",
                                                  encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "witness"}))
    if result["witness"] is not None:
        for key in ("even_holes", "odd_holes", "delta_even_minus_odd"):
            print(key, result["witness"][key])

