"""Construct the nonadjacent A4 spanning factor by exact augmenting paths.

This implements the Hall reduction, not a Hamilton-cycle algorithm.
The executable probe covers hole geometries, not all matchings.
"""
import json
import random
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def edge(x, y):
    return tuple(sorted((x, y)))


def factor(matching, forbidden, prescribed=None):
    f = {edge(*e) for e in matching}
    covered = [x for e in f for x in e]
    assert len(f) == 14 and len(covered) == len(set(covered)) == 28
    holes = set(range(32)) - set(covered)
    assert forbidden in holes
    p = forbidden.bit_count() % 2
    majority = {x for x in holes if x.bit_count() % 2 == p}
    assert len(majority) == 3
    minority, = holes - majority
    assert all((minority ^ y).bit_count() != 1 for y in majority - {forbidden})
    left, right = [], []
    for x in range(32):
        if x == forbidden:
            continue
        clones = [(x, i) for i in range(2 if x in holes else 1)]
        (right if x.bit_count() % 2 else left).extend(clones)
    assert len(left) == len(right) == 17
    adj = {l: [r for r in right if (l[0] ^ r[0]).bit_count() == 1
               and edge(l[0], r[0]) not in f] for l in left}
    assigned = {}
    fixed_left = fixed_right = None
    if prescribed is not None:
        x, y = prescribed
        if x.bit_count() % 2:
            x, y = y, x
        fixed_left, fixed_right = (x, 0), (y, 0)
        assert fixed_left in adj and fixed_right in adj[fixed_left]
        assigned[fixed_right] = fixed_left

    def augment(l, seen):
        for r in adj[l]:
            if r in seen or r == fixed_right:
                continue
            seen.add(r)
            if r not in assigned or augment(assigned[r], seen):
                assigned[r] = l
                return True
        return False

    for l in left:
        if l != fixed_left:
            assert augment(l, set()), 'Hall certificate predicts success'
    h = {edge(l[0], r[0]) for r, l in assigned.items()}
    assert len(h) == 17 and not (h & f)
    j = f | h
    neighbors = {x: [] for x in range(32) if x != forbidden}
    for x, y in j:
        neighbors[x].append(y)
        neighbors[y].append(x)
    assert all(len(ns) == 2 for ns in neighbors.values())
    remaining = set(neighbors)
    cycles = []
    while remaining:
        start = min(remaining)
        c = [start]
        previous, current = None, start
        while True:
            nxt = next(y for y in neighbors[current] if y != previous)
            if nxt == start:
                break
            assert nxt not in c
            c.append(nxt)
            previous, current = current, nxt
        remaining.difference_update(c)
        cycles.append(c)
    return {'matching': sorted(f), 'forbidden': forbidden,
            'prescribed': prescribed, 'cycles': cycles}


def main():
    rng = random.Random(20261101)
    odd = [x for x in range(32) if x.bit_count() % 2]
    far = [x for x in odd if x.bit_count() != 1]
    cases = []
    for i, b in enumerate(far):
        for t in far[i + 1:]:
            for v in odd:
                if v in (b, t):
                    continue
                vertices = sorted(set(range(32)) - {0, b, t, v})
                rng.shuffle(vertices)
                f = {edge(vertices[k], vertices[k + 1]) for k in range(0, 28, 2)}
                allowed = [edge(x, y) for x in range(32) for y in range(x + 1, 32)
                           if v not in (x, y) and (x ^ y).bit_count() == 1
                           and edge(x, y) not in f]
                cases.append(factor(f, v, rng.choice(allowed)))
    hist = Counter(len(c['cycles']) for c in cases)
    report = {'scope': '770 arbitrary matchings, one per nonadjacent hole geometry; not exhaustive matchings',
              'count': len(cases), 'component_histogram': dict(sorted(hist.items())),
              'cases': cases, 'full_p6_proved': False}
    (ROOT / 'a4_factor_construction_results.json').write_text(
        json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: report[k] for k in ('scope', 'count', 'component_histogram')}))


if __name__ == '__main__':
    main()
