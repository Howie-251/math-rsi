"""Read the literal new source once for degrees and source-grounded block structure."""
from collections import Counter
from pathlib import Path
import json
import resource
import time

P = Path(__file__).resolve().parent
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (89, 90))
N = 94186
BASE = 88452
degree = bytearray(N)
adj = [[] for _ in range(N)]
coredegree = bytearray(BASE)
samefiber = bytearray(BASE)
extra_degree = bytearray(N-BASE)
edge_regions = Counter()
edges = 0
loops = 0
header = None
leading_comments = []
with (P / 'source94186.edges').open() as f:
    for line in f:
        if not line.strip():
            continue
        if line.lstrip().startswith('#'):
            if edges == 0:
                leading_comments.append(line.rstrip())
            continue
        row = list(map(int, line.split()))
        assert len(row) == 2
        u, v = row
        if edges == 0 and header is None and u == N and v > N:
            header = [u, v]
            continue
        assert 0 <= u < N and 0 <= v < N
        edges += 1
        degree[u] += 1
        degree[v] += 1
        adj[u].append(v)
        adj[v].append(u)
        loops += u == v
        a, b = u < BASE, v < BASE
        if a and b:
            coredegree[u] += 1
            coredegree[v] += 1
            edge_regions['prefix_prefix'] += 1
            if u // 243 == v // 243:
                samefiber[u] += 1
                samefiber[v] += 1
        elif a or b:
            edge_regions['prefix_extra'] += 1
            extra_degree[(v if a else u)-BASE] += 1
        else:
            edge_regions['extra_extra'] += 1
degree_hist = dict(sorted(Counter(degree).items()))
assert loops == 0 and sum(degree) == 2*edges and max(degree) <= 14
if header is not None:
    assert header == [N, edges]
free = [v for v, d in enumerate(degree) if d < 14]
low = [v for v, d in enumerate(degree) if d == 12]
lowset = set(low)
low_structure = {'source_n': N, 'source_m': edges, 'vertices_degree12': low,
     'records': [{'vertex': v, 'neighbors': sorted(adj[v]),
                  'neighbor_degree_histogram': dict(sorted(Counter(degree[w] for w in adj[v]).items())),
                  'free_neighbors': sorted(w for w in adj[v] if degree[w] < 14),
                  'other_degree12_neighbors': sorted(w for w in adj[v] if w in lowset)} for v in low],
     'degree12_pair_common_neighbor_histogram': dict(sorted(Counter(len(set(adj[u]) & set(adj[v]))
          for i,u in enumerate(low) for v in low[i+1:]).items())),
     'degree12_induced_edges': [[u,v] for u in low for v in adj[u] if u < v and v in lowset],
     'scope': 'One-hop structural profile only; no source distances or R4 evaluated.'}
(P / 'RARE15_STRUCTURE.json').write_text(json.dumps(low_structure, indent=2)+'\n')
(P / 'degree14.u8.bin').write_bytes(degree)
(P / 'free_ports.json').write_text(json.dumps({'source_n': N, 'source_m': edges, 'delta': 14,
     'ports': free, 'degrees': [degree[v] for v in free], 'free_slots': [14-degree[v] for v in free]}, indent=2)+'\n')
result = {'status': 'SOURCE_DEGREE_PROFILE_COMPLETE', 'source_n': N, 'source_m': edges,
          'degree_histogram': degree_hist, 'maximum_degree': max(degree), 'minimum_degree': min(degree),
          'free_vertices': len(free), 'total_free_slots': sum(14-d for d in degree),
          'free_prefix88452_vertices': sum(v < BASE for v in free),
          'free_extra5734_vertices': sum(v >= BASE for v in free),
          'edge_region_counts_assuming_literal_prefix': edge_regions,
          'prefix88452_induced_degree_histogram': dict(sorted(Counter(coredegree).items())),
          'prefix_literal243fiber_internal_degree_histogram': dict(sorted(Counter(samefiber).items())),
          'extra5734_old_prefix_neighbor_count_histogram': dict(sorted(Counter(extra_degree).items())),
          'prefix_interpretation_scope': 'Numeric source prefix only; not an identified Mizuno subgraph without generation or edge relation evidence.',
          'source_header': header, 'leading_comments': leading_comments,
          'degree12_vertices': low,
          'prediction_ports_at_least14': len(free) >= 14,
          'source_allBFS': 0, 'new_graphs': 0, 'R4_tests': 0,
          'CPU_seconds': time.process_time()-START}
(P / 'SOURCE_PROFILE.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
