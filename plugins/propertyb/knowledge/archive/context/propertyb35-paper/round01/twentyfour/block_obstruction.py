"""Find and exactly replay a type-count obstruction; not a hypergraph realization."""
from pathlib import Path
from fractions import Fraction as Q
import json,time,numpy as np
from scipy.optimize import milp,LinearConstraint,Bounds
HERE=Path(__file__).parent
z=json.loads((HERE/'LINK_BLOCK_PILOT.json').read_text());es=z['edges'];P=[[Q(x) for x in r] for r in z['probabilities']];mat=np.array([[float(x) for x in r] for r in P]);A=[np.ones(len(es)),*[np.array([e[i] for e in es]) for i in [0]],np.array([sum(e[1:3]) for e in es]),np.array([sum(e[3:]) for e in es]),np.array([e[1]*e[2] for e in es]),np.array([sum(e[1:3])*sum(e[3:]) for e in es]),np.array([sum(e[i]*e[j] for i in range(3,7) for j in range(i+1,7)) for e in es])];lo=[29,4,30,80,9,96,96];hi=[29]+[np.inf]*6
st=time.time();sol=milp(np.zeros(len(es)),integrality=np.ones(len(es)),bounds=Bounds(0,29),constraints=LinearConstraint(np.vstack((A,mat)),lo+[1]*len(P),hi+[np.inf]*len(P)),options={'time_limit':40})
print('status',sol.message,'time',time.time()-st,flush=True)
if sol.x is None:raise SystemExit(1)
n=[round(x) for x in sol.x];scores=[sum(a*b for a,b in zip(n,row)) for row in P];marg=[sum(int(x)*int(y) for x,y in zip(n,row)) for row in A]
assert min(scores)>=1 and all(a>=b for a,b in zip(marg,lo)) and sum(n)==29
out=dict(scope=__doc__,type_counts=[dict(edge=e,count=c) for e,c in zip(es,n) if c],family_count=len(P),exact_minimum=str(min(scores)),constraints=marg,required=lo,passed=True,elapsed_seconds=time.time()-st)
(HERE/'BLOCK_TYPE_OBSTRUCTION.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
