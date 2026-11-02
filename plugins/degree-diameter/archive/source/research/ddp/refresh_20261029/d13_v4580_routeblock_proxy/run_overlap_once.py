#!/usr/bin/env python3
"""One overlap-aware acceptance DP on the unchanged saved nine block masks."""
from collections import deque
import json
from pathlib import Path
import resource
import time

OUT = Path(__file__).resolve().parent


def read(name):
    return json.loads((OUT / name).read_text())


def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n')


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (1, 1))
    start = time.process_time()
    pred = read('PREDICTION.json')
    assert pred['revisions'][-1]['status'] == 'FROZEN_BEFORE_CORRECTED_ACCEPTANCE_DP'
    data = read('BLOCKS.json')
    guards_data = read('GUARD_BLOCK_MASKS.json')
    blocks = sorted((b for b in data['blocks'] if b['target_count']), key=lambda b: b['block_bit'])
    columns = guards_data['unique_nonzero_block_masks']
    assert len(columns) == 9 and len(blocks) == 11
    assert [b['center_r'] for b in blocks] == guards_data['block_bit_order']
    full_targets = (1 << data['missing_targets']) - 1
    unions = {0: 0}

    def target_union(mask):
        if mask not in unions:
            bit = mask & -mask
            unions[mask] = target_union(mask ^ bit) | blocks[bit.bit_length()-1]['target_index_mask']
        return unions[mask]

    distances = {0: 0}
    previous = {}
    queue = deque([0])
    transitions = 0
    hit_state = None
    while queue and hit_state is None:
        mask = queue.popleft()
        if distances[mask] == pred['guard_limit']:
            continue
        for column in columns:
            nxt = mask | column['mask']
            transitions += 1
            if nxt in distances:
                continue
            distances[nxt] = distances[mask] + 1
            previous[nxt] = (mask, column['representative_guard'])
            if target_union(nxt) == full_targets:
                hit_state = nxt
                break
            queue.append(nxt)
    chosen = None
    selected = None
    if hit_state is not None:
        chosen = []
        cursor = hit_state
        while cursor:
            cursor, g = previous[cursor]
            chosen.append(g)
        chosen.sort()
        assert len(set(chosen)) == len(chosen) == distances[hit_state] <= pred['guard_limit']
        selected = sorted(pred['mandatory_P'] + chosen)
        assert len(set(selected)) == len(selected) <= 13
        by_guard = {c['guard']: c for c in guards_data['columns']}
        assert all(by_guard[g]['current_degree'] < 13 for g in chosen)
        actual_blocks = [b for b in blocks if hit_state >> b['block_bit'] & 1]
        witnesses = {str(b['center_r']): min(g for g in chosen
                     if by_guard[g]['whole_block_mask'] >> b['block_bit'] & 1)
                     for b in actual_blocks}
        write('OVERLAP_HIT.json', {
            'status': 'OVERLAP_AWARE_WHOLE_ROUTE_BLOCK_HIT_PENDING_ROOT_ACCEPTANCE',
            'source_graph': pred['source_graph'], 'source_n': pred['source_n'],
            'source_m': pred['source_m'], 'prototype': pred['prototype'],
            'mandatory_P': pred['mandatory_P'], 'guards_A': chosen, 'selected_S': selected,
            'guard_current_degrees': {str(g): by_guard[g]['current_degree'] for g in chosen},
            'covered_block_state': hit_state, 'block_cover_witnesses': witnesses,
            'covered_target_count': target_union(hit_state).bit_count(),
            'all2755_missing_targets_covered_by_whole_block_union': True,
            'new_graphs': 0, 'new_graph_reads': 0, 'new_neighborhood_expansions': 0,
            'new_R4_BFS': 0, 'solver_calls': 0
        })
        (OUT / 'overlap_selected_S.txt').write_text(' '.join(map(str, selected)) + '\n')
    states = []
    for mask, depth in distances.items():
        predecessor, g = previous.get(mask, (None, None))
        states.append({'block_mask': mask, 'guard_count': depth,
                       'covered_target_count': target_union(mask).bit_count(),
                       'target_union_mask': target_union(mask),
                       'previous_block_mask': predecessor, 'last_guard': g})
    write('OVERLAP_DP_STATES.json', {
        'block_bit_order': guards_data['block_bit_order'],
        'guard_cap': pred['guard_limit'], 'states': states,
        'hit_state': hit_state,
        'complete_within_cap': hit_state is None
    })
    cpu = time.process_time() - start
    result = {
        'status': 'FIRST_PROOF_BACKED_OVERLAP_AWARE_WHOLE_ROUTE_BLOCK_HIT' if chosen is not None
                  else 'COMPLETE_OVERLAP_AWARE_WHOLE_ROUTE_BLOCK_NEGATIVE',
        'running': False, 'source_n': pred['source_n'], 'source_m': pred['source_m'],
        'prototype': pred['prototype'], 'guard_cap': pred['guard_limit'],
        'same_guard_pool': True, 'same_saved_blocks': True, 'unique_nonzero_block_masks': len(columns),
        'acceptance': 'Actual target union of covered complete route blocks equals all2755 missing targets.',
        'DP_states': len(distances), 'DP_transitions': transitions,
        'minimum_guard_count_if_found': len(chosen) if chosen is not None else None,
        'guards_A': chosen, 'selected_S': selected,
        'new_graph_reads': 0, 'new_local_B3_expansions': 0, 'new_R4_BFS': 0,
        'new_source_allroot_BFS': 0, 'solver_calls': 0, 'complete_graphs_generated': 0,
        'CPU_seconds': cpu, 'CPU_budget_seconds': 1, 'workers': 1,
        'unrestricted_four_guard_R4_excluded': False,
        'pending': ['Root graph generation and independent acceptance'] if chosen is not None else [],
        'stopped_no_refinement': True
    }
    write('OVERLAP_RESULT.json', result)
    write('OVERLAP_TERMINAL.json', result)
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
