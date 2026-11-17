"""One fixed large-face diagnostic, reusing the audited E16 edge-model bytes."""

import argparse
import json
import sys
from hashlib import sha256
from pathlib import Path
from time import perf_counter

from google.protobuf import text_format
from ortools.sat import cp_model_pb2
from ortools.sat.python import cp_model
import ortools

HERE = Path(__file__).resolve().parent
MU1 = HERE.parent
MU0 = MU1.parent / "mu0_global_2026_11_15"
CERT = MU1 / "certificates"
sys.path.insert(0, str(MU1))

from EDGE_HIGH_GAP_PROBE import INNER_AXES, validate_high_geometry
from EDGE_LOW_GAP_PROBE import validate_sat
from EDGE_PROBE import (
    ALPHA, B_ALPHA, B_BETA, BETA, OUTER, SEED, VERTICES, bit_is_one,
    check_matching, short_maximum_matching,
)
from probe import add_coverage

BASIS = HERE / "STRUCTURE_BASIS_PREFLIGHT.json"
ORIGINAL = CERT / "edge_a1.pb"
ORIGINAL_SHA256 = "992b8fe7617c3cb5cdd69054b60027f8b6045eedade1e45c4d9b335a06a4c6a2"
LIMIT_SECONDS = 60
WORKERS = 8
HALF_MASK = (1 << OUTER) - 1


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def read_basis():
    data = json.loads(BASIS.read_text(encoding="utf-8-sig"))
    assert data["status"] == "COMPLETE" and len(data["representatives"]) == 23
    return data["representatives"]


def physical_B(representative):
    L, V = representative["L"], representative["V"]
    majority = representative["family"] == "E"
    assert len(L) == len(set(L)) == 7 and len(V) == len(set(V)) == 6
    assert all(0 <= label <= HALF_MASK for label in L + V)
    assert all(label.bit_count() % 2 == (0 if majority else 1) for label in L)
    assert all(label.bit_count() % 2 == (1 if majority else 0) for label in V)
    shift = int(not majority)
    to_B = lambda u: (1 << OUTER) | (u ^ shift)
    alpha = set(map(to_B, L))
    beta = {to_B(HALF_MASK ^ v) for v in V}
    assert alpha <= set(B_ALPHA) and beta <= set(B_BETA)
    assert all((u ^ v).bit_count() != 1 for u in alpha for v in beta)
    return alpha, beta, shift


def strip_only_label_choices(proto):
    """Remove the anchor and five signed-difference sorts by exact named form."""
    expected = {
        ("hole_0",): ((1,), (1, 1)),
        **{(f"global_alpha_{i}", f"global_beta_{i}",
            f"global_alpha_{i+1}", f"global_beta_{i+1}"):
           ((1, -1, -1, 1), (-(1 << 63), 0)) for i in range(5)},
    }
    removed = []
    for index, row in enumerate(proto.constraints):
        if row.WhichOneof("constraint") != "linear" or row.enforcement_literal:
            continue
        term_names = tuple(proto.variables[v].name for v in row.linear.vars)
        numeric = (tuple(row.linear.coeffs), tuple(row.linear.domain))
        if expected.get(term_names) == numeric:
            removed.append((index, term_names, numeric))
    assert len(removed) == len(expected) == 6
    assert {names for _, names, _ in removed} == expected.keys()
    for index, _, _ in reversed(removed):
        del proto.constraints[index]
    return removed


def build(indices):
    bases = read_basis()
    assert len(indices) == len(set(indices)) > 0
    assert all(0 <= index < len(bases) for index in indices)
    assert digest(ORIGINAL) == ORIGINAL_SHA256
    bridge_proof = MU0 / "Q6_BALANCED_DELTA2_TRANSFER.md"
    bridge_review = MU0 / "Q6_BALANCED_DELTA2_TRANSFER_REVIEW.json"
    review = json.loads(bridge_review.read_text(encoding="utf-8-sig"))
    assert review["verdict"] == "PASS"
    assert review["audited_input_hashes"][bridge_proof.name] == f"sha256:{digest(bridge_proof)}"

    proto = cp_model_pb2.CpModelProto.FromString(ORIGINAL.read_bytes())
    count_before = len(proto.constraints)
    removed = strip_only_label_choices(proto)
    model = cp_model.CpModel()
    assert model.proto.parse_text_format(text_format.MessageToString(proto))
    assert len(model.proto.constraints) == count_before - len(removed)
    ids = {var.name: i for i, var in enumerate(proto.variables)}
    holes = [model.get_bool_var_from_proto_index(ids[f"hole_{vertex}"]) for vertex in VERTICES]

    rows = []
    bound = []
    for index in indices:
        representative = bases[index]
        alpha, beta, shift = physical_B(representative)
        rows.append(tuple(int(v in alpha or v in beta) for v in range(64, 128)))
        bound.append(dict(index=index, representative=representative, internal_xor=shift,
                          B_alpha_odd=sorted(alpha), B_beta_even=sorted(beta)))
    assert len(rows) == len(set(rows))
    model.add_allowed_assignments(holes[64:], rows)
    new_gate_rows = add_coverage(model, holes, 1)
    if error := model.validate():
        raise ValueError(error)
    return model, holes, dict(
        original_constraints=count_before, removed=removed, preserved=count_before-len(removed),
        declared_B_rows=bound, delta2_forbidden_rows=new_gate_rows,
        hashes={path.name: digest(path) for path in
                [ORIGINAL, BASIS, bridge_proof, bridge_review, Path(__file__)]},
    )


def readback(H, bound):
    assert tuple(sorted(H.intersection(B_ALPHA))) == tuple(bound["B_alpha_odd"])
    assert tuple(sorted(H.intersection(B_BETA))) == tuple(bound["B_beta_even"])
    assert all(any(u ^ (1 << j) not in H for j in range(7)) for u in VERTICES if u not in H)
    # Translate by an even small-face original hole only for existing readback.
    # The diagnostic model itself has no anchor or global axis order.
    small_even = sorted(v for v in H.intersection(BETA) if v < 64)
    assert len(small_even) == 2
    shift = small_even[0]
    normalized = {v ^ shift for v in H}
    validate_sat(1, normalized)
    assert not any(validate_high_geometry(H).values())
    axes = []
    for j in INNER_AXES:
        halves = []
        for side in (False, True):
            a = sum(v in H and bit_is_one(v, j) == side for v in B_ALPHA)
            b = sum(v in H and bit_is_one(v, j) == side for v in B_BETA)
            assert a - b != 3 or min(b, 4 - b) >= 2
            halves.append([a, b])
        axes.append(dict(axis=j, large_half_counts=halves))
    matching = short_maximum_matching(H)
    return dict(H_alpha_odd=sorted(H.intersection(ALPHA)), H_beta_even=sorted(H.intersection(BETA)),
                delta=[sum(bit_is_one(v,j) for v in H.intersection(ALPHA)) -
                       sum(bit_is_one(v,j) for v in H.intersection(BETA)) for j in range(7)],
                internal_large_face_axes=axes, short_matching_size=len(matching),
                realized_by_short_matching=check_matching(H, matching), short_matching=matching)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("index", type=int)
    args = parser.parse_args()
    start = perf_counter()
    destination = HERE / f"fixed_face_{args.index:02}.json"
    if destination.exists():
        raise FileExistsError("This fixed-face attempt already exists")
    model, holes, stats = build((args.index,))
    build_seconds = perf_counter() - start
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = LIMIT_SECONDS
    solver.parameters.num_search_workers = WORKERS
    solver.parameters.random_seed = SEED
    print(f"Fixed B #{args.index}: built in {build_seconds:.3f}s, one 60s CP query", flush=True)
    status = solver.solve(model)
    result = dict(scope="One fixed B representative; diagnostic CP only", calls=1,
                  a=1, index=args.index, status=solver.status_name(status),
                  build_wall_seconds=build_seconds, solver_wall_seconds=solver.wall_time,
                  time_limit=LIMIT_SECONDS, workers=WORKERS, seed=SEED,
                  ortools=ortools.__version__, model_stats=model.model_stats(),
                  solver_stats=solver.response_stats(), input=stats)
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        H = {v for v in VERTICES if solver.value(holes[v])}
        result["witness"] = readback(H, stats["declared_B_rows"][0])
    destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"Fixed B #{args.index}: {result['status']} after {solver.wall_time:.3f}s", flush=True)


if __name__ == "__main__":
    main()
