"""Independent generic and typed full-edge-list validation of the sole candidate."""
import json
import resource
import subprocess
import time
from collections import Counter, defaultdict, deque
from pathlib import Path

start = time.process_time()
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
before = resource.getrusage(resource.RUSAGE_CHILDREN)
checked = subprocess.run([str(ROOT / 'computations/ddp/verify_graph'), str(OUT / 'candidate.edges'), '5', '5'],
                         capture_output=True, text=True)
after = resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu = after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime
assert checked.returncode in (0, 1), checked.stderr
generic = json.loads(checked.stdout)
(OUT / 'candidate.generic_verify.json').write_text(json.dumps(generic, indent=2) + '\n')
data = list(map(int, (OUT / 'candidate.edges').read_text().split()))
n, m = data[:2]
edges = [tuple(data[i:i + 2]) for i in range(2, len(data), 2)]
assert (n, m) == (676, 1690) and len(edges) == len(set(edges)) == m
adj = [set() for _ in range(n)]
for u, v in edges:
    assert 0 <= u < v < n
    adj[u].add(v)
    adj[v].add(u)
assert all(len(a) == 5 for a in adj)
types = ['head' if v % 26 == 0 else 'block' if v % 26 <= 5 else 'leaf' for v in range(n)]
order = {'head': 0, 'block': 1, 'leaf': 2}
leaf_pair_counts = Counter()
leaf_block_degree = Counter()
block_pair_counts = Counter()
for u, v in edges:
    if types[u] == types[v] == 'leaf':
        gu, gv = u // 26, v // 26
        bu, bv = (u % 26 - 6) // 4, (v % 26 - 6) // 4
        assert gu != gv and bu == bv
        leaf_pair_counts[tuple(sorted((gu, gv)))] += 1
        leaf_block_degree.update(((gu, bu), (gv, bv)))
        block_pair_counts[(gu, bu, gv, bv)] += 1
assert len(leaf_pair_counts) == 325
assert Counter(leaf_pair_counts.values()) == Counter({3: 260, 4: 65})
assert len(leaf_block_degree) == 130 and set(leaf_block_degree.values()) == {16}
assert set(block_pair_counts.values()) == {1}
for g in range(26):
    head = 26 * g
    assert adj[head] == set(range(head + 1, head + 6))
    for b in range(5):
        assert adj[head + 1 + b] == {head, *range(head + 6 + 4 * b, head + 10 + 4 * b)}
        for v in range(head + 6 + 4 * b, head + 10 + 4 * b):
            assert sum(types[w] == 'leaf' for w in adj[v]) == 4
bad = []
bad_type = Counter()
bad_group_pair = Counter()
hist = Counter()
type_hist = defaultdict(Counter)
ecc = Counter()
missing = {}
head_hist = {}
for root in range(n):
    dist = [-1] * n
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                queue.append(v)
    assert -1 not in dist
    hist.update(dist)
    ecc[max(dist)] += 1
    missing[root] = sum(d > 5 for d in dist)
    if types[root] == 'head':
        head_hist[root] = dict(sorted(Counter(dist).items()))
    for v in range(root + 1, n):
        pair_type = '-'.join(sorted((types[root], types[v]), key=order.get))
        type_hist[pair_type][dist[v]] += 1
        if dist[v] > 5:
            bad.append((root, v, dist[v]))
            bad_type[pair_type] += 1
            bad_group_pair[tuple(sorted((root // 26, v // 26)))] += 1
assert len(bad) == generic['bad_unordered_pairs']
assert max(ecc) == generic['diameter']
assert {str(k): v for k, v in hist.items()} == generic['ordered_distance_histogram']
with (OUT / 'candidate.bad_pairs.tsv').open('w') as out:
    out.write('u\tv\tdistance\ttype_u\ttype_v\n')
    for u, v, d in bad:
        out.write(f'{u}\t{v}\t{d}\t{types[u]}\t{types[v]}\n')
result = {
    'status': 'COMPLETE_ONE_CANDIDATE_VALIDATION', 'vertices': n, 'edges': m,
    'simple': True, 'connected': True, 'degree_histogram': dict(sorted(Counter(map(len, adj)).items())),
    'diameter': max(ecc), 'valid_degree_five_diameter_five': not bad,
    'bad_unordered_pairs': len(bad), 'bad_pairs_by_type': dict(sorted(bad_type.items())),
    'ordered_distance_histogram': dict(sorted(hist.items())),
    'all_unordered_type_distance_histograms': {k: dict(sorted(v.items())) for k, v in sorted(type_hist.items())},
    'eccentricity_histogram': dict(sorted(ecc.items())),
    'head_distance_histograms': head_hist, 'missing_within_five_per_vertex': missing,
    'bad_pairs_by_group_pair': [{'groups': list(k), 'bad_pairs': v} for k, v in sorted(bad_group_pair.items())],
    'group_pair_multiplicities_checked': {'3': 260, '4': 65},
    'block_external_incidence_count': 16, 'all_leaf_external_degrees': 4,
    'generic_checker_returncode': checked.returncode,
    'generic_checker_cpu_seconds': child_cpu,
    'python_validation_cpu_seconds': time.process_time() - start,
    'scope': 'Fresh adjacency and every root BFS from the sole complete edge list; no generator distance cache or candidate search.',
}
(OUT / 'candidate.independent_validation.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k not in ('missing_within_five_per_vertex', 'head_distance_histograms', 'all_unordered_type_distance_histograms', 'bad_pairs_by_group_pair')}, indent=2))
