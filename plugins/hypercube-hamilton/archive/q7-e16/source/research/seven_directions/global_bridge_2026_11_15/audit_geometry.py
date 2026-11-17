"""Independently recover the bounded marked-exception basis by coefficients."""
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
S = {0, 3}
WS = ({28, 44, 52, 56, 61}, {28, 44, 52, 61, 62})
N6 = 6


def frozen(name):
    raw = (HERE.parent / name).read_bytes()
    return json.loads(raw), sha256(raw).hexdigest()


def suitable_split(send, recv):
    # All arrays use physical (alpha, beta) color order.
    total = [sum(cell[color] for cell in send) for color in (0, 1)]
    if abs(total[0] - total[1]) not in (3, 4) or min(total) > 5:
        return False
    major = int(total[1] > total[0])
    for donors, receivers in zip(send, recv):
        gap = receivers[1-major] - receivers[major]
        if gap not in (1, 2) or donors[major] < gap:
            return False
        if gap == 2 and receivers[major] >= 2:
            return False
    return True


def scalar_alphabet():
    with_abs, after_outer, after_transpose = set(), set(), set()
    for a, b, c, d in product(range(4), range(7), range(6), range(3)):
        x, y = a+c, b+d
        if abs(x-y) < 3:
            continue
        row = (a, b, c, d)
        with_abs.add(row)
        low_face = ((3-a, 6-b), (a, b))
        high_face = ((5-c, 2-d), (c, d))
        if suitable_split(low_face, high_face) or suitable_split(high_face, low_face):
            continue
        after_outer.add(row)
        lower_slice = (low_face[0], high_face[0])
        upper_slice = (low_face[1], high_face[1])
        if suitable_split(lower_slice, upper_slice) or suitable_split(upper_slice, lower_slice):
            continue
        if sorted((x, y)) in ([0, 3], [5, 8]):
            continue
        after_transpose.add(row)
    assert tuple(map(len, (with_abs, after_outer, after_transpose))) == (212, 204, 166)
    old = {row for row in after_transpose if abs(row[0]+row[2]-row[1]-row[3]) <= 6}
    new = {row for row in old if sorted((row[0]+row[2], row[1]+row[3])) not in ([1, 4], [4, 7])}
    assert (len(old), len(new)) == (156, 140)
    old_json, old_hash = frozen("R7_E16_MU3_CENTRAL_LOWM_PREFLIGHT_COUNT.json")
    r41_json, r41_hash = frozen("R7_E16_MU3_CENTRAL_AFTER_R41_SCALAR_NOTE.json")
    assert old == {(a, b, group["c"], group["d"])
                   for group in old_json["allowed_a_b_gap"] for a, b, _ in group["rows"]}
    assert old-new == set(map(tuple, r41_json["removed_columns_abcd"]))
    return new, (old_hash, r41_hash)


def loads(vertices, dim=N6):
    return tuple(sum((v >> i) % 2 for v in vertices) for i in range(dim))


def is_valid_points(u, y):
    return all((v^w).bit_count() != 1 for v in u for w in y)


def count_completions(pool, choices):
    # Deficits from each permissible full loading and a split of the pool into
    # disjoint coordinate-0 fibers. Do not materialize the three-point sets.
    def make_counter(vertices):
        counts = [Counter(), Counter(), Counter(), Counter()]
        counts[0][(0,)*N6] = 1
        for point in vertices:
            bits = loads([point])
            for degree in (3, 2, 1):
                for exp, mult in counts[degree-1].items():
                    shifted = tuple(map(sum, zip(exp, bits)))
                    if all(x <= max_a for x, max_a in zip(shifted, maxima)):
                        counts[degree][shifted] += mult
        return counts

    maxima = tuple(max(values) for values in choices)
    counts_zero = make_counter(v for v in pool if not v % 2)
    counts_one = make_counter(v for v in pool if v % 2)
    return sum(m1*m2
               for p in choices[0]
               for ex1, m1 in counts_zero[3-p].items()
               for ex2, m2 in counts_one[p].items()
               if all(x+y in allowed for x, y, allowed in zip(ex1, ex2, choices)))


def recover_branch(w, scalar, fixed_axes=None, sorted_high=False):
    c, d = loads(w), loads(S)
    bits = [i for i, (ci, di) in enumerate(zip(c, d)) if ci == di]
    assert bits == list(fixed_axes)
    y_pool = [v for v in range(64) if v.bit_count() % 2 == 1 and v not in w
              and all(v & (1 << i) for i in fixed_axes)]
    even = [v for v in range(64) if v.bit_count() % 2 == 0 and v not in S]
    lookup = {(b, c1, d1): tuple(a for a in range(4) if (a, b, c1, d1) in scalar)
              for b, c1, d1 in product(range(7), range(6), range(3))}
    counts = {}
    for y in combinations(y_pool, 6):
        b = loads(y)
        if sorted_high and b[2:] != tuple(sorted(b[2:])):
            continue
        choices = tuple(lookup[key] for key in zip(b, c, d))
        if not all(choices):
            continue
        pool = [v for v in even if is_valid_points((v,), y)]
        counts[y] = count_completions(pool, choices)
    return counts


def proof_geometry(scalar, y, u):
    w = WS[0]
    assert len(u) == 3 and len(y) == 6
    assert tuple(sorted(set(u))) == u and tuple(sorted(set(y))) == y
    assert all(0 <= v < 64 and not v.bit_count() % 2 for v in u)
    assert all(0 <= v < 64 and v.bit_count() % 2 == 1 and v % 2 for v in y)
    assert not set(u) & S and not set(y) & w
    assert is_valid_points(u, y) and is_valid_points(S, w)
    a, b, c, d = map(loads, (u, y, w, S))
    assert b[2:] == tuple(sorted(b[2:]))
    assert all(row in scalar for row in zip(a, b, c, d))
    alpha = set(u) | {64+v for v in w}
    beta = set(y) | {64+v for v in S}
    gaps = [abs(x-y) for x, y in zip(loads(alpha, 7), loads(beta, 7))]
    assert min(gaps) == 3
    return alpha, beta


def check_transport():
    from itertools import permutations

    def permute(v, order):
        return (v & 3) + sum((v >> source & 1) << target for source, target in zip(range(2, 6), order))

    w = WS[0]
    assert w == {61, *(60 ^ (1 << axis) for axis in range(2, 6))}
    for order in permutations(range(2, 6)):
        assert {permute(v, order) for v in S} == S
        assert {permute(v, order) for v in w} == w
        assert {permute(v, order) for v in range(64) if v % 2} == {v for v in range(64) if v % 2}


def fixed_basis():
    scalar, scalar_hashes = scalar_alphabet()
    check_transport()
    first = recover_branch(WS[0], scalar, (0,), sorted_high=True)
    second = recover_branch(WS[1], scalar, (0, 1))
    assert len(second) == 10 and not any(second.values())
    assert sum(first.values()) == 2757
    by_b1 = Counter()
    for y, count in first.items():
        if count:
            by_b1[loads(y)[1]] += count
    assert by_b1 == Counter({3: 93, 4: 2332, 5: 332})
    return scalar, scalar_hashes, first, second, by_b1


if __name__ == "__main__":
    _, hashes, first, second, groups = fixed_basis()
    print(json.dumps({
        "scalar_input_sha256": hashes,
        "sorted_W1_sources": len(first),
        "sorted_W1_positive_sources": sum(n > 0 for n in first.values()),
        "sorted_W1_completions": sum(first.values()),
        "sorted_W1_completions_by_b1": groups,
        "W2_sources": len(second),
        "W2_completions": sum(second.values())
    }, indent=2))
