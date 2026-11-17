"""Run one audited, capped diagnostic on the joint E16 mu-zero hole model."""

import json
from collections import deque
from itertools import product
from pathlib import Path

from google.protobuf import text_format
from ortools.sat import cp_model_pb2
from ortools.sat.python import cp_model

from MU0_JOINT_NECESSARY import (
    ALPHA, A_ALPHA, A_BETA, AXES, B_ALPHA, B_BETA, BETA, EDGES,
    HERE, INNER_AXES, OUTER, VERTICES, bit_is_one, digest,
)
from EDGE_PROBE import SEED, check_matching, short_maximum_matching
from EDGE_MENU_PROBE import pointwise_gates
from EDGE_LOW_GAP_PROBE import central_column_hit, peeled_outer_type
from EDGE_HIGH_GAP_PROBE import validate_high_geometry
from PROBE import controlled_count, oriented_cut

SECONDS = 60.0
WORKERS = 8


def counts(holes, group, axis):
    return sum(vertex in holes and bit_is_one(vertex, axis) for vertex in group)


def inspect_holes(H, selected_a):
    assert len(H.intersection(ALPHA)) == len(H.intersection(BETA)) == 8
    assert not any(u in H and v in H for u, v in EDGES)
    assert all(any((v ^ (1 << j)) not in H for j in AXES) for v in VERTICES if v not in H)
    a = len(H.intersection(A_ALPHA))
    assert a == len(H.intersection(A_BETA)) == selected_a and 0 <= a <= 2
    r = 8 - a
    assert len(H.intersection(B_ALPHA)) == len(H.intersection(B_BETA)) == r
    global_rows = [(counts(H, ALPHA, j), counts(H, BETA, j)) for j in AXES]
    global_delta = [x - y for x, y in global_rows]
    assert global_delta[OUTER] == 0
    assert global_delta[:OUTER] == sorted(global_delta[:OUTER])
    assert all(delta <= -2 for delta in global_delta[:OUTER])
    assert not any(peeled_outer_type(*row) for row in global_rows)
    large_rows = [(counts(H, B_ALPHA, j), counts(H, B_BETA, j)) for j in INNER_AXES]
    for p, q in large_rows:
        assert p - q <= -2 and (p - q != -2 or 2 <= p <= r - 4)
    assert not pointwise_gates(H)
    colors = tuple(tuple(v for v in group if v in H) for group in (BETA, ALPHA))
    for j, side in product(INNER_AXES, (0, 1)):
        aa, ab, ba, bb = oriented_cut(colors, j, side)
        k = len(ba) - len(bb)
        for i in AXES:
            if i == j:
                continue
            if k in (2, 3, 4) and len(aa) <= 5:
                assert not controlled_count(ab, ba, bb, i)
            if (k, len(aa), len(bb)) == (2, 3, 3):
                for half in (0, 1):
                    a_h, b_h, c_h = [sum(bit_is_one(v, i) == half for v in group)
                                        for group in (bb, ba, ab)]
                    assert not central_column_hit(a_h, b_h, c_h)

    # The inherited direct high-gap check supports an outer gap of zero by skipping it.
    assert not any(validate_high_geometry(H).values())
    return dict(a=a, H_odd=sorted(H.intersection(ALPHA)), H_even=sorted(H.intersection(BETA)),
                global_axis_counts=global_rows, global_odd_minus_even=global_delta,
                large_inner_axis_counts=large_rows)


def hall_certificate(holes, matching):
    remaining = set(VERTICES)-holes
    odd_mate = dict(matching)
    even_mate = {v:u for u,v in matching}
    seeds = set(ALPHA).intersection(remaining)-odd_mate.keys()
    seen_odd, seen_even = set(seeds), set()
    queue = deque(seeds)
    while queue:
        u = queue.popleft()
        for axis in AXES:
            v = u ^ (1 << axis)
            if v not in remaining or v == odd_mate.get(u) or v in seen_even:
                continue
            seen_even.add(v)
            assert v in even_mate
            w = even_mate[v]
            if w not in seen_odd:
                seen_odd.add(w)
                queue.append(w)
    neighbors = {u ^ (1 << j) for u in seen_odd for j in AXES} & remaining
    assert neighbors == seen_even and len(neighbors) < len(seen_odd)
    return dict(odd_set=sorted(seen_odd), even_short_neighbors=sorted(neighbors),
                deficit=len(seen_odd)-len(neighbors))


def main():
    receipt = HERE / "MU0_JOINT_NECESSARY.json"
    pb = HERE / "MU0_JOINT_NECESSARY.pb"
    output = HERE / "MU0_JOINT_DIAGNOSTIC.json"
    if output.exists():
        raise FileExistsError("The one joint diagnostic attempt already exists")
    expected = json.loads(receipt.read_text(encoding="utf-8"))
    assert expected["sha256"]["pb"] == digest(pb)
    assert expected["sha256"]["source"] == digest(HERE / "MU0_JOINT_NECESSARY.py")
    data = cp_model_pb2.CpModelProto.FromString(pb.read_bytes())
    model = cp_model.CpModel()
    assert model.proto.parse_text_format(text_format.MessageToString(data))
    if error := model.validate():
        raise ValueError(error)
    ids = {var.name: i for i, var in enumerate(data.variables)}
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = SECONDS
    solver.parameters.num_search_workers = WORKERS
    solver.parameters.random_seed = SEED
    print("One joint mu-zero diagnostic, one 60s CP-SAT call", flush=True)
    status = solver.solve(model)
    result = dict(status=solver.status_name(status), scope="joint a=0,1,2 diagnostic only",
                  diagnostic_solver_calls=1, budget_seconds=SECONDS, workers=WORKERS, seed=SEED,
                  solver_wall_seconds=solver.wall_time, solver_statistics=solver.response_stats(),
                  original_source_sha256=expected["sha256"]["source"], original_pb_sha256=digest(pb),
                  diagnostic_sha256=digest(Path(__file__)),
                  matching_calls=0, matching_enumerations=0)
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        selected_a = solver.value(model.get_int_var_from_proto_index(ids["small_face_holes_per_color"]))
        H = {v for v in VERTICES if solver.value(model.get_bool_var_from_proto_index(ids[f"hole_{v}"]))}
        witness = inspect_holes(H, selected_a)
        matching = short_maximum_matching(H)
        realized = check_matching(H, matching)
        witness.update(maximum_matching_size=len(matching), realized_by_short_matching=realized,
                       short_matching=matching)
        if not realized:
            witness["hall_certificate"] = hall_certificate(H, matching)
        else:
            witness["original_matching_direction_counts"] = [
                sum((u ^ v) == (1 << j) for u, v in matching) for j in AXES
            ]
        witness["axis_table"] = []
        for j, row in enumerate(witness["global_axis_counts"]):
            record = dict(axis=j, global_alpha=row[0], global_beta=row[1], s=row[0] - row[1])
            if j != OUTER:
                p, q = witness["large_inner_axis_counts"][j]
                record.update(B_alpha=p, B_beta=q, B_deficit=q-p)
            if realized:
                record["original_matching_edges"] = witness["original_matching_direction_counts"][j]
            witness["axis_table"].append(record)
        result.update(matching_calls=1, witness=witness)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Result: {result['status']} after {result['solver_wall_seconds']:.3f}s", flush=True)


if __name__ == "__main__":
    main()
