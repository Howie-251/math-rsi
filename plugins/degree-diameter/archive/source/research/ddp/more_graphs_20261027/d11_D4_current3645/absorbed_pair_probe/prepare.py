"""Freeze original-spread two-edge insertions; no BFS or candidate search."""
import collections
import json
import re
import time
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent
PARENT = OUT.parent
SOURCE = PARENT / "source3645.header.edges"
rows = SOURCE.read_text().splitlines()
n, m = map(int, rows[0].split())
edges = {tuple(sorted(map(int, row.split()))) for row in rows[1:] if row.strip()}
assert (n, m, len(edges)) == (3645, 20044, 20044)
adj = [set() for _ in range(n)]
for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)
free = [v for v in range(n) if len(adj[v]) < 11]
assert free == [3456, 3489, 3564, 3571, 3583, 3603, 3643]
assert all(len(adj[v]) == 10 for v in free)

base_edges = {e for e in edges if e[1] < 3444}
author_steps = []
for row in (PARENT / "insertions.author.txt").read_text().splitlines():
    if not row.strip() or row.startswith("#"):
        continue
    z, deleted, joined = re.fullmatch(r"(\d+): deleted (.*?); joined to (.*)", row).groups()
    deleted = [tuple(sorted(map(int, e))) for e in re.findall(r"(\d+)-(\d+)", deleted)]
    joined = list(map(int, joined.split()))
    point_choices = sorted({u // 2 for u in joined if u < 1640 and (u ^ 1) in joined})
    assert len(point_choices) == 1
    author_steps.append({"newlabel": int(z), "point_p": point_choices[0]})
    base_edges.update(e for e in deleted if e[1] < 3444)
assert len(author_steps) == 201
base_adj = [set() for _ in range(3444)]
for u, v in base_edges:
    base_adj[u].add(v)
    base_adj[v].add(u)
assert len(base_edges) == 18942 and all(len(row) == 11 for row in base_adj)

line_by_signature = {}
for line in range(1640, 3280):
    signature = tuple(sorted(v for v in base_adj[line] if v < 1640))
    assert len(signature) == 10 and signature not in line_by_signature
    line_by_signature[signature] = line
twin_to_line = {}
for twin in range(3280, 3444):
    signature = tuple(sorted(v for v in base_adj[twin] if v < 1640))
    assert len(signature) == 10
    twin_to_line[twin] = line_by_signature[signature]
used_by = collections.defaultdict(list)
for step in author_steps:
    used_by[step["point_p"]].append(step["newlabel"])

records, point_hosts = [], []
missing_by_host, valid_by_host, valid_by_used = collections.Counter(), collections.Counter(), collections.Counter()
root_hist = collections.Counter()
for p in range(820):
    choices = []
    for u in (2 * p, 2 * p + 1):
        twins = sorted(v for v in base_adj[u] if v >= 3280)
        assert len(twins) == 1
        twin = twins[0]
        line = twin_to_line[twin]
        assert line in base_adj[u]
        choices.append({"T": twin, "L": line})
    point_hosts.append({"point_p": p, "point_copies": [2*p, 2*p+1], "hosts_per_copy": choices,
                        "author_insertions": used_by[p]})
    for type0 in ("T", "L"):
        for type1 in ("T", "L"):
            hosts = [choices[0][type0], choices[1][type1]]
            cuts = [tuple(sorted((2*p+i, hosts[i]))) for i in range(2)]
            kind = type0 + type1
            if not all(e in edges for e in cuts):
                missing_by_host[kind] += 1
                continue
            endpoints = sorted({v for e in cuts for v in e})
            assert len(endpoints) == 4 and all(len(adj[v]) == 11 for v in endpoints)
            neighbors = sorted(set(endpoints) | set(free))
            assert len(neighbors) == 11
            affected = sorted(set(endpoints).union(*(adj[v] for v in endpoints)))
            record = {"ordinal": len(records), "point_p": p, "used_in_author_chain": bool(used_by[p]),
                      "author_insertions": used_by[p], "point_copies": [2*p, 2*p+1],
                      "host_types": [type0, type1], "hosts": hosts,
                      "deleted_edges": [list(e) for e in cuts], "endpoint_set": endpoints,
                      "new_neighbors": neighbors, "affected_roots": affected,
                      "root_count": len(affected), "newlabel": n, "candidate_n": n+1,
                      "candidate_m": m-2+len(neighbors)}
            records.append(record)
            valid_by_host[kind] += 1
            valid_by_used["used" if used_by[p] else "unused"] += 1
            root_hist[len(affected)] += 1

cover = json.loads((PARENT / "COVER_RESULT.json").read_text())
assert cover["source_n"] == n and cover["source_m"] == m and cover["free_vertices"] == free
missing = cover["missing"]
assert len(missing) == 743 and len(set(missing)) == 743
cover_mask = ((1 << n) - 1) ^ sum(1 << v for v in missing)
cache = {"status": "REFORMATTED_EXISTING_EXACT_MULTISOURCE_R3_NO_NEW_BFS",
         "source_file": str(SOURCE), "source_n": n, "source_m": m, "free_ports": free,
         "radius": 3, "covered_count": n-len(missing), "missing_count": len(missing),
         "missing": missing, "word_layout": "word j bit k is vertex 64*j+k; final padding zero",
         "covered_words_u64": [(cover_mask >> (64*j)) & ((1 << 64)-1) for j in range((n+63)//64)],
         "reused_evidence": str(PARENT / "COVER_RESULT.json"), "new_BFS_runs": 0}

stats = {"status": "FROZEN_LITERAL_CANDIDATES_NOT_EVALUATED", "source_file": str(SOURCE),
         "source_n": n, "source_m": m, "delta": 11, "D": 4, "savedL": 3645,
         "candidate_n": n+1, "candidate_m": 20053, "raw_points": 820, "raw_host_choices": 3280,
         "candidate_count": len(records), "current_missing_edge_rejections": sum(missing_by_host.values()),
         "missing_by_host": dict(missing_by_host), "valid_by_host": dict(valid_by_host),
         "valid_by_author_used": dict(valid_by_used), "original_base_n": 3444,
         "original_base_m": len(base_edges), "restored_original_base_all_degree_11": True,
         "original_twin_count": 164, "unique_matching_linecopy_count": len(set(twin_to_line.values())),
         "author_step_count": 201, "distinct_author_points": sum(bool(z) for z in used_by.values()),
         "repeated_author_points": [{"point_p": p, "insertions": z} for p,z in sorted(used_by.items()) if len(z)>1],
         "affected_root_count_histogram": dict(sorted(root_hist.items())),
         "affected_root_count_max": max(root_hist), "free_ports": free,
         "candidate_distance_computations": 0, "BFS_runs": 0,
         "actual_candidate_D": None, "CPU_seconds": time.process_time()-START,
         "producer": "/root/expert_brief_evidence", "pending": ["producer finite candidate evaluation"]}
frozen = {**stats, "order": "point_p increasing; first host T then L; second host T then L; skip absent current edges",
          "free_R3_cache": str(OUT / "FREE_R3_CACHE.json"), "records": records}
binding = {"status": "RECONSTRUCTED_FROM_CURRENT_EDGESET_PLUS_ORIGINAL_BASE_DELETIONS",
           "source_file": str(SOURCE), "author_insertions_file": str(PARENT / "insertions.author.txt"),
           "base_n": 3444, "base_m": len(base_edges), "twin_to_spread_linecopy": twin_to_line,
           "point_hosts": point_hosts, "author_steps": author_steps,
           "matching_rule": "Exact equality of original neighbors in pointcopies 0..1639"}
for name, obj in [("frozen.json", frozen), ("HOST_BINDING.json", binding),
                  ("FREE_R3_CACHE.json", cache), ("PREPARATION_RESULT.json", stats)]:
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2)+"\n")
print(json.dumps(stats, ensure_ascii=False))
