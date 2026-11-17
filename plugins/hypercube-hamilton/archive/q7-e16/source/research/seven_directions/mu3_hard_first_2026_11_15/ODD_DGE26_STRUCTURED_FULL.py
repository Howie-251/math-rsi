"""One structured query on the full normalized odd D>=26 union."""
from hashlib import sha256
import json
import os
from pathlib import Path
from time import monotonic

from google.protobuf import text_format
from ortools.sat import cp_model_pb2
from ortools.sat.python import cp_model

from FINAL_JOINT_PROBE import scalar_rows
from ODD_DGE26_B180 import one_legacy_plan
from ODD_DGE26_REDUCED import add_structure, direct_readback
from ODD_FULL_JOINT_PROBE import build, verify_candidate
from ODD_WHOLE_PAIR_PROBE import add_whole_pair_exclusions, every_whole_pair, scalar_pair
from PROBE import in_side, oriented_cut

HERE = Path(__file__).resolve().parent
SECONDS = 120
WORKERS = 8
SEED = 20261115


def check_previous_d26():
    filename = "ODD_DGE26_REDUCED.json"
    result = json.loads((HERE / filename).read_text(encoding="utf-8"))
    w = result["candidate"]
    old = w["legacy_single_input"]["plan"]
    j, bs = old["outer"], old["B_side"]
    S = (old["receiver"]["inner"], old["receiver"]["mark_side"])
    T = (old["supplier"]["inner"], old["supplier"]["mark_side"])
    colors = w["even_holes"], w["odd_holes"]
    groups = oriented_cut(colors, j, bs)
    aa, ab, ba, bb = groups
    X, U = set(old["X"]), set(old["U"])
    donor_pool = in_side(ab, *S)
    return_pool = in_side(ba, *T)
    assert X <= set(donor_pool) and U <= set(return_pool)
    a, b = (len(in_side(group, *T)) for group in (aa, ab))
    c, d = (len(in_side(group, *S)) for group in (ba, bb))
    epsilon = len(in_side(X, *T))
    t = len(in_side(U, *S))
    cp = len(in_side(donor_pool, *T))
    cq = len(in_side(return_pool, *S))
    assert (j, bs, S, T, a, b, c, d, epsilon, t, cp, cq) == (
        2, 1, (0, 1), (5, 0), 0, 5, 5, 1, 2, 1, 2, 1)
    assert scalar_pair(groups, S, T)
    return dict(source=filename, r=len(aa), s=len(bb), outer=j, receiver_side=bs, S=S, T=T,
                a=a,b=b,c=c,d=d, epsilon=epsilon,t=t, X=sorted(X),U=sorted(U),
                X_capacities=[cp,len(donor_pool)-cp], U_capacities=[cq,len(return_pool)-cq],
                donor_ell=b-epsilon+2-a, receiver_ell=c-t+2-d)


def store_model(model, path):
    # The native exporter on Windows may reject a Unicode absolute filename.
    # The already-scoped current directory keeps the native filename ASCII.
    os.chdir(HERE)
    if not model.export_to_file(path.name):
        native = text_format.Parse(str(model.proto), cp_model_pb2.CpModelProto())
        path.write_bytes(native.SerializeToString(deterministic=True))


def main():
    started = monotonic()
    previous = check_previous_d26()
    rows = scalar_rows()
    model, holes, counts = build(rows)
    counts["whole_pairs"] = add_whole_pair_exclusions(model, holes)
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
    store_model(model,pb)
    params.write_text(str(solver.parameters), encoding="utf-8")
    prepared = monotonic()
    print(model.model_stats().splitlines()[0],
          f"validated and exported in {prepared-started:.3f}s", flush=True)
    status = solver.solve(model)
    data = dict(support_parity=1, minimum_D=26, seconds_limit=SECONDS, workers=WORKERS,
                seed=SEED, status=solver.status_name(status),
                build_seconds=prepared-started, solver_wall_seconds=solver.wall_time,
                model_stats=model.model_stats(), response_stats=solver.response_stats(),
                plan_counts=counts, model_sha256=sha256(pb.read_bytes()).hexdigest(),
                params_sha256=sha256(params.read_bytes()).hexdigest(), prior_D26_plan=previous)
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        w = direct_readback(verify_candidate(solver, holes, rows))
        checks = every_whole_pair((w["even_holes"], w["odd_holes"]), w["delta_even_minus_odd"])
        assert not any(row["first_plan"] for row in checks)
        w["whole_pair_direct_checks"] = checks
        data["candidate"] = w
    out = prefix.with_suffix(".json")
    out.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
    print(data["status"], solver.wall_time, flush=True)
    if "candidate" in data:
        w = data["candidate"]
        print(w["D"], w["even_holes"], w["odd_holes"], "matching found",
              w["matching"] is not None, flush=True)
        w["legacy_single_input"] = one_legacy_plan(w)
        out.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
        print(w["legacy_single_input"]["status"], flush=True)


if __name__ == "__main__":
    main()

