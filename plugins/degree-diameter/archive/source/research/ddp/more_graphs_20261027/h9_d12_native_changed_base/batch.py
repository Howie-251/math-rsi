"""One native complete<=2-anchor pass; CPU budget includes every child."""
from pathlib import Path
from collections import Counter
import json
import resource
import subprocess
import time

OUT=Path(__file__).resolve().parent;BASE=OUT.parent;ROOT=OUT.parents[3]
START=time.process_time();initial_child=resource.getrusage(resource.RUSAGE_CHILDREN)
resource.setrlimit(resource.RLIMIT_CPU,(45,45))
load=lambda p:json.loads(p.read_text())
plan=load(OUT/'PREDICTION.json');assert plan['frozen_before_native_checks']
freeze=load(OUT/'freeze_summary.json');items=load(OUT/'frozen_items.json')
NATIVE=BASE/'h9_d12_eightpin_extensions/cover'
source=BASE/'h9_d12_eightpin_constructive/graphs/graph_d12_D5_n42396.edges'
with source.open() as f:
 initial_n,initial_m=map(int,f.readline().split());adj=[[] for _ in range(initial_n)]
 for line in f:
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert (initial_n,initial_m)==(42396,245865)
current_file=source;current_m=initial_m;rows=[];accepted=[];prepare_calls=0;verify_calls=0
(OUT/'items').mkdir(exist_ok=True);(OUT/'graphs').mkdir(exist_ok=True)
def cpu():
 c=resource.getrusage(resource.RUSAGE_CHILDREN)
 return freeze['prepare_CPU_seconds']+time.process_time()-START+(c.ru_utime+c.ru_stime)-(initial_child.ru_utime+initial_child.ru_stime)
def writegraph(path):
 with path.open('w') as f:
  f.write(f'{len(adj)} {current_m}\n')
  for u,ns in enumerate(adj):
   for v in ns:
    if u<v:f.write(f'{u} {v}\n')
def checkpoint():
 (OUT/'accepted_extensions.json').write_text(json.dumps(dict(initial_n=initial_n,initial_m=initial_m,
    final_n=len(adj),final_m=current_m,records=accepted,root_allsource_requested=False),indent=2)+'\n')
status='ALL_FROZEN_ITEMS_TERMINAL';profile=False
for ordinal,item in enumerate(items):
 if 45-cpu()<7.8:status='TOTAL_CPU_RESERVE_STOP';break
 pins=item['pins'];row=dict(ordinal=ordinal,pool_index=item['pool_index'],source_n=len(adj),source_m=current_m,
   mandatory_pins=pins,last_evaluation=item['last_evaluation'],
   prior_accepted_line_vertices=item['prior_accepted_line_vertices'],
   multiple_line_vertex=item['prior_accepted_line_vertices']>0)
 if any(len(adj[v])>=12 for v in pins):
  row.update(status='CURRENT_DEGREE_BLOCKED');rows.append(row);continue
 prefix=OUT/'items'/f"ord{ordinal:03d}_pool{item['pool_index']}_n{len(adj)}"
 pinfile=Path(str(prefix)+'.pins.txt');pinfile.write_text(' '.join(map(str,pins))+'\n')
 with Path(str(prefix)+'.log').open('w') as log:
  ret=subprocess.run([str(NATIVE),'prepare',str(current_file),str(pinfile),str(prefix)],stdout=log,stderr=log)
 prepare_calls+=1
 if ret.returncode!=0:
  row.update(status='UNKNOWN_NATIVE_CPU_OR_PROCESS_LIMIT',returncode=ret.returncode,CPU_total_after=cpu())
  rows.append(row);continue
 prepared=load(Path(str(prefix)+'.json'));row.update(native_prepare_file=str(Path(str(prefix)+'.json').relative_to(ROOT)),
   mandatory_missing_count=prepared.get('missing_count'),native_prepare_CPU_seconds=prepared['CPU_seconds'])
 if prepared['status']=='DEGREE_INFEASIBLE':row['status']='CURRENT_DEGREE_BLOCKED_NATIVE';rows.append(row);continue
 anchors=[] if prepared['missing_count']==0 else (prepared.get('exact_anchors') if prepared.get('exact_one_or_two_found') else None)
 if anchors is None:
  row['status']='EXACT_NO_AT_MOST_TWO_ANCHORS' if prepared['exact_two_complete'] else 'UNKNOWN_NATIVE_EXACT_TWO_LIMIT'
  rows.append(row)
 else:
  neighbors=sorted(pins+anchors)
  assert len(neighbors)==len(set(neighbors))<=12 and all(len(adj[v])<12 for v in neighbors)
  pinfile.write_text(' '.join(map(str,neighbors))+'\n');selected=Path(str(prefix)+'_selected')
  with Path(str(selected)+'.log').open('w') as log:
   ret=subprocess.run([str(NATIVE),'verify',str(current_file),str(pinfile),str(selected)],stdout=log,stderr=log)
  verify_calls+=1
  if ret.returncode!=0:
   row.update(status='UNKNOWN_NATIVE_SELECTED_VERIFY_LIMIT',returncode=ret.returncode);rows.append(row);continue
  check=load(Path(str(selected)+'.json'))
  assert check['status']=='FULL_SELECTED_R4_CHECK_COMPLETE' and check['missing_count']==0
  assert all(d<12 for d in check['pin_current_degrees'])
  row.update(status='ACCEPTED_ACTUAL_DEGREE_COMPLETE_R4',new_vertex=len(adj),full_neighbor_set=neighbors,
    anchors=anchors,new_vertex_degree=len(neighbors),neighbors_old_degrees=check['pin_current_degrees'],actual_current_R4_covered=len(adj),
    actual_current_R4_missing=0,new_n=len(adj)+1,new_m=current_m+len(neighbors),
    native_selected_R4_file=str(Path(str(selected)+'.json').relative_to(ROOT)),CPU_total_after=cpu())
  adj.append(neighbors.copy())
  for v in neighbors:adj[v].append(len(adj)-1)
  current_m+=len(neighbors);current_file=OUT/'graphs'/f'graph_d12_D5_n{len(adj)}.edges';writegraph(current_file)
  row['graph_file']=str(current_file.relative_to(ROOT));rows.append(row);accepted.append(row);checkpoint()
  print('HIT '+json.dumps(dict(accepted=len(accepted),ordinal=ordinal,pool_index=item['pool_index'],new_n=len(adj),CPU_total=cpu())),flush=True)
 if prepare_calls>=10 and not profile:
  profile=True
  p=dict(rows_attempted=len(rows),native_prepare_calls=prepare_calls,native_verify_calls=verify_calls,
         accepted=len(accepted),current_n=len(adj),parent_and_all_child_CPU_seconds=cpu())
  (OUT/'profile10.json').write_text(json.dumps(p,indent=2)+'\n');print('PROFILE10 '+json.dumps(p),flush=True)
 if len(accepted)==32:status='ACCEPTED32_REVIEW_POINT';break
checkpoint()
result=dict(status=status,initial_n=initial_n,initial_m=initial_m,final_n=len(adj),final_m=current_m,
 frozen_candidates=len(items),rows_attempted=len(rows),items_unattempted=len(items)-len(rows),
 complete_items=sum(not r['status'].startswith('UNKNOWN') for r in rows),
 unknown_items=sum(r['status'].startswith('UNKNOWN') for r in rows),rows=rows,accepted_extensions=len(accepted),
 final_graph=str(current_file.relative_to(ROOT)),native_prepare_calls=prepare_calls,native_selected_R4_calls=verify_calls,
 CPU_parent_and_all_children_seconds=cpu(),CPU_accounting='Freeze parent plus runningparent and every native child; delivery child added below',
 Python_reverse_target_BFS=0,MIP_calls=0,allsource_BFS=0,externalreview=0,pending=[],
 row_status_counts=dict(Counter(r['status'] for r in rows)),samebase_prior_failures_repeated=False,
 failed_current_batch_items_retried=False,general_family_excluded=False)
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
if accepted:exec(compile((OUT/'deliver.py').read_text(),str(OUT/'deliver.py'),'exec'))
