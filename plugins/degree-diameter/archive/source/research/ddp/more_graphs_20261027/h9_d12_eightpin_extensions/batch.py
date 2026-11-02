"""Produce the frozen13 eight-pin Q-line extensions; one sequential CPU worker."""
from pathlib import Path
import json
import resource
import subprocess
import time
import warnings

START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(84,87))
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
frozen=json.loads((OUT/'PREDICTION.json').read_text())
assert frozen['frozen_before_batch']
source=ROOT/frozen['base_source']
with source.open() as f:
 initial_n,initial_m=map(int,f.readline().split())
 adj=[[] for _ in range(initial_n)]
 for line in f:
  if not line.strip():continue
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert initial_n==42377
# Existing42377 correctness is inherited; no graph audit or all-source BFS here.
current_file=source;current_m=initial_m
pool=json.loads((ROOT/frozen['pool']).read_text())['records']
rows=[];accepted=[];mip_calls=0;selected_checks=0;mandatory_checks=0

def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-START+r.ru_utime+r.ru_stime

def native(mode,pins,prefix):
 pinfile=Path(str(prefix)+'.pins.txt');pinfile.write_text(' '.join(map(str,pins))+'\n')
 run=subprocess.run([str(OUT/'cover'),mode,str(current_file),str(pinfile),str(prefix)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
 if run.returncode:return None,{'returncode':run.returncode,'stderr':run.stderr[-1000:]}
 return json.loads(Path(str(prefix)+'.json').read_text()),None

def save_graph():
 path=OUT/'graphs'/f'graph_d12_D5_n{len(adj)}.edges'
 with path.open('w') as f:
  f.write(f'{len(adj)} {current_m}\n')
  for u,ns in enumerate(adj):
   for v in ns:
    if u<v:f.write(f'{u} {v}\n')
 return path

def checkpoint(final=False):
 result=dict(status='COMPLETE_FIXED13_PASS' if final else 'RUNNING_FIXED13_PASS',initial_graph=str(source.relative_to(ROOT)),initial_n=initial_n,initial_m=initial_m,
  final_n=len(adj),final_m=current_m,target_Delta=12,target_D=5,scope_items=13,rows_attempted=len(rows),accepted_extensions=len(accepted),
  accepted_pool_indices=[r['pool_index'] for r in accepted],rows=rows,final_graph=str(current_file.relative_to(ROOT)),
  producer_selected_full_R4_checks=selected_checks,mandatory_full_R4_checks=mandatory_checks,MIP_calls=mip_calls,
  total_CPU_seconds=cpu(),all_source_BFS_executed=0,old_base_reaudited=False,older_snapshots_modified=False,
  single_vertex_R4_induction=True,actual_D=5,actual_D_scope='Inherit verified42377D5; every accepted addition passed complete selectedR4 on its immediately preceding graph. No fresh all-source BFS. Moore(12,4)<n gives exact5.',
  pending=[] if final else ['complete frozen13 production pass'])
 (OUT/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 (OUT/'accepted_extensions.json').write_text(json.dumps(dict(initial_n=initial_n,final_n=len(adj),records=accepted),ensure_ascii=False,indent=2)+'\n')
 return result

for item in frozen['items']:
 ordinal,index,pins=item['ordinal'],item['pool_index'],item['mandatory_pins']
 start=cpu();N=len(adj)
 row=dict(ordinal=ordinal,pool_index=index,source_n=N,source_m=current_m,source_graph=str(current_file.relative_to(ROOT)),mandatory_pins=pins,
  mandatory_old_degrees=[len(adj[v]) for v in pins],anchor_cap=4)
 if cpu()>78:
  row.update(status='UNATTEMPTED_TOTAL_CPU_LIMIT',CPU_seconds=0);rows.append(row);continue
 prefix=OUT/'items'/f'item{ordinal:02d}_pool{index}'
 prepared,error=native('prepare',pins,prefix)
 if error:
  row.update(status='UNKNOWN_PREPARATION_PROCESS_LIMIT',preparation_process=error,CPU_seconds=cpu()-start);rows.append(row);checkpoint();continue
 row['prepare_CPU_seconds']=prepared['CPU_seconds']
 if prepared['status']=='DEGREE_INFEASIBLE':
  row.update(status='DEGREE_INFEASIBLE_ON_CURRENT_BASE',saturated_mandatory_pins=prepared['blocked'],CPU_seconds=cpu()-start);rows.append(row);checkpoint();continue
 mandatory_checks+=1
 row.update(mandatory_R4_missing_count=prepared['missing_count'],mandatory_R4_missing=prepared['missing'],mandatory_R4_covered_count=prepared['covered_count'],
  eligible_anchors=prepared.get('eligible_anchors',0),unique_nonzero_anchor_masks=prepared.get('unique_nonzero_masks',0),
  exact_two_complete=prepared.get('exact_two_complete',True),exact_two_first_masks_tested=prepared.get('exact_two_first_masks_tested',0))
 anchors=[] if prepared['missing_count']==0 else (prepared['exact_anchors'] if prepared.get('exact_one_or_two_found') else None)
 if anchors is None and prepared.get('zero_cover_targets'):
  row.update(status='NO_ALLOWED_ANCHOR_COVERS_A_MISSING_TARGET',zero_cover_targets=prepared['zero_cover_targets'],CPU_seconds=cpu()-start);rows.append(row);checkpoint();continue
 if anchors is None:
  if cpu()>78:
   row.update(status='UNKNOWN_TOTAL_CPU_LIMIT_BEFORE_MIP',CPU_seconds=cpu()-start);rows.append(row);checkpoint();continue
  import numpy as np
  from scipy.optimize import milp,Bounds,LinearConstraint
  from scipy.sparse import coo_matrix
  K=prepared['unique_nonzero_masks'];W=prepared['mask_words_per_row'];T=prepared['missing_count']
  masks=np.fromfile(str(prefix)+'.masks.u64.bin',dtype=np.uint64).reshape(K,W)
  rr=[];cc=[]
  for j in range(T):
   cols=np.flatnonzero((masks[:,j//64]>>np.uint64(j%64))&np.uint64(1)).astype(np.int32)
   rr.append(np.full(len(cols),j,dtype=np.int32));cc.append(cols)
  rr.append(np.full(K,T,dtype=np.int32));cc.append(np.arange(K,dtype=np.int32))
  ridx=np.concatenate(rr);cidx=np.concatenate(cc)
  A=coo_matrix((np.ones(len(ridx),dtype=np.float64),(ridx,cidx)),shape=(T+1,K)).tocsc()
  lower=np.r_[np.ones(T),-np.inf];upper=np.r_[np.full(T,np.inf),4.0]
  timecap=min(4.0,max(.05,78-cpu()))
  row.update(MIP_rows=T+1,MIP_variables=K,MIP_nonzeros=int(A.nnz),MIP_time_limit_seconds=timecap)
  mipstart=cpu();mip_calls+=1
  with warnings.catch_warnings():
   warnings.filterwarnings('ignore',message='Unrecognized options detected')
   res=milp(c=np.zeros(K),integrality=np.ones(K,dtype=np.uint8),bounds=Bounds(np.zeros(K),np.ones(K)),
    constraints=LinearConstraint(A,lower,upper),options={'time_limit':timecap,'presolve':True,'threads':1})
  row.update(MIP_status=int(res.status),MIP_message=str(res.message),MIP_CPU_seconds=cpu()-mipstart)
  if res.x is not None:
   chosen=np.flatnonzero(res.x>.5)
   if len(chosen)<=4:
    combined=np.bitwise_or.reduce(masks[chosen],axis=0) if len(chosen) else np.zeros(W,dtype=np.uint64)
    full=np.full(W,np.uint64(2**64-1));
    if T%64:full[-1]=np.uint64((1<<(T%64))-1)
    if np.array_equal(combined,full):anchors=sorted(prepared['representatives'][int(i)] for i in chosen)
  if anchors is None:
   row.update(status='SOLVER_REPORTED_NO_LE4_COVER_ON_CURRENT_BASE' if res.status==2 else 'UNKNOWN_MIP_NO_VERIFIED_INCUMBENT',CPU_seconds=cpu()-start)
   rows.append(row);checkpoint();print('ITEM '+json.dumps({k:row[k] for k in ['ordinal','pool_index','status','source_n','mandatory_R4_missing_count','MIP_status','MIP_CPU_seconds']}),flush=True);continue
 neighbors=sorted(pins+anchors)
 if anchors:
  finalcheck,error=native('verify',neighbors,Path(str(prefix)+'_selected'))
  if error or finalcheck.get('status')!='FULL_SELECTED_R4_CHECK_COMPLETE' or finalcheck.get('missing_count')!=0:
   row.update(status='ERROR_SELECTED_COMPLETE_R4_DID_NOT_PASS',error=error,selected_result=finalcheck);rows.append(row);checkpoint();raise RuntimeError('Selected fullR4 did not pass; no graph accepted')
  selected_checks+=1;olddegrees=finalcheck['pin_current_degrees'];covered=finalcheck['covered_count'];reused=False
 else:
  olddegrees=prepared['pin_current_degrees'];covered=prepared['covered_count'];reused=True
 assert len(neighbors)==len(set(neighbors))<=12 and len(anchors)<=4
 row.update(status='ACCEPTED_BY_COMPLETE_R4_INDUCTION',anchors=anchors,new_vertex=N,new_vertex_degree=len(neighbors),full_neighbor_set=neighbors,
  neighbors_old_degrees=olddegrees,selected_full_R4_covered_count=covered,selected_full_R4_missing_count=0,
  selected_R4_reused_mandatory=reused,new_n=N+1,new_m=current_m+len(neighbors),geometric_witnesses=pool[index].get('geometric_witnesses',[]))
 adj.append(neighbors.copy())
 for v in neighbors:adj[v].append(N)
 current_m+=len(neighbors)
 current_file=save_graph()
 row.update(graph_file=str(current_file.relative_to(ROOT)),CPU_seconds=cpu()-start)
 rows.append(row);accepted.append(row)
 (OUT/f'accepted_{len(accepted):02d}_pool{index}.json').write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
 checkpoint()
 print('HIT '+json.dumps(dict(accepted=len(accepted),pool_index=index,new_n=len(adj),new_vertex=N,new_vertex_degree=len(neighbors),anchors=anchors,full_neighbor_set=neighbors,graph_file=str(current_file.relative_to(ROOT)),total_CPU_seconds=cpu())),flush=True)
final=checkpoint(True)
final['items_unknown']=sum(r['status'].startswith('UNKNOWN') for r in rows)
final['items_unattempted']=sum(r['status'].startswith('UNATTEMPTED') for r in rows)
final['degree_infeasible_items']=sum(r['status']=='DEGREE_INFEASIBLE_ON_CURRENT_BASE' for r in rows)
final['pending']=[]
(OUT/'RESULT.json').write_text(json.dumps(final,ensure_ascii=False,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps({k:v for k,v in final.items() if k!='rows'},ensure_ascii=False,indent=2)+'\n')
print('TERMINAL '+json.dumps({k:v for k,v in final.items() if k!='rows'}),flush=True)
