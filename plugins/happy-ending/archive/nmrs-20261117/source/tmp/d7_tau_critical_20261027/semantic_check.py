"""Independent color-only checker; no CNF builder or flag inputs."""
from itertools import combinations
import json


def analyze(colors, n):
    endpoint = {c: {} for c in (True, False)}
    ending = {c: [(v,) for v in range(n)] for c in (True, False)}
    starting = {c: [(v,) for v in range(n)] for c in (True, False)}
    for c in (True, False):
        for a in range(n):
            states = {}
            for i in range(a, n):
                for j in range(i + 1, n):
                    if i == a:
                        path = (a, j)
                    else:
                        choices = [states[h, i] + (j,) for h in range(a, i)
                                   if (h, i) in states and colors[h, i, j] == c]
                        if not choices:
                            continue
                        path = max(choices, key=lambda q: (len(q), q))
                    states[i, j] = path
                    if len(path) > len(endpoint[c].get((a, j), ())):
                        endpoint[c][a, j] = path
                    if len(path) > len(ending[c][j]): ending[c][j] = path
                    if len(path) > len(starting[c][a]): starting[c][a] = path
    bad_packets = []
    for q in combinations(range(n), 4):
        bits = [colors[t] for t in combinations(q, 3)]
        if sum(a != b for a, b in zip(bits, bits[1:])) > 1:
            bad_packets.append(list(q))
    weak = []
    for a, b in combinations(range(n), 2):
        red, blue = endpoint[True].get((a, b), ()), endpoint[False].get((a, b), ())
        if len(red) + len(blue) >= 9:
            weak.append({'ends': [a, b], 'red': red, 'blue': blue})
    joint = [v for v in range(n) if len(ending[True][v]) >= 5
             and len(starting[False][v]) >= 4]
    maxred = max(ending[True], key=len)
    maxblue = max(ending[False], key=len)
    return {'n': n, 'all_triples': len(colors), 'all_packets': len(list(combinations(range(n), 4))),
            'bad_packets': bad_packets, 'longest_red': maxred, 'longest_blue': maxblue,
            'max_same_endpoint_sum': max((len(endpoint[True].get(p, ())) +
                len(endpoint[False].get(p, ())) for p in combinations(range(n), 2)), default=0),
            'weak_witnesses': weak, 'EndR5': [v for v in range(n) if len(ending[True][v]) >= 5],
            'SrcB4': [v for v in range(n) if len(starting[False][v]) >= 4],
            'forbidden_joint': joint,
            'D7_valid': not bad_packets and len(maxblue) < 5 and len(maxred) < 7 and not weak and not joint,
            '_endpoints': endpoint}


def fixture_checks():
    import random
    rng = random.Random(2701)
    records = []
    for n in (3, 5, 7, 8):
        for trial in range(6):
            colors = {t: bool(rng.getrandbits(1)) if trial > 1 else trial == 0
                      for t in combinations(range(n), 3)}
            got = analyze(colors, n)
            direct = {c: {} for c in (True, False)}
            for k in range(2, n + 1):
                for p in combinations(range(n), k):
                    for c in (True, False):
                        if all(colors[p[i], p[i+1], p[i+2]] == c for i in range(k-2)):
                            key = (p[0], p[-1])
                            if k > len(direct[c].get(key, ())): direct[c][key] = p
            for c in (True, False):
                for ends in combinations(range(n), 2):
                    assert len(direct[c].get(ends, ())) == len(got['_endpoints'][c].get(ends, ()))
            records.append({'n': n, 'trial': trial, 'status': 'PASS'})
    return {'status': 'PASS', 'comparisons': records,
            'scope': '24 deterministic color fixtures; exhaustive consecutive-triple paths vs independent longest-path DP'}


def transversals(colors, n):
    edges = [sum(1 << v for v in p) for p in combinations(range(n), 6)
             if all(colors[t] for t in combinations(p, 3))]
    covers = [0] * n
    for i, edge in enumerate(edges):
        for v in range(n):
            if edge >> v & 1: covers[v] |= 1 << i
    all_edges = (1 << len(edges)) - 1
    def search(k):
        seen, solutions = set(), set()
        def visit(chosen, remaining):
            if chosen in seen: return
            seen.add(chosen)
            used = chosen.bit_count()
            if not remaining:
                solutions.add(chosen)
                return
            if used >= k: return
            edge_index = (remaining & -remaining).bit_length() - 1
            candidates = edges[edge_index]
            while candidates:
                bit = candidates & -candidates
                candidates -= bit
                v = bit.bit_length() - 1
                visit(chosen | bit, remaining & ~covers[v])
        visit(0, all_edges)
        return solutions
    for k in range(6):
        found = search(k)
        if found:
            rows = [[v for v in range(n) if mask >> v & 1] for mask in sorted(found)]
            return {'status': 'EXHAUSTIVE_MINIMUM_TRANSVERSALS', 'tau': k,
                    'red6_count': len(edges), 'red6_masks': edges,
                    'minimum_transversals': rows, 'minimum_count': len(rows),
                    'uses_b25_or_tau5_as_search_assumption': False}
    return {'status': 'NO_TRANSVERSAL_OF_SIZE_AT_MOST_FIVE', 'red6_count': len(edges), 'red6_masks': edges}


def check_assignment(path):
    data = json.loads(path.read_text())
    n = data['n']
    colors = {tuple(row['triple']): row['red'] for row in data['colors']}
    if set(colors) != set(combinations(range(n), 3)): raise ValueError('incomplete triple coloring')
    result = analyze(colors, n)
    result.pop('_endpoints')
    if result['D7_valid']: result['red6_transversals'] = transversals(colors, n)
    return result
