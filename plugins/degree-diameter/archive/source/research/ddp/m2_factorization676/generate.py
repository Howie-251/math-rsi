"""Expand exactly one prescribed factorization and cyclic-port candidate."""
import json
import time
from collections import Counter, defaultdict
from pathlib import Path

start = time.process_time()
OUT = Path(__file__).resolve().parent
groups = 26
group_pairs = {}
factors = []
block_links = []
incidences = defaultdict(list)
for color in range(25):
    pairs = [(color, 25)] + [tuple(sorted(((color + i) % 25, (color - i) % 25))) for i in range(1, 13)]
    assert len(pairs) == 13 and sorted(v for pair in pairs for v in pair) == list(range(26))
    factors.append({'color': color, 'group_pairs': [list(pair) for pair in sorted(pairs)]})
    c = color % 5
    bs = [(c + j) % 5 for j in range(3 + int(color < 5))]
    for g, h in pairs:
        assert (g, h) not in group_pairs
        group_pairs[g, h] = color
        for b in bs:
            index = len(block_links)
            block_links.append({'groups': [g, h], 'blocks': [b, b], 'color': color})
            incidences[g, b].append((h, b, color, index, 0))
            incidences[h, b].append((g, b, color, index, 1))
assert len(group_pairs) == 325 and len(block_links) == 1040
assert len(incidences) == 130 and all(len(v) == 16 for v in incidences.values())
ports = [[None, None] for _ in block_links]
block_assignments = []
for (g, b), links in sorted(incidences.items()):
    ordered = sorted(links)
    records = []
    for rank, (h, other_b, color, index, side) in enumerate(ordered):
        port = rank % 4
        ports[index][side] = port
        records.append({'rank': rank, 'opposite_group': h, 'opposite_block': other_b,
                        'color': color, 'leaf_port': port, 'block_link_index': index})
    assert Counter(record['leaf_port'] for record in records) == Counter({p: 4 for p in range(4)})
    block_assignments.append({'group': g, 'block': b, 'ordered_incidences': records})

def head(g): return 26 * g
def block(g, b): return 26 * g + 1 + b
def leaf(g, b, p): return 26 * g + 6 + 4 * b + p

tree_edges = []
for g in range(26):
    for b in range(5):
        tree_edges.append((head(g), block(g, b)))
        tree_edges.extend((block(g, b), leaf(g, b, p)) for p in range(4))
leaf_edges = []
for link, (p, q) in zip(block_links, ports):
    g, h = link['groups']
    b, other_b = link['blocks']
    edge = tuple(sorted((leaf(g, b, p), leaf(h, other_b, q))))
    leaf_edges.append(edge)
    link['leaf_ports'] = [p, q]
    link['leaf_edge'] = list(edge)
edges = sorted(tree_edges + leaf_edges)
assert len(edges) == len(set(edges)) == 1690
assert len(tree_edges) == 650 and len(leaf_edges) == 1040
degree = Counter(v for e in edges for v in e)
assert len(degree) == 676 and set(degree.values()) == {5}
leaf_degree = Counter(v for e in leaf_edges for v in e)
assert len(leaf_degree) == 520 and set(leaf_degree.values()) == {4}
with (OUT / 'candidate.edges').open('w') as out:
    out.write('676 1690\n')
    for u, v in edges:
        out.write(f'{u} {v}\n')
parameters = {
    'groups': 26, 'finite_group_labels': list(range(25)), 'infinity_group_label': 25,
    'label_rule': 'head=26*g; block=26*g+1+b; leaf=26*g+6+4*b+p',
    'blocks_per_group': 5, 'leaf_ports_per_block': 4,
    'factorizations': factors, 'bonus_colors': list(range(5)),
    'port_rule': 'sort by (opposite_group, opposite_block, color), assign zero-based rank modulo four',
    'block_links': block_links, 'block_port_assignments': block_assignments,
}
(OUT / 'candidate.parameters.json').write_text(json.dumps(parameters, indent=2) + '\n')
result = {
    'status': 'ONE_DETERMINISTIC_CANDIDATE_GENERATED', 'vertices': 676, 'edges': 1690,
    'degree_histogram': dict(sorted(Counter(degree.values()).items())),
    'leaf_vertices': 520, 'leaf_edges': 1040, 'leaf_degree_histogram': dict(sorted(Counter(leaf_degree.values()).items())),
    'group_pairs': len(group_pairs),
    'group_pair_leaf_edge_multiplicity_histogram': dict(sorted(Counter(3 + int(t < 5) for t in group_pairs.values()).items())),
    'block_incidence_histogram': dict(sorted(Counter(map(len, incidences.values())).items())),
    'cpu_seconds': time.process_time() - start,
    'scope': 'Exactly the prescribed one-factorization, same-index blocks and cyclic rank-modulo-four ports; no randomization, alternative scheme or candidate search.',
}
(OUT / 'generation.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
