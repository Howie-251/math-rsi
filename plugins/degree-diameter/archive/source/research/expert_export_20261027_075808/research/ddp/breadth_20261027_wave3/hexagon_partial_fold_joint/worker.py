import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:
 os.environ[key]='1'
from pathlib import Path
import sys,json,time,warnings,resource,math
resource.setrlimit(resource.RLIMIT_CPU,(10,10))
started=time.process_time();wall=time.monotonic()
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import coo_matrix

P=Path(__file__).resolve().parent;S=P.parent/'hexagon_partial_fold_scout';index=int(sys.argv[1])
D=json.loads((S/'Q_data.json').read_text());W=json.loads((P/'current_state.json').read_text());reg=json.loads((P/'regions.json').read_text())[index]
Q=D['Q'];h_of=D['H3_neighbors'];HN=D['H3_graph'];HQ=D['H3_generic_neighbors'];absolute=D['H3_absolute'];state=W['states'];cp=W['h3_extra_copies']
R=reg['generic_ids'];H=reg['H3_ids'];ri={v:i for i,v in enumerate(R)};hi={h:2*len(R)+i for i,h in enumerate(H)};nv=2*len(R)+len(H)
rows=[];cols=[];data=[];lbs=[];ubs=[];constant_rows=0
def addterm(expr,kind,u,k=0,factor=1):
 terms,const=expr
 if kind=='s':
  if u in ri:
   for j in (2*ri[u],2*ri[u]+1):terms[j]=terms.get(j,0)+factor
  else:const+=factor*(state[u]!=0)
 elif kind=='x':
  if u in ri:
   j=2*ri[u]+k;terms[j]=terms.get(j,0)+factor
  else:const+=factor*(state[u]==k+1)
 else:
  if u>=0:
   if u in hi:terms[hi[u]]=terms.get(hi[u],0)+factor
   else:const+=factor*cp[u]
 return terms,const
def addrow(expr,lb=-np.inf,ub=np.inf):
 global constant_rows
 terms,const=expr;terms={j:v for j,v in terms.items() if v}
 if not terms:
  assert lb-1e-8<=const<=ub+1e-8
  constant_rows+=1;return
 row=len(lbs)
 for j,v in terms.items():rows.append(row);cols.append(j);data.append(v)
 lbs.append(lb-const);ubs.append(ub-const)

affected=set(R)|{v for u in R for v in Q[u]}|{u for u,h in enumerate(h_of) if h in hi}
affected_h={h for h,row in enumerate(HQ) if any(u in ri for u in row)}|{h for h,row in enumerate(HN) if any(v in hi for v in row)}
for f in sorted(affected):
 df=len(Q[f]);expr=({},0)
 for g in Q[f]:expr=addterm(expr,'s',g)
 expr=addterm(expr,'z',h_of[f]);expr=addterm(expr,'s',f,factor=-df);addrow(expr,ub=2)
 for k in range(2):
  expr=({},0)
  for g in Q[f]:expr=addterm(expr,'x',g,k=k)
  expr=addterm(expr,'z',h_of[f]);expr=addterm(expr,'x',f,k=k,factor=df);addrow(expr,ub=2+df)
for f in R:addrow(addterm(({},0),'s',f),ub=1)
for h in sorted(affected_h):
 expr=({},0)
 for f in HQ[h]:expr=addterm(expr,'s',f)
 for k in HN[h]:expr=addterm(expr,'z',k)
 addrow(expr,ub=5+int(absolute[h]))
old_local=sum(state[u]!=0 for u in R)+sum(cp[h] for h in H)
addrow(({j:1 for j in range(nv)},0),lb=old_local)
A=coo_matrix((np.asarray(data,dtype=np.float64),(np.asarray(rows,dtype=np.int32),np.asarray(cols,dtype=np.int32))),shape=(len(lbs),nv)).tocsc()
xold=np.zeros(nv)
for u in R:
 if state[u]:xold[2*ri[u]+state[u]-1]=1
for h in H:xold[hi[h]]=cp[h]
ax=A@xold
assert np.all(ax>=np.asarray(lbs)-1e-8) and np.all(ax<=np.asarray(ubs)+1e-8)
upper=np.ones(nv);upper[2*len(R):]=2
prep_cpu=time.process_time()-started
with warnings.catch_warnings(record=True) as ww:
 warnings.simplefilter('always')
 sol=milp(-np.ones(nv),integrality=np.ones(nv),bounds=Bounds(np.zeros(nv),upper),constraints=LinearConstraint(A,np.asarray(lbs),np.asarray(ubs)),options=dict(time_limit=8.5,threads=1,mip_rel_gap=0.0,disp=False))
result=dict(region=index,name=reg['name'],root=reg['root'],free_generic=len(R),free_H3_copies=len(H),variables=nv,actual_constraint_rows=len(lbs),constant_legal_rows_skipped=constant_rows,nonzero_coefficients=A.nnz,affected_generic=len(affected),affected_H3=len(affected_h),old_local_objective=old_local,baseline_vector_satisfies_all_constraints=True,status=int(sol.status),message=str(sol.message),incumbent_returned=sol.x is not None,preparation_CPU_seconds=prep_cpu,total_worker_CPU_seconds=time.process_time()-started,wall_seconds=time.monotonic()-wall,solver_time_limit_seconds=8.5,process_CPU_hard_limit_seconds=10,threads=1,warnings=[str(a.message) for a in ww])
for attr in ['mip_node_count','mip_gap','mip_dual_bound','fun']:
 value=getattr(sol,attr,None)
 result[attr]=float(value) if value is not None and math.isfinite(value) else None
if sol.x is not None:
 integral=bool(np.all(np.abs(sol.x-np.round(sol.x))<=1e-5));result['integer_candidate']=integral
 if integral:
  xx=np.round(sol.x).astype(int);cand=state.copy();cc=cp.copy()
  for u in R:
   a,b=xx[2*ri[u]],xx[2*ri[u]+1]
   if a+b>1 or min(a,b)<0:integral=False;break
   cand[u]=1 if a else 2 if b else 0
  for h in H:cc[h]=int(xx[hi[h]])
  if integral:
   f=P/f'region_{index}_candidate.json';f.write_text(json.dumps(dict(states=cand,h3_extra_copies=cc),separators=(',',':'))+'\n');result['candidate_file']=f.name
(P/f'region_{index}_result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
