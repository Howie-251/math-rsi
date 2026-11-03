"""One finite controlled9pin deletion batch with complete <=2anchor search."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
from pathlib import Path
from collections import Counter
import time,json,resource,sys
resource.setrlimit(resource.RLIMIT_CPU,(5,5));start=time.process_time();wall=time.perf_counter()
H=Path(__file__).resolve().parent;ROOT=H.parents[3];MORE=H.parent
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen

def save(name,obj):
 def texts(z):
  if isinstance(z,str):return[z]
  if isinstance(z,dict):return[t for v in z.values() for t in texts(v)]
  if isinstance(z,(list,tuple)):return[t for v in z for t in texts(v)]
  return[]
 assert not screen('\n'.join(texts(obj)));(H/name).write_text(json.dumps(obj,indent=2)+'\n')
assert not(H/'terminal.json').exists(),'Frozen batch already has terminal data'
source=MORE/'h9_d11_followups/graph_d11_D5_n37631.edges'
with source.open() as f:
 initial_n,initial_m=map(int,next(f).split());assert(initial_n,initial_m)==(37631,205329);actual=[[] for _ in range(initial_n)]
 for line in f:
  u,v=map(int,line.split());actual[u].append(v);actual[v].append(u)
# Recover all available radius4 balls to the exact current source.
cache=ROOT/'research/ddp/breadth_20261027_wave9/cooperative37630';cm=json.loads((cache/'coverage_cache.json').read_text());P=cm['eligible_vertices'];raw=(cache/'radius4.u64.bin').read_bytes();stride=588*8
adj=[[v for v in actual[u] if v<37628] for u in range(37628)];assert sum(map(len,adj))//2==205296
assert P==[v for v in range(37628) if len(adj[v])<11] and len(P)==2504 and len(raw)==len(P)*stride and cm['source_edges']==205296
full=(1<<37628)-1;balls={v:int.from_bytes(raw[i*stride:(i+1)*stride],'little')&full for i,v in enumerate(P)}

def layers(seeds,radius):
 d=[-1]*len(adj);q=[]
 for v in seeds:
  if d[v]<0:d[v]=0;q.append(v)
 for u in q:
  if d[u]==radius:continue
  nd=d[u]+1
  for v in adj[u]:
   if d[v]<0:d[v]=nd;q.append(v)
 return d,q

updates=[]
def append_exact(neighbors,d):
 global full,balls
 z=len(adj);bit=1<<z;masks=[0,0,0,0]
 for u,du in enumerate(d):
  if 0<=du<=3:
   bu=1<<u
   for r in range(du,4):masks[r]|=bu
 updated={}
 for a,b in balls.items():
  k=d[a]
  if 0<=k<=2:b|=masks[2-k]
  if 0<=k<=3:b|=bit
  updated[a]=b
 adj.append(list(neighbors))
 for v in neighbors:adj[v].append(z)
 balls={a:b for a,b in updated.items() if len(adj[a])<11}
 if len(neighbors)<11:balls[z]=masks[3]|bit
 full|=bit
 assert set(balls)=={v for v in range(len(adj)) if len(adj[v])<11}
 return z

for z in range(37628,initial_n):
 neighbors=sorted(actual[z]);assert len(neighbors)==11 and all(v<z for v in neighbors)
 d,q=layers(neighbors,3);append_exact(neighbors,d);updates.append(dict(new_vertex=z,neighbors=neighbors,depth=3))
assert all(sorted(adj[u])==sorted(actual[u]) for u in range(initial_n))
frozen=json.loads((H/'frozen_candidates.json').read_text())['frozen'];assert len(frozen)==17
save('cache_binding.json',dict(original_cache=str(cache.relative_to(ROOT)),original_n=37628,current_n=initial_n,current_m=initial_m,
 initial_available_R4_rows=len(balls),exact_append_updates=updates,all_current_adjacency_rows_match=True,
 formula='oldBall4(a) gains R_(2-k)(S) if k=d_old(a,S)<=2 and newz if k<=3; newBall4(z) is newz union R3_old(S).'))
import numpy as np
rows=[];accepted=[];current_m=initial_m;stop=None;coverers=None;Pcurrent=None;transpose_builds=0;first_tests=0;positive_checks=0

def build_coverers():
 global coverers,Pcurrent,transpose_builds
 Pcurrent=sorted(balls);width=(len(adj)+7)//8
 data=b''.join(balls[v].to_bytes(width,'little') for v in Pcurrent)
 matrix=np.unpackbits(np.frombuffer(data,dtype=np.uint8).reshape(len(Pcurrent),width),axis=1,bitorder='little')[:,:len(adj)]
 packed=np.packbits(matrix.T,axis=1,bitorder='little')
 coverers=[int.from_bytes(row.tobytes(),'little') for row in packed];transpose_builds+=1

for item in frozen:
 if time.process_time()-start>3.8:stop='CPU_WINDOW_UNPROCESSED_REMAINDER';break
 ts=time.process_time();pins=item['mandatory_pins'];n=len(adj);row=dict(frozen_index=item['frozen_index'],provenance=item['provenance'],mandatory_pins=pins,base_n=n,base_m=current_m)
 blocked=[p for p in pins if len(adj[p])>=11]
 assert all(len(adj[p])==11 for p in item['deleted_saturated_pins'])
 if blocked:
  row.update(status='CURRENT_DEGREE_BLOCKED',saturated_pins=blocked,CPU_seconds=time.process_time()-ts);rows.append(row);continue
 mandatory=0
 for p in pins:mandatory|=balls[p]
 missing=full&~mandatory;missing_targets=[];cursor=missing
 while cursor:
  low=cursor&-cursor;cursor-=low;missing_targets.append(low.bit_length()-1)
 row.update(mandatory_R4_missing_count=len(missing_targets),mandatory_R4_missing_targets=missing_targets)
 anchors=[] if not missing else None;tested=0
 if missing:
  if coverers is None:build_coverers()
  index={v:i for i,v in enumerate(Pcurrent)};allowed=(1<<len(Pcurrent))-1
  for p in pins:allowed&=~(1<<index[p])
  cr=sorted(((coverers[t]&allowed,t) for t in missing_targets),key=lambda p:(p[0].bit_count(),p[1]))
  row.update(allowed_anchor_count=allowed.bit_count(),minimum_target_anchor_coverers=cr[0][0].bit_count())
  one=allowed
  for c,t in cr:
   one&=c
   if not one:break
  if one:anchors=[Pcurrent[(one&-one).bit_length()-1]]
  elif cr[0][0]:
   # At least one member of every <=2cover must cover this rare target.
   firsts=cr[0][0]
   while firsts:
    if tested%32==0 and time.process_time()-start>3.8:stop='CPU_WINDOW_PARTIAL_CURRENT_ITEM';break
    a=firsts&-firsts;firsts-=a;second=allowed&~a
    for c,t in cr:
     if not(c&a):
      second&=c
      if not second:break
    tested+=1;first_tests+=1
    if second:anchors=sorted([Pcurrent[a.bit_length()-1],Pcurrent[(second&-second).bit_length()-1]]);break
 row['first_anchors_tested']=tested
 if stop:
  row.update(status='UNKNOWN_CPU_WINDOW',CPU_seconds=time.process_time()-ts);rows.append(row);break
 if anchors is None:
  row.update(status='EXACT_NO_AT_MOST_TWO_ANCHORS_ON_RECORDED_BASE',all_relevant_first_anchors_exhausted=True,CPU_seconds=time.process_time()-ts);rows.append(row);continue
 neighbors=sorted(pins+anchors);assert not(set(neighbors)&set(item['deleted_saturated_pins']));assert len(neighbors)==len(set(neighbors))<=11 and all(len(adj[v])<11 for v in neighbors)
 union=mandatory
 for a in anchors:union|=balls[a]
 assert union&full==full
 # One positive current-source R4 computation binds every accepted full neighborhood.
 d,q=layers(neighbors,4);positive_checks+=1;assert len(q)==n and min(d)>=0 and max(d)<=4
 row.update(status='COMPLETE_CURRENT_EXTENSION_AWAIT_ROOT',anchors=anchors,full_neighbor_set=neighbors,new_vertex=n,new_n=n+1,new_m=current_m+len(neighbors),
  neighbors_old_degrees=[len(adj[v]) for v in neighbors],new_vertex_degree=len(neighbors),all_current_old_R4_covered=n,missing_after_anchors=0,
  positive_actual_current_multisource_R4=True,R4_depth_histogram=dict(Counter(d)),CPU_seconds=time.process_time()-ts)
 append_exact(neighbors,d);current_m+=len(neighbors);accepted.append(row);rows.append(row);coverers=None
 save(f'accepted_{len(accepted):02d}.json',row)
 save('accepted_sequence.json',dict(initial_n=initial_n,initial_m=initial_m,source_file=str(source.relative_to(ROOT)),accepted=accepted,final_n=len(adj),final_m=current_m))
 if len(accepted)==1:save('first_hit.json',row)
 print('HIT '+json.dumps(dict(accepted=len(accepted),frozen_index=item['frozen_index'],provenance=item['provenance'],n=len(adj),full_neighbor_set=neighbors,anchors=anchors,CPU_seconds=time.process_time()-start)),flush=True)
 if len(accepted)>=17:stop='SEVENTEEN_ACCEPTANCE_REVIEW_POINT';break
 if len(rows)==10:save('profile10.json',dict(rows=10,CPU_seconds=time.process_time()-start,accepted=len(accepted),transpose_builds=transpose_builds,first_anchor_tests=first_tests))
if stop is None:stop='ALL_FROZEN_ITEMS_PROCESSED'
edge_file=None
if accepted:
 edge_file=f'graph_d11_D5_n{len(adj)}.edges';edges=[(u,v) for u,ns in enumerate(adj) for v in ns if u<v];assert len(edges)==current_m
 (H/edge_file).write_text(f'{len(adj)} {current_m}\n'+''.join(f'{u} {v}\n' for u,v in edges))
save('accepted_sequence.json',dict(initial_n=initial_n,initial_m=initial_m,source_file=str(source.relative_to(ROOT)),accepted=accepted,final_n=len(adj),final_m=current_m))
r=dict(status=stop,initial_n=initial_n,initial_m=initial_m,final_n=len(adj),final_m=current_m,target_Delta=11,target_D=5,
 raw_variants=17,initial_degree_blocked=0,frozen_items=17,items_processed=len(rows),items_unprocessed=17-len(rows),rows=rows,
 accepted_count=len(accepted),current_degree_blocked_count=sum(x['status']=='CURRENT_DEGREE_BLOCKED' for x in rows),
 exact_two_anchor_failures=sum(x['status']=='EXACT_NO_AT_MOST_TWO_ANCHORS_ON_RECORDED_BASE' for x in rows),
 unknown_current_items=sum(x['status']=='UNKNOWN_CPU_WINDOW' for x in rows),
 available_R4_transposes=transpose_builds,first_anchor_candidates_tested=first_tests,positive_current_R4_checks=positive_checks,
 final_edge_file=edge_file,final_max_degree=max(map(len,adj)),allsource_BFS=0,solver_calls=0,workers=1,
 CPU_seconds=time.process_time()-start,wall_seconds=time.perf_counter()-wall,extra_rounds=0,third_anchors=0,rejected_items_retried=False,
 source_and_verified_graphs_modified=False,root_unique_strongest_verification_pending=bool(accepted),
 scope='Only17global single-fault9pin images; negative rows apply to their recorded current base; no unprocessed item is excluded.')
save('RESULT.json',r);save('terminal.json',r);print('FINAL '+json.dumps({k:v for k,v in r.items() if k!='rows'}),flush=True)
