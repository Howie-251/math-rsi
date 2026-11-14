"""Bounded full check of the 560 independent completions of one fixed source."""

from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from time import process_time
from unittest.mock import patch

import R7_E16_CENTRAL_FAR_TRIPLES_CLOSURE as far
from R7_E16_CENTRAL_SOURCE_COLUMN_COVERAGE import BITS, EVENS, ODDS, gate
from R7_E16_ODD_22_COMPLETE_COVERAGE import get_plan
from R7_E16_TWO_HOLE_HIGH_FACE_JOINT_COVERAGE import controlled_count
import R7_E16_TWO_HOLE_HIGH_FACE_COVERAGE as joint


HERE = Path(__file__).resolve().parent
CPU_LIMIT = 20
S, T, Y = (0, 3, 5), (14, 22, 26, 28, 31), (1, 32, 35, 37, 41)
EXPECTED_POOL = (6, 10, 12, 15, 18, 20, 23, 24, 27, 29, 30, 46, 54, 58, 60, 63)
INPUTS = (
    "R7_E16_CENTRAL_FIRST_RESIDUAL_FIXED_CHECK_REVIEW.md",
    "R7_E16_CENTRAL_SOURCE_COLUMN_COVERAGE_REVIEW.md",
    "R7_E16_CENTRAL_FAR_TRIPLES_CLOSURE_REVIEW.md",
    "R7_TWO_MAJORITY_ROOTS_AVOID_TWO_REVIEW.md",
    "R7_E16_ODD_22_COMPLETE_COVERAGE_REVIEW.md",
    "R7_E16_DISTANCE2_TWO_RETURN_PLAN_REVIEW.md",
    "R7_E16_TWO_HOLE_FACE_FULL_CLOSURE_REVIEW.md",
)
face = joint.face


def source_gate(colors, receive_side):
    b_minor = face(colors[receive_side], 6, receive_side)
    b_major = face(colors[1 - receive_side], 6, receive_side)
    source = face(colors[receive_side], 6, 1 - receive_side)
    candidates = tuple(sorted(v ^ 64 for v in source))
    for inner, bit in enumerate(BITS):
        for side in (0, 1):
            small, large, inside = (face(g, inner, side) for g in (b_minor, b_major, candidates))
            outside = face(candidates, inner, 1 - side)
            difference = len(large) - len(small)
            root = None
            if difference == 1 and inside and outside:
                mode, marks = "net1_split", (inside[0], outside[0])
            elif difference == 1 and len(small) in (1, 2) and len(inside) == 5:
                mode, marks, root = "net1_same_side_root", inside[:2], small[0]
            elif difference == 2 and len(small) <= 1 and len(inside) >= 2:
                mode, marks = "net2_balanced_two_marks", inside[:2]
            elif difference == 2 and len(small) <= 1 and len(inside) == 1:
                mode, marks = "net2_separated_root", (inside[0], outside[0])
                root = next(v for v in face(b_minor, inner, 1 - side) if (v ^ bit) != inside[0])
            elif difference in (3, 4) and len(small) <= 1 and len(inside) >= 2:
                mode, marks = f"net{difference}_majority_roots", inside[:2]
            else:
                continue
            marked_major = tuple(sorted((*b_major, *marks)))
            original_counts = [(len(face(b_minor, inner, v)), len(face(b_major, inner, v))) for v in (0, 1)]
            actual_counts = [(len(face(b_minor, inner, v)), len(face(marked_major, inner, v))) for v in (0, 1)]
            assert not set(marks) & set(colors[0] + colors[1])
            assert root is None or root ^ bit not in marks
            return dict(gate="central_source_" + mode, outer=6, B_side=receive_side,
                        inner=inner, side=side, donor_minority_count=3,
                        X=tuple(sorted(v ^ 64 for v in marks)), Y=tuple(sorted(marks)),
                        root=root, mirror=None if root is None else root ^ bit,
                        original_counts=original_counts, modified_counts=actual_counts)
    return None


def symbolic_plan(u, colors):
    zero = face(u, 1, 0)
    if len(zero) != 1 or zero[0] & 16:
        return None
    one = face(u, 1, 1)
    for a, c in (one, one[::-1]):
        if a & 16 or c & 32:
            continue
        plan = get_plan(colors, 1, 0, (0, 5), (14, 64 ^ a), Counter())
        assert plan is not None
        return dict(gate="symbolic_double_whole", a=a, b=zero[0], c=c,
                    symbolic_inner_axes=(4, 5), **plan)
    return None


def classify(u, colors, start, broad):
    columns = tuple(tuple(len(face(g, i, 1)) for g in colors) for i in joint.AXES)
    for i, (e, o) in enumerate(columns[:6]):
        hit = gate(e, o)
        if hit:
            return dict(gate="column_" + hit, outer=i, bit_one=(e, o), bit_zero=(8 - e, 8 - o)), None
    plan = joint.counts_orbits(colors)
    if plan:
        return plan, None
    distances = tuple(sorted((a ^ b).bit_count() for a, b in combinations(u, 2)))
    if distances in ((2, 4, 6), (4, 4, 4)):
        return dict(gate="far_triple", outer=6, B_side=1, minority_distances=distances), None
    plan = source_gate(colors, 0) or source_gate(colors, 1) or symbolic_plan(u, colors)
    if plan:
        return plan, None
    plan = far.original_double_bridge(colors, start) or controlled_count(colors)
    if plan:
        return plan, None
    forced, exclusion = joint.forced_original_edges(colors)
    if exclusion:
        return None, exclusion
    loads = tuple(8 - abs(e - o) for e, o in columns)
    four = joint.find_four_return_plan(colors, loads, Counter(), start)
    if four:
        return dict(gate="k4_two_return", **four), None
    if min(loads) <= 4:
        if broad[0] is None:
            broad[0] = joint.broad_returns.make_search()
        sets = tuple(map(frozenset, colors))
        for edge in (None, *forced):
            result, _ = broad[0](sets, edge, start)
            if result:
                return dict(gate="registry_two_return", forced_edge=edge, **result), None
    return None, None


def run(start):
    assert set(S) <= EVENS and set(T) <= ODDS and set(Y) <= ODDS and not set(T) & set(Y)
    assert all((s ^ t).bit_count() != 1 for s in S for t in T)
    pool = tuple(sorted(EVENS - set(S) - {y ^ bit for y in Y for bit in BITS}))
    assert pool == EXPECTED_POOL
    completion_keys = list(combinations(pool, 3))
    assert len(completion_keys) == 560
    counts, positive, impossible, unknown = Counter(), [], [], []
    broad = [None]
    original_surviving = joint.broad_returns.surviving

    def surviving_optional(edge, outer, side, omitted):
        return None if edge is None else original_surviving(edge, outer, side, omitted)

    with (
        patch.object(joint.broad_returns, "surviving", surviving_optional),
        patch.object(joint.broad_returns, "CPU_LIMIT", CPU_LIMIT),
        patch.object(far, "CPU_LIMIT", CPU_LIMIT),
    ):
        for u in completion_keys:
            colors = (tuple(sorted((*S, *(64 ^ y for y in Y)))),
                      tuple(sorted((*T, *(64 ^ v for v in u)))))
            try:
                if process_time() - start >= CPU_LIMIT:
                    raise TimeoutError
                assert all(len(set(group)) == 8 and all(v.bit_count() % 2 == i for v in group)
                           for i, group in enumerate(colors))
                assert all((e ^ o).bit_count() != 1 for e in colors[0] for o in colors[1])
                plan, exclusion = classify(u, colors, start, broad)
                if process_time() - start >= CPU_LIMIT:
                    raise TimeoutError
            except TimeoutError:
                break
            if plan:
                positive.append(dict(U=u, plan=plan))
                counts[plan["gate"]] += 1
            elif exclusion:
                impossible.append(dict(U=u, exclusion=exclusion))
            else:
                unknown.append(u)
    completed = len(positive) + len(impossible) + len(unknown)
    unvisited = completion_keys[completed:]
    status = "cpu_limit" if unvisited else "complete"
    return dict(status=status, direct_caller="/root", worker="/root/source_columns_resume",
                S=S, T=T, Y=Y, pool=pool, total=len(completion_keys), visited=completed,
                counts_by_first_gate=counts, positive=positive, impossible=impossible,
                unknown=unknown, unvisited=unvisited, geometry_limit=560,
                opposite_minority_completions_enumerated=completed, other_source_geometries=0,
                original_matching_enumerations=0, solver_calls=0, rank_runs=0,
                input_sha256={name: sha256((HERE / name).read_bytes()).hexdigest() for name in INPUTS},
                cpu_limit_seconds=CPU_LIMIT, cpu_seconds=process_time() - start)


if __name__ == "__main__":
    start = process_time()
    result = run(start)
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: len(v) if isinstance(v, list) else v for k, v in result.items()
                      if k != "input_sha256"}, indent=2))
