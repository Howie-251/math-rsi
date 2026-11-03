#!/usr/bin/env python3
"""Only linear diagnostics on saved tight fibers; no path/mask/graph enumeration."""
from pathlib import Path
from collections import Counter, defaultdict
from math import gcd
import json
import time

HERE = Path(__file__).resolve().parent
MOD, N = 32, 13


def valuation(x):
    x %= MOD
    return 5 if not x else (x & -x).bit_length() - 1


def matmul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) % MOD for col in zip(*b)] for row in a]


def linear_system(original, rhs):
    """Invertible row/column operations over Z/32, never divide a nonunit."""
    m = len(original)
    a = [[x % MOD for x in row] for row in original]
    b = [x % MOD for x in rhs]
    r = [[int(i == j) for j in range(m)] for i in range(m)]
    c = [[int(i == j) for j in range(N)] for i in range(N)]
    k = 0
    while k < min(m, N):
        candidates = [(valuation(a[i][j]), i, j) for i in range(k, m) for j in range(k, N) if a[i][j]]
        if not candidates:
            break
        v, ri, cj = min(candidates)
        a[k], a[ri] = a[ri], a[k]
        r[k], r[ri] = r[ri], r[k]
        b[k], b[ri] = b[ri], b[k]
        for matrix in (a, c):
            for row in matrix:
                row[k], row[cj] = row[cj], row[k]
        d = 1 << v
        unit = pow(a[k][k] // d, -1, MOD)
        a[k] = [x * unit % MOD for x in a[k]]
        r[k] = [x * unit % MOD for x in r[k]]
        b[k] = b[k] * unit % MOD
        assert a[k][k] == d
        for i in range(k + 1, m):
            assert a[i][k] % d == 0
            q = a[i][k] // d
            a[i] = [(x-q*y) % MOD for x, y in zip(a[i], a[k])]
            r[i] = [(x-q*y) % MOD for x, y in zip(r[i], r[k])]
            b[i] = (b[i]-q*b[k]) % MOD
        for j in range(k + 1, N):
            assert a[k][j] % d == 0
            q = a[k][j] // d
            for matrix in (a, c):
                for row in matrix:
                    row[j] = (row[j]-q*row[k]) % MOD
        k += 1
    assert matmul(matmul(r, original), c) == a
    assert [sum(x*y for x, y in zip(row, rhs)) % MOD for row in r] == b
    assert all(a[i][j] == (a[i][i] if i == j and i < k else 0) for i in range(m) for j in range(N))
    bad = next((i for i in range(m) if (b[i] % a[i][i] if i < k else b[i]) != 0), None)
    result = {'consistent': bad is None, 'nonzero_diagonal_count': k,
              'diagonal': [a[i][i] for i in range(k)], 'transformed_rhs': b,
              'row_transform': r, 'column_transform': c}
    if bad is not None:
        multiplier = MOD // a[bad][bad] if bad < k else 1
        witness = [multiplier*x % MOD for x in r[bad]]
        lhs = [sum(witness[i]*original[i][j] for i in range(m)) % MOD for j in range(N)]
        value = sum(x*y for x, y in zip(witness, rhs)) % MOD
        assert lhs == [0]*N and value != 0
        result.update(inconsistent_row=bad, left_kernel_witness=witness,
                      witness_coefficient_sum=lhs, witness_rhs=value)
    else:
        # Exact projection of the linear solution set to coordinate parities.
        y = [b[i] // a[i][i] % 2 if i < k else 0 for i in range(N)]
        parity = [sum(x*t for x, t in zip(row, y)) % 2 for row in c]
        directions = [[c[i][j] % 2 for i in range(N)] for j in range(k, N)]
        result.update(solution_count=MOD**(N-k) * __import__('math').prod(a[i][i] for i in range(k)),
                      parity_particular=parity, parity_basis=directions)
    return result


def main():
    start = time.process_time()
    assert not (HERE / 'TIGHT_RING_DIAGNOSTICS.json').exists(), 'No automatic duplicate run'
    output = {}
    for group in ['d64', 'q64']:
        source = json.loads((HERE/group/'results.json').read_text())
        assert source['status'] == 'COMPLETE'
        bymask = defaultdict(list)
        fiber_types = Counter()
        self_reflection_pairs_checked = 0
        for line in (HERE/group/'forms_tight.jsonl').open():
            row = json.loads(line)
            forms = row['forms']
            assert len(forms) == 32
            assert len({(tuple(x % MOD for x in f['coefficients']), f['constant'] % MOD) for f in forms}) == 32
            assert all(f['constant'] in ([0] if group == 'd64' else [0, 16]) for f in forms)
            coefficients = [sum(f['coefficients'][j] for f in forms) % MOD for j in range(N)]
            constant = sum(f['constant'] for f in forms) % MOD
            b = (16-constant) % MOD
            g = gcd(MOD, *coefficients)
            equation = {k: row[k] for k in ['root', 'target', 'target_phase']}
            equation.update(coefficients_mod32=coefficients, constant_sum_mod32=constant,
                            rhs_mod32=b, coefficient_gcd_with32=g, single_row_consistent=(b % g == 0))
            bymask[row['phase_mask']].append(equation)
            fiber_types[(row['root'] == row['target'], row['target_phase'])] += 1
            if row['root'] == row['target']:
                assert row['target_phase'] == 1, 'Self-rotation coefficient sets are odd-sized'
                formset = {(tuple(x % MOD for x in f['coefficients']), f['constant']) for f in forms}
                if group == 'q64':
                    assert all((c, (d+16) % MOD) in formset for c, d in formset)
                    assert constant == 0 and all(x % 2 == 0 for x in coefficients)
                    self_reflection_pairs_checked += 1
                else:
                    assert all(d == 0 for c, d in formset)
        results = []
        for mask, equations in sorted(bymask.items()):
            assert time.process_time()-start < 28
            a = [e['coefficients_mod32'] for e in equations]
            b = [e['rhs_mod32'] for e in equations]
            result = linear_system(a, b)
            item = {'phase_mask': mask, 'tight_fibers': equations, **result}
            if result['consistent']:
                particular, basis = result['parity_particular'], result['parity_basis']
                p = [(mask >> i) & 1 for i in range(N)]
                # Only a <=1-dimensional parity coset could lie in {0,p}.
                if len(basis) <= 1:
                    parities = [particular] + ([[x ^ y for x, y in zip(particular, basis[0])]] if basis else [])
                    item['forces_disconnected_mod2_quotient'] = all(v in [[0]*N, p] for v in parities)
                else:
                    item['forces_disconnected_mod2_quotient'] = False
            results.append(item)
        (HERE/f'{group}_tight_linear_systems.json').write_text(json.dumps(results, indent=2)+'\n')
        bad = [r for r in results if not r['consistent']]
        parity_bad = [r for r in results if r['consistent'] and r['forces_disconnected_mod2_quotient']]
        summary = {'capacity_surviving_phase_masks': source['capacity_pass_count'],
                   'saved_tight_fibers_read': sum(map(len, bymask.values())),
                   'masks_with_tight_fibers': len(results),
                   'masks_without_tight_fibers_not_processed': source['capacity_pass_count']-len(results),
                   'single_row_inconsistent_masks': [r['phase_mask'] for r in results if any(not e['single_row_consistent'] for e in r['tight_fibers'])],
                   'joint_linear_inconsistent_masks': [r['phase_mask'] for r in bad],
                   'additional_mod2_connectivity_rejected_masks': [r['phase_mask'] for r in parity_bad],
                   'capacity_masks_remaining_after_these_necessary_filters': source['capacity_pass_count']-len(bad)-len(parity_bad),
                   'tight_fiber_types': [{'same_base_vertex': k[0], 'target_phase': k[1], 'count': v} for k, v in sorted(fiber_types.items())],
                   'q64_selfreflection_reversal_pair_fibers_checked': self_reflection_pairs_checked,
                   'diagonal_type_histogram': {','.join(map(str,k)): v for k,v in Counter(tuple(r['diagonal']) for r in results).items()},
                   'example': results[0] if results else None,
                   'first_joint_inconsistency': bad[0] if bad else None}
        output[group] = summary
    output.update(status='COMPLETE_SAVED_TIGHT_LINEAR_DIAGNOSTICS', CPU_seconds=time.process_time()-start,
                  CPU_budget_seconds=30, worker_count=1,
                  phase_patterns_reenumerated=0, actual_rotation_assignments=0, graphs_generated=0, BFS_roots=0)
    (HERE/'TIGHT_RING_DIAGNOSTICS.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({g:{k:v for k,v in output[g].items() if k not in ['example','first_joint_inconsistency']} for g in ['d64','q64']},indent=2))
    print('CPU_seconds',output['CPU_seconds'])


if __name__ == '__main__':
    main()
