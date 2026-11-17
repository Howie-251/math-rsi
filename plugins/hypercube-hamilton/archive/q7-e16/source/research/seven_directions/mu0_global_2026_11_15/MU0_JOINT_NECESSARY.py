"""Build the joint necessary hole model for E16 minimum imbalance zero."""

import json
import sys
from collections import Counter
from hashlib import file_digest
from pathlib import Path

from google.protobuf import text_format
from ortools.sat import cp_model_pb2
from ortools.sat.python import cp_model
import ortools

HERE = Path(__file__).resolve().parent
MU1 = HERE.parent / "mu1_global_2026_11_15"
sys.path.insert(0, str(MU1))

from EDGE_PROBE import (
    ALPHA, A_ALPHA, A_BETA, B_ALPHA, B_BETA, BETA, EDGES, OUTER, VERTICES,
    admissible_global_counts, bit_is_one,
)
from EDGE_MENU_PROBE import add_menu
from EDGE_LOW_GAP_PROBE import add_old_coverage
from EDGE_HIGH_GAP_PROBE import AXES, INNER_AXES, add_high_gaps
from GLOBAL_PROBE import indicator_equal


def build_base():
    """Use physical alpha=odd and a single small-face size variable."""
    assert OUTER == 6
    assert AXES == tuple(range(7)) and INNER_AXES == tuple(range(6))
    model = cp_model.CpModel()
    holes = [model.new_bool_var(f"hole_{v}") for v in VERTICES]
    a = model.new_int_var(0, 2, "small_face_holes_per_color")
    r = model.new_int_var(0, 8, "large_face_holes_per_color")
    model.add_allowed_assignments([a, r], [(0, 8), (1, 7), (2, 6)])
    for side, count in ((A_ALPHA, a), (A_BETA, a), (B_ALPHA, r), (B_BETA, r)):
        model.add(sum(holes[v] for v in side) == count)

    for u, v in EDGES:
        model.add(holes[u] + holes[v] <= 1)
    for v in VERTICES:
        model.add_bool_or([holes[v], *[~holes[v ^ (1 << j)] for j in AXES]])

    # Only inner axes see the nonzero imbalance menu. The outer counts are
    # bound through B and therefore have the required physical equality.
    negative_inner_rows = [
        (x, y) for x in range(9) for y in range(x + 2, 9)
        if admissible_global_counts(x, y)
    ]
    for j in AXES:
        x = model.new_int_var(0, 8, f"global_alpha_{j}")
        y = model.new_int_var(0, 8, f"global_beta_{j}")
        model.add(x == sum(holes[v] for v in ALPHA if bit_is_one(v, j)))
        model.add(y == sum(holes[v] for v in BETA if bit_is_one(v, j)))
        if j == OUTER:
            continue
        model.add_allowed_assignments([x, y], negative_inner_rows)

        p = model.new_int_var(0, 8, f"large_alpha_{j}")
        q = model.new_int_var(0, 8, f"large_beta_{j}")
        model.add(p == sum(holes[v] for v in B_ALPHA if bit_is_one(v, j)))
        model.add(q == sum(holes[v] for v in B_BETA if bit_is_one(v, j)))
        model.add(p - q <= -2)
        delta_two = indicator_equal(model, p - q, -2, f"large_delta_two_{j}")
        model.add(p >= 2).only_enforce_if(delta_two)
        model.add(p <= r - 4).only_enforce_if(delta_two)

    return model, holes, dict(
        small_large_count_rows=[[0, 8], [1, 7], [2, 6]],
        outer_balanced_axis=OUTER, inner_negative_count_rows=negative_inner_rows,
        nonisolated_vertex_clauses=len(VERTICES), independent_edge_constraints=len(EDGES),
        conditional_double_bridge_axes=len(INNER_AXES), anchored_hole=False,
        inner_global_alpha_minus_beta_upper_bound=-2,
    )


def build():
    model, holes, base = build_base()
    stats = dict(base=base, three_bridge_and_split=add_menu(model, holes),
                 low_difference=add_old_coverage(model, holes),
                 high_difference=add_high_gaps(model, holes))
    if error := model.validate():
        raise ValueError(error)
    return model, holes, stats


def source_proto():
    model, _, stats = build()
    proto = text_format.Parse(str(model.proto), cp_model_pb2.CpModelProto())
    assert len(proto.variables) == len(model.proto.variables)
    assert len(proto.constraints) == len(model.proto.constraints)
    assert model.model_stats().startswith("satisfaction model")
    return proto, stats


def digest(path):
    with path.open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


def main():
    proto, stats = source_proto()
    pb = HERE / "MU0_JOINT_NECESSARY.pb"
    report = HERE / "MU0_JOINT_NECESSARY.json"
    if pb.exists() or report.exists():
        raise FileExistsError("Static source artifacts already exist")
    pb.write_bytes(proto.SerializeToString(deterministic=True))
    paths = {
        "source": Path(__file__),
        "pb": pb,
        "domain_contract": HERE / "MU0_FULL_DOMAIN_CONTRACT.md",
        "necessity_note": HERE / "MU0_JOINT_NECESSARY.md",
        "bridge_theorem": HERE / "Q6_BALANCED_DELTA2_TRANSFER.md",
        "bridge_review": HERE / "Q6_BALANCED_DELTA2_TRANSFER_REVIEW.json",
        "first_menus": MU1 / "EDGE_MENU_PROBE.py",
        "low_difference_menus": MU1 / "EDGE_LOW_GAP_PROBE.py",
        "high_difference_menus": MU1 / "EDGE_HIGH_GAP_PROBE.py",
        "first_menu_review": MU1 / "EDGE_MODEL_REVIEW.json",
        "high_menu_review": MU1 / "EDGE_HIGH_GAP_MODEL_REVIEW.json",
    }
    result = dict(status="STATIC_BUILD_ONLY", solver_calls=0, matching_enumerations=0,
                  geometry_enumerations=0, variable_count=len(proto.variables),
                  constraint_count=len(proto.constraints),
                  constraint_types=Counter(row.WhichOneof("constraint") for row in proto.constraints),
                  model_parameters=stats, ortools=ortools.__version__,
                  sha256={key: digest(path) for key, path in paths.items()})
    report.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: result[key] for key in (
        "status", "solver_calls", "variable_count", "constraint_count", "constraint_types", "sha256"
    )}), flush=True)


if __name__ == "__main__":
    main()
