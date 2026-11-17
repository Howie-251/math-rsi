"""One bounded a=1 query with the audited two-bridge receive condition."""

import hashlib
import json
from pathlib import Path
import sys
from time import perf_counter

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
SUPPLEMENT = BASE.parent / "mu0_global_2026_11_15"
sys.path.insert(0, str(BASE))

import ortools
from ortools.sat.python import cp_model

from EDGE_HIGH_GAP_PROBE import INNER_AXES, build
from EDGE_PROBE import ALPHA, BETA, B_ALPHA, B_BETA, SEED, VERTICES, bit_is_one, check_holes


LIMIT_SECONDS = 60
WORKERS = 8


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def forbidden_pairs(a):
    r = 7 - a
    rows = set()
    for q in (0, 1, r - 3, r - 2):
        rows.add((q + 3, q))
        rows.add((r - q - 2, r - q))
    assert len(rows) == 8
    return sorted(rows)


def add_coverage(model, holes, a):
    rows = forbidden_pairs(a)
    for axis in INNER_AXES:
        alpha = model.new_int_var(0, 8 - a, f"delta2_large_alpha_{axis}")
        beta = model.new_int_var(0, 7 - a, f"delta2_large_beta_{axis}")
        model.add(alpha == sum(holes[v] for v in B_ALPHA if bit_is_one(v, axis)))
        model.add(beta == sum(holes[v] for v in B_BETA if bit_is_one(v, axis)))
        model.add_forbidden_assignments([alpha, beta], rows)
    return rows


def describe_solution(solver, holes, a):
    vertices = {v for v in VERTICES if solver.value(holes[v])}
    axes = check_holes(a, vertices)
    # Check both half orientations directly from returned physical vertex labels.
    r = 7 - a
    for axis in INNER_AXES:
        for side in (False, True):
            alpha = sum(v in vertices and bit_is_one(v, axis) == side for v in B_ALPHA)
            beta = sum(v in vertices and bit_is_one(v, axis) == side for v in B_BETA)
            assert alpha - beta != 3 or min(beta, r - beta - 2) >= 2
    return {
        "holes_alpha_odd": sorted(vertices.intersection(ALPHA)),
        "holes_beta_even": sorted(vertices.intersection(BETA)),
        "axes": axes,
        "short_matching_realization_checked": False,
    }


def main():
    proof = SUPPLEMENT / "Q6_BALANCED_DELTA2_TRANSFER.md"
    audit = SUPPLEMENT / "Q6_BALANCED_DELTA2_TRANSFER_REVIEW.json"
    receipt = json.loads(audit.read_text(encoding="utf-8-sig"))
    assert receipt["verdict"] == "PASS"
    assert receipt["audited_input_hashes"][proof.name] == f"sha256:{digest(proof)}"
    frozen_model = BASE / "EDGE_HIGH_GAP_PROBE.py"
    frozen_review = BASE / "EDGE_HIGH_GAP_MODEL_REVIEW.json"
    frozen_receipt = json.loads(frozen_review.read_text(encoding="utf-8-sig"))
    assert frozen_receipt["verdict"] == "PASS"
    assert frozen_receipt["audited_input_hashes"][frozen_model.name] == f"sha256:{digest(frozen_model)}"

    a = 1
    start = perf_counter()
    model, holes, old_gate_stats = build(a)
    rows = add_coverage(model, holes, a)
    error = model.validate()
    if error:
        raise ValueError(error)
    build_seconds = perf_counter() - start
    print(f"a={a} validated in {build_seconds:.3f}s", flush=True)

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = LIMIT_SECONDS
    solver.parameters.num_search_workers = WORKERS
    solver.parameters.random_seed = SEED
    status = solver.solve(model)
    result = {
        "scope": "Diagnostic only: EDGE_HIGH_GAP plus the audited majority deletion and difference-two two-bridge condition on the selected large face.",
        "a": a,
        "cp_calls": 1,
        "cp_limit_seconds": LIMIT_SECONDS,
        "workers": WORKERS,
        "seed": SEED,
        "ortools_version": ortools.__version__,
        "status": solver.status_name(status),
        "build_wall_seconds": build_seconds,
        "cp_wall_seconds": solver.wall_time,
        "old_gate_stats": old_gate_stats,
        "new_gate": {"axes": INNER_AXES, "forbidden_alpha_beta_pairs_per_axis": rows},
        "model_stats": model.model_stats(),
        "solver_stats": solver.response_stats(),
        "sha256": {
            path.name: digest(path)
            for path in (Path(__file__), frozen_model, frozen_review, proof, audit)
        },
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        result["solution"] = describe_solution(solver, holes, a)
    (HERE / "probe.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"a={a}: {result['status']} in {solver.wall_time:.3f}s", flush=True)


if __name__ == "__main__":
    main()
