"""A fixed actual24-point35-edge pair-covering H and a targeted blocking color.
This is a colorability/initial-state witness search on one H, not H enumeration.
No non-B or edge-critical counterexample is claimed.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time,random
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
P=Path(__file__).resolve().parent;st=time.perf_counter();rng=random.Random(73027)
lines=[]
for c in range(5):lines.append(tuple(5*c+y for y in range(5)))
for a in range(5):
 for b in range(5):lines.append(tuple(sorted(5*x+(a*x+b)%5 for x in range(5))))
blocks=sorted(tuple(v for v in e if v!=24) for e in lines if 24 in e);base=[e for e in lines if 24 not in e];pads=[blocks[(i+1)%6][0] for i in range(6)];aug=[tuple(sorted(set(B)|{q})) for B,q in zip(blocks,pads)];assert all(len(e)==5 for e in aug)
nonpad=[v for v in range(24) if v not in pads];rng.shuffle(nonpad);G=tuple(sorted(nonpad[:5]));others=[v for v in range(24) if v not in G];rng.shuffle(others);extra=[G]+[tuple(sorted(others[5*j:5*j+5])) for j in range(3)]+[tuple(sorted(others[15:]+[nonpad[5]]))];assert all(len(e)==5 for e in extra)
H=sorted(set(base+aug+extra));assert len(H)==35 and len(set(H))==35
ds=[sum(v in e for e in H) for v in range(24)];assert min(ds)==7 and all(ds[g]==7 for g in G)
assert all(sum(a in e and b in e for e in H)>=1 for a,b in combinations(range(24),2))
attempts=[];found=None
for g in G:
 for E in H:
  if set(E)&set(G)!={g}:continue
  A=set(E)-{g};candidates={x:[f for f in H if g not in f and x in f and not ((set(f)-{x})&A)] for x in A}
  if any(not fs for fs in candidates.values()):continue
  ys=[(x,f) for x,fs in candidates.items() for f in fs];nvar=24+len(ys);rows=[];lo=[];hi=[]
  def add(dic,l=-np.inf,u=np.inf):rows.append(dic);lo.append(l);hi.append(u)
  for f in H:
   if f!=G:add({v:1 for v in f},1,4)
  for x in A:add({24+j:1 for j,(xx,f) in enumerate(ys) if xx==x},1)
  for j,(x,f) in enumerate(ys):
   for v in f:
    if v!=x:add({24+j:1,v:-1},u=0)
  mat=lil_matrix((len(rows),nvar),dtype=float)
  for i,rr in enumerate(rows):
   for j,v in rr.items():mat[i,j]=v
  lb=np.zeros(nvar);ub=np.ones(nvar)
  for v in G:lb[v]=1
  for v in A:ub[v]=0
  res=milp(np.zeros(nvar),integrality=np.ones(nvar),bounds=Bounds(lb,ub),constraints=LinearConstraint(mat.tocsr(),lo,hi),options={'time_limit':4.0});attempts.append(dict(g=g,E=E,status=int(res.status),message=res.message))
  if res.x is None:continue
  red={v for v in range(24) if res.x[v]>.5};assert set(G)<=red and not A&red;assert all(0<len(set(f)&red)<5 for f in H if f!=G);assert all(any(g not in f and set(f)-red=={x} for f in H) for x in A)
  found=dict(g=g,E=E,positive_A=sorted(A),initial_red=sorted(red),singleton_blockers={str(x):next(f for f in H if g not in f and set(f)-red=={x}) for x in A});break
 if found is not None or time.perf_counter()-st>35:break
out=dict(scope=__doc__,actual_H=dict(points=list(range(24)),edges=H,degrees=ds,G=G,deleted_point=24,star_blocks=blocks,pads=pads,extra_edges=extra),attempts=attempts,found=found,elapsed_seconds=time.perf_counter()-st)
(P/'CRITICAL_SMALL_BLOCKERS_PILOT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['found','attempts','elapsed_seconds']},indent=2))
