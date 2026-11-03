"""Full61 construction in complete epsilon=1 single-packing coordinates.

No solve at import/build.  CNF gates and counters are imported unchanged from
the earlier joint H35 encoder; the new model and all61 coverage are below.
"""
import argparse
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
LIBRARY = HERE.parent / 'joint_six_star_h35_run' / 'encode.py'
spec = importlib.util.spec_from_file_location('prior_h35_cnf_library', LIBRARY)
library = importlib.util.module_from_spec(spec)
spec.loader.exec_module(library)
CNF, neg, truth = library.CNF, library.neg, library.truth

A, P, L = list(range(6)), list(range(6, 11)), list(range(11, 35))
FIRST_A = [0, 0, 1, 2, 3, 4]
FIRST = FIRST_A + list(range(5)) + [b for a in FIRST_A for b in range(5) if b != a]
# S=(A,q,B2,B3,B4,B5); T=(p,B,Y2,Y3,Y4,Y5).
K = {(0, 0), (1, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)}
S_SIZES, T_SIZES = [6, 5, 6, 6, 6, 6], [5, 6, 6, 6, 6, 6]


def pair(a, b):
    return min(a, b), max(a, b)


def onehot_row(em, width, fixed=None, allowed=None):
    if fixed is not None:
        return [b == fixed for b in range(width)]
    allowed = set(range(width)) if allowed is None else set(allowed)
    return [em.var() if b in allowed else False for b in range(width)]


def closed_count_port(em, inputs, blocked):
    """Exact c+b in {1,2}, port=c+b-1; valid also when b=own=1.

    The returned bit is total on arbitrary primary assignments, but represents
    c+b-1 only when the three local requirements hold.
    """
    present = em.gate('or', inputs)
    repeat = em.threshold(inputs, 2)
    em.at_most(inputs, 2)
    em.add(present, blocked)
    em.add(neg(repeat), neg(blocked))
    return em.gate('or', [repeat, em.gate('and', [blocked, present])])


def build():
    em = CNF()
    fixed = {pair(a, 11+4*a+j) for a in A for j in range(4)}
    free_pairs = list(product(P, L)) + list(combinations(L, 2))
    free = {pair(*ab): em.var() for ab in free_pairs}
    # Once the A first colors are named, each star's leaves are named by f.
    # This is only a vertex labeling; every second-color assignment stays free.
    f = [onehot_row(em, 5, FIRST[v]) for v in range(35)]
    g = [onehot_row(em, 5, v-6 if v in P else None) for v in range(35)]
    S = [onehot_row(em, 6, 0 if v in A else None, range(1, 6)) for v in range(35)]
    T = [onehot_row(em, 6, 0 if v in P else None, range(1, 6)) for v in range(35)]
    primary_count = em.nv

    def edge(a, b):
        if a == b:
            return False
        ab = pair(a, b)
        return True if ab in fixed else free.get(ab, False)

    def onehot():
        for rows in (f, g, S, T):
            for row in rows:
                em.exact(row, 1)
    em.section('onehot_incidence_maps', onehot)

    def degree_split():
        for p in P:
            em.exact([edge(p, w) for w in L], 4)
        for v in L:
            em.exact([edge(v, w) for w in P+L if w != v], 3)
    em.section('single_packing_degree_split', degree_split)

    def normalization():
        # A is an ordinary S class; its second repeated color remains free.
        for b in range(5):
            em.at_least([g[v][b] for v in A], 1)
            em.at_most([g[v][b] for v in A], 2)
    em.section('legal_color_normalization', normalization)

    def color_grid():
        for rows in (f, g):
            for b in range(5):
                em.exact([row[b] for row in rows], 7)
        for a, b in product(range(5), repeat=2):
            em.at_least([em.gate('and', [f[v][a], g[v][b]]) for v in range(35)], 1)
    em.section('color_sizes_and_M_ge_J', color_grid)

    def dual_colors():
        for rows in (f, g):
            for v, b in product(range(35), range(5)):
                inputs = [rows[v][b]] + [em.gate('and', [edge(v, w), rows[w][b]])
                          for w in range(35) if w != v and edge(v, w) is not False]
                em.exact(inputs, 1)
    em.section('dual_local_bijections', dual_colors)

    def parent_sizes():
        for rows, sizes in ((S, S_SIZES), (T, T_SIZES)):
            for x, size in enumerate(sizes):
                em.exact([row[x] for row in rows], size)
    em.section('full_parent_class_sizes', parent_sizes)

    def independence():
        for u, v in combinations(range(35), 2):
            h = edge(u, v)
            if h is False:
                continue
            for rows in (S, T):
                for x in range(6):
                    em.add(neg(h), neg(rows[u][x]), neg(rows[v][x]))
    em.section('full_S_T_independence', independence)

    def parent_color_counts():
        for parent, special in ((S, 1), (T, 0)):
            for colors in (f, g):
                for x, b in product(range(6), range(5)):
                    inputs = [em.gate('and', [parent[v][x], colors[v][b]]) for v in range(35)]
                    em.at_least(inputs, 1)
                    em.at_most(inputs, 1 if x == special else 2)
    em.section('full_parent_color_marginals', parent_color_counts)

    ports = {}

    def parent_ports(rows, other, transpose, support, row_sums, name):
        actual_ports = [[False]*35 for _ in range(6)]
        for z, x in product(range(35), range(6)):
            inputs = [rows[z][x]] + [em.gate('and', [edge(z, w), rows[w][x]])
                      for w in range(35) if w != z and edge(z, w) is not False]
            blockers = [other[z][y] for y in range(6)
                        if ((y, x) if transpose else (x, y)) in K]
            blocked = em.gate('or', blockers)
            port = closed_count_port(em, inputs, blocked)
            actual_ports[x][z] = port
            em.add(neg(port), support[z])
            # No own-parent-zero restriction: P intersect Q has own port 1.
        for x in range(6):
            em.exact(actual_ports[x], row_sums[x])
        for z in range(35):
            col = [actual_ports[x][z] for x in range(6)]
            em.at_most(col, 1)
            any_port = em.gate('or', col)
            em.add(neg(any_port), support[z])
            em.add(any_port, neg(support[z]))
        ports[name] = actual_ports

    em.section('exact_S_closed_counts_and_beta',
               lambda: parent_ports(S, T, False, [v in P for v in range(35)],
                                    [0, 1, 1, 1, 1, 1], 'beta'))
    em.section('exact_T_closed_counts_and_gamma',
               lambda: parent_ports(T, S, True, [S[v][1] for v in range(35)],
                                    [1, 0, 1, 1, 1, 1], 'gamma'))

    def intersection():
        for x, y in product(range(6), repeat=2):
            inputs = [em.gate('and', [S[v][x], T[v][y]]) for v in range(35)]
            if (x, y) in K:
                if (x, y) != (1, 0):
                    em.at_most(inputs, 0)
                # Gamma[q,p] is free; exact row/column sizes imply eta in {0,1}.
            else:
                em.at_least(inputs, 1)
    em.section('actual_ST_intersection_permutation', intersection)

    # All 61 vertices, including actual core, parents, K and H incidences.
    full = {ab: False for ab in combinations(range(61), 2)}
    core = {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)}
    core |= {(0, 4+i) for i in range(5)} | {(1, 9+i) for i in range(5)}
    core |= {(2, 14+x) for x in range(6)} | {(3, 20+y) for y in range(6)}
    core |= {(14+x, 20+y) for x, y in K}
    for ab in core:
        full[pair(*ab)] = True
    for z in range(35):
        for rows, offset in ((f, 4), (g, 9), (S, 14), (T, 20)):
            for x, lit in enumerate(rows[z]):
                full[offset+x, 26+z] = lit
    for a, b in combinations(range(35), 2):
        full[26+a, 26+b] = edge(a, b)

    def full_edge(a, b):
        return False if a == b else full[pair(a, b)]

    covered = {}
    def complete_coverage():
        for a, b in combinations(range(61), 2):
            terms = [full_edge(a, b)]
            terms += [em.gate('and', [full_edge(a, w), full_edge(w, b)])
                      for w in range(61) if w not in (a, b)]
            literal = em.gate('or', terms)
            covered[a, b] = literal
            em.add(literal)
    em.section('all_1830_original_pairs_covered', complete_coverage)
    return dict(em=em, fixed=fixed, free=free, f=f, g=g, S=S, T=T,
                ports=ports, primary_count=primary_count, full_edges=full, covered=covered)


def assignment(model, data):
    edges = {pair(*ab) for ab in data['edges']}
    values = {var: ab in edges for ab, var in model['free'].items()}
    for name in ('f', 'g', 'S', 'T'):
        for v, row in enumerate(model[name]):
            for b, var in enumerate(row):
                if not isinstance(var, bool):
                    values[var] = data[name][v] == b
                else:
                    assert var == (data[name][v] == b), ('fixed map', name, v, b)
    return model['em'].extend(values)


def rejected_groups(model, values):
    em = model['em']
    return sorted(name for name, (lo, hi) in em.groups.items()
                  if any(not any(truth(x, values) for x in clause)
                         for clause in em.clauses[lo:hi]))


def save(path, value):
    path.write_text(json.dumps(value, indent=2)+'\n')


def prepare():
    assert not any((HERE/x).exists() for x in ('input.cnf', 'encoding.json', 'variable_map.json'))
    model = build()
    em = model['em']
    with (HERE/'input.cnf').open('w') as stream:
        stream.write(f'p cnf {em.nv} {len(em.clauses)}\n')
        for row in em.clauses:
            stream.write(' '.join(map(str, row))+' 0\n')
    mapping = dict(fixed_edges=sorted(model['fixed']),
                   free_edges=[[*ab, var] for ab, var in model['free'].items()],
                   **{name: model[name] for name in ('f', 'g', 'S', 'T')})
    save(HERE/'variable_map.json', mapping)
    info = dict(status='PREPARED_NOT_RUN', variables=em.nv, clauses=len(em.clauses),
                primary_variables=model['primary_count'], free_H_edge_variables=len(model['free']),
                fixed_H_edges=len(model['fixed']), covered_original_pairs=len(model['covered']),
                groups=em.groups, proof_logging=False, epsilon=1, eta_fixed=False,
                shared_centers_fixed=False,
                scope='Complete epsilon=1 adjacent-double full61 construction in single-packing '
                      'coordinates; all second colors, all shared-center counts, full S/T, '
                      'correct blocked and own ports, and all 1830 actual original pairs. '
                      'No epsilon=0 input is included.')
    save(HERE/'encoding.json', info)
    print(json.dumps(info, indent=2))


def decode():
    values = {}
    for line in (HERE/'solver.log').read_text().splitlines():
        if line.startswith('v '):
            for lit in map(int, line[2:].split()):
                if lit:
                    values[abs(lit)] = lit > 0
    checked = 0
    with (HERE/'input.cnf').open() as stream:
        for line in stream:
            if line.startswith(('p', 'c')):
                continue
            row = list(map(int, line.split()))
            assert row[-1] == 0
            assert any(truth(lit, values) for lit in row[:-1]), ('false CNF row', checked+1)
            checked += 1
    mapping = json.loads((HERE/'variable_map.json').read_text())
    edges = [tuple(ab) for ab in mapping['fixed_edges']]
    edges += [(a, b) for a, b, var in mapping['free_edges'] if values[var]]
    data = dict(n=35, edges=sorted(edges))
    for name in ('f', 'g', 'S', 'T'):
        data[name] = []
        for row in mapping[name]:
            selected = [b for b, lit in enumerate(row) if truth(lit, values)]
            assert len(selected) == 1
            data[name].append(selected[0])
    save(HERE/'candidate_h35.json', data)
    # Decode actual original edges directly from the original adjacency recipe.
    actual = {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)}
    actual |= {(0, 4+i) for i in range(5)} | {(1, 9+i) for i in range(5)}
    actual |= {(2, 14+x) for x in range(6)} | {(3, 20+y) for y in range(6)}
    actual |= {(14+x, 20+y) for x, y in K}
    for z in range(35):
        for name, offset in (('f', 4), ('g', 9), ('S', 14), ('T', 20)):
            actual.add((offset+data[name][z], 26+z))
    actual |= {(26+a, 26+b) for a, b in edges}
    result = dict(n=61, edges=sorted(actual), source='same H35 and four decoded parent maps')
    save(HERE/'candidate.json', result)
    with (HERE/'candidate.edges').open('w') as stream:
        stream.write(f'61 {len(actual)}\n')
        stream.writelines(f'{a} {b}\n' for a, b in sorted(actual))
    save(HERE/'model_check.json', dict(all_saved_clauses_satisfied=True, clauses=checked,
                                      target61_verified=False))
    print('All saved CNF clauses checked; actual61 edge table decoded for independent BFS.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode'))
    args = parser.parse_args()
    prepare() if args.action == 'prepare' else decode()
