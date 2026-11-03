#!/usr/bin/env python3
"""Exact triangle incidence and minimum triangle-destruction cover for Brown57.
This is a necessary condition for insertion, not a search for complete graphs.
"""
from pathlib import Path
from itertools import combinations, product
from collections import Counter,deque
import json,time
start=time.monotonic()
root=Path(__file__).parent
rows=[list(map(int,line.split())) for line in (root/'brown57.edges').read_text().splitlines()]
n,m=rows[0];adj=[set() for _ in range(n)]
for u,v in rows[1:]:adj[u].add(v);adj[v].add(u)
triangles=[(u,v,w) for u in range(n) for v in sorted(adj[u]) if u<v for w in sorted(adj[u]&adj[v]) if v<w]
counts=Counter(v for t in triangles for v in t)
C={v for v in range(n) if len(adj[v])==7}
I={v for v in range(n) if v not in C and not adj[v]&C}
E=set(range(n))-C-I
assert all(not (adj[v]&C) for v in C)
assert len(triangles)==56 and all(len(adj[u]&adj[v])<=1 for u,v in rows[1:])
assert all(counts[v]==4 for v in I) and all(counts[v]==3 for v in E) and all(counts[v]==0 for v in C)
III=[t for t in triangles if set(t)<=I]
IEE=[t for t in triangles if len(set(t)&I)==1 and len(set(t)&E)==2]
assert len(III)==14 and len(IEE)==42
# Any 7-triangle cover must use only all-internal triangles, with no overlap.
parallel_classes=[]
for ix in combinations(range(len(III)),7):
 selected=[III[i] for i in ix]
 if len(set(v for t in selected for v in t))==21:
  parallel_classes.append([list(t) for t in selected])
assert len(parallel_classes)==2
# Explicit deletion patterns meeting the lower bound, still only a necessary condition.
patterns=[]
for family in parallel_classes:
 for choice in product(range(3),repeat=7):
  removed=[list(combinations(t,2))[i] for t,i in zip(family,choice)]
  patterns.append([list(edge) for edge in removed])
assert len(patterns)==4374
(root/'seven_edge_deletion_patterns.json').write_text(json.dumps(patterns)+'\n')
result={'status':'EXACT_MINIMUM_FOR_DESTROYING_INTERNAL_TRIANGLE_EXCESS',
 'scope':'Necessary old-triangle destruction in Brown57 extensions to n=58 or n=59. No extension graph was constructed and no whole insertion family excluded.',
 'triangle_count':len(triangles),'triangles_by_internal_vertex_count':dict(Counter(len(set(t)&I) for t in triangles)),
 'triangles_at_vertex_histogram':dict(Counter(counts[v] for v in range(n))),
 'all_internal_triangles':[list(t) for t in III],
 'minimum_destroyed_old_triangles':7,'minimum_deleted_old_edges_for_this_condition':7,
 'minimum_cover_parallel_classes':parallel_classes,
 'necessary_deletion_patterns_at_7':len(patterns),
 'proof':'21 vertices each need to lose an old triangle; one old edge is in at most one old triangle; each old triangle contains at most 3 internal vertices. Seven are necessary. The displayed parallel classes show seven suffice for this condition only.',
 'wall_time_seconds':time.monotonic()-start,'cpu_limit':1}
(root/'triangle_edit_obstruction.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
