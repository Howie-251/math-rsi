"""Bounded D=24 preflight on eight complete source representatives."""
from collections import Counter
from itertools import combinations
import json
from math import comb
from pathlib import Path
from time import process_time

from FREE_A6_SUPPLY import forward_supply
from NEW_SPLIT_CHECK import check_cut
from PROBE import AXES, MASK, axis_info, load, test_central

HERE = Path(__file__).resolve().parent
CPU_SECONDS = 60
FAMILIES = (
    (0, "one_side", 0, (0, 1, 2), (3, 4, 5)),
    (0, "outside", 6, (0, 1, 2), (3, 4, 5)),
    (1, "common", 0, (0, 1, 2), (0, 3, 4)),
    (1, "one_side", 1, (0, 1, 2), (0, 3, 4)),
    (1, "outside", 5, (0, 1, 2), (0, 3, 4)),
    (2, "common", 0, (0, 1, 2), (0, 1, 3)),
    (2, "one_side", 2, (0, 1, 2), (0, 1, 3)),
    (2, "outside", 4, (0, 1, 2), (0, 1, 3)),
)
TRIPLES = tuple(sum(1 << i for i in axes) for axes in combinations(AXES, 3))
Q_PARAMS = tuple((q, C, D) for q in AXES for C, D in combinations(TRIPLES, 2))
assert len(Q_PARAMS) == 4165


def group(missing, triple, other):
    return tuple(sorted({1 << i for i in AXES if i != missing} | {triple, other}))


def covering_gate(colors, lam):
    gap3 = [j for j in AXES if lam[j] == 5]
    for j in gap3:
        for b in (0, 1):
            accepted = axis_info(colors, j, b)["accepted_macros"]
            if accepted:
                return accepted[0]
    for j in AXES:
        if lam[j] == 4:
            for b in (0, 1):
                accepted = axis_info(colors, j, b)["accepted_macros"]
                if "four_mono_capacity" in accepted:
                    return "four_mono_capacity"
    for j in gap3:
        if forward_supply(colors, j, 0) or forward_supply(colors, j, 1):
            return "free_A6_same_side"
    for j in AXES:
        if 3 <= lam[j] <= 5 and (check_cut(colors, j, 0) or check_cut(colors, j, 1)):
            return "split_small_receiver"
    for j in gap3:
        for b in (0, 1):
            # Only one orientation can have a (6,3) receiver.
            if axis_info(colors, j, b)["counts"] != (2, 5, 6, 3):
                continue
            if test_central(colors, j, b)["joint_witness"] is not None:
                return "reverse_old_five"
    return None


def run():
    started = process_time()
    rows = []
    completed = True
    for t, position, p, A, B in FAMILIES:
        assert len(set(A) & set(B)) == t
        part = "common" if p in set(A) & set(B) else (
            "one_side" if p in set(A) | set(B) else "outside")
        assert part == position
        pa, pb = (sum(1 << i for i in support) for support in (A, B))
        P = group(p, pa, pb)
        p_load = [load(P, i) for i in AXES]
        counts = Counter()
        survivors = []
        for q, C, D in Q_PARAMS:
            if process_time()-started >= CPU_SECONDS:
                completed = False
                break
            counts["generated"] += 1
            # Units cannot have distance six from a triple. A pair of triples
            # has distance six exactly when their supports are disjoint.
            if any((p3 & q3) == 0 for p3 in (pa, pb) for q3 in (C, D)):
                counts["reject_nonindependent"] += 1
                continue
            Q = group(q, C, D)
            lam = tuple(p_load[i]+load(Q, i) for i in AXES)
            if min(lam) < 2 or max(lam) != 5:
                counts["reject_load"] += 1
                continue
            counts["admitted"] += 1
            colors = (tuple(sorted(MASK ^ v for v in Q)), P)
            gate = covering_gate(colors, lam)
            if gate is not None:
                counts[gate] += 1
                continue
            counts["outside_checked_gates"] += 1
            survivors.append(dict(q=q, C=C, D=D, Q=Q, lambda_by_axis=lam,
                                  even_holes=colors[0], odd_holes=colors[1]))
        pair_mass = len(TRIPLES)*comb(3,t)*comb(4,3-t)//2
        p_choices = {"common": t, "one_side": 2*(3-t), "outside": 1+t}[position]
        next_Q = None if counts["generated"] == len(Q_PARAMS) else Q_PARAMS[counts["generated"]]
        rows.append(dict(t=t, position=position, missing_unit=p, A=A, B=B,
                         P=P, first_group_orbit_mass=pair_mass*p_choices,
                         next_Q_parameter=next_Q, counts=counts, surviving_inputs=survivors))
        if not completed:
            break
    total = Counter()
    for row in rows:
        total.update(row["counts"])
    if completed:
        assert len(rows) == 8 and total["generated"] == 33320
        assert sum(row["first_group_orbit_mass"] for row in rows) == 4165
    return dict(cpu_limit_seconds=CPU_SECONDS, cpu_seconds=process_time()-started,
                complete=completed, maximum_parameters=33320,
                parameters_per_source_family=len(Q_PARAMS), total=total, families=rows)


if __name__ == "__main__":
    data = run()
    Path(__file__).with_suffix(".json").write_text(json.dumps(data, indent=2)+"\n",
                                                  encoding="utf-8")
    print(data["complete"], data["cpu_seconds"], dict(data["total"]), flush=True)
    for row in data["families"]:
        print(row["t"], row["position"], dict(row["counts"]), flush=True)

