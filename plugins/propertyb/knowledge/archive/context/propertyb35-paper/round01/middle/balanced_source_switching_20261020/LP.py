import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
import json,time
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix
P=Path(__file__).resolve().parent
rows=[tuple(map(int,x.split())) for x in (P/'WEIGHTS.tsv').read_text().splitlines()]
sets=[tuple(i for i in range(20) if m>>i&1) for m,w in rows];weights=[w for m,w in rows]
links=[{0,1,2,6},{3,4,7,10},{5,8,11,12},{6,7,13,14},{8,9,15,16},{9,17,18,19}]
pairs=list(combinations(range(20),2));pi={q:i for i,q in enumerate(pairs)}
r=[];c=[];v=[];rr=[];cc=[];vv=[]
for j,q in enumerate(sets):
 for a in (20,*q):r.append(a);c.append(j);v.append(1)
 for ab in combinations(q,2):rr.append(pi[ab]);cc.append(j);vv.append(-1)
eq=csc_matrix((v,(r,c)),shape=(21,len(rows)))
ub=csc_matrix((vv,(rr,cc)),shape=(190,len(rows)))
deg=[7]*5+[6]+[6]*4+[8]*10
rhs=[-int(not any(set(q)<=l for l in links)) for q in pairs]
st=time.process_time();sol=linprog(-np.array(weights,dtype=float),A_ub=ub,b_ub=rhs,A_eq=eq,b_eq=deg+[29],bounds=(0,1),method='highs')
out={'scope':'one fixed six-link A1 star; fractional Hbar edge inventory with exact degrees, 29 edges, simple upper bounds and actual residual paircover','status':sol.message,'cpu_seconds':time.process_time()-st,'C_count':167174}
if sol.success:
 out.update(objective_float=-sol.fun,margin_float=167174+sol.fun,nonzero_variables=int(sum(sol.x>1e-8)))
 # Preserve a rational feasible witness only if all exact constraints survive rationalization.
 z=[F(float(x)).limit_denominator(1000000) for x in sol.x];bad=[]
 if sum(z)!=29:bad.append('total')
 for a in range(20):
  if sum(z[j] for j,q in enumerate(sets) if a in q)!=deg[a]:bad.append('degree'+str(a))
 for a,b in pairs:
  if not any({a,b}<=l for l in links) and sum(z[j] for j,q in enumerate(sets) if a in q and b in q)<1:bad.append('pair'+str((a,b)))
 if any(x<0 or x>1 for x in z):bad.append('simplecap')
 val=sum(x*w for x,w in zip(z,weights));out.update(rational_witness_exact_constraints=not bad,rational_failures=bad,rational_objective=str(val))
 if not bad:out['rational_witness']=[{'edge':q,'multiplicity':str(x),'weight':w} for q,x,w in zip(sets,z,weights) if x]
(P/'LP.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='rational_witness'})
