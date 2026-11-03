import os
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import sys,json,time,warnings,resource
from pathlib import Path
resource.setrlimit(resource.RLIMIT_CPU,(7,7));started=time.process_time()
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix
P=Path(sys.argv[1]);d=json.loads((P/'problem.json').read_text());npairs=len(d['pairs']);ne=len(d['graph']['edges']);cols=d['columns'];rr=[];cc=[];vv=[]
for j,col in enumerate(cols):
 e,oi=col['edge'],col['option']
 for row,value in d['edge_options'][e][oi]['bad_endpoint_counts']:rr.append(row);cc.append(j);vv.append(value)
 rr.append(npairs+e);cc.append(j);vv.append(1)
A=coo_matrix((np.asarray(vv,dtype=float),(np.asarray(rr,dtype=np.int32),np.asarray(cc,dtype=np.int32))),shape=(npairs+ne,len(cols))).tocsc();b=np.asarray(d['demands']+[1]*ne,dtype=float)
with warnings.catch_warnings(record=True) as ww:
 warnings.simplefilter('always');sol=milp(np.zeros(len(cols)),integrality=np.ones(len(cols)),bounds=Bounds(np.zeros(len(cols)),np.ones(len(cols))),constraints=LinearConstraint(A,b,b),options=dict(time_limit=5.0,threads=1,mip_rel_gap=0.0,disp=False))
r=dict(status=int(sol.status),message=str(sol.message),incumbent=sol.x is not None,CPU_seconds=time.process_time()-started,solver_time_limit_seconds=5,process_CPU_hard_limit_seconds=7,threads=1,variables=len(cols),rows=A.shape[0],nonzeros=A.nnz,warnings=[str(x.message) for x in ww])
if sol.x is not None:
 x=np.round(sol.x).astype(int);valid=bool(np.max(np.abs(sol.x-x))<1e-5 and np.all(A@x==b) and np.all((x==0)|(x==1)));r['integer_equalities_pass']=valid
 if valid:
  choice=[-1]*ne
  for j,value in enumerate(x):
   if value:assert choice[cols[j]['edge']]<0;choice[cols[j]['edge']]=cols[j]['option']
  assert min(choice)>=0;r['choice']=choice
(P/'solver_result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='choice'}),flush=True)
