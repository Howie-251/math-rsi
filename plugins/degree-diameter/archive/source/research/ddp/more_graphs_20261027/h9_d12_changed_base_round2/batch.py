"""Exact sequential extensions from the592 new ten-pin Q-lines. One CPU."""
from pathlib import Path
import json
import resource
import time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(90,90))
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_extension_batch']
source=OUT.parent/'h9_d12_global_remainder/graphs/graph_d12_D5_n42391.edges'
with source.open() as stream:
 initial_n,initial_m=map(int,stream.readline().split());adj=[[] for _ in range(initial_n)]
 for line in stream:
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert initial_n==42391 and initial_m==245805 and max(map(len,adj))==12
for ns in adj:ns.sort()
allpool=json.loads((OUT.parent/'h9_global_line_pool_d12/pool.json').read_text())['records']
frozen=json.loads((OUT/'frozen_items.json').read_text())
items=[(r['pool_index'],allpool[r['pool_index']]) for r in frozen]
frozen_by_index={r['pool_index']:r for r in frozen}
assert all(item['pins']==frozen_by_index[i]['pins'] for i,item in items)
rows=[];accepted=[];current_m=initial_m;radius_checks=0;reverse_checks=0
stop_reason=None
target_cache={}
reverse_cache_hits=0

def r4(seeds):
 global radius_checks
 dist=bytearray([255])*len(adj);queue=list(seeds)
 for s in seeds:dist[s]=0
 for u in queue:
  d=dist[u]+1
  if d>4:break
  for v in adj[u]:
   if dist[v]==255:dist[v]=d;queue.append(v)
 radius_checks+=1;return dist

def path_from_anchor(a,t,ds):
 path=[a]
 while path[-1]!=t:
  u=path[-1];path.append(min(v for v in adj[u] if ds[v]+1==ds[u]))
 return path

def checkpoint():
 d=dict(initial_graph=str(source.relative_to(ROOT)),initial_n=initial_n,initial_m=initial_m,
        final_n=len(adj),final_m=current_m,target_Delta=12,target_D=5,
        accepted_extensions=len(accepted),records=accepted,
        root_final_independent_acceptance_pending=False)
 (OUT/'accepted_extensions.json').write_text(json.dumps(d,indent=2)+'\n')

def profile10():
 if len(rows)==10:
  p=dict(actual_rows=10,CPU_seconds=time.process_time()-START,
         accepted_extensions=len(accepted),current_n=len(adj),
         mandatory_R4_checks=sum('mandatory_R4_missing_count' in r for r in rows),
         reverse_R4_checks=reverse_checks,
         first_anchor_candidates_tested=sum(r.get('first_anchors_tested',0) for r in rows))
  (OUT/'profile10.json').write_text(json.dumps(p,indent=2)+'\n')
  print('PROFILE10 '+json.dumps(p),flush=True)

for ordinal,(pool_index,item) in enumerate(items):
 stepstart=time.process_time()
 if stepstart-START>82:stop_reason='CPU_LIMIT_UNPROCESSED_REMAINDER';break
 N=len(adj);pins=item['pins']
 row=dict(ordinal=ordinal,pool_index=pool_index,source_n=N,source_m=current_m,
          mandatory_pins=pins,mandatory_pin_current_degrees=[len(adj[v]) for v in pins],
          previously_accepted_pool_indices=[r['pool_index'] for r in accepted])
 row['last_evaluation']=frozen_by_index[pool_index]['last_evaluation']
 row['prior_accepted_line_vertices']=frozen_by_index[pool_index]['prior_accepted_line_vertices']
 row['multiple_line_vertex']=frozen_by_index[pool_index]['multiple_line_vertex_candidate']
 blocked=[v for v in pins if len(adj[v])>=12]
 if blocked:
  row.update(status='DEGREE_INFEASIBLE_ON_THIS_BASE',saturated_mandatory_pins=blocked,
             CPU_seconds=time.process_time()-stepstart)
  rows.append(row);profile10();continue
 mandatory=r4(pins)
 missing=[v for v in range(N) if mandatory[v]==255]
 row.update(mandatory_R4_missing=missing,mandatory_R4_missing_count=len(missing),
            mandatory_R4_allold_covered_count=N-len(missing))
 pinset=set(pins);available=[v for v in range(N) if len(adj[v])<12 and v not in pinset]
 row['allowed_anchors']=len(available);allbits=(1<<len(available))-1
 coverers={};distances={}
 for t in missing:
  if time.process_time()-START>82:stop_reason='CPU_LIMIT_PARTIAL_CURRENT_ITEM';break
  if t in target_cache:
   ds=target_cache[t];reverse_cache_hits+=1
  else:
   ds=bytes(r4([t]));reverse_checks+=1;target_cache[t]=ds
  bits=bytearray((len(available)+7)//8)
  for j,v in enumerate(available):
   if ds[v]<=4:bits[j>>3]|=1<<(j&7)
  coverers[t]=int.from_bytes(bits,'little');distances[t]=bytes(ds)
 if stop_reason:
  row.update(status='UNKNOWN_CPU_LIMIT',reverse_targets_completed=len(coverers),CPU_seconds=time.process_time()-stepstart)
  rows.append(row);profile10();break
 anchors=[] if not missing else None;firsttested=0
 if missing:
  order=sorted(missing,key=lambda t:(coverers[t].bit_count(),t));one=allbits
  for t in order:one&=coverers[t]
  row['one_anchor_exists']=bool(one)
  if one:anchors=[available[(one&-one).bit_length()-1]]
  else:
   cursor=allbits
   while cursor:
    if firsttested%128==0 and time.process_time()-START>82:stop_reason='CPU_LIMIT_PARTIAL_CURRENT_ITEM';break
    first=cursor&-cursor;cursor-=first;second=allbits&~first
    for t in order:
     if not (coverers[t]&first):
      second&=coverers[t]
      if not second:break
    firsttested+=1
    if second:
     anchors=[available[first.bit_length()-1],available[(second&-second).bit_length()-1]];break
 row['first_anchors_tested']=firsttested
 if stop_reason:
  row.update(status='UNKNOWN_CPU_LIMIT',CPU_seconds=time.process_time()-stepstart);rows.append(row);profile10();break
 if anchors is None:
  row.update(status='NO_AT_MOST_TWO_ANCHORS_ON_THIS_BASE',all_allowed_first_anchors_exhausted=True,
             CPU_seconds=time.process_time()-stepstart);rows.append(row);profile10();continue
 neighbors=sorted(pins+anchors)
 assert len(neighbors)==len(set(neighbors))<=12 and all(len(adj[v])<12 for v in neighbors)
 actual_positive=r4(neighbors)
 assert all(x<=4 for x in actual_positive)
 row.update(actual_current_R4_covered=N,actual_current_R4_missing=0)
 evidence=[]
 for t in missing:
  a=next(a for a in anchors if distances[t][a]<=4)
  evidence.append(dict(target=t,covering_anchor=a,old_base_distance=distances[t][a],path=path_from_anchor(a,t,distances[t])))
 row.update(status='ACCEPTED_ACTUAL_DEGREE_COMPLETE_R4',new_vertex=N,full_neighbor_set=neighbors,
            anchors=anchors,new_vertex_degree=len(neighbors),neighbors_old_degrees=[len(adj[v]) for v in neighbors],
            coverage_paths_for_mandatory_missing=evidence,alloldvertices_R4_covered=True,
            new_n=N+1,new_m=current_m+len(neighbors),CPU_seconds=time.process_time()-stepstart)
 (OUT/f"accepted_{len(accepted)+1:02d}_pool{pool_index}.json").write_text(json.dumps(row,indent=2)+'\n')
 target_cache.clear()
 adj.append(neighbors.copy())
 for v in neighbors:adj[v].append(N)
 current_m+=len(neighbors);rows.append(row);accepted.append(row)
 assert max(map(len,adj))<=12
 checkpoint();profile10()
 print('HIT '+json.dumps(dict(accepted=len(accepted),ordinal=ordinal,pool_index=pool_index,source_n=N,
       new_n=N+1,new_vertex=N,full_neighbor_set=neighbors,anchors=anchors,
       mandatory_missing=len(missing),total_CPU_seconds=time.process_time()-START)),flush=True)
 if len(accepted)==32:stop_reason='ACCEPTED32_REVIEW_POINT';break

if stop_reason is None:stop_reason='ALL_FROZEN_ITEMS_TERMINAL'
checkpoint()
terminal=sum(r['status']!='UNKNOWN_CPU_LIMIT' for r in rows)
result=dict(prediction_id='N12_CHANGED_BASE_ROUND2_ON_42391',status=stop_reason,
            initial_n=initial_n,initial_m=initial_m,final_n=len(adj),final_m=current_m,target_Delta=12,target_D=5,
            scope_items=len(items),rows_attempted=len(rows),items_terminal=terminal,items_unattempted=len(items)-len(rows),
            remaining_unknown_current_items=sum(r['status']=='UNKNOWN_CPU_LIMIT' for r in rows),
            rows=rows,accepted_extensions=len(accepted),
            accepted_pool_indices=[r['pool_index'] for r in accepted],
            mandatory_multisource_R4_checks=sum('mandatory_R4_missing_count' in r for r in rows),
            reverse_target_R4_checks=reverse_checks,reverse_target_R4_samebase_cache_hits=reverse_cache_hits,total_radius4_checks=radius_checks,
            allsource_BFS_executed=0,old7_pool_retested=False,eightpin_items_run=0,
            failed_earlier_items_retried=False,historical_graphs_modified=False,
            final_graph_generated_by_producer=False,CPU_seconds=time.process_time()-START,
            pending=[],
            scope_warning='Rejections apply only to their recorded current base; unattempted or partially processed items remain untested, not excluded.')
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)

# Deterministic delivery, without graphwide revalidation.
exec(compile((OUT/"deliver.py").read_text(),str(OUT/"deliver.py"),"exec"))
