"""One fixed-base run of unconditional E16 gates for the m=3 branch."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from time import process_time
from unittest.mock import patch

import R7_E16_D35_B14_ZERO_SOURCE_CHECK as accepted
import R7_E16_ODD_22_JOINT_COVERAGE as four_limits


HERE = Path(__file__).resolve().parent
BASE = HERE / "E16_MU3_ROUTE_R41_M3_COMPLETION_BASE.json"
BASE_SHA256 = "b25f5f6895cfb0ce161a4d1151fff674390e00f2148abd5f1d3b0eac9bcb197e"
EXPECTED = 3785
CPU_LIMIT = 60


def first_plan(colors, gaps, search, counters, start):
    plan = accepted.joint.counts_orbits(colors) or accepted.controlled_count(colors)
    if plan:
        return plan
    _, exclusion = accepted.joint.forced_original_edges(colors)
    if exclusion:
        return dict(gate="impossible_geometry", exclusion=exclusion)
    if search["lookup"] is None:
        search["lookup"] = accepted.make_receiver_lookup()
    plan = accepted.all_cut_single_forward(colors, search["lookup"], counters, start)
    if plan:
        return plan
    plan = accepted.joint.find_four_return_plan(colors, tuple(8 - abs(gap) for gap in gaps), counters, start)
    if plan:
        return dict(gate="k4_two_return", **plan)
    if search["broad"] is None:
        search["broad"] = accepted.joint.broad_returns.make_search()
    plan, counts = search["broad"](tuple(map(frozenset, colors)), None, start)
    counters.update(counts)
    if plan:
        return dict(gate="registry_two_return", required_forced_edge=None, **plan)
    return None


def run(start):
    raw = BASE.read_bytes()
    assert sha256(raw).hexdigest() == BASE_SHA256
    data = json.loads(raw)
    rows = data["representatives"]
    assert data["summary"]["status"] == "complete" and len(rows) == EXPECTED
    broad = accepted.joint.broad_returns
    surviving = broad.surviving

    def surviving_optional(edge, outer, side, omitted):
        return None if edge is None else surviving(edge, outer, side, omitted)

    search = dict(lookup=None, broad=None)
    positives = []
    status = "complete"
    failure = None
    with (
        patch.object(accepted, "CPU_LIMIT", CPU_LIMIT),
        patch.object(four_limits, "CPU_LIMIT", CPU_LIMIT),
        patch.object(broad, "CPU_LIMIT", CPU_LIMIT),
        patch.object(broad, "surviving", surviving_optional),
        patch.object(broad, "whole_interface", accepted.balanced_whole_wrapper(broad.whole_interface)),
    ):
        for index, row in enumerate(rows):
            colors = tuple(row["even_holes"]), tuple(row["odd_holes"])
            assert all(len(set(group)) == 8 and all(p.bit_count() % 2 == parity for p in group)
                       for parity, group in enumerate(colors))
            assert all((p ^ q).bit_count() != 1 for p in colors[0] for q in colors[1])
            gaps = tuple(len(accepted.face(colors[0], i, 1)) - len(accepted.face(colors[1], i, 1))
                         for i in accepted.AXES)
            assert min(map(abs, gaps)) == 3 and gaps == tuple(row["bit_one_even_minus_odd"])
            counters = Counter()
            try:
                accepted.check_time(start)
                plan = first_plan(colors, gaps, search, counters, start)
                accepted.check_time(start)
            except TimeoutError:
                status = "cpu_limit"
                failure = dict(index=index, representative=row, counters=dict(counters))
                break
            if plan is None:
                status = "first_unsupported"
                failure = dict(index=index, representative=row, counters=dict(counters))
                break
            assert plan.get("required_forced_edge") is None
            positives.append(dict(index=index, plan=plan))

    visited = len(positives) + int(failure is not None)
    return dict(
        status=status, base_sha256=BASE_SHA256, input_representatives=EXPECTED,
        visited=visited, unvisited=EXPECTED - visited, cpu_limit_seconds=CPU_LIMIT,
        cpu_seconds=process_time() - start, positives=positives, first_failure=failure,
        plan_counts=Counter(row["plan"]["gate"] for row in positives),
        nested_T63_separate_gate=False, original_matchings_enumerated=0,
        solver_calls=0, rank_runs=0, new_geometries=0,
    )


if __name__ == "__main__":
    result = run(process_time())
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "positives"}, indent=2))
