"""Bind the author's 760 source and freeze the specified two-edge rule.

No shortest-path computation or candidate coverage test is performed.
"""
import collections
import json
import time
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent
author = OUT / "source760.author.edges.txt"
literal = []
for row in author.read_text().splitlines():
    if row.strip() and not row.startswith("#"):
        literal.append(tuple(sorted(map(int, row.split()))))
edges = set(literal)
n, m = 760, len(edges)
assert len(literal) == m == 1520
assert all(0 <= u < v < n for u,v in edges)
adj = [set() for _ in range(n)]
for u,v in edges:
    adj[u].add(v)
    adj[v].add(u)
assert all(len(row) == 4 for row in adj)
base_edges = sorted(e for e in edges if e[1] < 728)
layer_edges = sorted(e for e in edges if e[0] >= 728)
cross_edges = sorted(e for e in edges if e[0] < 728 <= e[1])
assert (len(base_edges),len(layer_edges),len(cross_edges)) == (1424,32,64)
assert all(u < 364 <= v < 728 for u,v in base_edges)
flags = []
for w in range(728,760):
    point = sorted(u for u in adj[w] if u < 364)
    line = sorted(u for u in adj[w] if 364 <= u < 728)
    layer = sorted(u for u in adj[w] if u >= 728)
    assert len(point) == len(line) == 1 and len(layer) == 2
    flag = (point[0],line[0])
    assert flag not in edges
    flags.append({"layer_vertex":w,"original_flag":list(flag),"layer_neighbors":layer})
restored_flags = {tuple(row["original_flag"]) for row in flags}
assert len(restored_flags) == 32
original = set(base_edges) | restored_flags
original_degree = [0]*728
for u,v in original:
    original_degree[u] += 1
    original_degree[v] += 1
assert len(original) == 1456 and set(original_degree) == {4}
seen, cycles = set(), []
for first in range(728,760):
    if first in seen:
        continue
    prev, cur, cycle = -1, first, []
    while cur not in seen:
        seen.add(cur)
        cycle.append(cur)
        nxt = sorted(v for v in adj[cur] if v>=728 and v!=prev)[0]
        prev, cur = cur, nxt
    assert cur == first
    cycles.append(cycle)
assert sorted(map(len,cycles)) == [8,8,16]
header = OUT / "source760.header.edges"
header.write_text(f"{n} {m}\n"+"".join(f"{u} {v}\n" for u,v in sorted(edges)))
records=[]
for eid,e in enumerate(base_edges):
    for fid,f in enumerate(layer_edges):
        endpoints = sorted(set(e+f))
        assert len(endpoints) == 4
        records.append({"ordinal":len(records),"base_edge_index":eid,"layer_edge_index":fid,
                        "deleted_edges":[list(e),list(f)],"endpoint_set":endpoints,
                        "new_neighbors":endpoints})
assert len(records) == 45568
source_urls={
    "main_table":"https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html",
    "author_directory":"https://github.com/f4t4nt/degree-diameter-graphs/tree/main/graphs/deg4/dia6",
    "author_README":"https://raw.githubusercontent.com/f4t4nt/degree-diameter-graphs/main/graphs/deg4/dia6/README.md",
    "author_literal":"https://raw.githubusercontent.com/f4t4nt/degree-diameter-graphs/main/graphs/deg4/dia6/deg4-dia6-n760.edges.txt"}
html=(OUT/'main_table_fresh.html').read_text()
cell=html[html.index('760')-160:html.index('760')+100]
assert 'desc_g6.html#46' in cell and '<b' not in cell.lower() and '<strong' not in cell.lower()
profile={"status":"SOURCE_BOUND_AND_COMPLETE_SPECIFIED_CANDIDATE_LIST_FROZEN",
         "source_file":str(header),"author_literal_file":str(author),"source_n":n,"source_m":m,
         "source_degree_histogram":dict(collections.Counter(map(len,adj))),"delta":4,"D":6,
         "savedL":760,"baseline_checked_date":"2026-10-27","baseline_bold":False,
         "baseline_cell_html":cell,"base_point_labels":[0,363],"base_line_labels":[364,727],
         "inserted_layer_labels":[728,759],"base_edges":len(base_edges),"cross_edges":len(cross_edges),
         "layer_edges":len(layer_edges),"layer_cycle_lengths":sorted(map(len,cycles)),
         "each_layer_vertex_neighbors":{"point":1,"line":1,"layer":2},
         "restored_incidence_n":728,"restored_incidence_m":1456,"restored_incidence_all_degree_4":True,
         "source_diameter_evidence":"verification.author.txt; author's all-source BFS reused, not rerun",
         "exact_source_Wiki_lookup":"No exact 760 or deg4/dia6 experiment found in current method ledger/experiment notes",
         "original_recipe_group_binding":"Sylow-2 orbit description is author's claim; explicit group permutations not needed or recovered",
         "candidate_count":len(records),"newlabel":760,"candidate_n":761,"candidate_m":1522,
         "actual_candidate_D":None,"candidate_BFS_runs":0,"source_BFS_runs":0,
         "CPU_seconds":time.process_time()-START,"sources":source_urls,
         "preparation_terminal":"COMPLETE_NO_CANDIDATES_EVALUATED","producer":"/root/expert_brief_evidence"}
frozen={**profile,"order":"base_edge sorted lexicographically outer; layer_edge sorted lexicographically inner",
        "base_edges_table":base_edges,"layer_edges_table":layer_edges,
        "check_roots":"For each candidate use closed source R2(endpoint_set), plus new vertex 760; at most 69 roots",
        "records":records}
binding={"source_file":str(header),"flags":flags,"layer_cycles":cycles,
         "base_edges":base_edges,"layer_edges":layer_edges,
         "restoration":"Remove all layer vertices and restore each recorded original_flag; obtain original 728/1456 incidence literal without geometry reconstruction"}
for name,data in [("frozen.json",frozen),("SOURCE_PROFILE.json",profile),("RECIPE_BINDING.json",binding)]:
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,separators=(',',':'))+'\n')
print(json.dumps(profile,ensure_ascii=False))
