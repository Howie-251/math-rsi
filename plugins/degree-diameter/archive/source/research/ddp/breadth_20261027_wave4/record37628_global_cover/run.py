"""One full 37628-row set-cover MILP; no reduced leftover-only model."""

from collections import Counter, deque
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "pencil_source/deg11_diam5_n37628.txt"


def worker():
    # Compilation plus the already completed matrix builder consumed <3 CPU s;
    # this stricter worker cap keeps the entire finite batch below60 CPU s.
    resource.setrlimit(resource.RLIMIT_CPU, (56, 56))
    start = time.process_time()
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, milp
    from scipy.sparse import csc_array

    metadata = json.loads((HERE / "matrix_metadata.json").read_text())
    n, f = metadata["base_vertices"], metadata["eligible_variables"]
    indices = np.fromfile(HERE / "indices.i32.bin", dtype=np.int32)
    pointers = np.fromfile(HERE / "indptr.i32.bin", dtype=np.int32)
    assert len(indices) == metadata["total_nonzeros"]
    assert len(pointers) == f + 1 and pointers[-1] == len(indices)
    counts = np.bincount(indices, minlength=n + 1)
    assert np.all(counts[:n] > 0) and counts[n] == f
    matrix = csc_array((np.ones(len(indices), dtype=np.float64), indices, pointers), shape=(n + 1, f))
    lower = np.ones(n + 1)
    upper = np.full(n + 1, np.inf)
    lower[n], upper[n] = -np.inf, 11
    preparation = time.process_time() - start
    result = milp(
        np.ones(f), integrality=np.ones(f), bounds=Bounds(np.zeros(f), np.ones(f)),
        constraints=LinearConstraint(matrix, lower, upper),
        options={"time_limit": 45.0, "threads": 1, "mip_rel_gap": 0.0, "disp": True},
    )
    out = {
        "solver_status": int(result.status), "solver_message": str(result.message),
        "solver_calls": 1, "solver_handle_restarts": 0, "threads": 1,
        "solver_time_limit_seconds": 45, "worker_CPU_hard_limit_seconds": 56,
        "batch_CPU_budget_seconds": 60, "warm_start_used": False,
        "variables": f, "coverage_rows": n, "cardinality_rows": 1,
        "total_nonzeros": len(indices), "minimum_row_covering_eligible_count": int(counts[:n].min()),
        "maximum_row_covering_eligible_count": int(counts[:n].max()),
        "preparation_CPU_seconds": preparation, "incumbent_returned": result.x is not None,
        "mip_node_count": getattr(result, "mip_node_count", None),
        "mip_gap": getattr(result, "mip_gap", None),
        "mip_dual_bound": getattr(result, "mip_dual_bound", None),
        "full_source_BFS_performed": False, "new_graph_generated": False,
    }
    if result.x is not None:
        rounded = np.rint(result.x).astype(int)
        integral = bool(np.max(np.abs(result.x - rounded)) < 1e-6)
        eligible = metadata["eligible_vertices"]
        neighbours = [eligible[i] for i, selected in enumerate(rounded) if selected]
        adjacency = []
        for line in SOURCE.read_text().splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            row = list(map(int, line.split()))
            assert row[0] == len(adjacency)
            adjacency.append(row[1:])
        distances = [-1] * n
        queue = deque(neighbours)
        for v in neighbours:
            distances[v] = 0
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if distances[v] < 0:
                    distances[v] = distances[u] + 1
                    queue.append(v)
        missing = [v for v, d in enumerate(distances) if d < 0 or d > 4]
        budget = {
            "new_vertex_degree": len(neighbours), "degree_cap": 11,
            "neighbour_old_degrees": [len(adjacency[v]) for v in neighbours],
            "neighbour_new_degrees": [len(adjacency[v]) + 1 for v in neighbours],
            "all_selected_eligible": all(len(adjacency[v]) < 11 for v in neighbours),
        }
        valid = integral and bool(np.all((rounded == 0) | (rounded == 1))) and 1 <= len(neighbours) <= 11
        valid = valid and budget["all_selected_eligible"] and not missing
        check = {
            "integer_candidate": integral, "neighbours": neighbours,
            "independent_multi_source_BFS_runs": 1, "BFS_nodes": n,
            "distance_histogram": dict(sorted(Counter(distances).items())),
            "uncovered_vertices": missing, "uncovered_count": len(missing),
            "degree_budget": budget, "candidate_valid": valid,
            "method": "Full multi-source deque BFS on source adjacency, independent of the R4 matrix.",
        }
        (HERE / "candidate_cover_check.json").write_text(json.dumps(check, indent=2) + "\n")
        out.update(check)
        if valid:
            (HERE / "candidate_neighbors.json").write_text(json.dumps({
                "base_vertices": n, "prospective_order": n + 1,
                "neighbours": neighbours, "degree_cap": 11,
                "all37628_vertices_covered_within4": True,
            }, indent=2) + "\n")
    out["worker_CPU_seconds"] = time.process_time() - start
    out["worker_peak_resident_KiB"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    (HERE / "worker_result.json").write_text(json.dumps(out, indent=2) + "\n")


def children_cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime + r.ru_stime


def main():
    if "--worker" in sys.argv:
        return worker()
    started, wall, child_before = time.process_time(), time.monotonic(), children_cpu()
    # Reproducible entry point: if temporary CSC files were removed, regenerate
    # precisely the same complete matrix, never a115-point relaxation.
    if not (HERE / "indices.i32.bin").exists():
        subprocess.run(["g++", "-O3", "-std=c++17", str(HERE / "build_matrix.cpp"),
                        "-o", str(HERE / "build_matrix")], check=True)
        subprocess.run([str(HERE / "build_matrix"), str(SOURCE), str(HERE)], check=True)
    env = dict(os.environ)
    env.update({"OMP_NUM_THREADS": "1", "OPENBLAS_NUM_THREADS": "1", "MKL_NUM_THREADS": "1"})
    with (HERE / "solver.log").open("w") as output:
        completed = subprocess.run([sys.executable, str(Path(__file__).resolve()), "--worker"],
                                   stdout=output, stderr=subprocess.STDOUT, env=env)
    result_file = HERE / "worker_result.json"
    result = json.loads(result_file.read_text()) if result_file.exists() else {}
    if result.get("candidate_valid"):
        status = "GLOBAL_COVER_HIT_ALL37628_VERIFIED"
    elif result.get("solver_status") == 2:
        status = "GLOBAL_SET_COVER_SOLVER_REPORTED_INFEASIBLE_UNCERTIFIED"
    elif completed.returncode:
        status = "PROCESS_TERMINATED_UNKNOWN_NO_VALID_COVER"
    else:
        status = "GLOBAL_SET_COVER_UNKNOWN_NO_VALID_INCUMBENT"
    metadata = json.loads((HERE / "matrix_metadata.json").read_text())
    result.update({
        "status": status, "process_returncode": completed.returncode,
        "child_process_CPU_seconds_this_driver": children_cpu() - child_before,
        "driver_CPU_seconds": time.process_time() - started,
        "wall_seconds_this_driver": time.monotonic() - wall,
        "earlier_compile_CPU_seconds": metadata.get("compile_CPU_seconds", 0),
        "earlier_builder_CPU_seconds": metadata.get("builder_child_CPU_seconds", 0),
        "total_CPU_seconds_including_prior_matrix_build": children_cpu() - child_before
            + time.process_time() - started + metadata.get("compile_CPU_seconds", 0)
            + metadata.get("builder_child_CPU_seconds", 0),
        "temporary_CSC_files_removed": True,
        "scope": "All2504 eligible vertices; all37628 radius4 cover inequalities plus sum x<=11; one solver handle.",
        "direction_stopped_after_this_terminal": True, "new_lower_bounds": 0,
    })
    for name in ("indices.i32.bin", "indptr.i32.bin"):
        (HERE / name).unlink(missing_ok=True)
    (HERE / "terminal.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
