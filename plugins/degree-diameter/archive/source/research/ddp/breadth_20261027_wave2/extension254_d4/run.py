from pathlib import Path
from collections import Counter, deque
import json,random,subprocess,time,resource

HERE=Path(__file__).resolve().parent
PROJECT=HERE.parents[3]
SOURCE=PROJECT/'research/ddp/second_mechanism/rajiv252.edges'
assert not (HERE/'terminal.json').exists(), 'Do not restart an existing profile.'
cpu0=time.process_time(); children0=resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime+resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime; wall0=time.monotonic()
def all_cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-cpu0+r.ru_utime+r.ru_stime-children0

source=sorted(tuple(map(int,s.split())) for s in SOURCE.read_text().splitlines() if s.strip() and not s.startswith('#'))
assert len(source)==len(set(source))==630
assert all(0<=u<v<252 for u,v in source)
base=[set() for _ in range(252)]
for u,v in source:base[u].add(v);base[v].add(u)
assert {len(s) for s in base}=={5}
(HERE/'source.edges').write_text('252 630\n'+''.join(f'{u} {v}\n' for u,v in source))

starts=[]
for st in range(8):
 rng=random.Random(20261027252+st); chosen=[];used=set()
 while len(chosen)<4:
  k=rng.randrange(len(source));u,v=source[k]
  if u not in used and v not in used:chosen.append(k);used|={u,v}
 starts.append(dict(source_edge_ids=chosen,orientations=[rng.randrange(2) for _ in range(4)]))
(HERE/'starts.txt').write_text(''.join(' '.join(map(str,s['source_edge_ids']+s['orientations']))+'\n' for s in starts))
(HERE/'inputs.json').write_text(json.dumps(dict(source=str(SOURCE.relative_to(PROJECT)),source_order=252,source_edges=630,source_degree=5,new_order=254,target_max_degree=5,target_D=4,source_selection='fixed saved Rajiv252 graph',start_seed_base=20261027252,mutation_seed_base=202610272540,starts=starts,proposals_per_start=10000,starts_count=8,CPU_budget_seconds=60,workers=1,scope='Four mutually vertex-disjoint deleted source edges; add two adjacent vertices each attached to its four oriented endpoints; finite annealing profile, not full source-family enumeration.'),indent=2)+'\n')

# This first formal state is independently expanded, then checked by ordinary
# full-source BFS. C++ must compare every saved edge and every root deficit.
initial=starts[0];edges=set(source)
for k,flip in zip(initial['source_edge_ids'],initial['orientations']):
 u,v=source[k];edges.remove((u,v))
 if flip:u,v=v,u
 edges.add(tuple(sorted((252,u))));edges.add(tuple(sorted((253,v))))
edges.add((252,253));assert len(edges)==635
adj=[set() for _ in range(254)]
for u,v in edges:adj[u].add(v);adj[v].add(u)
assert {len(s) for s in adj}=={5}
t=time.process_time();deficits=[];hist=Counter()
for root in range(254):
 dist=[-1]*254;dist[root]=0;q=deque([root])
 while q:
  u=q.popleft()
  for v in adj[u]:
   if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
 deficits.append(sum(d<0 or d>4 for d in dist));hist.update(dist)
assert sum(deficits)%2==0
first=dict(status='COMPLETE_FIRST_FORMAL_CALIBRATION',n=254,m=635,minimum_degree=5,maximum_degree=5,BFS_roots_checked=254,bad_pairs=sum(deficits)//2,ordered_distance_histogram=dict(sorted(hist.items())),first_score_to_be_reused=True,CPU_seconds=time.process_time()-t)
(HERE/'first.independent_calibration.json').write_text(json.dumps(first,indent=2)+'\n')
(HERE/'first.expected.edges').write_text('254 635\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
(HERE/'first.expected.deficits').write_text(' '.join(map(str,deficits))+'\n')
with (HERE/'compile.log').open('w') as f:subprocess.run(['g++','-O3','-std=c++17',str(HERE/'search.cpp'),'-o',str(HERE/'search')],check=True,stdout=f,stderr=f)
prep=all_cpu();remaining=60-prep-1
assert remaining>0
run=dict(status='RUNNING',started_utc=time.strftime('%Y-%m-%d %H:%M:%S UTC',time.gmtime()),preparation_CPU_seconds=prep,total_CPU_budget_seconds=60,production_budget_seconds=remaining,worker_count=1)
(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n')
with (HERE/'search.log').open('w') as f:
 proc=subprocess.Popen([str(HERE/'search'),str(HERE),str(remaining)],stdout=f,stderr=subprocess.STDOUT)
 run['pid']=proc.pid;(HERE/'run.json').write_text(json.dumps(run,indent=2)+'\n');rc=proc.wait()
assert rc==0
term=json.loads((HERE/'terminal.json').read_text());term.update(preparation_CPU_seconds=prep,total_measured_CPU_seconds=all_cpu(),wall_seconds=time.monotonic()-wall0,total_CPU_budget_seconds=60,first_calibration_roots=254,first_score_reused=True)
(HERE/'terminal.json').write_text(json.dumps(term,indent=2)+'\n');(HERE/'run.json').write_text(json.dumps(term,indent=2)+'\n')
print(json.dumps({k:v for k,v in term.items() if k not in ['current_deleted_ids','current_orientations']},ensure_ascii=False))
