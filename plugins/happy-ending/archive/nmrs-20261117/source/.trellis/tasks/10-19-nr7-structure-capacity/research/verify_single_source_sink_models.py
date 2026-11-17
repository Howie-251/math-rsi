#!/usr/bin/env python3
"""Exact finite geometric checks; run on the authoritative Linux server.

Usage: python3 -B verify_single_source_sink_models.py --output FILE.json
No solver, floating point, external package, or external review is used.
All monochromatic subsets are enumerated; independent consecutive-triple
checks test the path-closure convention on every subset in each fixture.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
import hashlib
import json
import math
from pathlib import Path
import platform
import socket
import sys


def determinant(a, b, c):
    return ((b[0] - a[0]) * (c[1] - b[1])
            - (b[1] - a[1]) * (c[0] - b[0]))


def check(name, points, named):
    n = len(points)
    vertices = tuple(range(n))
    assert all(points[i][0] < points[i + 1][0] for i in range(n - 1))
    denominator = math.lcm(*(v.denominator for p in points for v in p))
    integer_points = [tuple(int(v * denominator) for v in p) for p in points]
    det = {t: determinant(*(integer_points[i] for i in t))
           for t in combinations(vertices, 3)}
    colors = {t: 'R' if d > 0 else 'B' if d < 0 else '0' for t, d in det.items()}

    def mono(seq, color='R'):
        return all(colors[t] == color for t in combinations(seq, 3))

    families = {c: {k: [] for k in range(1, n + 1)} for c in 'RB'}
    closure_failures = []
    for k in range(1, n + 1):
        for seq in combinations(vertices, k):
            for c in 'RB':
                full = mono(seq, c)
                if full:
                    families[c][k].append(seq)
                local = all(colors[seq[j:j + 3]] == c for j in range(k - 2))
                if full != local:
                    closure_failures.append({'path': seq, 'color': c})
    packet_failures = []
    for q in combinations(vertices, 4):
        word = ''.join(colors[t] for t in combinations(q, 3))
        switches = sum(a != b for a, b in zip(word, word[1:]))
        if switches > 1 or '0' in word:
            packet_failures.append({'vertices': q, 'word': word})

    endpoint_rows = []
    for endpoints in combinations(vertices, 2):
        row = {'endpoints': endpoints}
        for c in 'RB':
            candidates = [p for group in families[c].values() for p in group
                          if len(p) >= 2 and (p[0], p[-1]) == endpoints]
            best = max(candidates, key=len)
            row[c] = {'length': len(best), 'witness': best}
        row['sum'] = row['R']['length'] + row['B']['length']
        endpoint_rows.append(row)

    r6 = families['R'].get(6, [])
    masks = [sum(1 << v for v in p) for p in r6]

    @lru_cache(None)
    def packing(available):
        best = ()
        for i, mask in enumerate(masks):
            if mask & available == mask:
                trial = (i,) + packing(available ^ mask)
                if len(trial) > len(best):
                    best = trial
        return best

    optimum = packing((1 << n) - 1)
    hit_by_size = []
    minimum_hits = []
    for k in range(n + 1):
        hits = [s for s in combinations(vertices, k)
                if all(any(v in s for v in p) for p in r6)]
        hit_by_size.append({'size': k, 'tested': math.comb(n, k), 'hits': len(hits)})
        if hits:
            minimum_hits = hits
            break
    paths = {key: {'vertices': seq, 'red': mono(seq), 'blue': mono(seq, 'B'),
                   'nonred_triples': [t for t in combinations(seq, 3) if colors[t] != 'R']}
             for key, seq in named.items()}
    pools = {}
    for key in ('T', 'S'):
        if key not in named:
            continue
        seq = named[key]
        pools['A_' + key] = [v for v in vertices if v < seq[0] and mono((v,) + seq)]
        pools['B_' + key] = [v for v in vertices if v > seq[-1] and mono(seq + (v,))]
    extensions = {key: [v for v in vertices if v not in named[key]
                        and mono(tuple(sorted(named[key] + (v,))))]
                  for key in ('F', 'G') if key in named}
    P, Q = named['P'], named['Q']
    core = set(vertices) - {0, n - 1}
    disjoint_pairs = [(a, b) for i, a in enumerate(r6) for b in r6[i + 1:]
                      if set(a).isdisjoint(b)]
    prescribed = ((0, 1, 2, 7, 8, 9), (3, 4, 5, 10, 11, 12)) if n == 13 else None
    result = {
        'name': name, 'n': n,
        'coordinates': [[str(x), str(y)] for x, y in points],
        'all_x_strictly_increasing': True,
        'coordinate_scale': denominator,
        'collinear_triples': [t for t, d in det.items() if d == 0],
        'minimum_absolute_scaled_determinant': min(abs(d) for d in det.values()),
        'packet_count': math.comb(n, 4), 'packet_failures': packet_failures,
        'path_closure_subsets_tested_per_color': (1 << n) - 1,
        'path_closure_failures': closure_failures,
        'monochromatic_counts': {c: {str(k): len(ps) for k, ps in by_k.items()}
                                 for c, by_k in families.items()},
        'longest': {c: max(k for k, ps in families[c].items() if ps) for c in 'RB'},
        'R7': families['R'].get(7, []), 'B6': families['B'].get(6, []),
        'weak7_definition': 'R and B share both first and last vertex; lengths sum >= 9',
        'weak7_violations': [row for row in endpoint_rows if row['sum'] >= 9],
        'maximum_same_endpoint_sum': max(row['sum'] for row in endpoint_rows),
        'same_endpoint_maxima': endpoint_rows,
        'R6': r6, 'nu_R6': len(optimum), 'packing_witness': [r6[i] for i in optimum],
        'tau_R6': len(minimum_hits[0]), 'all_minimum_R6_transversals': minimum_hits,
        'transversal_exhaustion': hit_by_size,
        'disjoint_R6_pairs_count': len(disjoint_pairs),
        'first_disjoint_R6_pair': disjoint_pairs[0] if disjoint_pairs else None,
        'prescribed_disjoint_pair': ({'paths': prescribed,
                                     'both_red': all(mono(p) for p in prescribed),
                                     'disjoint': set(prescribed[0]).isdisjoint(prescribed[1])}
                                    if prescribed else None),
        'named_paths': paths, 'actual_endpoint_pools': pools,
        'all_single_point_R6_extensions': extensions,
        'P_Q_intersection': sorted(set(P) & set(Q)),
        'P_Q_intersection_positions_one_based': [
            {'vertex': v, 'P': P.index(v) + 1, 'Q': Q.index(v) + 1}
            for v in sorted(set(P) & set(Q))],
        'R6_in_core_deleting_extreme_vertices': [p for p in r6 if set(p) <= core],
    }
    result['checks'] = {
        'general_position': not result['collinear_triples'],
        'ordered_packets': not packet_failures,
        'no_R7': not result['R7'], 'no_B6': not result['B6'],
        'no_weak7': not result['weak7_violations'],
        'nu_R6_equals_1': len(optimum) == 1,
        'P_and_Q_red': paths['P']['red'] and paths['Q']['red'],
    }
    return result


def fixtures():
    left = [(F(x), F(y)) for x, y in [('0', '0'), ('.75', '-4.14'),
            ('.85', '-4.50'), ('1', '-6'), ('2', '-20'), ('3', '-19'), ('4', '-16')]]
    symmetric = left + [(8 - x, y) for x, y in reversed(left[:-1])]
    e = F(1, 100)
    original = [(F(i), F(y)) for i, y in enumerate((0, 0, -2, -2, 2, 3, 5, 17, 23))]
    inserted = sorted(original + [(1 - e, F('1.5') * e),
        (1 - e - e * e, F('1.5') * e - F('.7') * e * e),
        (7 + e, 17 + 9 * e), (7 + e + e * e, 17 + 9 * e + F('4.9') * e * e)])
    frame = {'F': (0, 1, 2, 3, 5), 'G': (7, 9, 10, 11, 12),
             'T': (1, 2, 7, 9), 'S': (3, 5, 10, 11),
             'P': (0, 3, 6, 7, 8, 9), 'Q': (3, 4, 5, 6, 9, 12)}
    nine = [(F(i), F(y)) for i, y in enumerate((0, 0, -2, -2, 2, 3, 5, 17, 25))]
    yield 'symmetric_13', symmetric, frame
    yield 'epsilon_inserted_13', inserted, frame
    yield 'original_9', nine, {'P': (0, 1, 4, 5, 6, 7), 'Q': (1, 2, 3, 4, 7, 8)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    assert platform.system() == 'Linux', 'Research execution is Linux only'
    results = [check(*fixture) for fixture in fixtures()]
    payload = {
        'scope': 'Exact finite geometric fixtures only; no global theorem or independent review',
        'execution': {'hostname': socket.gethostname(), 'platform': platform.platform(),
                      'python': sys.executable, 'version': platform.python_version(),
                      'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
        'models': results,
        'fixed_frame_search': {
            'performed': False,
            'reason': 'Caller supplied an analytic fixed-frame disjoint-path obstruction; '
                      'the same specified disjoint pair is checked explicitly for both candidates. '
                      'No ordered-packet search or general impossibility certificate is claimed.'},
    }
    args.output.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
    print(json.dumps([{'model': r['name'], 'checks': r['checks'],
                       'nu_R6': r['nu_R6'], 'tau_R6': r['tau_R6'],
                       'actual_endpoint_pools': r['actual_endpoint_pools'],
                       'P_Q_intersection': r['P_Q_intersection']} for r in results], indent=2))


if __name__ == '__main__':
    main()
