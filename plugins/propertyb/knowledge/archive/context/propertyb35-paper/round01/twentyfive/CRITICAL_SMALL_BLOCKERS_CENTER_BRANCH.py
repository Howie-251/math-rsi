"""Four bounded integer count relaxations, adding the true center disjunction.
Not hypergraphs or incidence assignments. Existing source read but not executed below its model functions.
"""
from pathlib import Path
import json,time
import numpy as np
from scipy.optimize import milp,LinearConstraint,Bounds
P=Path(__file__).resolve().parent
ns={'__file__':str(P/'CRITICAL_SMALL_BLOCKERS_ACTION_PARITY_LP.py')};exec((P/'CRITICAL_SMALL_BLOCKERS_ACTION_PARITY_LP.py').read_text().split('\nresults=[]')[0],ns)
st=time.perf_counter();rows=[]
for a in [7,8]:
 m=ns['model'](24,34,35,a);types=m['types'];c=[int(z==(1,0,4)) for z in types];b1=[int(z[2]==1) for z in types]
 for branch in ['many_positive','singleton_blockers']:
  A=list(m['ge']);lo=list(m['ge_rhs']);hi=[np.inf]*len(A)
  if branch=='many_positive':A.append(c);lo.append(10);hi.append(np.inf)
  else:A.extend([c,b1]);lo.extend([0,4]);hi.extend([9,np.inf])
  A.extend(m['equalities']);lo.extend(m['equality_rhs']);hi.extend(m['equality_rhs'])
  z=milp(np.zeros(len(types)),integrality=np.ones(len(types)),bounds=Bounds(0,np.inf),constraints=LinearConstraint(A,lo,hi),options={'time_limit':2})
  row=dict(a=a,b=m['b'],branch=branch,status=int(z.status),message=z.message)
  if z.x is not None:
   x=[round(v) for v in z.x]
   exact=all(sum(v*y for v,y in zip(rr,x))>=bd for rr,bd in zip(m['ge'],m['ge_rhs'])) and all(sum(v*y for v,y in zip(rr,x))==bd for rr,bd in zip(m['equalities'],m['equality_rhs'])) and (sum(v*y for v,y in zip(c,x))>=10 if branch=='many_positive' else sum(v*y for v,y in zip(c,x))<=9 and sum(v*y for v,y in zip(b1,x))>=4)
   row.update(support=[dict(r=r,s=s,t=t,N=v) for (r,s,t),v in zip(types,x) if v],exact_passed=exact)
  rows.append(row)
out=dict(scope=__doc__,elapsed_seconds=time.perf_counter()-st,results=rows)
(P/'CRITICAL_SMALL_BLOCKERS_CENTER_BRANCH.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
