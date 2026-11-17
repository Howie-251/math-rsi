"""Smaller fixed-union query for normalized odd support with D at least 26."""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
from time import monotonic

from google.protobuf import text_format
from ortools.sat import cp_model_pb2
from ortools.sat.python import cp_model

from FINAL_JOINT_PROBE import add_scalar_reduction, check_candidate_scalars, scalar_rows
from FREE_A6_JOINT_PROBE import add_forward_exclusions, verify
from FREE_A6_SUPPLY import verify_supply_table
from GLOBAL_PROBE import indicator_equal, make_model
from ODD_DGE26_B180 import one_legacy_plan
from PROBE import AXES, MASK, donor_gates, in_side, oriented_cut
from SPLIT_SMALL_GLOBAL_PROBE import add_split_exclusions, verify_candidate_splits

HERE = Path(__file__).resolve().parent
PARITY = 1
SECONDS = 120
WORKERS = 8
SEED = 20261115


def add_structure(model, holes):
    groups = [holes[PARITY], {v ^ MASK: flag for v, flag in holes[1-PARITY].items()}]
    for group in groups:
        model.add(group[MASK] == 0)
    units = sum(value for group in groups for v, value in group.items() if v.bit_count() == 1)
    heavy = sum(value for group in groups for v, value in group.items() if v.bit_count() == 5)
    model.add(heavy <= 2)
    # With 16 odd supports of weight 1, 3, or 5, D = 48 - 2*units + 2*heavy.
    model.add_linear_constraint(units-heavy, 7, 11)

    existing = {v.name: model.get_int_var_from_proto_index(i)
                for i, v in enumerate(model.proto.variables)}
    loads = [(existing[f"count_{(PARITY, ((j, 1),))}"],
              existing[f"count_{(1-PARITY, ((j, 0),))}"]) for j in AXES]
    for j, ((p, q), (p1, q1)) in enumerate(zip(loads, loads[1:])):
        tied = indicator_equal(model, p+q-p1-q1, 0, f"profile_tie_{j}")
        model.add(p>=p1).only_enforce_if(tied)


def direct_central_cut(aa, ab, ba, bb, j, inner):
    counts = Counter()
    for x, U in product(ab, combinations(ba, 2)):
        y = x ^ (1 << j)
        V = tuple(u ^ (1 << j) for u in U)
        new_ab = (set(ab)-{x}) | set(V)
        new_ba = (set(ba)-set(U)) | {y}
        can_receive = len(aa) == 3 or any(
            len(in_side(new_ba, i, (y>>i)&1))-len(in_side(bb, i, (y>>i)&1)) == 2
            for i in inner
        )
        counts["source_return_combinations"] += 1
        if not can_receive:
            continue
        for i in inner:
            if ((V[0]^V[1])>>i)&1:
                continue
            bit = (V[0]>>i)&1
            a = len(in_side(aa, i, bit))
            ell = len(in_side(new_ab, i, bit))-a
            counts["same_side_halves_checked"] += 1
            assert not any(donor_gates(len(aa), a, ell))
    return counts


def direct_split_cut(aa, ab, ba, bb, j, inner):
    k = len(ba)-len(bb)
    counts = Counter()
    for x, U in product(ab, combinations(ba, k-1)):
        V = tuple(u ^ (1 << j) for u in U)
        new_ab = (set(ab)-{x}) | set(V)
        counts["source_return_combinations"] += 1
        for i in inner:
            q = len(in_side(V, i, 0))
            qe = len(V)-q
            if q not in (1, 2) or qe not in (1, 2):
                continue
            a = len(in_side(aa, i, 0))
            ae = len(aa)-a
            if q == 2 and a > 1 or qe == 2 and ae > 1:
                continue
            b = len(in_side(new_ab, i, 0))
            be = len(new_ab)-b
            counts["marked_halves_checked"] += 1
            assert (b-a, be-ae) != (2*q, 2*qe)
    return counts


def direct_readback(w):
    p, q = w["P"], w["Q"]
    assert MASK not in p and MASK not in q
    assert sum(v.bit_count() == 5 for v in p+q) <= 2
    w["D"] = sum(v.bit_count() for v in p+q)
    assert 26 <= w["D"] <= 34
    sort_key = [(w["lambda_by_axis"][j], sum((v>>j)&1 for v in p)) for j in AXES]
    assert sort_key == sorted(sort_key, reverse=True)
    colors = w["even_holes"], w["odd_holes"]
    checks = []
    for j, side in product(AXES, (0, 1)):
        aa, ab, ba, bb = oriented_cut(colors, j, side)
        k = len(ba)-len(bb)
        inner = [i for i in AXES if i != j]
        row = dict(outer=j, B_side=side, gap=k)
        if k == 3:
            row["direct_central"] = direct_central_cut(aa, ab, ba, bb, j, inner)
        if k in (3, 4, 5) and len(bb) <= 2:
            row["direct_split"] = direct_split_cut(aa, ab, ba, bb, j, inner)
        checks.append(row)
    w["physical_direct_readback"] = checks
    if w["matching"] is not None:
        ends = [v for edge in w["matching"] for v in edge]
        assert len(ends) == len(set(ends)) == 112
        assert set(range(128))-set(ends) == set(w["even_holes"]) | set(w["odd_holes"])
        assert all((u^v).bit_count() == 1 for u, v in w["matching"])
    return w


def main():
    started = monotonic()
    verify_supply_table()
    rows = scalar_rows()
    model, holes, _ = make_model(PARITY)
    add_forward_exclusions(model, holes, PARITY)
    add_split_exclusions(model, PARITY)
    add_scalar_reduction(model, PARITY, rows)
    add_structure(model, holes)
    error = model.validate()
    if error:
        raise ValueError(error)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = SECONDS
    solver.parameters.num_workers = WORKERS
    solver.parameters.random_seed = SEED
    prefix = Path(__file__)
    pb = prefix.with_suffix(".pb")
    params = prefix.with_suffix(".params.textproto")
    exported = text_format.Parse(str(model.proto), cp_model_pb2.CpModelProto())
    pb.write_bytes(exported.SerializeToString(deterministic=True))
    params.write_text(str(solver.parameters), encoding="utf-8")
    prepared = monotonic()
    print(f"model and parameters saved in {prepared-started:.3f}s", flush=True)
    print(model.model_stats(), flush=True)
    status = solver.solve(model)
    data = dict(support_parity=PARITY, seconds_limit=SECONDS, workers=WORKERS, seed=SEED,
                status=solver.status_name(status), build_seconds=prepared-started,
                solver_wall_seconds=solver.wall_time, model_stats=model.model_stats(),
                response_stats=solver.response_stats(), model_sha256=sha256(pb.read_bytes()).hexdigest(),
                params_sha256=sha256(params.read_bytes()).hexdigest())
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        colors = [sorted(v for v, selected in holes[c].items() if solver.value(selected))
                  for c in (0, 1)]
        w = verify(colors, PARITY)
        w["direct_split_cuts_checked"] = verify_candidate_splits(w)
        check_candidate_scalars(w, rows)
        data["candidate"] = direct_readback(w)
    out = prefix.with_suffix(".json")
    out.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
    print(data["status"], solver.wall_time, flush=True)
    if "candidate" in data:
        w = data["candidate"]
        print(w["D"], w["even_holes"], w["odd_holes"],
              "matching found", w["matching"] is not None, flush=True)
        w["legacy_single_input"] = one_legacy_plan(w)
        out.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
        print(w["legacy_single_input"]["status"], flush=True)


if __name__ == "__main__":
    main()

