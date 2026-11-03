"""One deterministic hierarchy extension; no random seeds or candidate queue."""
import csv
import json
import time
from collections import Counter
from itertools import combinations
from pathlib import Path

start = time.process_time()
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
source = ROOT / 'research/ddp/m1_degree5_transfer/rithwik650_source.edges'
compressed = json.loads((ROOT / 'research/ddp/source650_hierarchy/compressed_graph.json').read_text())
data = list(map(int, source.read_text().split()))
n, m = data[:2]
edges = [tuple(data[i:i + 2]) for i in range(2, len(data), 2)]
assert (n, m) == (650, 1625) and len(edges) == m
V0, V1, V2 = map(set, compressed['layer_vertices'])
blocks = compressed['blocks']
groups = compressed['groups']
block_of = {v: block['block'] for block in blocks for v in block['ports_v0']}
group_of_block = {b: group['group'] for group in groups for b in group['blocks']}
group_of = {v: group_of_block[block_of[v]] for v in V0}
adj = [set() for _ in range(n)]
for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)
assert all(len(a) == 5 for a in adj)
damage_rows = list(csv.DictReader((ROOT / 'research/ddp/m1_matching_joint/source650_diagnosis/diagnosis.edge_damage.tsv').open(), delimiter='\t'))
damage = []
for eid, row in enumerate(damage_rows):
    assert (int(row['eid']), int(row['u']), int(row['v'])) == (eid, *edges[eid])
    damage.append(int(row['bad_pairs']))
leaf_eids = [eid for eid, (u, v) in enumerate(edges) if u in V0 and v in V0]
pair_of = {eid: tuple(sorted((group_of[edges[eid][0]], group_of[edges[eid][1]]))) for eid in leaf_eids}
original_pair_count = Counter(pair_of.values())
remaining_pair_count = original_pair_count.copy()
used = set()
group_load = Counter()
block_load = Counter()
selected = []
for step in range(40):
    choices = []
    for eid in leaf_eids:
        u, v = edges[eid]
        if u in used or v in used or remaining_pair_count[pair_of[eid]] <= 1:
            continue
        g, h = pair_of[eid]
        newly_covered = int(group_load[g] == 0) + int(group_load[h] == 0)
        key = (-newly_covered, group_load[g] + group_load[h], max(group_load[g], group_load[h]),
               damage[eid], block_load[block_of[u]] + block_load[block_of[v]], eid)
        choices.append((key, eid))
    if not choices:
        break
    _, eid = min(choices)
    selected.append(eid)
    u, v = edges[eid]
    used.update((u, v))
    group_load.update((group_of[u], group_of[v]))
    block_load.update((block_of[u], block_of[v]))
    remaining_pair_count[pair_of[eid]] -= 1
if len(selected) != 40 or len(group_load) != 25:
    failure = {'status': 'DETERMINISTIC_GREEDY_FEASIBILITY_NOT_MET', 'selected_edges': len(selected),
               'covered_old_groups': len(group_load), 'selected_edge_ids': selected,
               'cpu_seconds': time.process_time() - start}
    (OUT / 'generation.json').write_text(json.dumps(failure, indent=2) + '\n')
    print(json.dumps(failure))
    raise SystemExit(1)
assert len(used) == 80 and min(remaining_pair_count.values()) >= 1

# Evaluate only assignment coverage, not graph distance or any alternative full candidate.
remaining = set(selected)
direct_coverage = [set() for _ in range(5)]
one_step_coverage = [set() for _ in range(5)]
bundles = [[] for _ in range(5)]
endpoint_sets = {eid: set(edges[eid]) for eid in selected}
edge_direct = {eid: {group_of[v] for v in edges[eid]} for eid in selected}
edge_one_step = {}
for eid in selected:
    reached = endpoint_sets[eid] | set().union(*(adj[v] & V0 for v in edges[eid]))
    edge_one_step[eid] = {group_of[v] for v in reached}
for step in range(20):
    b = step % 5
    choice = None
    for e, f in combinations(sorted(remaining), 2):
        direct = edge_direct[e] | edge_direct[f]
        nearby = edge_one_step[e] | edge_one_step[f]
        key = (-len(direct - direct_coverage[b]), -len(nearby - one_step_coverage[b]),
               -len(direct), e, f)
        if choice is None or key < choice[0]:
            choice = (key, e, f, direct, nearby)
    _, e, f, direct, nearby = choice
    remaining.difference_update((e, f))
    direct_coverage[b].update(direct)
    one_step_coverage[b].update(nearby)
    bundles[b].append((e, f))
assert not remaining and all(len(bs) == 4 for bs in bundles)

new_head = 650
new_blocks = list(range(651, 656))
new_leaves = list(range(656, 676))
new_edges = set(edges) - {edges[eid] for eid in selected}
tree_edges = [(new_head, b) for b in new_blocks]
attachment_edges = []
assignments = []
for b, paired_edges in enumerate(bundles):
    for port, (e, f) in enumerate(paired_edges):
        leaf = 656 + 4 * b + port
        tree_edges.append((new_blocks[b], leaf))
        endpoints = sorted(endpoint_sets[e] | endpoint_sets[f])
        assert len(endpoints) == 4
        attachment_edges.extend(tuple(sorted((leaf, v))) for v in endpoints)
        assignments.append({'new_leaf': leaf, 'new_block_head': new_blocks[b],
                            'old_edge_ids': [e, f], 'old_leaf_endpoints': endpoints,
                            'old_groups': sorted({group_of[v] for v in endpoints})})
new_edges.update(tree_edges)
new_edges.update(attachment_edges)
assert len(tree_edges) == 25 and len(attachment_edges) == 80 and len(new_edges) == 1690
degree = Counter(v for e in new_edges for v in e)
assert len(degree) == 676 and set(degree.values()) == {5}
assert set(edges) - new_edges == {edges[eid] for eid in selected}
assert new_edges - set(edges) == set(tree_edges + attachment_edges)
with (OUT / 'candidate.edges').open('w') as out:
    out.write(f'676 {len(new_edges)}\n')
    for u, v in sorted(new_edges):
        out.write(f'{u} {v}\n')
parameters = {
    'old_source': str(source.relative_to(ROOT)),
    'new_group_head': new_head, 'new_block_heads': new_blocks, 'new_leaves': new_leaves,
    'old_layers': {'leaf': sorted(V0), 'block': sorted(V1), 'head': sorted(V2)},
    'selected_original_edge_ids': selected,
    'deleted_edges': [list(edges[eid]) for eid in selected],
    'new_tree_edges': tree_edges, 'new_old_leaf_edges': attachment_edges,
    'leaf_assignments': assignments,
    'selected_old_group_endpoint_counts': dict(sorted(group_load.items())),
    'remaining_old_group_pair_edges': [{'groups': list(pair), 'before': original_pair_count[pair], 'after': count}
                                      for pair, count in sorted(remaining_pair_count.items())],
    'new_block_direct_old_groups': [sorted(s) for s in direct_coverage],
    'new_block_original_one_step_old_groups': [sorted(s) for s in one_step_coverage],
}
(OUT / 'candidate.parameters.json').write_text(json.dumps(parameters, indent=2) + '\n')
result = {
    'status': 'ONE_DETERMINISTIC_CANDIDATE_GENERATED', 'vertices': 676, 'edges': 1690,
    'degree_histogram': dict(sorted(Counter(degree.values()).items())),
    'deleted_old_leaf_edges': 40, 'distinct_old_leaf_endpoints': len(used),
    'covered_old_groups': len(group_load),
    'minimum_remaining_old_group_pair_edges': min(remaining_pair_count.values()),
    'old_group_endpoint_load_histogram': dict(sorted(Counter(group_load.values()).items())),
    'direct_groups_per_new_block': list(map(len, direct_coverage)),
    'original_one_step_groups_per_new_block': list(map(len, one_step_coverage)),
    'selected_single_edge_damage_sum': sum(damage[eid] for eid in selected),
    'selected_single_edge_damage_histogram': dict(sorted(Counter(damage[eid] for eid in selected).items())),
    'cpu_seconds': time.process_time() - start,
    'scope': 'Exactly one greedy matching and one deterministic pairing/assignment; no candidate-distance optimization, retries, random seed or search queue.',
}
(OUT / 'generation.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
