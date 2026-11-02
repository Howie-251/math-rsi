"""Independent full graph check from a saved expanded edge list."""
from pathlib import Path
import collections,itertools,json,sys
p=Path(sys.argv[1]);data=json.loads(p.read_text());n=data["n"];raw=data["edges"]
assert all(0<=u<n and 0<=v<n and u!=v for u,v in raw)
edges={tuple(sorted(e)) for e in raw};assert len(edges)==len(raw)
ns=[set() for _ in range(n)]
for u,v in edges:ns[u].add(v);ns[v].add(u)
bad=[];diameter=0
for u in range(n):
    dist={u:0};q=collections.deque([u])
    while q:
        x=q.popleft()
        for y in ns[x]:
            if y not in dist:dist[y]=dist[x]+1;q.append(y)
    for v in range(u+1,n):
        d=dist.get(v)
        if d is None or d>2:bad.append(dict(pair=[u,v],distance=d,common_neighbors=sorted(ns[u]&ns[v])))
        if d is not None:diameter=max(diameter,d)
report=dict(n=n,edges=len(edges),degrees=[len(s) for s in ns],max_degree=max(map(len,ns)),
    bad_pair_count=len(bad),bad_pairs=bad,diameter=diameter if all(x["distance"] is not None for x in bad) else None,
    valid_target=(58<=n<=61 and max(map(len,ns))<=8 and not bad))
p.with_suffix(".verification.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps({k:v for k,v in report.items() if k not in ("degrees","bad_pairs")}))
