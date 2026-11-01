"""Root's exact interface arithmetic. Imports frozen M,J,K; does not reprove their domain."""
from itertools import product
from pathlib import Path
import json
import time

base = Path(__file__).resolve().parent
start = time.process_time()
rows = json.loads((base / "marked_partition/RESULT.json").read_text())["matrices"]
N = 184756
worst = (-1, None)
calls = 0
for row in rows:
    J, K = row["J"], row["maxK"]
    e = 660 - K
    assert 330 <= e <= 660 and J - 15 * K >= 324
    for alpha in range(20):
        for D in range(12, 42):
            q, k, ell = D - 5 * alpha, D - 2 - 2 * alpha, 21 - D + alpha
            if k < 0 or ell < 0 or q > 17:
                continue
            assert alpha + k + ell == 19
            raw = 3 * 16980 + 8008 * k + 6006 * ell
            assert raw == 161050 + 2002 * q
            bound = raw - J - 400 - k * e
            assert bound < N
            calls += 1
            if bound > worst[0]:
                worst = (bound, {"matrix": row["id"], "D": D, "alpha": alpha,
                                 "q": q, "k": k, "ell": ell})
assert worst[0] == 184460
star_types = {}
for r in range(9, 26):
    allowed = []
    for a in product(range(7), repeat=4):
        a1, a2, a3, a4 = a
        if sum(a) == 6 and a3 + 2*a4 - a1 == r-7 and 4*a3 + 5*a4 <= r:
            allowed.append(a)
    star_types[str(r)] = allowed
assert star_types["9"] == [(0, 4, 2, 0), (0, 5, 0, 1), (1, 3, 1, 1)]
assert star_types["10"] == [(0, 4, 1, 1), (1, 3, 0, 2)]
assert star_types["11"] == [(0, 4, 0, 2)]
assert all(not star_types[str(r)] for r in range(12, 26))
out = {"status": "PASS", "scope": "exact scalar interface, imported full local matrix data",
       "matrices": len(rows), "feasible_D_alpha_calls": calls,
       "maximum_bound": worst[0], "strict_margin": N-worst[0], "witness": worst[1],
       "star_types": star_types, "cpu_seconds": time.process_time()-start,
       "new_original_hypergraphs_enumerated": 0}
(base / "ROOT_SCALAR_CHECK.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({k: v for k, v in out.items() if k != "star_types"}, indent=2))
