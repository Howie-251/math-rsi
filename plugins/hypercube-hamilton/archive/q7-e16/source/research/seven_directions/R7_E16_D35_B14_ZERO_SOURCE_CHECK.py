"""Check the 36 explicit degree families for the D35 b14 zero-source branch."""

from collections import Counter
from hashlib import sha256
from itertools import combinations, permutations
import json
from pathlib import Path
from time import process_time
from unittest.mock import patch

import R7_E16_CENTRAL_FAR_TRIPLES_CLOSURE as far
import R7_E16_TWO_HOLE_HIGH_FACE_COVERAGE as joint
from R7_E16_CENTRAL_FIRST_SOURCE_FULL_COVERAGE import source_gate
from R7_E16_EVEN_HIGH_GAP_CHECK import make_receiver_lookup, receiver_plan
from R7_E16_TWO_HOLE_HIGH_FACE_JOINT_COVERAGE import controlled_count


HERE = Path(__file__).resolve().parent
CPU_LIMIT = 30
S, T, Y = (0, 3, 46), (13, 21, 25, 28, 31), (32, 35, 38, 42, 50)
AXES = joint.AXES
face = joint.face
TABLE = "R7_CENTRAL_D35_COUNT_DELTA.json"
DEPENDENCIES = (
    TABLE, "R7_E16_D35_FULL_CLOSURE_REVIEW.md",
    "R7_E16_CENTRAL_FAR_TRIPLES_CLOSURE_REVIEW.md",
    "R7_E16_CENTRAL_FIRST_SOURCE_FULL_COVERAGE_REVIEW.md",
    "R7_E16_DISTANCE2_SWITCH_CUT_REVIEW.md",
    "R7_E16_DISTANCE2_TWO_RETURN_PLAN_REVIEW.md",
    "R7_E16_ODD_22_COMPLETE_COVERAGE_REVIEW.md",
    "R7_CONTROLLED_THREE_ROOT_RECEIVER_REVIEW.md",
    "R7_TWO_MAJORITY_ROOTS_AVOID_TWO_REVIEW.md",
    "R7_E14_LOW_GAP_DIRECT_TRANSFERS.md", "R7_E14_NEXT_REVIEW.md",
    "R7_E14_THREE_BRIDGE_ODD_RECEIVER_REVIEW.md",
    "R7_E16_CENTRAL_FAR_TRIPLES_CLOSURE.py",
    "R7_E16_CENTRAL_FIRST_SOURCE_FULL_COVERAGE.py",
    "R7_E16_DISTANCE2_TWO_RETURN_PLAN.py",
    "R7_E16_EVEN_HIGH_GAP_CHECK.py",
    "R7_E16_TWO_HOLE_HIGH_FACE_COVERAGE.py",
    "R7_E16_TWO_HOLE_HIGH_FACE_JOINT_COVERAGE.py",
)


def basis():
    unit = tuple(1 << i for i in range(5))
    four = unit[:4]
    families = (
        [(a | b, a | c, b | c) for a, b, c in combinations(unit, 3)],
        [(unit[4] | b, b | c, c) for b, c in permutations(four, 2)],
        [(a, b, a | b) for a, b in combinations(unit, 2)],
        [(0, a, unit[4] | a) for a in four],
    )
    assert tuple(map(len, families)) == (10, 12, 10, 4)
    rows = []
    for family, objects in enumerate(families, 1):
        for q in sorted(tuple(sorted(objects_q)) for objects_q in objects):
            u = tuple(sorted((29 ^ v) | (32 * (v.bit_count() % 2)) for v in q))
            rows.append(dict(family=family, q_masks=q, U=u))
    assert len({row["U"] for row in rows}) == 36
    return rows


def check_time(start):
    if process_time() - start >= CPU_LIMIT:
        raise TimeoutError


def central_gate(colors):
    # Verified below from all seven original column gaps.
    for side in (0, 1):
        minor = face(colors[side], 6, side)
        major = face(colors[1 - side], 6, side)
        candidates = tuple(sorted(p ^ 64 for p in face(colors[side], 6, 1 - side)))
        distances = sorted((a ^ b).bit_count() for a, b in combinations(minor, 2))
        if distances in ([2, 4, 6], [4, 4, 4]):
            return dict(gate="far_triple", outer=6, receiver_side=side,
                        receiver_minority=minor, distances=distances)
        for inner in range(6):
            for block in (0, 1):
                small, large, inside = (face(group, inner, block)
                                        for group in (minor, major, candidates))
                if len(inside) < 2:
                    continue
                shape = len(small), len(large)
                if shape == (2, 5):
                    name = "D35_full"
                elif shape == (0, 5):
                    name = "controlled_three_majority_roots"
                elif shape[0] <= 1 and shape[1] == shape[0] + 4:
                    name = "two_majority_roots"
                else:
                    continue
                return dict(gate=name, outer=6, receiver_side=side, inner=inner,
                            marked_side=block, receiver_minority=minor, receiver_majority=major,
                            marks=inside[:2], sources=tuple(p ^ 64 for p in inside[:2]))
        old = source_gate(colors, side)
        if old:
            return old
    return None


def all_cut_single_forward(colors, lookup, counters, start):
    for outer in AXES:
        bit = 1 << outer
        for side in (0, 1):
            a = tuple(face(group, outer, side) for group in colors)
            beta = int(len(a[1]) > len(a[0]))
            alpha = 1 - beta
            r, k = len(a[alpha]), len(a[beta]) - len(a[alpha])
            if r > 5 or k < 2:
                continue
            small = frozenset(face(colors[beta], outer, 1 - side))
            large = frozenset(face(colors[alpha], outer, 1 - side))
            for sources in combinations(a[beta], k):
                check_time(start)
                marks = frozenset(p ^ bit for p in sources)
                if k == 3 and (len(small), len(large)) == (1, 4):
                    root, = small
                    for inner in AXES:
                        if inner == outer:
                            continue
                        block = (root >> inner) & 1
                        if (len(face(large, inner, block)) == 2
                                and len(face(marks, inner, block)) == 2
                                and root ^ (1 << inner) not in marks):
                            return dict(gate="universal_delta3", outer=outer, donor_side=side,
                                        alpha_parity=alpha, r=r, k=k, sources=sources,
                                        marks=sorted(marks), receiver_minority=sorted(small),
                                        receiver_majority=sorted(large), inner=inner, root=root,
                                        mirror=root ^ (1 << inner))
                plan = receiver_plan(outer, small, large, marks, lookup, counters, "single_forward")
                if plan:
                    return dict(gate="controlled_cycle_registered_split", outer=outer,
                                donor_side=side, alpha_parity=alpha, r=r, k=k, sources=sources,
                                marks=sorted(marks), receiver_minority=sorted(small),
                                receiver_majority=sorted(large), receiver=plan)
    return None


def balanced_whole_wrapper(old_whole):
    def whole(outer, minority, retained, marks, edge=None, allow_t15_odd=False):
        plan = old_whole(outer, minority, retained, marks, edge, allow_t15_odd)
        if plan or len(marks) != 2:
            return plan
        majority = retained | marks
        for inner in AXES:
            if inner == outer:
                continue
            for side in (0, 1):
                if set(face(marks, inner, side)) != marks:
                    continue
                a, b = (len(face(group, inner, side)) for group in (minority, majority))
                t, n = len(minority) - a, len(majority) - b
                if a in (0, 1) and b == a + 4 and 1 <= t <= 16 and n == t:
                    return dict(kind="Q6_balanced_complement_avoid_two", inner=inner, side=side,
                                face_counts=((a, b), (t, n)))
        return None

    return whole


def classify(colors, gaps, search, counters, start):
    plan = joint.counts_orbits(colors) or far.two_hole_full(colors) or central_gate(colors)
    if plan:
        return plan
    plan = far.original_double_bridge(colors, start) or controlled_count(colors)
    if plan:
        return plan
    if search["lookup"] is None:
        search["lookup"] = make_receiver_lookup()
    plan = all_cut_single_forward(colors, search["lookup"], counters, start)
    if plan:
        return plan
    forced, exclusion = joint.forced_original_edges(colors)
    if exclusion:
        return dict(gate="impossible_geometry", exclusion=exclusion)
    loads = tuple(8 - abs(gap) for gap in gaps)
    plan = joint.find_four_return_plan(colors, loads, counters, start)
    if plan:
        return dict(gate="k4_two_return", **plan)
    if search["broad"] is None:
        search["broad"] = joint.broad_returns.make_search()
    for edge in (None, *forced):
        plan, counts = search["broad"](tuple(map(frozenset, colors)), edge, start)
        counters.update(counts)
        if plan:
            return dict(gate="registry_two_return", required_forced_edge=edge, **plan)
    return None


def run(start):
    rows = basis()
    allowed = {tuple(row) for row in json.loads((HERE / TABLE).read_bytes())["conditional_remainder"]}
    assert len(allowed) == 124
    positive, failure = [], None
    search = dict(lookup=None, broad=None)
    broad = joint.broad_returns
    surviving = broad.surviving

    def surviving_optional(edge, outer, side, omitted):
        return None if edge is None else surviving(edge, outer, side, omitted)

    status = "complete"
    with (
        patch.object(far, "CPU_LIMIT", CPU_LIMIT),
        patch.object(broad, "CPU_LIMIT", CPU_LIMIT),
        patch.object(broad, "surviving", surviving_optional),
        patch.object(broad, "whole_interface", balanced_whole_wrapper(broad.whole_interface)),
    ):
        for row in rows:
            u = row["U"]
            columns = [tuple(len(face(group, axis, 1)) for group in (S, T, Y, u))
                       for axis in range(6)]
            assert all(col in allowed for col in columns)
            colors = (tuple(sorted((*S, *(64 ^ y for y in Y)))),
                      tuple(sorted((*T, *(64 ^ p for p in u)))))
            assert all(len(set(group)) == 8 and all(v.bit_count() % 2 == i for v in group)
                       for i, group in enumerate(colors))
            assert all((a ^ b).bit_count() != 1 for a in colors[0] for b in colors[1])
            gaps = tuple(len(face(colors[0], i, 1)) - len(face(colors[1], i, 1)) for i in AXES)
            assert [i for i, gap in enumerate(gaps) if abs(gap) == 2] == [6]
            current = dict(**row, even_holes=colors[0], odd_holes=colors[1],
                           columns=columns, bit_one_even_minus_odd=gaps)
            counters = Counter()
            try:
                check_time(start)
                plan = classify(colors, gaps, search, counters, start)
                check_time(start)
            except TimeoutError:
                status = "cpu_limit"
                failure = dict(**current, counters=counters)
                break
            if plan is None:
                status = "first_unsupported"
                failure = dict(**current, counters=counters,
                               forced_original_edges=joint.forced_original_edges(colors)[0])
                break
            positive.append(dict(**current, plan=plan))
    visited = len(positive) + (failure is not None)
    return dict(status=status, S=S, T=T, Y=Y, expected_families=(10, 12, 10, 4),
                geometry_limit=36, cpu_limit_seconds=CPU_LIMIT, cpu_seconds=process_time() - start,
                checked_geometries=visited, positive=positive, first_unsupported=failure,
                unvisited=rows[visited:], plan_counts=Counter(row["plan"]["gate"] for row in positive),
                e14_missing_edge_three_bridge_applicable=False,
                e14_missing_edge_three_bridge_reason="Requires fourteen original holes and fixed outer shape.",
                other_Y_or_U_geometries_checked=0, original_matchings_enumerated=0,
                solver_calls=0, rank_runs=0,
                input_sha256={name: sha256((HERE / name).read_bytes()).hexdigest() for name in DEPENDENCIES})


if __name__ == "__main__":
    result = run(process_time())
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: len(v) if k in ("positive", "unvisited") else v for k, v in result.items()
                      if k != "input_sha256"}, indent=2))
