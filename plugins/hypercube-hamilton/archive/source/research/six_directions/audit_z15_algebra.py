"""Z15 finite bookkeeping checks; no Hamilton-cycle existence is inferred."""
from pathlib import Path
import itertools
import json
import random


def parity(x):
    return x.bit_count() & 1


def edge(a, b):
    return tuple(sorted((a, b)))


def covered(m):
    return {x for e in m for x in e}


def matching(m):
    return len(covered(m)) == 2 * len(m)


def short_matching(holes, forced):
    used = set(holes) | covered(forced)
    odd_to_even = {}

    def augment(x, seen):
        for i in range(6):
            y = x ^ (1 << i)
            if y in used or y in seen:
                continue
            seen.add(y)
            if y not in odd_to_even or augment(odd_to_even[y], seen):
                odd_to_even[y] = x
                return True
        return False

    for x in range(64):
        if x not in used and not parity(x):
            assert augment(x, set())
    m = set(forced) | {edge(x, y) for y, x in odd_to_even.items()}
    assert matching(m)
    assert covered(m) == set(range(64)) - set(holes)
    assert all((x ^ y).bit_count() == 1 for x, y in m)
    return m


def pairs(xs):
    return {edge(xs[i], xs[i + 1]) for i in range(0, len(xs), 2)}


def check_fixture(u, z, w, t, v, h, expected):
    i = 0
    holes = {u, z, w, t}
    assert len(holes) == 4 and v not in holes
    assert parity(u) == parity(z) == 0
    assert parity(w) == parity(t) == parity(v) == 1
    assert (v & 1) == (w & 1) == (t & 1) != (z & 1)
    assert (z ^ w).bit_count() != 1 and (z ^ t).bit_count() != 1
    m = short_matching(holes, {edge(v, h)})
    star = (m - {edge(v, h)}) | {edge(h, u)}
    a = {x for x in range(64) if (x & 1) == (v & 1)}
    bface = set(range(64)) - a
    ma = {e for e in star if set(e) <= a}
    mb = {e for e in star if set(e) <= bface}
    c = star - ma - mb
    xa, xb = covered(c) & a, covered(c) & bface
    candidates = {w ^ 1, t ^ 1}
    usable = candidates & covered(mb)
    assert usable
    b = u if expected == 'br_is_hu' else min(usable)
    assert b in usable
    r = next(y if x == b else x for x, y in mb if b in (x, y))
    selected_t = b ^ 1
    other_w = next(x for x in (w, t) if x != selected_t)
    assert len(xa) % 2 == 1
    assert len(xa) >= 1
    assert matching(star)
    assert covered(star) == set(range(64)) - {v, z, w, t}
    rng = random.Random(1500 + v)
    checks = 0
    for _ in range(20):
        dverts = sorted(xa | {selected_t})
        rng.shuffle(dverts)
        d = pairs(dverts)
        la = ma | d
        assert matching(la)
        assert covered(la) == a - {v, other_w}
        # R stands only for an arbitrary endpoint pairing. This does not assert
        # it is realized by a short-edge extension of this particular L_A.
        rverts = sorted(xb | {b})
        rng.shuffle(rverts)
        transfer = pairs(rverts)
        s = next(y if x == b else x for x, y in transfer if b in (x, y))
        assert covered(mb) & covered(transfer) == {b}
        assert len({b, r, z, s}) == 4
        lb = (mb - {edge(b, r)}) | (transfer - {edge(b, s)}) | {edge(r, s)}
        assert matching(lb)
        assert covered(lb) == bface - {z, b}
        assert parity(z) == parity(b)
        assert edge(r, s) not in (mb - {edge(b, r)})
        assert edge(r, s) not in (transfer - {edge(b, s)})
        # Abstract expansion r--b--[the transfer segment]--s introduces b once
        # and restores the removed original B-side matching edge.
        restored = (lb - {edge(r, s)}) | {edge(r, b), edge(b, s)}
        assert restored == mb | transfer
        if expected == 'br_is_hu':
            assert edge(b, r) == edge(h, u)
        if expected == 'hu_crosses':
            assert edge(h, u) in c
        if expected == 'hu_inside_A':
            assert edge(h, u) in ma
        checks += 1
    return {'case': expected, 'holes': sorted(holes), 'v': v, 'h': h,
            'M': sorted(m), 'ports': len(xa), 'selected_b': b, 'r': r,
            'pairing_bookkeeping_checks': checks}


def main():
    fixtures = [
        check_fixture(0, 6, 25, 1, 11, 10, 'br_is_hu'),
        check_fixture(0, 6, 25, 1, 7, 3, 'hu_crosses'),
        check_fixture(0, 9, 28, 2, 4, 6, 'hu_inside_A'),
    ]
    truth_checks = 0
    for v, z, w, t in itertools.product((0, 1), repeat=4):
        z14 = v != z and w != t
        z15 = v == w == t and v != z
        residual = v != z and w == t == z
        assert (v != z) == (z14 or z15 or residual)
        assert sum((z14, z15, residual)) <= 1
        truth_checks += 1
    out = {'status': 'PASS', 'scope': 'Three actual Q6 short-matching fixtures; '
           '60 abstract D/R pairing bookkeeping checks; no Hamilton-path search '
           'and no claim every abstract R is realized by an A-side cycle.',
           'fixtures': fixtures, 'coordinate_truth_table_cases': truth_checks}
    Path(__file__).with_name('Z15_ALGEBRA_CHECKS.json').write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': out['status'], 'cases': [f['case'] for f in fixtures],
                      'pairing_checks': sum(f['pairing_bookkeeping_checks'] for f in fixtures),
                      'coordinate_truth_table_cases': truth_checks}))


if __name__ == '__main__':
    main()
