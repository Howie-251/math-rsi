"""One fifteen-second maximum-hit matching MILP on the one saved actual H."""
from pathlib import Path
from collections import Counter
from itertools import combinations
from time import process_time, monotonic
import json
import resource
import os
import warnings

os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

P = Path(__file__).parent
source = P.parents[2]/"middle"/"pairing_global"/"COUNTEREXAMPLE.json"
raw = json.loads(source.read_text())
edges = [set(e) for e in raw["edges"]]
n = raw["vertices"]
assert n == 24 and len(edges) == 35 and len({frozenset(e) for e in edges}) == 35
degree = Counter(v for e in edges for v in e)
pair_coverage = Counter(p for e in edges for p in combinations(sorted(e), 2))
assert min(degree.values()) == 7 and len(pair_coverage) == 276
pairs = list(combinations(range(n), 2))
N = len(pairs)
assert N == 276
start, wall = process_time(), monotonic()
# Every partial matching extends to a perfect one without losing any hit.
# Thus equality in the 24 degree rows preserves the maximum.
A = np.zeros((n+35, N+35))
lower, upper = [], []
for v in range(n):
    for j, pair in enumerate(pairs):
        A[v, j] = int(v in pair)
    lower.append(1.0); upper.append(1.0)
for i, edge in enumerate(edges):
    for j, pair in enumerate(pairs):
        if set(pair) <= edge:
            A[n+i, j] = -1.0
    A[n+i, N+i] = 1.0
    lower.append(-np.inf); upper.append(0.0)
objective = np.r_[np.zeros(N), -np.ones(35)]
with warnings.catch_warnings(record=True) as log:
    sol = milp(
        objective, integrality=np.ones(N+35),
        bounds=Bounds(np.zeros(N+35), np.ones(N+35)),
        constraints=LinearConstraint(A, lower, upper),
        options={"time_limit": 15, "threads": 1, "presolve": True},
    )
result = {
    "scope": "one fixed old actual H24; maximum hit matching; no new instances",
    "input": str(source.relative_to(P.parents[5])),
    "pair_variables": N, "hit_variables": 35, "vertex_rows": 24, "hit_link_rows": 35,
    "perfect_matching_without_loss": True,
    "numerical_status": int(sol.status), "numerical_message": str(sol.message),
    "solver_warnings": [str(w.message) for w in log],
    "numerical_objective": None if sol.fun is None else float(sol.fun),
    "numerical_dual_bound": (None if getattr(sol, "mip_dual_bound", None) is None
                             else float(sol.mip_dual_bound)),
    "analytic_old_hit_upper": 19,
}
if sol.x is not None:
    assert all(abs(float(x)-round(float(x))) < 1e-6 for x in sol.x)
    matching = [pairs[i] for i in range(N) if sol.x[i] > 0.5]
    assert len(matching) == 12 and len(set().union(*map(set, matching))) == 24
    hit = [i for i, e in enumerate(edges) if any(set(p) <= e for p in matching)]
    unhit = [i for i in range(35) if i not in hit]
    components, signs = {}, {}
    for c, (x, y) in enumerate(matching):
        components[x] = components[y] = c
        signs[x], signs[y] = 0, 1
    views = [{components[x]: signs[x] for x in edges[i]} for i in unhit]
    assert all(len(v) == 5 for v in views)
    compatibility = []
    for ii, jj in combinations(range(len(unhit)), 2):
        shared = set(views[ii]) & set(views[jj])
        relative = [views[ii][c] ^ views[jj][c] for c in sorted(shared)]
        compatible = len(set(relative)) <= 1
        if compatible:
            compatibility.append({
                "edge_indices": [unhit[ii], unhit[jj]],
                "shared_components": sorted(shared),
                "relative_signs": relative,
                "intersection_probability": (
                    "1/256" if not shared else f"1/{2**(9-len(shared))}"
                ),
            })
    result.update(
        matching=[list(p) for p in matching],
        actual_hit_count=len(hit), hit_edge_indices=hit, unhit_edge_indices=unhit,
        compatible_unhit_pairs=compatibility,
        new_19_hit_gate_applies=(len(hit) >= 20
                                or len(hit) == 19 and bool(compatibility)),
        exact_maximum_certified_by_old_analytic_upper=(len(hit) == 19),
    )
result.update(cpu_seconds=process_time()-start, wall_seconds=monotonic()-wall)
(P/"RESULT.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result))
