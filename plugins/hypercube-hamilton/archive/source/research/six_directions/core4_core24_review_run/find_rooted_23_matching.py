"""Search for a 23-edge matching maximal in Q6 minus root 0. No UNSAT claim."""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csc_matrix

ROOT = Path(__file__).resolve().parent
es = [(a, a ^ (1 << j)) for a in range(1, 64) for j in range(6)
      if a < (a ^ (1 << j)) and (a ^ (1 << j)) != 0]
degree = np.array([[int(v in e) for e in es] for v in range(1, 64)])
dominated = np.array([[int(bool(set(e) & set(f))) for f in es] for e in es])
rows = np.vstack([degree, dominated, np.ones((1, len(es)))])
lo = np.r_[np.zeros(63), np.ones(len(es)), 23]
hi = np.r_[np.ones(63), np.full(len(es), np.inf), 23]
r = milp(np.zeros(len(es)), integrality=np.ones(len(es)),
         bounds=Bounds(np.zeros(len(es)), np.ones(len(es))),
         constraints=LinearConstraint(csc_matrix(rows), lo, hi),
         options={'time_limit': 45})
out = dict(scope='One feasibility search for rooted maximal cardinality 23',
           solver_status=int(r.status), solver_message=str(r.message),
           status='UNKNOWN', full_p6_proved=False)
if r.x is not None and max(abs(r.x-np.round(r.x))) < 1e-6:
    x = np.round(r.x).astype(int)
    if np.all(rows @ x >= lo) and np.all(rows @ x <= hi):
        m = [e for e, use in zip(es, x) if use]
        out.update(status='FOUND', matching=m, u=0,
                   holes=sorted(set(range(64))-{q for e in m for q in e}))
(ROOT/'rooted_23_matching.json').write_text(json.dumps(out, indent=2), encoding='utf8')
print(json.dumps(out, indent=2))
