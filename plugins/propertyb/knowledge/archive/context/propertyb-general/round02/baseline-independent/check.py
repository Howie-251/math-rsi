"""Independent exact checks of normalization and integer relaxation margins.

No imports from the submitted comparison and no floating point arithmetic.
Finite checks supplement, but do not prove, the all-k inequalities in REPORT.md.
"""
import json
from fractions import Fraction as Q
from math import comb, isqrt
from pathlib import Path


def choose(n, r):
    return comb(n, r) if n >= r >= 0 else 0


def finite_sum(k, v, m, gamma):
    r = k - 1
    d1, d2 = comb(v - 1, r), comb(v - k, r)
    return sum((min(Q(m*k*choose(h-1, r), v*d1),
                    Q(m*k*choose(v-h, r), v*d1),
                    Q(gamma*choose(h-1, r)*choose(v-h, r), v*d1*d2))
                for h in range(1, v+1)), Q(0))


checks = []
for k in range(2, 11):
    r, m, kap = k-1, 2**k, Q(2)
    for v in (2*k-1, 4*k+1, 9*k+2):
        for mode in ("interior", "p0"):
            if mode == "interior":
                p = Q(1, 3)
                q = kap*k/(1+p)**r
                integral = sum(((-1)**j*comb(r, j)*p**(2*j+1)/Q(2*j+1)
                                for j in range(r+1)), Q(0))
                continuous = kap*(1-p)**k+q*integral
            else:
                q, continuous = 2*kap*k, kap
            gamma = q*4**r
            s = Q(v-2*k+3, v)
            lower = s**(2*k-1)*continuous-2*s**(2*k-2)*min(kap*k, q)/v
            margin = finite_sum(k, v, m, gamma)-lower
            assert margin >= 0
            checks.append({"k": k, "v": v, "mode": mode,
                           "exact_margin": str(margin)})


def ceildiv(a, b):
    return (a+b-1)//b


integer_rows = []
for k in (256, 257, 384, 512, 1024):
    for label, m in (("bottom", 2**k), ("split", 3*k*2**(k-1)),
                     ("large", 10*k*2**(k-1)), ("very_large", 2**(2*k))):
        v = isqrt((k-2)**2*m)
        n = v-1
        t, d = m//k**16, m-m//k**16
        cf, cc = (k-1)*d//n, ceildiv((k-1)*d, n)
        bf, bc = k*t//n, ceildiv(k*t, n)
        lam = d*(d-1)-cc*(cc-1)
        assert t >= 1 and cc < d < m
        assert cf*cf >= m and bc*bc*4 <= m
        assert v*v*4 >= k*k*m and cc*cc <= 4*m
        assert cf+bf >= ceildiv(v-1, k-1)
        assert d >= ceildiv(v-1, k-1)
        assert (k-2)*cf+(k-1)*bf >= v-2
        # An upper row capacity valid even when its smallest caps are used.
        assert (k-2)*cc+(k-1)*bc <= (v-2)*cf
        assert ceildiv(v*ceildiv(v-1, k-1), k) <= m
        assert lam*2 >= m*m
        assert m*(m-1)-lam <= 2*m*t+4*m
        assert ((k-1)*(k-2)*d+k*(k-1)*t) % 2 == 0
        integer_rows.append({"k": k, "M_regime": label, "status": "PASS"})

assert 2**128 > 300*256**10
assert Q(96, 300)+Q(18, 256**6) < 1
receipt = {"status": "PASS", "arithmetic": "exact rational/integer only",
           "discrete_cases": len(checks), "integer_data_cases": len(integer_rows),
           "discrete": checks, "integer_data": integer_rows,
           "scope": "Finite independent implementation checks; universal proof is textual."}
Path(__file__).with_name("CHECKS.json").write_text(json.dumps(receipt, indent=2)+"\n")
print(json.dumps({key: receipt[key] for key in ("status", "arithmetic", "discrete_cases", "integer_data_cases")}))
