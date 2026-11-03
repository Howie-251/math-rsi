"""Full original61 graph with a triangle-free isolated nonadjacent double pair.

No solver runs on import or build. Only R parent-vector lex order is imposed.
CNF gates/counters are imported from the previously reviewed joint H35 code.
"""
import argparse
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('reviewed_joint_cnf',
    HERE.parent/'joint_six_star_h35_run'/'encode.py')
library = importlib.util.module_from_spec(spec)
spec.loader.exec_module(library)
CNF, neg, truth = library.CNF, library.neg, library.truth

N = 61
S, U, V, R = list(range(2, 5)), list(range(5, 10)), list(range(10, 15)), list(range(15, 61))
PARENTS = S+U+V
SCOPE = ('Original61 simple 8-regular diameter2 graphs with nonadjacent roots '
         'u=0,v=1 having exactly three common neighbors, neither root in a triangle, '
         'and no other double defect incident with either root; inherited global '
         'common-neighbor cap3 and adjacent common-neighbor cap1; all remaining '
         'edges free, modulo only nonincreasing R parent-vector lex order.')


def pair(a, b):
    return (min(a, b), max(a, b))


def count_thresholds(em, inputs, maximum):
    """Equivalent sum>=j for j=0..maximum, sharing the reviewed recurrence.

    This is CNF.threshold's recurrence with all final levels retained. Constants
    are removed with their exact offset; repeated/signed inputs retain multiplicity.
    """
    offset = sum(x is True for x in inputs)
    inputs = [x for x in inputs if not isinstance(x, bool)]
    depth = max(0, maximum-offset)
    prev = [True]+[False]*depth
    for x in inputs:
        current = [True]
        for k in range(1, depth+1):
            p, q = prev[k], prev[k-1]
            if p is False:
                out = em.gate('and', [q, x])
            elif q is True:
                out = em.gate('or', [p, x])
            else:
                out = em.var()
                em.add(neg(p), out)
                em.add(neg(q), -x, out)
                em.add(-out, p, q)
                em.add(-out, p, x)
                em.gates.append((out, 'threshold', [p, q, x]))
            current.append(out)
        prev = current
    return [True if j <= offset else prev[j-offset] for j in range(maximum+1)]


def lex_nonincreasing(em, left, right):
    """Allow equality; at the first unequal coordinate require left=1,right=0."""
    assert len(left) == len(right)
    prefix_equal = True
    for x, y in zip(left, right):
        em.add(neg(prefix_equal), x, neg(y))
        equal = em.gate('or', [em.gate('and', [x, y]),
                               em.gate('and', [neg(x), neg(y)])])
        prefix_equal = em.gate('and', [prefix_equal, equal])


def common_cap_constraint(em, thresholds, edge, kind):
    """The same individual restrictions used in the three global groups."""
    if kind == 'global':
        em.add(neg(thresholds[4]))
    elif kind == 'adjacent':
        em.add(neg(edge), neg(thresholds[2]))
    elif kind == 'root':
        em.add(neg(thresholds[3]))
    else:
        raise ValueError(kind)


def build():
    em = CNF()
    fixed = {(0, x) for x in S+U} | {(1, x) for x in S+V}
    allowed = ({pair(a, b) for a in U for b in V}
               | {pair(a, b) for a in PARENTS for b in R}
               | set(combinations(R, 2)))
    free = {ab: em.var() for ab in sorted(allowed)}
    primary_count = em.nv
    assert primary_count == 1658 and len(fixed) == 16

    def edge(a, b):
        if a == b:
            return False
        ab = pair(a, b)
        return True if ab in fixed else free.get(ab, False)

    full_edges = {ab: edge(*ab) for ab in combinations(range(N), 2)}

    def degrees():
        for a in range(N):
            em.exact([edge(a, b) for b in range(N) if b != a], 8)
    em.section('all_original_degrees_8', degrees)

    common_terms, thresholds, covered = {}, {}, {}
    def definitions():
        for a, b in combinations(range(N), 2):
            terms = [em.gate('and', [edge(a, w), edge(b, w)])
                     for w in range(N) if w not in (a, b)]
            common_terms[a, b] = terms
            thresholds[a, b] = count_thresholds(em, terms, 4)
            covered[a, b] = em.gate('or', [edge(a, b), thresholds[a, b][1]])
    em.section('exact_common_and_coverage_definitions', definitions)

    em.section('all_1830_original_pairs_covered',
               lambda: [em.add(lit) for lit in covered.values()])
    em.section('global_common_at_most_3',
               lambda: [common_cap_constraint(em, row, full_edges[ab], 'global')
                        for ab, row in thresholds.items()])
    em.section('adjacent_common_at_most_1',
               lambda: [common_cap_constraint(em, row, full_edges[ab], 'adjacent')
                        for ab, row in thresholds.items()])
    em.section('selected_roots_no_other_double',
               lambda: [common_cap_constraint(em, row, full_edges[ab], 'root')
                        for ab, row in thresholds.items()
                        if (0 in ab or 1 in ab) and ab != (0, 1)])
    em.section('R_parent_vectors_nonincreasing_lex',
               lambda: [lex_nonincreasing(em, [edge(p, a) for p in PARENTS],
                                          [edge(p, b) for p in PARENTS])
                        for a, b in zip(R, R[1:])])
    return dict(em=em, fixed=fixed, free=free, primary_count=primary_count,
                full_edges=full_edges, common_terms=common_terms,
                thresholds=thresholds, covered=covered)


def assignment(model, data):
    edges = set(map(tuple, data['edges']))
    assert data['n'] == N and model['fixed'] <= edges <= model['fixed'] | set(model['free'])
    return model['em'].extend({var: ab in edges for ab, var in model['free'].items()})


def rejected_groups(model, values):
    em = model['em']
    return sorted(name for name, (start, stop) in em.groups.items()
                  if not all(any(truth(lit, values) for lit in em.clauses[i])
                             for i in range(start, stop)))


def save(path, data):
    path.write_text(json.dumps(data, indent=2)+'\n')


def prepare():
    assert not any((HERE/name).exists() for name in ('input.cnf', 'encoding.json', 'variable_map.json'))
    model = build()
    em = model['em']
    with (HERE/'input.cnf').open('w') as stream:
        stream.write(f'p cnf {em.nv} {len(em.clauses)}\n')
        for row in em.clauses:
            stream.write(' '.join(map(str, row))+' 0\n')
    save(HERE/'variable_map.json', dict(n=N, fixed_edges=sorted(model['fixed']),
         free_edges=[[a, b, var] for (a, b), var in model['free'].items()]))
    info = dict(status='PREPARED_NOT_RUN', scope=SCOPE, variables=em.nv,
                clauses=len(em.clauses), primary_edge_variables=model['primary_count'],
                fixed_original_edges=len(model['fixed']), covered_original_pairs=1830,
                groups={name: dict(start=start, stop=stop, clauses=stop-start)
                        for name, (start, stop) in em.groups.items()},
                solver_calls=0, proof_logging=False,
                symmetry='Only R parent-vector nonincreasing lex; ties allowed',
                forbidden_extra_restrictions='No fixed h, overlap, triangle-free whole graph, '
                                             'global isolated D, Wi pattern, or automorphism')
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
            assert any(truth(lit, values) for lit in row[:-1]), ('false saved CNF clause', checked+1)
            checked += 1
    enc = json.loads((HERE/'encoding.json').read_text())
    assert checked == enc['clauses']
    mapping = json.loads((HERE/'variable_map.json').read_text())
    edges = [tuple(ab) for ab in mapping['fixed_edges']]
    edges += [(a, b) for a, b, var in mapping['free_edges'] if values[var]]
    data = dict(n=N, edges=sorted(edges), source='Decoded actual original61 edge variables')
    save(HERE/'candidate.json', data)
    with (HERE/'candidate.edges').open('w') as stream:
        stream.write(f'{N} {len(edges)}\n')
        stream.writelines(f'{a} {b}\n' for a, b in sorted(edges))
    save(HERE/'model_check.json', dict(all_saved_clauses_satisfied=True,
                                      clauses=checked, target61_verified=False))
    print('All saved CNF clauses checked; actual61 edges ready for independent BFS.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode'))
    args = parser.parse_args()
    prepare() if args.action == 'prepare' else decode()
