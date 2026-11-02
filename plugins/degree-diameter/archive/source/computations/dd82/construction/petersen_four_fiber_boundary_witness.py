"""Read-only actual-row witnesses for the boundary rigidity proof.

No candidate search, SAT call, graph optimization, or BFS replay.
"""
from pathlib import Path
import json
import time

from hs_augmentation import dump
from petersen_four_fiber_reassembly import OUT, SOURCE, RELEASED, adjacency, matching


start = time.process_time()
original = {tuple(e) for e in json.loads(SOURCE.read_text())["edges"]}
ns = adjacency(original)
fixed = {e for e in original if (e[0]//10,e[1]//10) not in RELEASED}
fixed_ns = adjacency(fixed)
f = {(i,j):matching(ns,i,j) for i in range(6) for j in range(6) if i != j}
signatures = {i:{v:(f[i,2][v-10*i], f[i,3][v-10*i])
                 for v in range(10*i,10*i+10)} for i in (1,4,5)}
sigma = set(signatures[1].values())
pi = set(signatures[4].values())
assert pi == set(signatures[5].values())
assert sigma.isdisjoint(pi)
assert all(len({p[c] for p in curve}) == 10 for curve in (pi,sigma) for c in (0,1))
rows = []
for u in range(10):
    p = signatures[4][f[0,4][u]]
    q = signatures[1][f[0,1][u]]
    assert all(p[c] != q[c] for c in (0,1))
    fixed_routes = {}
    missing = {}
    for j in (2,3):
        counts = {v:int(v in fixed_ns[u]) + len(fixed_ns[u]&fixed_ns[v])
                  for v in range(10*j,10*j+10)}
        assert sorted(counts.values()) == [0,0,1,1,1,1,1,1,1,1]
        fixed_routes[str(j)] = counts
        missing[str(j)] = sorted(v for v,c in counts.items() if c == 0)
        assert missing[str(j)] == sorted([p[j-2],q[j-2]])
    rows.append(dict(source=u, original_core_neighbor=f[0,1][u],
                     original_twin_neighbor=f[0,4][u],
                     twin_signature=p, core_signature=q,
                     fixed_route_counts=fixed_routes, missing_boundary_targets=missing))
result = dict(source=str(SOURCE), fixed_interfaces=sorted({(e[0]//10,e[1]//10) for e in fixed if e[0]//10!=e[1]//10}),
              sigma_fiber1=sorted(sigma), pi_fibers4_and5=sorted(pi),
              signature_curves_disjoint=True, all_rows_have_eight_distinct_fixed_routes=True,
              rows=rows, cpu_seconds=time.process_time()-start,
              scope="Actual boundary-data check only; the implication forcing M01 is proved in the mathematical note.")
dump(OUT/"boundary_rigidity.json",result)
print(json.dumps({k:v for k,v in result.items() if k not in ("rows","sigma_fiber1","pi_fibers4_and5")}))
