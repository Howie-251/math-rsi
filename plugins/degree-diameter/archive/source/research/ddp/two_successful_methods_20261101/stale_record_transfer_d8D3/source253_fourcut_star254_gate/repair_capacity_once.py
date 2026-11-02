#!/usr/bin/env python3
"""One new cached-witness repair-capacity gate; no BFS or cut search."""
import time
START = time.process_time()
import csv
import json
import os
from pathlib import Path
import resource
import traceback

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / 'AGENTS.md').is_file())
PRIOR = 1.299030906
PREP = 0.10
resource.setrlimit(resource.RLIMIT_CPU, (8, 8))


def write(name, data):
    (HERE / name).write_text(json.dumps(data, indent=2) + '\n')


write('REPAIR_HANDLE.json', {
    'status': 'RUNNING', 'pid': os.getpid(), 'single_worker': True,
    'stage': 'cached vertex bounds then local two-old-leg repair masks',
    'prior_case_CPU_seconds': PRIOR, 'new_preparation_charge_CPU_seconds': PREP,
    'process_hard_CPU_seconds': 8, 'wholecase_CPU_cap_seconds': 10,
})

try:
    parent = json.loads((HERE / 'GATE_RESULT.json').read_text())
    assert parent['all_four_classes_strict_three_edge_capacity_NO']
    source_path = REPO / 'context/DD_PORTFOLIO_START_20261026/baselines/d8_D3_known.edges'
    with source_path.open() as stream:
        assert tuple(map(int, next(stream).split())) == (253, 1012)
        old_edges = {tuple(map(int, line.split())) for line in stream if line.strip()}
    adj = [set() for _ in range(253)]
    for u, v in old_edges:
        adj[u].add(v)
        adj[v].add(u)

    profiles = []
    for kind in range(4):
        cached = json.loads((HERE / f'GATE_TYPE{kind}_OBLIGATIONS_AND_CLASSES.json').read_text())
        profile = cached['profile']
        obligations = cached['obligations']
        s = profile['positive_label']
        m_edge = profile['maximum_single_otheredge_hits']
        assert len(obligations) == 27 and m_edge == 6
        vertex_masks = [0] * 253
        for o in obligations:
            for x in o['hitset']:
                vertex_masks[x] |= 1 << o['obligation_id']
        allowed_vertices = [x for x in range(253) if x not in (0, s)]
        m_vertex = max(vertex_masks[x].bit_count() for x in allowed_vertices)
        vertex_argmax = [x for x in allowed_vertices if vertex_masks[x].bit_count() == m_vertex]
        star_upper = 2 * m_edge + 2 * m_vertex

        # Exact local old-leg supports in H = G - {0,s}; no graph traversal.
        h_adj = [neighbors.copy() for neighbors in adj]
        h_adj[0].remove(s)
        h_adj[s].remove(0)
        closed1 = [neighbors | {x} for x, neighbors in enumerate(h_adj)]
        closed2 = []
        for x in range(253):
            support = closed1[x].copy()
            for y in h_adj[x]:
                support.update(h_adj[y])
            closed2.append(support)

        # Pair-mask table includes every possible placement of R in a <=3 walk.
        # Old-leg length pairs: (0,<=2), (<=2,0), (<=1,<=1).
        pair_masks = [0] * (253 * 253)

        def add_pair(a, b, bit):
            if a != b:
                if a > b:
                    a, b = b, a
                pair_masks[253 * a + b] |= bit

        for o in obligations:
            u, v = o['normalized_path'][0], o['normalized_path'][-1]
            bit = 1 << o['obligation_id']
            for b in closed2[v]:
                add_pair(u, b, bit)
            for a in closed2[u]:
                add_pair(a, v, bit)
            for a in closed1[u]:
                for b in closed1[v]:
                    add_pair(a, b, bit)

        classes = {}
        eligible = 0
        max_repair = -1
        first_repair = None
        mask_at_first = None
        output = HERE / f'REPAIR_TYPE{kind}_ALL_NONEDGE_MASKS.tsv'
        with output.open('w', newline='') as stream:
            out = csv.writer(stream, delimiter='\t')
            out.writerow(['repair_index', 'a', 'b', 'obligations_hit', 'mask_hex'])
            for a in allowed_vertices:
                for b in range(a + 1, 253):
                    if b in (0, s) or (a, b) in old_edges:
                        continue
                    mask = pair_masks[253 * a + b]
                    count = mask.bit_count()
                    out.writerow([eligible, a, b, count, hex(mask)])
                    classes.setdefault(mask, []).append([a, b])
                    if count > max_repair:
                        max_repair, first_repair, mask_at_first = count, [a, b], mask
                    eligible += 1
        assert eligible == 30378

        def leg(x, y):
            if x == y:
                return [x]
            if y in h_adj[x]:
                return [x, y]
            common = h_adj[x] & h_adj[y]
            if common:
                return [x, min(common), y]
            return None

        max_repair_paths = []
        position_counts = {'0': 0, '1': 0, '2': 0}
        a, b = first_repair
        for o in obligations:
            bit = 1 << o['obligation_id']
            if not (mask_at_first & bit):
                continue
            u, v = o['normalized_path'][0], o['normalized_path'][-1]
            found = None
            for ra, rb in ((a, b), (b, a)):
                left, right = leg(u, ra), leg(rb, v)
                if left is not None and right is not None and len(left) + len(right) - 1 <= 3:
                    found = left + right
                    assert len(found) - 1 <= 3 and len(set(found)) == len(found)
                    assert sum(tuple(sorted((x, y))) == (a, b) for x, y in zip(found, found[1:])) == 1
                    assert all(tuple(sorted((x, y))) == (a, b) or y in h_adj[x]
                               for x, y in zip(found, found[1:]))
                    break
            assert found is not None
            position_counts[str(o['cut_position'])] += 1
            max_repair_paths.append({
                'obligation_id': o['obligation_id'], 'old_unique3_path': o['normalized_path'],
                'old_cut_position': o['cut_position'], 'repair_path_in_H_plus_R': found,
            })
        combined = star_upper + max_repair
        result = {
            'first_type': kind, 'positive_generator': profile['positive_generator'],
            'positive_label': s, 'cached_obligation_count': len(obligations),
            'inherited_max_otheredge_hits': m_edge, 'max_other_vertex_hits': m_vertex,
            'vertex_argmax_labels': vertex_argmax,
            'star_other_six_pins_upper_bound': star_upper,
            'eligible_source_nonedges_avoiding_firstpins': eligible,
            'repair_mask_classes': len(classes), 'zero_mask_repairs': len(classes.get(0, [])),
            'max_repair_hits': max_repair, 'first_max_repair': first_repair,
            'first_max_repair_mask_hex': hex(mask_at_first),
            'first_max_repair_position_counts': position_counts,
            'combined_capacity_upper_bound': combined,
            'strict_capacity_NO': combined < len(obligations),
            'max_repair_witness_paths': max_repair_paths,
            'all_repair_data': output.name,
            'bounds_relaxations': [
                'ignore other four deleted edges in old-leg supports',
                'ignore whether repair endpoints come from two of the other cuts',
                'maximize star and repair coverage independently; overlap only lowers union',
            ],
        }
        profiles.append(result)
        write(f'REPAIR_TYPE{kind}_CLASSES_AND_WITNESSES.json', {
            'profile': result,
            'vertex_hit_masks': [
                {'label': x, 'mask_hex': hex(vertex_masks[x]), 'hit_count': vertex_masks[x].bit_count()}
                for x in allowed_vertices
            ],
            'repair_mask_classes': [
                {'mask_hex': hex(mask), 'hit_count': mask.bit_count(), 'count': len(pairs),
                 'all_nonedges': pairs} for mask, pairs in sorted(classes.items())
            ],
        })

    all_no = all(p['strict_capacity_NO'] for p in profiles)
    result = {
        'status': ('COMPLETE_NO_FIXED_CM253_FIVECUT_SOURCE_NONEDGE_REPAIR_8STAR_BY_CAPACITY'
                   if all_no else 'REPAIR_CAPACITY_PREDICTION_NOT_SUPPORTED_FIVECUT_REPAIR_FAMILY_OPEN'),
        'prediction_supported': all_no, 'all_four_classes_strict_capacity_NO': all_no,
        'profiles': profiles, 'literal_source_parse_count': 1,
        'new_BFS_field_sourcevalidation_fourcut_fivecut_graph_solver_count': 0,
        'new_graphs': 0,
        'scope': 'fixed CM253; five vertex-disjoint old cuts; one original-source-nonedge repair between two omitted endpoints from different cuts; new star on remaining eight endpoints',
        'next': 'STOP; any prototype/search/full obligations require root authorization',
    }
except Exception as exc:
    result = {
        'status': 'UNKNOWN_REPAIR_CAPACITY_PROCESS_OR_INPUT_FAILURE',
        'error_type': type(exc).__name__, 'error': str(exc),
        'traceback': traceback.format_exc(), 'prediction_supported': None,
        'scope': 'no family exclusion from a process/input failure', 'next': 'STOP preserve failure',
    }

actual = time.process_time() - START
total = PRIOR + PREP + actual
result.update({
    'prior_case_CPU_seconds': PRIOR, 'new_preparation_charge_CPU_seconds': PREP,
    'actual_process_CPU_seconds': actual, 'wholecase_CPU_seconds': total,
    'wholecase_CPU_cap_seconds': 10,
})
write('REPAIR_RESULT.json', result)
write('REPAIR_TERMINAL.json', {**result, 'terminal': True, 'active_processes': 0})
write('REPAIR_HANDLE.json', {
    'status': result['status'], 'pid': os.getpid(), 'terminal': True, 'active_processes': 0,
    'wholecase_CPU_seconds': total,
})
print(json.dumps({
    'status': result['status'], 'wholecase_CPU_seconds': total,
    'profiles': [{k: p[k] for k in (
        'first_type', 'max_other_vertex_hits', 'star_other_six_pins_upper_bound',
        'max_repair_hits', 'first_max_repair', 'first_max_repair_position_counts',
        'combined_capacity_upper_bound', 'strict_capacity_NO',
    )} for p in result.get('profiles', [])],
    'error': result.get('error'),
}))
