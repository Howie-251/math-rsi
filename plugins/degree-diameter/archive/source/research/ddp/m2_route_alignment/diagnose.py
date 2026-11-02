"""Read-only exact head/block routing and incidence alignment in three saved graphs."""
import csv
import json
import time
from collections import Counter, defaultdict, deque
from pathlib import Path

START = time.process_time()
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[2]
base_hierarchy = json.loads((ROOT / 'research/ddp/source650_hierarchy/compressed_graph.json').read_text())

def hierarchy(kind):
    if kind == 'cyclic676':
        groups = [{'head': 26 * g, 'blocks': [26 * g + 1 + b for b in range(5)]} for g in range(26)]
        blocks = [{'vertex': 26 * g + 1 + b, 'group': g,
                   'leaves': list(range(26 * g + 6 + 4 * b, 26 * g + 10 + 4 * b))}
                  for g in range(26) for b in range(5)]
        return groups, blocks
    group_of_block = {b: g['group'] for g in base_hierarchy['groups'] for b in g['blocks']}
    blocks = [{'vertex': b['center_v1'], 'group': group_of_block[b['block']], 'leaves': b['ports_v0']}
              for b in base_hierarchy['blocks']]
    groups = [{'head': g['center_v2'], 'blocks': [blocks[b]['vertex'] for b in g['blocks']]}
              for g in base_hierarchy['groups']]
    if kind == 'expanded676':
        groups.append({'head': 650, 'blocks': list(range(651, 656))})
        blocks.extend({'vertex': 651 + b, 'group': 25, 'leaves': list(range(656 + 4 * b, 660 + 4 * b))}
                      for b in range(5))
    return groups, blocks

def distribution(values):
    values = sorted(values)
    if not values:
        return {'count': 0, 'minimum': None, 'median': None, 'maximum': None, 'histogram': {}}
    return {'count': len(values), 'minimum': values[0],
            'median': (values[(len(values) - 1) // 2] + values[len(values) // 2]) / 2,
            'maximum': values[-1], 'histogram': dict(sorted(Counter(values).items()))}

def diagnose(name, relative_path, expected_bad):
    start = time.process_time()
    data = list(map(int, (ROOT / relative_path).read_text().split()))
    n, m = data[:2]
    edges = [tuple(data[i:i + 2]) for i in range(2, len(data), 2)]
    assert len(edges) == m and len(set(edges)) == m
    adj = [set() for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < v < n
        adj[u].add(v)
        adj[v].add(u)
    groups, blocks = hierarchy(name)
    group_count, block_count = len(groups), len(blocks)
    block_index = {b['vertex']: i for i, b in enumerate(blocks)}
    leaf_info = {v: (b, p) for b, block in enumerate(blocks) for p, v in enumerate(block['leaves'])}
    assert len(leaf_info) == group_count * 20
    for g, group in enumerate(groups):
        assert adj[group['head']] == set(group['blocks'])
    for block in blocks:
        assert adj[block['vertex']] == set(block['leaves']) | {groups[block['group']]['head']}
    incidences = [[] for _ in blocks]
    leaf_edges = []
    for eid, (u, v) in enumerate(edges):
        if u not in leaf_info or v not in leaf_info:
            continue
        b, p = leaf_info[u]
        c, q = leaf_info[v]
        assert b != c
        incidences[b].append({'edge_id': eid, 'leaf_here': u, 'port_here': p,
                              'neighbor_leaf': v, 'neighbor_block': c, 'neighbor_group': blocks[c]['group']})
        incidences[c].append({'edge_id': eid, 'leaf_here': v, 'port_here': q,
                              'neighbor_leaf': u, 'neighbor_block': b, 'neighbor_group': blocks[b]['group']})
        leaf_edges.append({'edge_id': eid, 'endpoints': [u, v], 'blocks': [b, c], 'ports': [p, q]})
    assert all(len(inc) == 16 for inc in incidences)
    from_group = [[[] for _ in blocks] for _ in groups]
    from_block = [[[] for _ in blocks] for _ in blocks]
    for middle, inc in enumerate(incidences):
        for edge in inc:
            from_group[edge['neighbor_group']][middle].append(edge)
            from_block[edge['neighbor_block']][middle].append(edge)
    rows = []
    bad_records = []
    class_counts = Counter()
    distance_mismatches = []
    for g, group in enumerate(groups):
        root = group['head']
        distance = [-1] * n
        distance[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if distance[v] < 0:
                    distance[v] = distance[u] + 1
                    queue.append(v)
        assert -1 not in distance
        for target, block in enumerate(blocks):
            if block['group'] == g:
                assert distance[block['vertex']] == 1
                continue
            direct = len(from_group[g][target])
            potential = 0
            true_two_walks = 0
            middle_count = 0
            block_two_walks = 0
            candidates = []
            for middle in range(block_count):
                incoming = from_group[g][middle]
                outgoing = from_block[target][middle]
                if not incoming or not outgoing:
                    continue
                middle_count += 1
                block_two_walks += len({e['neighbor_block'] for e in incoming})
                potential += len(incoming) * len(outgoing)
                for left in incoming:
                    for right in outgoing:
                        aligned = left['leaf_here'] == right['leaf_here']
                        true_two_walks += aligned
                        if distance[block['vertex']] > 5:
                            assert not aligned
                            candidates.append({
                                'middle_block_index': middle, 'middle_block_vertex': blocks[middle]['vertex'],
                                'source_block_index': left['neighbor_block'],
                                'incoming_edge_id': left['edge_id'], 'outgoing_edge_id': right['edge_id'],
                                'current_middle_leaf_vertices': [left['leaf_here'], right['leaf_here']],
                                'current_middle_leaf_ports': [left['port_here'], right['port_here']],
                                'required_constraint': 'The two listed middle-block incidences must use the same leaf port.',
                            })
            condition = direct > 0 or true_two_walks > 0
            actual_good = distance[block['vertex']] <= 5
            if condition != actual_good:
                distance_mismatches.append([root, block['vertex'], condition, distance[block['vertex']]])
            if actual_good:
                category = 'covered'
            elif potential == 0:
                assert direct == 0
                category = 'no_block_path_within_two'
            else:
                assert direct == 0 and true_two_walks == 0
                category = 'block_paths_exist_but_middle_ports_do_not_align'
            class_counts[category] += 1
            row = {'head': root, 'head_group': g, 'target_block': block['vertex'],
                   'target_block_index': target, 'target_group': block['group'],
                   'full_graph_distance': distance[block['vertex']], 'category': category,
                   'direct_leaf_edges': direct, 'potential_middle_blocks': middle_count,
                   'potential_unweighted_block_two_walks': block_two_walks,
                   'potential_incidence_pair_routes': potential,
                   'actual_leaf_two_walks': true_two_walks}
            rows.append(row)
            if not actual_good:
                assert len(candidates) == potential
                bad_records.append({**row, 'alternative_same_port_constraints': candidates})
    assert not distance_mismatches
    assert len(bad_records) == expected_bad
    bad_rows = [row for row in rows if row['category'] != 'covered']
    good_rows = [row for row in rows if row['category'] == 'covered']
    route_stats = {}
    for label, selected in (('all_cross_group_head_block_pairs', rows), ('bad_pairs', bad_rows), ('covered_pairs', good_rows)):
        route_stats[label] = {field: distribution([row[field] for row in selected]) for field in
                             ('direct_leaf_edges', 'potential_middle_blocks', 'potential_unweighted_block_two_walks',
                              'potential_incidence_pair_routes', 'actual_leaf_two_walks')}
    with (OUT / f'{name}.pairs.tsv').open('w') as out:
        writer = csv.DictWriter(out, fieldnames=list(rows[0]), delimiter='\t')
        writer.writeheader()
        writer.writerows(rows)
    (OUT / f'{name}.bad_pair_alignment_constraints.json').write_text(json.dumps({
        'source': relative_path,
        'constraint_semantics': 'For each currently bad pair with existing block two-walks, at least one listed pair of middle-block incidences must share a leaf port. Each block must still partition its sixteen incidences into four ports of capacity four. These OR constraints are necessary and sufficient for repairing that head-block pair at fixed block incidences; independent repair choices may conflict and do not certify any other distance type.',
        'blocks': blocks, 'groups': groups, 'leaf_edge_id_reference': leaf_edges,
        'bad_pairs': bad_records,
    }, indent=2) + '\n')
    result = {
        'name': name, 'source': relative_path, 'vertices': n, 'edges': m,
        'groups': group_count, 'blocks': block_count,
        'cross_group_head_block_pairs_checked': len(rows),
        'own_group_head_block_pairs_trivially_covered': group_count * 5,
        'bad_head_block_pairs': len(bad_records), 'category_counts': dict(sorted(class_counts.items())),
        'port_independent_obstruction_exists': class_counts['no_block_path_within_two'] > 0,
        'head_block_route_condition_exact_full_head_BFS_match': True,
        'route_statistics': route_stats,
        'no_block_path_examples': [row for row in bad_records if row['category'] == 'no_block_path_within_two'][:3],
        'misaligned_route_examples': [row for row in bad_records if row['category'] != 'no_block_path_within_two'][:2],
        'cpu_seconds': time.process_time() - start,
    }
    (OUT / f'{name}.summary.json').write_text(json.dumps(result, indent=2) + '\n')
    return result

results = [
    diagnose('baseline650', 'research/ddp/m1_degree5_transfer/rithwik650_source.edges', 0),
    diagnose('expanded676', 'research/ddp/m2_hierarchical676/candidate.edges', 6),
    diagnose('cyclic676', 'research/ddp/m2_factorization676/cyclic_pairing/candidate.edges', 588),
]
output = {'status': 'COMPLETE_THREE_EXISTING_GRAPHS_READ_ONLY_DIAGNOSIS',
          'cpu_seconds': time.process_time() - START,
          'graphs': [{k: v for k, v in r.items() if k not in ('route_statistics', 'misaligned_route_examples', 'no_block_path_examples')} for r in results]}
(OUT / 'summary.json').write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps(output, indent=2))
for result in results:
    print(result['name'], 'bad-pair potential/actual route distributions:',
          json.dumps(result['route_statistics']['bad_pairs']))
