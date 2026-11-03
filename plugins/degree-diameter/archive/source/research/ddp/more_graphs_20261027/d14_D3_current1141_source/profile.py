"""Reproduce the saved literal profile only; does not fetch or BFS."""
from collections import Counter
from pathlib import Path
import json

p=Path(__file__).resolve().parent
rows=[tuple(sorted(map(int,r.split()))) for r in (p/'source1141.author.edges').read_text().splitlines() if r.strip() and not r.startswith('#')]
edges=set(rows)
n=1+max(v for e in edges for v in e)
adj=[set() for _ in range(n)]
for u,v in edges:
    adj[u].add(v);adj[v].add(u)
degree=list(map(len,adj))
print(json.dumps({'source_n':n,'source_m':len(edges),'degree_histogram':dict(Counter(degree)),
                  'duplicates':len(rows)-len(edges),'loops':sum(u==v for u,v in edges),
                  'free_vertices':[v for v,d in enumerate(degree) if d<14],
                  'minSatN':min(sum(degree[w]==14 for w in a) for a in adj),
                  'BFS':0,'candidate_graphs':0},indent=2))
