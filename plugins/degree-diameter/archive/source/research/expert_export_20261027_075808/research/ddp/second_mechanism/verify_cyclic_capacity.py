"""Independent enumeration of the cyclic controller capacity obstruction.

Uses integer walk convolution (no edge-history/rank routine, numpy, or prime
normalization), and reads expected minima only after finishing each modulus.
"""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json,time

HERE=Path(__file__).resolve().parent


def score(m,a,b,c,d):
    adj=[[(1,0),(1,a),(2,0),(2,b)],
         [(0,0),(0,-a),(2,c),(2,d)],
         [(0,0),(0,-b),(1,-c),(1,-d)]]
    deficit=0
    for source in range(3):
        W=[{(source,0):1}]
        for _ in range(3):
            nxt=defaultdict(int)
            for (i,z),count in W[-1].items():
                for j,delta in adj[i]:nxt[j,(z+delta)%m]+=count
            W.append(nxt)
        for i in range(3):
            for z in range(m):
                key=(i,z)
                cap=27*W[3].get(key,0)+9*W[2].get(key,0)-129*W[1].get(key,0)-23*W[0].get(key,0)
                deficit+=max(0,27-cap)
    return deficit


def main():
    observed=[]
    for m in range(10,18):
        start=time.monotonic();total=passing=0;best=10**9;arg=None
        for a in range(1,m):
            for b in range(1,m):
                for c,d in combinations(range(m),2):
                    s=score(m,a,b,c,d);total+=1
                    if s==0:passing+=1
                    if s<best:best=s;arg=[a,b,c,d]
        expected=next(r for r in json.loads((HERE/'cyclic_capacity_results.json').read_text()) if r['m']==m)
        assert best==expected['min_optimistic_missing']
        assert (passing==0)==(expected['passing']==0)
        r=dict(m=m,full_enumerated=total,passing=passing,min_optimistic_missing=best,
               first_best_parameters=arg,agrees_with_primary=True,seconds=time.monotonic()-start)
        observed.append(r);print(json.dumps(r),flush=True)
        (HERE/'cyclic_capacity_independent.json').write_text(json.dumps(observed,indent=2)+'\n')


if __name__=='__main__':main()
