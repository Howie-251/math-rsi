"""Exact fixed-witness enumeration; run only on the authoritative Linux host.

Usage: python3.12 -B check_rational10.py > rational10-result.json
No solver, repository imports, floating-point geometry, or external packages.
"""
from fractions import Fraction as F
from itertools import combinations
import hashlib
import json
import platform
import socket
import sys
from datetime import datetime, timezone


COORDS = [('-1', '8'), ('0', '0'), ('1/2', '6'), ('1', '-3/10'),
          ('2', '-10'), ('3', '0'), ('4', '11'), ('9/2', '17'),
          ('5', '16'), ('6', '25')]
P = [(F(x), F(y)) for x, y in COORDS]
V = tuple(range(len(P)))


def det(i, j, k):
    a, b, c = P[i], P[j], P[k]
    return (b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])


triples = {q: det(*q) for q in combinations(V, 3)}
colors = {q: ('R' if d > 0 else 'B' if d < 0 else '0')
          for q, d in triples.items()}


def path(p, color):
    return all(colors[p[t:t+3]] == color for t in range(len(p)-2))


def paths(domain):
    return {c: [p for k in range(2, len(domain)+1)
                for p in combinations(domain, k) if path(p, c)]
            for c in ('R', 'B')}


def hitting(edges, universe):
    """All subsets by size; empty edge means no transversal exists."""
    edges = sorted(set(tuple(sorted(e)) for e in edges))
    levels = []
    for k in range(len(universe)+1):
        good = [list(h) for h in combinations(universe, k)
                if all(set(h).intersection(e) for e in edges)]
        levels.append({'size': k, 'number': len(good), 'sets': good})
    first = next((a for a in levels if a['number']), None)
    return {'edges': edges, 'tau': first['size'] if first else None,
            'all_minimum_transversals': first['sets'] if first else [],
            'all_transversals_by_size': levels}


def pair_intersections(family):
    return [{'a': a, 'b': b,
             'physical': sorted(set(a).intersection(b)),
             'internal': sorted(set(a[1:-1]).intersection(b[1:-1])),
             'outer_endpoint': sorted({a[0], a[-1]} & {b[0], b[-1]})}
            for a, b in combinations(family, 2)]


def hull(p):
    """Independent monotone-chain convex hull, with exact determinants."""
    chains = []
    for order in (p, tuple(reversed(p))):
        chain = []
        for v in order:
            while len(chain) >= 2 and det(chain[-2], chain[-1], v) <= 0:
                chain.pop()
            chain.append(v)
        chains.append(chain[:-1])
    return chains[0] + chains[1]


def main():
    all_paths = paths(V)
    by_end = {}
    for i, j in combinations(V, 2):
        by_end[i, j] = {c: [p for p in all_paths[c]
                           if (p[0], p[-1]) == (i, j)] for c in ('R', 'B')}
    same_end = []
    weak7 = []
    opposite_overlap = []
    for (i, j), pp in by_end.items():
        maxima = {c: max(map(len, pp[c])) for c in ('R', 'B')}
        same_end.append({'endpoints': [i, j], 'maxima': maxima,
                         'maximum_sum': sum(maxima.values()),
                         'maximal_paths': {c: [p for p in pp[c]
                                             if len(p) == maxima[c]]
                                           for c in ('R', 'B')}})
        for r in pp['R']:
            for b in pp['B']:
                overlap = sorted(set(r[1:-1]) & set(b[1:-1]))
                if overlap:
                    opposite_overlap.append({'R': r, 'B': b, 'internal': overlap})
                if len(r)+len(b) == 9:
                    weak7.append({'R': r, 'B': b, 'internal_intersection': overlap,
                                  'union': sorted(set(r) | set(b))})
    # Independently compute exact reachable lengths using state (start,prev,last).
    reachable = {c: {} for c in ('R', 'B')}
    for c in ('R', 'B'):
        for j in V:
            for i in range(j):
                reachable[c][i, i, j] = {2}
            states = list(reachable[c].items())
            for (s, i, last), lengths in states:
                if last == j:
                    for k in range(j+1, len(V)):
                        if colors[i, j, k] == c:
                            reachable[c].setdefault((s, j, k), set()).update(
                                length+1 for length in lengths)
    dp_differences = []
    dp_lengths = []
    for endpoints, pp in by_end.items():
        row = {'endpoints': endpoints}
        for c in ('R', 'B'):
            got = sorted({length for (s, _, last), lengths in reachable[c].items()
                          if (s, last) == endpoints for length in lengths})
            expected = sorted(set(map(len, pp[c])))
            row[c] = got
            if got != expected:
                dp_differences.append({'endpoints': endpoints, 'color': c,
                                       'dp': got, 'enumeration': expected})
        dp_lengths.append(row)
    packets = []
    for q in combinations(V, 4):
        seq = ''.join(colors[t] for t in combinations(q, 3))
        changes = sum(a != b for a, b in zip(seq, seq[1:]))
        packets.append({'vertices': q, 'colors': seq, 'changes': changes,
                        'valid': changes <= 1 and '0' not in seq})
    r6 = [p for p in all_paths['R'] if len(p) == 6]
    b4 = [p for p in all_paths['B'] if len(p) == 4]
    sources = sorted({p[0] for p in r6})
    terminals = sorted({p[-1] for p in r6})
    neutral = tuple(v for v in V if v not in sources+terminals)
    neutral_paths = paths(neutral)
    neutral_r4 = [p for p in neutral_paths['R'] if len(p) == 4]
    all7 = [{'vertices': p, 'hull': hull(p), 'convex': len(hull(p)) == 7}
            for p in combinations(V, 7)]
    anticipated_r6 = [tuple(map(int, s)) for s in
                      ('013567', '014567', '234567', '013589', '013689')]
    source_sha = globals().get('CHECKER_SOURCE_SHA256')
    if source_sha is None:
        with open(__file__, 'rb') as stream:
            source_sha = hashlib.sha256(stream.read()).hexdigest()
    result = {
        'scope': 'One explicit rational planar 10-point witness, no general bound or external audit.',
        'definitions': {
            'indexing': '0-based, strictly increasing x coordinate',
            'R': 'slope(i,j)<slope(j,k), equivalently determinant>0',
            'B': 'slope(i,j)>slope(j,k), equivalently determinant<0',
            'path': 'Increasing vertex sequence; each consecutive triple has its color; length counts vertices; 2-point paths both colors.',
            'weak7': 'Same outer endpoints, R and B lengths sum to 9; no disjointness assumption imposed.',
            'hitting': 'Minimum vertex set meeting every listed edge; complete subsets are enumerated.',
        },
        'execution': {'utc': datetime.now(timezone.utc).isoformat(),
                      'host': socket.gethostname(), 'platform': platform.platform(),
                      'python_executable': sys.executable, 'python_version': sys.version,
                      'source_sha256': source_sha},
        'points': [{'index': i, 'x': x, 'y': y} for i, (x, y) in enumerate(COORDS)],
        'triples': [{'vertices': q, 'determinant': str(d), 'color': colors[q]}
                    for q, d in triples.items()],
        'degenerate_triples': [q for q, d in triples.items() if d == 0],
        'packets': packets,
        'all_monochromatic_paths': all_paths,
        'path_counts_by_length': {c: {str(k): sum(len(p) == k for p in all_paths[c])
                                    for k in range(2, len(V)+1)} for c in ('R', 'B')},
        'longest': {c: max(map(len, all_paths[c])) for c in ('R', 'B')},
        'same_endpoint_maxima': same_end,
        'maximum_same_endpoint_sum': max(r['maximum_sum'] for r in same_end),
        'same_endpoint_dp_reachable_lengths': dp_lengths,
        'dp_enumeration_differences': dp_differences,
        'R6': r6, 'B4': b4, 'weak7': weak7,
        'same_endpoint_opposite_color_internal_overlaps': opposite_overlap,
        'R6_pair_intersections': pair_intersections(r6),
        'R6_total_internal_intersection': sorted(set.intersection(*(set(p[1:-1]) for p in r6))) if r6 else [],
        'R6_physical_transversal': hitting(r6, V),
        'R6_internal_transversal': hitting([p[1:-1] for p in r6], V),
        'R6_outer_endpoint_transversal': hitting([(p[0], p[-1]) for p in r6], V),
        'R6_sources': sources, 'R6_terminals': terminals, 'D0': neutral,
        'D0_all_monochromatic_paths': neutral_paths,
        'D0_R4': neutral_r4,
        'D0_R4_transversal': hitting(neutral_r4, neutral),
        'all_seven_subsets_convex_hull_check': all7,
        'convex_seven_subsets': [row['vertices'] for row in all7 if row['convex']],
        'anticipated_R6_matches': sorted(r6) == sorted(anticipated_r6),
        'anticipated_B4_matches': b4 == [(1, 2, 7, 8)],
    }
    result['summary'] = {
        'triple_count': len(triples), 'degenerate_count': len(result['degenerate_triples']),
        'packet_count': len(packets), 'invalid_packet_count': sum(not p['valid'] for p in packets),
        'weak7_count': len(weak7), 'convex_seven_count': len(result['convex_seven_subsets']),
        'longest': result['longest'], 'maximum_same_endpoint_sum': result['maximum_same_endpoint_sum'],
        'R6_count': len(r6), 'B4_count': len(b4),
        'physical_tau': result['R6_physical_transversal']['tau'],
        'internal_tau': result['R6_internal_transversal']['tau'],
        'endpoint_tau': result['R6_outer_endpoint_transversal']['tau'],
        'D0': neutral, 'D0_R4_count': len(neutral_r4),
        'dp_enumeration_agree': not dp_differences,
    }
    print(json.dumps(result, indent=2))
    return 0 if (not result['degenerate_triples'] and
                 all(p['valid'] for p in packets) and not dp_differences) else 1


if __name__ == '__main__':
    sys.exit(main())
