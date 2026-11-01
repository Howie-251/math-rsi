"""One fixed swapped-cube completion attack; one MILP, at most 30 seconds."""
from collections import Counter
from itertools import combinations
from pathlib import Path
from time import process_time, monotonic
import json
import resource
import os
import warnings

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
resource.setrlimit(resource.RLIMIT_CPU, (40, 40))
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import csc_matrix

P = Path(__file__).parent
start, wall = process_time(), monotonic()
low = [0, 1, 2]
high = list(range(3, 25))
base = [frozenset(range(5))]
for i in low:
    blocks = [
        {v for v in cube if ((v-cube.start) >> i) & 1 == bit}
        for cube in (range(5, 13), range(13, 21)) for bit in (0, 1)
    ] + [set(range(21, 25))]
    if i == 2:
        blocks[0] ^= {5, 21}
        blocks[4] ^= {5, 21}
    assert len(blocks) == 5 and all(len(q) == 4 for q in blocks)
    base.extend(frozenset({i} | q) for q in blocks)
assert len(set(base)) == 16
degree = Counter(v for e in base for v in e)
pairs = Counter(pair for e in base for pair in combinations(sorted(e), 2))
target = {v: 6 if v in low else 8 if v in (22, 23, 24) else 7
          for v in range(25)}
remaining = {v: target[v]-degree[v] for v in high}
repeat_used = {
    v: sum(max(0, pairs[tuple(sorted((v, w)))]-1)
           for w in range(25) if w != v) for v in high
}
repeat_left = {v: 4*target[v]-24-repeat_used[v] for v in high}
star = [[e-{z} for e in base if z in e] for z in low]
for z, blocks in zip(low, star):
    assert len(blocks) == 6 and sum(map(len, blocks)) == 24
    assert set().union(*map(set, blocks)) == set(range(25))-{z}
base_W = [
    sum(sum(len(e & q)*(len(e & q)-1)//2 for q in blocks)
        for e in base if z not in e)
    for z, blocks in zip(low, star)
]
assert base_W == [24, 24, 20]
missing = [pair for pair in combinations(high, 2) if pairs[pair] == 0]
cheap = {
    "base_edge_count": len(base), "base_W": base_W,
    "base_high_pairs_covered": 231-len(missing),
    "missing_high_pairs": len(missing),
    "remaining_degree": remaining, "remaining_degree_sum": sum(remaining.values()),
    "positive_base_repeat_rows": repeat_used, "repeat_budget_left": repeat_left,
}
output = {
    "scope": "one fixed three-low swapped-cube construction, nineteen all-high extras",
    "L": low, "base_edges": [sorted(e) for e in base],
    "target_degree": target, "cheap_base": cheap,
    "solver_time_limit_seconds": 30, "threads_requested": 1,
    "witnesses": [], "property_b_counterexample_claimed": False,
}

def save():
    output.update(cpu_seconds=process_time()-start, wall_seconds=monotonic()-wall)
    (P/"RESULT.json").write_text(json.dumps(output, indent=2)+"\n")

if (sum(remaining.values()) != 95 or min(remaining.values()) < 0
        or min(repeat_left.values()) < 0 or len(missing) > 190):
    output["stop_reason"] = "cheap degree or pair-count contradiction; MILP not called"
    save()
    raise SystemExit(0)

all_candidates = list(combinations(high, 5))
assert len(all_candidates) == 26334
# Every base-covered pair newly repeated spends one unit at each endpoint.
# This necessary row budget safely removes individual impossible extras.
candidates = [
    e for e in all_candidates
    if all(sum(pairs[tuple(sorted((v, w)))] > 0 for w in e if w != v)
           <= repeat_left[v] for v in e)
]
support = Counter(v for e in candidates for v in e)
pair_support = Counter(pair for e in candidates for pair in combinations(e, 2))
maps = [{v: i for i, q in enumerate(blocks) for v in q} for blocks in star]
coeff = [
    [sum(mp[v] == mp[w] for v, w in combinations(e, 2)) for mp in maps]
    for e in candidates
]
maxima = [max(c[i] for c in coeff) for i in range(3)]
upper_W = [base_W[i]+19*maxima[i] for i in range(3)]
cheap.update({
    "all_high_five_sets": len(all_candidates),
    "after_safe_row_prune": len(candidates),
    "unsupported_missing_pairs": [p for p in missing if pair_support[p] == 0],
    "insufficient_vertex_support": [v for v in high if support[v] < remaining[v]],
    "single_extra_W_max": maxima,
    "nineteen_extra_linear_W_upper": upper_W,
    "single_extra_sumW_max": max(map(sum, coeff)),
    "nineteen_extra_sumW_upper": sum(base_W)+19*max(map(sum, coeff)),
})
if (cheap["unsupported_missing_pairs"] or cheap["insufficient_vertex_support"]
        or min(upper_W) < 26):
    output["stop_reason"] = "cheap support or linear W upper contradiction; MILP not called"
    save()
    raise SystemExit(0)

# Exact remaining degree rows, exact extra count, missing pair coverage,
# three W thresholds, and necessary old-pair repetition budgets.
lo, hi = [19.0], [19.0]
degree_row = {}
for v in high:
    degree_row[v] = len(lo)
    lo.append(float(remaining[v])); hi.append(float(remaining[v]))
pair_row = {}
for pair in missing:
    pair_row[pair] = len(lo)
    lo.append(1.0); hi.append(np.inf)
W_row = []
for i in range(3):
    W_row.append(len(lo))
    lo.append(float(26-base_W[i])); hi.append(np.inf)
repeat_row = {}
for v in high:
    repeat_row[v] = len(lo)
    lo.append(0.0); hi.append(float(repeat_left[v]))

rr, cc, data = [], [], []
for j, e in enumerate(candidates):
    entries = {0: 1.0}
    for v in e:
        entries[degree_row[v]] = 1.0
        used = sum(pairs[tuple(sorted((v, w)))] > 0 for w in e if w != v)
        if used:
            entries[repeat_row[v]] = float(used)
    for pair in combinations(e, 2):
        if pair in pair_row:
            entries[pair_row[pair]] = 1.0
    for i in range(3):
        if coeff[j][i]:
            entries[W_row[i]] = float(coeff[j][i])
    for row, value in entries.items():
        rr.append(row); cc.append(j); data.append(value)
matrix = csc_matrix((data, (rr, cc)), shape=(len(lo), len(candidates)))
cheap["milp_rows"] = len(lo)
save()
with warnings.catch_warnings(record=True) as log:
    sol = milp(
        np.zeros(len(candidates)),
        integrality=np.ones(len(candidates), dtype=np.int32),
        bounds=Bounds(np.zeros(len(candidates)), np.ones(len(candidates))),
        constraints=LinearConstraint(matrix, np.asarray(lo), np.asarray(hi)),
        options={"time_limit": 30, "threads": 1, "presolve": True},
    )
output.update(numerical_status=int(sol.status),
              numerical_message=str(sol.message),
              solver_warnings=[str(w.message) for w in log])
if sol.x is not None:
    chosen = [i for i, x in enumerate(sol.x) if x > 0.5]
    assert len(chosen) == 19
    assert all(abs(float(x)-round(float(x))) < 1e-6 for x in sol.x)
    extras = [frozenset(candidates[i]) for i in chosen]
    edges = base+extras
    assert len(set(edges)) == 35
    actual_degree = Counter(v for e in edges for v in e)
    assert all(actual_degree[v] == target[v] for v in range(25))
    actual_pairs = Counter(pair for e in edges for pair in combinations(sorted(e), 2))
    assert len(actual_pairs) == 300
    W = {
        str(z): sum(sum(len(e&q)*(len(e&q)-1)//2 for q in blocks)
                    for e in edges if z not in e)
        for z, blocks in zip(low, star)
    }
    assert min(W.values()) >= 26
    output["witnesses"].append({
        "L": low, "edges": [sorted(e) for e in edges], "W": W,
        "sum_W": sum(W.values()), "degree": dict(actual_degree),
        "all_low_W_at_least_26": True, "strong_average_counterexample": True,
    })
    output["stop_reason"] = "actual H refutes both W criteria; not Property B"
else:
    output["stop_reason"] = "one authorized solver call returned no incumbent; no general conclusion"
save()
print(json.dumps({k: output[k] for k in (
    "numerical_status", "numerical_message", "stop_reason", "cpu_seconds", "wall_seconds"
)}))
