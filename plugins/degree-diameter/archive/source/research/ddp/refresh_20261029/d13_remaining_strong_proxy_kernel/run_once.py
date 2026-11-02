#!/usr/bin/env python3
"""One fixed current-source closed-B1 certificate kernel; no BFS or solver."""
from collections import Counter, deque
import json
from pathlib import Path
import resource
import time

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
BASE = ROOT / 'research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe'


def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n')


def load(path):
    return json.loads(path.read_text())


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (20, 20))
    start = time.process_time()
    pred = load(OUT / 'PREDICTION.json')
    assert pred['status'] == 'FROZEN_BEFORE_KERNEL_EXECUTION'
    original = load(BASE / 'RESULT.json')['rows']
    continuation = load(BASE / 'continuation/RESULT.json')['rows']
    failed = sorted((r for r in original + continuation if 'ACCEPTED' not in r['status']),
                    key=lambda r: r['ordinal'])
    assert len(failed) == 51
    n = pred['source_n']
    adj = [set() for _ in range(n)]
    edges = 0
    # The sole read of the actual source edge table.
    with (ROOT / pred['source_graph']).open() as handle:
        assert tuple(map(int, next(handle).split())) == (n, pred['source_m'])
        for line in handle:
            if not line.strip() or line.lstrip().startswith('#'):
                continue
            u, v = map(int, line.split())
            assert 0 <= u < n and 0 <= v < n and u != v and v not in adj[u]
            adj[u].add(v)
            adj[v].add(u)
            edges += 1
    degrees = list(map(len, adj))
    assert edges == pred['source_m'] and max(degrees) <= 13
    pool = [r for r in failed if all(degrees[p] < 13 for p in r['mandatory_pins'])]
    assert len(pool) == 38
    frozen = []
    for old in pool:
        v = old['prototype']
        current = sorted(adj[v])
        saturated = [u for u in current if degrees[u] == 13]
        f = saturated[0] if len(saturated) == 1 else None
        pins = [u for u in current if u != f] if f is not None else None
        frozen.append({
            'ordinal': old['ordinal'], 'prototype': v,
            'old_status': old['status'],
            'original_deleted_saturated_pin': old['deleted_saturated_pin'],
            'original_mandatory': old['mandatory_pins'],
            'current_neighborhood': current,
            'current_neighbor_degrees': {str(u): degrees[u] for u in current},
            'current_saturated_neighbors': saturated,
            'omitted_saturated_pin': f,
            'mandatory_P': pins,
            'guard_budget': 13-len(pins) if pins is not None else None,
            'current_eligible': pins is not None and len(pins) <= 13 and
                                all(degrees[u] < 13 for u in pins)
        })
    # This literal38 and every current P are saved before any DP transition.
    write('FROZEN_POOL.json', {
        'status': 'FROZEN_BEFORE_ANY_DP',
        'source_graph': pred['source_graph'], 'source_n': n, 'source_m': edges,
        'maximum_degree': max(degrees),
        'source_degree_histogram': dict(sorted(Counter(degrees).items())),
        'old_failure_count': len(failed), 'original_mandatory_still_free_count': len(pool),
        'blocked_old_failure_prototypes': [r['prototype'] for r in failed if r not in pool],
        'records': frozen
    })
    rows = []
    hit = None
    dp_runs = 0
    for item in frozen:
        row = dict(item)
        if not item['current_eligible']:
            row['status'] = 'CURRENT_RULE_INELIGIBLE'
            rows.append(row)
            continue
        v, f = item['prototype'], item['omitted_saturated_pin']
        pins = set(item['mandatory_P'])
        covered = set(pins)
        for p in pins:
            covered.update(adj[p])
        full_targets = sorted(adj[f])
        residual = sorted(set(full_targets) - covered)
        assert len(full_targets) <= 13
        candidates = set()
        supports = {}
        for r in residual:
            support = sorted(g for g in adj[r] | {r} if degrees[g] < 13 and g not in pins)
            supports[str(r)] = support
            candidates.update(support)
        masks = {}
        raw_masks = {}
        for g in sorted(candidates):
            mask = sum(1 << j for j, r in enumerate(residual) if g == r or r in adj[g])
            assert mask
            raw_masks[g] = mask
            masks.setdefault(mask, g)
        row.update({
            'omitted_pin_degree': degrees[f],
            'omitted_pin_neighbors': full_targets,
            'mandatory_closedB1_covered_neighbors': sorted(set(full_targets) & covered),
            'residual_targets': residual,
            'free_guard_supports': supports,
            'eligible_useful_guards': len(candidates),
            'unique_nonzero_masks': len(masks),
            'guard_columns': [{'guard': g, 'current_degree': degrees[g], 'mask': raw_masks[g]}
                              for g in sorted(candidates)],
        })
        # Reuse the already proved current v4580 negative rather than rerun it.
        if v == 4580 and f == 45089 and sorted(pins) == sorted(item['original_mandatory']):
            proof = load(OUT.parent / 'd13_joint_capacity_read/ANALYSIS.json')['v4580']['strong_proxy_obstruction']
            groups = proof['five_disjoint_supports']
            assert len(groups) == 5 and item['guard_budget'] == 4
            actual_groups = []
            for group in groups:
                r = group['target']
                assert r in residual
                # The old proof's supports can only shrink in this kept-edge source.
                actual = set(supports[str(r)])
                assert actual <= set(group['old_free_closed_B1_coverers'])
                actual_groups.append(actual)
            assert all(not actual_groups[i] & actual_groups[j]
                       for i in range(5) for j in range(i))
            row.update({
                'status': 'REUSED_PROVED_STRONG_LOWER_BOUND_EXCEEDS_BUDGET',
                'guard_lower_bound': 5, 'DP_executed': False,
                'proof_source': 'research/ddp/refresh_20261029/d13_joint_capacity_read/ANALYSIS.json',
                'reused_proof_current_support_sets_checked': True
            })
            rows.append(row)
            continue
        zero_support = [r for r in residual if not supports[str(r)]]
        if zero_support:
            row.update({'status': 'STRONG_CERTIFICATE_IMPOSSIBLE_ZERO_SUPPORT',
                        'zero_support_targets': zero_support, 'DP_executed': False})
            rows.append(row)
            continue
        budget = item['guard_budget']
        target_mask = (1 << len(residual)) - 1
        dp_runs += 1
        # Breadth by number of union columns, not graph-distance BFS.
        distances = {0: 0}
        predecessor = {}
        queue = deque([0])
        found = target_mask == 0
        transitions = 0
        while queue and not found:
            mask = queue.popleft()
            depth = distances[mask]
            if depth == budget:
                continue
            for column, g in masks.items():
                nxt = mask | column
                transitions += 1
                if nxt in distances:
                    continue
                distances[nxt] = depth + 1
                predecessor[nxt] = (mask, g)
                if nxt == target_mask:
                    found = True
                    break
                queue.append(nxt)
        row.update({'DP_executed': True, 'DP_reached_states': len(distances),
                    'DP_transitions': transitions, 'DP_guard_cap': budget})
        if found:
            chosen = []
            mask = target_mask
            while mask:
                mask, g = predecessor[mask]
                chosen.append(g)
            guards = sorted(chosen)
            selected = sorted(pins | set(guards))
            assert len(guards) == distances[target_mask] and len(set(guards)) == len(guards)
            assert len(selected) <= 13 and all(degrees[g] < 13 for g in selected)
            selected_closed = set(selected)
            for g in selected:
                selected_closed.update(adj[g])
            assert set(full_targets) <= selected_closed
            witnesses = {str(r): min(g for g in selected if g == r or r in adj[g])
                         for r in full_targets}
            row.update({'status': 'PROOF_BACKED_STRONG_CERTIFICATE_HIT',
                        'minimum_guard_count': len(guards), 'guards_A': guards,
                        'selected_S': selected,
                        'selected_current_degrees': {str(g): degrees[g] for g in selected},
                        'neighbor_cover_witnesses': witnesses})
            hit = row
            write('HIT.json', {
                'status': 'PROOF_BACKED_HIT_PENDING_ROOT_GRAPH_AND_INDEPENDENT_ACCEPTANCE',
                'source_graph': pred['source_graph'], 'source_n': n, 'source_m': edges,
                'new_vertex_label': n, 'new_vertex_degree': len(selected),
                'new_edges': [[n, g] for g in selected],
                'certificate': pred['certificate'], 'record': row,
                'generated_complete_graph': False, 'new_graph_BFS_calls': 0
            })
            (OUT / 'selected_S.txt').write_text(' '.join(map(str, selected)) + '\n')
            rows.append(row)
            break
        row.update({'status': 'EXACT_NO_STRONG_CERTIFICATE_WITHIN_ACTUAL_BUDGET',
                    'minimum_guard_count_lower_bound': budget+1})
        rows.append(row)
    cpu = time.process_time() - start
    result = {
        'status': 'FIRST_PROOF_BACKED_HIT' if hit else 'COMPLETE_FIXED38_STRONG_CERTIFICATE_NEGATIVE',
        'running': False, 'source_graph': pred['source_graph'], 'source_n': n, 'source_m': edges,
        'frozen_count': len(frozen), 'visited': len(rows), 'unattempted': len(frozen)-len(rows),
        'row_status_counts': dict(Counter(r['status'] for r in rows)),
        'DP_runs': dp_runs, 'rows': rows,
        'proof_backed_hits': int(hit is not None),
        'prediction': 'SUPPORTED_PENDING_ROOT_ACCEPTANCE' if hit else 'REFUTED_WITHIN_FIXED_STRONG_CERTIFICATE_SCOPE',
        'source_edge_reads': 1, 'workers': 1,
        'source_header_parse_correction': 'Initial invocation rejected the numeric n/m header before reading any edge row or running any DP; parser corrected to consume the documented header explicitly. Edge rows read once in the successful invocation.',
        'CPU_seconds': cpu, 'CPU_budget_seconds': 20,
        'solver_calls': 0, 'graph_distance_BFS_calls': 0,
        'complete_graphs_generated': 0, 'main_Wiki_changed': False,
        'unrestricted_R4_guard_covers_excluded': False,
        'pending': ['Root complete graph construction and independent acceptance'] if hit else []
    }
    write('RESULT.json', result)
    write('TERMINAL.json', {k: result[k] for k in [
        'status', 'running', 'frozen_count', 'visited', 'unattempted', 'row_status_counts',
        'DP_runs', 'proof_backed_hits', 'source_edge_reads', 'workers', 'CPU_seconds',
        'CPU_budget_seconds', 'solver_calls', 'graph_distance_BFS_calls',
        'complete_graphs_generated', 'main_Wiki_changed', 'pending']})
    print(json.dumps({k: result[k] for k in [
        'status', 'frozen_count', 'visited', 'unattempted', 'row_status_counts',
        'DP_runs', 'CPU_seconds', 'proof_backed_hits']}), flush=True)


if __name__ == '__main__':
    main()
