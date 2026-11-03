"""One literal degree/fiber profile. No BFS, regeneration, or candidate search."""
from collections import Counter
from pathlib import Path
import json
import resource
import time

started = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
out = Path(__file__).resolve().parent
recipe = json.loads((out / 'construction.json').read_text())
n = recipe['order']
assert n == 6804
adj = [set() for _ in range(n)]
edges = set()
sections = Counter()
section = 'unlabelled'
duplicate = loops = 0
for line in (out / 'source6804.edges').read_text().splitlines():
    if line.startswith('#'):
        section = line[1:].strip()
        continue
    if not line.strip():
        continue
    u, v = map(int, line.split())
    assert 0 <= u < n and 0 <= v < n
    loops += u == v
    e = min(u,v), max(u,v)
    duplicate += e in edges
    edges.add(e)
    adj[u].add(v)
    adj[v].add(u)
    sections[section] += 1

fiber_pairs = Counter()
intrafiber = plain = 0
plain_degree = [0] * n
plain_relation_misses = []
controller = [set() for _ in range(84)]
for u,v in edges:
    gu, gv = u//81, v//81
    intrafiber += gu == gv
    fiber_pairs[min(gu,gv),max(gu,gv)] += 1
    controller[gu].add(gv)
    controller[gv].add(gu)
    if gv == (gu+42) % 84:
        plain += 1
        plain_degree[u] += 1
        plain_degree[v] += 1
        x = [(u%81)//3**i%3 for i in range(4)]
        expected_y = sum(((int(i==2)-x[i])%3)*3**i for i in range(4))
        if v%81 != expected_y:
            plain_relation_misses.append([u,v])

degrees = [len(a) for a in adj]
free = [v for v in range(n) if degrees[v] < 13]
sat_neighbors = [sum(degrees[u] == 13 for u in adj[v]) for v in range(n)]
result = {
    'status':'COMPLETE_PREDICTION_REFUTED_NO_SPARES',
    'n':n,'m':len(edges),'simple':loops==duplicate==0,
    'loops':loops,'repeated_edge_rows':duplicate,
    'degree_histogram':dict(Counter(degrees)),
    'free_vertices':free,'free_count':len(free),
    'source_sections':dict(sections),
    'fiber_count':84,'fiber_size':81,
    'intrafiber_edges':intrafiber,
    'controller_degree_histogram':dict(Counter(map(len,controller))),
    'fiber_pair_edgecount_histogram':dict(Counter(fiber_pairs.values())),
    'plain_matching_edges':plain,
    'plain_degree_histogram':dict(Counter(plain_degree)),
    'plain_neighbor_fiber_rule':'g -> (g+42) mod84, hence always a different fiber',
    'plain_fiber_coordinate_rule':'x -> -x+(0,0,1,0) over F3',
    'plain_relation_misses':plain_relation_misses,
    'min_saturated_neighbors':min(sat_neighbors),
    'saturated_neighbor_count_histogram':dict(Counter(sat_neighbors)),
    'prediction_disposition':'REFUTED',
    'reason':'The reflection is between paired controller fibers g and gz, rather than within one odd-size fiber; it has no graph fixed vertex.',
    'D':None,'source_reported_D':4,
    'source_D4_basis':'Inherited current primary recipe/public report; not revalidated by BFS.',
    'allfree_R3_executed':False,
    'graph_BFS':0,'candidate_search':False,
    'CPU_seconds':time.process_time()-started,
    'edge_preserving_extension_obstruction':'All old vertices are saturated. No connected enlargement preserving every source edge and maximum degree13 can attach even one new vertex, regardless of helper count.',
    'running':False,'pending':[]}
assert len(edges)==44226 and Counter(degrees)==Counter({13:6804})
assert plain==3402 and Counter(plain_degree)==Counter({1:6804})
assert not plain_relation_misses and not intrafiber
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
