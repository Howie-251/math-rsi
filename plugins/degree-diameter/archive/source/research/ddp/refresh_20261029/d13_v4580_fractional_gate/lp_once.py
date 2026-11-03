#!/usr/bin/env python3
"""One fractional-cover diagnostic with exact integer certificate checks."""
import os
for name in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"]:
    os.environ[name] = "1"
import json
from pathlib import Path
import resource
import time
import warnings

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "d13_v4580_fourguard"
assert not (HERE / "RESULT.json").exists(), "fixed LP already recorded"
resource.setrlimit(resource.RLIMIT_CPU, (29, 30))
START = time.process_time()
WALL = time.monotonic()
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix

r = json.loads((SOURCE / "prepared.json").read_text())
K, N, W = len(r["representatives"]), len(r["missing"]), r["mask_words_per_row"]
raw = np.fromfile(SOURCE / "prepared.masks.u64.bin", dtype=np.uint8).reshape(K, W*8)
cover = np.unpackbits(raw, axis=1, bitorder="little")[:, :N]
A = csc_matrix(cover, dtype=np.float64)
A.indices = A.indices.astype(np.int32)
A.indptr = A.indptr.astype(np.int32)
(HERE / "HANDLE.json").write_text(json.dumps(dict(status="RUNNING", pid=os.getpid(), stage="ONE_FULL_DUAL_LP")) + "\n")
with warnings.catch_warnings(record=True) as notes:
    warnings.simplefilter("always")
    ans = linprog(-np.ones(N), A_ub=A, b_ub=np.ones(K), bounds=(0, None), method="highs",
                  options={"time_limit":20.0, "threads":1, "presolve":True})
out = dict(status="NUMERICAL_LP_RETURNED", scipy_status=int(ans.status), message=str(ans.message),
           target_rows=N, guard_columns=K, matrix_nnz=int(A.nnz), LP_calls=1,
           new_SAT_calls=0, new_BFS=0, new_graphs=0,
           warnings=[str(note.message) for note in notes])
if ans.x is not None:
    # These integer dot products are independent of numerical LP feasibility.
    q = np.floor(np.maximum(ans.x, 0) * 1_000_000).astype(np.int64)
    nz = np.flatnonzero(q)
    loads = cover[:, nz] @ q[nz]
    total, maximum = int(q.sum()), int(loads.max())
    assert total < 2**62 and maximum < 2**62
    (HERE / "DUAL_INTEGER_WEIGHTS.json").write_text(json.dumps(dict(targets=r["missing"], weights=q.tolist(),
                     total_weight=total, maximum_guard_load=maximum), separators=(",", ":")) + "\n")
    out.update(numerical_optimum=None if ans.fun is None else float(-ans.fun),
               exact_dual_total_weight=total, exact_dual_maximum_guard_load=maximum,
               exact_guard_budget4_excluded=maximum > 0 and total > 4*maximum)
    marginals = getattr(getattr(ans, "ineqlin", None), "marginals", None)
    if marginals is not None:
        p = np.ceil(np.maximum(-np.asarray(marginals), 0) * 1_000_000).astype(np.int64)
        nzp = np.flatnonzero(p)
        target_load = cover[nzp, :].T @ p[nzp]
        minimum, primal_total = int(target_load.min()), int(p.sum())
        (HERE / "PRIMAL_INTEGER_WEIGHTS.json").write_text(json.dumps(dict(guards=r["representatives"],
                     weights=p.tolist(), total_weight=primal_total, minimum_target_load=minimum),
                     separators=(",", ":")) + "\n")
        out.update(exact_primal_total_weight=primal_total, exact_primal_minimum_target_load=minimum,
                   exact_fractional_cover_budget4_feasible=minimum > 0 and primal_total <= 4*minimum)
    if out["exact_guard_budget4_excluded"]:
        out["status"] = "EXACT_INTEGER_DUAL_EXCLUDES_FOUR_GUARDS"
    elif out.get("exact_fractional_cover_budget4_feasible"):
        out["status"] = "EXACT_FRACTIONAL_BUDGET4_FEASIBLE_INTEGER_UNRESOLVED"
    else:
        out["status"] = "LP_RETURN_WITHOUT_DECISIVE_EXACT_BUDGET4_CERTIFICATE"
else:
    out["status"] = "LP_UNKNOWN_NO_CERTIFICATE"
out.update(worker_CPU_seconds=time.process_time()-START, wall_seconds=time.monotonic()-WALL)
(HERE / "RESULT.json").write_text(json.dumps(out, indent=2) + "\n")
(HERE / "HANDLE.json").write_text(json.dumps(dict(status="TERMINAL", pid=os.getpid(), result="RESULT.json")) + "\n")
print(json.dumps(out), flush=True)
