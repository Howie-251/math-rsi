"""Independent literal-edge acceptance; inherit only the published old D5 fact."""
from pathlib import Path
from collections import Counter, deque
from datetime import datetime, timezone
import json
import time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
start=time.process_time()
hit=json.loads((OUT/'first_hit.json').read_text())
n0,m0=51417,324451
old_edges=set()
old_degrees=[0]*n0
seen_rows=set()
with (OUT.parent/'source51417.adjlist.txt').open() as stream:
    for line in stream:
        if not line.strip() or line.lstrip().startswith('#'): continue
        row=list(map(int,line.split()))
        u,*neighbors=row
        assert 0<=u<n0 and u not in seen_rows
        seen_rows.add(u)
        assert len(neighbors)==len(set(neighbors)) and u not in neighbors
        old_degrees[u]=len(neighbors)
        for v in neighbors:
            assert 0<=v<n0
            if u<v: old_edges.add((u,v))
assert len(seen_rows)==n0 and len(old_edges)==m0 and sum(old_degrees)==2*m0

graph=ROOT/hit['graph_file']
with graph.open() as stream:
    n,m=map(int,next(stream).split())
    edges=set()
    g=[[] for _ in range(n)]
    rows=0
    for line in stream:
        u,v=map(int,line.split())
        assert 0<=u<n and 0<=v<n and u!=v
        edge=(min(u,v),max(u,v))
        assert edge not in edges
        edges.add(edge);rows+=1
        g[u].append(v);g[v].append(u)
assert (n,m,rows)==(51418,324461,324461)
pins=sorted(hit['full_neighbor_set'])
expected_added={(p,n0) for p in pins}
assert len(pins)==len(set(pins))==10
assert not (old_edges-edges) and edges-old_edges==expected_added
assert sorted(g[n0])==pins and max(map(len,g))==13
assert all(old_degrees[p]<13 for p in pins)
assert all(len(g[u])==old_degrees[u]+int(u in pins) for u in range(n0))

dist=[-1]*n;dist[n0]=0;q=deque([n0])
while q:
    u=q.popleft()
    for v in g[u]:
        if dist[v]<0: dist[v]=dist[u]+1;q.append(v)
assert min(dist)==0 and max(dist)==5
result=dict(status='ACCEPTED_COMPLETE_D13_D5_GRAPH_BY_RETAINED_BASE_AND_FRESH_NEWROOT',
    checked_UTC=datetime.now(timezone.utc).isoformat(),n=n,m=m,simple=True,
    maximum_degree=13,connected=True,new_root=n0,new_root_degree=len(pins),
    independently_rebuilt_from_literal_edges=True,original_public_raw_source_compared=True,
    source_n=n0,source_m=m0,all_source_edges_retained=True,
    new_neighbors=pins,neighbors_original_degrees=[old_degrees[p] for p in pins],
    roots_checked=1,source_allBFS_rerun=False,new_root_eccentricity=5,
    distance_histogram=dict(sorted(Counter(dist).items())),
    diameter_exact=5,
    allpair_D5_argument='Old-old distances inherit published51417sourceD5 because every original raw-source edge is retained. Every new-old pair is independently BFSchecked here. The newroot has eccentricity5, so diameter is exactly5.',
    graph_file=hit['graph_file'],complete_Lean_instance=False,
    CPU_seconds=time.process_time()-start)
(OUT/'independent_newroot51418.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
