"""Actual constant-route witnesses forcing five neighbors inside fiber 0."""
from pathlib import Path
import json
import time

from hs_augmentation import dump
from petersen_four_fiber_reassembly import adjacency, matching

HERE=Path(__file__).resolve().parent
OUT=HERE/"petersen_internal_reassembly_run"
SOURCE=HERE/"petersen_four_fiber_reassembly_run/seed.json"
start=time.process_time()
edges={tuple(e) for e in json.loads(SOURCE.read_text())["edges"]}
ns=adjacency(edges)
f={(i,j):matching(ns,i,j) for i in range(6) for j in range(6) if i!=j}
rows=[]
for u in (0,1):
    required=set()
    blocks=[]
    for j in (2,3):
        direct=f[0,j][u]
        internal_target=sorted(v for v in ns[direct] if v//10==j)
        exterior={k:f[k,j][f[0,k][u]-10*k] for k in range(1,6) if k!=j}
        reached={direct,*internal_target,*exterior.values()}
        missing=sorted(set(range(10*j,10*j+10))-reached)
        needed=[w for w in range(10) if f[0,j][w] in missing]
        required.update(needed)
        blocks.append(dict(target_fiber=j,direct=direct,
                           routes_using_target_internal_edge=internal_target,
                           routes_through_other_fibers=exterior,
                           missing_targets=missing,required_internal_neighbors=needed))
    assert len(required)==5
    rows.append(dict(source=u,blocks=blocks,required_internal_neighbors=sorted(required),
                     required_degree=len(required),available_internal_degree=3))
report=dict(source=str(SOURCE),rows=rows,cpu_seconds=time.process_time()-start,
            conclusion="No cubic internal graph in fiber0 can cover both boundary fibers with these fixed external matchings and P2/P3, regardless of internal graphs in fibers1,4,5.",
            scope="Read-only route witness; no enumeration, solver, or BFS replay")
dump(OUT/"required_neighbor_obstruction.json",report)
print(json.dumps(report))
