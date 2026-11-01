"""Two bounded actual-H affine attacks on the proposed shared W bound."""
import json
import os
from pathlib import Path
from itertools import combinations
from time import process_time, monotonic
import resource
import warnings

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
resource.setrlimit(resource.RLIMIT_CPU, (85, 85))
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csc_matrix

P = Path(__file__).parent
cpu, wall = process_time(), monotonic()
points = [(x, y) for x in range(5) for y in range(5)]
labels = list(range(25))
base = []
for slope in range(5):
    for intercept in range(5):
        base.append(tuple(5*x + ((slope*x+intercept) % 5) for x in range(5)))
for x in range(5):
    base.append(tuple(5*x+y for y in range(5)))
base = [tuple(sorted(e)) for e in base]
base_set = set(base)
assert len(base_set) == 30
orbits = [("collinear", [0, 5, 10]), ("noncollinear", [0, 5, 1])]
output = {
    "scope": "AG(2,5) 30 lines plus five distinct nonlines avoiding exactly three lows",
    "cpu_limit_seconds": 85,
    "solver_time_limit_per_orbit_seconds": 30,
    "threads_requested": 1,
    "point_label": "5*x+y",
    "orbits": [], "witnesses": [],
    "property_b_counterexample_claimed": False,
}

for name, lows in orbits:
    orbit_cpu, orbit_wall = process_time(), monotonic()
    outside = [v for v in labels if v not in lows]
    candidates = [e for e in combinations(outside, 5) if e not in base_set]
    # Every low lies on the unique affine line through a candidate point-pair
    # exactly when this determinant vanishes.
    pair_weights = {}
    for a, b in combinations(outside, 2):
        ax, ay = points[a]
        bx, by = points[b]
        pair_weights[a, b] = [
            int(((bx-ax)*(points[z][1]-ay)
                 -(by-ay)*(points[z][0]-ax)) % 5 == 0) for z in lows
        ]
    values = np.asarray([
        [sum(pair_weights[a, b][i] for a, b in combinations(e, 2))
         for i in range(3)] for e in candidates
    ], dtype=np.int32)
    objective = values.sum(axis=1)
    row_index, col_index, data = [], [], []
    location = {v: i+1 for i, v in enumerate(outside)}
    for j, edge in enumerate(candidates):
        row_index.append(0); col_index.append(j); data.append(1.0)
        for v in edge:
            row_index.append(location[v]); col_index.append(j); data.append(1.0)
    matrix = csc_matrix((data, (row_index, col_index)), shape=(23, len(candidates)))
    lower = np.asarray([5]+[1]*22, dtype=float)
    upper = np.asarray([5]+[np.inf]*22, dtype=float)
    with warnings.catch_warnings(record=True) as log:
        solution = milp(
            -objective.astype(float),
            integrality=np.ones(len(candidates), dtype=np.int32),
            bounds=Bounds(np.zeros(len(candidates)), np.ones(len(candidates))),
            constraints=LinearConstraint(matrix, lower, upper),
            options={"time_limit": 30, "threads": 1,
                     "presolve": True, "mip_rel_gap": 0.0},
        )
    row = {
        "name": name, "L": lows, "candidate_count": len(candidates),
        "single_edge_weight_max": int(objective.max()),
        "top_five_weight_upper": int(sum(sorted(map(int, objective), reverse=True)[:5])),
        "numerical_status": int(solution.status),
        "numerical_message": str(solution.message),
        "solver_warnings": [str(w.message) for w in log],
        "mip_dual_bound": (None if getattr(solution, "mip_dual_bound", None) is None
                           else float(solution.mip_dual_bound)),
    }
    if solution.x is not None:
        selected = [i for i, x in enumerate(solution.x) if x > 0.5]
        assert len(selected) == 5
        assert all(abs(float(solution.x[i])-round(float(solution.x[i]))) < 1e-6
                   for i in range(len(candidates)))
        extra = [candidates[i] for i in selected]
        assert set().union(*map(set, extra)) == set(outside)
        W = list(map(int, values[selected].sum(axis=0)))
        total = sum(W)
        witness = {
            "orbit": name, "L": lows, "edges": [list(e) for e in base+extra],
            "extra_edges": [list(e) for e in extra],
            "W": {str(z): v for z, v in zip(lows, W)},
            "sum_W": total,
            "strong_average_counterexample": total >= 78,
            "all_low_W_at_least_26": min(W) >= 26,
            "scope": "counterexample to W criterion only, never to Property B",
        }
        output["witnesses"].append(witness)
        row.update(best_integral_sum_W=total, best_integral_W=W)
    row.update(cpu_seconds=process_time()-orbit_cpu,
               wall_seconds=monotonic()-orbit_wall)
    output["orbits"].append(row)
    output.update(cpu_seconds=process_time()-cpu, wall_seconds=monotonic()-wall)
    (P/"RESULT.json").write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(row), flush=True)
    if output["witnesses"] and output["witnesses"][-1]["strong_average_counterexample"]:
        output["stop_reason"] = "explicit strong-W counterexample found; no family expansion"
        break
else:
    output["stop_reason"] = "two authorized affine orbits exhausted within solver limits"
output.update(cpu_seconds=process_time()-cpu, wall_seconds=monotonic()-wall)
(P/"RESULT.json").write_text(json.dumps(output, indent=2)+"\n")
