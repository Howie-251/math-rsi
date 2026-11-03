"""One bounded210pair common-old-anchor block on the verified37631source."""
import resource,time,json,sys
from pathlib import Path
from itertools import combinations
from collections import Counter
resource.setrlimit(resource.RLIMIT_CPU,(10,10));start=time.process_time();wall=time.perf_counter()
H=Path(__file__).resolve().parent;ROOT=H.parents[3];MORE=H.parent
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen

def save(name,obj):
 def txt(z):
  if isinstance(z,str):return[z]
  if isinstance(z,dict):return[t for v in z.values() for t in txt(v)]
  if isinstance(z,list):return[t for v in z for t in txt(v)]
  return[]
 assert not screen('\n'.join(txt(obj)));(H/name).write_text(json.dumps(obj,indent=2)+'\n')
assert not (H/'terminal.json').exists(),'One-shot shared-anchor experiment already completed'
source=MORE/'h9_d11_followups/graph_d11_D5_n37631.edges';N=37631;M=205329;current=[[] for _ in range(N)]
with source.open() as f:
 n,m=map(int,next(f).split());assert(n,m)==(N,M)
 for line in f:
  u,v=map(int,line.split());current[u].append(v);current[v].append(u)
assert sum(map(len,current))//2==M and max(map(len,current))==11
anchors=[v for v in range(N) if len(current[v])<=9];pred=json.loads((H/'PREDICTION.json').read_text());assert anchors==pred['anchor_vertices'] and len(anchors)==315
# Recover only these315 anchor balls, updating the true fixed base one append at a time.
cache=ROOT/'research/ddp/breadth_20261027_wave9/cooperative37630';cm=json.loads((cache/'coverage_cache.json').read_text());P=cm['eligible_vertices']
adj=[[v for v in current[u] if v<37628] for u in range(37628)]
assert sum(map(len,adj))//2==205296 and P==[u for u in range(37628) if len(adj[u])<11] and len(P)==2504 and cm['source_edges']==205296
raw=(cache/'radius4.u64.bin').read_bytes();stride=588*8;assert len(raw)==2504*stride;index={v:i for i,v in enumerate(P)};full=(1<<37628)-1
balls={a:int.from_bytes(raw[index[a]*stride:(index[a]+1)*stride],'little')&full for a in anchors};updates=[]

def layers(S,r):
 d=[-1]*len(adj);q=[]
 for s in S:
  if d[s]<0:d[s]=0;q.append(s)
 for u in q:
  if d[u]==r:continue
  nd=d[u]+1
  for v in adj[u]:
   if d[v]<0:d[v]=nd;q.append(v)
 return d,q

for z in range(37628,N):
 S=sorted(current[z]);assert len(S)==11 and all(v<z for v in S)
 d,q=layers(S,3);masks=[0,0,0]
 for u in q:
  du=d[u]
  if du<=2:
   bit=1<<u
   for r in range(du,3):masks[r]|=bit
 newbit=1<<z
 for a in anchors:
  k=d[a]
  if 0<=k<=2:balls[a]|=masks[2-k]
  if 0<=k<=3:balls[a]|=newbit
 adj.append(S)
 for v in S:adj[v].append(z)
 full|=newbit;updates.append(dict(new_vertex=z,neighbors=S,exact_R4_anchor_rows_updated=len(anchors),bounded_multisource_depth=3))
assert full==(1<<N)-1 and all(sorted(adj[u])==sorted(current[u]) for u in range(N))
# Use only metadata-bound actual-current line caches from the other finite block.
linecache=MORE/'h9_d11_two_qline_block';lm=json.loads((linecache/'cache_metadata.json').read_text());assert(lm['source_n'],lm['source_m'],lm['R3_row_bytes'])==(N,M,N)
indices=lm['pool_indices'];assert indices==[i for i in range(24) if i not in [3,17,21]]
records=json.loads((MORE/'h9_d11_followups/frozen_pool_order.json').read_text())['records'];assert len(records)==24
raw3=(linecache/'line_R3_rows.u8.bin').read_bytes();assert len(raw3)==len(indices)*N
R2={};R4={};pins={}
for row,i in enumerate(indices):
 pins[i]=records[i]['pins'];assert len(pins[i])==10 and len(set(pins[i]))==10 and all(len(adj[p])<11 for p in pins[i])
 dist=raw3[row*N:(row+1)*N];ball=0
 for v,d in enumerate(dist):
  if d<=2:ball|=1<<v
 R2[i]=ball;missing=sum(1<<v for v in lm['R4_missing_targets'][str(i)]);R4[i]=full&~missing
 assert all(R2[i]&(1<<p) for p in pins[i])
save('cache_binding.json',dict(source_file=str(source.relative_to(ROOT)),source_n=N,source_m=M,anchor_count=len(anchors),
 original_R4_cache=str(cache.relative_to(ROOT)),original_cache_n=37628,original_cache_candidates=2504,
 exact_append_updates=updates,all_current_adjacency_rows_match=True,anchor_current_R4_rows=len(balls),
 line_cache=str(linecache.relative_to(ROOT)),line_cache_source_n=N,line_cache_source_m=M,
 line_indices=indices,line_R2_from_actual_R3_depth=True,new_line_BFS=0,full_allsource_BFS=0))
rows=[];hit=None;anchor_tests=0
for i,j in combinations(indices,2):
 usage=Counter(pins[i]+pins[j]);bad=[p for p,c in usage.items() if len(adj[p])+c>11]
 if bad:
  rows.append(dict(A=i,B=j,status='SHARED_PIN_DEGREE_BLOCKED',pins=bad));continue
 missing=(full&~(R4[i]|R2[j]))|(full&~(R4[j]|R2[i]));chosen=None;tested=0
 for h in anchors:
  if h in usage:continue
  tested+=1;anchor_tests+=1
  if not(missing&~balls[h]):chosen=h;break
 if chosen is None:
  rows.append(dict(A=i,B=j,status='NO_COMPLETE_SHARED_ANCHOR',missing_count=missing.bit_count(),anchor_candidates_tested=tested));continue
 h=chosen;ZA=sorted(pins[i]+[h]);WB=sorted(pins[j]+[h]);assert len(ZA)==len(WB)==11 and len(set(ZA))==len(set(WB))==11
 assert not(full&~(R4[i]|R2[j]|balls[h])) and not(full&~(R4[j]|R2[i]|balls[h]))
 proposed=[list(v) for v in adj]+[ZA,WB]
 for v in ZA:proposed[v].append(N)
 for v in WB:proposed[v].append(N+1)
 assert max(map(len,proposed))<=11 and N+1 not in proposed[N]
 positive=[]
 for root in [N,N+1]:
  d=[-1]*len(proposed);d[root]=0;q=[root]
  for u in q:
   if d[u]==5:continue
   for v in proposed[u]:
    if d[v]<0:d[v]=d[u]+1;q.append(v)
  assert len(q)==len(proposed)
  positive.append(dict(root=root,reached=len(q),maximum_depth=max(d),depth_histogram=dict(Counter(d))))
 hit=dict(source_n=N,source_m=M,target_n=N+2,target_m=M+22,target_Delta=11,target_D=5,
  pool_A=i,pool_B=j,A=pins[i],B=pins[j],shared_anchor=h,old_anchor_degree=len(adj[h]),new_anchor_degree=len(proposed[h]),
  new_vertices=[N,N+1],new_neighbors={str(N):ZA,str(N+1):WB},no_new_new_edge=True,new_vertex_degrees=[11,11],
  full_oldtarget_cover_verified=True,full_cover_formula='R4h covers (Vminus(R4AunionR2B))union(Vminus(R4BunionR2A))',
  missing_before_anchor=missing.bit_count(),missing_after_anchor=0,max_degree=max(map(len,proposed)),source_edges_retained=True,
  positive_new_root_radius5_checks=positive,allsource_BFS_count=0,root_allsource_verification_pending=True,
  source_file=str(source.relative_to(ROOT)),edge_file='graph_d11_D5_n37633.edges')
 save('hit.json',hit)
 edges=[(u,v) for u,ns in enumerate(proposed) for v in ns if u<v];assert len(edges)==M+22
 (H/'graph_d11_D5_n37633.edges').write_text(f'{N+2} {M+22}\n'+''.join(f'{u} {v}\n' for u,v in edges))
 rows.append(dict(A=i,B=j,status='COMPLETE_SHARED_ANCHOR_HIT',anchor=h));print('HIT '+json.dumps(hit),flush=True);break
result=dict(status='COMPLETE_SHARED_ANCHOR_BLOCK_FOUND_AWAIT_ROOT' if hit else 'ALL210_SHARED_ANCHOR_PAIRS_EXACTLY_EXHAUSTED',
 incumbent=hit is not None,source_n=N,source_m=M,target_n=N+2,pairs_available=210,pairs_processed=len(rows),anchor_candidates=len(anchors),anchor_tests=anchor_tests,
 degree_blocked_pairs=sum(r['status']=='SHARED_PIN_DEGREE_BLOCKED' for r in rows),rows=rows,
 new_bounded_multisource_R3_for_cache_restore=3,new_line_radius_computations=0,positive_new_root_R5_checks=2 if hit else 0,
 fullgraph_allsource_BFS=0,solver_calls=0,CPU_seconds=time.process_time()-start,wall_seconds=time.perf_counter()-wall,
 extra_rounds=0,third_new_vertex=False,extra_anchors=False)
save('RESULT.json',result);save('terminal.json',result);print('FINAL '+json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)
