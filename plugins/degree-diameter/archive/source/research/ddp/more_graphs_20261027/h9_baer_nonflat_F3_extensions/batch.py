"""One canonical34-item cap0 Baer production pass; no anchor preparation."""
import time,resource
initial_child=resource.getrusage(resource.RUSAGE_CHILDREN)
from pathlib import Path
import json,subprocess
from collections import Counter
OUT=Path(__file__).resolve().parent;BASE=OUT.parent;ROOT=OUT.parents[3]
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
load=lambda p:json.loads(p.read_text())
assert load(OUT/'PREDICTION.json')['frozen_before_checks']
pool=load(BASE/'h9_baer_nonflat_F3_pool/pool12.json');assert (pool['source_n'],pool['source_m'])==(42398,245889)
items=sorted(enumerate(pool['records']),key=lambda x:(tuple(x[1]['pins']),x[0]))
assert len(items)==34 and all(len(r['pins'])==12 and r['anchor_cap']==0 for i,r in items)
(OUT/'frozen_items.json').write_text(json.dumps([dict(oldindex=i,pool_index=r['pool_index'],pins=r['pins']) for i,r in items],indent=2)+'\n')
source=BASE/'h9_baer_plane_extensions/graphs/graph_d12_D5_n42398.edges'
with source.open() as f:
 initial_n,initial_m=map(int,f.readline().split());adj=[[] for _ in range(initial_n)]
 for line in f:
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert (initial_n,initial_m)==(42398,245889)
NATIVE=BASE/'h9_d12_eightpin_extensions/cover';current_file=source;current_m=initial_m
rows=[];accepted=[];status='ALL34_FROZEN_ITEMS_TERMINAL'
(OUT/'items').mkdir(exist_ok=True);(OUT/'graphs').mkdir(exist_ok=True)
def cpu():
 c=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()+c.ru_utime+c.ru_stime-initial_child.ru_utime-initial_child.ru_stime
print('FROZEN '+json.dumps(dict(items=34,source_n=initial_n,cap0=True,CPU_total=cpu())),flush=True)
for ordinal,(oldindex,item) in enumerate(items):
 pins=item['pins'];row=dict(ordinal=ordinal,pool_index=item['pool_index'],oldindex=oldindex,source_n=len(adj),source_m=current_m,
   mandatory_pins=pins,neighbor_type='nonflat F3-plane Baer PG2(F3) folded blocking set',raw_point_count=13)
 blocked=[v for v in pins if len(adj[v])>=12]
 if blocked:row.update(status='CURRENT_DEGREE_BLOCKED',blocked_pins=blocked);rows.append(row);continue
 if 5-cpu()<1.0:status='TOTAL_CPU_RESERVE_STOP';break
 prefix=OUT/'items'/f'ord{ordinal:02d}_pool{item["pool_index"]}_n{len(adj)}';pf=Path(str(prefix)+'.pins.txt');pf.write_text(' '.join(map(str,pins))+'\n')
 with Path(str(prefix)+'.log').open('w') as log:
  ret=subprocess.run([str(NATIVE),'verify',str(current_file),str(pf),str(prefix)],stdout=log,stderr=log)
 if ret.returncode:row.update(status='UNKNOWN_NATIVE_VERIFY_LIMIT',returncode=ret.returncode);rows.append(row);continue
 check=load(Path(str(prefix)+'.json'));missing=check['missing'];core=[v for v in missing if v<41356]
 row.update(core_R4_missing_count=len(core),extra_R4_missing_count=len(missing)-len(core),
            full_R4_missing=missing,native_verify_file=str(Path(str(prefix)+'.json').relative_to(ROOT)),native_CPU_seconds=check['CPU_seconds'])
 if core:
  row.update(status='PCORE_COUNTEREXAMPLE_STOP',Baer_witness=item['witness']);rows.append(row);status='PCORE_COUNTEREXAMPLE_STOP'
  (OUT/'Pcore_counterexample.json').write_text(json.dumps(row,indent=2)+'\n');break
 if missing:row['status']='EXACT_CAP0_EXTRAS_MISSING';rows.append(row);continue
 assert max(check['pin_current_degrees'])<12
 row.update(status='ACCEPTED_NONFLAT_BAER_CURRENT_R4',new_vertex=len(adj),full_neighbor_set=pins,anchors=[],
   neighbors_old_degrees=check['pin_current_degrees'],new_vertex_degree=12,new_n=len(adj)+1,new_m=current_m+12,
   actual_current_R4_covered=len(adj),actual_current_R4_missing=0,Baer_witness=item['witness'])
 adj.append(pins.copy())
 for v in pins:adj[v].append(len(adj)-1)
 current_m+=12;current_file=OUT/'graphs'/f'graph_d12_D5_n{len(adj)}.edges'
 with current_file.open('w') as f:
  f.write(f'{len(adj)} {current_m}\n')
  for u,ns in enumerate(adj):
   for v in ns:
    if u<v:f.write(f'{u} {v}\n')
 rows.append(row);accepted.append(row)
 (OUT/'accepted_extensions.json').write_text(json.dumps(dict(initial_n=initial_n,records=accepted,final_n=len(adj),final_m=current_m),indent=2)+'\n')
 print('HIT '+json.dumps(dict(pool_index=item['pool_index'],new_n=len(adj),CPU_total=cpu())),flush=True)
result=dict(status=status,initial_n=initial_n,initial_m=initial_m,final_n=len(adj),final_m=current_m,scope_items=34,
 rows_visited=len(rows),items_unattempted=34-len(rows),rows=rows,records=accepted,accepted_extensions=len(accepted),
 final_graph=str(current_file.relative_to(ROOT)),Pcore_counterexample=status=='PCORE_COUNTEREXAMPLE_STOP',
 native_verify_calls=sum('native_verify_file' in r for r in rows),native_prepare_calls=0,anchors_optimized=False,
 CPU_parent_plus_all_children_seconds=cpu(),row_status_counts=dict(Counter(r['status'] for r in rows)),
 allsource_BFS=0,externalreview=0,Lean=0,delivery_modified=False,pending=[])
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'accepted_extensions.json').write_text(json.dumps(dict(initial_n=initial_n,records=accepted,final_n=len(adj),final_m=current_m),indent=2)+'\n')
print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k not in ['rows','records']}),flush=True)
if accepted:exec(compile((OUT/'deliver.py').read_text(),str(OUT/'deliver.py'),'exec'))
