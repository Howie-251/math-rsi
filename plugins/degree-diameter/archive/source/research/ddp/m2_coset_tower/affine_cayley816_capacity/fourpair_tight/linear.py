#!/usr/bin/env python3
"""Iterate necessary exact-17-fiber sum constraints on only the12 four-pair modes."""
from pathlib import Path
import json
import sys
import time

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / 'axis_cayley272'))
from symbolic_affine_words import affine_word_forms
Q, M = 17, 48


def kernel(matrix, columns):
    reduced = [[x % Q for x in r] for r in matrix]
    pivots = []
    for col in range(columns):
        pivot = next((r for r in range(len(pivots), len(reduced)) if reduced[r][col]), None)
        if pivot is None:
            continue
        row = len(pivots)
        reduced[row], reduced[pivot] = reduced[pivot], reduced[row]
        scale = pow(reduced[row][col], -1, Q)
        reduced[row] = [x * scale % Q for x in reduced[row]]
        for r in range(len(reduced)):
            if r != row and reduced[r][col]:
                scale = reduced[r][col]
                reduced[r] = [(x - scale * y) % Q for x, y in zip(reduced[r], reduced[row])]
        pivots.append(col)
    basis = []
    for col in range(columns):
        if col in pivots:
            continue
        v = [int(i == col) for i in range(columns)]
        for row, pivot in enumerate(pivots):
            v[pivot] = -reduced[row][col] % Q
        assert all(sum(x * y for x, y in zip(r, v)) % Q == 0 for r in matrix)
        basis.append(v)
    return reduced, pivots, basis


def project(forms, basis):
    return [{tuple(sum(x * y for x, y in zip(c, b)) % Q for b in basis) for c in cell}
            for cell in forms]


def compose(new, old):
    return [[sum(k * old[i][j] for i, k in enumerate(row)) % Q for j in range(7)]
            for row in new]


def main():
    start = time.process_time()
    assert not (HERE / 'linear.terminal.json').exists(), 'No automatic rerun'
    rows = [json.loads(s) for s in (HERE.parent / 'survivors.jsonl').read_text().splitlines()]
    rows = [r for r in rows if r['pair_count'] == 4]
    assert len(rows) == 12 and all(r['involution_count'] == 4 and min(r['symbolic_capacity']) == Q for r in rows)
    assert sum(r['projective_marked_inputs'] for r in rows) == 307754004
    scalar = [pow(3, j, Q) for j in range(M)]
    assert scalar[8] == 16 and scalar[16] == 1 and scalar[24] == 16
    product = [[(i + j) % M for j in range(M)] for i in range(M)]
    inverse = [(-j) % M for j in range(M)]
    results, survivors = [], []
    calibration = None
    for index, row in enumerate(rows):
        assert time.process_time() - start < 110
        phases = row['pair_phases'] + [24] * 4
        anchor = next(i for i, j in enumerate(phases) if scalar[j] != 1)
        assert anchor == row['anchor_component']
        components = [{'phase': j, 'kind': 'pair'} for j in row['pair_phases']]
        components += [{'phase': 24, 'kind': 'involution'} for _ in range(4)]
        original = affine_word_forms(Q, product, inverse, scalar, components)
        assert original['form_counts'] == row['symbolic_capacity']
        anchored = [{c[:anchor] + c[anchor + 1:] for c in cell} for cell in original['forms']]
        assert list(map(len, anchored)) == original['form_counts']
        basis = [[int(i == j) for j in range(7)] for i in range(7)]
        forms = anchored
        iterations = []
        for step in range(8):
            counts = list(map(len, forms))
            deficient = [j for j, n in enumerate(counts) if n < Q]
            if deficient:
                status = 'REJECTED_RESTRICTED_CAPACITY'
                break
            tight = [j for j, n in enumerate(counts) if n == Q]
            dim = len(basis)
            matrix = [[sum(c[k] for c in forms[j]) % Q for k in range(dim)] for j in tight]
            rref, pivots, newbasis = kernel(matrix, dim)
            record = {'iteration': step, 'dimension_before': dim, 'counts_before': counts,
                      'exact_17_phases': tight, 'sum_matrix_current_coordinates': matrix,
                      'rref': rref, 'pivot_columns': pivots, 'rank': len(pivots),
                      'kernel_basis_in_current_coordinates': newbasis}
            if not pivots:
                record['status'] = 'STABLE_NO_NEW_LINEAR_CONSTRAINT'
                iterations.append(record)
                status = 'SURVIVES_STABLE_TIGHT_LINEAR_CLOSURE'
                break
            oldbasis = basis
            basis = compose(newbasis, oldbasis)
            forms = project(forms, newbasis)
            assert forms == project(anchored, basis)
            record.update(dimension_after=len(basis), basis_in_original_anchored_coordinates=basis,
                          counts_after=list(map(len, forms)))
            iterations.append(record)
        else:
            raise AssertionError('A strict dimension drop cannot occur more than7 times')
        counts = list(map(len, forms))
        deficient = [j for j, n in enumerate(counts) if n < Q]
        result = {**row, 'anchor_component': anchor, 'iterations': iterations,
                  'status': status, 'final_dimension': len(basis),
                  'basis_in_original_anchored_coordinates': basis,
                  'final_form_counts': counts, 'deficient_phases': deficient,
                  'projective_inputs_after_closure': (Q ** len(basis) - 1) // (Q - 1)}
        if deficient:
            witness = min(deficient, key=lambda j: counts[j])
            result['witness_phase'] = witness
            result['witness_restricted_forms'] = sorted(forms[witness])
        else:
            result['restricted_forms_by_phase'] = [sorted(cell) for cell in forms]
            survivors.append(result)
        results.append(result)

        # One independent group-word calibration of the final basis restoration.
        if calibration is None:
            z = list(range(1, len(basis) + 1))
            x = [sum(z[k] * basis[k][j] for k in range(len(basis))) % Q for j in range(7)]
            x.insert(anchor, 0)
            generators = []
            for field, phase in zip(x[:4], row['pair_phases']):
                generators += [(field, phase), (-scalar[-phase % M] * field % Q, -phase % M)]
            generators += [(field, 24) for field in x[4:]]
            actual = [set() for _ in range(M)]
            actual[0].add(0)
            level = {(0, 0)}
            for depth in range(3):
                nxt = set()
                for field, phase in level:
                    for y, j in generators:
                        value = (field + scalar[phase] * y) % Q
                        target = (phase + j) % M
                        actual[target].add(value)
                        nxt.add((value, target))
                level = nxt
            predicted = [{sum(v * w for v, w in zip(c, z)) % Q for c in cell} for cell in forms]
            assert actual == predicted
            calibration = {'source_cursor': row['cursor'], 'pair_phases': row['pair_phases'],
                           'final_dimension': len(basis), 'z': z, 'restored_fields': x,
                           'actual_generators': generators,
                           'actual_12_elements_legal': len(set(generators)) == 12 and (0, 0) not in generators,
                           'all48_actual_word_value_sets_equal_restored_symbolic_sets': True,
                           'actual_sets': [sorted(v) for v in actual],
                           'symbolic_sets': [sorted(v) for v in predicted],
                           'graph_constructed': False, 'BFS_runs': 0,
                           'scope': 'one arithmetic calibration, not a search or additional family'}
    (HERE / 'patterns.json').write_text(json.dumps(results, indent=2) + '\n')
    (HERE / 'survivors.json').write_text(json.dumps(survivors, indent=2) + '\n')
    (HERE / 'restoration_calibration.json').write_text(json.dumps(calibration, indent=2) + '\n')
    summary = {
        'status': 'COMPLETE_ITERATED_TIGHT_LINEAR_CAPACITY',
        'group': 'F17 semidirect_3 C48', 'degree': 12,
        'input_patterns': 12, 'patterns_completed': 12,
        'original_projective_inputs': 307754004,
        'rejected_patterns': 12 - len(survivors), 'surviving_patterns': len(survivors),
        'remaining_projective_inputs': sum(r['projective_inputs_after_closure'] for r in survivors),
        'per_pattern': [{k: r[k] for k in ['cursor', 'pair_phases', 'status', 'final_dimension', 'deficient_phases', 'projective_inputs_after_closure']} for r in results],
        'CPU_seconds': time.process_time() - start, 'worker_count': 1,
        'actual_search_assignments': 0, 'arithmetic_calibration_assignments': 1,
        'graphs_generated': 0, 'BFS_runs': 0,
    }
    (HERE / 'linear.terminal.json').write_text(json.dumps(summary, indent=2) + '\n')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
