"""Bounded search outside the fixed central and split-supply union for E16 mu=3."""
from itertools import product
import json
from pathlib import Path
from time import monotonic

from ortools.sat.python import cp_model

from FREE_A6_JOINT_PROBE import add_forward_exclusions, verify
from FREE_A6_SUPPLY import forward_supply, verify_supply_table
from GLOBAL_PROBE import make_model
from NEW_SPLIT_CHECK import INPUTS, check_cut, read_saved_input
from PROBE import AXES, load, oriented_cut, test_central
from SPLIT_SMALL_GLOBAL_PROBE import add_split_exclusions, old_gate_checks, verify_candidate_splits

HERE = Path(__file__).resolve().parent
SECONDS = 60
WORKERS = 8
SAVED_INPUTS = INPUTS + ("SPLIT_SMALL_GLOBAL_PROBE.json",)


def scalar_rows():
    data = json.loads((HERE / "SCALAR_NEW_GATES.json").read_text(encoding="utf-8"))
    rows = set(tuple(row) for row in data["residual_rows"])
    assert tuple(data["base_totals"]) == (3, 6, 5, 2) and len(rows) == 106
    return rows


def readback_known():
    results = []
    for filename in SAVED_INPUTS:
        colors, delta = read_saved_input(filename)
        hits = []
        for j, side in product(AXES, (0, 1)):
            if abs(delta[j]) == 3:
                a6 = forward_supply(colors, j, side)
                if a6 is not None:
                    hits.append(dict(axis=j, B_side=side, gate="forward_A6", plan=a6))
                old = test_central(colors, j, side)["joint_witness"]
                if old is not None:
                    hits.append(dict(axis=j, B_side=side, gate="old_central", plan=old))
            split = check_cut(colors, j, side)
            if split is not None:
                hits.append(dict(axis=j, B_side=side, gate="split_supply", plan=split))
        assert hits, filename
        results.append(dict(input=filename, hits=hits))
    return results


def add_scalar_reduction(model, parity, rows):
    existing = {v.name: model.get_int_var_from_proto_index(i)
                for i, v in enumerate(model.proto.variables)}

    def count(color, *positions):
        pattern = tuple(sorted(positions))
        return existing[f"count_{(color, pattern)}"]

    for j, side in product(AXES, (0, 1)):
        alpha = parity ^ side
        beta = 1-alpha
        A, B = (j, 1-side), (j, side)
        gap3 = existing[f"gap3_{j}"]
        forward = existing[f"new_forward_{j}_{side}"]
        for i in AXES:
            if i == j:
                continue
            one = (i, 1)
            a, b = count(alpha, A, one), count(beta, A, one)
            c, d = count(alpha, B, one), count(beta, B, one)
            model.add_allowed_assignments((a, b, c, d), sorted(rows)).only_enforce_if((gap3, forward))


def check_candidate_scalars(w, rows):
    colors = w["even_holes"], w["odd_holes"]
    for j, side in product(AXES, (0, 1)):
        groups = oriented_cut(colors, j, side)
        if tuple(map(len, groups)) != (3, 6, 5, 2):
            continue
        for i in AXES:
            if i != j:
                assert tuple(load(group, i) for group in groups) in rows


def solve(parity, rows):
    started = monotonic()
    model, by_color, old_plans = make_model(parity)
    forward_plans = add_forward_exclusions(model, by_color, parity)
    split_plans = add_split_exclusions(model, parity)
    add_scalar_reduction(model, parity, rows)
    error = model.validate()
    if error:
        raise ValueError(error)
    built = monotonic()
    print(f"parity={parity} model built and validated in {built-started:.3f}s", flush=True)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = SECONDS
    solver.parameters.num_workers = WORKERS
    solver.parameters.random_seed = 20261115
    status = solver.solve(model)
    result = dict(parity=parity, status=solver.status_name(status),
                  build_seconds=built-started, solver_wall_seconds=solver.wall_time,
                  model_stats=model.model_stats(), response_stats=solver.response_stats(),
                  old_central_plans=old_plans, free_A6_plans=forward_plans,
                  split_plans=split_plans)
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        colors = [sorted(v for v, flag in by_color[c].items() if solver.value(flag))
                  for c in (0, 1)]
        w = verify(colors, parity)
        w["direct_split_cuts_checked"] = verify_candidate_splits(w)
        check_candidate_scalars(w, rows)
        result["candidate"] = w
    return result


def main():
    verify_supply_table()
    rows = scalar_rows()
    data = dict(seconds_per_parity=SECONDS, workers=WORKERS, scalar_rows=len(rows),
                known_input_gate_checks=readback_known(), solves=[])
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
    print([(r["input"], len(r["hits"])) for r in data["known_input_gate_checks"]], flush=True)
    for parity in (0, 1):
        row = solve(parity, rows)
        data["solves"].append(row)
        out.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
        print(f"parity={parity} {row['status']} wall={row['solver_wall_seconds']:.3f}s", flush=True)
        w = row.get("candidate")
        if w is not None and w["matching"] is not None:
            print(w["even_holes"], w["odd_holes"], "matching found", flush=True)
            w["fixed_input_old_checks"] = old_gate_checks(w)
            out.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
            print("legacy", w["fixed_input_old_checks"]["legacy"]["status"], flush=True)
            break


if __name__ == "__main__":
    main()

