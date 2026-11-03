"""Individual-group-element and symmetry data; no generating-set search."""
import json
from collections import Counter
from math import comb
from pathlib import Path
from time import process_time

start = process_time()
polynomial = 67


def mul(x, y):
    result = 0
    while y:
        if y & 1:
            result ^= x
        y >>= 1
        x <<= 1
        if x & 64:
            x ^= polynomial
    return result


def power(x, n):
    result = 1
    while n:
        if n & 1:
            result = mul(result, x)
        x = mul(x, x)
        n >>= 1
    return result


r = 8
rpowers = [power(r, a) for a in range(21)]
A = set(rpowers)
assert len(A) == 21


def encode(g):
    x, a, e = g
    return x + 64 * (a + 21 * e)


def decode(code):
    x = code % 64
    quotient = code // 64
    return x, quotient % 21, quotient // 21


def inverse(g):
    x, a, e = g
    b = (-pow(8, e) * a) % 21
    return mul(rpowers[b], power(x, pow(8, e))), b, e


def frobenius(code):
    x, a, e = decode(code)
    return encode((mul(x, x), 2 * a % 21, e))


def horizontal_class(code):
    x = code % 64
    return "zero" if x == 0 else ("A21" if x in A else "BC42")


involutions = []
pair_counts = Counter()
for code in range(2688):
    g = decode(code)
    gi = inverse(g)
    assert inverse(gi) == g
    other = encode(gi)
    if code == 0:
        continue
    if other == code:
        involutions.append(code)
    elif code < other:
        pair_counts[horizontal_class(code)] += 1

assert len(involutions) == 87
assert pair_counts == {"A21": 420, "BC42": 861, "zero": 19}
assert Counter(horizontal_class(code) for code in involutions) == {"A21": 42, "BC42": 42, "zero": 3}
involution_set = set(involutions)
assert {frobenius(code) for code in involutions} == involution_set

seen = set()
orbits = []
for code in involutions:
    if code in seen:
        continue
    orbit = []
    current = code
    while current not in orbit:
        orbit.append(current)
        current = frobenius(current)
    assert current == code
    orbit.sort()
    seen.update(orbit)
    representative = orbit[0]
    assert len({horizontal_class(c) for c in orbit}) == 1
    orbits.append({
        "representative_code": representative,
        "representative_coordinates": decode(representative),
        "member_codes": orbit,
        "size": len(orbit),
        "horizontal_class": horizontal_class(representative),
        "semilinear_exponent": decode(representative)[2],
    })

assert len(orbits) == 21
assert Counter(o["semilinear_exponent"] for o in orbits) == {0: 13, 1: 8}
assert Counter(o["horizontal_class"] for o in orbits) == {"A21": 12, "BC42": 7, "zero": 2}
type_i = []
for first in [(1, 0, 0), (1, 0, 1)]:
    first_code = encode(first)
    assert frobenius(first_code) == first_code
    remaining = [o for o in orbits if first_code not in o["member_codes"]]
    assert len(remaining) == 20
    assert sum(o["size"] for o in remaining) == 86
    assert sum(o["horizontal_class"] == "BC42" for o in remaining) == 7
    type_i.append({
        "first_involution_code": first_code,
        "first_involution_coordinates": first,
        "second_representative_codes": [o["representative_code"] for o in remaining],
        "second_orbits": remaining,
        "orbit_count": len(remaining),
        "bc_orbit_count": 7,
        "non_bc_orbit_count": 13,
    })

type_ii_codes = [c for c in involutions if horizontal_class(c) != "A21"]
assert len(type_ii_codes) == 45
assert Counter(horizontal_class(c) for c in type_ii_codes) == {"BC42": 42, "zero": 3}
counts = {
    "type_i_valid": 2 * 20 * comb(1300, 2),
    "type_i_hh_pass": 2 * (7 * comb(1300, 2) + 13 * (comb(1300, 2) - comb(439, 2))),
    "type_ii_valid": 6 * 1299 * comb(45, 2),
    "type_ii_hh_pass": 6 * (987 * 1299 + 3 * 861),
}
assert counts == {"type_i_valid": 33774000, "type_i_hh_pass": 31274334, "type_ii_valid": 7716060, "type_ii_hh_pass": 7708176}
counts["total_valid"] = counts["type_i_valid"] + counts["type_ii_valid"]
counts["total_hh_pass"] = counts["type_i_hh_pass"] + counts["type_ii_hh_pass"]
result = {
    "status": "NORMALIZATION_LISTS_COMPLETE_NO_GENERATOR_SET_SEARCH",
    "field_polynomial_binary": polynomial,
    "r_encoding": r,
    "encoding": "x + 64*(a + 21*e)",
    "coordinate_order": ["x", "a_mod21", "e_mod2"],
    "frobenius": "(x,a,e) -> (x^2,2*a mod21,e)",
    "nonidentity_involution_codes": involutions,
    "inverse_pair_counts": dict(pair_counts),
    "all_involution_frobenius_orbits": orbits,
    "type_i": type_i,
    "type_ii": {
        "allowed_involution_codes": type_ii_codes,
        "allowed_involution_coordinates": [decode(c) for c in type_ii_codes],
        "count": len(type_ii_codes),
        "first_pair_representatives": [[1, a, e] for a in [1, 3, 7] for e in [0, 1]],
    },
    "counts_not_search_completion": counts,
    "cpu_seconds": process_time() - start,
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"path": str(path), "counts": counts, "cpu_seconds": result["cpu_seconds"], "type_i_reps": [v["second_representative_codes"] for v in type_i], "type_ii_count": len(type_ii_codes)}, indent=2))
