"""Two fixed8pin items: forced raretarget prefixes plus exacttwo tail."""
from pathlib import Path
import json
import resource
import subprocess
import time

OUT=Path(__file__).resolve().parent;BASE=OUT.parent;ROOT=OUT.parents[3]
START=time.process_time();initial_child=resource.getrusage(resource.RUSAGE_CHILDREN)
resource.setrlimit(resource.RLIMIT_CPU,(20,20))
load=lambda p:json.loads(p.read_text())
plan=load(OUT/'PREDICTION.json');assert plan['frozen_before_actual_checks']
NATIVE=BASE/'h9_d12_eightpin_extensions/cover'
source=BASE/'h9_d12_eightpin_constructive/graphs/graph_d12_D5_n42396.edges'
with source.open() as f:
 initial_n,initial_m=map(int,f.readline().split());adj=[[] for _ in range(initial_n)]
 for line in f:
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert (initial_n,initial_m)==(42396,245865)
allpool=load(BASE/'h9_global_line_pool_d12/pool.json')['records']
previous={r['pool_index']:r for r in load(BASE/'h9_d12_eightpin_constructive/RESULT.json')['rows']}
current_file=source;current_m=initial_m;rows=[];accepted=[]
(OUT/'items').mkdir(exist_ok=True);(OUT/'graphs').mkdir(exist_ok=True)
def cpu():
 c=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-START+c.ru_utime+c.ru_stime-initial_child.ru_utime-initial_child.ru_stime
def indices(bits):
 while bits:
  low=bits&-bits;bits-=low;yield low.bit_length()-1
def search(masks,targets,reps,seconds):
 start=time.process_time();full=(1<<targets)-1;K=len(masks);coverers=[0]*targets
 for i,m in enumerate(masks):
  for j in indices(m):coverers[j]|=1<<i
 counts=[c.bit_count() for c in coverers];order=sorted(range(targets),key=lambda j:(counts[j],j))
 groups={}
 for j in order:groups[counts[j]]=groups.get(counts[j],0)|(1<<j)
 groups=list(groups.values());rare=order[0];rare_set=coverers[rare]
 stats=dict(rare_target_index=rare,rare_target_unique_coverers=counts[rare],first_coverer_set_size=rare_set.bit_count(),
            first_prefix_limit=32,second_prefix_limit=16,prefixes_tested=0,third_masks_tested=0,
            search_CPU_limit_reached=False,all_selected_prefixes_exhausted=False)
 if not rare_set:return None,stats
 def expired():return time.process_time()-start>seconds or cpu()>18.2
 def key(i,left):
  m=masks[i]&left
  return tuple(-(m&g).bit_count() for g in groups)+(-m.bit_count(),reps[i])
 firsts=sorted(indices(rare_set),key=lambda i:key(i,full))[:32]
 stats['first_prefixes_selected']=len(firsts);allbits=(1<<K)-1
 for first in firsts:
  if expired():stats['search_CPU_limit_reached']=True;return None,stats
  left=full&~masks[first]
  if not left:return [first],stats
  pivot=next(j for j in order if left>>j&1)
  seconds_ids=coverers[pivot]&~(1<<first)
  seconds_list=sorted(indices(seconds_ids),key=lambda i:key(i,left))[:16]
  for second in seconds_list:
   if expired():stats['search_CPU_limit_reached']=True;return None,stats
   stats['prefixes_tested']+=1;left2=left&~masks[second]
   if not left2:return [first,second],stats
   pivot=next(j for j in order if left2>>j&1)
   thirds=coverers[pivot]&~(1<<first)&~(1<<second)
   for third in indices(thirds):
    if stats['third_masks_tested']%64==0 and expired():stats['search_CPU_limit_reached']=True;return None,stats
    stats['third_masks_tested']+=1;left3=left2&~masks[third]
    if not left3:return [first,second,third],stats
    fourths=allbits&~(1<<first)&~(1<<second)&~(1<<third)
    for j in order:
     if left3>>j&1:
      fourths&=coverers[j]
      if not fourths:break
    if fourths:return [first,second,third,(fourths&-fourths).bit_length()-1],stats
 stats['all_selected_prefixes_exhausted']=True;return None,stats

for pool_index in plan['pool_indices']:
 if 20-cpu()<7.6:break
 item=allpool[pool_index];pins=item['pins'];assert len(pins)==8
 row=dict(pool_index=pool_index,source_n=len(adj),source_m=current_m,mandatory_pins=pins,
          last_evaluation=dict(source_n=previous[pool_index]['source_n'],status=previous[pool_index]['status']),
          prior_accepted_line_vertices=0,multiple_line_vertex=False)
 blocked=[v for v in pins if len(adj[v])>=12]
 row['mandatory_current_degrees']=[len(adj[v]) for v in pins]
 if blocked:row.update(status='CURRENT_DEGREE_BLOCKED',blocked_pins=blocked);rows.append(row);continue
 prefix=OUT/'items'/f'pool{pool_index}_n{len(adj)}';pinfile=Path(str(prefix)+'.pins.txt')
 pinfile.write_text(' '.join(map(str,pins))+'\n')
 print('START '+json.dumps(dict(pool_index=pool_index,source_n=len(adj),degree_legal=True,CPU_total=cpu())),flush=True)
 with Path(str(prefix)+'.log').open('w') as log:
  ret=subprocess.run([str(NATIVE),'prepare',str(current_file),str(pinfile),str(prefix)],stdout=log,stderr=log)
 if ret.returncode!=0:row.update(status='UNKNOWN_NATIVE_LIMIT',returncode=ret.returncode);rows.append(row);continue
 prep=load(Path(str(prefix)+'.json'));row.update(mandatory_missing_count=prep['missing_count'],native_prepare_CPU_seconds=prep['CPU_seconds'])
 anchors=[] if prep['missing_count']==0 else (prep.get('exact_anchors') if prep.get('exact_one_or_two_found') else None)
 if anchors is None:
  raw=Path(str(prefix)+'.masks.u64.bin').read_bytes();word_bytes=8*prep['mask_words_per_row']
  masks=[int.from_bytes(raw[i:i+word_bytes],'little') for i in range(0,len(raw),word_bytes)]
  begin=time.process_time();chosen,stats=search(masks,prep['missing_count'],prep['representatives'],min(5.,max(0.,18.2-cpu())))
  row.update(rare_target=prep['missing'][stats['rare_target_index']],search_statistics=stats,search_CPU_seconds=time.process_time()-begin)
  if chosen is not None:anchors=[prep['representatives'][j] for j in chosen]
 if anchors is None:row['status']='NO_HIT_FINITE_RARE_TARGET_RULE' if row['search_statistics']['all_selected_prefixes_exhausted'] else 'UNKNOWN_RARE_PREFIX_TIME_LIMIT'
 else:
  neighbors=sorted(pins+anchors);assert len(neighbors)==len(set(neighbors))<=12 and all(len(adj[v])<12 for v in neighbors)
  pinfile.write_text(' '.join(map(str,neighbors))+'\n');selected=Path(str(prefix)+'_selected')
  subprocess.run([str(NATIVE),'verify',str(current_file),str(pinfile),str(selected)],check=True)
  check=load(Path(str(selected)+'.json'));assert check['missing_count']==0 and max(check['pin_current_degrees'])<12
  row.update(status='ACCEPTED_ACTUAL_DEGREE_COMPLETE_R4',new_vertex=len(adj),full_neighbor_set=neighbors,
   anchors=anchors,new_vertex_degree=len(neighbors),neighbors_old_degrees=check['pin_current_degrees'],
   actual_current_R4_covered=len(adj),actual_current_R4_missing=0,new_n=len(adj)+1,new_m=current_m+len(neighbors))
  adj.append(neighbors.copy())
  for v in neighbors:adj[v].append(len(adj)-1)
  current_m+=len(neighbors);current_file=OUT/'graphs'/f'graph_d12_D5_n{len(adj)}.edges'
  with current_file.open('w') as f:
   f.write(f'{len(adj)} {current_m}\n')
   for u,ns in enumerate(adj):
    for v in ns:
     if u<v:f.write(f'{u} {v}\n')
  accepted.append(row);print('HIT '+json.dumps(dict(pool_index=pool_index,new_n=len(adj),anchors=anchors,CPU_total=cpu())),flush=True)
 rows.append(row)
result=dict(status='FIXED_TWO_ITEMS_FINISHED' if len(rows)==2 else 'TOTAL_CPU_STOP_WITH_UNATTEMPTED_ITEM',
 initial_n=initial_n,initial_m=initial_m,final_n=len(adj),final_m=current_m,rows=rows,records=accepted,
 accepted_extensions=len(accepted),items_attempted=len(rows),items_unattempted=2-len(rows),
 final_graph=str(current_file.relative_to(ROOT)),CPU_parent_and_all_children_seconds=cpu(),
 allsource_BFS=0,externalreview=0,MIP=0,tenpin_pool_repeated=False,
 general_four_anchor_feasibility_excluded=False,pending=[])
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'accepted_extensions.json').write_text(json.dumps(dict(initial_n=initial_n,records=accepted,final_n=len(adj),final_m=current_m),indent=2)+'\n')
print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k not in ['rows','records']}),flush=True)
if accepted:exec(compile((BASE/'h9_d12_native_changed_base/deliver.py').read_text(),str(OUT/'deliver.py'),'exec'))
