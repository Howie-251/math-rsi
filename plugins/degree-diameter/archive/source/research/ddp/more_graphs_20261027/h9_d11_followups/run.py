"""One prescribed20record sequentialbatch with exactincrementalR4; oneCPU,no secondanchors."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import json,resource,sys,time
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3];BASE=HERE.parent/'h9_other_degrees'
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
start=time.process_time();wall=time.perf_counter()
assert not (HERE/'terminal.json').exists(),'Thisfixedbatchalreadyhasterminalstate'
pred=dict(prediction_id='N11_REMAINING20_ON_SUCCESSIVE_BASES',status='FROZEN_BEFORE_SEQUENTIAL_BATCH',timestamp=datetime.now(timezone.utc).isoformat(),
 hypothesis='Thechangedbase37629maypermitoneormoreofremaining20fixedQlinepinsetswithatmostoneanchor.',
 order='Exactlypoolindices4..23afterpinslexsortusedbyinitialcomplete11; indices0..2notrevisited,index3alreadyused.',
 current_degree=True,coverage='ActualcurrentbaseR4 by exactincremental formula,positivehit directly checked by one multi-sourceR4.',
 no_second_anchor=True,no_extra_round=True,worker_limit=1,hard_CPU_seconds=60)
def save(name,x):
 def prose(z):
  if isinstance(z,str):return[z]
  if isinstance(z,dict):return[s for y in z.values() for s in prose(y)]
  if isinstance(z,(list,tuple)):return[s for y in z for s in prose(y)]
  return[]
 assert not screen('\n'.join(prose(x)))
 (HERE/name).write_text(json.dumps(x,indent=2)+'\n')
save('PREDICTION.json',pred)
source=ROOT/'research/ddp/breadth_20261027_wave4/pencil_source/deg11_diam5_n37628.txt';adj=[]
for line in source.read_text().splitlines():
 if line.strip() and not line.startswith('#'):
  row=list(map(int,line.split()));assert row[0]==len(adj);adj.append(row[1:])
assert len(adj)==37628 and sum(map(len,adj))//2==205296
cache=ROOT/'research/ddp/breadth_20261027_wave9/cooperative37630'
meta=json.loads((cache/'coverage_cache.json').read_text());P=[v for v in range(len(adj)) if len(adj[v])<11]
assert P==meta['eligible_vertices'] and len(P)==2504 and meta['source_edges']==205296
raw=(cache/'radius4.u64.bin').read_bytes();B=588*8;assert len(raw)==B*len(P)
full=(1<<len(adj))-1;balls={v:int.from_bytes(raw[i*B:(i+1)*B],'little')&full for i,v in enumerate(P)}

def layers(pins,radius):
 dist=[-1]*len(adj);q=[]
 for p in pins:
  if dist[p]<0:dist[p]=0;q.append(p)
 for u in q:
  if dist[u]==radius:continue
  nd=dist[u]+1
  for v in adj[u]:
   if dist[v]<0:dist[v]=nd;q.append(v)
 return dist,q

def apply_extension(pins,dist):
 """Exactonallkeptoldballs; proofisinthe accompanyingreport, no oldcache rejection."""
 global balls,full
 z=len(adj);newbit=1<<z
 masks=[0,0,0,0]
 for u,d in enumerate(dist):
  if 0<=d<=3:
   for r in range(d,4):masks[r]|=1<<u
 newballs={}
 for a,old in balls.items():
  k=dist[a];b=old
  if 0<=k<=2:b|=masks[2-k]
  if 0<=k<=3:b|=newbit
  newballs[a]=b
 adj.append(list(pins))
 for p in pins:adj[p].append(z)
 balls={a:b for a,b in newballs.items() if len(adj[a])<11}
 if len(pins)<11:balls[z]=masks[3]|newbit
 full|=newbit
 assert set(balls)=={v for v in range(len(adj)) if len(adj[v])<11}
 assert all(b&(1<<a) for a,b in balls.items())
 return z

initial=json.loads((BASE/'degree11_hit.json').read_text());seed=initial['complete_new_neighbor_set']
D,Q=layers(seed,3);apply_extension(seed,D)
assert len(adj)==37629
verified=BASE/'candidate37629/graph_d11_D5_n37629.edges'
with verified.open() as f:
 n,m=map(int,next(f).split());assert(n,m)==(37629,205307)
 c=0
 for line in f:
  u,v=map(int,line.split());assert v in adj[u];c+=1
 assert c==m==sum(map(len,adj))//2
pool=json.loads((HERE.parent/'h9_global_line_pool/pool.json').read_text())['records']
order=sorted(enumerate(pool),key=lambda q:tuple(q[1]['pins']));assert len(order)==24
assert order[3][1]['pins']==initial['mandatory_pins']
save('frozen_pool_order.json',dict(records=[dict(pool_index=i,original_pool_index=j,**r) for i,(j,r) in enumerate(order)]))
rows=[];accepted=[]
for i in range(4,24):
 original_index,row=order[i];pins=row['pins'];assert len(pins)==10
 n=len(adj);bad=[p for p in pins if len(adj[p])>=11]
 if bad:
  rows.append(dict(pool_index=i,original_pool_index=original_index,base_n=n,status='CURRENT_DEGREE_BLOCKED',saturated_pins=bad));continue
 covered=0
 for p in pins:covered|=balls[p]
 missing=full&~covered
 anchor=None;success=missing==0;tested=0
 if not success:
  for a in sorted(balls):
   if a in pins:continue
   tested+=1
   if not(missing&~balls[a]):anchor=a;success=True;break
 if not success:
  rows.append(dict(pool_index=i,original_pool_index=original_index,base_n=n,status='EXACT_CURRENT_ONE_ANCHOR_FAIL',
   mandatory_missing_count=missing.bit_count(),all_current_available_anchors_considered=True,anchor_tests=tested));continue
 complete=sorted(pins+([] if anchor is None else[anchor]));assert len(complete)<=11 and len(set(complete))==len(complete)
 assert all(len(adj[p])<11 for p in complete)
 D,Q=layers(complete,4);assert len(Q)==n,'IncrementalR4predictionfailsactualcurrentpositiveR4check'
 record=dict(pool_index=i,original_pool_index=original_index,old_n=n,new_vertex=n,new_n=n+1,
   mandatory_pins=pins,anchors=[] if anchor is None else[anchor],new_neighbors=complete,
   old_pin_degrees=[len(adj[p]) for p in complete],current_old_vertices_R4_covered=n,
   actual_positive_R4_missing=0,current_R4_depth_histogram=dict(Counter(D)),geometric_witnesses=row['geometric_witnesses'])
 apply_extension(complete,D);accepted.append(record);rows.append({**record,'status':'ACCEPTED_COMPLETE_EXTENSION'})
 save('accepted_sequence.json',dict(initial_verified_n=37629,accepted=accepted))
 print(json.dumps(dict(event='ACCEPTED',pool_index=i,n=len(adj),pins=complete)),flush=True)

edges=[(u,v) for u,ns in enumerate(adj) for v in ns if u<v]
assert len(edges)==len(set(edges)) and max(map(len,adj))<=11
name=f'graph_d11_D5_n{len(adj)}.edges'
if accepted:
 (HERE/name).write_text(f'{len(adj)} {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
params=dict(source_file=str(source.relative_to(ROOT)),source_n=37628,source_m=205296,initial_verified_addition=initial['complete_new_neighbor_set'],
 initial_verified_graph=str(verified.relative_to(ROOT)),extensions=accepted,final_n=len(adj),final_m=len(edges),final_edge_file=name if accepted else str(verified.relative_to(ROOT)))
save('parameters.json',params)
result=dict(status='FINITE20_BATCH_COMPLETE',initial_n=37629,final_n=len(adj),final_m=len(edges),max_degree=max(map(len,adj)),
 processed_indices=list(range(4,24)),accepted_count=len(accepted),accepted_orders=[r['new_n'] for r in accepted],
 degree_blocked=sum(r['status']=='CURRENT_DEGREE_BLOCKED' for r in rows),
 exact_one_anchor_failures=sum(r['status']=='EXACT_CURRENT_ONE_ANCHOR_FAIL' for r in rows),rows=rows,
 incremental_R4_formula='oldBall4(a)unionR_{2-k}(S)whenk=d_old(a,S)<=2;alsoaddnewzwhenk<=3. newBall4(z)={z}unionR3_old(S).',
 positive_actual_multisource_R4_checks=len(accepted),initial_depth3_update_count=1,
 full_all_source_BFS_count=0,solver_calls=0,new_seeds=0,extra_rounds=0,second_anchors=0,
 final_graph=name if accepted else str(verified.relative_to(ROOT)),
 pending=['root_unique_final_strongest_all_source_BFS'] if accepted else [],
 CPU_seconds=time.process_time()-start,wall_seconds=time.perf_counter()-wall)
save('RESULT.json',result);save('terminal.json',result)
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2),flush=True)
