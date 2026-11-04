"""Independent finite sanity checks for the recut proof review.

No Hamilton-path search and no enumeration of all Q6 matchings is claimed.
Run with the standard Python library only.
"""
import itertools
import json
from pathlib import Path


def parity(x):
    return x.bit_count() & 1


def short(x, y):
    return (x ^ y).bit_count() == 1


def edge(x, y):
    return tuple(sorted((x, y)))


def half_layer(n, face, face_bit, direction, excluded):
    """The unique half-layer of this direction avoiding excluded."""
    mask = ((1 << n) - 1) ^ (1 << face) ^ (1 << direction)
    desired = 1 - parity(excluded & mask)
    return {
        edge(x, x ^ (1 << direction))
        for x in range(1 << n)
        if ((x >> face) & 1) == face_bit
        and not ((x >> direction) & 1)
        and parity(x & mask) == desired
    }


def vertices(edges):
    return {x for e in edges for x in e}


def pairings4(ys):
    a, b, c, d = ys
    return [((a, b), (c, d)), ((a, c), (b, d)), ((a, d), (b, c))]


def swap(x, a, b):
    if ((x >> a) ^ (x >> b)) & 1:
        return x ^ (1 << a) ^ (1 << b)
    return x


def main():
    result = {"scope": "finite algebra only; not all matching inputs or Hamilton paths"}
    counts = {}
    # Translation is a cube automorphism, so v=0 checks all coordinate patterns.
    for n in range(4, 9):
        count = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                h = half_layer(n, i, 0, j, 0)
                u = {x for x in vertices(h) if not (x >> j) & 1}
                expected = {x for x in range(1 << n)
                            if not (x >> i) & 1 and not (x >> j) & 1
                            and parity(x)}
                assert u == expected
                for k in range(n):
                    if k == j:
                        continue
                    kh = half_layer(n, j, 0, k, 0)
                    assert u & vertices(kh), (n, i, j, k)
                    count += 1
        counts[str(n)] = count
    result["E2_intersection_checks_v_normalized_to_zero"] = counts
    h3 = half_layer(3, 0, 0, 1, 0)
    k3 = half_layer(3, 1, 0, 2, 0)
    assert not vertices(h3) & vertices(k3)
    result["E2_excluded_n3_counterexample"] = {"H": sorted(h3), "K": sorted(k3)}

    # All 4-element subsets of Q5, each of the five forbidden short directions.
    # This is the minimum Y-size in N12, not an exhaustive check for arbitrary F.
    ycount = 0
    forbidden_checks = 0
    for ys in itertools.combinations(range(32), 4):
        ps = pairings4(ys)
        assert any(sum(short(a, b) for a, b in p) <= 1 for p in ps)
        for j in range(5):
            assert any(all((a ^ b) != (1 << j) for a, b in p) for p in ps)
            forbidden_checks += 1
        ycount += 1
    result["N12_all_Q5_four_sets"] = ycount
    result["N12_forbidden_direction_checks"] = forbidden_checks

    # Exact excluded Y=2 boundary example, v=0 and b=1, full Q5 direction 0.
    h = {edge(x, x ^ 1) for x in range(32) if not (x & 1) and parity(x >> 1)}
    ys = {2, 3}
    t = sorted(set(range(32)) - vertices(h) - {0, 1})
    # Pair the complementary vertices arbitrarily: this cannot create H.
    f = (h - {edge(2, 3)}) | {edge(a, b) for a, b in zip(t[::2], t[1::2])}
    all_halves = []
    for j in range(5):
        mask = 31 ^ (1 << j)
        for p in range(2):
            all_halves.append({edge(x, x ^ (1 << j)) for x in range(32)
                               if not (x >> j) & 1 and parity(x & mask) == p})
    assert vertices(f) == set(range(32)) - {0, 1} - ys
    assert len(vertices(f)) == 2 * len(f)
    assert not any(q <= f for q in all_halves)
    assert h <= f | {edge(2, 3)}
    result["N12_excluded_Y2_counterexample"] = {
        "v": 0, "b": 1, "Y": sorted(ys), "F": sorted(f)}

    # The fixed coordinate deductions in Z10 and Z12.
    assert [j for j in range(1, 6) if ((0 >> j) & 1) == ((12 >> j) & 1)
            == ((48 >> j) & 1)] == [1]
    candidate_data = {}
    holes = {0, 60, 13, 14}
    for i in (2, 3):
        c, d, e = (x ^ (1 << i) for x in (60, 13, 14))
        js = [j for j in range(6) if j != i and ((d >> j) & 1)
              == ((e >> j) & 1) != ((c >> j) & 1)]
        assert js == [4, 5]
        assert (c ^ d).bit_count() == (c ^ e).bit_count() == 3
        assert not {c, d, e} & holes
        candidate_data[str(i)] = {"c": c, "d": d, "e": e, "J": js}
    result["Z12_coordinates"] = candidate_data
    failure_cases = []
    for j2, j3 in itertools.product((4, 5), repeat=2):
        x = 1 << j2
        allowed = []
        for k in range(6):
            y = x ^ (1 << k)
            if y in holes:
                continue
            if not (x >> 2) & 1 and not (y >> 2) & 1 and k != j2:
                continue
            if not (x >> 3) & 1 and not (y >> 3) & 1 and k != j3:
                continue
            allowed.append(y)
        assert not allowed
        failure_cases.append({"j2": j2, "j3": j3, "x": x, "allowed": allowed})
    result["Z12_double_failure_witnesses"] = failure_cases

    # Z13: every coordinate pair and every normalized admissible four-hole set.
    geometries = 0
    nonadjacent = 0
    double_failures = 0
    for i, k in itertools.combinations(range(6), 2):
        both_one = [x for x in range(64) if (x >> i) & 1 and (x >> k) & 1]
        evens = [x for x in both_one if not parity(x)]
        odds = [x for x in both_one if parity(x)]
        for z in evens:
            for w, t in itertools.combinations(odds, 2):
                geometries += 1
                if short(z, w) or short(z, t):
                    continue
                nonadjacent += 1
                for s in (i, k):
                    c, d, e = (x ^ (1 << s) for x in (z, w, t))
                    assert c and d and e
                    js = [j for j in range(6) if j != s and ((d >> j) & 1)
                          == ((e >> j) & 1) != ((c >> j) & 1)]
                    assert not set(js) & {i, k}
                    e3js = [j for j in range(6) if j != s
                            and not (w >> j) & 1 and not (t >> j) & 1]
                    assert not set(e3js) & {i, k}
        for ji, jk in itertools.product([j for j in range(6) if j not in (i, k)], repeat=2):
            x = 1 << ji
            allowed = []
            for q in range(6):
                y = x ^ (1 << q)
                if y == 0:
                    continue
                if not (x >> i) & 1 and not (y >> i) & 1 and q != ji:
                    continue
                if not (x >> k) & 1 and not (y >> k) & 1 and q != jk:
                    continue
                allowed.append(y)
            assert not allowed
            double_failures += 1
    result["Z13_coordinate_pair_geometries"] = geometries
    result["Z13_nonadjacent_geometries"] = nonadjacent
    result["Z13_double_failure_direction_patterns"] = double_failures

    # Z14: geometry only, with root normalized to 0; no matching enumeration.
    z14_geometries = 0
    z14_target_checks = 0
    z14_distance_counts = {2: 0, 4: 0, 6: 0}
    odd_vertices = [x for x in range(64) if parity(x)]
    for z in range(1, 64):
        if parity(z):
            continue
        for w, t in itertools.combinations(odd_vertices, 2):
            d = (w ^ t).bit_count()
            exceptions = 0
            for v in odd_vertices:
                mask_condition = ((v ^ z) & (w ^ t)) != 0
                coordinate_condition = any(((v >> i) & 1) != ((z >> i) & 1)
                                           and ((w >> i) & 1) != ((t >> i) & 1)
                                           for i in range(6))
                assert mask_condition == coordinate_condition
                exceptions += not mask_condition
                z14_target_checks += 1
            assert exceptions == {2: 8, 4: 2, 6: 0}[d]
            z14_geometries += 1
            z14_distance_counts[d] += 1
    result["Z14_normalized_four_hole_geometries"] = z14_geometries
    result["Z14_target_checks"] = z14_target_checks
    result["Z14_geometry_counts_by_odd_hole_distance"] = z14_distance_counts

    f = {0, 3, 13, 49}
    automorphisms = {
        "root3_to_0": lambda x: swap(x ^ 3, 0, 1),
        "root49_to_13": lambda x: swap(swap(x, 2, 4), 3, 5),
    }
    for name, fn in automorphisms.items():
        assert {fn(x) for x in f} == f
        assert len({fn(x) for x in range(64)}) == 64
        assert all(parity(fn(x)) == parity(x) for x in range(64))
        assert all(short(fn(x), fn(x ^ (1 << j)))
                   for x in range(64) for j in range(6))
    assert automorphisms["root3_to_0"](3) == 0
    assert automorphisms["root49_to_13"](49) == 13
    assert {x ^ 13 for x in f} == holes
    result["automorphism_checks"] = {"maps": 2, "vertices_per_map": 64,
                                      "directed_edges_per_map": 384}
    result["status"] = "PASS"
    out = Path(__file__).with_name("RECUT_ALGEBRA_CHECKS.json")
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
