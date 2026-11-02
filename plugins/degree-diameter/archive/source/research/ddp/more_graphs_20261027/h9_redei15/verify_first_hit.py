"""Independent expanded-edge acceptance of the first Redei15 append step."""
from pathlib import Path
from collections import Counter, deque
import json
import time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
START=time.process_time()
hit=json.loads((OUT/'production/first_hit.json').read_text())


def read(path, build_adjacency):
    with path.open() as f:
        n,m=map(int,f.readline().split())
        assert n<65536
        codes=set();adj=[[] for _ in range(n)] if build_adjacency else None
        for line in f:
            u,v=map(int,line.split())
            assert 0<=u<n and 0<=v<n and u!=v
            if u>v:u,v=v,u
            code=(u<<16)|v
            assert code not in codes
            codes.add(code)
            if adj is not None:adj[u].append(v);adj[v].append(u)
    assert len(codes)==m
    return n,m,codes,adj


oldn,oldm,oldedges,_=read(ROOT/hit['source_graph'],False)
n,m,edges,adj=read(ROOT/hit['graph_file'],True)
assert n==oldn+1==42399 and oldm==245889 and m==245901
z=n-1
neighbors=sorted(adj[z])
assert neighbors==hit['full_neighbor_set'] and len(neighbors)==12
expected={(v<<16)|z for v in neighbors}
assert oldedges<=edges and edges-oldedges==expected
degrees=list(map(len,adj))
assert max(degrees)==12
old_neighbor_degrees=[degrees[v]-1 for v in neighbors]
assert old_neighbor_degrees==hit['neighbors_old_degrees']
dist=[-1]*n;dist[z]=0;todo=deque([z])
while todo:
    u=todo.popleft()
    for v in adj[u]:
        if dist[v]<0:dist[v]=dist[u]+1;todo.append(v)
assert min(dist)>=0 and max(dist)==5
assert n>1+12*sum(11**j for j in range(4))
result=dict(valid=True,n=n,m=m,simple=True,connected=True,max_degree=12,
            exact_diameter=5,diameter_scope='Freshone-rootBFSplusalloldedgesretainedandtheinheritedvalidD5source;noall-sourceBFSrepeat.',
            roots_checked=1,new_root=z,new_root_eccentricity=5,
            distance_histogram=dict(sorted(Counter(dist).items())),new_old_bad_pairs=0,
            all_old_edges_retained=True,new_edges_only_incident_to_new_root=True,
            source_n=oldn,source_m=oldm,source_graph=hit['source_graph'],
            new_graph=hit['graph_file'],neighbors=neighbors,
            independent_from_search_caches=True,CPU_seconds=time.process_time()-START,
            public_baseline=42342,mathematical_improvement=57,
            formal_Lean_complete=False)
(OUT/'production/independent_newroot42399.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
