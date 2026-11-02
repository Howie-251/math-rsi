"""Generic checker plus independent all-root type-resolved BFS of one saved graph."""
import json
import resource
import subprocess
import time
from collections import Counter, defaultdict, deque
from pathlib import Path

start = time.process_time()
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
child_before = resource.getrusage(resource.RUSAGE_CHILDREN)
command = [str(ROOT / 'computations/ddp/verify_graph'), str(OUT / 'candidate.edges'), '5', '5']
checked = subprocess.run(command, text=True, capture_output=True)
child_after = resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu = child_after.ru_utime + child_after.ru_stime - child_before.ru_utime - child_before.ru_stime
assert checked.returncode in (0, 1), checked.stderr
generic = json.loads(checked.stdout)
(OUT / 'candidate.generic_verify.json').write_text(json.dumps(generic, indent=2) + '\n')

def read_edges(path):
    data = list(map(int, path.read_text().split()))
    n, m = data[:2]
    edges = [tuple(data[i:i + 2]) for i in range(2, len(data), 2)]
    assert len(edges) == m and len(set(edges)) == m
    assert all(0 <= u < v < n for u, v in edges)
    return n, set(edges)

n, edges = read_edges(OUT / 'candidate.edges')
old_n, old_edges = read_edges(ROOT / 'research/ddp/m1_degree5_transfer/rithwik650_source.edges')
assert (n, old_n, len(edges), len(old_edges)) == (676, 650, 1690, 1625)
hierarchy = json.loads((ROOT / 'research/ddp/source650_hierarchy/compressed_graph.json').read_text())
old_leaves, old_blocks, old_heads = map(set, hierarchy['layer_vertices'])
types = {}
for vs, label in ((old_leaves, 'leaf'), (old_blocks, 'block'), (old_heads, 'head')):
    types.update({v: label for v in vs})
types[650] = 'head'
types.update({v: 'block' for v in range(651, 656)})
types.update({v: 'leaf' for v in range(656, 676)})
adj = [set() for _ in range(n)]
for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)
assert all(len(a) == 5 for a in adj)
removed = old_edges - edges
added = edges - old_edges
assert len(removed) == 40 and len(added) == 105
old_endpoints = [v for e in removed for v in e]
assert len(set(old_endpoints)) == 80 and set(old_endpoints) <= old_leaves
assert len([e for e in added if e[0] < 650]) == 80
assert adj[650] == set(range(651, 656))
for b in range(5):
    assert adj[651 + b] == {650, *range(656 + 4 * b, 660 + 4 * b)}
    for leaf in range(656 + 4 * b, 660 + 4 * b):
        assert len(adj[leaf] & old_leaves) == 4
        assert adj[leaf] - old_leaves == {651 + b}
block_of_leaf = {v: b['block'] for b in hierarchy['blocks'] for v in b['ports_v0']}
group_of_block = {b: g['group'] for g in hierarchy['groups'] for b in g['blocks']}
group_of_leaf = {v: group_of_block[b] for v, b in block_of_leaf.items()}
assert len({group_of_leaf[v] for v in old_endpoints}) == 25
remaining_pairs = Counter(tuple(sorted((group_of_leaf[u], group_of_leaf[v])))
                          for u, v in edges if u in old_leaves and v in old_leaves)
assert len(remaining_pairs) == 300 and min(remaining_pairs.values()) >= 1
all_hist = Counter()
bad_by_type = Counter()
bad_by_old_new_type = Counter()
bad_by_age = Counter()
all_type_distance_hist = defaultdict(Counter)
new_root_histograms = {}
vertex_missing = {}
bad_pairs = []
eccentricity_hist = Counter()
type_order = {'head': 0, 'block': 1, 'leaf': 2}
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
    all_hist.update(dist)
    eccentricity_hist[max(dist)] += 1
    vertex_missing[root] = sum(d > 5 for d in dist)
    if root >= 650:
        new_root_histograms[root] = dict(sorted(Counter(dist).items()))
    for v in range(root + 1, n):
        labels = sorted((types[root], types[v]), key=type_order.get)
        type_pair = '-'.join(labels)
        all_type_distance_hist[type_pair][dist[v]] += 1
        if dist[v] > 5:
            bad_pairs.append((root, v, dist[v]))
            bad_by_type[type_pair] += 1
            age_labels = sorted(('old' if x < 650 else 'new' for x in (root, v)))
            bad_by_age['-'.join(age_labels)] += 1
            full_labels = sorted((('old_' if x < 650 else 'new_') + types[x] for x in (root, v)))
            bad_by_old_new_type['-'.join(full_labels)] += 1
assert len(bad_pairs) == generic['bad_unordered_pairs']
assert max(eccentricity_hist) == generic['diameter']
assert {str(k): v for k, v in all_hist.items()} == generic['ordered_distance_histogram']
with (OUT / 'candidate.bad_pairs.tsv').open('w') as out:
    out.write('u\tv\tdistance\ttype_u\ttype_v\n')
    for u, v, d in bad_pairs:
        out.write(f'{u}\t{v}\t{d}\t{types[u]}\t{types[v]}\n')
result = {
    'status': 'COMPLETE_ONE_CANDIDATE_VALIDATION',
    'vertices': n, 'edges': len(edges), 'simple': True, 'connected': True,
    'degree_histogram': dict(sorted(Counter(map(len, adj)).items())),
    'diameter': max(eccentricity_hist), 'valid_degree_five_diameter_five': not bad_pairs,
    'bad_unordered_pairs': len(bad_pairs),
    'bad_pairs_by_type': dict(sorted(bad_by_type.items())),
    'bad_pairs_by_age': dict(sorted(bad_by_age.items())),
    'bad_pairs_by_old_new_type': dict(sorted(bad_by_old_new_type.items())),
    'all_unordered_type_distance_histograms': {k: dict(sorted(v.items())) for k, v in sorted(all_type_distance_hist.items())},
    'ordered_distance_histogram': dict(sorted(all_hist.items())),
    'eccentricity_histogram': dict(sorted(eccentricity_hist.items())),
    'new_root_distance_histograms': new_root_histograms,
    'missing_within_five_per_vertex': vertex_missing,
    'exact_matching_tree_attachment_rule_checked': True,
    'old_groups_covered_by_new_leaf_attachments': 25,
    'minimum_remaining_old_group_pair_edges': min(remaining_pairs.values()),
    'generic_checker_returncode': checked.returncode,
    'generic_checker_cpu_seconds': child_cpu,
    'python_validation_cpu_seconds': time.process_time() - start,
    'scope': 'Two independent complete edge-list distance checks on exactly one generated candidate; no modification or search.',
}
(OUT / 'candidate.independent_validation.json').write_text(json.dumps(result, indent=2) + '\n')
brief = {k: v for k, v in result.items() if k not in ('missing_within_five_per_vertex', 'new_root_distance_histograms', 'all_unordered_type_distance_histograms')}
print(json.dumps(brief, indent=2))
