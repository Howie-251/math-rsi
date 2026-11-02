#!/usr/bin/env python3
"""One released literal-GQ(4,4) spread augmentation; zero solver/all-roots BFS."""
import collections
import json
from pathlib import Path
import resource
import time

OUT = Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
START = time.process_time()

def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n')

# This file is only executed when the root-owned release has actually been saved.
release = json.loads((OUT / 'ROOT_GRAPH_RELEASE.json').read_text())
assert release['full_fixed_graph_execution_authorized'] is True
assert not (OUT / 'graph_d25_D3_n7242.edges').exists(), 'one fixed candidate, do not overwrite'
parameters = json.loads((OUT / 'PARAMETERS.json').read_text())
geometry = json.loads((OUT / 'GQ_AXIOM_CHECK.json').read_text())
assert geometry['status'] == 'PASS_GEOMETRY_READY_AWAIT_ROOT_GRAPH_RELEASE'
lines = [item['points'] for item in parameters['lines']]
point_lines = parameters['point_incident_lines']
spread = parameters['spread']
assert len(lines) == len(point_lines) == 85 and len(spread) == 17

# Literal old source. No source-distance BFS is used.
adj = [set() for _ in range(7225)]
for p in range(85):
    for l in range(85):
        u = 85*p+l
        for q in lines[l]:
            for m in point_lines[p]:
                v = 85*q+m
                if u != v:
                    adj[u].add(v)
assert all(u not in nbs for u,nbs in enumerate(adj))
assert all(u in adj[v] for u,nbs in enumerate(adj) for v in nbs)
source_hist = dict(sorted(collections.Counter(map(len,adj)).items()))
flags = {85*p+l for p in range(85) for l in point_lines[p]}
assert len(flags) == 425
assert source_hist == {24:425,25:6800}
assert {u for u,nbs in enumerate(adj) if len(nbs)==24} == flags
old_edges = {(u,v) for u,nbs in enumerate(adj) for v in nbs if u<v}
assert len(old_edges) == 90100
source_cpu = time.process_time() - START
write('SOURCE_CHECK.json', {
    'status':'PASS_LITERAL_SOURCE_GENERATED_NO_SOURCE_BFS',
    'vertices':7225,'edges':len(old_edges),'degree_histogram':source_hist,
    'degree24_vertices_exactly_incident_flags':True,
    'flags':425,'nonflags':6800,'simple':True,'reciprocal':True,
    'source_BFS_runs':0,'source_CPU_seconds':source_cpu,
    'source_rule':'old label85*p+l; distinct (p,l)~(q,m) iff p in m and q in l',
    'incidence_binding':'PARAMETERS.json lines[].points and point_incident_lines read literally'})

steps = []
used_pins = set()
for j,spread_item in enumerate(spread):
    assert spread_item['index'] == j
    pins = [85*p+l for p in spread_item['points'] for l in point_lines[p]]
    assert len(pins) == len(set(pins)) == 25
    assert not (set(pins) & used_pins)
    assert all(len(adj[p])==24 for p in pins)
    # Expand over the complete current graph, including every earlier new vertex.
    current_n = len(adj)
    distances = {p:0 for p in pins}
    frontier = set(pins)
    for d in (1,2):
        reached = {v for u in frontier for v in adj[u]} - distances.keys()
        distances.update({v:d for v in reached})
        frontier = reached
    uncovered = sorted(set(range(current_n))-distances.keys())
    assert not uncovered, (j,uncovered[:10],len(uncovered))
    prior_new_distances = {str(v): distances[v] for v in range(7225,current_n)}
    new = current_n
    assert new == 7225+j
    adj.append(set(pins))
    for p in pins:
        adj[p].add(new)
    assert max(map(len,adj)) <= 25
    used_pins.update(pins)
    steps.append({'step':j,'new_vertex':new,'spread_line':spread_item['line_id'],
        'slope_code':spread_item['slope_code'],'pins':pins,
        'pin_order':'spread five point IDs ascending, then each point five incidentline IDs ascending',
        'pins_count':25,'pin_degree_before':{'24':25},
        'current_n_before':current_n,'full_current_R2_covered':len(distances),
        'R2_uncovered_count':0,
        'R2_distance_histogram':dict(sorted(collections.Counter(distances.values()).items())),
        'earlier_new_vertex_distances_from_pin_union':prior_new_distances,
        'degree_cap_after':25})
assert used_pins == flags
assert len(adj) == 7242
assert dict(collections.Counter(map(len,adj))) == {25:7242}
assert all(u not in nbs for u,nbs in enumerate(adj))
assert all(u in adj[v] for u,nbs in enumerate(adj) for v in nbs)
edges = {(u,v) for u,nbs in enumerate(adj) for v in nbs if u<v}
assert len(edges)==90525 and old_edges <= edges
assert len(edges-old_edges)==425
# Exactly one final ordinary root BFS; no source or final all-roots run.
q=collections.deque([0])
seen={0}
while q:
    u=q.popleft()
    for v in adj[u]:
        if v not in seen:
            seen.add(v)
            q.append(v)
assert len(seen)==7242
with (OUT/'graph_d25_D3_n7242.edges').open('w') as stream:
    stream.write(f'{len(adj)} {len(edges)}\n')
    for u,v in sorted(edges):
        stream.write(f'{u} {v}\n')
CPU=time.process_time()-START
write('EXTENSION_STEPS.json',{'status':'ALL17_COMPLETE_CURRENT_R2_CHECKS_PASS',
    'steps':steps,'all425_flags_used_once':True,'source_vertices':7225,
    'final_vertices':7242,'final_edges':90525,'all_old_edges_retained':90100})
result={'status':'PRODUCER_PASS_FIXED7242_CANDIDATE_AWAIT_INDEPENDENT_ACCEPTANCE',
    'target_Delta':25,'target_D':3,'n':7242,'m':90525,
    'source_n':7225,'source_m':90100,'source_degree_histogram':source_hist,
    'geometry_points':85,'geometry_lines':85,'geometry_unique_projections':6800,
    'spread_lines':17,'pins_per_new_vertex':25,'new_vertices':17,'new_edges':425,
    'degree_histogram':{'25':7242},'simple':True,'reciprocal':True,
    'old_edges_retained':90100,'current_R2_checks':17,'R2_uncovered_count':0,
    'complete_current_graph_includes_previous_new_vertices':True,
    'final_root0_connectivity_vertices':7242,'ordinary_connectivity_BFS_runs':1,
    'source_BFS_runs':0,'candidate_allroots_BFS_runs':0,
    'producer_CPU_seconds':CPU,'worker_count':1,'solver_calls':0,
    'independent_acceptance':'PENDING_ROOT_SEPARATE_CHECK',
    'public_comparison':'ROOT_OWNED_SEPARATE_TASK_NO_RECORD_CLAIM',
    'concrete_Lean':'SEPARATE_PENDING_TASK',
    'actual_graphs_generated':1,'source_reproduction_counted_as_new_graph':False}
write('RESULT.json',result)
write('TERMINAL.json',{'status':'PRODUCER_LOCAL_FIXED_CONSTRUCTION_TERMINAL',
    'producer_result':result,'further_construction_running':False})
parameters['stage']='COMPLETE_FIXED7242_CANDIDATE_GENERATED'
parameters['old_vertex_label']=parameters.pop('old_vertex_label_prediction')
parameters['old_adjacency']=parameters.pop('old_adjacency_prediction')
parameters['new_vertex_label']=parameters.pop('new_vertex_label_prediction')
parameters['new_pins']=parameters.pop('new_pins_prediction')
parameters['scope']='One fixed GF4 balanced GQ and one GF16 slope spread; unique7242candidate'
write('PARAMETERS.json',parameters)
print(json.dumps(result,indent=2))
