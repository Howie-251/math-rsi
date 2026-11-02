#!/usr/bin/env python3
"""Exhaust the extra translation structure found in the saved candidate.
Parameters d,b0,b1,c0,c1 range over F5 (3125 assignments). This is a strict
subfamily of the three-S10 construction, not a second randomized search.
Independent set-based coverage equations, no C++ score implementation imported.
"""
from collections import Counter
from itertools import product
import json
from pathlib import Path
from time import process_time

HERE=Path(__file__).resolve().parent
P=[{(i+1)%5,(i-1)%5,i+5} for i in range(5)]+[{5+(i+2)%5,5+(i-2)%5,i} for i in range(5)]
R=[(i+1)%5 for i in range(5)]+[5+(i+1)%5 for i in range(5)]
def inv(p):return [p.index(i) for i in range(10)]
def compose(p,q):return [p[q[i]] for i in range(10)]
def flip_translate(s,t):return [5+(x+s)%5 for x in range(5)]+[(x+t)%5 for x in range(5)]
def score(d,b0,b1,c0,c1):
    A=[5+(-x)%5 for x in range(5)]+[(-x+d)%5 for x in range(5)]
    B=flip_translate(b0,b1);C=flip_translate(c0,c1)
    Ai,Bi,Ci,Ri=map(inv,(A,B,C,R))
    routes=[(A,[compose(B,compose(A,R)),compose(Bi,compose(A,Ri)),compose(C,compose(A,compose(R,R))),compose(Ci,compose(A,compose(Ri,Ri)))]),
            (B,[compose(A,compose(Ri,Ai)),compose(Bi,C),compose(Ci,Ci),compose(C,Bi)]),
            (C,[compose(A,compose(Ri,compose(Ri,Ai))),compose(B,B),compose(Bi,Ci),compose(Ci,Bi)])]
    # Extra coordinate translations preserve all three representative fiber-pair
    # relations. Each of the two source layers has five equivalent vertices.
    missing=0
    for M,via in routes:
        for u in (0,5):
            covered={M[u]} | P[M[u]] | {M[v] for v in P[u]} | {f[u] for f in via}
            missing+=10-len(covered)
    return 25*missing # 5 source-coordinate translates * 5 fiber translates.

def main():
    t=process_time();hist=Counter();best=1500;best_parameters=[]
    for params in product(range(5),repeat=5):
        e=score(*params);hist[e]+=1
        if e<best:best=e;best_parameters=[list(params)]
        elif e==best:best_parameters.append(list(params))
    original=[3,2,3,1,3]
    assert score(*original)==50
    result={'scope':'A swaps layers with reflection; B,C swap layers with translations; A first offset normalized to zero',
            'parameter_order':['d','b0','b1','c0','c1'],'parameter_domain':list(range(5)),
            'assignments':sum(hist.values()),'complete_for_stated_subfamily':True,
            'minimum_uncovered_pairs':best,'uncovered_pair_count_histogram':dict(sorted(hist.items())),
            'all_minimizing_parameters':best_parameters,'saved_search_candidate_parameters':original,
            'cpu_seconds':process_time()-t}
    out=HERE/'petersen_six_fibers_translation.json';out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='all_minimizing_parameters'},indent=2))
    print('number of minimizers:',len(best_parameters))
if __name__=='__main__':main()
