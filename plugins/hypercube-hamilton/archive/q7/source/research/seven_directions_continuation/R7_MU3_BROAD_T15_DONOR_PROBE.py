"""Check four/five-bridge donors against split and audited six-dimensional interfaces."""

from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
from time import process_time
import json

from R7_MU3_FOUR_BRIDGE_SPLIT_DONOR_PROBE import (
    BITS, HERE, face, obstruction, read, receiver_plans, split_donors,
)


RESEARCH = Path("E:/新问题/research/seven_directions")
ORDERS = [(a, b) for a in permutations(range(3)) for b in permutations(range(3, 5))]


def project(point, coordinate):
    low = (1 << coordinate) - 1
    return (point & low) | ((point >> (coordinate + 1)) << coordinate)


def marked_signature(retained, marks):
    points = (*retained, *marks)
    columns = [tuple((p >> k) & 1 for p in points) for k in range(6)]
    return min(tuple(sorted(sum(column[j] << i for i, j in enumerate((*a, *b)))
                            for column in columns))
               for a, b in ORDERS)


def accepted_cores():
    registry = json.loads((RESEARCH / "Q6_T15_GOOD_ROOT_ALL_CLOSED.json").read_text(encoding="utf-8"))
    profile = json.loads((RESEARCH / "Q6_T15_ACTUAL_PROFILE.json").read_text(encoding="utf-8"))
    core_ids = {row["core_index"] for row in registry["cores"]}
    assert len(core_ids) == 1017
    # Individually closed after the audited GOOD_ROOT union.
    core_ids.update({85, 386, 1007, 1054, 2189})
    cores = {marked_signature(row["included"], row["omitted"]): row["index"]
             for row in profile["orbits"] if row["index"] in core_ids}
    assert len(cores) == 1022
    return cores


def donor_interfaces(outer, a, retained, marks, x, cores):
    result = []
    # For five bridges, each eligible pair can be prescribed in the free set D.
    for pair in combinations(x, 2):
        for plan in split_donors(1 << outer, a, retained, marks, pair):
            if plan["forced_positive_crossing"]:
                result.append(dict(plan, kind="forced_split", prescribed_pair=pair))
    all_holes = {a} | retained | marks
    for k, bit in enumerate(BITS):
        if k == outer:
            continue
        partition = [face(all_holes, bit, side) for side in (0, 1)]
        if any(not side for side in partition):
            result.append(dict(kind="audited_easy_same_face", direction=k))
        for side in partition:
            if len(side) == 1 and side <= marks:
                result.append(dict(kind="audited_easy_isolated_mark", direction=k, isolated_mark=next(iter(side))))
    groups = (sorted(project(p ^ a, outer) for p in retained), sorted(project(p ^ a, outer) for p in marks))
    index = cores.get(marked_signature(*groups))
    if index is not None:
        result.append(dict(kind="audited_exact_core", index=index, normalized_groups=groups))
    return result


def five_bridge_receivers(outer, minority, retained, marks):
    a, = minority
    majority = retained | marks
    for k, bit in enumerate(BITS):
        if bit == outer:
            continue
        side = int(bool(a & bit))
        if (len(face(majority, bit, side)), len(face(marks, bit, side))) != (4, 2):
            continue
        w = a ^ bit
        if w not in marks:
            yield dict(kind="T17", direction=k, side=side, minority=a, w=w,
                       necessary_edge=sorted((w, w ^ outer)), universal=False)


def audit(row, frozen, cores):
    colors = set(row["L"]), {127 ^ v for v in row["V"]}
    holes = colors[0] | colors[1]
    old_edges = {tuple(sorted(edge)) for edge in frozen["necessary_edges"]}
    saved_matching = {tuple(sorted(edge)) for edge in frozen["short_matching"]}
    assert old_edges <= saved_matching
    plans = []
    counts = {"four": Counter(), "five": Counter()}
    for j, outer in enumerate(BITS):
        for side in (0, 1):
            for alpha, beta in (colors, colors[::-1]):
                a_alpha, a_beta = face(alpha, outer, side), face(beta, outer, side)
                if len(a_alpha) != 1 or len(a_beta) not in (5, 6):
                    continue
                gate = "four" if len(a_beta) == 5 else "five"
                stat = counts[gate]
                stat["outer"] += 1
                a, = a_alpha
                b_alpha, b_beta = alpha - a_alpha, beta - a_beta
                for x in combinations(sorted(a_beta), len(a_beta) - 3):
                    y = {v ^ outer for v in x}
                    for u in combinations(sorted(b_alpha), 2):
                        v = {p ^ outer for p in u}
                        stat["bridge_choices"] += 1
                        assert not (y | v) & holes
                        donors = donor_interfaces(j, a, a_beta - set(x), v, x, cores)
                        receiver_scan = receiver_plans if gate == "four" else five_bridge_receivers
                        receivers = list(receiver_scan(outer, b_beta, b_alpha - set(u), y))
                        if donors:
                            stat["donor"] += 1
                            for kind in {p["kind"] for p in donors}:
                                stat[kind] += 1
                        if receivers:
                            stat["receiver"] += 1
                        if donors and receivers:
                            stat["complete_bridge_choices"] += 1
                            plans.append(dict(gate=gate, outer_direction=j, donor_side=side, donor_minority=a,
                                              x=x, u=u, y=sorted(y), v=sorted(v), donors=donors, receivers=receivers))
    universal = any(q["universal"] for p in plans for q in p["receivers"])
    edges = {tuple(q["necessary_edge"]) for p in plans for q in p["receivers"] if not q["universal"]}
    return dict(id=row["id"], counts={gate: dict(c) for gate, c in counts.items()}, plans=plans,
                universal=universal, absent_from_frozen_matching=sorted(edges - saved_matching),
                old_necessary_edges=sorted(old_edges), new_necessary_edges=sorted(edges),
                joint_obstruction=obstruction(edges | old_edges, holes))


def main():
    start = process_time()
    cores = accepted_cores()
    remaining = read("R7_MU3_REMAINDER_UPDATE.json")["remaining"]
    four_rows = read("R7_MU3_FOUR_BRIDGE_SPLIT_DONOR_PROBE.json")
    closed_by_four = set(four_rows["candidate_closures"])
    frozen = {row["id"]: row for row in read("R7_MU3_COVERAGE_RESIDUAL_MATCHING.json")["orbits"]}
    results = []
    for row in remaining:
        if row["id"] in closed_by_four:
            continue
        result = audit(row, frozen[row["id"]], cores)
        results.append(result)
        if process_time() - start >= 59:
            raise TimeoutError("Fixed probe exceeded its CPU budget")
        print(result["id"], result["counts"], result["universal"], result["joint_obstruction"])
    data = dict(scope="Fixed 14 E14 remainder after positive split four-bridge candidates",
                ordinary_matching_enumerations=0, hamilton_calls=0, cpu_seconds=process_time() - start,
                closed_by_four=sorted(closed_by_four), rows=results)
    (HERE / "R7_MU3_BROAD_T15_DONOR_PROBE.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
