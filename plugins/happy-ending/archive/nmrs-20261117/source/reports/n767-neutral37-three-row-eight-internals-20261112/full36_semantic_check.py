"""Independent DIMACS/schema equality checker and direct SAT witness checker.

Does not import the CNF builder. Triple IDs use a counting formula. The weak
clauses arise by pairing whole subsets, instead of choosing endpoint interiors.
"""
from functools import lru_cache
from itertools import combinations, product
from math import comb
from pathlib import Path


def vertex_tuple(mask):
    return tuple(i for i in range(14) if mask & (1 << i))


def color_id(i, j, k):
    assert 0 <= i < j < k < 14
    return (1 + sum(comb(13-a, 2) for a in range(i))
            + sum(13-b for b in range(i+1, j)) + k-j-1)


def path_terms(path):
    return [color_id(*path[i:i+3]) for i in range(len(path)-2)]


def put(target, values):
    clause = frozenset(values)
    if not any(-v in clause for v in clause):
        target.add(clause)


@lru_cache(maxsize=1)
def independent_common():
    expected = set()
    for a in range(14):
        for b in range(a+1, 14):
            for c in range(b+1, 14):
                for d in range(c+1, 14):
                    ids = [color_id(a,b,c), color_id(a,b,d),
                           color_id(a,c,d), color_id(b,c,d)]
                    for signs in product((-1, 1), repeat=4):
                        if sum(signs[i] != signs[i+1] for i in range(3)) >= 2:
                            put(expected, [-sign*variable for sign, variable in zip(signs, ids)])
    grouped = {}
    for mask in range(1 << 14):
        size = mask.bit_count()
        if not 2 <= size <= 7:
            continue
        path = vertex_tuple(mask)
        tt = path_terms(path)
        grouped.setdefault((path[0], path[-1], size), []).append(tt)
        if size == 7:
            put(expected, [-v for v in tt])
        if size == 6:
            put(expected, tt)
    # Whole-path Cartesian products, without any disjointness assumption.
    for (first, last, length), red_paths in grouped.items():
        for red in red_paths:
            for blue in grouped.get((first, last, 9-length), []):
                put(expected, [-v for v in red]+blue)
    return frozenset(expected)


def expected_schema(sources, terminals):
    expected = set(independent_common())
    allowed = {(sources[row], terminals[col])
               for row in range(3) for col in range(3) if row <= col}
    # Explicit inverse direction p_j -> q_i, j > i; all intervening vertices.
    for i in range(3):
        for j in range(i+1, 3):
            first, last = sources[j], terminals[i]
            for interior in combinations(range(first+1, last), 3):
                put(expected, [-v for v in path_terms((first,)+interior+(last,))])
    candidates = []
    all_six = sorted(vertex_tuple(mask) for mask in range(1 << 14)
                     if mask.bit_count() == 6)
    for path in all_six:
        is_allowed = ((path[0], path[-1]) in allowed
                      and all(3 <= v <= 10 for v in path[1:-1]))
        if not is_allowed:
            put(expected, [-v for v in path_terms(path)])
        else:
            selector = 365+len(candidates)
            candidates.append((path, selector))
            for term in path_terms(path):
                put(expected, [-selector, term])
            put(expected, [selector]+[-v for v in path_terms(path)])
    for row in range(3):
        put(expected, [selector for path, selector in candidates
                       if path[0] == sources[row] and path[-1] == terminals[row]])
    for x in range(14):
        for y in range(x+1, 14):
            deletion_mask = (1 << x) | (1 << y)
            put(expected, [selector for path, selector in candidates
                           if sum(1 << v for v in path) & deletion_mask == 0])
    return expected, 364+len(candidates)


def check_dimacs(path, sources, terminals):
    expected, expected_nvars = expected_schema(sources, terminals)
    actual = set()
    header = None
    row_count = 0
    errors = []
    for line in Path(path).read_text(encoding='ascii').splitlines():
        if not line or line.startswith('c'):
            continue
        if line.startswith('p '):
            if header is not None:
                errors.append('duplicate header')
            parts = line.split()
            header = (int(parts[2]), int(parts[3]))
            continue
        literals = list(map(int, line.split()))
        if not literals or literals[-1] != 0 or 0 in literals[:-1]:
            errors.append('noncanonical clause termination')
            continue
        clause = frozenset(literals[:-1])
        if any(-v in clause for v in clause):
            errors.append('tautology')
        actual.add(clause)
        row_count += 1
    missing = expected-actual
    extra = actual-expected
    if header != (expected_nvars, len(expected)):
        errors.append('header mismatch')
    if row_count != len(actual):
        errors.append('duplicate clauses')
    return {'pass': not errors and not missing and not extra,
            'method': 'independent full literal-set reconstruction; closed-form triple numbering, bit-mask path generation, whole-path weak pairs',
            'header': header, 'parsed_clause_count': row_count,
            'expected_clause_count': len(expected),
            'missing_clause_count': len(missing), 'extra_clause_count': len(extra),
            'missing_examples': [sorted(c) for c in list(missing)[:3]],
            'extra_examples': [sorted(c) for c in list(extra)[:3]],
            'errors': errors}


def transversal(edges, universe):
    for size in range(len(universe)+1):
        good = [h for h in combinations(universe, size)
                if all(set(h)&set(edge) for edge in edges)]
        if good:
            return {'tau': size, 'all_minimum': good}
    return {'tau': None, 'all_minimum': []}


def inspect_sat(model, sources, terminals):
    colors = {t: 'R' if color_id(*t) in model else 'B'
              for t in combinations(range(14), 3)}
    paths = {c: [] for c in ('R', 'B')}
    for mask in range(1 << 14):
        if mask.bit_count() < 2:
            continue
        path = vertex_tuple(mask)
        for c in paths:
            if all(colors[path[i:i+3]] == c for i in range(len(path)-2)):
                paths[c].append(path)
    r6 = sorted(path for path in paths['R'] if len(path) == 6)
    packets = []
    for packet in combinations(range(14), 4):
        cs = ''.join(colors[t] for t in combinations(packet, 3))
        packets.append({'vertices': packet, 'colors': cs,
                        'valid': sum(a != b for a, b in zip(cs, cs[1:])) <= 1})
    by_end = []
    weak7 = []
    for endpoints in combinations(range(14), 2):
        pp = {c: [p for p in paths[c] if (p[0], p[-1]) == endpoints] for c in paths}
        by_end.append({'endpoints': endpoints,
                       'maxima': {c: max(map(len, pp[c])) for c in paths},
                       'R5': [p for p in pp['R'] if len(p) == 5]})
        weak7.extend({'R': r, 'B': b} for r in pp['R'] for b in pp['B']
                     if len(r)+len(b) == 9)
    endpoints = set((p[0], p[-1]) for p in r6)
    allowed = {(sources[i], terminals[j]) for i in range(3) for j in range(i, 3)}
    reverse = [p for p in paths['R'] if len(p) == 5 and any(
        (p[0], p[-1]) == (sources[j], terminals[i]) for i in range(3) for j in range(i+1, 3))]
    deletion = [{'deleted': pair, 'R6_indices': [i for i, p in enumerate(r6)
                                              if not set(pair)&set(p)]}
                for pair in combinations(range(14), 2)]
    checks = {'packets': all(p['valid'] for p in packets),
              'no_R7': max(map(len, paths['R'])) < 7,
              'no_B6': max(map(len, paths['B'])) < 6, 'no_weak7': not weak7,
              'R6_triangular': endpoints <= allowed,
              'R6_in_pool': all(all(3 <= v <= 10 for v in p[1:-1]) for p in r6),
              'diagonals': set(zip(sources, terminals)) <= endpoints,
              'no_reverse_R5': not reverse,
              'every_pair_deletion_survives': all(d['R6_indices'] for d in deletion)}
    return {'all_checks_pass': all(checks.values()), 'checks': checks,
            'colors': [{'vertices': t, 'color': colors[t]} for t in colors],
            'packets': packets, 'all_paths': paths, 'R6': r6,
            'same_endpoint_maxima_and_R5': by_end, 'weak7': weak7,
            'reverse_R5': reverse, 'deletion_witnesses': deletion,
            'physical_transversal': transversal(r6, range(14)),
            'internal_transversal': transversal([p[1:-1] for p in r6], range(3, 11)),
            'endpoint_transversal': transversal(endpoints, range(14))}
