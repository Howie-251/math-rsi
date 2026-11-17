"""Capped test for unrestricted forward A6 supply or the old central five gates."""
import json
from itertools import product
from pathlib import Path
from time import monotonic

from ortools.sat.python import cp_model

from FREE_A6_SUPPLY import VALID_B, forward_supply, verify_supply_table
from GLOBAL_PROBE import indicator_equal, make_model, verify_model_solution
from PROBE import AXES, MASK

SECONDS = 60
WORKERS = 8
HERE = Path(__file__).resolve().parent


def add_forward_exclusions(model, holes, parity):
    existing = {v.name: model.get_int_var_from_proto_index(k)
                for k, v in enumerate(model.proto.variables)}

    def count(color, *positions):
        pattern = tuple(sorted(positions))
        return existing[f"count_{(color, pattern)}"]

    lam = [count(parity, (j, 1)) + count(1-parity, (j, 0)) for j in AXES]
    for left, right in zip(lam, lam[1:]):
        model.add(left >= right)
    model.add(count(parity, (0, 1)) == 3)
    model.add(count(1-parity, (0, 0)) == 2)
    if parity == 1:
        model.add(sum(flag for v, flag in holes[parity].items() if v.bit_count() == 1) <= 6)
        model.add(sum(flag for v, flag in holes[1-parity].items()
                      if (MASK ^ v).bit_count() == 1) <= 6)

    supplier_rows = [(a, b, c) for a, bs in VALID_B.items() for b in bs for c in range(2, 6)]
    n = 0
    for j, B_side in product(AXES, (0, 1)):
        alpha = parity ^ B_side
        beta = 1-alpha
        A, B = (j, 1-B_side), (j, B_side)
        r3 = indicator_equal(model, count(alpha, A), 3, f"new_forward_{j}_{B_side}")
        active = (existing[f"gap3_{j}"], r3)
        for k, t in product(AXES, (0, 1)):
            if k == j:
                continue
            T = (k, t)
            counts = (count(alpha, A, T), count(beta, A, T), count(alpha, B, T))
            model.add_forbidden_assignments(counts, supplier_rows).only_enforce_if(active)
            n += 1
    assert n == 168
    return n


def verify(colors, parity):
    w = verify_model_solution(colors, parity)
    lam = w["lambda_by_axis"]
    assert lam == sorted(lam, reverse=True)
    assert tuple(sum(v & 1 for v in w[key]) for key in ("P", "Q")) == (3, 2)
    if parity == 1:
        assert all(sum(v.bit_count() == 1 for v in w[key]) <= 6 for key in ("P", "Q"))
    for j, B_side in product(AXES, (0, 1)):
        assert forward_supply(colors, j, B_side) is None
    return w


def solve(parity):
    started = monotonic()
    model, by_parity, gap3_plans = make_model(parity)
    forward_plans = add_forward_exclusions(model, by_parity, parity)
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
    row = dict(parity=parity, status=solver.status_name(status),
               build_seconds=built-started, solver_wall_seconds=solver.wall_time,
               model_stats=model.model_stats(), response_stats=solver.response_stats(),
               gap3_plans=gap3_plans, forward_plans=forward_plans)
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        colors = [sorted(v for v, flag in by_parity[c].items() if solver.value(flag))
                  for c in (0, 1)]
        row["candidate"] = verify(colors, parity)
    return row


def main():
    verify_supply_table()
    result = dict(seconds_per_parity=SECONDS, workers=WORKERS, solves=[])
    output = Path(__file__).with_suffix(".json")
    for parity in (0, 1):
        row = solve(parity)
        result["solves"].append(row)
        output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
        print(f"parity={parity} {row['status']} wall={row['solver_wall_seconds']:.3f}s", flush=True)
        candidate = row.get("candidate")
        if candidate is not None:
            print(candidate["even_holes"], candidate["odd_holes"],
                  "matching found", candidate["matching"] is not None,
                  "omitted macros", candidate["omitted_macro_hits"], flush=True)
            break


if __name__ == "__main__":
    main()

