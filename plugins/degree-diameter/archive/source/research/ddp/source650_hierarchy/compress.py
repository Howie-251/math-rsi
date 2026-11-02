"""Exact labelled compression of the existing published 650 graph; no search."""
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
source = ROOT / 'research/ddp/m1_degree5_transfer/rithwik650_source.edges'
data = list(map(int, source.read_text().split()))
n, m = data[:2]
edges = [tuple(data[i:i + 2]) for i in range(2, len(data), 2)]
assert (n, m) == (650, 1625) and len(edges) == m
adj = [set() for _ in range(n)]
for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)
assert all(len(a) == 5 for a in adj)
damage_path = ROOT / 'research/ddp/m1_matching_joint/source650_diagnosis/diagnosis.edge_damage.tsv'
rows = list(csv.DictReader(damage_path.open(), delimiter='\t'))
assert len(rows) == m
damage = []
for eid, row in enumerate(rows):
    assert (int(row['eid']), int(row['u']), int(row['v'])) == (eid, *edges[eid])
    damage.append(int(row['bad_pairs']))
minimum_edges = [e for e, d in zip(edges, damage) if d == min(damage)]
V0 = set(v for e in minimum_edges for v in e)
V1 = set().union(*(adj[v] for v in V0)) - V0
V2 = set(range(n)) - V0 - V1
layers = [V0, V1, V2]
layer_of = {v: i for i, vs in enumerate(layers) for v in vs}
layer_degrees = [Counter(tuple(len(adj[v] & vs) for vs in layers) for v in layer) for layer in layers]
layer_edges = Counter(tuple(sorted((layer_of[u], layer_of[v]))) for u, v in edges)
damage_by_layers = defaultdict(Counter)
for (u, v), d in zip(edges, damage):
    damage_by_layers[d][tuple(sorted((layer_of[u], layer_of[v])))] += 1
centers = sorted(V1)
blocks = [sorted(adj[v] & V0) for v in centers]
assert all(len(b) == 4 for b in blocks)
assert sorted(x for block in blocks for x in block) == sorted(V0)
port_of = {x: (bi, pi) for bi, block in enumerate(blocks) for pi, x in enumerate(block)}
group_centers = sorted(V2)
center_to_block = {v: i for i, v in enumerate(centers)}
groups = [sorted(center_to_block[v] for v in adj[g] & V1) for g in group_centers]
assert all(len(g) == 5 for g in groups)
assert sorted(b for group in groups for b in group) == list(range(len(blocks)))
group_of = {b: (gi, pos) for gi, group in enumerate(groups) for pos, b in enumerate(group)}
block_edges = defaultdict(list)
group_edges = defaultdict(list)
for u, v in edges:
    if u in V0 and v in V0:
        b, i = port_of[u]
        c, j = port_of[v]
        if b > c:
            b, c, i, j = c, b, j, i
        block_edges[b, c].append([i, j])
        gb, bp = group_of[b]
        gc, cp = group_of[c]
        if gb > gc:
            gb, gc, bp, cp, i, j = gc, gb, cp, bp, j, i
        group_edges[gb, gc].append([bp, i, cp, j])
internal_edges_per_block = [len(block_edges.get((b, b), [])) for b in range(len(blocks))]
block_neighbor_degree = [0] * len(blocks)
block_weighted_degree = [0] * len(blocks)
block_pair_patterns = Counter()
for (b, c), ports in block_edges.items():
    if b != c:
        block_neighbor_degree[b] += 1
        block_neighbor_degree[c] += 1
        block_weighted_degree[b] += len(ports)
        block_weighted_degree[c] += len(ports)
    left = Counter(p[0] for p in ports)
    right = Counter(p[1] for p in ports)
    signature = (len(ports), tuple(sorted(left.values())), tuple(sorted(right.values())))
    block_pair_patterns[str(signature)] += 1
group_neighbor_degree = [0] * len(groups)
group_pair_patterns = Counter()
group_records = []
for (g, h), links in sorted(group_edges.items()):
    matrix = [[0] * 5 for _ in range(5)]
    for b, i, c, j in links:
        matrix[b][c] += 1
    if g != h:
        group_neighbor_degree[g] += 1
        group_neighbor_degree[h] += 1
    signature = (len(links), tuple(sorted(map(sum, matrix))), tuple(sorted(sum(row[j] for row in matrix) for j in range(5))))
    group_pair_patterns[str(signature)] += 1
    group_records.append({'groups': [g, h], 'block_edge_multiplicity_matrix': matrix, 'port_links': sorted(links)})
five_adj = [set() for _ in groups]
for (g, h), links in group_edges.items():
    if len(links) == 5:
        five_adj[g].add(h)
        five_adj[h].add(g)
five_components = []
seen = set()
for root in range(len(groups)):
    if root in seen:
        continue
    component = [root]
    seen.add(root)
    for g in component:
        for h in five_adj[g] - seen:
            seen.add(h)
            component.append(h)
    five_components.append(sorted(component))
assert len(five_components) == 5 and all(len(c) == 5 for c in five_components)
assert all(len(a) == 4 for a in five_adj)
compressed = {
    'source': str(source.relative_to(ROOT)),
    'layer_vertices': [sorted(vs) for vs in layers],
    'blocks': [{'block': b, 'center_v1': centers[b], 'ports_v0': block} for b, block in enumerate(blocks)],
    'groups': [{'group': g, 'center_v2': group_centers[g], 'blocks': group} for g, group in enumerate(groups)],
    'block_edges': [{'blocks': list(pair), 'port_edges': sorted(ports)} for pair, ports in sorted(block_edges.items())],
    'group_edges': group_records,
}
reconstructed = set()
for b, block in enumerate(blocks):
    reconstructed.update(tuple(sorted((centers[b], v))) for v in block)
for g, group in enumerate(groups):
    reconstructed.update(tuple(sorted((group_centers[g], centers[b]))) for b in group)
for (b, c), ports in block_edges.items():
    reconstructed.update(tuple(sorted((blocks[b][i], blocks[c][j]))) for i, j in ports)
assert reconstructed == set(edges)
summary = {
    'status': 'COMPLETE_EXACT_COMPRESSION', 'source_vertices': n, 'source_edges': m,
    'layer_sizes': list(map(len, layers)),
    'layer_degree_profiles': [{str(k): v for k, v in sorted(c.items())} for c in layer_degrees],
    'layer_edge_counts': {str(k): v for k, v in sorted(layer_edges.items())},
    'damage_by_layer_pair': {str(d): {str(k): v for k, v in sorted(c.items())} for d, c in sorted(damage_by_layers.items())},
    'blocks': len(blocks), 'block_size': 4, 'groups': len(groups), 'blocks_per_group': 5,
    'block_internal_edge_histogram': dict(sorted(Counter(internal_edges_per_block).items())),
    'block_quotient_distinct_neighbor_histogram': dict(sorted(Counter(block_neighbor_degree).items())),
    'block_quotient_weighted_degree_histogram': dict(sorted(Counter(block_weighted_degree).items())),
    'block_pair_edge_multiplicity_histogram': dict(sorted(Counter(map(len, block_edges.values())).items())),
    'block_pair_port_degree_patterns': dict(sorted(block_pair_patterns.items())),
    'group_internal_v0_edges': [len(group_edges.get((g, g), [])) for g in range(len(groups))],
    'group_quotient_distinct_neighbor_histogram': dict(sorted(Counter(group_neighbor_degree).items())),
    'group_pair_edge_multiplicity_histogram': dict(sorted(Counter(map(len, group_edges.values())).items())),
    'group_pair_block_degree_patterns': dict(sorted(group_pair_patterns.items())),
    'five_edge_group_pairs_form_five_disjoint_K5': True,
    'five_edge_group_components': five_components,
    'exact_original_edge_reconstruction': True,
    'scope': 'Exact labelled compression only. It does not by itself establish an algebraic or parameterized construction rule.'
}
(OUT / 'compressed_graph.json').write_text(json.dumps(compressed, indent=2) + '\n')
(OUT / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps(summary, indent=2))
