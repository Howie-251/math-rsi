"""Solver-free check of the forced-triangle EP0 geometry certificate.

Positive EP0 follows from the analytic N10/triangle lemma in the companion
document, rather than enumeration of Hamilton paths. Negative witnesses below
refute only completeness of this particular sufficient triangle rule.
"""
from pathlib import Path
from itertools import permutations
import json
import hashlib

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'eight_hole_covered_next_probe.json'


def parity(x):
    return x.bit_count() % 2


def check_matching(M, H):
    assert len(M) == 28
    ends = [x for e in M for x in e]
    assert len(set(ends)) == len(ends)
    assert set(ends) == set(range(64)) - H
    assert all((a ^ b).bit_count() == 1 for a, b in M)


def main():
    source = json.loads(SOURCE.read_text(encoding='utf-8-sig'))
    out = []
    for row in source['joint_results']:
        v, Z, W = row['target'], set(row['Z']), set(row['W'])
        H = {0} | Z | W
        assert parity(v) == 1 and v not in H
        assert all(parity(z) == 0 for z in Z)
        assert all(parity(w) == 1 for w in W)
        assert all((z ^ w).bit_count() != 1 for z in Z for w in W)
        cuts = [i for i in range(6)
                if sum(((z ^ v) >> i & 1) == 0 for z in Z) == 2
                and all(((w ^ v) >> i & 1) == 1 for w in W)]
        assert cuts == row['cuts']
        good = []
        for i in cuts:
            A = {x for x in range(64) if ((x ^ v) >> i & 1) == 0}
            ZA = Z & A
            S = {w ^ (1 << i) for w in W}
            if 0 not in A:
                continue
            for q in sorted(A - H - {v}):
                if parity(q) != 1 or q ^ (1 << i) in H:
                    continue
                N = {q ^ (1 << j) for j in range(6) if j != i}
                if N - S == ZA:
                    assert len(ZA) == 2 and len(N & S) == 3
                    assert not (S & ZA) and 0 not in ZA
                    good.append({'cut': i, 'q': q, 'mirror': q ^ (1 << i),
                                 'non_S_neighbors': sorted(ZA),
                                 'S_neighbors': sorted(N & S)})
        forbidden = {frozenset((g['q'], g['mirror'])) for g in good}
        V = set(range(64)) - H
        ev = {x for x in V if parity(x) == 0}
        adj = {a: [a ^ (1 << j) for j in range(6)
                   if a ^ (1 << j) in V
                   and frozenset((a, a ^ (1 << j))) not in forbidden]
               for a in ev}
        mate = {}

        def augment(a, seen):
            for b in adj[a]:
                if b in seen:
                    continue
                seen.add(b)
                if b not in mate or augment(mate[b], seen):
                    mate[b] = a
                    return True
            return False

        for a in sorted(ev):
            augment(a, set())
        proof = {}
        if len(mate) < len(ev):
            U = ev - set(mate.values())
            stack = list(U)
            while stack:
                a = stack.pop()
                for b in adj[a]:
                    if b in mate and mate[b] not in U:
                        U.add(mate[b])
                        stack.append(mate[b])
            N = {b for a in U for b in adj[a]}
            assert len(U) > len(N)
            proof = {'Hall_even_subset': sorted(U), 'Hall_neighbors': sorted(N),
                     'Hall_deficiency': len(U) - len(N)}
            # Check the especially short direct certificate as well.
            isolated = sorted(a for a in ev if not adj[a])
            assert isolated
            proof['isolated_even_vertices'] = isolated
        else:
            M = sorted([a, b] for b, a in mate.items())
            check_matching(M, H)
            assert all(frozenset(e) not in forbidden for e in M)
            proof['matching_avoiding_all_triangle_rule_edges'] = M
        images = set()
        for p in permutations(range(6)):
            def transform(x):
                return sum(((x >> j) & 1) << p[j] for j in range(6))
            if transform(v) == v:
                images.add((tuple(sorted(map(transform, Z))),
                            tuple(sorted(map(transform, W)))))
        out.append({'target': v, 'Z': sorted(Z), 'W': sorted(W),
                    'target_preserving_orbit_size': len(images),
                    'triangle_sufficient_crossing_edges': good,
                    'all_realizing_matchings_EP0_closed': len(mate) < len(ev),
                    **proof})
    assert len(out) == 7
    assert sum(r['target_preserving_orbit_size'] for r in out) == 50
    closed = [r for r in out if r['all_realizing_matchings_EP0_closed']]
    assert [(r['target'], r['Z']) for r in closed] == [
        (1, [3, 5, 9]), (7, [15, 23, 39])]
    assert sum(r['target_preserving_orbit_size'] for r in closed) == 11
    result = {'status': 'PASS', 'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'EP0_closed_orbits': 2, 'EP0_closed_normalized_geometries': 11,
              'EP0_remaining_orbits': 5, 'EP0_remaining_normalized_geometries': 39,
              'scope': 'EP0 only, relative to N10 and the analytic forced-triangle lemma; full eight-hole extension still depends on T15',
              'full_eight_hole_proved': False, 'full_p6_proved': False, 'orbits': out}
    (ROOT / 'eight_ep0_fast_route_check.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in result if k != 'orbits'}))


if __name__ == '__main__':
    main()
