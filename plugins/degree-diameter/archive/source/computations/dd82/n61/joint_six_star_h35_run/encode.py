"""Joint actual H, second coloring, A packing and independent P; no solver here."""
import argparse
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def neg(x):
    return not x if isinstance(x, bool) else -x


def truth(x, values):
    return x if isinstance(x, bool) else values[abs(x)] == (x > 0)


class CNF:
    def __init__(self):
        self.nv = 0
        self.clauses = []
        self.gates = []
        self.groups = {}

    def var(self):
        self.nv += 1
        return self.nv

    def add(self, *lits):
        if any(x is True for x in lits):
            return
        row = tuple(dict.fromkeys(x for x in lits if x is not False))
        if not any(-x in row for x in row):
            self.clauses.append(row)

    def gate(self, kind, lits):
        lits = list(lits)
        annihilator = False if kind == 'and' else True
        identity = not annihilator
        if any(x is annihilator for x in lits):
            return annihilator
        lits = list(dict.fromkeys(x for x in lits if x is not identity))
        if any(-x in lits for x in lits):
            return annihilator
        if not lits:
            return identity
        if len(lits) == 1:
            return lits[0]
        out = self.var()
        if kind == 'and':
            for x in lits:
                self.add(-out, x)
            self.add(out, *map(neg, lits))
        else:
            for x in lits:
                self.add(out, -x)
            self.add(-out, *lits)
        self.gates.append((out, kind, lits))
        return out

    def threshold(self, inputs, target):
        """Full equivalence for sum(inputs)>=target, including signed literals."""
        target -= sum(x is True for x in inputs)
        inputs = [x for x in inputs if not isinstance(x, bool)]
        if target <= 0:
            return True
        if target > len(inputs):
            return False
        prev = [True] + [False]*target
        for x in inputs:
            current = [True]
            for k in range(1, target+1):
                p, q = prev[k], prev[k-1]
                if p is False:
                    out = self.gate('and', [q, x])
                elif q is True:
                    out = self.gate('or', [p, x])
                else:
                    out = self.var()
                    self.add(neg(p), out)
                    self.add(neg(q), -x, out)
                    self.add(-out, p, q)
                    self.add(-out, p, x)
                    self.gates.append((out, 'threshold', [p, q, x]))
                current.append(out)
            prev = current
        return prev[target]

    def at_least(self, inputs, bound):
        # Complement when this uses fewer thresholds.
        if len(inputs)-bound+1 < bound:
            self.add(neg(self.threshold(list(map(neg, inputs)), len(inputs)-bound+1)))
        else:
            self.add(self.threshold(inputs, bound))

    def at_most(self, inputs, bound):
        self.add(neg(self.threshold(inputs, bound+1)))

    def exact(self, inputs, bound):
        if bound == 1:
            self.add(*inputs)
            for a, b in combinations(inputs, 2):
                self.add(neg(a), neg(b))
        else:
            self.at_least(inputs, bound)
            self.at_most(inputs, bound)

    def section(self, name, callback):
        first = len(self.clauses)
        callback()
        self.groups[name] = (first, len(self.clauses))

    def extend(self, primary):
        values = dict(primary)
        for out, kind, lits in self.gates:
            args = [truth(x, values) for x in lits]
            values[out] = (all(args) if kind == 'and' else any(args) if kind == 'or'
                           else args[0] or (args[1] and args[2]))
        return values


def pair(a, b):
    return (min(a, b), max(a, b))


def build(q=5):
    n = q*(q+2)
    colors = [i % q for i in range(n)]
    center_colors = [0, 0] + list(range(1, q))
    centers = [q*s+c for s, c in enumerate(center_colors)]
    leftover = list(range(q*(q+1), n))
    leaves = sorted(set(range(n))-set(centers)-set(leftover))
    stars = [list(range(q*s, q*(s+1))) for s in range(q+1)]
    fixed = {pair(c, v) for c, star in zip(centers, stars) for v in star if v != c}
    em = CNF()
    free = {ab: em.var() for ab in combinations(range(n), 2)
            if colors[ab[0]] != colors[ab[1]] and
            ((ab[0] in leaves and ab[1] in leaves) or
             (ab[0] in leaves and ab[1] in leftover))}
    second = [[em.var() for _ in range(q)] for _ in range(n)]
    primary_count = em.nv

    def edge(a, b):
        if a == b:
            return False
        ab = pair(a, b)
        return True if ab in fixed else free.get(ab, False)

    def onehot():
        for row in second:
            em.exact(row, 1)
    em.section('second_color_onehot', onehot)

    def static_colors():
        for block in stars+[leftover]:
            for b in range(q):
                em.exact([second[v][b] for v in block], 1)
        for b in range(q):
            bits = [second[v][b] for v in centers]
            em.at_least(bits, 1)
            em.at_most(bits, 2)
    em.section('stars_P_and_center_colors', static_colors)

    def grid():
        for a, b in product(range(q), repeat=2):
            em.at_least([second[v][b] for v in range(n) if colors[v] == a],
                        1+int(a == b))
    em.section('all_permutation_intersection_grid', grid)

    def first_neighborhoods():
        for v in range(n):
            for b in range(q):
                if b != colors[v]:
                    em.exact([edge(v, w) for w in range(n) if colors[w] == b], 1)
    em.section('first_color_closed_neighborhoods', first_neighborhoods)

    def second_neighborhoods():
        for v, b in product(range(n), range(q)):
            inputs = [second[v][b]]
            inputs += [em.gate('and', [edge(v, w), second[w][b]])
                       for w in range(n) if w != v and edge(v, w) is not False]
            em.exact(inputs, 1)
    em.section('second_color_closed_neighborhoods', second_neighborhoods)

    covered = {}
    def coverage():
        for a, b in combinations(range(n), 2):
            if colors[a] == colors[b]:
                covered[a, b] = True
                continue
            terms = [edge(a, b)]
            terms += [em.gate('and', [second[a][c], second[b][c]]) for c in range(q)]
            terms += [em.gate('and', [edge(a, w), edge(w, b)])
                      for w in range(n) if w not in (a, b)]
            covered[a, b] = em.gate('or', terms)
    em.section('exact_actual_coverage_gates', coverage)

    def cov(a, b):
        return covered[pair(a, b)]

    if q == 5:
        def capacities():
            for v in range(n):
                em.at_least([cov(v, w) for w in range(n) if w != v],
                            25 if v in leftover else 24)
            em.at_least(list(covered.values()), 425)
        em.section('rho_capacities', capacities)

        def father_obligations():
            for a, p in product(centers, leftover):
                em.add(cov(a, p))
            for block in (centers, leftover):
                outside = sorted(set(range(n))-set(block))
                for v in block:
                    holes = [neg(cov(v, w)) for w in outside]
                    em.at_most(holes, 5)
                    for x, y in combinations(outside, 2):
                        em.add(cov(v, x), cov(v, y), neg(edge(x, y)))
        em.section('known_A_P_and_remaining_father_holes', father_obligations)
    return dict(q=q, n=n, em=em, colors=colors, centers=centers, P=leftover,
                stars=stars, fixed=fixed, free=free, second=second,
                primary_count=primary_count, covered=covered)


def assignment(model, edges, second_colors):
    edges = set(map(lambda ab: pair(*ab), edges))
    values = {var: ab in edges for ab, var in model['free'].items()}
    values.update({var: second_colors[v] == b for v, row in enumerate(model['second'])
                   for b, var in enumerate(row)})
    return model['em'].extend(values)


def rejected_groups(model, values):
    em = model['em']
    return sorted(name for name, (lo, hi) in em.groups.items()
                  if any(not any(truth(x, values) for x in clause)
                         for clause in em.clauses[lo:hi]))


def save(path, data):
    path.write_text(json.dumps(data, indent=2)+'\n')


def prepare():
    model = build()
    em = model['em']
    assert not (HERE/'input.cnf').exists()
    with (HERE/'input.cnf').open('w') as f:
        f.write(f'p cnf {em.nv} {len(em.clauses)}\n')
        for clause in em.clauses:
            f.write(' '.join(map(str, clause))+' 0\n')
    mapping = dict(q=5, n=35, f=model['colors'], centers=model['centers'], P=model['P'],
                   fixed_edges=sorted(model['fixed']),
                   free_edges=[[*ab, var] for ab, var in model['free'].items()],
                   second_variables=model['second'])
    save(HERE/'variable_map.json', mapping)
    info = dict(status='PREPARED_NOT_RUN', variables=em.nv, clauses=len(em.clauses),
                primary_variables=model['primary_count'], free_edge_variables=len(model['free']),
                fixed_edges=len(model['fixed']), groups=em.groups,
                scope='All normalized necessary H35/U/V/A6/P5 objects, all sigma and g(P); '
                      'true remaining-father hole conditions included; not a full61 target model.')
    save(HERE/'encoding.json', info)
    print(json.dumps(info, indent=2))


def decode():
    values = {}
    for line in (HERE/'solver.log').read_text().splitlines():
        if line.startswith('v '):
            for lit in map(int, line[2:].split()):
                if lit:
                    values[abs(lit)] = lit > 0
    clauses = 0
    with (HERE/'input.cnf').open() as f:
        for line in f:
            if line.startswith(('p', 'c')):
                continue
            row = list(map(int, line.split()))
            assert row[-1] == 0
            assert any(truth(lit, values) for lit in row[:-1]), ('false model clause', clauses+1)
            clauses += 1
    mp = json.loads((HERE/'variable_map.json').read_text())
    edges = [tuple(ab) for ab in mp['fixed_edges']]
    edges += [(a, b) for a, b, var in mp['free_edges'] if values[var]]
    g = []
    for row in mp['second_variables']:
        actual = [b for b, var in enumerate(row) if values[var]]
        assert len(actual) == 1
        g.append(actual[0])
    result = dict(n=35, edges=sorted(edges), f=mp['f'], g=g, A=mp['centers'], P=mp['P'])
    save(HERE/'candidate.json', result)
    with (HERE/'candidate.edges').open('w') as f:
        f.write(f'35 {len(edges)}\n')
        f.writelines(f'{a} {b}\n' for a, b in sorted(edges))
    save(HERE/'model_check.json', dict(all_clauses_satisfied=True, clauses=clauses,
                                     target61_verified=False))
    print('Complete saved CNF model checked; H35 candidate saved for independent check.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode'))
    args = parser.parse_args()
    prepare() if args.action == 'prepare' else decode()
