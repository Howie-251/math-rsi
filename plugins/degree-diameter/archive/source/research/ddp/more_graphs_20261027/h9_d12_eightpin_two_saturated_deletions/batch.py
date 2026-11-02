"""Two complementary core repairs then exacttwo extra-tail; fixed29 production."""
import time,resource
initial_child=resource.getrusage(resource.RUSAGE_CHILDREN)
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
import json,subprocess
import numpy as np

OUT=Path(__file__).resolve().parent;BASE=OUT.parent;ROOT=OUT.parents[3]
load=lambda p:json.loads(p.read_text())
plan=load(OUT/'PREDICTION.json');assert plan['frozen_before_checks']
freeze=load(OUT/'freeze_summary.json');items=load(OUT/'frozen_items.json')
resource.setrlimit(resource.RLIMIT_CPU,(30,30))
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
 return freeze['prepare_CPU_seconds']+time.process_time()+c.ru_utime+c.ru_stime-initial_child.ru_utime-initial_child.ru_stime
def indices(bits):
 while bits:
  low=bits&-bits;bits-=low;yield low.bit_length()-1
def repair(masks,missing,reps,counts,deadline):
 C=sum(v<41356 for v in missing);E=len(missing)-C;core=(1<<C)-1;extra=(1<<E)-1
 stats=dict(core_holes=C,extra_holes=E,first_prefix_limit=16,second_prefix_limit=8,
   firsts_tested=0,core_repair_pairs_tested=0,nontrivial_complementary_core_pairs=0,
   exact_tail_first_masks_tested=0,limited=False,all_selected_prefixes_exhausted=False)
 if not missing:return [],stats
 pivot=min(range(C),key=lambda j:(counts[j],missing[j])) if C else min(range(len(missing)),key=lambda j:(counts[j],missing[j]))
 firsts=[i for i,m in enumerate(masks) if m>>pivot&1]
 firsts.sort(key=lambda i:(-(masks[i]&core).bit_count(),-(masks[i]>>C).bit_count(),reps[i]))
 firsts=firsts[:16];stats.update(rare_first_target=missing[pivot],first_prefixes_selected=len(firsts))
 projected={}
 for m,rep in zip(masks,reps):
  ex=m>>C
  if ex:projected[ex]=min(rep,projected.get(ex,rep))
 tails=sorted((rep,m) for m,rep in projected.items());labels=[p for p,m in tails];ms=[m for p,m in tails];K=len(ms)
 if E:
  width=(E+7)//8;raw=b''.join(m.to_bytes(width,'little') for m in ms)
  bits=np.unpackbits(np.frombuffer(raw,dtype=np.uint8).reshape(K,width),axis=1,bitorder='little')[:,:E]
  packed=np.packbits(bits.T,axis=1,bitorder='little');coverers=[int.from_bytes(r.tobytes(),'little') for r in packed]
  order=sorted(range(E),key=lambda j:(coverers[j].bit_count(),j))
 else:coverers=[];order=[]
 allbits=(1<<K)-1;label_index={v:i for i,v in enumerate(labels)}
 def expired():return cpu()>deadline
 for first in firsts:
  if expired():stats['limited']=True;return None,stats
  stats['firsts_tested']+=1;leftcore=core&~masks[first];leftextra=extra&~(masks[first]>>C)
  secondlist=[i for i,m in enumerate(masks) if i!=first and m&leftcore==leftcore]
  secondlist.sort(key=lambda i:(-((masks[i]>>C)&leftextra).bit_count(),reps[i]));secondlist=secondlist[:8]
  for second in secondlist:
   if expired():stats['limited']=True;return None,stats
   stats['core_repair_pairs_tested']+=1
   if leftcore:stats['nontrivial_complementary_core_pairs']+=1
   pair=[reps[first],reps[second]];res=extra&~((masks[first]|masks[second])>>C)
   if not res:return pair,stats
   allowed=allbits
   for a in pair:
    if a in label_index:allowed&=~(1<<label_index[a])
   one=allowed
   for j in order:
    if res>>j&1:
     one&=coverers[j]
     if not one:break
   if one:return pair+[labels[(one&-one).bit_length()-1]],stats
   target=next(j for j in order if res>>j&1)
   thirdlist=sorted(indices(coverers[target]&allowed),key=lambda i:(-(ms[i]&res).bit_count(),labels[i]))
   for third in thirdlist:
    if stats['exact_tail_first_masks_tested']%8==0 and expired():stats['limited']=True;return None,stats
    stats['exact_tail_first_masks_tested']+=1;left=res&~ms[third]
    if not left:return pair+[labels[third]],stats
    last=allowed&~(1<<third)
    for j in order:
     if left>>j&1:
      last&=coverers[j]
      if not last:break
    if last:return pair+[labels[third],labels[(last&-last).bit_length()-1]],stats
 stats['all_selected_prefixes_exhausted']=True;return None,stats

status='ALL_FROZEN29_ITEMS_VISITED';native_calls=0
for ordinal,item in enumerate(items):
 if 30-cpu()<1.8:status='TOTAL_CPU_RESERVE_STOP';break
 begin=cpu();pins=item['mandatory_pins'];row=dict(**item,ordinal=ordinal,source_n=len(adj),source_m=current_m)
 blocked=[v for v in pins if len(adj[v])>=12]
 if blocked:row.update(status='CURRENT_DEGREE_BLOCKED',blocked_pins=blocked,item_CPU_seconds=cpu()-begin);rows.append(row);continue
 prefix=OUT/'items'/f'ord{ordinal:02d}_pool{item["pool_index"]}_n{len(adj)}';pf=Path(str(prefix)+'.pins.txt');pf.write_text(' '.join(map(str,pins))+'\n')
 try:
  ret=subprocess.run([str(NATIVE),'prepare',str(current_file),str(pf),str(prefix)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=.58);native_calls+=1
  if ret.returncode:raise RuntimeError('native itemlimit')
  prep=load(Path(str(prefix)+'.json'))
 except (subprocess.TimeoutExpired,RuntimeError,json.JSONDecodeError):
  row.update(status='UNKNOWN_NATIVE_ITEM_LIMIT',item_CPU_seconds=cpu()-begin);rows.append(row);continue
 row.update(mandatory_missing=prep['missing_count'],native_prepare_CPU_seconds=prep['CPU_seconds'],native_prepare_file=str(Path(str(prefix)+'.json').relative_to(ROOT)))
 anchors=[] if not prep['missing_count'] else prep.get('exact_anchors') if prep.get('exact_one_or_two_found') else None
 if anchors is None:
  W=8*prep['mask_words_per_row'];raw=Path(str(prefix)+'.masks.u64.bin').read_bytes();masks=[int.from_bytes(raw[i:i+W],'little') for i in range(0,len(raw),W)]
  anchors,stats=repair(masks,prep['missing'],prep['representatives'],prep['target_coverage_counts'],min(begin+.61,28.0))
  row['two_core_repair']=stats
 if anchors is None:row.update(status='UNKNOWN_PREFIX_ITEM_LIMIT' if stats['limited'] else 'FINITE_TWO_CORE_PREFIX_NO_HIT',item_CPU_seconds=cpu()-begin);rows.append(row)
 else:
  neighbors=sorted(pins+anchors)
  assert len(neighbors)==len(set(neighbors))<=12 and all(len(adj[v])<12 for v in neighbors)
  assert not set(item['deleted_saturated_pins'])&set(neighbors)
  pf.write_text(' '.join(map(str,neighbors))+'\n');selected=Path(str(prefix)+'_selected')
  ret=subprocess.run([str(NATIVE),'verify',str(current_file),str(pf),str(selected)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=.30);native_calls+=1
  assert ret.returncode==0;check=load(Path(str(selected)+'.json'));assert check['missing_count']==0 and max(check['pin_current_degrees'])<12
  row.update(status='ACCEPTED_ACTUAL_DEGREE_COMPLETE_R4',new_vertex=len(adj),full_neighbor_set=neighbors,anchors=anchors,
   neighbors_old_degrees=check['pin_current_degrees'],new_vertex_degree=len(neighbors),new_n=len(adj)+1,new_m=current_m+len(neighbors),
   actual_current_R4_covered=len(adj),actual_current_R4_missing=0,native_verify_file=str(Path(str(selected)+'.json').relative_to(ROOT)))
  adj.append(neighbors.copy())
  for v in neighbors:adj[v].append(len(adj)-1)
  current_m+=len(neighbors);current_file=OUT/'graphs'/f'graph_d12_D5_n{len(adj)}.edges'
  with current_file.open('w') as f:
   f.write(f'{len(adj)} {current_m}\n')
   for u,ns in enumerate(adj):
    for v in ns:
     if u<v:f.write(f'{u} {v}\n')
  row.update(graph_file=str(current_file.relative_to(ROOT)),item_CPU_seconds=cpu()-begin);rows.append(row);accepted.append(row)
  (OUT/'accepted_extensions.json').write_text(json.dumps(dict(initial_n=initial_n,records=accepted,final_n=len(adj),final_m=current_m),indent=2)+'\n')
  print('HIT '+json.dumps(dict(pool_index=item['pool_index'],n=len(adj),anchors=anchors,CPU_total=cpu())),flush=True)
 if len(rows)==10:print('PROFILE10 '+json.dumps(dict(rows=10,accepted=len(accepted),CPU_total=cpu())),flush=True)
 if len(accepted)==16:status='SIXTEEN_ACCEPTED_REVIEW_POINT';break
(OUT/'accepted_extensions.json').write_text(json.dumps(dict(initial_n=initial_n,records=accepted,final_n=len(adj),final_m=current_m),indent=2)+'\n')
result=dict(status=status,initial_n=initial_n,initial_m=initial_m,final_n=len(adj),final_m=current_m,
 frozen_items=len(items),items_visited=len(rows),items_unattempted=len(items)-len(rows),rows=rows,records=accepted,accepted_extensions=len(accepted),
 final_graph=str(current_file.relative_to(ROOT)),native_calls=native_calls,total_parent_plus_children_CPU_seconds=cpu(),
 max_item_CPU_seconds=max((r['item_CPU_seconds'] for r in rows),default=0),allsource_BFS=0,MIP=0,externalreview=0,
 general_four_anchor_feasibility_excluded=False,pending=[])
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k not in ['rows','records']}),flush=True)
if accepted:
 text=(BASE/'h9_d12_ninepin_coreguard/deliver.py').read_text()
 text=text.replace('h9_d12_ninepin_coreguard','h9_d12_eightpin_two_saturated_deletions')
 text=text.replace("deleted_saturated_pin=r['deleted_saturated_pin']","deleted_saturated_pins=r['deleted_saturated_pins']")
 text=text.replace('Oneeligiblecoreguard plus exactatmosttwo extra-complement anchors','Two complementary core repairs plus exactatmosttwo extra-tail anchors')
 text=text.replace('Nine-point subset','Eight-point subset').replace('coreguard-first','two-core-repair').replace('Coreguard-first9pin+atmost3anchors','Two-saturated-deletion8pin+atmost4anchors')
 exec(compile(text,str(OUT/'deliver.py'),'exec'))
