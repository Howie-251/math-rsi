"""Exact arithmetic certificate for the order-63 spectral obstruction.

Only Python standard-library integer arithmetic is used. Coefficients are
stored in increasing exponent order. This certifies the finite norm table,
not the graph-to-field argument in the accompanying paper proof.
"""

from math import comb, isqrt
from pathlib import Path
import json


def trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q, scale=1):
    out = p[:] + [0] * max(0, len(q) - len(p))
    for i, coefficient in enumerate(q):
        out[i] += scale * coefficient
    return trim(out)


def divide_monic(p, q):
    assert q[-1] == 1 and len(p) >= len(q)
    remainder = p[:]
    quotient = [0] * (len(p) - len(q) + 1)
    for shift in range(len(quotient) - 1, -1, -1):
        coefficient = remainder[shift + len(q) - 1]
        quotient[shift] = coefficient
        for i, qi in enumerate(q):
            remainder[shift + i] -= coefficient * qi
    assert not any(remainder), (p, q, remainder)
    return trim(quotient)


def norm_table(max_order=63):
    phi = {}
    # F_j(t+t^-1)=t^j+t^-j.
    f = [[2], [0, 1]]
    for j in range(2, max_order // 2 + 1):
        f.append(add([0] + f[-1], f[-2], -1))
    rows = []
    moduli = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    for ell in range(1, max_order + 1):
        p = [-1] + [0] * (ell - 1) + [1]
        for divisor in range(1, ell):
            if ell % divisor == 0:
                p = divide_monic(p, phi[divisor])
        phi[ell] = p
        if ell == 1:
            c = [-2, 1]
        elif ell == 2:
            c = [2, 1]
        else:
            assert (len(p) - 1) % 2 == 0 and p == p[::-1]
            d = (len(p) - 1) // 2
            c = [p[d]]
            for j in range(1, d + 1):
                c = add(c, f[j], p[d + j])
            # Check t^d C_ell(t+t^-1)=Phi_ell(t) exactly.
            lift = [0] * (2 * d + 1)
            for j, coefficient in enumerate(c):
                for k in range(j + 1):
                    lift[d + j - 2 * k] += coefficient * comb(j, k)
            assert lift == p
        d = len(c) - 1
        assert c[-1] == 1
        # (-4)^d C_ell(-29/4), with no rational or floating-point arithmetic.
        norm = sum(coefficient * 29**j * (-4)**(d - j)
                   for j, coefficient in enumerate(c))
        assert norm > 0
        lower = isqrt(norm)
        row = dict(order=ell, degree=d, real_cyclotomic_coefficients=c,
                   discriminant_norm=norm, sqrt_floor=lower)
        if ell == 3:
            assert c == [1, 1] and norm == 25
            row.update(exception=True, reason="mu=-1; quadratic roots 2 and -3")
        else:
            assert lower * lower < norm < (lower + 1) ** 2
            modulus = next(m for m in moduli
                           if norm % m not in {a * a % m for a in range(m)})
            residues = sorted({a * a % modulus for a in range(modulus)})
            row.update(exception=False, modulus=modulus,
                       norm_residue=norm % modulus, square_residues=residues)
        rows.append(row)
    return rows


def main():
    rows = norm_table()
    out = Path(__file__).with_suffix('.json')
    out.write_text(json.dumps({
        "scope": "All eigenvalue conductors of cycles of order at most 63; finite arithmetic only",
        "coefficient_order": "increasing exponent",
        "checked_rows": len(rows),
        "nonsquare_rows": sum(not r['exception'] for r in rows),
        "rows": rows,
    }, indent=2) + '\n')
    table = ['| conductor ell | degree | modulus | norm residue |',
             '|---:|---:|---:|---:|']
    for r in rows:
        table.append(f"| {r['order']} | {r['degree']} | "
                     + ('exception' if r['exception'] else str(r['modulus']))
                     + ' | ' + ('25 = 5²' if r['exception'] else str(r['norm_residue'])) + ' |')
    Path(__file__).with_suffix('.table.md').write_text('\n'.join(table) + '\n')
    print(json.dumps(dict(checked=63, nonsquare=62, exception=[3],
                          exact_polynomial_lifts=True, certificate=str(out))))


if __name__ == '__main__':
    main()
