"""Independent ordinary queue BFS over literal files; imports no geometry/generator."""
from collections import Counter, deque
from pathlib import Path
import json
import time

BASE = Path(__file__).resolve().parent


def read(path):
    with path.open() as f:
        n,m = map(int,next(f).split())
        edges = [tuple(map(int,line.split())) for line in f if line.strip()]
    assert len(edges) == m and len(set(edges)) == m
    assert all(0 <= a < b < n for a,b in edges)
    adj = [[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b)
        adj[b].append(a)
    return n,m,set(edges),adj


def main():
    start = time.process_time()
    n0,m0,e0,g0 = read(BASE/"source_d5_D2_n21.edges")
    n,m,e,g = read(BASE/"graph_d5_D2_n22.edges")
    pins = json.loads((BASE/"PINS.json").read_text())["pins"]
    assert (n0,m0,n,m) == (21,50,22,55)
    assert {edge for edge in e if edge[1] < 21} == e0
    assert e-e0 == {(s,21) for s in pins}
    assert Counter(map(len,g0)) == Counter({4:5,5:16})
    assert Counter(map(len,g)) == Counter({5:22})
    spare = {v for v in range(n0) if len(g0[v]) < 5}
    assert set(pins) == spare
    covered = spare | {w for v in spare for w in g0[v]}
    assert covered == set(range(n0))
    root_rows = []
    pair_hist = Counter()
    for root in range(n):
        dist = [-1]*n
        dist[root] = 0
        q = deque([root])
        while q:
            v = q.popleft()
            for w in g[v]:
                if dist[w] < 0:
                    dist[w] = dist[v]+1
                    q.append(w)
        assert min(dist) == 0 and max(dist) == 2
        counts = [dist.count(k) for k in range(3)]
        assert counts == [1,5,16]
        root_rows.append({"root":root,"counts":counts,"eccentricity":max(dist)})
        for target in range(root+1,n):
            pair_hist[dist[target]] += 1
    assert pair_hist == Counter({1:55,2:176})
    result = {"status":"PASS","method":"ordinary all-roots queue BFS from literal final edge list",
        "imports_generator":False,"source_BFS_roots":0,"final_BFS_roots":22,
        "n":n,"m":m,"simplicity":True,"degree_histogram":{"5":22},"diameter":2,
        "unordered_pair_distances":dict(sorted(pair_hist.items())),
        "all_root_histograms":[1,5,16],"all_root_eccentricities":2,
        "exact_old_edge_retention":True,"closed_spare_coverage":len(covered),
        "final_spare_vertices":[],"process_CPU_seconds":time.process_time()-start,
        "roots":root_rows}
    (BASE/"INDEPENDENT_VALIDATION.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k != "roots"}))


if __name__ == "__main__":
    main()
