#!/usr/bin/env python3
from pathlib import Path
import json

R=Path(__file__).resolve().parent
PROJECT=R.parents[3]
D=json.loads((PROJECT/'research/ddp/m1_fullgraph_repair/diagnosis.json').read_text())
edges=D['C13_quotient']['edge_voltages']
with (R/'base.txt').open('w')as f:
 print(54,189,13,file=f)
 for edge in edges:print(*edge,file=f)
def original(base,x):return (base//27)*351+x*27+base%27
expanded={tuple(sorted((original(u,x),original(v,(x+z)%13))))for u,v,z in edges for x in range(13)}
source=PROJECT/D['source'];lines=source.read_text().splitlines()
assert expanded=={tuple(map(int,line.split()))for line in lines[1:]}
adj=[[]for _ in range(54)]
for eid,(u,v,z)in enumerate(edges):adj[u].append((v,eid,1));adj[v].append((u,eid,-1))
def extend(form,eid,sgn):
 d=dict(form);d[eid]=(d.get(eid,0)+sgn)%13
 if not d[eid]:del d[eid]
 return tuple(sorted(d.items()))
with (R/'routes.txt').open('w')as f:
 print(54*54,file=f)
 for root in range(54):
  reached={(root,())};frontier=reached.copy()
  for depth in range(4):
   new={(v,extend(form,e,sgn))for u,form in frontier for v,e,sgn in adj[u]}-reached
   reached.update(new);frontier=new
  buckets=[set()for _ in range(54)]
  for v,form in reached:buckets[v].add(form)
  for v,forms in enumerate(buckets):
   assert len(forms)==D['C13_quotient']['formal_counts'][root][v]
   print(root,v,len(forms),file=f)
   for form in sorted(forms):print(len(form),*(a for pair in form for a in pair),file=f)
print('Exact source-edge equality; exported54basevertices,189edges,2916short-route sets.')
