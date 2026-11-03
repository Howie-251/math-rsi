from pathlib import Path
from itertools import product
import json,os,random,resource,subprocess,time
P=Path(__file__).resolve().parent
assert not (P/'terminal.json').exists(), 'Do not restart a completed finite profile.'
t=time.process_time();wall=time.monotonic()
def cpu():
 r=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()-t+r.ru_utime+r.ru_stime
n=175
fixed={tuple(sorted((5*b+i,5*b+(i+1)%5))) for b in range(35) for i in range(5)}
assert len(fixed)==175
starts=[];draws=[]
for seed in range(202610271750,202610271754):
 rng=random.Random(seed);attempts=0
 while True:
  order=list(range(n));rng.shuffle(order);attempts+=1
  E=[tuple(sorted((order[i],order[(i+1)%n]))) for i in range(n)]
  if not (set(E)&fixed):break
 assert len(set(E))==175;starts.append(E);draws.append(attempts)
(P/'starts.txt').write_text(''.join(f'{u} {v}\n' for E in starts for u,v in E))
adj=[set() for _ in range(n)]
for u,v in sorted(fixed|set(starts[0])):adj[u].add(v);adj[v].add(u)
assert all(len(row)==4 for row in adj)
# Independent root-by-root state DP; the C++ scorer propagates all roots as bitsets.
target_sources=[0]*n
for root in range(n):
 states={(root,v) for v in adj[root]}
 for length in range(2,6):states={(v,w) for u,v in states for w in adj[v] if w!=u}
 for v in {v for _,v in states}:target_sources[v]|=1<<root
expected=[[mask&((1<<64)-1),(mask>>64)&((1<<64)-1),mask>>128] for mask in target_sources]
(P/'first_expected.txt').write_text('\n'.join(' '.join(map(str,row)) for row in expected)+'\n')
first_missing=n*n-sum(mask.bit_count() for mask in target_sources)
(P/'first_calibration.json').write_text(json.dumps(dict(n=n,all_ordered_pairs=n*n,exact_length=5,backtracking_forbidden=True,independent_method='Root-by-root Python last-directed-edge state DP',missing_ordered_pairs=first_missing,complete_target_source_bitmasks=target_sources,score_reused=True),indent=2)+'\n')
(P/'inputs.json').write_text(json.dumps(dict(n=n,fixed_cycles=[list(range(5*b,5*b+5)) for b in range(35)],external_degree=2,start_seeds=list(range(202610271750,202610271754)),start_shuffle_draws=draws,mutation_seed=202610271751,starts=4,proposals_per_start=10000,temperature='30 * 0.02**(step/9999)',objective='Missing ordered pairs with no nonbacktracking walk of exactly5 edges, including diagonal',target_final_lift=dict(field=3,dimension=5,n=42525,degree=12,diameter_bound=5,saved_baseline=42342),fiber_chart='../source_scout/route_chart_F3_5.json',total_CPU_budget=90,workers=1),indent=2)+'\n')
subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=P,check=True)
remaining=90-cpu()-1
assert remaining>0
worker=subprocess.Popen(['./search',str(remaining)],cwd=P,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
(P/'run.json').write_text(json.dumps(dict(status='RUNNING',running=True,driver_pid=os.getpid(),worker_pid=worker.pid,CPU_budget_seconds=90),indent=2)+'\n')
output,_=worker.communicate(timeout=100)
(P/'production.log').write_text(output);assert worker.returncode==0,output
r=json.loads((P/'production_terminal.json').read_text());r.update(total_measured_CPU_seconds=cpu(),wall_seconds=time.monotonic()-wall,CPU_budget_seconds=90,workers=1,partial_controller_only=True,large_lift_generated=False,pending=['root independent final saved-edge BFS and exact-NB5 confirmation'])
# Orient every external cycle for inverse-consistent b/b^-1 labels.
E=[tuple(map(int,s.split())) for s in (P/'best.external_edges').read_text().splitlines() if s.strip()]
ext=[[] for _ in range(n)]
for u,v in E:ext[u].append(v);ext[v].append(u)
assert all(len(x)==2 for x in ext)
bp=[-1]*n;bm=[-1]*n;done=set()
for start in range(n):
 if start in done:continue
 previous=-1;u=start
 while u not in done:
  done.add(u);v=min(ext[u]) if previous<0 else next(x for x in ext[u] if x!=previous)
  bp[u]=v;bm[v]=u;previous,u=u,v
 assert u==start
labels=[[v-v%5+(v%5+1)%5,v-v%5+(v%5+4)%5,bp[v],bm[v]] for v in range(n)]
assert all(len(set(row))==4 for row in labels)
assert all(labels[labels[v][j]][j^1]==v for v in range(n) for j in range(4))
(P/'best.labels.json').write_text(json.dumps(dict(symbols=['a','a^-1','b','b^-1'],inverse_symbols=[1,0,3,2],neighbors_by_label=labels))+'\n')
(P/'terminal.json').write_text(json.dumps(r,indent=2)+'\n');(P/'run.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
