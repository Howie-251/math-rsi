#!/usr/bin/env python3
"""Exact short-cycle energy from expanded six-Petersen-fiber edge lists."""
import itertools
import json
import math
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).parent
INPUTS=[ROOT/"petersen_six_fibers.best.edges",
        ROOT/"petersen_all_matchings_run/snapshot20.json",
        ROOT/"petersen_all_matchings_run/candidate.best.edges"]


def check(path):
    if path.suffix==".json":
        obj=json.loads(path.read_text());n=obj["n"];edges=obj["edges"]
    else:
        rows=[list(map(int,line.split())) for line in path.read_text().splitlines() if line.strip()]
        n,m=rows[0];edges=rows[1:];assert len(edges)==m
    assert n==60 and len(edges)==240
    ns=[set() for _ in range(n)]
    for u,v in edges:ns[u].add(v);ns[v].add(u)
    assert all(len(s)==8 for s in ns)
    assert all([sum(v//10==j for v in ns[u]) for j in range(6)]==
               [3 if j==u//10 else 1 for j in range(6)] for u in range(n))
    common=[[len(ns[u]&ns[v]) for v in range(n)] for u in range(n)]
    b=[[0 if u==v else common[u][v]+int(v in ns[u])-1 for v in range(n)] for u in range(n)]
    assert all(b[u][v]==0 for u in range(n) for v in range(n) if u//10==v//10)
    assert all(sum(b[u][10*j:10*j+10])==(u//10!=j) for u in range(n) for j in range(6))
    triangle_incidence=sum(common[u][v] for u,v in edges)
    opposite_incidence=sum(math.comb(common[u][v],2) for u in range(n) for v in range(u+1,n))
    assert triangle_incidence%3==0 and opposite_incidence%2==0
    triangles=triangle_incidence//3;four_cycles=opposite_incidence//2
    bad=sum(b[u][v]==-1 for u in range(n) for v in range(u+1,n))
    crowded=sum(math.comb(b[u][v],2) for u in range(n) for v in range(u+1,n) if b[u][v]>=2)
    energy=2*four_cycles+3*triangles-150
    trace_b2=sum(x*x for row in b for x in row)
    assert energy==bad+crowded==(trace_b2-300)//4
    local=[(sum(x*x for x in row)-5)//2 for row in b]
    assert min(local)>=0 and sum(local)==2*energy
    q=0
    for i in range(6):
        for j in range(i+1,6):
            matching={u:next(v for v in ns[u] if v//10==j) for u in range(10*i,10*i+10)}
            for u in range(10*i,10*i+10):
                for v in ns[u]:
                    if u<v and v//10==i and matching[v] in ns[matching[u]]:q+=1
    return dict(file=str(path.relative_to(ROOT)),n=n,triangles=triangles,four_cycles=four_cycles,
                cycle_energy=energy,bad_pairs=bad,crowding_penalty=crowded,trace_B_squared=trace_b2,
                pair_matching_overlap_sum=q,local_energy_histogram=dict(Counter(local)),
                defect_entry_histogram=dict(Counter(b[u][v] for u in range(n) for v in range(u+1,n))))


if __name__=="__main__":
    result=[check(p) for p in INPUTS]
    Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))
