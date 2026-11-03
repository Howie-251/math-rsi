"""One source-edge pass; inspect only the forty newborn open neighborhoods."""
from pathlib import Path
from collections import Counter
import json
import resource
import time

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent.parents[3]
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (1, 2))
spec = json.loads((OUT / 'PREDICTION.json').read_text())
assert spec['status'] == 'FROZEN_BEFORE_NEWBORN40_FULLSTAR_SCAN'
source = ROOT / spec['source_graph']
degree = [0] * 51457
nbr = {v: [] for v in range(51417, 51457)}
with source.open() as f:
    assert tuple(map(int, next(f).split())) == (51457, 324863)
    count = 0
    for line in f:
        u, v = map(int, line.split())
        degree[u] += 1
        degree[v] += 1
        count += 1
        if u in nbr:
            nbr[u].append(v)
        if v in nbr:
            nbr[v].append(u)
assert count == 324863 and max(degree) == 13
rows = []
for v in range(51417, 51457):
    ns = sorted(nbr[v])
    assert len(ns) == degree[v] and v not in ns
    saturated = [u for u in ns if degree[u] >= 13]
    rows.append({'prototype': v, 'full_neighbors': ns,
                 'neighbor_current_degrees': [degree[u] for u in ns],
                 'saturated_neighbors': saturated, 'saturated_neighbor_count': len(saturated),
                 'fullstar_legal': not saturated})
pool = [r for r in rows if r['fullstar_legal']]
independent = all(u < 51417 for row in rows for u in row['full_neighbors'])
result = {'status': 'COMPLETE_NEWBORN40_FULLSTAR_SCAN',
          'source_n': 51457, 'source_m': 324863, 'source_max_degree': 13,
          'prototypes_scanned': 40, 'candidate_count': len(pool),
          'saturated_neighbor_count_histogram': dict(sorted(Counter(r['saturated_neighbor_count'] for r in rows).items())),
          'newborn_prototypes_independent': independent,
          'all_prototype_neighbors_in_original51417': independent,
          'prediction': 'SUPPORTED' if pool else 'REFUTED',
          'CPU_seconds': time.process_time() - START, 'CPU_limit_seconds': 1,
          'BFS': 0, 'R4_evaluations': 0, 'graphs_generated': 0,
          'scope': 'Only40newbornvertices51417..51456; no oldvertex scan or recursiveclonepool.'}
(OUT / 'frozen40.json').write_text(json.dumps({'records': rows}, indent=2) + '\n')
(OUT / 'eligible_pool.json').write_text(json.dumps({'records': pool}, indent=2) + '\n')
(OUT / 'source_degrees.u8.bin').write_bytes(bytes(degree))
(OUT / 'SCAN_RESULT.json').write_text(json.dumps(result, indent=2) + '\n')
(OUT / 'terminal.json').write_text(json.dumps({**result, 'running': False, 'pending': ['Firstcloneproduction'] if pool else []}, indent=2) + '\n')
print(json.dumps(result, indent=2), flush=True)
