"""Check the controlled donor split only on four saved, realizable Q7 inputs."""
import json
from itertools import product
from pathlib import Path
from time import process_time

from PROBE import AXES, in_side, oriented_cut

HERE = Path(__file__).resolve().parent
INPUTS = ("GLOBAL_PROBE.json", "FREE_A6_SUPPLY.json",
          "FREE_A6_COUNT_PROBE.json", "FREE_A6_JOINT_PROBE.json")


def read_saved_input(filename):
    data = json.loads((HERE / filename).read_text(encoding="utf-8"))
    witness = next(row["candidate"] for row in data["solves"] if "candidate" in row)
    colors = tuple(tuple(witness[name]) for name in ("even_holes", "odd_holes"))
    matching = witness["matching"]
    endpoints = {v for edge in matching for v in edge}
    assert len(matching) == 56 and len(endpoints) == 112
    assert all((u ^ v).bit_count() == 1 for u, v in matching)
    assert set(range(128)) - endpoints == set(colors[0]) | set(colors[1])
    assert all(len(group) == 8 and all(v.bit_count() % 2 == c for v in group)
               for c, group in enumerate(colors))
    assert all((u ^ v).bit_count() != 1 for u in colors[0] for v in colors[1])
    assert min(abs(g) for g in witness["delta_even_minus_odd"]) == 3
    return colors, witness["delta_even_minus_odd"]


def check_cut(colors, outer, B_side):
    aa, ab, ba, bb = oriented_cut(colors, outer, B_side)
    r, s = len(aa), len(bb)
    k = len(ba)-s
    if k not in (3, 4, 5) or s > 2:
        return None
    assert len(ab) - r == k
    for inner in AXES:
        if inner == outer:
            continue
        for x in ab:
            # Label T by the actual inner bit containing x. Swapping the two
            # halves exchanges the same count conditions and return quotas.
            t = (x >> inner) & 1
            a, b = (len(in_side(group, inner, t)) for group in (aa, ab))
            q_T = b-a-1
            q_E = k-1-q_T
            if q_T not in (1, 2) or q_E not in (1, 2):
                continue
            if (q_T == 2 and a > 1) or (q_E == 2 and r-a > 1):
                continue
            available_T = in_side(ba, inner, t)
            available_E = in_side(ba, inner, 1-t)
            if len(available_T) < q_T or len(available_E) < q_E:
                continue
            U = sorted(available_T[:q_T] + available_E[:q_E])
            y = x ^ (1 << outer)
            V = sorted(u ^ (1 << outer) for u in U)
            holes = set(colors[0]) | set(colors[1])
            assert not (set(V) | {y}) & holes and len(set(V) | {y}) == k
            new_ab = (set(ab)-{x}) | set(V)
            new_ba = (set(ba)-set(U)) | {y}
            counts_T = (a, len(in_side(new_ab, inner, t)))
            counts_E = (r-a, len(in_side(new_ab, inner, 1-t)))
            assert counts_T[1]-counts_T[0] == 2*q_T
            assert counts_E[1]-counts_E[0] == 2*q_E
            assert (len(new_ba), len(bb)) == (s+2, s)
            return dict(outer=outer, donor_bit=1-B_side, receiver_bit=B_side,
                        alpha_parity=ba[0].bit_count() % 2, r=r, s=s, k=k,
                        x=x, U=U, y=y, V=V, inner=inner, T_bit=t,
                        epsilon=1, a=a, b=b, q_T=q_T, q_E=q_E,
                        return_capacities=[len(available_T), len(available_E)],
                        original_donor_halves=[(a,b), (r-a,len(ab)-b)],
                        modified_donor_halves=[counts_T, counts_E],
                        modified_receiver_holes=[sorted(new_ba), sorted(bb)],
                        modified_receiver_counts=(s+2,s))


def main():
    start = process_time()
    rows = []
    for filename in INPUTS:
        colors, delta = read_saved_input(filename)
        plans = [plan for j, b in product(AXES, (0, 1))
                 if (plan := check_cut(colors, j, b)) is not None]
        rows.append(dict(input=filename, delta=delta, covered=bool(plans),
                         plans_by_cut=plans))
    result = dict(cpu_seconds=process_time()-start, inputs=rows)
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n",
                                                  encoding="utf-8")
    for row in rows:
        plans = row["plans_by_cut"]
        print(row["input"], "covered", row["covered"],
              "directions", [(plan["outer"], plan["receiver_bit"]) for plan in plans],
              "first plan", plans[0] if plans else None)
    print("CPU seconds", result["cpu_seconds"])


if __name__ == "__main__":
    main()

