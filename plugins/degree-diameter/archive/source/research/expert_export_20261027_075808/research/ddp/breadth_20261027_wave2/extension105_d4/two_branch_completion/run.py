from pathlib import Path
from collections import Counter,deque
from itertools import combinations
import json,time,subprocess,sys

HERE=Path(__file__).resolve().parent;PARENT=HERE.parent
assert not (HERE/'terminal.json').exists(),'Do not restart this fixed completion batch.'
old=json.loads((PARENT/'best.independent_check.json').read_text());assert old['n']==105 and old['bad_unordered_pairs']==8
rows=[tuple(map(int,s.split())) for s in (PARENT/'best.edges').read_text().splitlines() if s.strip()];assert rows[0]==(105,210);source=set(rows[1:]);assert len(source)==210
removed={e for e in source if 12 in e or 13 in e};assert len(removed)==8
fixed=source-removed;free=sorted({v for e in removed for v in e});assert free==[12,13,41,44,48,49,52,53,104]
degrees=Counter(v for e in fixed for v in e);need=[4-degrees[v] for v in free];assert sorted(need)==[1]*6+[2,4,4]
assert not [e for e in fixed if set(e)<=set(free)]
outside=set(range(105))-set(free);assert all(degrees[v]==4 for v in outside)
solutions=[]
def complete(d,chosen):
 active=[i for i,x in enumerate(d) if x]
 if not active:solutions.append(tuple(sorted(chosen)));return
 i=max(active,key=lambda k:(d[k],-k));others=[j for j in active if j!=i and tuple(sorted((free[i],free[j]))) not in fixed]
 k=d[i]
 if k>len(others):return
 for neighbors in combinations(others,k):
  nd=d.copy();nd[i]=0
  for j in neighbors:nd[j]-=1
  if any(x<0 for x in nd):continue
  # Every edge incident to i is fixed now; future recursion excludes i.
  complete(nd,chosen+[tuple(sorted((free[i],free[j]))) for j in neighbors])
enum_t=time.process_time();complete(need,[]);solutions=sorted(solutions);enum_cpu=time.process_time()-enum_t
assert len(solutions)==len(set(solutions))==230
assert tuple(sorted(removed)) in solutions
counts=Counter()
for e in solutions:
 assert len(e)==8 and not (set(e)&fixed)
 assert Counter(v for edge in e for v in edge)==dict(zip(free,need))
 core=sum(u in {12,13,104} and v in {12,13,104} for u,v in e);leaf=sum(u not in {12,13,104} and v not in {12,13,104} for u,v in e);assert core-leaf==2
 counts[core,leaf]+=1
assert counts=={(2,0):140,(3,1):90}
(HERE/'fixed.edges').write_text('105 202\n'+''.join(f'{u} {v}\n' for u,v in sorted(fixed)))
(HERE/'source.edges').write_text('105 210\n'+''.join(f'{u} {v}\n' for u,v in sorted(source)))
(HERE/'completions.txt').write_text('230\n'+''.join(' '.join(str(v) for edge in e for v in edge)+'\n' for e in solutions))
(HERE/'inputs.json').write_text(json.dumps(dict(source='../best.edges',source_independent_check='../best.independent_check.json',free_vertices=free,residual_degrees=dict(zip(free,need)),removed_source_edges=sorted(removed),fixed_edge_count=202,completion_edges_per_graph=8,all_simple_completions=230,core_leaf_count_crosscheck={'core2_leaf0':140,'core3_leaf1':90},enumeration_CPU_seconds=enum_cpu,CPU_budget_seconds=30,workers=1,label_correction='The task initially listed P-neighbor labels 42,43,46,47. Actual saved source endpoints are 41,44,48,49,52,53; root confirmed the correction before this batch. Source and selected branches 12,13 were unchanged.'),indent=2)+'\n')

# Independent ordinary-BFS calibration of the first formal completion.
first_edges=fixed|set(solutions[0]);assert len(first_edges)==210
adj=[set() for _ in range(105)]
for u,v in first_edges:adj[u].add(v);adj[v].add(u)
assert {len(s) for s in adj}=={4}
first_t=time.process_time();hist=Counter();deficits=[]
for root in range(105):
 d=[-1]*105;d[root]=0;q=deque([root])
 while q:
  u=q.popleft()
  for v in adj[u]:
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 hist.update(d);deficits.append(sum(x<0 or x>4 for x in d))
assert sum(deficits)%2==0
(HERE/'first.independent_calibration.json').write_text(json.dumps(dict(status='COMPLETE_FIRST_FORMAL_COMPLETION_CALIBRATION',completion_index=0,BFS_roots_checked=105,bad_pairs=sum(deficits)//2,ordered_distance_histogram=dict(sorted(hist.items())),CPU_seconds=time.process_time()-first_t,first_score_reused=True),indent=2)+'\n')
(HERE/'first.expected.edges').write_text('105 210\n'+''.join(f'{u} {v}\n' for u,v in sorted(first_edges)))
(HERE/'first.expected.deficits').write_text(' '.join(map(str,deficits))+'\n')
subprocess.run([sys.executable,str(HERE/'score_all_python.py')],check=True)
