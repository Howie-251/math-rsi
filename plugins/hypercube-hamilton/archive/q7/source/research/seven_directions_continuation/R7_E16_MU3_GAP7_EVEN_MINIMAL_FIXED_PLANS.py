"""One joint all-axis plan check on the frozen even gap-seven basis."""

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from time import process_time
from unittest.mock import patch

import R7_E16_MU3_GAP8_FIXED_PLANS as previous
from R7_E16_MU3_GAP8_ODD5_1_3_THREE_BRIDGE_CHECK import (
    RESEARCH, accepted_cores, core_transport, marked_signature, supplier, t26_registry,
)


AXES = tuple(range(7))
CPU_LIMIT = 180
EXPECTED = 23032
BASE = Path(__file__).with_name("R7_E16_MU3_GAP7_EVEN_MINIMAL_BASE.json")
BASE_SHA256 = "895c81781da07915e103e2d7dcf2e35898c836503b0ecfb7de59d8515734b235"
accepted = previous.accepted
face = previous.face


def directed_cuts(colors):
    for outer in AXES:
        for side in (0, 1):
            b = tuple(face(points, outer, side) for points in colors)
            alpha = int(len(b[1]) > len(b[0]))
            donor = tuple(face(colors[color], outer, 1 - side) for color in (alpha, 1 - alpha))
            receiver = b[alpha], b[1 - alpha]
            yield outer, side, alpha, donor, receiver


def make_t15_lookup():
    accepted_targets = accepted_cores()
    profile = json.loads((RESEARCH / "Q6_T15_ACTUAL_PROFILE.json").read_bytes())
    targets = {row["index"]: row for row in profile["orbits"]}

    def lookup(retained, marks):
        index = accepted_targets.get(marked_signature(retained, marks))
        if index is None:
            return None
        groups = retained, marks
        return dict(kind="T15_exact_core", index=index, normalized_groups=groups,
                    coordinate_transport=core_transport(groups, targets[index]))

    return lookup


def k3_whole(colors, lookup_t15, t26, counters, start):
    holes = set(colors[0] + colors[1])
    for outer, b_side, alpha, donor, receiver in directed_cuts(colors):
        a_minor, a_major = map(frozenset, donor)
        b_major, b_minor = map(frozenset, receiver)
        if len(b_major) - len(b_minor) != 3:
            continue
        assert len(a_major) - len(a_minor) == 3
        counters["k3_directed_cuts"] += 1
        bit = 1 << outer
        for x in sorted(a_major):
            y = x ^ bit
            for u in combinations(sorted(b_major), 2):
                accepted.check_time(start)
                counters["k3_source_choices"] += 1
                b_new = (b_major - set(u)) | {y}
                for inner in AXES:
                    if inner == outer:
                        continue
                    marked_side = (y >> inner) & 1
                    deltas = tuple(len(face(b_new, inner, side)) - len(face(b_minor, inner, side))
                                   for side in (0, 1))
                    if deltas[marked_side] == 2 and deltas[1 - marked_side] == 0:
                        break
                else:
                    continue
                counters["k3_whole_receiver_choices"] += 1
                v = frozenset(p ^ bit for p in u)
                a_kept = a_major - {x}
                assert not ({y} | v) & holes
                tool = supplier(outer, a_minor, a_kept, v, lookup_t15, t26)
                if tool:
                    return dict(gate="k3_whole_receiver", outer=outer, A_side=1 - b_side,
                                alpha_parity=alpha, X=[x], U=u, Y=[y], V=sorted(v),
                                A_minor=sorted(a_minor), A_retained=sorted(a_kept),
                                B_minor=sorted(b_minor), B_new_major=sorted(b_new),
                                B_inner=inner, B_marked_side=marked_side, B_deltas=deltas, donor=tool)
    return None


def run(start):
    raw = BASE.read_bytes()
    assert sha256(raw).hexdigest() == BASE_SHA256
    rows = json.loads(raw)["records"]
    assert len(rows) == EXPECTED
    broad = accepted.joint.broad_returns
    old_surviving = broad.surviving

    def surviving_optional(edge, outer, side, omitted):
        return None if edge is None else old_surviving(edge, outer, side, omitted)

    lookup_t15 = make_t15_lookup()
    t26 = t26_registry()
    search = dict(lookup=None, broad=None)
    positives = []
    failure = None
    status = "complete"
    with (
        patch.object(previous, "directed_cuts", directed_cuts),
        patch.object(accepted, "CPU_LIMIT", CPU_LIMIT),
        patch.object(previous.four_limits, "CPU_LIMIT", CPU_LIMIT),
        patch.object(broad, "CPU_LIMIT", CPU_LIMIT),
        patch.object(broad, "surviving", surviving_optional),
        patch.object(broad, "whole_interface", accepted.balanced_whole_wrapper(broad.whole_interface)),
    ):
        for index, row in enumerate(rows):
            colors = previous.physical_colors(row)
            gaps = tuple(len(face(colors[0], i, 1)) - len(face(colors[1], i, 1)) for i in AXES)
            assert len(colors[0]) == len(colors[1]) == 8
            assert min(map(abs, gaps)) == 3 and abs(gaps[6]) == 7
            assert all((p ^ q).bit_count() != 1 for p in colors[0] for q in colors[1])
            assert tuple(8 - abs(gap) for gap in gaps) == tuple(row["column_loads"])
            counters = Counter()
            try:
                accepted.check_time(start)
                high = previous.high_m_witnesses(colors)
                plan = dict(gate="accepted_high_m", witnesses=high) if high else None
                plan = (plan or accepted.joint.counts_orbits(colors) or previous.four_mono(colors)
                        or accepted.controlled_count(colors)
                        or k3_whole(colors, lookup_t15, t26, counters, start)
                        or previous.first_plan(colors, gaps, search, counters, start))
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
                          for outer, b_side, alpha, donor, receiver in directed_cuts(colors)],
                    counters=dict(counters),
                )
                break
            assert plan.get("required_forced_edge") is None
            positives.append(dict(index=index, plan=plan))
    visited = len(positives) + int(failure is not None)
    return dict(status=status, base_sha256=BASE_SHA256, input_representatives=EXPECTED, visited=visited,
                unvisited=EXPECTED-visited, cpu_seconds=process_time()-start, cpu_limit_seconds=CPU_LIMIT,
                positives=positives, first_failure=failure, plan_counts=Counter(r["plan"]["gate"] for r in positives),
                k3_donor_counts=Counter(r["plan"]["donor"]["kind"] for r in positives
                                        if r["plan"]["gate"] == "k3_whole_receiver"),
                original_matchings_enumerated=0, solver_calls=0, rank_runs=0, new_geometries=0)


if __name__ == "__main__":
    result = run(process_time())
    with Path(__file__).with_suffix(".json").open("x", encoding="utf-8", newline="\n") as file:
        json.dump(result, file, separators=(",", ":"))
        file.write("\n")
    print(json.dumps({key: value for key, value in result.items() if key != "positives"}, indent=2))
