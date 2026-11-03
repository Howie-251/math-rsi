#!/usr/bin/env python3
"""Whole route-block certificate from a saved exact R4 matrix."""
from collections import deque
import json
from pathlib import Path
import resource
import time

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]


def read(path):
    return json.loads(path.read_text())


def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, indent=2) + '\n')


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
    start = time.process_time()
    pred = read(OUT / 'PREDICTION.json')
    cache = read(ROOT / pred['prepared_json'])
    n, m = pred['source_n'], pred['source_m']
    prototype, f = pred['prototype'], pred['omitted_saturated_pin']
    pins = sorted(pred['mandatory_P'])
    assert (cache['source_n'], cache['source_m']) == (n, m)
    assert sorted(cache['pins']) == pins
    missing = cache['missing']
    representatives = cache['representatives']
    assert len(missing) == cache['missing_count'] == pred['prepared_missing_targets']
    assert len(representatives) == cache['unique_nonzero_masks'] == pred['prepared_unique_guard_masks']
    assert len(set(missing)) == len(missing)
    assert len(set(representatives)) == len(representatives)
    assert cache['mask_bit_order'] == 'little target-index bits per nativeu64 row'
    rowbytes = cache['mask_words_per_row'] * 8
    binary = (ROOT / pred['prepared_binary']).read_bytes()
    assert len(binary) == rowbytes * len(representatives)
    target_masks = [int.from_bytes(binary[i:i+rowbytes], 'little')
                    for i in range(0, len(binary), rowbytes)]
    assert all(mask and mask >> len(missing) == 0 for mask in target_masks)
    adj = [set() for _ in range(n)]
    edges = 0
    with (ROOT / pred['source_graph']).open() as handle:
        assert tuple(map(int, next(handle).split())) == (n, m)
        for line in handle:
            if not line.strip():
                continue
            u, v = map(int, line.split())
            assert 0 <= u < n and 0 <= v < n and u != v and v not in adj[u]
            adj[u].add(v)
            adj[v].add(u)
            edges += 1
    degrees = list(map(len, adj))
    assert edges == m and max(degrees) <= 13
    assert adj[prototype] == set(pins) | {f}
    assert degrees[f] == 13
    assert all(degrees[p] < 13 for p in pins)
    assert all(degrees[g] < 13 and g not in pins for g in representatives)
    assert [degrees[p] for p in cache['pins']] == cache['pin_current_degrees']
    target_index = {t: i for i, t in enumerate(missing)}
    all_targets = (1 << len(missing)) - 1
    blocks = []
    union = 0
    # Exactly13 local closed radius-three expansions; no full-source checks.
    for r in sorted(adj[f]):
        seen = {r}
        frontier = {r}
        layers = [1]
        for _ in range(3):
            nxt = set()
            for u in frontier:
                nxt.update(adj[u])
            nxt.difference_update(seen)
            seen.update(nxt)
            frontier = nxt
            layers.append(len(frontier))
        labels = sorted(seen & target_index.keys())
        target_mask = sum(1 << target_index[t] for t in labels)
        union |= target_mask
        blocks.append({'center_r': r, 'current_degree': degrees[r],
                       'local_closed_B3_size': len(seen), 'local_layer_sizes': layers,
                       'target_count': len(labels), 'targets': labels,
                       'target_index_mask': target_mask})
    assert len(blocks) == 13 and union == all_targets
    nonempty = [b for b in blocks if b['target_count']]
    assert len(nonempty) <= 13
    for j, block in enumerate(nonempty):
        block['block_bit'] = j
    full = (1 << len(nonempty)) - 1
    columns = []
    unique = {}
    for g, mask in zip(representatives, target_masks):
        block_mask = 0
        near_mask = 0
        for j, block in enumerate(nonempty):
            r = block['center_r']
            covers_whole = mask & block['target_index_mask'] == block['target_index_mask']
            if covers_whole:
                block_mask |= 1 << j
            if g == r or r in adj[g]:
                near_mask |= 1 << j
                assert covers_whole
        columns.append({'guard': g, 'current_degree': degrees[g],
                        'whole_block_mask': block_mask,
                        'closedB1_center_mask': near_mask,
                        'far_route_additional_block_mask': block_mask & ~near_mask})
        if block_mask:
            unique.setdefault(block_mask, g)
    zero = []
    for j, block in enumerate(nonempty):
        bit = 1 << j
        support = [c['guard'] for c in columns if c['whole_block_mask'] & bit]
        near = [c['guard'] for c in columns if c['closedB1_center_mask'] & bit]
        far = [c['guard'] for c in columns if c['far_route_additional_block_mask'] & bit]
        block.update({'whole_block_covering_guard_representatives': support,
                      'whole_block_support_count': len(support),
                      'near_center_support_count_among_representatives': len(near),
                      'far_route_support_count_among_representatives': len(far)})
        if not support:
            zero.append(block['center_r'])
    write('BLOCKS.json', {
        'source_n': n, 'source_m': m, 'prototype': prototype, 'omitted_pin': f,
        'mandatory_P': pins, 'missing_targets': len(missing),
        'local_radius3_expansions': len(blocks), 'nonempty_blocks': len(nonempty),
        'all_missing_targets_in_block_union': union == all_targets,
        'target_index_order_source': pred['prepared_json'],
        'blocks': blocks
    })
    write('GUARD_BLOCK_MASKS.json', {
        'source_n': n, 'guard_representatives': len(columns),
        'block_bit_order': [b['center_r'] for b in nonempty],
        'columns': columns,
        'unique_nonzero_block_masks': [{'mask': mask, 'representative_guard': g}
                                       for mask, g in unique.items()]
    })
    # Exact shortest-union DP capped at the actual four-guard budget.
    distances = {0: 0}
    predecessor = {}
    queue = deque([0])
    transitions = 0
    found = full == 0
    while queue and not found:
        mask = queue.popleft()
        depth = distances[mask]
        if depth == pred['guard_limit']:
            continue
        for column, g in unique.items():
            nxt = mask | column
            transitions += 1
            if nxt in distances:
                continue
            distances[nxt] = depth + 1
            predecessor[nxt] = (mask, g)
            if nxt == full:
                found = True
                break
            queue.append(nxt)
    guards = []
    selected = None
    if found:
        mask = full
        while mask:
            mask, g = predecessor[mask]
            guards.append(g)
        guards.sort()
        assert len(guards) == len(set(guards)) == distances[full] <= pred['guard_limit']
        assert len(guards) >= 3 or not cache['exact_two_complete']
        chosen_mask = 0
        for g in guards:
            chosen_mask |= target_masks[representatives.index(g)]
        assert chosen_mask == all_targets
        selected = sorted(pins + guards)
        assert len(set(selected)) == len(selected) <= 13
        assert all(degrees[g] < 13 for g in selected)
        witness = {str(b['center_r']): min(g for g in guards
                   if target_masks[representatives.index(g)] & b['target_index_mask'] == b['target_index_mask'])
                   for b in nonempty}
        write('HIT.json', {
            'status': 'WHOLE_ROUTE_BLOCK_PROOF_BACKED_HIT_PENDING_ROOT_ACCEPTANCE',
            'source_graph': pred['source_graph'], 'source_n': n, 'source_m': m,
            'prototype': prototype, 'omitted_saturated_pin': f,
            'mandatory_P': pins, 'guards_A': guards, 'selected_S': selected,
            'selected_current_degrees': {str(g): degrees[g] for g in selected},
            'block_cover_witnesses': witness,
            'all_saved_target_bits_covered': True,
            'complete_graph_generated': False,
            'new_selected_R4_BFS': 0, 'source_allroot_BFS': 0
        })
        (OUT / 'selected_S.txt').write_text(' '.join(map(str, selected)) + '\n')
    cpu = time.process_time() - start
    result = {
        'status': 'FIRST_PROOF_BACKED_WHOLE_ROUTE_BLOCK_HIT' if found else 'COMPLETE_WHOLE_ROUTE_BLOCK_NEGATIVE',
        'running': False, 'source_n': n, 'source_m': m,
        'prototype': prototype, 'omitted_saturated_pin': f,
        'mandatory_P': pins, 'guard_limit': pred['guard_limit'],
        'missing_targets': len(missing), 'guard_representatives': len(representatives),
        'local_radius3_expansions': len(blocks), 'nonempty_blocks': len(nonempty),
        'all_missing_targets_in_block_union': True,
        'unique_nonzero_block_masks': len(unique),
        'guards_with_nonzero_block_mask': sum(bool(c['whole_block_mask']) for c in columns),
        'guards_with_far_route_additional_blocks': sum(bool(c['far_route_additional_block_mask']) for c in columns),
        'zero_whole_block_support_centers': zero,
        'DP_states': len(distances), 'DP_transitions': transitions,
        'minimum_guard_count_if_found': len(guards) if found else None,
        'guards_A': guards if found else None, 'selected_S': selected,
        'prediction': 'SUPPORTED_PENDING_ROOT_ACCEPTANCE' if found else 'REFUTED_ONLY_IN_FIXED_WHOLE_BLOCK_SUFFICIENT_DOMAIN',
        'arbitrary_four_guard_R4_excluded': False,
        'CPU_seconds': cpu, 'CPU_budget_seconds': 20, 'workers': 1,
        'source_edge_reads': 1, 'source_allroot_BFS': 0,
        'new_selected_R4_BFS': 0, 'solver_calls': 0,
        'complete_graphs_generated': 0, 'main_Wiki_changed': False,
        'pending': ['Root complete graph construction and independent acceptance'] if found else []
    }
    write('RESULT.json', result)
    write('TERMINAL.json', {k: result[k] for k in [
        'status', 'running', 'prototype', 'missing_targets', 'guard_representatives',
        'local_radius3_expansions', 'nonempty_blocks', 'unique_nonzero_block_masks',
        'zero_whole_block_support_centers', 'DP_states', 'DP_transitions',
        'CPU_seconds', 'CPU_budget_seconds', 'workers', 'source_allroot_BFS',
        'new_selected_R4_BFS', 'solver_calls', 'complete_graphs_generated', 'pending']})
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
