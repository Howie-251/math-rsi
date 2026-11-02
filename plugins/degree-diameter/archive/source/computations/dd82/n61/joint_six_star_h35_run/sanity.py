"""Truth tables and independent actual-assignment checks, without SAT calls."""
from itertools import combinations, product
import json
from pathlib import Path
import check
import encode

HERE = Path(__file__).resolve().parent


def counter_checks():
    checks = 0
    for relation, bound in product(('at_least', 'at_most', 'exact'), range(10)):
        em = encode.CNF()
        x = [em.var() for _ in range(6)]
        inputs = x + [-x[0], x[1], True, False]
        getattr(em, relation)(inputs, bound)
        for bits in product((False, True), repeat=6):
            val = em.extend(dict(zip(x, bits)))
            count = sum(encode.truth(v, val) for v in inputs)
            want = count >= bound if relation == 'at_least' else count <= bound if relation == 'at_most' else count == bound
            actual = all(any(encode.truth(v, val) for v in row) for row in em.clauses)
            assert actual == want, (relation, bound, bits, count)
            checks += 1
    for kind in ('and', 'or'):
        em = encode.CNF()
        x = [em.var() for _ in range(3)]
        out = em.gate(kind, [x[0], -x[1], x[2]])
        for bits in product((False, True), repeat=4):
            values = dict(zip(x+[out], bits))
            want = all((bits[0], not bits[1], bits[2])) if kind == 'and' else any((bits[0], not bits[1], bits[2]))
            actual = all(any(encode.truth(v, values) for v in row) for row in em.clauses)
            assert actual == (bits[3] == want)
            checks += 1
    return checks


def compare(model, requested_edges, g, label):
    # The actual assignment graph includes all fixed stars, only permitted free bits.
    edges = model['fixed'] | (set(requested_edges) & set(model['free']))
    data = dict(n=model['n'], edges=sorted(edges), f=model['colors'], g=g,
                A=model['centers'], P=model['P'])
    direct = check.inspect(data, model['q'])
    values = encode.assignment(model, edges, g)
    rejects = encode.rejected_groups(model, values)
    expected = sorted(k for k, passed in direct['groups'].items() if not passed)
    assert rejects == expected, (label, rejects, expected)
    for ab, lit in model['covered'].items():
        assert encode.truth(lit, values) == direct['covered'][ab], (label, ab)
    return dict(label=label, rejected_groups=rejects, edges=len(edges),
                valid_necessary_object=direct['valid_necessary_object'])


def main():
    tables = counter_checks()
    small = encode.build(3)
    # C15 has a genuine four-center packing and independent three-point complement.
    original_centers = [0, 12, 4, 8]
    mapping = {}
    for s, v in enumerate(original_centers):
        for w in ((v-1) % 15, v, (v+1) % 15):
            mapping[w] = 3*s+(w % 3)
    rest = set(range(15))-set(mapping)
    for w in rest:
        mapping[w] = 12+(w % 3)
    assert len(set(mapping.values())) == 15
    cycle = {encode.pair(mapping[i], mapping[(i+1) % 15]) for i in range(15)}
    g = list(small['colors'])
    cases = [compare(small, cycle, g, 'C15-real-packing-dual-local-colors')]
    assert cases[0]['rejected_groups'] == ['all_permutation_intersection_grid']
    edge = next(ab for ab in sorted(cycle) if ab not in small['fixed'])
    cases.append(compare(small, cycle-{edge}, g, 'C15-delete-free-edge'))
    changed = list(g)
    changed[0] = (changed[0]+1) % 3
    cases.append(compare(small, cycle, changed, 'C15-change-one-second-color'))
    formal = encode.build()
    # Distinct fixed-front assignments exercise every formal condition group.
    for mode in ('identity', 'reflection', 'shifted'):
        g = []
        for s in range(6):
            for a in range(5):
                g.append(a if mode == 'identity' else (2*s-a) % 5 if mode == 'reflection' else (a+s) % 5)
        g += list(range(5))
        extra = {ab for index, ab in enumerate(formal['free']) if index % 7 == 0}
        cases.append(compare(formal, formal['fixed'] | extra, g, 'formal-static-'+mode))
    result = dict(status='PASSED', solver_calls=0, truth_table_assignments=tables,
                  assignment_cases=cases, formal_variables=formal['em'].nv,
                  formal_clauses=len(formal['em'].clauses),
                  note='Positive C15 exercises packing and both local colors; grid rejects it. '
                       'All formal constraint groups and actual covered pairs compared independently.')
    (HERE/'sanity.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
