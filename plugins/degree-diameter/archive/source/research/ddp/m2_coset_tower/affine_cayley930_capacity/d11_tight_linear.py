#!/usr/bin/env python3
"""One necessary tight-fiber linear pass on the existing 78 degree11 patterns."""
from collections import Counter
from pathlib import Path
import json
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'axis_cayley272'))
from symbolic_affine_words import affine_word_forms

def kernel(matrix, columns):
    reduced = [[x % 31 for x in row] for row in matrix]
    pivots = []
    for col in range(columns):
        pivot = next((r for r in range(len(pivots), len(reduced)) if reduced[r][col]), None)
        if pivot is None:
            continue
        row = len(pivots)
        reduced[row], reduced[pivot] = reduced[pivot], reduced[row]
        scale = pow(reduced[row][col], -1, 31)
        reduced[row] = [x * scale % 31 for x in reduced[row]]
        for r in range(len(reduced)):
            if r != row and reduced[r][col]:
                scale = reduced[r][col]
                reduced[r] = [(x - scale * y) % 31 for x, y in zip(reduced[r], reduced[row])]
        pivots.append(col)
    free = [c for c in range(columns) if c not in pivots]
    basis = []
    for col in free:
        vector = [int(i == col) for i in range(columns)]
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][col] % 31
        assert all(sum(x * y for x, y in zip(r, vector)) % 31 == 0 for r in matrix)
        basis.append(vector)
    return reduced, pivots, basis

def main():
    start = time.process_time()
    originals = [json.loads(line) for line in (HERE / 'survivors.jsonl').open()]
    originals = [row for row in originals if row['degree'] == 11]
    assert len(originals) == 78
    product = [[(i + j) % 30 for j in range(30)] for i in range(30)]
    inverse = [(-j) % 30 for j in range(30)]
    scalar = [pow(3, j, 31) for j in range(30)]
    results, survivors = [], []
    processed_tight = 0
    for row in originals:
        assert time.process_time() - start < 20
        tight = [j for j, count in enumerate(row['symbolic_capacity']) if count == 31]
        m, anchor = row['field_variables'], row['anchor_component']
        n = m - 1
        full_matrix, matrix = [], []
        if tight:
            processed_tight += 1
            components = [{'phase': j, 'kind': 'pair'} for j in row['pair_phases']]
            components += [{'phase': 15, 'kind': 'involution'} for _ in range(row['involution_count'])]
            symbolic = affine_word_forms(31, product, inverse, scalar, components)
            assert symbolic['form_counts'] == row['symbolic_capacity']
            forms = [{c[:anchor] + c[anchor + 1:] for c in group}
                     for group in symbolic['forms']]
            assert list(map(len, forms)) == row['symbolic_capacity']
            for phase in tight:
                full = [sum(c[i] for c in symbolic['forms'][phase]) % 31 for i in range(m)]
                reduced = full[:anchor] + full[anchor + 1:]
                assert reduced == [sum(c[i] for c in forms[phase]) % 31 for i in range(n)]
                full_matrix.append(full)
                matrix.append(reduced)
            reduced, pivots, basis = kernel(matrix, n)
            restricted = [{tuple(sum(x * y for x, y in zip(c, b)) % 31 for b in basis)
                           for c in phase_forms} for phase_forms in forms]
            counts = list(map(len, restricted))
            witness_phase = min(range(30), key=lambda j: counts[j])
            witness_forms = [list(c) for c in sorted(restricted[witness_phase])]
        else:
            reduced, pivots, basis = kernel([], n)
            counts = row['symbolic_capacity']
            witness_phase, witness_forms = None, None
        deficient = [j for j, count in enumerate(counts) if count < 31]
        dimension = len(basis)
        marked = (31 ** dimension - 1) // 30
        result = {**row, 'original_tight_phases': tight,
                  'sum_coeff_matrix_full_variables': full_matrix,
                  'sum_coeff_matrix_after_anchor': matrix,
                  'rank_mod31': len(pivots), 'rref': reduced, 'pivot_columns': pivots,
                  'nullspace_basis_after_anchor': basis,
                  'nullspace_dimension': dimension,
                  'restricted_form_counts': counts,
                  'restricted_deficient_phases': deficient,
                  'passes_one_tight_linear_step': not deficient,
                  'projective_marked_inputs_after_linear_constraints': marked,
                  'newly_tight_phases_not_iterated': [j for j, count in enumerate(counts)
                                                      if count == 31 and j not in tight],
                  'restricted_witness_phase': witness_phase,
                  'restricted_witness_forms': witness_forms}
        results.append(result)
        if not deficient:
            survivors.append(result)
    assert processed_tight == 41
    (HERE / 'd11_tight_linear.patterns.json').write_text(json.dumps(results, indent=2) + '\n')
    (HERE / 'd11_tight_linear.survivors.json').write_text(json.dumps(survivors, indent=2) + '\n')
    elapsed = time.process_time() - start
    summary = {'status': 'COMPLETE_ONE_TIGHT_LINEAR_STEP_D11_ONLY',
               'input_patterns': 78, 'patterns_with_original_tight31_fiber': processed_tight,
               'patterns_without_tight31_fiber': 78 - processed_tight,
               'rank_histogram_all_patterns': dict(sorted(Counter(r['rank_mod31'] for r in results).items())),
               'patterns_rejected_after_nullspace_form_dedup': 78 - len(survivors),
               'patterns_surviving': len(survivors),
               'projective_marked_inputs_before': sum(r['projective_marked_inputs'] for r in results),
               'projective_marked_inputs_after': sum(r['projective_marked_inputs_after_linear_constraints'] for r in survivors),
               'branches': [{'pairs': p, 'involutions': 11 - 2 * p,
                             'input_patterns': sum(r['pair_count'] == p for r in results),
                             'patterns_with_tight31': sum(r['pair_count'] == p and bool(r['original_tight_phases']) for r in results),
                             'surviving_patterns': sum(r['pair_count'] == p for r in survivors),
                             'projective_marked_inputs_after': sum(r['projective_marked_inputs_after_linear_constraints'] for r in survivors if r['pair_count'] == p)}
                            for p in (4, 5)],
               'CPU_seconds': elapsed, 'CPU_budget_seconds': 20, 'worker_count': 1,
               'field_assignments_tested': 0, 'graphs_generated': 0, 'BFS_runs': 0,
               'd12_patterns_processed': 0, 'iteration_count': 1, 'running': False}
    (HERE / 'd11_tight_linear.terminal.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main()
