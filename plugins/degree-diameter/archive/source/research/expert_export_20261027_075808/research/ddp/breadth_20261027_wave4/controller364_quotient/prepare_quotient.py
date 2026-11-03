from pathlib import Path
from collections import Counter
import json, time

P = Path(__file__).resolve().parent
B = P.parent.parent / 'breadth_20261027_wave3'
t = time.process_time()
source = json.loads((B / 'hexagon_partial_fold_scout/Q_data.json').read_text())['H3_graph']
perm = json.loads((P / 'root_two_anchor_refinement.json').read_text())['permutation']
assert sorted(perm) == list(range(364)) and all(perm[perm[u]] == u for u in range(364))
source_edges = {(u,v) for u,row in enumerate(source) for v in row if u<v}
assert {(min(perm[u],perm[v]),max(perm[u],perm[v])) for u,v in source_edges} == source_edges
orb = [-1] * 364
members = []
for u in range(364):
    if orb[u] < 0:
        row = sorted({u,perm[u]})
        i = len(members)
        for v in row: orb[v] = i
        members.append(row)
assert len(members) == 192
edge_sources = {}
loops = []
for u,v in sorted(source_edges):
    a,b = sorted((orb[u],orb[v]))
    if a == b:
        loops.append([u,v])
    else:
        edge_sources.setdefault((a,b),[]).append([u,v])
edges = sorted(edge_sources)
adj = [[] for _ in members]
for u,v in edges:
    adj[u].append(v);adj[v].append(u)
assert max(map(len,adj)) <= 4
missing = []
diagonal = []
counts = Counter()
for root in range(len(adj)):
    states = {(root,-1):1}
    for _ in range(5):
        nxt = {}
        for (u,prev),count in states.items():
            for v in adj[u]:
                if v != prev: nxt[(v,u)] = nxt.get((v,u),0) + count
        states = nxt
    endpoints = [0] * len(adj)
    for (u,prev),count in states.items(): endpoints[u] += count
    counts.update(endpoints)
    missing.extend([root,v] for v,c in enumerate(endpoints) if not c)
    diagonal.append(endpoints[root])
fixed_orbits = [i for i,row in enumerate(members) if len(row)==1]
deficit = {i:4-len(row) for i,row in enumerate(adj) if len(row)<4}
mapping = dict(source_vertices=364,quotient_vertices=192,source_to_orbit=orb,orbit_members=members,
               fixed_orbits=fixed_orbits,discarded_source_loops=loops,
               quotient_edge_to_source_edges=[dict(edge=list(e),source_edges=edge_sources[e]) for e in edges])
(P/'quotient_mapping.json').write_text(json.dumps(mapping,indent=2)+'\n')
with (P/'quotient.edges').open('w') as f:
    print(len(adj),len(edges),file=f)
    for u,v in edges:print(u,v,file=f)
with (P/'quotient_input.txt').open('w') as f:
    print(len(adj),len(edges),file=f)
    for u,v in edges:print(u,v,file=f)
out = dict(status='EXPLICIT_INVOLUTION_QUOTIENT_COMPLETE',n=192,m=len(edges),simple=True,
           degree_histogram=dict(Counter(map(len,adj))),fixed_vertices=len(fixed_orbits),
           fixed_orbit_degree_histogram=dict(Counter(len(adj[u]) for u in fixed_orbits)),
           deleted_loops=len(loops),source_edge_multiplicity_histogram=dict(Counter(map(len,edge_sources.values()))),
           deficit_vertices=len(deficit),deficit_slots=sum(deficit.values()),deficits=deficit,
           exact_NB5_missing_ordered_pairs=len(missing),exact_NB5_missing_unordered_offdiag=sum(u<v for u,v in missing),
           exact_NB5_diagonal_zero=[u for u,c in enumerate(diagonal) if not c],
           exact_NB5_endpoint_count_histogram=dict(sorted(counts.items())),
           missing_ordered_pairs=missing,ordinary_BFS_performed=False,
           inherited_diameter_bound=5,CPU_seconds=time.process_time()-t)
(P/'quotient_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['missing_ordered_pairs','deficits','exact_NB5_endpoint_count_histogram']},indent=2))
print('deficits',deficit)
