from array import array
from collections import Counter
import gzip
import json
import pathlib
import time

HERE = pathlib.Path(__file__).resolve().parent
N = 186033
CAP = 11
start = time.process_time()
assert json.loads((HERE / "DOWNLOAD_HANDLE.json").read_text())["status"] == "COMPLETE"
keys = set()
rows = set()
row_entries = 0
comments = []
with gzip.open(HERE / "source186033.adjlist.gz", "rt") as source:
    for line in source:
        if not line.strip():
            continue
        if line.startswith("#"):
            comments.append(line.rstrip())
            continue
        values = list(map(int, line.split()))
        v = values[0]
        assert 0 <= v < N and v not in rows
        rows.add(v)
        for w in values[1:]:
            assert 0 <= w < N and v != w
            a, b = sorted((v, w))
            keys.add(a * N + b)
            row_entries += 1
assert len(rows) == N
g = [[] for _ in range(N)]
with (HERE / "source186033.header.edges").open("w") as output:
    output.write(f"{N} {len(keys)}\n")
    for key in sorted(keys):
        a, b = divmod(key, N)
        g[a].append(b)
        g[b].append(a)
        output.write(f"{a} {b}\n")
del keys
degrees = [len(a) for a in g]
assert max(degrees) <= CAP and min(degrees) > 0
sat = bytearray(d == CAP for d in degrees)
satN = bytearray(sum(sat[w] for w in a) for a in g)
free = [v for v, d in enumerate(degrees) if d < CAP]
prototypes = [v for v in range(N) if satN[v] <= 1]
records = [{
    "prototype": v, "degree": degrees[v], "satN": satN[v],
    "saturated_neighbors": [w for w in g[v] if sat[w]],
    "free_neighbors": [w for w in g[v] if not sat[w]],
    "full_neighborhood": sorted(g[v]),
    "neighbors_old_degrees": {str(w): degrees[w] for w in sorted(g[v])},
    "source_partition": "old182618" if v < 182618 else "append3415"
} for v in prototypes]
(HERE / "degrees.u8.bin").write_bytes(bytes(degrees))
(HERE / "saturated_neighbor_counts.u8.bin").write_bytes(satN)
offsets = array("I", [0])
neighbors = array("I")
for a in g:
    neighbors.extend(sorted(a))
    offsets.append(len(neighbors))
with (HERE / "adjacency.csr.u32le.bin").open("wb") as output:
    array("I", [N, len(neighbors)]).tofile(output)
    offsets.tofile(output)
    neighbors.tofile(output)
(HERE / "PROTOTYPES.json").write_text(json.dumps({
    "source_n": N, "source_m": len(neighbors)//2, "delta": CAP,
    "records": records}, indent=2) + "\n")
profile = {
    "status": "ACTUAL_SOURCE_PROFILE_COMPLETE",
    "source_n": N, "source_m": len(neighbors)//2,
    "source_file": str(HERE / "source186033.adjlist.gz"),
    "normalized_edge_file": str(HERE / "source186033.header.edges"),
    "source_comments": comments, "format": "NetworkX adjacency list; normalized unordered edges",
    "input_rows": len(rows), "input_neighbor_entries": row_entries,
    "degree_histogram": dict(sorted(Counter(degrees).items())),
    "free_vertices": len(free), "free_slots": sum(CAP-d for d in degrees),
    "saturated_neighbor_histogram": dict(sorted(Counter(satN).items())),
    "minSatN": min(satN), "zero_satN_prototypes": sum(x == 0 for x in satN),
    "one_satN_prototypes": sum(x == 1 for x in satN),
    "prototype_count_satN_le1": len(prototypes),
    "prototype_partitions": dict(Counter(r["source_partition"] for r in records)),
    "prediction": "SUPPORTED" if prototypes else "REFUTED",
    "source_full_diameter_BFS": 0, "graph_candidates": 0,
    "csr_layout": "native little-endian uint32 n,2m; n+1 offsets;2m neighbor IDs",
    "profile_CPU_seconds": time.process_time()-start
}
(HERE / "SOURCE_PROFILE.json").write_text(json.dumps(profile, indent=2) + "\n")
print(json.dumps(profile, indent=2))
