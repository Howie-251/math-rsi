"""One fixed 14-point schema; all 36 external endpoint orders use this file."""
from functools import lru_cache
from itertools import combinations

N = 14
VERTICES = tuple(range(N))
POOL = tuple(range(3, 11))
TRIPLES = tuple(combinations(VERTICES, 3))
COLOR = {triple: i+1 for i, triple in enumerate(TRIPLES)}


def terms(path):
    return tuple(COLOR[path[i:i+3]] for i in range(len(path)-2))


def normalized(literals):
    values = set(literals)
    return None if any(-v in values for v in values) else tuple(sorted(values))


@lru_cache(maxsize=1)
def common_clauses():
    clauses = set()
    def add(literals):
        clause = normalized(literals)
        if clause is not None:
            clauses.add(clause)
    for packet in combinations(VERTICES, 4):
        ids = [COLOR[triple] for triple in combinations(packet, 3)]
        for mask in range(16):
            bits = [(mask >> i) & 1 for i in range(4)]
            if sum(a != b for a, b in zip(bits, bits[1:])) > 1:
                add([-v if b else v for v, b in zip(ids, bits)])
    for path in combinations(VERTICES, 7):
        add([-v for v in terms(path)])
    for path in combinations(VERTICES, 6):
        add(terms(path))
    # Enumerate ALL shared-endpoint path pairs of length sum 9, including
    # overlapping interiors. No signotope disjointness lemma is needed.
    for first, last in combinations(VERTICES, 2):
        middle = tuple(range(first+1, last))
        for nr in range(6):
            nb = 5-nr
            for red_inside in combinations(middle, nr):
                red = (first,)+red_inside+(last,)
                for blue_inside in combinations(middle, nb):
                    blue = (first,)+blue_inside+(last,)
                    add([-v for v in terms(red)]+list(terms(blue)))
    return frozenset(clauses)


def build(sources, terminals):
    assert sorted(sources) == [0, 1, 2]
    assert sorted(terminals) == [11, 12, 13]
    allowed = {(sources[i], terminals[j]) for i in range(3) for j in range(i, 3)}
    forbidden_reverse = {(sources[j], terminals[i])
                         for i in range(3) for j in range(i+1, 3)}
    clauses = set(common_clauses())
    def add(literals):
        clause = normalized(literals)
        if clause is not None:
            clauses.add(clause)
    # This ranges over ALL five-vertex subsets, including other endpoints.
    for path in combinations(VERTICES, 5):
        if (path[0], path[-1]) in forbidden_reverse:
            add([-v for v in terms(path)])
    candidates = []
    for path in combinations(VERTICES, 6):
        if ((path[0], path[-1]) not in allowed or
                not set(path[1:-1]) <= set(POOL)):
            add([-v for v in terms(path)])
        else:
            selector = len(TRIPLES)+len(candidates)+1
            candidates.append((path, selector))
            # Exact equivalence: selector iff the candidate is an actual R6.
            for variable in terms(path):
                add([-selector, variable])
            add([selector]+[-variable for variable in terms(path)])
    for endpoints in zip(sources, terminals):
        add([selector for path, selector in candidates
             if (path[0], path[-1]) == endpoints])
    for deleted in combinations(VERTICES, 2):
        add([selector for path, selector in candidates
             if not set(deleted)&set(path)])
    clauses = sorted(clauses)
    nvars = len(TRIPLES)+len(candidates)
    dimacs = 'p cnf %d %d\n' % (nvars, len(clauses))
    dimacs += ''.join(' '.join(map(str, clause))+' 0\n' for clause in clauses)
    return dimacs, {'sources': sources, 'terminals': terminals, 'pool': POOL,
                    'variables': nvars, 'clauses': len(clauses),
                    'candidate_paths': len(candidates),
                    'selectors': [{'path': path, 'variable': selector}
                                  for path, selector in candidates]}
