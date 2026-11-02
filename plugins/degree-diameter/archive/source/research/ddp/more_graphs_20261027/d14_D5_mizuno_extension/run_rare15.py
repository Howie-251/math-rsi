"""One frozen15-point-class cover comparison; no pin optimization."""
from collections import Counter, deque
from pathlib import Path
import json
import resource
import subprocess
import time

P = Path(__file__).resolve().parent
START = time.process_time()
CHILD = resource.getrusage(resource.RUSAGE_CHILDREN)

def cpu():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+r.ru_utime+r.ru_stime-CHILD.ru_utime-CHILD.ru_stime

def save(name, value):
    (P/name).write_text(json.dumps(value, indent=2)+'\n')

pred = json.loads((P/'RARE15_PREDICTION.json').read_text())
assert pred['status'] == 'FROZEN_AFTER_LITERAL_LOCAL_STRUCTURE_BEFORE_R4'
assert not (P/'RARE15_RESULT.json').exists()
subprocess.run(['g++','-O3','-std=c++17',str(P/'rare15_balls.cpp'),'-o',str(P/'rare15_balls')],check=True)
compile_cpu = cpu()
subprocess.run([str(P/'rare15_balls'),str(P/'source94186.edges'),str(P)],check=True,timeout=10)
info = json.loads((P/'RARE15_BALLS.json').read_text())
n, m = info['source_n'], info['source_m']
roots, width = info['degree12_vertices'], info['mask_words_per_row']*8
raw = (P/'rare15_R4.u64le.bin').read_bytes()
assert len(raw) == 15*width
balls = [int.from_bytes(raw[i*width:(i+1)*width],'little') for i in range(15)]
pair = pred['false_twin_pair']
assert balls[roots.index(pair[0])] == balls[roots.index(pair[1])]
full = (1<<n)-1
allmask = 0
for b in balls:
    allmask |= b
canonical = 0
for v in pred['pins14']:
    canonical |= balls[roots.index(v)]
assert canonical == allmask
rows = []
hit = None
for omit in range(15):
    mask = 0
    for i,b in enumerate(balls):
        if i != omit:
            mask |= b
    missing_count = n-mask.bit_count()
    rows.append({'omitted': roots[omit], 'missing_count': missing_count})
    if missing_count == 0:
        hit = [v for i,v in enumerate(roots) if i != omit]
        break
missing = [v for v in range(n) if not (allmask>>v)&1]
degrees = (P/'degree14.u8.bin').read_bytes()
save('RARE15_MISSING.json', {'all15_and_canonical14_missing': missing,
     'missing_by_source_degree': dict(sorted(Counter(degrees[v] for v in missing).items()))})
graph = None
new_ecc = None
if hit is not None:
    graph = P/'graph_d14_D5_n94187.edges'
    adj = [[] for _ in range(n+1)]
    seen = 0
    with (P/'source94186.edges').open() as old, graph.open('w') as out:
        out.write(f'{n+1} {m+14}\n')
        for line in old:
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            u,v = map(int,line.split())
            out.write(f'{u} {v}\n')
            adj[u].append(v)
            adj[v].append(u)
            seen += 1
        assert seen == m
        for v in hit:
            assert len(adj[v]) < 14
            out.write(f'{n} {v}\n')
            adj[n].append(v)
            adj[v].append(n)
    assert max(map(len,adj)) == 14
    d = [-1]*(n+1)
    d[n] = 0
    todo = deque([n])
    while todo:
        u = todo.popleft()
        for v in adj[u]:
            if d[v] < 0:
                d[v] = d[u]+1
                todo.append(v)
    assert min(d) == 0 and max(d) <= 5
    new_ecc = max(d)
result = {'status': 'COMPLETE94187_EXTENSION' if hit else 'FIXED_RARE15_14SUBSETS_FAILED',
     'prediction_id': pred['prediction_id'], 'prediction_verdict': 'SUPPORTED' if not missing else 'REFUTED',
     'source_n': n, 'source_m': m, 'delta': 14, 'D': 5, 'hypothetical_n': n+1,
     'degree12_vertices': roots, 'false_twin_pair': pair, 'distinct_open_neighborhoods': 14,
     'R4_balls_computed': 15, 'fourteen_subsets_tested': len(rows), 'subsets': rows,
     'all15_union_equals_canonical14_union': True,
     'all15_and_canonical14_missing_count': len(missing),
     'selected14pins_if_hit': hit, 'actual_new_n': n+1 if hit else None,
     'actual_D': 5 if hit else None, 'ordinary_bad_unordered_pairs': None,
     'graph_file': str(graph) if graph else None,
     'source_edges_retained_if_generated': bool(hit), 'new_root_BFS': int(bool(hit)),
     'new_root_eccentricity': new_ecc, 'source_allBFS': 0,
     'compile_CPU_seconds': compile_cpu, 'native_R4_CPU_seconds': info['CPU_seconds'],
     'total_process_and_children_CPU_seconds': cpu(), 'CPU_budget_seconds': 10,
     'scope': 'Only14-subsets of the literal15 degree12 vertices; no replacement from3670 degree13 spares.',
     'pending': []}
save('RARE15_RESULT.json', result)
print(json.dumps(result,indent=2))
