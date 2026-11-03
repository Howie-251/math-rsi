import os
for key in['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from collections import deque,Counter
import json,time,resource,subprocess,math,warnings
P=Path(__file__).resolve().parent;BASE=P.parent
assert not(P/'RESULT.json').exists()
START=time.process_time();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
 c=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-START+c.ru_utime+c.ru_stime-c0.ru_utime-c0.ru_stime
assert json.loads((P/'PREDICTION.json').read_text())['eligible_count']==648
subprocess.run(['g++','-O3','-std=c++17',str(P/'prepare.cpp'),'-o',str(P/'prepare')],check=True)
compiled=cpu()
with(P/'prepare.log').open('w')as log:
 subprocess.run([str(P/'prepare'),str(BASE/'source15552.header.edges'),str(P)],check=True,stdout=log,stderr=log,timeout=8)
prep=json.loads((P/'PREPARATION_RESULT.json').read_text())
out={'status':'PREPARATION_PENDING','hypothetical_n':15553,'actual_n':None,'actual_D':None,'ordinary_bad_unordered_pairs':None,
 'source_n':15552,'source_m':116316,'eligible_count':648,'compile_CPU_seconds':compiled,
 'prep_CPU_seconds':prep['CPU_seconds'],'source_original_BFS':0,'new_graphs_generated':0,'solver_runs':0,'prediction':'UNRESOLVED','pending':[]}
if prep['CPU_limited']:
 out['status']='PREPARATION_CPU_LIMITED_UNKNOWN'
elif prep['allfree_union_missing']:
 out.update(status='ALLFREE_R3_UNION_OBSTRUCTION',prediction='REFUTED',allfree_union_missing=prep['allfree_union_missing'])
else:
 import numpy as np
 from scipy.sparse import csc_matrix,vstack
 from scipy.optimize import milp,Bounds,LinearConstraint
 with(P/'COVER_CSC.bin').open('rb')as f:
  n,nc,nnz=map(int,np.fromfile(f,dtype='<u4',count=3));ptr=np.fromfile(f,dtype='<i4',count=nc+1);rows=np.fromfile(f,dtype='<i4',count=nnz)
 assert(n,nc)==(15552,648)
 A=csc_matrix((np.ones(nnz,dtype=float),rows,ptr),shape=(n,nc))
 model=vstack([A,csc_matrix(np.ones((1,nc)))],format='csc')
 lb=np.r_[np.ones(n),0];ub=np.r_[np.full(n,np.inf),15]
 (P/'RUN_HANDLE.json').write_text(json.dumps({'status':'SINGLE_MILP_RUNNING','variables':nc,'coverage_rows':n,'nnz':nnz,'solver_seconds_limit':4.5,'threads':1},indent=2)+'\n')
 sc=time.process_time()
 with warnings.catch_warnings():
  warnings.simplefilter('ignore',RuntimeWarning)
  result=milp(c=np.ones(nc),integrality=np.ones(nc,dtype=int),bounds=Bounds(0,1),
   constraints=LinearConstraint(model,lb,ub),options={'time_limit':4.5,'presolve':True,'mip_rel_gap':0,'threads':1})
 solvercpu=time.process_time()-sc
 raw={'status':int(result.status),'message':str(result.message),'solver_CPU_seconds':solvercpu}
 for k in['fun','mip_node_count','mip_dual_bound','mip_gap']:
  val=getattr(result,k,None)
  if val is not None:raw[k]=float(val)if math.isfinite(float(val))else None
 (P/'SOLVER_RESULT.json').write_text(json.dumps(raw,indent=2)+'\n')
 out.update(solver_runs=1,solver=raw,variables=nc,coverage_rows=n,matrix_nonzeros=nnz)
 pins=[]
 if result.x is not None:pins=[prep['eligible_vertices'][i]for i,x in enumerate(result.x)if x>0.5]
 if pins and len(pins)<=15:
  it=iter(map(int,(BASE/'source15552.header.edges').read_text().split()));N=next(it);M=next(it);adj=[[]for _ in range(N+1)];edges=[]
  for _ in range(M):
   u,v=next(it),next(it);edges.append((u,v));adj[u].append(v);adj[v].append(u)
  assert len(set(pins))==len(pins)and all(len(adj[u])==14 for u in pins)
  for u in pins:adj[u].append(N);adj[N].append(u)
  dist=[-1]*(N+1);dist[N]=0;q=deque([N])
  while q:
   u=q.popleft()
   for v in adj[u]:
    if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
  missing=[u for u,d in enumerate(dist)if d<0 or d>4]
  assert not missing
  assert max(map(len,adj))<=15
  edgefile=P/'graph_d15_D4_n15553.edges'
  with edgefile.open('w')as f:
   f.write(f'{N+1} {M+len(pins)}\n')
   for u,v in edges:f.write(f'{u} {v}\n')
   for u in pins:f.write(f'{u} {N}\n')
  hit={'source_file':str(BASE/'source15552.header.edges'),'source_n':N,'source_m':M,
   'new_n':N+1,'new_m':M+len(pins),'new_vertex':N,'new_neighbors':pins,'new_degree':len(pins),
   'selected_old_degrees':[14]*len(pins),'maxdegree':15,'simple':True,'all_old_edges_retained':True,
   'fresh_newroot_BFS_visited':sum(d>=0 for d in dist),'fresh_newroot_eccentricity':max(dist),
   'fresh_newroot_missing':missing,'newroot_distance_histogram':dict(sorted(Counter(dist).items())),
   'graph_file':str(edgefile),'inherited_source_D4':True,'ordinary_bad_unordered_pairs':None,
   'actual_global_D_by_inheritance_and_Moore':4,'parent_acceptance_pending':True}
  (P/'FIRST_HIT.json').write_text(json.dumps(hit,indent=2)+'\n')
  out.update(status='FIRST_HIT_REQUIRES_PARENT_ACCEPTANCE',prediction='SUPPORTED',actual_n=N+1,actual_D=4,
   new_graphs_generated=1,graph_file=str(edgefile),pins=pins,pending=['Parent independent newroot/degree/oldedge acceptance'])
 else:
  out.update(status='SINGLE_MILP_INFEASIBLE'if result.status==2 else'SINGLE_MILP_UNKNOWN_NO_INCUMBENT',
   prediction='REFUTED'if result.status==2 else'UNRESOLVED',incumbent_pin_count=len(pins)if pins else None)
out['total_batch_CPU_seconds']=cpu()
for fn in['RESULT.json','terminal.json','RUN_HANDLE.json']:(P/fn).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)
