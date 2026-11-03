#!/usr/bin/env python3
"""Five exact cycle-resonance gcds for the actual (6,25,30) quotient.

No graph enumeration or numerical eigenvalues. Polynomial coefficients are
stored in ascending order; Euclidean division uses fractions.Fraction.
"""
from fractions import Fraction
from pathlib import Path
import json
import time


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0)
                 + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def divide(a, b):
    a, b = trim(map(Fraction, a)), trim(map(Fraction, b))
    assert b != [0]
    q = [Fraction(0)] * max(1, len(a)-len(b)+1)
    while a != [0] and len(a) >= len(b):
        k, c = len(a)-len(b), a[-1]/b[-1]
        q[k] += c
        for j, x in enumerate(b):
            a[k+j] -= c*x
        a = trim(a)
    return trim(q), a


def gcd(a, b):
    degrees = []
    while b != [0]:
        degrees.append([len(a)-1, len(b)-1])
        _, r = divide(a, b)
        a, b = b, r
    return [x/a[-1] for x in a], degrees


def compose_minus_one_minus_x(a):
    result = [0]
    for c in reversed(a):
        result = add(mul(result, [-1, -1]), [c])
    return result


def ints(a):
    a = list(map(Fraction, a))
    assert all(x.denominator == 1 for x in a)
    return [int(x) for x in a]


def main():
    cpu, wall = time.process_time(), time.perf_counter()
    lp = [[2], [0, 1]]
    for p in range(2, 31):
        lp.append(add([0]+lp[-1], [-x for x in lp[-2]]))
    chi = {p: add(lp[p], [-2]) for p in range(3, 31)}
    shifted = compose_minus_one_minus_x(chi[30])
    records = []
    for p in (5, 10, 15, 20, 25):
        g, degrees = gcd(chi[p], shifted)
        qa, ra = divide(chi[p], g)
        qb, rb = divide(shifted, g)
        assert ra == rb == [0]
        records.append({
            'p': p, 'q': 30,
            'chi_p_ascending': chi[p],
            'monic_gcd_ascending': ints(g),
            'chi_p_over_gcd_ascending': ints(qa),
            'shifted_chi_30_over_gcd_ascending': ints(qb),
            'euclidean_dividend_divisor_degrees': degrees,
        })
    result = {
        'scope': 'gcd_Q[x](chi_Cp(x), chi_C30(-1-x)), p=5,10,15,20,25',
        'arithmetic': 'exact integer recurrence and rational Euclidean division',
        'complete': True,
        'chi_30_ascending': chi[30],
        'shifted_chi_30_ascending': shifted,
        'records': records,
        'graph_searches': 0, 'solver_calls': 0,
        'cpu_seconds': time.process_time()-cpu,
        'wall_seconds': time.perf_counter()-wall,
    }
    out = Path(__file__).with_suffix('.result.json')
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'output': str(out), 'complete': True,
                      'gcds': [[r['p'], r['monic_gcd_ascending']] for r in records],
                      'cpu_seconds': result['cpu_seconds'],
                      'wall_seconds': result['wall_seconds']}, indent=2))


if __name__ == '__main__':
    main()
