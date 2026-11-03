"""Refresh only stale first-Baer prefix on42398; no unrelatedscope repeats."""
import time,resource
initial_child=resource.getrusage(resource.RUSAGE_CHILDREN)
from pathlib import Path
import json,subprocess
from collections import Counter
OUT=Path(__file__).resolve().parent;BASE=OUT.parent;ROOT=OUT.parents[3]
load=lambda p:json.loads(p.read_text())
assert load(OUT/'PREDICTION.json')['frozen_before_checks']
freeze=load(OUT/'freeze_summary.json');items=load(OUT/'frozen_items.json')
resource.setrlimit(resource.RLIMIT_CPU,(10,10))
NATIVE=BASE/'h9_d12_ninepin_saturated_deletion/cover'
pool=load(BASE/'h9_baer_plane_pool/pool12.json')['records']
source=BASE/'h9_baer_plane_extensions/graphs/graph_d12_D5_n42398.edges'
with source.open() as f:
 initial_n,initial_m=map(int,f.readline().split());adj=[[] for _ in range(initial_n)]
 for line in f:
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert (initial_n,initial_m)==(42398,245889)
current_file=source;current_m=initial_m;rows=[];accepted=[];prepare_calls=0;verify_calls=0
(OUT/'items').mkdir(exist_ok=True);(OUT/'graphs').mkdir(exist_ok=True)
def cpu():
 c=resource.getrusage(resource.RUSAGE_CHILDREN)
 return freeze['prepare_CPU_seconds']+time.process_time()+c.ru_utime+c.ru_stime-initial_child.ru_utime-initial_child.ru_stime
status='ALL_FROZEN_STALE_ITEMS_TERMINAL'
for ordinal,item in enumerate(items):
 pins=item['pins'];cap=item['anchor_cap'];row=dict(**item,ordinal=ordinal,source_n=len(adj),source_m=current_m,
   mandatory_pins=pins,neighbor_type='Baer PG2(F3) folded blocking set',raw_point_count=13)
 blocked=[v for v in pins if len(adj[v])>=12]
 if blocked:row.update(status='CURRENT_DEGREE_BLOCKED',blocked_pins=blocked);rows.append(row);continue
 if 10-cpu()<1.8:status='TOTAL_CPU_RESERVE_STOP';break
 prefix=OUT/'items'/f'ord{ordinal:02d}_pool{item["pool_index"]}_n{len(adj)}';pf=Path(str(prefix)+'.pins.txt');pf.write_text(' '.join(map(str,pins))+'\n')
 mode='prepare' if cap else 'verify'
 with Path(str(prefix)+'.log').open('w') as log:
  ret=subprocess.run([str(NATIVE),mode,str(current_file),str(pf),str(prefix)],stdout=log,stderr=log)
 if cap:prepare_calls+=1
 else:verify_calls+=1
 if ret.returncode:row.update(status='UNKNOWN_NATIVE_LIMIT',returncode=ret.returncode);rows.append(row);continue
 prep=load(Path(str(prefix)+'.json'));missing=prep['missing'];core=[v for v in missing if v<41356]
 row.update(mandatory_R4_missing=len(missing),core_R4_missing_count=len(core),extra_R4_missing_count=len(missing)-len(core),
            native_prepare_file=str(Path(str(prefix)+'.json').relative_to(ROOT)),native_CPU_seconds=prep['CPU_seconds'])
 if core:
  row.update(status='PCORE_COUNTEREXAMPLE_STOP',missing_core_vertices=core);rows.append(row);status='PCORE_COUNTEREXAMPLE_STOP'
  (OUT/'Pcore_counterexample.json').write_text(json.dumps(row,indent=2)+'\n');break
 anchors=[] if not missing else None
 if missing:
  if cap==0:row['status']='EXACT_CAP0_EXTRAS_MISSING'
  elif cap==1:
   a=prep.get('exact_anchors',[])
   if prep.get('exact_one_or_two_found') and len(a)==1:anchors=a
   else:row['status']='EXACT_NO_ONE_ANCHOR'
  elif prep.get('exact_one_or_two_found'):anchors=prep['exact_anchors']
  else:row['status']='EXACT_NO_AT_MOST_TWO_ANCHORS' if prep['exact_two_complete'] else 'UNKNOWN_NATIVE_EXACT_TWO_LIMIT'
 if anchors is None:rows.append(row);continue
 neighbors=sorted(pins+anchors);assert len(neighbors)==len(set(neighbors))<=12 and all(len(adj[v])<12 for v in neighbors)
 if anchors:
  pf.write_text(' '.join(map(str,neighbors))+'\n');selected=Path(str(prefix)+'_selected')
  ret=subprocess.run([str(NATIVE),'verify',str(current_file),str(pf),str(selected)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL);verify_calls+=1
  assert ret.returncode==0;good=load(Path(str(selected)+'.json'));selected_file=Path(str(selected)+'.json')
 else:good=prep;selected_file=Path(str(prefix)+'.json')
 assert good['missing_count']==0 and max(good['pin_current_degrees'])<12
 row.update(status='ACCEPTED_BAER_COMPLETE_CURRENT_R4',new_vertex=len(adj),full_neighbor_set=neighbors,anchors=anchors,
   neighbors_old_degrees=good['pin_current_degrees'],new_vertex_degree=len(neighbors),new_n=len(adj)+1,new_m=current_m+len(neighbors),
   actual_current_R4_covered=len(adj),actual_current_R4_missing=0,native_verify_file=str(selected_file.relative_to(ROOT)),
   Baer_witness=pool[item['oldindex']]['witness'])
 adj.append(neighbors.copy())
 for v in neighbors:adj[v].append(len(adj)-1)
 current_m+=len(neighbors);current_file=OUT/'graphs'/f'graph_d12_D5_n{len(adj)}.edges'
 with current_file.open('w') as f:
  f.write(f'{len(adj)} {current_m}\n')
  for u,ns in enumerate(adj):
   for v in ns:
    if u<v:f.write(f'{u} {v}\n')
 row['graph_file']=str(current_file.relative_to(ROOT));rows.append(row);accepted.append(row)
 (OUT/'accepted_extensions.json').write_text(json.dumps(dict(initial_n=initial_n,records=accepted,final_n=len(adj),final_m=current_m),indent=2)+'\n')
 print('HIT '+json.dumps(dict(pool_index=item['pool_index'],new_n=len(adj),anchors=anchors,CPU_total=cpu())),flush=True)
 if len(accepted)==16:status='SIXTEEN_ACCEPTED_REVIEW_POINT';break
# Explicit stale refreshprefix rows; a hit does not certify old failures on the laterbase.
latest={r['pool_index']:r for r in rows}
stale=[]
for item in items:
 r=latest.get(item['pool_index'])
 if r is None or (r['source_n']<len(adj) and not r['status'].startswith('ACCEPTED')) or r['status'].startswith('UNKNOWN'):
  if all(len(adj[v])<12 for v in item['pins']):stale.append(dict(pool_index=item['pool_index'],pins=item['pins'],last_evaluation_source_n=r['source_n'] if r else item['prior_source_n'],status=r['status'] if r else 'UNATTEMPTED'))
(OUT/'stale_items.json').write_text(json.dumps(stale,indent=2)+'\n')
(OUT/'accepted_extensions.json').write_text(json.dumps(dict(initial_n=initial_n,records=accepted,final_n=len(adj),final_m=current_m),indent=2)+'\n')
result=dict(status=status,initial_n=initial_n,initial_m=initial_m,final_n=len(adj),final_m=current_m,
 scope_frozen=len(items),rows_visited=len(rows),items_unattempted=len(items)-len(rows),rows=rows,records=accepted,
 accepted_extensions=len(accepted),stale_currentlegal_prefix_items=len(stale),stale_items_file='stale_items.json',
 previous_same42398_failure_scopes_need_refresh=bool(accepted),final_graph=str(current_file.relative_to(ROOT)),
 native_prepare_calls=prepare_calls,native_verify_calls=verify_calls,CPU_parent_plus_all_children_seconds=cpu(),
 row_status_counts=dict(Counter(r['status'] for r in rows)),Pcore_counterexample=status=='PCORE_COUNTEREXAMPLE_STOP',
 allsource_BFS=0,externalreview=0,Lean=0,MIP=0,delivery_modified=False,closure_decision_owner='root',pending=[])
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k not in ['rows','records']}),flush=True)
if accepted:exec(compile((OUT/'deliver.py').read_text(),str(OUT/'deliver.py'),'exec'))
