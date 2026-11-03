#!/usr/bin/env python3
"""Complete fixed 144-line-edge new-root gate; no candidate construction."""
from collections import defaultdict, deque
from pathlib import Path
import json
import resource
import time

started = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
here = Path(__file__).resolve().parent
parent = here.parent
project = here.parents[4]
params = json.loads((parent / 'PARAMETERS.json').read_text())
old_dist = json.loads((parent / 'DISTANCES_TO_T.json').read_text())
T = set(params['T'])
M = {tuple(sorted(e)) for e in params['deleted_matching']}
gaps = [v for v,t in enumerate(old_dist) if t > 3]
assert len(gaps) == 312 and max(old_dist) == 4
adj = [[] for _ in old_dist]
edges = set()
for line in (project / params['source']).read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    u,v = map(int,line.split())
    edges.add(tuple(sorted((u,v))))
    adj[u].append(v)
    adj[v].append(u)
by_q = defaultdict(list)
for v in sorted(T):
    external = sorted(q for q in adj[v] if q not in T)
    assert len(external) == 12
    for q in external:
        assert tuple(sorted((v,q))) not in M
        assert q//81 != (v//81+42)%84  # not the central plain port
        by_q[q].append(v)
assert sum(map(len,by_q.values())) == 144
(here/'INPUT.json').write_text(json.dumps({
    'source':params['source'], 'T':sorted(T), 'M':params['deleted_matching'],
    'gaps':gaps, 'raw_line_edges':144, 'distinct_q':len(by_q),
    'q_with_source_endpoints':[{'q':q,'source_v':by_q[q]} for q in sorted(by_q)],
    'symmetry_pruning':False,
},indent=2)+'\n')

records = []
passing = []
for index,q in enumerate(sorted(by_q)):
    dist = [-1]*len(adj)
    dist[q] = 0
    queue = deque([q])
    while queue:
        u = queue.popleft()
        if dist[u] == 3:
            continue
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u]+1
                queue.append(v)
    missed = [v for v in gaps if dist[v] < 0]
    row = {'index':index, 'q':q, 'source_v':by_q[q],
           'covered_gaps':len(gaps)-len(missed), 'missing_gaps':len(missed),
           'first_missing_gap':missed[0] if missed else None,
           'new_root_gate_pass':not missed}
    records.append(row)
    if not missed:
        passing.extend({'q':q,'v':v} for v in by_q[q])
with (here/'CASES.jsonl').open('w') as out:
    for row in records:
        out.write(json.dumps(row,separators=(',',':'))+'\n')
result = {
    'status':'COMPLETE_NO_NEW_ROOT_PASS' if not passing else 'COMPLETE_GATE_HAS_CANDIDATES',
    'raw_line_edges':144, 'distinct_q':len(by_q),
    'q_evaluated':len(records), 'passing_q':sum(r['new_root_gate_pass'] for r in records),
    'passing_changed_graph_parameters':passing,
    'maximum_gaps_covered_by_one_q':max(r['covered_gaps'] for r in records),
    'minimum_gaps_remaining':min(r['missing_gaps'] for r in records),
    'fixed_gap_count':len(gaps),
    'source_radius3_bfs_runs':len(records),
    'repeated_original_multi_source_bfs':0,
    'candidate_graphs_generated':0, 'candidate_bfs_runs':0,
    'cpu_seconds':time.process_time()-started,
}
(here/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
if not passing:
    (here/'TERMINAL.json').write_text(json.dumps({**result,'running':False,'pending':[]},indent=2)+'\n')
print(json.dumps(result,separators=(',',':')))
