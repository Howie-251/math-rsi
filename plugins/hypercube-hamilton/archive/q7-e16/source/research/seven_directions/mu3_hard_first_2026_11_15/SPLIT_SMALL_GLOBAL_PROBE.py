"""Search the light normalized domain for a hole set outside both free A6 supply gates."""
from collections import Counter
from itertools import product
import json
from pathlib import Path
import sys
from time import monotonic, process_time
from unittest.mock import patch

from ortools.sat.python import cp_model

from FREE_A6_SUPPLY import make_model, verify_candidate, verify_supply_table
from GLOBAL_PROBE import indicator_equal
from NEW_SPLIT_CHECK import check_cut
from PROBE import AXES

HERE = Path(__file__).resolve().parent
SECONDS = 30
LEGACY_CPU_LIMIT = 30
WORKERS = 8


def forbidden_rows(k):
    """Scalar profiles with a realizable controlled donor split on a fixed T."""
    rows = set()
    for s in range(3):
        r = 8-k-s
        b_total, c_total = r+k, s+k
        for a, b, c in product(range(r+1), range(b_total+1), range(c_total+1)):
            for eps in (0, 1):
                q_T = b-a-eps
                q_E = k-1-q_T
                if (q_T not in (1, 2) or q_E not in (1, 2)
                        or (q_T == 2 and a > 1) or (q_E == 2 and r-a > 1)):
                    continue
                if c < q_T or c_total-c < q_E:
                    continue
                if (b if eps else b_total-b) == 0:
                    continue
                rows.add((r, s, a, b, c))
    return sorted(rows)


def add_split_exclusions(model, parity):
    existing = {v.name: model.get_int_var_from_proto_index(i)
                for i, v in enumerate(model.proto.variables)}

    def count(color, *positions):
        pattern = tuple(sorted(positions))
        return existing[f"count_{(color, pattern)}"]

    tables = {k: forbidden_rows(k) for k in (3, 4, 5)}
    n_tables = 0
    for j in AXES:
        lam = count(parity, (j, 1)) + count(1-parity, (j, 0))
        active = {k: indicator_equal(model, lam, 8-k, f"split_gap_{j}_{k}")
                  for k in (4, 5)}
        active[3] = existing[f"gap3_{j}"]
        for B_side in (0, 1):
            alpha = parity ^ B_side
            beta = 1-alpha
            A, B = (j, 1-B_side), (j, B_side)
            r, s = count(alpha, A), count(beta, B)
            for inner in AXES:
                if inner == j:
                    continue
                T = (inner, 0)
                a, b, c = count(alpha, A, T), count(beta, A, T), count(alpha, B, T)
                for k, table in tables.items():
                    model.add_forbidden_assignments((r, s, a, b, c), table).only_enforce_if(active[k])
                    n_tables += 1
    assert n_tables == 252
    return dict(tables=n_tables, profile_counts={k: len(table) for k, table in tables.items()})


def verify_candidate_splits(candidate):
    colors = tuple(tuple(candidate[key]) for key in ("even_holes", "odd_holes"))
    checked = [(j, b) for j, b in product(AXES, (0, 1))
               if abs(candidate["delta_even_minus_odd"][j]) in (3, 4, 5)]
    for j, b in checked:
        assert check_cut(colors, j, b) is None, (j, b)
    return checked


def solve(parity):
    started = monotonic()
    verify_supply_table()
    model, holes = make_model(parity)
    new_split = add_split_exclusions(model, parity)
    error = model.validate()
    if error:
        raise ValueError(error)
    built = monotonic()
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = SECONDS
    solver.parameters.num_workers = WORKERS
    solver.parameters.random_seed = 20261115
    print(f"parity={parity} model built and validated in {built - started:.3f}s", flush=True)
    status = solver.solve(model)
    row = dict(parity=parity, status=solver.status_name(status),
               build_seconds=built-started, solver_wall_seconds=solver.wall_time,
               model_stats=model.model_stats(), response_stats=solver.response_stats(),
               new_split=new_split)
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        colors = [sorted(v for v, flag in holes[c].items() if solver.value(flag))
                  for c in (0, 1)]
        candidate = verify_candidate(colors, parity)
        candidate["direct_split_cuts_checked"] = verify_candidate_splits(candidate)
        row["candidate"] = candidate
    return row


def old_gate_checks(candidate):
    # Frozen legacy is called for one actual hole geometry only.
    sys.path.insert(0, str(HERE.parent / "global_bridge_2026_11_15"))
    import exception_legacy_menu as old
    from JOINT_GAP_PROBE import check_high_gaps

    colors = tuple(tuple(candidate[k]) for k in ("even_holes", "odd_holes"))
    delta = old.signed_gaps(colors)
    assert list(delta) == candidate["delta_even_minus_odd"]
    try:
        high_gap = dict(status="NO_PLAN", checks=check_high_gaps(colors, delta))
    except AssertionError as error:
        first = error.args[0]
        assert isinstance(first, dict) and first["four_donor_gates"] is not None
        high_gap = dict(status="PASS_PLAN", first_plan=first)

    plan = None
    begun = process_time()
    counters = Counter()
    try:
        with patch.object(old, "CPU_LIMIT", LEGACY_CPU_LIMIT), old.legacy_menu(begun) as find:
            plan = find(colors, delta, counters)
        status = "PASS_PLAN" if plan is not None else "NO_PLAN"
    except TimeoutError as error:
        status = f"TIMEOUT: {error}"
    legacy = dict(status=status, plan=plan, counters=counters, cpu_limit=LEGACY_CPU_LIMIT,
                  cpu_seconds=process_time()-begun, requires_edge=old.requires_edge(plan))
    return dict(high_gap_positive_split=high_gap, legacy=legacy)


def main():
    data = dict(seconds_per_parity=SECONDS, workers=WORKERS, solves=[])
    path = Path(__file__).with_suffix(".json")
    for parity in (0, 1):
        row = solve(parity)
        data["solves"].append(row)
        path.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
        print(f"parity={parity} {row['status']} wall={row['solver_wall_seconds']:.3f}s", flush=True)
        candidate = row.get("candidate")
        if candidate is not None and candidate["matching"] is not None:
            print(candidate["even_holes"], candidate["odd_holes"], "matching found", flush=True)
            candidate["fixed_input_old_checks"] = old_gate_checks(candidate)
            path.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
            print("legacy", candidate["fixed_input_old_checks"]["legacy"]["status"], flush=True)
            break


if __name__ == "__main__":
    main()

