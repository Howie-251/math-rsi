"""Coreguard-first9pin+<=3 production; all CPU, including native children, charged."""
import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
import json,resource,subprocess,time
import numpy as np

OUT=Path(__file__).resolve().parent;BASE=OUT.parent;ROOT=OUT.parents[3]
START=time.process_time();initial_child=resource.getrusage(resource.RUSAGE_CHILDREN)
resource.setrlimit(resource.RLIMIT_CPU,(40,40))
load=lambda p:json.loads(p.read_text())
assert load(OUT/'PREDICTION.json')['frozen_before_checks']
freeze=load(OUT/'freeze_summary.json');items=load(OUT/'frozen_items.json')
NATIVE=BASE/'h9_d12_ninepin_saturated_deletion/cover'
source=BASE/'h9_d12_ninepin_saturated_deletion/graphs/graph_d12_D5_n42397.edges'
with source.open() as f:
 initial_n,initial_m=map(int,f.readline().split());adj=[[] for _ in range(initial_n)]
 for line in f:
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert (initial_n,initial_m)==(42397,245877)
current_file=source;current_m=initial_m;rows=[];accepted=[]
(OUT/'items').mkdir(exist_ok=True);(OUT/'graphs').mkdir(exist_ok=True)
def cpu():
 c=resource.getrusage(resource.RUSAGE_CHILDREN)
 return freeze['prepare_CPU_seconds']+time.process_time()-START+c.ru_utime+c.ru_stime-initial_child.ru_utime-initial_child.ru_stime
def bitindices(bits):
 while bits:
  low=bits&-bits;bits-=low;yield low.bit_length()-1
def guard_search(masks,missing,reps,deadline):
 C=sum(v<41356 for v in missing);E=len(missing)-C;cm=(1<<C)-1
 assert all(v<41356 for v in missing[:C]) and all(v>=41356 for v in missing[C:])
 guards=[i for i,m in enumerate(masks) if m&cm==cm]
 guards.sort(key=lambda i:(-(masks[i]>>C).bit_count(),reps[i]))
 stats=dict(core_holes=C,extra_holes=E,guard_distinct_fullmask_count=len(guards),
            guard_representative_examples=[reps[i] for i in guards[:8]],guards_tested=0,
            tail_second_masks_tested=0,complete_restricted_rule=False,limited=False)
 if not guards:stats['complete_restricted_rule']=True;return None,stats,'NO_SINGLE_CORE_GUARD_RULE_INAPPLICABLE'
 full=(1<<E)-1
 if not E:return [reps[guards[0]]],stats,'FOUND'
 projected={}
 for m,rep in zip(masks,reps):
  extra=m>>C
  if extra:projected[extra]=min(rep,projected.get(extra,rep))
 tail=sorted((rep,m) for m,rep in projected.items());labels=[p[0] for p in tail];ms=[p[1] for p in tail]
 K=len(ms);width=(E+7)//8;raw=b''.join(m.to_bytes(width,'little') for m in ms)
 bits=np.unpackbits(np.frombuffer(raw,dtype=np.uint8).reshape(K,width),axis=1,bitorder='little')[:,:E]
 packed=np.packbits(bits.T,axis=1,bitorder='little');coverers=[int.from_bytes(r.tobytes(),'little') for r in packed]
 order=sorted(range(E),key=lambda j:(coverers[j].bit_count(),j));allbits=(1<<K)-1
 label_index={v:i for i,v in enumerate(labels)}
 for guard in guards:
  if cpu()>deadline:stats['limited']=True;return None,stats,'UNKNOWN_ITEM_COREGUARD_TAIL_LIMIT'
  stats['guards_tested']+=1;g=reps[guard];left=full&~(masks[guard]>>C)
  if not left:return[g],stats,'FOUND'
  allowed=allbits&~(1<<label_index[g]) if g in label_index else allbits
  one=allowed
  for j in order:
   if left>>j&1:
    one&=coverers[j]
    if not one:break
  if one:return[g,labels[(one&-one).bit_length()-1]],stats,'FOUND'
  pivot=next(j for j in order if left>>j&1)
  seconds=sorted(bitindices(coverers[pivot]&allowed),key=lambda i:(-(ms[i]&left).bit_count(),labels[i]))
  for second in seconds:
   if stats['tail_second_masks_tested']%8==0 and cpu()>deadline:
    stats['limited']=True;return None,stats,'UNKNOWN_ITEM_COREGUARD_TAIL_LIMIT'
   stats['tail_second_masks_tested']+=1;res=left&~ms[second]
   if not res:return[g,labels[second]],stats,'FOUND'
   third=allowed&~(1<<second)
   for j in order:
    if res>>j&1:
     third&=coverers[j]
     if not third:break
   if third:return[g,labels[second],labels[(third&-third).bit_length()-1]],stats,'FOUND'
 stats['complete_restricted_rule']=True
 return None,stats,'EXACT_NO_COREGUARD_PLUS_TWO_TAIL_RESTRICTED_RULE'
def checkpoint():
 (OUT/'accepted_extensions.json').write_text(json.dumps(dict(initial_n=initial_n,initial_m=initial_m,
   final_n=len(adj),final_m=current_m,records=accepted,parent_pending=False),indent=2)+'\n')
status='ALL_FROZEN_ITEMS_VISITED';native_calls=0
for ordinal,item in enumerate(items):
 if 40-cpu()<1.8:status='TOTAL_CPU_RESERVE_STOP';break
 begin=cpu();pins=item['mandatory_pins'];row=dict(**item,ordinal=ordinal,source_n=len(adj),source_m=current_m)
 blocked=[p for p in pins if len(adj[p])>=12]
 if blocked:row.update(status='CURRENT_DEGREE_BLOCKED',blocked_pins=blocked,item_CPU_seconds=cpu()-begin);rows.append(row);continue
 prefix=OUT/'items'/f'ord{ordinal:03d}_pool{item["pool_index"]}_n{len(adj)}';pf=Path(str(prefix)+'.pins.txt')
 pf.write_text(' '.join(map(str,pins))+'\n')
 try:
  ret=subprocess.run([str(NATIVE),'prepare',str(current_file),str(pf),str(prefix)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=.60)
  native_calls+=1
  if ret.returncode:raise RuntimeError('native item limit')
  prep=load(Path(str(prefix)+'.json'))
 except (subprocess.TimeoutExpired,RuntimeError,json.JSONDecodeError):
  row.update(status='UNKNOWN_NATIVE_ITEM_LIMIT',item_CPU_seconds=cpu()-begin);rows.append(row);continue
 row.update(native_prepare_file=str(Path(str(prefix)+'.json').relative_to(ROOT)),native_prepare_CPU_seconds=prep['CPU_seconds'],mandatory_missing=prep['missing_count'])
 anchors=[] if not prep['missing_count'] else None
 if anchors is None:
  W=8*prep['mask_words_per_row'];raw=Path(str(prefix)+'.masks.u64.bin').read_bytes()
  masks=[int.from_bytes(raw[i:i+W],'little') for i in range(0,len(raw),W)]
  anchors,stats,verdict=guard_search(masks,prep['missing'],prep['representatives'],min(begin+.61,38.0))
  row['coreguard_search']=stats
 else:verdict='FOUND'
 if anchors is None:row.update(status=verdict,item_CPU_seconds=cpu()-begin);rows.append(row)
 else:
  neighbors=sorted(pins+anchors)
  assert len(neighbors)==len(set(neighbors))<=12 and all(len(adj[v])<12 for v in neighbors)
  assert item['deleted_saturated_pin'] not in neighbors
  pf.write_text(' '.join(map(str,neighbors))+'\n');selected=Path(str(prefix)+'_selected')
  ret=subprocess.run([str(NATIVE),'verify',str(current_file),str(pf),str(selected)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=.30);native_calls+=1
  assert ret.returncode==0;check=load(Path(str(selected)+'.json'))
  assert check['missing_count']==0 and all(d<12 for d in check['pin_current_degrees'])
  row.update(status='ACCEPTED_ACTUAL_DEGREE_COMPLETE_R4',new_vertex=len(adj),full_neighbor_set=neighbors,
   anchors=anchors,neighbors_old_degrees=check['pin_current_degrees'],new_vertex_degree=len(neighbors),
   actual_current_R4_covered=len(adj),actual_current_R4_missing=0,new_n=len(adj)+1,new_m=current_m+len(neighbors),
   native_verify_file=str(Path(str(selected)+'.json').relative_to(ROOT)))
  adj.append(neighbors.copy())
  for v in neighbors:adj[v].append(len(adj)-1)
  current_m+=len(neighbors);current_file=OUT/'graphs'/f'graph_d12_D5_n{len(adj)}.edges'
  with current_file.open('w') as f:
   f.write(f'{len(adj)} {current_m}\n')
   for u,ns in enumerate(adj):
    for v in ns:
     if u<v:f.write(f'{u} {v}\n')
  row.update(graph_file=str(current_file.relative_to(ROOT)),item_CPU_seconds=cpu()-begin)
  rows.append(row);accepted.append(row);checkpoint()
  print('HIT '+json.dumps(dict(accepted=len(accepted),pool_index=item['pool_index'],new_n=len(adj),anchors=anchors,CPU_total=cpu())),flush=True)
 if len(rows)==10:print('PROFILE10 '+json.dumps(dict(rows=10,accepted=len(accepted),CPU_total=cpu())),flush=True)
 if len(accepted)==16:status='SIXTEEN_ACCEPTED_REVIEW_POINT';break
checkpoint()
result=dict(status=status,initial_n=initial_n,initial_m=initial_m,final_n=len(adj),final_m=current_m,
 frozen_items=len(items),items_visited=len(rows),items_unattempted=len(items)-len(rows),rows=rows,records=accepted,
 accepted_extensions=len(accepted),final_graph=str(current_file.relative_to(ROOT)),native_calls=native_calls,
 total_parent_plus_children_CPU_seconds=cpu(),max_item_CPU_seconds=max((r['item_CPU_seconds'] for r in rows),default=0),
 allsource_BFS=0,MIP=0,externalreview=0,restricted_rule_only=True,general_three_anchor_family_excluded=False,pending=[])
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k not in ['rows','records']}),flush=True)
if accepted:exec(compile((OUT/'deliver.py').read_text(),str(OUT/'deliver.py'),'exec'))
