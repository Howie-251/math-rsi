"""Check the fixed distance-two quotient with audited four/five-bridge donors."""

from collections import Counter
from functools import cache
from hashlib import sha256
from itertools import combinations, permutations
import json
from time import process_time

from R7_MU3_BROAD_T15_DONOR_PROBE import (
    BITS, HERE, RESEARCH, accepted_cores, donor_interfaces, face, five_bridge_receivers,
    obstruction, receiver_plans,
)


SOURCE = HERE / "R7_DELTA2_DISTANCE2_GLOBAL_QUOTIENT.json"
OUTPUT = HERE / "R7_DELTA2_DISTANCE2_BROAD_PLANS.json"


def order_donor(plan):
    return plan["kind"] != "forced_split", plan["kind"] != "audited_exact_core"


def core_transport(groups, core):
    def image(x, p):
        return sum(((x >> i) & 1) << p[i] for i in range(6))

    for p in permutations(range(6)):
        if [sorted(image(x, p) for x in group) for group in groups] == [core["included"], core["omitted"]]:
            return p
    raise AssertionError("Marked coordinate transport missing")


def check(record, interfaces):
    colors = set(record["even"]), set(record["odd"])
    holes = colors[0] | colors[1]
    assert len(holes) == 14 and all((e ^ o) not in BITS for e in colors[0] for o in colors[1])
    edges = {}
    counts = Counter()
    for j, outer in enumerate(BITS):
        for side in (0, 1):
            for alpha, beta in (colors, colors[::-1]):
                a_alpha, a_beta = face(alpha, outer, side), face(beta, outer, side)
                if len(a_alpha) != 1 or len(a_beta) not in (5, 6):
                    continue
                a, = a_alpha
                b_alpha, b_beta = alpha - a_alpha, beta - a_beta
                four = len(a_beta) == 5
                counts["four_outer" if four else "five_outer"] += 1
                for x in combinations(sorted(a_beta), len(a_beta) - 3):
                    y = frozenset(p ^ outer for p in x)
                    for u in combinations(sorted(b_alpha), 2):
                        v = frozenset(p ^ outer for p in u)
                        assert not (y | v) & holes
                        find_receivers = receiver_plans if four else five_bridge_receivers
                        receivers = list(find_receivers(outer, b_beta, b_alpha - set(u), y))
                        if not receivers:
                            continue
                        counts["receiver_choices"] += 1
                        donors = interfaces(j, a, frozenset(a_beta - set(x)), v, x)
                        if not donors:
                            continue
                        counts["complete_choices"] += 1
                        base = dict(bridges=4 if four else 5, outer=j, donor_side=side, donor_minority=a,
                                    source_x=x, source_u=u, donor_markers=sorted(v), receiver_markers=sorted(y),
                                    donor=min(donors, key=order_donor))
                        for receiver in receivers:
                            plan = dict(base, receiver=receiver)
                            if receiver["universal"]:
                                return counts, edges, dict(kind="same_side_s2", plans=[plan])
                            edge = tuple(receiver["necessary_edge"])
                            edges.setdefault(edge, plan)
                        same_side = [q for q in receivers if q["kind"] == "same" and q["counts"][0] == 1]
                        for p, q in combinations(same_side, 2):
                            if p["minority"] != q["minority"] or p["direction"] == q["direction"]:
                                continue
                            if len(set(p["opposite_majority"]) & set(q["opposite_majority"])) in (0, 2):
                                plans = [dict(base, receiver=receiver) for receiver in (p, q)]
                                return counts, edges, dict(kind="same_side_double_cut", plans=plans)
    conflict = obstruction(edges, holes)
    if conflict:
        conflict["plans"] = [edges[tuple(edge)] for edge in conflict["edges"]]
    return counts, edges, conflict


def main():
    start = process_time()
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    records = source["representatives"]
    assert len(records) == 81
    cores = accepted_cores()
    profile_path = RESEARCH / "Q6_T15_ACTUAL_PROFILE.json"
    profile = {row["index"]: row for row in json.loads(profile_path.read_text(encoding="utf-8"))["orbits"]}

    @cache
    def interfaces(j, a, retained, marks, x):
        return donor_interfaces(j, a, retained, marks, x, cores)

    summary = Counter()
    rows = []
    for record in records:
        if process_time() - start >= 58:
            break
        counts, edges, result = check(record, interfaces)
        reference = {key: record[key] for key in ("pair", "even_a")}
        row = dict(reference=reference, even=record["even"], odd=record["odd"],
                   counts=dict(counts), necessary_edges=sorted(edges), result=result)
        if result:
            plans = result["plans"]
            summary[result["kind"]] += 1
        else:
            plans = list(edges.values())
            row["necessary_plans"] = plans
            summary["uncovered"] += 1
        for plan in plans:
            donor = plan["donor"]
            if donor["kind"] == "audited_exact_core" and "coordinate_transport" not in donor:
                donor["coordinate_transport"] = core_transport(
                    donor["normalized_groups"], profile[donor["index"]],
                )
        rows.append(row)

    sources = (
        SOURCE, HERE / "R7_MU3_BROAD_T15_DONOR_PROBE.py",
        HERE / "R7_MU3_FOUR_BRIDGE_SPLIT_DONOR_PROBE.py",
        RESEARCH / "Q6_T15_GOOD_ROOT_ALL_CLOSED.json", profile_path,
    )
    output = dict(status="complete" if len(rows) == len(records) else "cpu_limit_reached",
                  summary=dict(summary), rows=rows, accepted_core_count=len(cores),
                  source_sha256={str(path): sha256(path.read_bytes()).hexdigest() for path in sources},
                  ordinary_matching_calls=0, hamilton_calls=0, rank_runs=0,
                  cpu_seconds=process_time() - start)
    OUTPUT.write_text(json.dumps(output, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({key: val for key, val in output.items() if key != "rows"}))


if __name__ == "__main__":
    main()
