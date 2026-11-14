"""Check fixed E14 plans using split T15 donors and audited T26 receivers."""

from collections import Counter
from itertools import combinations
from pathlib import Path
from time import process_time
import json


HERE = Path(__file__).resolve().parent
BITS = tuple(1 << k for k in range(7))


def read(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def face(points, bit, side):
    return {p for p in points if bool(p & bit) == side}


def split_donors(outer, a, retained, marks, sources):
    for direction, bit in enumerate(BITS):
        if bit == outer:
            continue
        counts = [
            [int(bool(a & bit) == side), len(face(retained | marks, bit, side)),
             len(face(marks, bit, side))]
            for side in (0, 1)
        ]
        balanced = all(major - minor == 2 * marked for minor, major, marked in counts)
        if balanced:
            yield dict(direction=direction, counts=counts,
                       forced_positive_crossing=bool((sources[0] ^ sources[1]) & bit))


def receiver_plans(outer, minority, retained, marks):
    majority = retained | marks
    for direction, bit in enumerate(BITS):
        if bit == outer:
            continue
        for side in (0, 1):
            minor_here = face(minority, bit, side)
            s = len(minor_here)
            if s not in (1, 2):
                continue
            q = len(face(majority, bit, side))
            m = len(face(marks, bit, side))
            if (m, q) == (2, s + 3):
                kind = "same"
            elif (m, q) == (1, s + 1):
                kind = "separated"
            else:
                continue
            for a in sorted(minor_here):
                w = a ^ bit
                if w not in marks:
                    yield dict(kind=kind, direction=direction, side=side, minority=a,
                               counts=[s, q, m], w=w,
                               necessary_edge=sorted([w, w ^ outer]),
                               universal=(kind == "same" and s == 2),
                               opposite_majority=sorted(majority - face(majority, bit, side)))


def obstruction(edges, holes):
    endpoint = {}
    for edge in sorted(edges):
        for v in edge:
            if v in holes:
                return dict(kind="necessary_edge_touches_hole", edges=[edge])
            if v in endpoint:
                return dict(kind="necessary_edges_share_endpoint", edges=[endpoint[v], edge])
            endpoint[v] = edge
    for v in sorted(set(range(128)) - holes - endpoint.keys()):
        neighbors = {v ^ bit for bit in BITS} - holes
        if neighbors and neighbors <= endpoint.keys():
            return dict(kind="necessary_edges_leave_isolate", vertex=v,
                        edges=sorted({endpoint[u] for u in neighbors}))
    return None


def audit(row, frozen):
    colors = set(row["L"]), {127 ^ v for v in row["V"]}
    holes = colors[0] | colors[1]
    saved_matching = {tuple(sorted(edge)) for edge in frozen["short_matching"]}
    old_edges = {tuple(sorted(edge)) for edge in frozen["necessary_edges"]}
    assert len(saved_matching) == 57 and old_edges <= saved_matching
    assert {v for edge in saved_matching for v in edge} == set(range(128)) - holes
    assert all((a ^ b) in BITS for a, b in saved_matching)

    counts = Counter()
    plans = []
    for outer_index, outer in enumerate(BITS):
        for side in (0, 1):
            for alpha, beta in (colors, colors[::-1]):
                a_alpha, a_beta = face(alpha, outer, side), face(beta, outer, side)
                if (len(a_alpha), len(a_beta)) != (1, 5):
                    continue
                counts["outer"] += 1
                a, = a_alpha
                b_alpha, b_beta = alpha - a_alpha, beta - a_beta
                for x in combinations(sorted(a_beta), 2):
                    y = {v ^ outer for v in x}
                    for u in combinations(sorted(b_alpha), 2):
                        v = {p ^ outer for p in u}
                        counts["bridge_choices"] += 1
                        assert not (y | v) & holes
                        donors = list(split_donors(outer, a, a_beta - set(x), v, x))
                        accepted = [donor for donor in donors if donor["forced_positive_crossing"]]
                        receivers = list(receiver_plans(outer, b_beta, b_alpha - set(u), y))
                        if donors:
                            counts["any_balanced_donor"] += 1
                        if accepted:
                            counts["positive_donor"] += 1
                        if receivers:
                            counts["audited_receiver"] += 1
                        if not (accepted and receivers):
                            continue
                        counts["complete_bridge_choices"] += 1
                        double_cut = any(
                            p["kind"] == q["kind"] == "same" and p["counts"][0] == q["counts"][0] == 1
                            and p["minority"] == q["minority"] and p["direction"] != q["direction"]
                            and len(set(p["opposite_majority"]) & set(q["opposite_majority"])) in (0, 2)
                            for p, q in combinations(receivers, 2)
                        )
                        plans.append(dict(outer_direction=outer_index, donor_side=side,
                                          donor_minority=a, x=x, u=u, y=sorted(y), v=sorted(v),
                                          donor_cuts=accepted, receivers=receivers,
                                          universal_double_receiver_cut=double_cut))

    universal = any(plan["universal_double_receiver_cut"] or any(
        receiver["universal"] for receiver in plan["receivers"]) for plan in plans)
    new_edges = {tuple(receiver["necessary_edge"])
                 for plan in plans for receiver in plan["receivers"] if not receiver["universal"]}
    witness_fails_new_conditions = not universal and new_edges <= saved_matching
    return dict(id=row["id"], counts=dict(counts), plans=plans,
                universal_receiver=universal, old_necessary_edges=sorted(old_edges),
                new_necessary_edges=sorted(new_edges),
                absent_from_frozen_matching=sorted(new_edges - saved_matching),
                frozen_matching_fails_new_conditions=witness_fails_new_conditions,
                joint_obstruction=obstruction(new_edges | old_edges, holes))


def main():
    start = process_time()
    remaining = read("R7_MU3_REMAINDER_UPDATE.json")["remaining"]
    frozen = {row["id"]: row for row in read("R7_MU3_COVERAGE_RESIDUAL_MATCHING.json")["orbits"]}
    rows = []
    for row in remaining:
        rows.append(audit(row, frozen[row["id"]]))
        if process_time() - start >= 59:
            raise TimeoutError("Fixed probe exceeded its CPU budget")
    result = dict(scope="Fixed 14 E14 cases; split T15 donor and odd T26 receiver geometry",
                  ordinary_matching_enumerations=0, hamilton_calls=0, cpu_seconds=process_time() - start,
                  candidate_closures=[row["id"] for row in rows
                                      if row["universal_receiver"] or row["joint_obstruction"]], rows=rows)
    output = HERE / "R7_MU3_FOUR_BRIDGE_SPLIT_DONOR_PROBE.json"
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        print(row["id"], row["counts"], row["universal_receiver"], row["joint_obstruction"])


if __name__ == "__main__":
    main()
