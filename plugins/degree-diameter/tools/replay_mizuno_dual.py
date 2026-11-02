#!/usr/bin/env python3
"""Replay the saved Mizuno13 affine-full27-block dual; standard library, read-only.

Reconstructs missing LP_INPUT rows from the present original MODEL.json.
It checks the integer combination, not the geometry proving rows necessary.
"""
import argparse
import json
import time
from collections import Counter
from fractions import Fraction
from pathlib import Path


def replay(source):
    start = time.process_time()
    model_path = source / ('research/ddp/two_successful_methods_20261101/'
        'mizuno13_clone_interface/source_dependent_geometry/controller213_capacity_gate/MODEL.json')
    certificate_path = model_path.parent / 'lp_exact_bound/SIMPLIFIED_DUAL_CERTIFICATE.json'
    model = json.loads(model_path.read_text())
    certificate = json.loads(certificate_path.read_text())
    n = model['binary_variables']
    assert n == model['controller_rows'] == 364
    rows = [[0] * n for _ in range(n)]
    for i, sparse in enumerate(model['row_sparse_coefficients']):
        for j, value in sparse:
            rows[i][j] += value
    assert len(model['row_sparse_coefficients']) == n
    assert all(sum(row) == 5 for row in rows)
    assert all(sum(row[j] for row in rows) == 5 for j in range(n))
    assert all(sorted(v for v in row if v) == [1, 1, 1, 2] for row in rows)
    assert Counter(model['source_cost']) == {5: 203, 6: 161}
    rows.append(model['source_cost'])
    rhs_rows = [3] * n + [model['cost_upper']]
    assert rhs_rows[-1] == 1092
    denominator = certificate['common_denominator']
    y = certificate['controller_and_cost_row_numerators']
    z = certificate['upper_bound_row_numerators']
    assert denominator > 0 and len(rows) == len(rhs_rows) == len(y) == 365
    assert len(z) == n and all(isinstance(v, int) and v >= 0 for v in y + z)
    columns = [sum(row[j] * multiplier for row, multiplier in zip(rows, y)) + z[j]
               for j in range(n)]
    rhs = sum(b * multiplier for b, multiplier in zip(rhs_rows, y)) + sum(z)
    assert columns == certificate['column_coefficient_numerators']
    assert min(columns) >= denominator
    assert rhs == certificate['RHS_numerator'] and rhs < 207 * denominator
    bound = Fraction(rhs, denominator)
    assert bound == Fraction(certificate['exact_upper_bound'])
    return {'status': 'PASS_EXACT_DUAL_ARITHMETIC', 'columns': n,
        'minimum_coefficient': min(columns), 'denominator': denominator,
        'RHS': rhs, 'bound': str(bound), 'integer_blocks_at_most': 206,
        'scope': 'Declared necessary controller/cost relaxation for all 364-source selections, one complete affine W-transverse 27-point block per selected original fiber; geometric row necessity imported from original proof',
        'missing_original_input_reconstructed': 'LP_INPUT.json',
        'source_writes': 0, 'solver_calls': 0, 'graph_generation': 0,
        'Lean_runs': 0, 'CPU_seconds': time.process_time() - start}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path,
        default=Path(__file__).resolve().parents[1] / 'archive/source',
        help='Copied handoff root; defaults to the archive beside this tool.')
    args = parser.parse_args()
    print(json.dumps(replay(args.source.resolve()), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
