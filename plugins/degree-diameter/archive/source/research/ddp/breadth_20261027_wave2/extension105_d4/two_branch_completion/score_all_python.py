from pathlib import Path
from collections import deque,Counter
import json,time

HERE=Path(__file__).resolve().parent;PARENT=HERE.parent
assert not (HERE/'terminal.json').exists(),'Do not restart this completed fixed scope.'
began=time.process_time();wall=time.monotonic()
inputs=json.loads((HERE/'inputs.json').read_text());assert inputs['all_simple_completions']==230
def read_edges(p):
 rows=[tuple(map(int,s.split())) for s in p.read_text().splitlines() if s.strip()]
 assert rows[0][0]==105 and rows[0][1]==len(rows)-1
 return set(rows[1:])
fixed=read_edges(HERE/'fixed.edges');source=read_edges(HERE/'source.edges');assert len(fixed)==202 and len(source)==210
raw=(HERE/'completions.txt').read_text().splitlines();assert raw[0]=='230'
completions=[]
for row in raw[1:]:
 values=list(map(int,row.split()));assert len(values)==16
 completions.append(tuple((values[i],values[i+1]) for i in range(0,16,2)))
assert len(completions)==len(set(completions))==230
assert all(len(fixed|set(c))==210 for c in completions)
first_edges=read_edges(HERE/'first.expected.edges')
assert first_edges==fixed|set(completions[0])
first=json.loads((HERE/'first.independent_calibration.json').read_text());assert first['BFS_roots_checked']==105
old=json.loads((PARENT/'best.independent_check.json').read_text());assert old['bad_unordered_pairs']==8 and old['n']==105
def score(edges):
 adj=[[] for _ in range(105)]
 for u,v in edges:adj[u].append(v);adj[v].append(u)
 assert {len(s) for s in adj}=={4}
 total=0
 for root in range(105):
  dist=[-1]*105;dist[root]=0;q=deque([root])
  while q:
   u=q.popleft()
   if dist[u]==4:continue
   for v in adj[u]:
    if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
  total+=dist.count(-1)
 assert total%2==0
 return total//2

best=8;best_edges=source;bestidx=None;done=0;new_BFS_roots=0;cached_parent=0;cached_first=0;hit=False;hist=Counter();records=[]
for idx,c in enumerate(completions):
 edges=fixed|set(c)
 if edges==source:value=8;cached_parent+=1
 elif idx==0:value=first['bad_pairs'];cached_first+=1
 else:value=score(edges);new_BFS_roots+=105
 done+=1;hist[value]+=1;records.append(dict(index=idx,bad_pairs=value))
 if value<best:
  best=value;best_edges=edges;bestidx=idx
  (HERE/'best.edges').write_text('105 210\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
  (HERE/'best.json').write_text(json.dumps(dict(n=105,m=210,degree=4,target_D=4,bad_unordered_pairs=best,completion_index=idx,new_completion_edges=c,diameter='pending root independent final check'),indent=2)+'\n')
  if not value:hit=True;break
 if time.process_time()-began>30:break

unchanged=best_edges==source
if unchanged:
 assert best==8
 (HERE/'best.edges').write_text('105 210\n'+''.join(f'{u} {v}\n' for u,v in sorted(source)))
 (HERE/'best.json').write_text(json.dumps(dict(n=105,m=210,degree=4,target_D=4,bad_unordered_pairs=8,unchanged_parent=True,independent_check_reused='../best.independent_check.json'),indent=2)+'\n')
 (HERE/'best.verification_reuse.json').write_text(json.dumps(dict(status='REUSE_PARENT_INDEPENDENT_CHECK',edge_sets_equal=True,independent_check='../best.independent_check.json',diameter=5,bad_pairs=8,new_BFS_roots=0),indent=2)+'\n')
(HERE/'candidates.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in records))
term=dict(status='FOUND_D4' if hit else 'COMPLETE_FIXED_NINE_VERTEX_COMPLETIONS_NO_D4' if done==230 else 'CPU_LIMIT_COMPLETION_PREFIX_NO_D4',running=False,found_D4=hit,completions_planned=230,completions_scored=done,scope_exhausted=done==230,source_bad_pairs=8,best_bad_pairs=best,best_completion_index=bestidx,bad_pair_histogram=dict(sorted(hist.items())),best_unchanged_parent=unchanged,cached_parent_scores_reused=cached_parent,cached_first_formal_scores_reused=cached_first,new_formal_scoring_BFS_roots=new_BFS_roots,prior_first_formal_calibration_BFS_roots=105,production_CPU_seconds=time.process_time()-began,production_wall_seconds=time.monotonic()-wall,enumeration_CPU_seconds=inputs['enumeration_CPU_seconds'],workers=1,restarts=0,CPU_budget_seconds=30,general105_graphs_excluded=False,pending=[] if unchanged else ['root independent final improved best graph check'],implementation='Ordinary Python deque BFS from every root, stopped after radius four; no C++ production run.',timing_scope='Python production timing includes loading prepared complete input and reuse checks; earlier enumeration/first-formal calibration separately recorded.')
(HERE/'terminal.json').write_text(json.dumps(term,indent=2)+'\n');(HERE/'run.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps(term,ensure_ascii=False))
