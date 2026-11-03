"""Arithmetic and symmetry check only; no generating-set or graph search."""
import json
from collections import Counter
from math import gcd
from pathlib import Path
from time import process_time

start = process_time()
polynomial = (1 << 6) | (1 << 1) | 1


def poly_remainder(a, b):
    while a and a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length() - b.bit_length())
    return a


def multiply(a, b):
    product = 0
    while b:
        if b & 1:
            product ^= a
        b >>= 1
        a <<= 1
        if a & 64:
            a ^= polynomial
    return product


def power(a, n):
    result = 1
    while n:
        if n & 1:
            result = multiply(result, a)
        a = multiply(a, a)
        n >>= 1
    return result


# Every reducible polynomial of degree 6 has a factor of degree at most 3.
factor_remainders = {}
for degree in range(1, 4):
    for low in range(1 << degree):
        factor = (1 << degree) | low
        remainder = poly_remainder(polynomial, factor)
        assert remainder != 0
        factor_remainders[factor] = remainder

primitive = 2
primitive_powers = [power(primitive, j) for j in range(63)]
assert len(set(primitive_powers)) == 63 and power(primitive, 63) == 1
logs = {x: j for j, x in enumerate(primitive_powers)}
r = power(primitive, 3)
rpowers = [power(r, j) for j in range(42)]
assert len(set(rpowers)) == 21 and power(r, 21) == 1
assert power(r, 23) == power(r, 2)
assert gcd(23, 42) == 1


def inverse(g):
    x, i = g
    return multiply(rpowers[(-i) % 42], x), (-i) % 42


involutions = set()
pair_classes = Counter()
for x in range(64):
    for i in range(42):
        g = x, i
        if g == (0, 0):
            continue
        gi = inverse(g)
        assert inverse(gi) == g
        if gi == g:
            involutions.add(g)
        elif g < gi:
            pair_classes["zero" if x == 0 else str(logs[x] % 3)] += 1

assert involutions == ({(x, 0) for x in range(1, 64)} | {(x, 21) for x in range(64)})
assert pair_classes == {"0": 420, "1": 420, "2": 420, "zero": 20}
generated_units = {sign * pow(23, j, 42) % 42 for sign in (-1, 1) for j in range(6)}
assert generated_units == {x for x in range(42) if gcd(x, 42) == 1}
reps = [1, 2, 3, 6, 7, 14]
quotient_orbits = {rep: sorted({rep * u % 42 for u in generated_units}) for rep in reps}
assert sum(map(len, quotient_orbits.values())) == 40
assert set().union(*map(set, quotient_orbits.values())) == set(range(42)) - {0, 21}
assert all(gcd(x, 42) == rep for rep, orbit in quotient_orbits.items() for x in orbit)
assert {23 * (7 * j) % 42 for j in range(6)} == {7 * j for j in range(6)}

result = {
    "status": "SCOPE_ARITHMETIC_COMPLETE_NO_GRAPH_SEARCH",
    "field_polynomial": "t^6+t+1",
    "polynomial_binary": polynomial,
    "degree_at_most3_factor_remainders": factor_remainders,
    "primitive_t_encoding": primitive,
    "primitive_t_order": 63,
    "r_encoding": r,
    "r_order": 21,
    "group_quotient_order": 42,
    "group_order": 64 * 42,
    "vertices": {"leaf": 64 * 42, "block": 64 * 7, "head": 64, "total": 64 * 50},
    "involution_count": len(involutions),
    "noninvolution_pairs_by_multiplicative_class": dict(sorted(pair_classes.items())),
    "frobenius_quotient_multiplier": 23,
    "generated_units_mod42": sorted(generated_units),
    "first_quotient_representative_orbits": quotient_orbits,
    "three_pair_normalized_inputs": 6 * 420 * 420,
    "one_pair_other_layer_upper_bound": 280,
    "zero_pair_other_layer_upper_bound": 78,
    "target_layer_size": 64 * 6,
    "two_pairs_two_involutions": "NOT_COVERED_BY_THIS_SCOPE",
    "cpu_seconds": process_time() - start,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
