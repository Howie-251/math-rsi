from pathlib import Path
import json, random, subprocess, time, itertools, resource

P=Path(__file__).resolve().parent
started=time.process_time()
wall=time.monotonic()
d=json.loads((P/'base_words.json').read_text())
edges=[tuple(e) for e in d['edges']]
free=d['free']; tree=d['tree']
def add(a,b): return ((a[0]+b[0])%4,(a[1]+b[1])%8)
def neg(a): return ((-a[0])%4,(-a[1])%8)
def code(a): return a[0]+4*a[1]
def pair(a): return (a%4,a//4)

pot=[None]*6;pot[0]=(0,0)
while any(x is None for x in pot):
 for e in tree:
  u,v=edges[e];g=tuple(d['source_gamma'][e])
  if pot[u] is not None and pot[v] is None:pot[v]=add(pot[u],g)
  if pot[v] is not None and pot[u] is None:pot[u]=add(pot[v],neg(g))
first=[code(add(add(tuple(d['source_gamma'][e]),pot[edges[e][0]]),neg(pot[edges[e][1]]))) for e in range(12)]
assert all(first[e]==0 for e in tree)

def graph(gamma):
 adj=[[] for _ in range(192)]; es=[]
 for e,(u,v) in enumerate(edges):
  for h in range(32):
   a=32*u+h;b=32*v+code(add(pair(h),pair(gamma[e])))
   idx=len(es);es.append((a,b));adj[a].append((b,idx));adj[b].append((a,idx))
 assert len(es)==384 and len({tuple(sorted(e)) for e in es})==384
 assert all(len(a)==4 for a in adj)
 return adj,es

def direct_support(gamma):
 adj,es=graph(gamma)
 out=[]
 for r in range(6):
  states={(32*r,-1)}
  for step in range(5):
   states={(v,e) for u,prev in states for v,e in adj[u] if e!=prev}
  out.append(sorted({u for u,e in states}))
 return out

def word_support(gamma):
 rows=[]
 for r in range(6):
  supp=set()
  for v in range(6):
   for w in d['words'][r][v]:
    c=w['coeff'];x=sum(c[e]*(gamma[e]%4) for e in free)%4;y=sum(c[e]*(gamma[e]//4) for e in free)%8
    supp.add(32*v+x+4*y)
  rows.append(sorted(supp))
 return rows

a=direct_support(first);b=word_support(first)
assert a==b
calibration=dict(status='MATCH',vertices=192,degree=4,source='original C4xC6 voltages reinterpreted in C4xC8 then tree-gauged',gamma_codes=first,free_gamma_codes=[first[e] for e in free],all_6_orbit_representative_NB5_matrices_equal=True,orbit_representative_reached=[len(row) for row in a],orbit_representative_misses=sum(192-len(row) for row in a),all_ordered_pair_misses=32*sum(192-len(row) for row in a),python_support=a,CPU_seconds=time.process_time()-started)
(P/'first_calibration.json').write_text(json.dumps(calibration,indent=2)+'\n')

# Coefficient multiplicity is irrelevant to coverage; retain each symbolic function once.
functions=[]
for r in range(6):
 for v in range(6):
  fs=sorted({tuple(w['coeff'][e] for e in free) for w in d['words'][r][v]})
  functions.append(fs)
rng=random.Random(20261027192)
starts=[[first[e] for e in free]]+[[rng.randrange(1,32) if j in (0,2) else rng.randrange(32) for j in range(7)] for _ in range(7)]
with (P/'input.txt').open('w') as f:
 print(len(functions),file=f)
 for fs in functions:
  print(len(fs),file=f)
  for c in fs: print(*c,file=f)
 print(len(starts),file=f)
 for s in starts:print(*s,file=f)

def limits():resource.setrlimit(resource.RLIMIT_CPU,(450,450))
compile_started=resource.getrusage(resource.RUSAGE_CHILDREN)
subprocess.run(['g++','-O3','-std=c++17',str(P/'search.cpp'),'-o',str(P/'search')],check=True)
compiled=resource.getrusage(resource.RUSAGE_CHILDREN)
with (P/'input.txt').open() as inp,(P/'search_output.json').open('w') as out:
 run=subprocess.run([str(P/'search')],stdin=inp,stdout=out,check=True,preexec_fn=limits)
searched=resource.getrusage(resource.RUSAGE_CHILDREN)
result=json.loads((P/'search_output.json').read_text())
assert result['first_score']==calibration['orbit_representative_misses']
best=[0]*12
for e,x in zip(free,result['best']):best[e]=x
adj,es=graph(best)

# Two oriented Hamiltonian cycles of the named base multigraph provide a±,b±.
factor_cycles=[[0,2,1,5,3,4,0],[0,3,1,5,2,4,0]]
factor_edges=[[0,4,6,11,10,2],[1,5,7,9,8,3]]
labels=[[-1]*4 for _ in range(192)]
for k,(cycle,eids) in enumerate(zip(factor_cycles,factor_edges)):
 for u,v,e in zip(cycle,cycle[1:],eids):
  g=pair(best[e]) if edges[e]==(u,v) else neg(pair(best[e]))
  for h in range(32):
   a=32*u+h;b=32*v+code(add(pair(h),g))
   labels[a][2*k]=b;labels[b][2*k+1]=a
inv=[1,0,3,2]
assert all(len(set(row))==4 and set(row)=={v for v,e in adj[u]} for u,row in enumerate(labels))
assert all(labels[v][inv[t]]==u for u,row in enumerate(labels) for t,v in enumerate(row))
(P/'best.edges').write_text(''.join(f'{u} {v}\n' for u,v in es))
(P/'best.labels.json').write_text(json.dumps(dict(vertices=192,symbols=['a','a_inverse','b','b_inverse'],inverse=inv,out=labels,base_factor_cycles=factor_cycles,base_factor_edge_ids=factor_edges))+'\n')
result.update(status='HIT_EXACT_NB5_CONTROLLER' if result['best_score']==0 else 'FINITE_VOLTAGE_TRIAL_FAILED',controller_vertices=192,controller_degree=4,controller_edges=384,voltage_group='C4 direct_product C8',base_edges=edges,tree_edges=tree,free_edges=free,best_full_gamma_codes=best,best_full_gamma_pairs=[pair(x) for x in best],representative_NB5_misses=result['best_score'],exact_NB5_ordered_pair_misses=32*result['best_score'],vertex_encoding='32*base + x + 4*y; x mod 4, y mod 8',edge_rule='(u,h) adjacent to (v,h+gamma_e), with named oriented base edge e=(u,v)',inverse_consistent_labels=True,compile_CPU_seconds=(compiled.ru_utime+compiled.ru_stime)-(compile_started.ru_utime+compile_started.ru_stime),search_process_CPU_seconds=(searched.ru_utime+searched.ru_stime)-(compiled.ru_utime+compiled.ru_stime),python_CPU_seconds=time.process_time()-started,wall_seconds=time.monotonic()-wall,independent_full_best_check='PENDING_ROOT_UNIQUE_FINAL_CHECK',actual_large_lift_generated=False)
result['total_CPU_seconds']=result['compile_CPU_seconds']+result['search_process_CPU_seconds']+result['python_CPU_seconds']
(P/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['base_edges','best_full_gamma_pairs']}))
