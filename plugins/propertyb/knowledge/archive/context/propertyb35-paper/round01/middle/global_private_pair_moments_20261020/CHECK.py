#!/usr/bin/env python3
"""Exact scalar/Johnson-kernel check; no hypergraph generation or LP dependency."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json
import time

ROOT = Path(__file__).resolve().parent

def C(n, r):
    return comb(n, r) if 0 <= r <= n else 0

def ceil(x):
    return -(-x.numerator // x.denominator)

def kernels(n, k=5):
    # B_t(E,F)=C(|E intersect F|,t); recursively extract Johnson projections.
    out = []
    for ell in range(k + 1):
        beta = C(n - 2 * ell, k - ell)
        row = []
        for s in range(k + 1):
            lower = sum(F(C(k-j, ell-j) * C(n-ell-j, k-ell)) * out[j][s]
                        for j in range(ell))
            row.append((F(C(s, ell)) - lower) / beta)
        out.append(row)
    return out

def convolution_counts(n, s, u, v, k=5):
    # Fixed E,F with intersection s; count Z with |Z intersect E|=u, |Z intersect F|=v.
    return sum(C(s, a) * C(k-s, u-a) * C(k-s, v-a) *
               C(n-2*k+s, k-u-v+a) for a in range(k+1))

def check_projectors(n, rows, k=5):
    entries = 0
    for s in range(k+1):
        counts = [[convolution_counts(n, s, u, v, k) for v in range(k+1)]
                  for u in range(k+1)]
        assert sum(map(sum, counts)) == C(n, k)
        for row in rows:
            square = sum(counts[u][v] * row[u] * row[v]
                         for u in range(k+1) for v in range(k+1))
            assert square == row[s], (n, s, row, square)
            entries += 1
    # Symmetric idempotent matrices are PSD. Their sum is the identity matrix.
    for s in range(k+1):
        assert sum(row[s] for row in rows) == int(s == k)
    return entries

def check_distribution(n, hist, rows, W=648, minimum_n1=397):
    assert len(hist) == 5 and all(x >= 0 for x in hist)
    assert sum(hist) == C(35, 2)
    assert sum(j * hist[j] for j in range(5)) == W
    T = sum(C(j, 2) * hist[j] for j in range(5))
    base = 350 - C(n, 2)
    assert T >= base
    assert hist[1] >= minimum_n1
    psd = [35 * row[5] + 2 * sum(hist[s] * row[s] for s in range(5))
           for row in rows]
    assert all(x >= 0 for x in psd)
    tau = T-base
    assert hist[1] == W - 2*T + 3*hist[3] + 8*hist[4]
    return {'histogram_n0_to_n4': hist, 'W': W, 'T': T, 'tau': tau,
            'weighted_high_intersection': 3*hist[3]+8*hist[4]-2*tau,
            'six_PSD_quadratic_forms': psd}

def rationalize(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {k: rationalize(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [rationalize(v) for v in value]
    return value

def main():
    started = time.process_time()
    tables = []
    all_rows = {}
    exact_entries = 0
    for n in range(21, 26):
        a = n // 2
        den = C(n, a)
        p = F(C(n-5, a-5) + C(n-5, a), den)
        assert p == F(C(a, 5)+C(n-a, 5), C(n, 5))
        q = F(C(n-9, a-5)+C(n-9, a-4), den)
        bound = 5*(2-35*p)/(2*q)
        rows = kernels(n)
        exact_entries += check_projectors(n, rows)
        all_rows[n] = rows
        tables.append({'n': n, 'a': a, 'p': p, 'q': q,
                       'lower_Pr_unique': 2-35*p,
                       'real_lower_n1': bound, 'integer_lower_n1': ceil(bound),
                       'paircover_T_baseline': 350-C(n,2),
                       'necessary_high_term': f'>={ceil(bound)+2*(350-C(n,2))}-W'})
    assert [r['integer_lower_n1'] for r in tables] == [397,397,366,366,338]
    assert 15+21+9*28+10*36 == 648
    integer_witness = check_distribution(21, list(map(F, [78,397,110,9,1])), all_rows[21])
    optimum_witness = check_distribution(21, [F(17),F(1664,3),F(0),F(0),F(70,3)], all_rows[21])
    # Exact LP optimality: W-(2/3)T=n1+(4/3)n2+n3 >= n1, T>=140.
    assert optimum_witness['histogram_n0_to_n4'][1] == F(648)-F(2,3)*140
    out = {'status': 'PASS', 'scope': 'scalar necessary conditions; not hypergraph realizability',
           'tables': tables, 'PSD_kernel_idempotence_entries_checked': exact_entries,
           'PSD_kernel_values_by_n': all_rows,
           'A1_integer_feasible_distribution': integer_witness,
           'A1_relaxation_max_n1': F(1664,3),
           'A1_optimum_rational_distribution': optimum_witness,
           'CPU_seconds': time.process_time()-started}
    (ROOT/'CHECK.json').write_text(json.dumps(rationalize(out), indent=2)+'\n')
    print('PASS: five threshold rows; 180 exact idempotence entries; A1 integer PSD witness')
    print('A1 n1 >=397; PSD relaxation feasible, exact max n1 =1664/3')
    print(f'CPU {out["CPU_seconds"]:.6f}s')

if __name__ == '__main__':
    main()
