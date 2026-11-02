"""N11: fixed changed-base retries, fresh exact one-anchor coverage only."""
import json
import resource
import time
from collections import Counter
from pathlib import Path

OUT=Path(__file__).resolve().parent
BASE=OUT.parent
START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
plan=json.loads((OUT/'PREDICTION.json').read_text())
assert plan['frozen_before_retry_checks']
load=lambda p:json.loads(p.read_text())
pool=load(BASE/'h9_d11_followups/frozen_pool_order.json')['records']
fail={r['pool_index']:37628 for r in load(BASE/'h9_other_degrees/degree11_complete_cover.json')['rows'] if not r['complete_single_anchors']}
oldrows=load(BASE/'h9_d11_followups/RESULT.json')['rows']
used={3}|{r['pool_index'] for r in load(BASE/'h9_d11_followups/accepted_sequence.json')['accepted']}
for r in oldrows:
 if r['status']=='EXACT_CURRENT_ONE_ANCHOR_FAIL':fail[r['pool_index']]=r['base_n']
items=[r for r in pool if r['pool_index'] not in used and fail.get(r['pool_index'],37631)<37631]
items.sort(key=lambda r:tuple(r['pins']))
assert [r['pool_index'] for r in items]==plan['canonical_pool_indices']
frozen=[dict(pool_index=r['pool_index'],original_pool_index=r['original_pool_index'],
             pins=r['pins'],last_failed_source_n=fail[r['pool_index']]) for r in items]
(OUT/'frozen_items.json').write_text(json.dumps(frozen,indent=2)+'\n')
source=BASE/'h9_d11_followups/graph_d11_D5_n37631.edges'
with source.open() as stream:
 n,m=map(int,stream.readline().split());adj=[[] for _ in range(n)]
 for line in stream:
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert (n,m)==(37631,205329)
rows=[];accepted=[];checks=0;stop='ALL19_TERMINAL'

def r4(seeds):
 global checks
 d=bytearray([255])*len(adj);q=list(seeds)
 for s in seeds:d[s]=0
 for u in q:
  nd=d[u]+1
  if nd>4:break
  for v in adj[u]:
   if d[v]==255:d[v]=nd;q.append(v)
 checks+=1;return d

for item in items:
 begin=time.process_time()
 if begin-START>55:stop='UNKNOWN_CPU_LIMIT';break
 pins=item['pins'];N=len(adj)
 row=dict(pool_index=item['pool_index'],original_pool_index=item['original_pool_index'],
          last_failed_source_n=fail[item['pool_index']],source_n=N,source_m=m,
          mandatory_pins=pins,previously_accepted_indices=[r['pool_index'] for r in accepted])
 blocked=[v for v in pins if len(adj[v])>=11]
 if blocked:
  row.update(status='DEGREE_INFEASIBLE_CURRENT_BASE',blocked_pins=blocked,CPU_seconds=time.process_time()-begin)
  rows.append(row);continue
 d=r4(pins);missing=[v for v in range(N) if d[v]==255]
 row['mandatory_missing_targets']=missing
 possible=[v for v in range(N) if len(adj[v])<11 and v not in set(pins)]
 row['all_allowed_anchor_count']=len(possible)
 targets_used=[]
 for t in missing:
  if time.process_time()-START>55:stop='UNKNOWN_CPU_LIMIT';break
  ds=r4([t]);targets_used.append(t);possible=[a for a in possible if ds[a]<=4]
  if not possible:break
 if stop=='UNKNOWN_CPU_LIMIT':
  row.update(status='UNKNOWN_CPU_LIMIT',targets_used=targets_used,CPU_seconds=time.process_time()-begin)
  rows.append(row);break
 if missing and not possible:
  row.update(status='EXACT_NO_AT_MOST_ONE_ANCHOR_ON_THIS_BASE',
             empty_coverer_intersection_targets=targets_used,all_allowed_anchors_considered=True,
             CPU_seconds=time.process_time()-begin)
  rows.append(row);continue
 anchors=[] if not missing else [possible[0]];neighbors=sorted(pins+anchors)
 assert len(neighbors)==len(set(neighbors))<=11 and all(len(adj[v])<11 for v in neighbors)
 actual=r4(neighbors)
 assert all(x<=4 for x in actual)
 row.update(status='ACCEPTED_COMPLETE_CURRENT_EXTENSION',new_vertex=N,new_n=N+1,
            anchors=anchors,new_neighbors=neighbors,old_pin_degrees=[len(adj[v]) for v in neighbors],
            actual_current_R4_covered=N,actual_current_R4_missing=0,
            current_R4_depth_histogram=dict(Counter(actual)),
            geometric_witnesses=item['geometric_witnesses'],CPU_seconds=time.process_time()-begin)
 adj.append(neighbors.copy())
 for v in neighbors:adj[v].append(N)
 m+=len(neighbors);row['new_m']=m;rows.append(row);accepted.append(row)
 (OUT/'accepted_sequence.json').write_text(json.dumps(dict(initial_n=37631,accepted=accepted,
     final_n=len(adj),final_m=m,certificate='Actualdegree and completecurrentR4 at every step; no all-source recheck requested'),indent=2)+'\n')
 print('HIT '+json.dumps(dict(pool_index=row['pool_index'],source_n=N,new_n=N+1,
       new_neighbors=neighbors,anchors=anchors,CPU_seconds=time.process_time()-START)),flush=True)

result=dict(status=stop,initial_n=37631,initial_m=205329,final_n=len(adj),final_m=m,
            frozen_indices=plan['canonical_pool_indices'],items_terminal=sum(r['status']!='UNKNOWN_CPU_LIMIT' for r in rows),
            items_unattempted=len(items)-len(rows),rows=rows,accepted_count=len(accepted),
            accepted_orders=[r['new_n'] for r in accepted],radius4_checks=checks,
            allsource_BFS=0,newreview=0,secondanchor=0,oldcache_rejections=0,
            historical_graphs_modified=False,delivery38_modified=False,
            CPU_seconds=time.process_time()-START,pending=[])
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
if not accepted:(OUT/'accepted_sequence.json').write_text(json.dumps(dict(initial_n=37631,accepted=[],final_n=len(adj),final_m=m),indent=2)+'\n')
print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
