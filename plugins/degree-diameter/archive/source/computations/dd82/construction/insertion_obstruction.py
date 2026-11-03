#!/usr/bin/env python3
"""Exact finite premises for the Brown57 one-vertex insertion obstruction.
Reads the explicit edge file; does not import its generator.
"""
import json
from collections import Counter
from pathlib import Path

root=Path(__file__).parent
rows=[list(map(int,line.split())) for line in (root/'brown57.edges').read_text().splitlines()]
n,m=rows[0]
adj=[set() for _ in range(n)]
for u,v in rows[1:]: adj[u].add(v);adj[v].add(u)
C={v for v in range(n) if len(adj[v])==7}
I={v for v in range(n) if v not in C and not adj[v]&C}
E=set(range(n))-C-I
cover={v:len((adj[v]|{v})&I) for v in range(n)}
assert n==57 and m==224 and len(C)==8 and len(I)==21 and len(E)==28
assert all(len(adj[v])==(7 if v in C else 8) for v in range(n))
assert all(cover[v]==0 for v in C)
assert all(cover[v]<=5 for v in range(n))
rows=[]
for r in range(3):
 for k in range(min(8,2*r)+1):
  # k = |S minus C|; deleted-edge incidences imply k <= 2r.
  rows.append({'deleted_old_edges':r,'new_nonconic_neighbors':k,
               'upper_bound_internal_vertices_reached':5*k+r-(k+1)//2})
assert max(row['upper_bound_internal_vertices_reached'] for row in rows)<len(I)
result={'status':'EXACT_FINITE_PREMISES_CHECKED','n':n,'conic_C':sorted(C),'internal_I':sorted(I),
'external_E':sorted(E),'internal_closed_neighbor_histogram':dict(Counter(cover.values())),
'insertion_without_edits_uncovered_vertices':sorted(I),
'no_insertion_with_fewer_than_3_old_edge_deletions':True,'bounds':rows,
'scope':'One new vertex added to this Brown57 graph; arbitrary old-edge additions/deletions, at most two deletions. Not a global n58 exclusion.'}
(root/'insertion_obstruction.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
