"""One bounded query on the normalized odd-support E16 joint remainder."""
import json
from pathlib import Path
from time import monotonic

from ortools.sat.python import cp_model

from FINAL_JOINT_PROBE import add_scalar_reduction, check_candidate_scalars, readback_known, scalar_rows
from FREE_A6_JOINT_PROBE import add_forward_exclusions, verify
from FREE_A6_SUPPLY import verify_supply_table
from GLOBAL_PROBE import make_model
from JOINT_GAP_PROBE import check_high_gaps, extend_model
from NEW_SPLIT_CHECK import read_saved_input
from SPLIT_SMALL_GLOBAL_PROBE import add_split_exclusions, old_gate_checks, verify_candidate_splits

PARITY = 1
SECONDS = 120
WORKERS = 8
HERE = Path(__file__).resolve().parent


def readback_high_gap_witness():
    filename = "FINAL_JOINT_PROBE.json"
    colors, delta = read_saved_input(filename)
    try:
        check_high_gaps(colors, delta)
    except AssertionError as error:
        row = error.args[0]
        assert row["gap"] == 5 and row["four_donor_gates"] is not None
        return dict(input=filename, gate="old_high_gap_positive_split", plan=row)
    raise AssertionError("Previous joint remainder missed its known gap-five plan")


def build(rows):
    model, holes, gap3_plans = make_model(PARITY)
    forward_plans = add_forward_exclusions(model, holes, PARITY)
    split_plans = add_split_exclusions(model, PARITY)
    add_scalar_reduction(model, PARITY, rows)
    high_plans = extend_model(model, holes)
    err = model.validate()
    if err:
        raise ValueError(err)
    return model, holes, dict(gap3=gap3_plans, forward=forward_plans, split=split_plans,
                              scalar=84, higher_gap=high_plans)


def verify_candidate(solver, holes, rows):
    colors = [sorted(v for v, selected in holes[c].items() if solver.value(selected))
              for c in (0, 1)]
    result = verify(colors, PARITY)
    result["direct_split_cuts_checked"] = verify_candidate_splits(result)
    check_candidate_scalars(result, rows)
    result["high_gap_positive_split_checked"] = check_high_gaps(colors,
                                                                result["delta_even_minus_odd"])
    return result


def main():
    verify_supply_table()
    rows = scalar_rows()
    known = readback_known()
    known.append(readback_high_gap_witness())
    data = dict(support_parity=PARITY, seconds_limit=SECONDS, workers=WORKERS,
                known_input_gate_checks=known)
    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
    started = monotonic()
    model, holes, counts = build(rows)
    built = monotonic()
    print(f"{len(known)} saved cases replayed; model built and validated in {built-started:.3f}s",
          flush=True)
    print(model.model_stats(), flush=True)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = SECONDS
    solver.parameters.num_workers = WORKERS
    solver.parameters.random_seed = 20261115
    status = solver.solve(model)
    data.update(status=solver.status_name(status), solver_wall_seconds=solver.wall_time,
                build_seconds=built-started, model_stats=model.model_stats(),
                response_stats=solver.response_stats(), plan_counts=counts)
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        data["candidate"] = verify_candidate(solver, holes, rows)
    out.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
    print(f"parity={PARITY} {data['status']} wall={solver.wall_time:.3f}s", flush=True)
    candidate = data.get("candidate")
    if candidate is not None and candidate["matching"] is not None:
        print(candidate["even_holes"], candidate["odd_holes"], "matching found", flush=True)
        candidate["fixed_input_old_checks"] = old_gate_checks(candidate)
        out.write_text(json.dumps(data, indent=2)+"\n", encoding="utf-8")
        print("legacy", candidate["fixed_input_old_checks"]["legacy"]["status"], flush=True)


if __name__ == "__main__":
    main()

