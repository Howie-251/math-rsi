from pathlib import Path
from collections import deque
import json,time
P=Path(__file__).resolve().parent;BASE=P.parent
assert not(P/'RESULT.json').exists()
START=time.process_time()
pred={'status':'FROZEN_BEFORE_FIXED_LEX_MATCHING_RELOCATION','prediction':'At least one relocation of matching0-26 to a necessary oldfree bridge preserves allsourceD3 routes and changes the eligible freeR2 cover problem.',
 'scope':'Onlydeletededge0-26/full-full witness332-326; allnecessarylegaloldfreebridges, nootherdeletededge/secondbridge.',
 'target_Delta':13,'target_D':3,'savedL':972,'possible_extension_n':973,
 'bridge_necessity':'332/326 arefull, notbridgeendpoints. Anewoldfree f-g must be the middleedge ofa<=3 repair, with f inN_H(332)∩F,g inN_H(326)∩F, orreverse.',
 'oldpair_proof':'Inherited sourceD3; priorprobe H=G-(0,26) u/v radius3 bothfullypass, notrerun. Anaddedbridge cannotworsen them. Allremainingoldpairs potentiallydamaged are x-0-26-y withx inNu-v,y inNv-u; exactR3 checktheseiscomplete.',
 'budget_CPU_seconds':3,'stop':'0validD3 stops. OnlyvalidD3 canenter oldintegerweightcapacity assessment andatmostone newF/R2+13cover<=5CPU. Noothercut/bridge/badscore.'}
(P/'PREDICTION.json').write_text(json.dumps(pred,indent=2)+'\n')
it=iter(map(int,(BASE/'source972.edges').read_text().split()));n=next(it);m=next(it);adj=[set()for _ in range(n)]
for _ in range(m):
 a,b=next(it),next(it);adj[a].add(b);adj[b].add(a)
F={z for z in range(n)if len(adj[z])<13};u,v,x,y=0,26,332,326
assert len(adj[x])==len(adj[y])==13 and v in adj[u]
old=json.loads((BASE/'matching_edge_release/CASES.jsonl').read_text().splitlines()[0])
assert old['edge']==[0,26] and old['status']=='MIDDLE_EDGE_CROSSPAIR_FAIL' and old['witness_root']==332 and old['witness_target']==326
adj[u].remove(v);adj[v].remove(u)
fx,fy=sorted(adj[x]&F),sorted(adj[y]&F)
raw=sorted({tuple(sorted((a,b)))for a in fx for b in fy if a!=b})
bridges=[(a,b)for a,b in raw if b not in adj[a]]
binding={'source':str(BASE/'source972.edges'),'deleted_edge':[u,v],'full_full_witness':[x,y],
 'free_neighbors_of_witness_root':fx,'free_neighbors_of_witness_target':fy,
 'raw_distinct_bridges':[list(e)for e in raw],'legal_nonedge_bridges':[list(e)for e in bridges],
 'oldfree_count':len(F),'inherited_u_v_modified_R3_passes':2,'source_BFS':0}
(P/'BINDING.json').write_text(json.dumps(binding,indent=2)+'\n')
def R3(root):
 d=[-1]*n;d[root]=0;q=deque([root])
 while q:
  a=q.popleft()
  if d[a]==3:continue
  for b in adj[a]:
   if d[b]<0:d[b]=d[a]+1;q.append(b)
 return d
results=[];roots=pairtests=0;valid=[]
for a,b in bridges:
 adj[a].add(b);adj[b].add(a);failed=None;cr=cp=0
 for xx in sorted(adj[u]):
  d=R3(xx);roots+=1;cr+=1
  for yy in sorted(adj[v]):
   pairtests+=1;cp+=1
   if d[yy]<0:failed=[xx,yy];break
  if failed:break
 rr={'added_bridge':[a,b],'deleted_edge':[u,v],
 'status':'FULL_D3_BY_COMPLETE_AFFECTED_PAIR_THEOREM'if failed is None else'MIDDLE_CROSSPAIR_STILL_FAILS',
 'modified_R3_roots':cr,'crosspairs_checked':cp,'first_distance_gt3_witness':failed}
 if failed is None:
  free=sorted(z for z in range(n)if len(adj[z])<13)
  assert free==sorted((F-{a,b})|{u,v}) and max(map(len,adj))<=13
  path=P/f'safe_relocation_{a}_{b}.edges'
  with path.open('w')as f:
   f.write(f'{n} {m}\n')
   for zz,row in enumerate(adj):
    for ww in sorted(row):
     if zz<ww:f.write(f'{zz} {ww}\n')
  rr.update(graph_file=str(path),free_vertices=free,free_count=len(free),maxdegree=max(map(len,adj)),actual_D=3)
  valid.append(rr)
 results.append(rr);adj[a].remove(b);adj[b].remove(a)
 assert time.process_time()-START<2.9
r={'status':'FIXED_EDGE_RELOCATION_VALID_D3_PRESENT'if valid else'FIXED_EDGE_ALL_NECESSARY_BRIDGES_FAIL',
 'prediction':'SUPPORTED'if valid else'REFUTED','deleted_edge':[u,v],
 'necessary_distinct_bridges':len(raw),'legal_bridges_tested':len(bridges),'unattempted_bridges':0,
 'complete_D3_variants':len(valid),'modified_radius3_roots':roots,'crosspairs_checked':pairtests,
 'original_source_BFS':0,'inherited_endpoint_R3_passes_not_rerun':2,
 'new973_graphs_generated':0,'newR2_balls_rebuilt':0,'solver_runs':0,
 'CPU_seconds':time.process_time()-START,'compile_CPU_seconds':0,
 'cases':results,'valid_variants':valid,'actual_new_n':None,'actual_new_D':None,
 'ordinary_bad_unordered_pairs':None,
 'pending':['Oldweightcapacityassessment andatmostone newR2/cover']if valid else[]}
for fn in['RESULT.json','terminal.json']:(P/fn).write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(binding,indent=2));print(json.dumps(r,indent=2))
