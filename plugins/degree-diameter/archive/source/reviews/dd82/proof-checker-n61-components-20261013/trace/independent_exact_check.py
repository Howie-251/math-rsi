"""One independent finite algebra check; never modifies the proof inputs."""
import json
from itertools import permutations, product
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[4]
x = s.symbols("x")


def cycle_charpoly(n):
    # Build the actual cycle matrix; do not use the submitted recurrence.
    matrix = s.zeros(n)
    for i in range(n):
        matrix[i, (i + 1) % n] = 1
        matrix[(i + 1) % n, i] = 1
    return matrix.charpoly(x).as_poly()


def ascending(poly):
    return [int(c) for c in reversed(poly.all_coeffs())]


resonance_input = json.loads(
    (ROOT / "computations/dd82/n61/component_6_25_30_resonance.result.json").read_text()
)
chi30 = cycle_charpoly(30)
shifted = s.Poly(chi30.as_expr().subs(x, -1 - x), x)
assert ascending(chi30) == resonance_input["chi_30_ascending"]
assert ascending(shifted) == resonance_input["shifted_chi_30_ascending"]
gcd_records = []
for record in resonance_input["records"]:
    p = record["p"]
    cp = cycle_charpoly(p)
    divisor = s.gcd(cp, shifted).monic()
    assert ascending(cp) == record["chi_p_ascending"]
    assert ascending(divisor) == record["monic_gcd_ascending"]
    assert ascending(cp.exquo(divisor)) == record["chi_p_over_gcd_ascending"]
    assert ascending(shifted.exquo(divisor)) == record["shifted_chi_30_over_gcd_ascending"]
    gcd_records.append({"p": p, "factorization": str(s.factor(divisor.as_expr()))})
assert [record["p"] for record in gcd_records] == [5, 10, 15, 20, 25]

# Enumerate diagonals of trace seven first, then each row's off-diagonal
# split. This is a bijection with all row-eight, trace-seven matrices.
counts = dict(all_labeled_matrices=45 ** 3, trace_seven=0,
              positive_component_identity=0, balance=0,
              size_and_handshake=0)
survivors = set()
for a, b, c in product(range(8), repeat=3):
    if a + b + c != 7:
        continue
    for u, v, w in product(range(9 - a), range(9 - b), range(9 - c)):
        q = ((a, u, 8 - a - u), (v, b, 8 - b - v), (w, 8 - c - w, c))
        counts["trace_seven"] += 1
        m = [[sum(q[i][k] * q[k][j] for k in range(3)) + q[i][j]
              - (11 if i == j else 0) for j in range(3)] for i in range(3)]
        if any(len({m[i][j] for i in range(3)}) != 1 for j in range(3)):
            continue
        n = tuple(m[2])
        if any(z < 2 for z in n) or sum(n) != 61:
            continue
        counts["positive_component_identity"] += 1
        if any(n[i] * q[i][j] != n[j] * q[j][i]
               for i in range(3) for j in range(i)):
            continue
        counts["balance"] += 1
        if any(q[i][i] > n[i] - 1 or n[i] * q[i][i] % 2 for i in range(3)):
            continue
        counts["size_and_handshake"] += 1
        survivors.add((n, q))
quotient_input = json.loads(
    (ROOT / "computations/dd82/n61/component_quotient_three.result.json").read_text()
)
saved = {(tuple(r["component_sizes"]), tuple(tuple(row) for row in r["quotient"]))
         for r in quotient_input["all_labeled_survivors"]}
assert len(saved) == len(quotient_input["all_labeled_survivors"])
assert survivors == saved
assert counts == quotient_input["counts"]
bases = [((12, 21, 28), ((1, 0, 7), (0, 4, 4), (3, 3, 2))),
         ((6, 25, 30), ((3, 0, 5), (0, 2, 6), (1, 5, 2)))]
orbits = set()
for n, q in bases:
    for perm in permutations(range(3)):
        orbits.add((tuple(n[i] for i in perm),
                    tuple(tuple(q[i][j] for j in perm) for i in perm)))
assert survivors == orbits and len(orbits) == 12
result = {
    "scope": "Single independent finite algebra check of the two submitted tables",
    "cycle_method": "Exact characteristic polynomials of explicit adjacency matrices",
    "quotient_method": "Trace-seven diagonal enumeration and off-diagonal row splits",
    "counts": counts,
    "survivors_match_saved_and_two_permutation_orbits": True,
    "gcd_records": gcd_records,
    "all_saved_polynomial_coefficients_and_cofactors_match": True,
    "solver_calls": 0,
    "graph_searches": 0,
}
out = Path(__file__).with_name("independent_exact_check.result.json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
