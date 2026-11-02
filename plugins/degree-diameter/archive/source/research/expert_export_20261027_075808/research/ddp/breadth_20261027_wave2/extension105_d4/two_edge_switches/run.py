from pathlib import Path
from collections import Counter,deque
import json,time,resource,subprocess,shutil

HERE=Path(__file__).resolve().parent;PARENT=HERE.parent
assert not (HERE/'terminal.json').exists(),'Do not restart a completed neighborhood.'
t0=time.process_time();r0=resource.getrusage(resource.RUSAGE_CHILDREN);child0=r0.ru_utime+r0.ru_stime;w0=time.monotonic()
def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-t0+r.ru_utime+r.ru_stime-child0
check=json.loads((PARENT/'best.independent_check.json').read_text());assert check['n']==105 and check['diameter']==5 and check['bad_unordered_pairs']==8
rows=[tuple(map(int,s.split())) for s in (PARENT/'best.edges').read_text().splitlines() if s.strip()]
assert rows[0]==(105,210);source=sorted(rows[1:]);assert len(set(source))==210
source_set=set(source)
adj=[set() for _ in range(105)]
for u,v in source:assert 0<=u<v<105;adj[u].add(v);adj[v].add(u)
assert {len(s) for s in adj}=={4}
(HERE/'source.edges').write_text('105 210\n'+''.join(f'{u} {v}\n' for u,v in source))
initial=None
for i,(a,b) in enumerate(source):
 for j in range(i+1,len(source)):
  c,d=source[j]
  if len({a,b,c,d})<4:continue
  for kind in range(2):
   u,v=(c,d) if not kind else (d,c)
   if u in adj[a] or v in adj[b]:continue
   initial=(i,j,kind,(a,u),(b,v));break
  if initial:break
 if initial:break
assert initial
i,j,kind,e1,e2=initial
edges=source_set-{source[i],source[j]};edges|={tuple(sorted(e1)),tuple(sorted(e2))};assert len(edges)==210
g=[set() for _ in range(105)]
for u,v in edges:g[u].add(v);g[v].add(u)
assert {len(s) for s in g}=={4}
first_t=time.process_time();hist=Counter();deficits=[]
for root in range(105):
 d=[-1]*105;d[root]=0;q=deque([root])
 while q:
  u=q.popleft()
  for v in g[u]:
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 hist.update(d);deficits.append(sum(x<0 or x>4 for x in d))
assert sum(deficits)%2==0
(HERE/'first.independent_calibration.json').write_text(json.dumps(dict(status='COMPLETE_FIRST_LEGAL_NEIGHBOR_CALIBRATION',source_edge_ids=[i,j],pairing=kind,BFS_roots_checked=105,bad_pairs=sum(deficits)//2,ordered_distance_histogram=dict(sorted(hist.items())),CPU_seconds=time.process_time()-first_t,first_score_reused=True),indent=2)+'\n')
(HERE/'first.expected.edges').write_text('105 210\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
(HERE/'first.expected.deficits').write_text(' '.join(map(str,deficits))+'\n')
(HERE/'inputs.json').write_text(json.dumps(dict(source='../best.edges',source_independent_check='../best.independent_check.json',source_bad_pairs=8,n=105,degree=4,target_D=4,scope='Every pair of vertex-disjoint saved-source edges, with both alternate reconnections; reject any new edge already present. Complete ordinary 2-edge-switch neighborhood only.',source_edge_count=210,raw_unordered_edge_pairs=21945,overlapping_pairs=630,disjoint_pairing_slots=42630,CPU_budget_seconds=30,workers=1),indent=2)+'\n')
shutil.copyfile(HERE/'source.edges',HERE/'best.edges')
(HERE/'best.json').write_text(json.dumps(dict(n=105,m=210,degree=4,target_D=4,bad_unordered_pairs=8,unchanged_parent=True,independent_check_reused='../best.independent_check.json'),indent=2)+'\n')
with (HERE/'compile.log').open('w') as f:subprocess.run(['g++','-O3','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],stdout=f,stderr=f,check=True)
prep=cpu();remaining=30-prep-1;assert remaining>0
with (HERE/'search.log').open('w') as f:
 proc=subprocess.Popen([str(HERE/'search'),str(HERE),str(remaining)],stdout=f,stderr=subprocess.STDOUT)
 (HERE/'run.json').write_text(json.dumps(dict(status='RUNNING',pid=proc.pid,preparation_CPU_seconds=prep,production_budget=remaining,workers=1),indent=2)+'\n');rc=proc.wait()
assert rc==0
term=json.loads((HERE/'terminal.json').read_text());term.update(preparation_CPU_seconds=prep,total_measured_CPU_seconds=cpu(),wall_seconds=time.monotonic()-w0,CPU_budget_seconds=30,first_calibration_BFS_roots=105,first_score_reused=True)
saved=[tuple(map(int,s.split())) for s in (HERE/'best.edges').read_text().splitlines() if s.strip()][1:]
unchanged=set(saved)==source_set
term['best_unchanged_parent']=unchanged
term['pending']=[] if unchanged else ['root independent final improved best graph check']
if unchanged:
 assert term['best_bad_pairs']==8
 (HERE/'best.verification_reuse.json').write_text(json.dumps(dict(status='REUSE_EXISTING_INDEPENDENT_CHECK',edge_sets_equal=True,source='../best.edges',independent_check='../best.independent_check.json',source_diameter=5,source_bad_pairs=8,new_BFS_roots=0),indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps(term,indent=2)+'\n');(HERE/'run.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps(term,ensure_ascii=False))
