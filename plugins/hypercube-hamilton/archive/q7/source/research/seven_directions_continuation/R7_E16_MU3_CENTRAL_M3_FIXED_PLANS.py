"""Check the frozen central m=3 basis using the accepted all-axis interfaces."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from time import process_time
from unittest.mock import patch

from R7_E16_MU3_CENTRAL_M3_BASE import physical_colors
from R7_E16_MU3_GAP7_EVEN_D30_FIXED_PLANS import K3_AUDITED_DONORS
import R7_E16_MU3_GAP7_EVEN_MINIMAL_FIXED_PLANS as gates


BASE = Path(__file__).with_name("R7_E16_MU3_CENTRAL_M3_BASE.json")
BASE_SHA256 = "487328e408fc2bf590dea9e751e61e460189652fcd56d8f60f574830220c0d94"
EXPECTED = 45_924
CPU_LIMIT = 150


def run(start):
    raw = BASE.read_bytes()
    assert sha256(raw).hexdigest() == BASE_SHA256
    data = json.loads(raw)
    rows = data["records"]
    assert data["status"] == "complete" and data["record_count"] == len(rows) == EXPECTED
    accepted = gates.accepted
    broad = accepted.joint.broad_returns
    old_surviving = broad.surviving
    old_supplier = gates.supplier

    def surviving_optional(edge, outer, side, omitted):
        return None if edge is None else old_surviving(edge, outer, side, omitted)

    def audited_supplier(outer, minor, retained, marks, lookup, t26):
        plan = old_supplier(outer, minor, retained, marks, lookup, t26)
        return plan if plan and plan["kind"] in K3_AUDITED_DONORS else None

    lookup_t15 = gates.make_t15_lookup()
    search = dict(lookup=None, broad=None)
    status = "complete"
    failure = None
    positives = []
    with (
        patch.object(gates.previous, "directed_cuts", gates.directed_cuts),
        patch.object(gates, "supplier", audited_supplier),
        patch.object(accepted, "CPU_LIMIT", CPU_LIMIT),
        patch.object(gates.previous.four_limits, "CPU_LIMIT", CPU_LIMIT),
        patch.object(broad, "CPU_LIMIT", CPU_LIMIT),
        patch.object(broad, "surviving", surviving_optional),
        patch.object(broad, "whole_interface", accepted.balanced_whole_wrapper(broad.whole_interface)),
    ):
        for index, row in enumerate(rows):
            colors = physical_colors(*(row[key] for key in ("S", "W", "Y", "U")))
            gaps = tuple(len(gates.face(colors[0], i, 1)) - len(gates.face(colors[1], i, 1))
                         for i in gates.AXES)
            assert gaps == tuple(row["signed_gaps"]) and gaps[6] == 3 and all(3 <= abs(d) <= 6 for d in gaps)
            counters = Counter()
            try:
                accepted.check_time(start)
                high = gates.previous.high_m_witnesses(colors)
                plan = dict(gate="accepted_high_m", witnesses=high) if high else None
                plan = (plan or accepted.joint.counts_orbits(colors) or gates.previous.four_mono(colors)
                        or accepted.controlled_count(colors)
                        or gates.k3_whole(colors, lookup_t15, {}, counters, start)
                        or gates.previous.first_plan(colors, gaps, search, counters, start))
                accepted.check_time(start)
            except TimeoutError:
                status = "cpu_limit"
                plan = None
            if plan is None:
                if status != "cpu_limit":
                    status = "first_unsupported"
                failure = dict(
                    index=index, representative=row, physical_colors=colors, signed_gaps=gaps,
                    cuts=[dict(outer=outer, A_side=1-b_side, alpha_parity=alpha,
                               shape=tuple(tuple(map(len, groups)) for groups in (donor, receiver)))
                          for outer, b_side, alpha, donor, receiver in gates.directed_cuts(colors)],
                    counters=dict(counters),
                )
                break
            assert plan.get("required_forced_edge") is None
            positives.append(dict(index=index, plan=plan))
    visited = len(positives)+int(failure is not None)
    return dict(status=status, base_sha256=BASE_SHA256, input_representatives=EXPECTED,
                visited=visited, unvisited=EXPECTED-visited, cpu_seconds=process_time()-start,
                cpu_limit_seconds=CPU_LIMIT, first_failure=failure, positives=positives,
                plan_counts=Counter(row["plan"]["gate"] for row in positives),
                k3_donor_counts=Counter(row["plan"]["donor"]["kind"] for row in positives
                                        if row["plan"]["gate"] == "k3_whole_receiver"),
                new_geometries=0, original_matchings_enumerated=0, solver_calls=0, rank_runs=0)


if __name__ == "__main__":
    result = run(process_time())
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as file:
        json.dump(result, file, separators=(",", ":"))
        file.write("\n")
    print(json.dumps({k:v for k,v in result.items() if k != "positives"}, indent=2))
