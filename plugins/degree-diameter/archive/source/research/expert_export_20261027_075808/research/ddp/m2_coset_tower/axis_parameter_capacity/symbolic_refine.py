#!/usr/bin/env python3
"""Refine only the saved 226 surviving patterns, using the shared pure routine."""
from pathlib import Path
import json
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'axis_cayley272'))
from symbolic_affine_words import affine_word_forms

def main():
    start = time.process_time()
    initial = json.loads((HERE / 'CAPACITY_RESULTS.json').read_text())
    summaries = []
    for case in initial['cases']:
        q, m, zorder, r = (case[k] for k in ('q', 'cyclic_order', 'extra_cyclic_order', 'r'))
        size = m * zorder
        product = [[(a % m + b % m) % m + m * ((a // m + b // m) % zorder)
                    for b in range(size)] for a in range(size)]
        inverse = [(-a % m) + m * ((-(a // m)) % zorder) for a in range(size)]
        scalar = [pow(r, a % m, q) for a in range(size)]
        invtypes = {c['phase']: c for c in case['involution_phase_classes']}
        patterns = json.loads((HERE / (case['name'] + '.survivors.json')).read_text())
        records, passed = [], []
        for row in patterns:
            components = [{'phase': k, 'kind': 'pair', 'free_coordinate': True}
                          for k in row['pair_phases']]
            components += [{'phase': k, 'kind': 'involution',
                            'free_coordinate': invtypes[k]['field_variable']}
                           for k in row['involution_phases']]
            symbolic = affine_word_forms(q, product, inverse, scalar, components)
            assert symbolic['raw_counts'] == row['capacity']
            assert symbolic['variable_count'] == row['field_variable_slots']
            anchor_component = next(i for i, c in enumerate(components)
                                    if c['free_coordinate'] and scalar[c['phase']] != 1)
            anchor_variable = symbolic['component_variables'][anchor_component]
            translation_direction = [1 - scalar[c['phase']] for c in components
                                     if c['free_coordinate']]
            normalized_counts = []
            for phase, forms in enumerate(symbolic['forms']):
                for coeff in forms:
                    assert sum(a * b for a, b in zip(coeff, translation_direction)) % q == (1 - scalar[phase]) % q
                projected = {c[:anchor_variable] + c[anchor_variable + 1:] for c in forms}
                normalized_counts.append(len(projected))
            # At a fixed endpoint phase, dropping a nontrivial-action anchor is
            # injective on coefficient forms by the preceding covariance identity.
            assert normalized_counts == symbolic['form_counts']
            deficient = [k for k, n in enumerate(symbolic['form_counts']) if n < q]
            critical = min(range(size), key=lambda k: symbolic['form_counts'][k])
            out = {**row, 'plain_word_capacity_pass': True,
                   'symbolic_form_counts': symbolic['form_counts'],
                   'minimum_symbolic_capacity': symbolic['form_counts'][critical],
                   'symbolic_deficient_phases': deficient, 'symbolic_pass': not deficient,
                   'anchor_component': anchor_component, 'anchor_variable': anchor_variable,
                   'anchor_drop_form_counts_unchanged': True,
                   'critical_phase': critical,
                   'critical_phase_coefficient_forms': [list(c) for c in sorted(symbolic['forms'][critical])]}
            records.append(out)
            if not deficient:
                passed.append(out)
        summary = {'name': case['name'], 'degree': case['degree'], 'group_order': case['group_order'],
                   'plain_patterns_total': case['phase_patterns'],
                   'saved_plain_pass_patterns_refined': len(patterns),
                   'symbolic_capacity_pass': len(passed),
                   'symbolic_marked_projective_input_bound': sum(p['projective_marked_input_bound'] for p in passed),
                   'branches': [{'pairs': p, 'involutions': case['degree'] - 2 * p,
                                 'symbolic_capacity_pass': sum(x['pairs'] == p for x in passed),
                                 'marked_projective_input_bound': sum(x['projective_marked_input_bound'] for x in passed if x['pairs'] == p)}
                                for p in range(case['degree'] // 2 + 1)],
                   'graphs_generated': 0, 'field_assignments_tested': 0, 'BFS_runs': 0}
        (HERE / (case['name'] + '.symbolic_patterns.json')).write_text(json.dumps(records, indent=2) + '\n')
        (HERE / (case['name'] + '.symbolic_survivors.json')).write_text(json.dumps(passed, indent=2) + '\n')
        summaries.append(summary)
        print(case['name'], 'plainpass', len(patterns), 'symbolicpass', len(passed),
              'marked_bound', summary['symbolic_marked_projective_input_bound'])
    elapsed = time.process_time() - start
    result = {'status': 'COMPLETE_SIX_FIXED_PARAMETERS_SYMBOLIC_CAPACITY_ONLY',
              'shared_pure_routine': '../axis_cayley272/symbolic_affine_words.py',
              'cases': summaries, 'CPU_seconds': elapsed,
              'cumulative_algorithm_CPU_seconds': initial['CPU_seconds'] + elapsed,
              'CPU_budget_seconds': 30, 'worker_count': 1,
              'field_assignments_tested': 0, 'graphs_generated': 0, 'BFS_runs': 0}
    assert result['cumulative_algorithm_CPU_seconds'] < 30
    (HERE / 'SYMBOLIC_CAPACITY_RESULTS.json').write_text(json.dumps(result, indent=2) + '\n')
    print('cumulative_algorithm_CPU_seconds', result['cumulative_algorithm_CPU_seconds'])

if __name__ == '__main__':
    main()
