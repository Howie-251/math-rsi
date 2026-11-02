"""One global equitable-cell H(9) partial-fold MILP; one solver handle only."""

from collections import Counter
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time
import warnings


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/Q_data.json"
TARGET_GAIN = 8946


def worker():
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    start = time.process_time()
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp
    from scipy.sparse import coo_array

    partition = json.loads((HERE / "partition.json").read_text())
    data = json.loads(SOURCE.read_text())
    cells = partition["cells"]
    qcells = [c for c in cells if c["kind"] == "generic"]
    hcells = [c for c in cells if c["kind"] != "generic"]
    assert len(qcells) <= 3000
    qindex = {c["id"]: i for i, c in enumerate(qcells)}
    hindex = {c["id"]: 2 * len(qcells) + i for i, c in enumerate(hcells)}
    nvars = 2 * len(qcells) + len(hcells)
    objective = np.zeros(nvars)
    for i, c in enumerate(qcells):
        objective[2 * i:2 * i + 2] = c["size"]
    for c in hcells:
        objective[hindex[c["id"]]] = c["size"]

    row_ids, column_ids, values, lower, upper = [], [], [], [], []

    def row(coefficients, lb, ub):
        r = len(lower)
        for v, coefficient in coefficients.items():
            if coefficient:
                row_ids.append(r)
                column_ids.append(v)
                values.append(coefficient)
        lower.append(lb)
        upper.append(ub)

    def add(d, v, a):
        d[v] = d.get(v, 0) + a

    for i, cell in enumerate(qcells):
        neighbours = {int(k): v for k, v in cell["neighbor_counts"].items()}
        dq = sum(m for j, m in neighbours.items() if j in qindex)
        merged, same0, same1 = {}, {}, {}
        for j, m in neighbours.items():
            if j in qindex:
                a = 2 * qindex[j]
                add(merged, a, m)
                add(merged, a + 1, m)
                add(same0, a, m)
                add(same1, a + 1, m)
            else:
                z = hindex[j]
                add(merged, z, m)
                add(same0, z, m)
                add(same1, z, m)
        add(merged, 2 * i, -dq)
        add(merged, 2 * i + 1, -dq)
        add(same0, 2 * i, dq)
        add(same1, 2 * i + 1, dq)
        row(merged, -np.inf, 2)
        row(same0, -np.inf, 2 + dq)
        row(same1, -np.inf, 2 + dq)
        row({2 * i: 1, 2 * i + 1: 1}, -np.inf, 1)
    for cell in hcells:
        coefficients = {}
        for sj, m in cell["neighbor_counts"].items():
            j = int(sj)
            if j in qindex:
                a = 2 * qindex[j]
                add(coefficients, a, m)
                add(coefficients, a + 1, m)
            else:
                add(coefficients, hindex[j], m)
        row(coefficients, -np.inf, 5 + (cell["kind"] == "H3_absolute"))
    row({i: int(c) for i, c in enumerate(objective)}, TARGET_GAIN, np.inf)
    matrix = coo_array((np.asarray(values, dtype=float),
                        (np.asarray(row_ids, dtype=np.int32), np.asarray(column_ids, dtype=np.int32))),
                       shape=(len(lower), nvars)).tocsc()
    # scipy's HiGHS binding expects C-int sparse indices.
    matrix.indices = matrix.indices.astype(np.int32)
    matrix.indptr = matrix.indptr.astype(np.int32)
    bounds_upper = np.ones(nvars)
    bounds_upper[2 * len(qcells):] = 2
    preparation = time.process_time() - start
    solver_limit = max(0.1, 28.0 - (time.process_time() - start))
    with warnings.catch_warnings(record=True):
        result = milp(
            -objective,
            integrality=np.ones(nvars),
            bounds=Bounds(np.zeros(nvars), bounds_upper),
            constraints=LinearConstraint(matrix, np.asarray(lower), np.asarray(upper)),
            options={"time_limit": solver_limit, "mip_rel_gap": 0.0, "threads": 1, "disp": False},
        )
    out = {
        "solver_status": int(result.status), "solver_message": str(result.message),
        "solver_calls": 1, "threads": 1, "warm_start_used": False,
        "objective": "maximize weighted splits plus H3 copies, with gain at least8946",
        "target_order": 42343, "target_gain_over33397": TARGET_GAIN,
        "generic_cells": len(qcells), "H3_cells": len(hcells),
        "variables": nvars, "constraint_rows": len(lower), "nonzero_coefficients": len(values),
        "preparation_CPU_seconds": preparation, "solver_time_limit_seconds": solver_limit,
        "process_CPU_hard_limit_seconds": 30,
        "incumbent_returned": result.x is not None,
        "mip_node_count": getattr(result, "mip_node_count", None),
        "mip_gap": getattr(result, "mip_gap", None),
        "mip_dual_bound": getattr(result, "mip_dual_bound", None),
        "explicit_large_graph_generated": False, "full_BFS_performed": False,
    }
    if result.x is not None:
        rounded = np.rint(result.x).astype(int)
        integral = bool(np.max(np.abs(result.x - rounded)) < 1e-6)
        products = matrix @ rounded
        linear_ok = bool(np.all(products >= np.asarray(lower)) and np.all(products <= np.asarray(upper)))
        bound_ok = bool(np.all(rounded >= 0) and np.all(rounded <= bounds_upper))
        states, copies = [0] * len(data["Q"]), [0] * len(data["H3_graph"])
        for i, cell in enumerate(qcells):
            state = int(rounded[2 * i] + 2 * rounded[2 * i + 1])
            for v in cell["members"]:
                states[v] = state
        for cell in hcells:
            for v in cell["members"]:
                copies[v - len(states)] = int(rounded[hindex[cell["id"]]])
        histogram = Counter()
        for f, neighbours in enumerate(data["Q"]):
            split = states[f] != 0
            extra = sum((states[g] == states[f]) if split else (states[g] != 0) for g in neighbours)
            h = data["H3_neighbors"][f]
            h_extra = copies[h] if h is not None and h >= 0 else 0
            degree = 10 + extra + h_extra
            histogram[degree] += 2 if split else 1
        for h, neighbours in enumerate(data["H3_graph"]):
            degree = (7 - data["H3_absolute"][h]
                      + sum(states[f] != 0 for f in data["H3_generic_neighbors"][h])
                      + sum(copies[j] for j in neighbours))
            histogram[degree] += 1 + copies[h]
        nsplit = sum(s != 0 for s in states)
        order = 33397 + nsplit + sum(copies)
        direct_ok = max(histogram) <= 12 and sum(histogram.values()) == order
        valid = integral and linear_ok and bound_ok and direct_ok and order >= 42343
        out.update({"integer_candidate": integral, "linear_constraints_checked": linear_ok,
                    "variable_bounds_checked": bound_ok, "direct_all_vertex_degree_check": direct_ok,
                    "candidate_order": order, "candidate_split_fibers": nsplit,
                    "candidate_H3_extra_copies": sum(copies),
                    "candidate_degree_histogram": dict(sorted(histogram.items())),
                    "candidate_valid": valid})
        if valid:
            (HERE / "candidate_state.json").write_text(json.dumps({
                "state": states, "H3_copies": copies, "order": order,
                "source_partition": "partition.json", "direct_all_vertex_degree_check": True,
            }, separators=(",", ":")) + "\n")
    out["worker_CPU_seconds"] = time.process_time() - start
    (HERE / "worker_result.json").write_text(json.dumps(out, indent=2) + "\n")


def main():
    if "--worker" in sys.argv:
        return worker()
    start = time.process_time()
    wall = time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    env = dict(os.environ)
    env.update({"OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"})
    with (HERE / "worker.log").open("w") as output:
        completed = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--worker"],
                                   stdout=output, stderr=subprocess.STDOUT, env=env)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    result_file = HERE / "worker_result.json"
    result = json.loads(result_file.read_text()) if result_file.exists() else {}
    if result.get("candidate_valid"):
        status = "FEASIBLE_GLOBAL_CELL_STATE_EXPANDED_DEGREES_CHECKED"
    elif result.get("solver_status") == 2:
        status = "ANCHORED_EQUITABLE_TARGET_MILP_REPORTED_INFEASIBLE"
    elif completed.returncode != 0:
        status = "CPU_LIMIT_OR_PROCESS_TERMINATION_UNKNOWN"
    else:
        status = "GLOBAL_CELL_TARGET_UNKNOWN_NO_VALID_INCUMBENT"
    result.update({
        "status": status, "process_returncode": completed.returncode,
        "child_process_CPU_seconds": after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime,
        "driver_CPU_seconds": time.process_time() - start,
        "wall_seconds": time.monotonic() - wall,
        "anchors_attempted": 1, "solver_handle_restarts": 0,
        "author_split_state_used": False,
        "scope": "One anchored equitable partition; global cell-constant states only, no fixed exterior and no author split lower bound.",
        "new_lower_bounds": 0,
    })
    (HERE / "terminal.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
