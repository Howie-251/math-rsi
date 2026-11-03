"""Recover explicit C5 x A4 coordinates from public 120-edge-list automorphisms."""
import json
from pathlib import Path
from collections import deque
P=Path(__file__).resolve().parent
G=json.loads((P/'120_automorphism_generators.json').read_text())
identity=tuple(range(120))
def mul(p,q):return tuple(p[q[i]] for i in range(len(p)))
def power(p,k):
 z=tuple(range(len(p)))
 for _ in range(k):z=mul(z,p)
 return z
def closure(gs):
 seen={identity};todo=[identity]
 for p in todo:
  for q in gs:
   a=mul(p,q)
   if a not in seen:seen.add(a);todo.append(a)
 return todo
A=closure([tuple(x) for x in G]);print('group size',len(A));assert len(A)==60
assert len({x[0] for x in A})==len({x[60] for x in A})==60

def order(p):
 q=p;k=1
 while q!=identity:q=mul(q,p);k+=1
 return k
z=next(x for x in A if order(x)==5 and all(mul(x,y)==mul(y,x) for y in A))
s=next(x for x in A if order(x)==2)
t=next(x for x in A if order(x)==3 and len(closure([s,x]))==12)
sa=(1,0,3,2);ta=(1,2,0,3);e4=tuple(range(4))
coords={e4:identity}; todo=[e4]
for p in todo:
 for q,h in [(sa,s),(ta,t)]:
  a=mul(p,q);v=mul(coords[p],h)
  if a in coords:assert coords[a]==v
  else:coords[a]=v;todo.append(a)
assert len(coords)==12
labels={};source_map={}
for k in range(5):
 for h,x in coords.items():
  g=mul(power(z,k),x)
  labels[g]=(k,h)
  for b in (0,1):source_map[g[60*b]]=(b,k,h)
assert len(source_map)==120
adj=[set() for _ in range(120)];edges=set()
for line in (P/'graph_6_3_n120.txt').read_text().splitlines():
 if line.startswith('#'):continue
 u,v=map(int,line.split());edges.add((u,v));adj[u].add(v);adj[v].add(u)
volts=[[[],[]],[[],[]]]
for b in (0,1):
 for v in sorted(adj[60*b]):
  c,k,h=source_map[v];volts[b][c].append((k,h))
print('volts',volts)
idx={v:k for k,v in source_map.items()}
recovered=set()
for u,(b,k,h) in source_map.items():
 for c in (0,1):
  for l,q in volts[b][c]:
   v=idx[c,(k+l)%5,mul(h,q)];recovered.add(tuple(sorted((u,v))))
assert recovered==edges
out={'group':'C5 x A4','multiplication':'(k,p)*(l,q)=((k+l) mod 5, tuple(p[q[i]] for i in 0..3))','source_vertices':[source_map[i] for i in range(120)],'voltage_sets':volts,'edge_count':len(edges),'recovered_equals_source':True,'coordinate_generators_source_images':{'central5':z[0],'involution':s[0],'order3':t[0]}}
(P/'120_recovered_construction.json').write_text(json.dumps(out,indent=2)+'\n')
print('all edges match',len(edges))
