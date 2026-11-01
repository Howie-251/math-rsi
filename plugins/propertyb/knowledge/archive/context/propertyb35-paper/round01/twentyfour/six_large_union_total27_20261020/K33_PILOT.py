"""One fixed six-positive-set family; bounded signed-counterexample feasibility.
Not a classification, no original H or exterior-layout enumeration.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json,time
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import csc_matrix
P=Path(__file__).resolve().parent;start=time.process_time()
edges=[(i,j) for i in range(3) for j in range(3,6)]
A=[{k for k,e in enumerate(edges) if i in e}|{9+i} for i in range(6)]
U=sorted(set.union(*A));N=len(U)
minimal=[]
for k in range(1,7):
 for T in combinations(U,k):
  R=set(T)
  if all(R&B for B in A) and all(any(R&B=={x} for B in A) for x in R):minimal.append(frozenset(R))
neg=[frozenset(T) for k in (3,4) for T in combinations(U,k) if any(set(T)<=R for R in minimal)]
n=len(neg);row=[];col=[];val=[];lo=[];hi=[]
for R in minimal:
 q=len(lo);lo.append(1);hi.append(np.inf)
 for j,B in enumerate(neg):
  if B<=R:row.append(q);col.append(j);val.append(1)
for k,cap in [(3,15),(4,12)]:
 q=len(lo);lo.append(-np.inf);hi.append(cap)
 for j,B in enumerate(neg):
  if len(B)==k:row.append(q);col.append(j);val.append(1)
for v in U:
 q=len(lo);lo.append(-np.inf);hi.append(7-sum(v in B for B in A))
 for j,B in enumerate(neg):
  if v in B:row.append(q);col.append(j);val.append(1)
M=csc_matrix((val,(row,col)),shape=(len(lo),n),dtype=float)
r=milp(np.zeros(n),integrality=np.ones(n),bounds=Bounds(np.zeros(n),np.ones(n)),constraints=LinearConstraint(M,lo,hi),options={'time_limit':8,'mip_rel_gap':0})
out={'scope':__doc__,'positive':[sorted(B) for B in A],'union':N,'positive_graph_edges':edges,'all_minimal_transversals':len(minimal),'minimal_size_counts':{k:sum(len(R)==k for R in minimal) for k in range(1,7)},'negative_variables':n,'solver_status':int(r.status),'solver_message':r.message,'cpu_seconds':time.process_time()-start}
if r.x is not None and all(abs(x-round(x))<1e-6 for x in r.x):
 chosen=[B for B,x in zip(neg,r.x) if round(x)]
 assert sum(len(B)==3 for B in chosen)<=15 and sum(len(B)==4 for B in chosen)<=12
 assert all(sum(v in B for B in A)+sum(v in B for B in chosen)<=7 for v in U)
 assert all(any(B<=R for B in chosen) for R in minimal)
 out.update({'status':'EXACT_SIGNED_COUNTEREXAMPLE','negative':[sorted(B) for B in chosen],'negative_size_counts':{k:sum(len(B)==k for B in chosen) for k in (3,4)},'all_minimal_transversals_exactly_blocked':True})
else:out['status']='NO_VERIFIED_COUNTEREXAMPLE_WITHIN_BOUND'
(P/'K33_PILOT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
