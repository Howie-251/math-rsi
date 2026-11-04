"""Finite audits for Z16/Z17/Z18; not exhaustive matching/path proofs."""
from pathlib import Path
import itertools
import json


def edge(x, y):
    return tuple(sorted((x, y)))


def cov(m):
    return {x for e in m for x in e}


def is_matching(m):
    return len(cov(m)) == 2 * len(m)


def partner(m, x):
    return next(b if a == x else a for a, b in m if x in (a, b))


def prescribed(holes, forced):
    """All additional edges internal to coordinate-0 faces."""
    occupied = set(holes) | cov(forced)
    odd_to_even = {}

    def aug(x, seen):
        for j in range(1, 6):
            y = x ^ (1 << j)
            if y in occupied or y in seen:
                continue
            seen.add(y)
            if y not in odd_to_even or aug(odd_to_even[y], seen):
                odd_to_even[y] = x
                return True
        return False

    for x in range(64):
        if x not in occupied and x.bit_count() % 2 == 0:
            assert aug(x, set()), (holes, forced, x)
    m = set(forced) | {edge(x, y) for y, x in odd_to_even.items()}
    assert is_matching(m)
    assert cov(m) == set(range(64)) - set(holes)
    assert all((x ^ y).bit_count() == 1 for x, y in m)
    return m


def half_layers(face_bit):
    hs = []
    for j in range(1, 6):
        mask = 63 ^ 1 ^ (1 << j)
        for p in (0, 1):
            hs.append({edge(x, x ^ (1 << j)) for x in range(64)
                       if (x & 1) == face_bit and not (x >> j) & 1
                       and (x & mask).bit_count() % 2 == p})
    return hs


def partition(m, v):
    a = {x for x in range(64) if (x & 1) == (v & 1)}
    b = set(range(64)) - a
    ma = {e for e in m if set(e) <= a}
    mb = {e for e in m if set(e) <= b}
    c = m - ma - mb
    return a, b, ma, mb, c, cov(c) & a, cov(c) & b


def fixture_z17(name, z, w, t, v, h, forced):
    holes = {0, z, w, t}
    assert len(holes) == 4 and v not in holes
    assert (v & 1) != (z & 1) == (w & 1) == (t & 1)
    assert (z ^ w).bit_count() != 1 and (z ^ t).bit_count() != 1
    m = prescribed(holes, forced | {edge(v, h)})
    star = m - {edge(v, h)} | {edge(0, h)}
    a, bface, ma, mb, c, xa, xb = partition(star, v)
    assert len(c) == 1
    candidates = {w ^ 1, t ^ 1}
    usable = candidates & cov(ma)
    assert usable
    anchor = next(iter(xa))
    compressions = {}
    for b in sorted(usable):
        k = partner(ma, b)
        compressed = ma - {edge(b, k)} | {edge(anchor, k)}
        assert is_matching(compressed)
        assert cov(compressed) == a - {v, b}
        compressions[b] = compressed
    if name == 'u_h_in_A_candidates_exactly_u_h':
        assert candidates == {0, h}
        assert compressions[0] & compressions[h] == ma - {edge(0, h)}
    if name == 'u_A_h_B_allowed_boundary':
        assert 0 in candidates and 0 not in cov(ma)
        assert len(usable) == 1
        assert len(partition(m, v)[4]) == 1
    if name == 'u_B_h_A_zero_original_crossings':
        assert not partition(m, v)[4]
    if name == 'u_h_in_B_two_original_crossings':
        assert len(partition(m, v)[4]) == 2
        assert anchor.bit_count() % 2 == 0
    return {'case': name, 'holes': sorted(holes), 'v': v, 'h': h,
            'M': sorted(m), 'M_star_crossings': sorted(c),
            'candidates': sorted(candidates), 'usable_candidates': sorted(usable)}


def check_z16():
    u, z, w, t, v, h = 0, 6, 13, 49, 2, 10
    m = prescribed({u, z, w, t}, {edge(v, h), edge(4, 5), edge(8, 9)})
    star = m - {edge(v, h)} | {edge(u, h)}
    a, bface, ma, mb, c, xa, xb = partition(star, v)
    assert len(c) == 2 and not any(q <= ma for q in half_layers(v & 1))
    b = w ^ 1
    k = partner(ma, b)
    f = ma - {edge(b, k)}
    y = z ^ 1
    r = partner(mb, y)
    rows = []
    for anchor in (z, min(xa)):
        residual = sorted((xa | {z, k}) - {anchor, k})
        d = {edge(residual[0], residual[1])}
        comp = f | d | {edge(anchor, k)}
        assert not any(q <= comp for q in half_layers(v & 1))
        la = ma | d
        assert is_matching(la) and cov(la) == a - {v, anchor}
        for s in (w, min(xb)):
            other = sorted((xb | {w, y}) - {y, s})
            transfer = {edge(y, s), edge(other[0], other[1])}
            assert cov(mb) & cov(transfer) == {y}
            lb = mb - {edge(y, r)} | transfer - {edge(y, s)} | {edge(r, s)}
            assert is_matching(lb) and cov(lb) == bface - {y, t}
            assert (lb - {edge(r, s)} | {edge(r, y), edge(y, s)}) == mb | transfer
            rows.append({'anchor': anchor, 'anchor_is_z': anchor == z,
                         's': s, 's_is_w': s == w, 'holes_LB': [y, t]})
    return {'holes': [u, z, w, t], 'v': v, 'h': h, 'M': sorted(m),
            'bookkeeping_cases': rows,
            'scope': 'actual no-half-layer compressions checked; abstract R not claimed to be realized by a particular A-side path'}


def boundary_z18():
    cases = 0
    second_coordinates = 0
    for i in range(6):
        w = 1 << i
        for z in range(1, 64):
            if z.bit_count() % 2 or not (z >> i) & 1:
                continue
            if (z ^ w).bit_count() == 1:
                continue
            for t in range(64):
                if t == w or not t.bit_count() % 2 or not (t >> i) & 1:
                    continue
                if (z ^ t).bit_count() == 1:
                    continue
                for v in range(64):
                    if not v.bit_count() % 2 or (v >> i) & 1:
                        continue
                    h = v ^ (1 << i)
                    if h == z:
                        continue
                    js = [j for j in range(6) if j != i and ((v ^ z) >> j) & 1]
                    assert js
                    cases += 1
                    for j in js:
                        z14 = ((w ^ t) >> j) & 1
                        z15 = ((v >> j) & 1) == ((w >> j) & 1) == ((t >> j) & 1)
                        if not z14 and not z15:
                            assert ((z >> j) & 1) == ((w >> j) & 1) == ((t >> j) & 1) == 0
                            assert (v >> j) & 1
                        second_coordinates += 1
    return {'normalized_boundary_geometries': cases,
            'all_possible_second_coordinate_checks': second_coordinates,
            'scope': 'geometry only; not assertion every geometry realizes a one-crossing matching'}


def main():
    fixtures = [
        fixture_z17('u_h_in_A_candidates_exactly_u_h', 57, 1, 7, 2, 6, {edge(8, 9)}),
        fixture_z17('u_A_h_B_allowed_boundary', 29, 1, 49, 2, 3, set()),
        fixture_z17('u_A_h_B_both_candidates_internal', 3, 13, 49, 4, 5, set()),
        fixture_z17('u_B_h_A_zero_original_crossings', 10, 4, 56, 7, 3, set()),
        fixture_z17('u_h_in_B_two_original_crossings', 10, 4, 56, 7, 6, {edge(3, 2)}),
    ]
    result = {'status': 'PASS', 'Z16': check_z16(), 'Z17_fixtures': fixtures,
              'Z18': boundary_z18(),
              'scope': 'finite structural checks only; universal theorems rely on the written proofs'}
    Path(__file__).with_name('FINAL_FOUR_HOLE_ALGEBRA_CHECKS.json').write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'PASS', 'Z16_cases': len(result['Z16']['bookkeeping_cases']),
                      'Z17_actual_matching_fixtures': len(fixtures), 'Z18': result['Z18']}))


if __name__ == '__main__':
    main()
