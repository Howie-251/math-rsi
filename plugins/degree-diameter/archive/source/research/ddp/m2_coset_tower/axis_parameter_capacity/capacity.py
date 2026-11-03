#!/usr/bin/env python3
"""Six fixed affine Cayley parameters. No graph construction or BFS."""
from collections import Counter
from itertools import combinations_with_replacement
from pathlib import Path
import json
import time

HERE = Path(__file__).resolve().parent
CASES = [
    ('agl7_d4', 7, 6, 1, 3, 4, 41),
    ('agl7_times_c2_d5', 7, 6, 2, 3, 5, 72),
    ('agl13_d6', 13, 12, 1, 2, 6, 120),
    ('agl11_times_c2_d7', 11, 10, 2, 2, 7, 170),
    ('f11_c20_nonfaithful_d7', 11, 20, 1, 2, 7, 170),
    ('agl19_d8', 19, 18, 1, 2, 8, 253),
]

def bounded_multisets(classes, count):
    for ids in combinations_with_replacement(range(len(classes)), count):
        multiplicities = Counter(ids)
        if all(number <= classes[k]['actual_component_count']
               for k, number in multiplicities.items()):
            yield ids

def formal_words(degree, pair_count):
    inverse = [i ^ 1 if i < 2 * pair_count else i for i in range(degree)]
    layers = [[()]]
    for unused in range(3):
        layers.append([w + (s,) for w in layers[-1] for s in range(degree)
                       if not w or s != inverse[w[-1]]])
    assert list(map(len, layers)) == [1, degree, degree * (degree - 1),
                                     degree * (degree - 1) ** 2]
    return [w for layer in layers for w in layer]

def one_case(spec):
    name, q, m, zorder, r, degree, threshold = spec
    size = m * zorder
    add = lambda a, b: (a % m + b % m) % m + m * ((a // m + b // m) % zorder)
    neg = lambda a: (-a % m) + m * ((-(a // m)) % zorder)
    action = lambda a: pow(r, a % m, q)
    assert pow(r, m, q) == 1
    action_order = next(i for i in range(1, m + 1) if pow(r, i, q) == 1)
    moore = 1 + degree + degree * (degree - 1) + degree * (degree - 1) ** 2
    assert threshold < q * size <= moore
    pair_classes, invol_classes = [], []
    for phase in range(size):
        inverse_phase = neg(phase)
        if phase > inverse_phase:
            continue
        common = {'phase': phase, 'coordinates': [phase % m, phase // m],
                  'action': action(phase), 'inverse_phase': inverse_phase}
        if phase != inverse_phase:
            pair_classes.append({**common, 'type': 'two_distinct_phases',
                                 'actual_component_count': q})
        elif action(phase) == q - 1:
            invol_classes.append({**common, 'type': 'reflection',
                                  'actual_component_count': q,
                                  'field_variable': True})
        else:
            assert action(phase) == 1
            pair_classes.append({**common, 'type': 'self_phase_nonzero_translation',
                                 'actual_component_count': (q - 1) // 2})
            if phase:
                invol_classes.append({**common, 'type': 'central_fixed_x0',
                                      'actual_component_count': 1,
                                      'field_variable': False})
    inverse_pairs = sum(c['actual_component_count'] for c in pair_classes)
    involutions = sum(c['actual_component_count'] for c in invol_classes)
    assert 2 * inverse_pairs + involutions + 1 == q * size
    records, survivors, branches = [], [], []
    for pairs in range(degree // 2 + 1):
        inv_count = degree - 2 * pairs
        words = formal_words(degree, pairs)
        branch = {'pairs': pairs, 'involutions': inv_count,
                  'phase_patterns': 0, 'capacity_pass': 0,
                  'projective_marked_input_bound': 0, 'minimum_capacity_histogram': Counter()}
        for pair_ids in bounded_multisets(pair_classes, pairs):
            pair_phases = [pair_classes[k]['phase'] for k in pair_ids]
            for invol_ids in bounded_multisets(invol_classes, inv_count):
                invol_phases = [invol_classes[k]['phase'] for k in invol_ids]
                letter_phases = [p for k in pair_phases for p in (k, neg(k))] + invol_phases
                capacity = [0] * size
                for word in words:
                    endpoint = 0
                    for symbol in word:
                        endpoint = add(endpoint, letter_phases[symbol])
                    capacity[endpoint] += 1
                assert sum(capacity) == moore
                assert all(capacity[k] == capacity[neg(k)] for k in range(size))
                deficient = [k for k, value in enumerate(capacity) if value < q]
                fixed_centers = sum(not invol_classes[k]['field_variable'] for k in invol_ids)
                variable_phases = pair_phases + [invol_classes[k]['phase'] for k in invol_ids
                                                if invol_classes[k]['field_variable']]
                can_anchor = any(action(k) != 1 for k in variable_phases)
                free_slots = len(variable_phases)
                bound = ((q ** (free_slots - 1) - 1) // (q - 1)
                         if not deficient and can_anchor else None)
                if not deficient:
                    # If the action generated by the phases were trivial, the quotient
                    # word ball could not cover K in these six nontrivial-action cases.
                    assert can_anchor and free_slots >= 2
                row = {'id': len(records), 'pairs': pairs, 'involutions': inv_count,
                       'pair_phases': pair_phases, 'involution_phases': invol_phases,
                       'capacity': capacity, 'minimum_capacity': min(capacity),
                       'deficient_phases': deficient, 'passes': not deficient,
                       'fixed_center_slots': fixed_centers, 'field_variable_slots': free_slots,
                       'projective_marked_input_bound': bound}
                records.append(row)
                branch['phase_patterns'] += 1
                branch['minimum_capacity_histogram'][min(capacity)] += 1
                if not deficient:
                    survivors.append(row)
                    branch['capacity_pass'] += 1
                    branch['projective_marked_input_bound'] += bound
        branch['minimum_capacity_histogram'] = dict(sorted(branch['minimum_capacity_histogram'].items()))
        branches.append(branch)
    summary = {'name': name, 'q': q, 'cyclic_order': m, 'extra_cyclic_order': zorder,
               'r': r, 'action_order': action_order, 'group_order': q * size,
               'degree': degree, 'diameter_target': 3, 'saved_threshold': threshold,
               'Moore_bound': moore, 'quotient_phase_encoding': 'i + cyclic_order*z',
               'pair_phase_classes': pair_classes, 'involution_phase_classes': invol_classes,
               'actual_nonidentity_involutions': involutions, 'actual_inverse_pairs': inverse_pairs,
               'phase_patterns': len(records), 'capacity_pass': len(survivors),
               'projective_marked_input_bound': sum(b['projective_marked_input_bound'] for b in branches),
               'branches': branches, 'graphs_generated': 0, 'BFS_runs': 0}
    (HERE / (name + '.patterns.json')).write_text(json.dumps(records, indent=2) + '\n')
    (HERE / (name + '.survivors.json')).write_text(json.dumps(survivors, indent=2) + '\n')
    return summary

def main():
    start = time.process_time()
    summaries = [one_case(spec) for spec in CASES]
    result = {'status': 'COMPLETE_SIX_FIXED_PARAMETERS_CAPACITY_ONLY', 'cases': summaries,
              'CPU_seconds': time.process_time() - start, 'CPU_budget_seconds': 30,
              'worker_count': 1, 'graphs_generated': 0, 'BFS_runs': 0,
              'existing_272_and_330_not_repeated': True, 'independent_312_not_included': True}
    assert result['CPU_seconds'] < 30
    (HERE / 'CAPACITY_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    for case in summaries:
        print(case['name'], 'patterns', case['phase_patterns'], 'pass', case['capacity_pass'],
              'marked_bound', case['projective_marked_input_bound'])
    print('CPU_seconds', result['CPU_seconds'])

if __name__ == '__main__':
    main()
