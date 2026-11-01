"""Independent small-graph definition check and exact pilot obstruction certificate."""
from pathlib import Path
from functools import lru_cache
from itertools import combinations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
def f(s):
 return sum(a*b for a,b in combinations([s//5+(i<s%5) for i in range(5)],2))
def g(q):return f(34-q)
@lru_cache(None)
def U(n,m,r=0):
 if m<0 or m>n*(n-1)//2:return -10**9
 if not n:return 0
 return max(g(r)+U(n-1,m,r),g(r+n-1)+U(n-1,m-(n-1),r+1))
small=[]
for n in range(1,7):
 E=list(combinations(range(n),2));best=[-1]*(len(E)+1)
 for mask in range(1<<len(E)):
  ds=[0]*n
  for i,(u,v) in enumerate(E):
   if mask>>i&1:ds[u]+=1;ds[v]+=1
  m=mask.bit_count();best[m]=max(best[m],sum(g(q) for q in ds))
 assert best==[U(n,m) for m in range(len(E)+1)]
 small.append({'n':n,'all_labeled_graphs':1<<len(E),'by_edge_count':best})
j=json.loads((P/'PILOT.json').read_text());value=U(35,76);assert value==j['P_component_majorant']==13074
# Recover a maximizing graph on all35 vertices by a separate recursive threshold construction.
edge=[];sequence=[];n=35;m=76;r=0
for v in range(35):
 universal=(g(r+n-1)+U(n-1,m-n+1,r+1)==U(n,m,r))
 sequence.append(int(universal))
 if universal:
  edge.extend((v,w) for w in range(v+1,35));m-=n-1;r+=1
 n-=1
assert m==0 and len(edge)==76 and len(set(edge))==76
ds=[0]*35
adj=[set() for _ in ds]
for a,b in edge:ds[a]+=1;ds[b]+=1;adj[a].add(b);adj[b].add(a)
assert sum(g(q) for q in ds)==13074
seen=set();sizes=[]
for v in range(35):
 if v in seen:continue
 todo=[v];seen.add(v);z=0
 while todo:
  u=todo.pop();z+=1
  for w in adj[u]:
   if w not in seen:seen.add(w);todo.append(w)
 sizes.append(z)
# The single nominal35-vertex component is legal in the SAFE RELAXATION regardless of these sizes.
rho35=1+(35-1).bit_length();assert rho35==7 and 76>=35-1 and rho35<=21
out={'status':'PASS','scope':'small graph exact definition of U; explicit global threshold maximizer; no H or real component construction','small_cases':small,'small_graphs_total':sum(v['all_labeled_graphs'] for v in small),'U35_76':value,'relaxed_single_component':{'s':35,'m':76,'rho':rho35,'isolates_declared':0},'threshold_sequence':sequence,'graph_edges':edge,'graph_degree_histogram':dict(Counter(ds)),'actual_graph_component_sizes':sorted(sizes,reverse=True),'actual_graph_isolates':sum(q==0 for q in ds),'cpu_seconds':time.process_time()-st}
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('small_cases','threshold_sequence','graph_edges')})
