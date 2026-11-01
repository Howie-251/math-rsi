"""Finite exact probability table for group-symmetric coloring distributions.
LP is diagnostic only. All coloring probabilities and adversarial count vertices
are rational and saved; a failed union bound is not an actual hypergraph.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations_with_replacement,permutations,combinations
from math import comb
import time,json
import numpy as np
from scipy.optimize import linprog
P=Path(__file__).resolve().parent
start=time.perf_counter()
parts=[(1,1,1,1,1),(2,1,1,1,0),(2,2,1,0,0),(3,1,1,0,0),(3,2,0,0,0),(4,1,0,0,0),(5,0,0,0,0)]
qs=[sum(comb(x,2) for x in t) for t in parts]
colorings=list(combinations_with_replacement(range(6),5))
probs=[]
for reds in colorings:
    perms=list(set(permutations(reds)));prow=[]
    for part in parts:
        z=Q()
        for r in perms:
            red=blue=Q(1)
            for a,b in zip(r,part):
                red*=Q(comb(a,b) if a>=b else 0,comb(5,b))
                blue*=Q(comb(5-a,b) if 5-a>=b else 0,comb(5,b))
            z+=red+blue
        prow.append(z/len(perms))
    probs.append(prow)
# Count vertices: n>=0, total35, pair excess100, full-group edges<=5.
vertices=set()
for active_full in (False,True):
    # Equality constraints rank2, or3 with n6=5. Basic points support<=rank.
    if not active_full:
        for i,j in combinations(range(7),2):
            if qs[i]==qs[j]:continue
            ni=Q(35*qs[j]-100,qs[j]-qs[i]);nj=35-ni
            n=[Q()]*7;n[i]=ni;n[j]=nj
            if min(n)>=0 and n[6]<=5:vertices.add(tuple(n))
    else:
        for i,j in combinations(range(6),2):
            if qs[i]==qs[j]:continue
            ni=Q(30*qs[j]-50,qs[j]-qs[i]);nj=30-ni
            n=[Q()]*7;n[i]=ni;n[j]=nj;n[6]=Q(5)
            if min(n)>=0:vertices.add(tuple(n))
vertices=sorted(vertices)
mat=np.array([[float(sum(p*n for p,n in zip(row,v))) for row in probs] for v in vertices])
# prob mixture (252 variables) and bound z.
a=np.column_stack([mat,-np.ones(len(vertices))])
res=linprog([0]*len(colorings)+[1],A_ub=a,b_ub=np.zeros(len(vertices)),A_eq=[[1]*len(colorings)+[0]],b_eq=[1],bounds=[(0,None)]*len(colorings)+[(None,None)],method='highs')
active=[]
if res.success:
    for i,w in enumerate(res.x[:-1]):
        if w>1e-8:active.append(dict(red_counts=colorings[i],lp_weight=float(w),rational_near=str(Q(float(w)).limit_denominator(100000)),probabilities=[str(x) for x in probs[i]]))
    adversarial=[dict(counts=[str(x) for x in vertices[i]],value=float(mat[i]@res.x[:-1])) for i in range(len(vertices)) if abs(mat[i]@res.x[:-1]-res.fun)<1e-7]
else:adversarial=[]
exact_certificate=None
if res.success:
    weights=[Q(float(x)).limit_denominator(1000000) for x in res.x[:-1]]
    dualweights=[Q(float(-x)).limit_denominator(1000000) for x in res.ineqlin.marginals]
    target=Q(27,23)
    assert sum(weights)==sum(dualweights)==1
    pp=[sum(w*row[j] for w,row in zip(weights,probs)) for j in range(7)]
    moment=[sum(w*v[j] for w,v in zip(dualweights,vertices)) for j in range(7)]
    assert all(sum(p*n for p,n in zip(pp,v))<=target for v in vertices)
    assert all(sum(p*n for p,n in zip(row,moment))>=target for row in probs)
    exact_certificate=dict(value=str(target),mixture_probabilities=[str(x) for x in pp],
      abstract_adversarial_counts=[str(x) for x in moment],
      lower_bound_minimum_over_252_colorings=str(min(sum(p*n for p,n in zip(row,moment)) for row in probs)),
      all_18_moment_vertices_primal_verified=True,all_252_coloring_orbits_dual_verified=True)
# Independent balanced group 2/3 probability formula, not a full-coloring LP claim.
pbal=[Q(1,16),Q(1,20),Q(1,25),Q(1,40),Q(1,50),Q(),Q()]
out=dict(scope=__doc__,edge_group_partitions=parts,pair_counts=qs,coloring_orbits=len(colorings),moment_vertices=len(vertices),exact_certificate=exact_certificate,lp_success=res.success,lp_optimum=float(res.fun) if res.success else None,active_coloring_orbits=active,active_adversarial_moments=adversarial,balanced_group_probabilities=[str(x) for x in pbal],all_vertices=[[str(x) for x in v] for v in vertices],elapsed_seconds=time.perf_counter()-start)
(P/'GROUP_BALANCE_PILOT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
