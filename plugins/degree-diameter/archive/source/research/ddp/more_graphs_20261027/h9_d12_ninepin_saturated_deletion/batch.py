"""Bounded9pin saturated-deletion production with <=3freeoldanchors."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
import resource,time,json,subprocess,sys
resource.setrlimit(resource.RLIMIT_CPU,(35,36))
H=Path(__file__).resolve().parent;ROOT=H.parents[3];START=time.process_time();WALL=time.perf_counter()
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen

def cpu():
 c=resource.getrusage(resource.RUSAGE_CHILDREN);return time.process_time()-START+c.ru_utime+c.ru_stime

def save(path,data):
 def text(z):
  if isinstance(z,str):return[z]
  if isinstance(z,dict):return[t for v in z.values() for t in text(v)]
  if isinstance(z,(list,tuple)):return[t for v in z for t in text(v)]
  return[]
 assert not screen('\n'.join(text(data)));path.write_text(json.dumps(data,indent=2)+'\n')
assert not(H/'terminal.json').exists(),'Fixed64candidate batch already terminal'
frozen=json.loads((H/'frozen64.json').read_text());items=frozen['selected64'];assert len(items)==64
source=ROOT/frozen['initial_source'];current_file=source
with source.open() as f:
 initial_n,initial_m=map(int,next(f).split());assert(initial_n,initial_m)==(42396,245865);adj=[[] for _ in range(initial_n)]
 for line in f:
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert max(map(len,adj))==12
(H/'items').mkdir(exist_ok=True);(H/'graphs').mkdir(exist_ok=True)
import numpy as np

# Complete <=2tail on a fixed residual, subject only to the explicit deadline.
def three_search(masks,T,deadline):
 K=len(masks);full=(1<<T)-1;allbits=(1<<K)-1
 width=(T+7)//8;raw=b''.join(m.to_bytes(width,'little') for m in masks)
 bits=np.unpackbits(np.frombuffer(raw,dtype=np.uint8).reshape(K,width),axis=1,bitorder='little')[:,:T]
 packed=np.packbits(bits.T,axis=1,bitorder='little');coverers=[int.from_bytes(r.tobytes(),'little') for r in packed]
 order=sorted(range(T),key=lambda j:(coverers[j].bit_count(),j));pivot=order[0]
 if not coverers[pivot]:return None,0,0,False
 firstidx=[];rem=coverers[pivot]
 while rem:
  low=rem&-rem;rem-=low;firstidx.append(low.bit_length()-1)
 firstidx.sort(key=lambda i:(-masks[i].bit_count(),i));firsttested=0;tailtested=0
 for a in firstidx:
  if cpu()>deadline:return None,firsttested,tailtested,True
  firsttested+=1;left=full&~masks[a]
  if not left:return[a],firsttested,tailtested,False
  available=allbits&~(1<<a);one=available
  for j in order:
   if (left>>j)&1:
    one&=coverers[j]
    if not one:break
  if one:return[a,(one&-one).bit_length()-1],firsttested,tailtested,False
  pivot2=next(j for j in order if (left>>j)&1);secondbits=coverers[pivot2]&available;seconds=[]
  while secondbits:
   low=secondbits&-secondbits;secondbits-=low;seconds.append(low.bit_length()-1)
  seconds.sort(key=lambda b:(-(masks[b]&left).bit_count(),b))
  for b in seconds:
   if tailtested%8==0 and cpu()>deadline:return None,firsttested,tailtested,True
   tailtested+=1;residue=left&~masks[b]
   if not residue:return[a,b],firsttested,tailtested,False
   last=available&~(1<<b)
   for j in order:
    if (residue>>j)&1:
     last&=coverers[j]
     if not last:break
   if last:return[a,b,(last&-last).bit_length()-1],firsttested,tailtested,False
 return None,firsttested,tailtested,False

rows=[];accepted=[];current_m=initial_m;stop=None;native_calls=0
for item in items:
 if cpu()>32:stop='TOTAL_CPU_WINDOW_REMAINDER_UNTESTED';break
 begin=cpu();pins=item['mandatory_pins'];row=dict(**item,source_n=len(adj),source_m=current_m)
 blocked=[p for p in pins if len(adj[p])>=12]
 if blocked:
  row.update(status='CURRENT_MANDATORY_DEGREE_BLOCKED',saturated_pins=blocked,CPU_seconds=cpu()-begin);rows.append(row);continue
 assert len(adj[item['deleted_saturated_pin']])==12 and item['deleted_saturated_pin'] not in pins
 prefix=H/'items'/f"ord{item['ordinal']:03d}_pool{item['pool_index']}_n{len(adj)}";pf=Path(str(prefix)+'.pins.txt');pf.write_text(' '.join(map(str,pins))+'\n')
 try:
  prep=subprocess.run([str(H/'cover'),'prepare',str(current_file),str(pf),str(prefix)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=2)
  native_calls+=1
  if prep.returncode:raise RuntimeError('Native preparation exited before complete output')
  d=json.loads(Path(str(prefix)+'.json').read_text())
 except (subprocess.TimeoutExpired,RuntimeError,json.JSONDecodeError):
  row.update(status='UNKNOWN_NATIVE_PREPARATION_ITEM_LIMIT',CPU_seconds=cpu()-begin);rows.append(row);continue
 assert d['source_n']==len(adj) and d['source_m']==current_m and d['pins']==pins
 row.update(mandatory_missing=d['missing_count'],eligible_anchors=d.get('eligible_anchors'),exact_two_complete=d.get('exact_two_complete'),
 exact_one_or_two_found=d.get('exact_one_or_two_found'),native_prepare_CPU_seconds=d['CPU_seconds'])
 anchors=[] if d['missing_count']==0 else d.get('exact_anchors') if d.get('exact_one_or_two_found') else None
 if anchors is None and d.get('zero_cover_targets'):
  row.update(status='EXACT_ZERO_ELIGIBLE_COVERER_TARGET',zero_cover_targets=d['zero_cover_targets'],CPU_seconds=cpu()-begin);rows.append(row);continue
 if anchors is None:
  W=d['mask_words_per_row'];raw=Path(str(prefix)+'.masks.u64.bin').read_bytes();assert len(raw)==8*W*len(d['representatives'])
  masks=[int.from_bytes(raw[i:i+8*W],'little') for i in range(0,len(raw),8*W)]
  deadline=min(begin+.72,32.)
  if cpu()>=deadline:chosen=None;firsts=tails=0;limited=True
  else:chosen,firsts,tails,limited=three_search(masks,d['missing_count'],deadline)
  row.update(first_anchors_tested=firsts,exact_tail_second_anchors_tested=tails,search_limit_reached=limited)
  if chosen is not None:anchors=sorted(d['representatives'][i] for i in chosen)
 if anchors is None:
  row.update(status='LIMITED_NO_HIT_THREE_ANCHOR_FEASIBILITY_OPEN',CPU_seconds=cpu()-begin);rows.append(row);continue
 neighbors=sorted(pins+anchors);assert len(neighbors)==len(set(neighbors))<=12 and all(len(adj[v])<12 for v in neighbors)
 assert item['deleted_saturated_pin'] not in neighbors
 pf.write_text(' '.join(map(str,neighbors))+'\n');selected=Path(str(prefix)+'_selected')
 check=subprocess.run([str(H/'cover'),'verify',str(current_file),str(pf),str(selected)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=2);native_calls+=1
 assert check.returncode==0
 good=json.loads(Path(str(selected)+'.json').read_text());assert good['status']=='FULL_SELECTED_R4_CHECK_COMPLETE' and good['missing_count']==0
 old_n=len(adj);row.update(status='ACCEPTED_COMPLETE_CURRENT_R4',anchors=anchors,full_neighbor_set=neighbors,new_vertex=old_n,new_n=old_n+1,
 new_m=current_m+len(neighbors),old_neighbor_degrees=[len(adj[v]) for v in neighbors],new_vertex_degree=len(neighbors),covered_old_vertices=old_n,
 actual_current_R4_missing=0,native_verify_file=str(Path(str(selected)+'.json').relative_to(ROOT)))
 adj.append(neighbors)
 for v in neighbors:adj[v].append(old_n)
 current_m+=len(neighbors);current_file=H/'graphs'/f'graph_d12_D5_n{len(adj)}.edges'
 with current_file.open('w') as out:
  out.write(f'{len(adj)} {current_m}\n')
  for u,ns in enumerate(adj):
   for v in ns:
    if u<v:out.write(f'{u} {v}\n')
 row.update(graph_file=str(current_file.relative_to(ROOT)),CPU_seconds=cpu()-begin);accepted.append(row);rows.append(row)
 save(H/f'accepted_{len(accepted):02d}.json',row)
 save(H/'accepted_extensions.json',dict(source_graph=str(source.relative_to(ROOT)),initial_n=initial_n,initial_m=initial_m,records=accepted,final_n=len(adj),final_m=current_m))
 if len(accepted)==1:save(H/'first_hit.json',row)
 print('HIT '+json.dumps(dict(accepted=len(accepted),ordinal=item['ordinal'],pool_index=item['pool_index'],n=len(adj),neighbors=neighbors,anchors=anchors,CPU_seconds=cpu())),flush=True)
 if len(accepted)>=16:stop='SIXTEEN_ACCEPTANCE_REVIEW_POINT';break
 if cpu()>32:stop='TOTAL_CPU_WINDOW_REMAINDER_UNTESTED';break
if stop is None:stop='ALL64_FROZEN_ITEMS_VISITED'
save(H/'accepted_extensions.json',dict(source_graph=str(source.relative_to(ROOT)),initial_n=initial_n,initial_m=initial_m,records=accepted,final_n=len(adj),final_m=current_m))
r=dict(status=stop,initial_n=initial_n,initial_m=initial_m,final_n=len(adj),final_m=current_m,target_Delta=12,target_D=5,
 source_graph=str(source.relative_to(ROOT)),final_graph=str(current_file.relative_to(ROOT)),scope126=126,frozen64=64,rows_visited=len(rows),
 unvisited_frozen=64-len(rows),outside_frozen_unattempted=62,accepted_count=len(accepted),records=accepted,rows=rows,
 limited_nohit_items=sum(x['status']=='LIMITED_NO_HIT_THREE_ANCHOR_FEASIBILITY_OPEN' for x in rows),
 unknown_preparations=sum(x['status']=='UNKNOWN_NATIVE_PREPARATION_ITEM_LIMIT' for x in rows),current_degree_blocked=sum(x['status']=='CURRENT_MANDATORY_DEGREE_BLOCKED' for x in rows),
 native_calls=native_calls,CPU_seconds_parent_and_children=cpu(),wall_seconds=time.perf_counter()-WALL,compile_CPU_not_in_batch_counter=True,
 global_budget40_including_compile=True,allsource_BFS=0,solver_calls=0,full_coverage_acceptance=True,three_anchor_nohit_is_not_infeasibility=True,
 extra_rounds=0,fourth_anchors=0,root_final_strongest_check_pending=bool(accepted))
save(H/'RESULT.json',r);save(H/'terminal.json',r);print('FINAL '+json.dumps({k:v for k,v in r.items() if k not in ['rows','records']}),flush=True)
