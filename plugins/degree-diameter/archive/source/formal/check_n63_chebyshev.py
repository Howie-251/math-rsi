"""Exact finite identities for the proposed n63 algebraic route; not a Lean proof."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
rows = json.loads((root / 'computations/dd82/construction/n63_cyclotomic_norms.json').read_text())['rows']
cs = {row['order']: row['real_cyclotomic_coefficients'] for row in rows}

def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def add(a, b, scale=1):
    out = a[:] + [0] * max(0, len(b) - len(a))
    for i, c in enumerate(b):
        out[i] += scale * c
    return trim(out)

def mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)

def comp(a, b):
    out = [0]
    for c in reversed(a):
        out = add(mul(out, b), [c])
    return out

rs = [[2], [0, 1]]
for r in range(2, 64):
    rs.append(add([0] + rs[-1], rs[-2], -1))
for r in range(1, 64):
    right = cs[1]
    if r % 2 == 0:
        right = mul(right, cs[2])
    for ell in range(3, r+1):
        if r % ell == 0:
            right = mul(right, mul(cs[ell], cs[ell]))
    assert add(rs[r], [-2]) == right, ('Chebyshev factorization', r)
for ell in range(1, 64):
    c = cs[ell]
    d = len(c)-1
    f = comp(c, [-7, 1, 1])
    assert len(f)-1 == 2*d and f[-1] == 1 and f[-2] == d, ('degree/nextCoeff', ell)
assert comp(cs[3], [-7, 1, 1]) == mul([-2, 1], [3, 1])
print('PASS: all 63 Chebyshev factorizations, all 63 composition degree/nextCoeff identities, and the ell=3 factorization.')
print('Scope: exact integer polynomial arithmetic only; no original-graph n63 exclusion is certified here.')
