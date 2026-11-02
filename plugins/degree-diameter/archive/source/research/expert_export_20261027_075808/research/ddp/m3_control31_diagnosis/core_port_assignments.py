"""Finite joint repair: all 113400 assignments of ten fixed external endpoints.

Only attachments to ports 0,1,18,19,24 of the seven-vertex triangle-chain
block may change. Internal edges and every other external edge remain fixed.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
import numpy as np

HERE=Path(__file__).resolve().parent


def main():
    started=time.process_time();source=HERE.parent/'second_mechanism/control_unrestricted_n31.edges'
    rows=[tuple(map(int,l.split())) for l in source.read_text().splitlines()];n,m=rows[0]
    A=np.zeros((n,n),dtype=np.int64)
    for u,v in rows[1:]:A[u,v]=A[v,u]=1
    core={0,1,11,18,19,24,30};ports=[0,1,18,19,24]
    targets=sorted(v for u in ports for v in np.flatnonzero(A[u]).tolist() if v not in core)
    assert len(targets)==len(set(targets))==10
    base=A.copy()
    for u in ports:
        for v in targets:base[u,v]=base[v,u]=0
    hist=Counter();count=0;best=n*n;best_count=0;best_assignments=[];bestB=None;timed_out=False
    def evaluate(assignment):
        nonlocal count,best,best_count,best_assignments,bestB,timed_out
        if count%1000==0 and time.process_time()-started>20:
            timed_out=True;return
        B=base.copy()
        for u,neighbors in zip(ports,assignment):
            for v in neighbors:B[u,v]=B[v,u]=1
        B3=(B@B)@B;zero=int(np.count_nonzero(B3==0));count+=1;hist[zero]+=1
        if zero<best:
            best=zero;best_count=1;best_assignments=[assignment];bestB=B.copy()
        elif zero==best:
            best_count+=1
            if len(best_assignments)<32:best_assignments.append(assignment)
    def visit(remaining,assignment):
        if timed_out:return
        if len(remaining)==2:
            evaluate(assignment+[list(remaining)]);return
        for pair in combinations(remaining,2):
            rest=tuple(v for v in remaining if v not in pair)
            visit(rest,assignment+[list(pair)])
            if timed_out:return
    visit(tuple(targets),[])
    result=dict(scope='only the ten attachments at the seven-vertex triangle-chain block; all other edges fixed',
                planned_assignments=113400,evaluated=count,complete=count==113400,timed_out=timed_out,
                ports=ports,external_targets=targets,best_zero_count=best,best_count=best_count,
                best_assignments_first32=best_assignments,zero_count_hist=dict(hist),
                best_zero_pairs=np.argwhere((bestB@bestB)@bestB==0).tolist(),
                cpu_seconds=time.process_time()-started)
    (HERE/'core_port_assignments.json').write_text(json.dumps(result,indent=2)+'\n')
    newedges=[(u,v) for u in range(n) for v in range(u+1,n) if bestB[u,v]]
    assert len(newedges)==62 and np.all(bestB.sum(axis=1)==4)
    (HERE/'core_port_best.edges').write_text(f'{n} {len(newedges)}\n'+''.join(f'{u} {v}\n' for u,v in newedges))
    print(json.dumps({k:v for k,v in result.items() if k not in ('best_assignments_first32','zero_count_hist','best_zero_pairs')},indent=2))


if __name__=='__main__':main()
