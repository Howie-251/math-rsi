"""Small semantics only: truth tables and actual assignments, never a solver."""
from itertools import combinations, product
import json
from pathlib import Path
import random
import check
import encode

HERE = Path(__file__).resolve().parent


def counter_checks():
    # Retain the previous counter contract test, including repeated/signed inputs.
    checks = 0
    for relation, bound in product(('at_least', 'at_most', 'exact'), range(10)):
        em = encode.CNF()
        x = [em.var() for _ in range(6)]
        inputs = x + [-x[0], x[1], True, False]
        getattr(em, relation)(inputs, bound)
        for bits in product((False, True), repeat=6):
            values = em.extend(dict(zip(x, bits)))
            count = sum(encode.truth(v, values) for v in inputs)
            want = count >= bound if relation == 'at_least' else count <= bound if relation == 'at_most' else count == bound
            actual = all(any(encode.truth(v, values) for v in row) for row in em.clauses)
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


def degree_fixture():
    """A prescribed uncolored double packing; it is not a claimed target."""
    c, d = [0, 0, 1, 2, 3, 4], [1, 2, 3, 4, 0, 1]
    f = c+d+list(range(5))
    for s in range(6):
        f.extend(sorted(set(range(5))-{c[s], d[s]}))
    edges = {(s, 6+s) for s in range(6)}
    edges |= {(s, 17+3*s+j) for s in range(6) for j in range(3)}
    edges |= {(6+s, 17+3*s+j) for s in range(6) for j in range(3)}
    # Two copies of the same 5-cycle kernel, with prescribed lengths 2^8,1^2.
    cursor = 17
    for index in range(10):
        count = 2 if index < 8 else 1
        path = [12+index % 5]+list(range(cursor, cursor+count))+[12+(index+1) % 5]
        edges |= {encode.pair(a, b) for a, b in zip(path, path[1:])}
        cursor += count
    assert cursor == 35
    s = [0]*6+[1]*6+[2]*5+[3]*6+[4]*6+[5]*6
    t = [None]*35
    for z in range(12, 17):
        t[z] = 0
    others = list(range(12))+list(range(17, 35))
    for index, z in enumerate(others):
        t[z] = 1+index//6
    return dict(n=35, edges=sorted(edges), f=f, g=list(f), S=s, T=t)


def compare(model, data, label):
    actual_edges = model['fixed'] | (set(map(tuple, data['edges'])) & set(model['free']))
    assert set(map(tuple, data['edges'])) == actual_edges
    direct = check.inspect(data)
    values = encode.assignment(model, data)
    rejected = encode.rejected_groups(model, values)
    expected = sorted(name for name, passed in direct['groups'].items() if not passed)
    assert rejected == expected, (label, rejected, expected)
    for ab, lit in model['full_edges'].items():
        assert encode.truth(lit, values) == (ab in direct['original_edges']), ('actual61 adjacency', label, ab)
    for ab, lit in model['covered'].items():
        assert encode.truth(lit, values) == direct['covered'][ab], ('actual61 coverage', label, ab)
    adj = [set() for _ in range(35)]
    for a, b in data['edges']:
        adj[a].add(b)
        adj[b].add(a)
    for port, parent in (('beta', 'S'), ('gamma', 'T')):
        for x, row in enumerate(model['ports'][port]):
            for z, lit in enumerate(row):
                count = sum(data[parent][v] == x for v in adj[z] | {z})
                assert encode.truth(lit, values) == (count >= 2), (port, label, x, z)
    return dict(label=label, rejected_groups=rejected,
                H_edges=len(data['edges']), target_candidate=False,
                original_covered=sum(direct['covered'].values()),
                degree_split_passed=direct['groups']['double_packing_degree_split'])


def main():
    tables = counter_checks()
    model = encode.build()  # Memory only: no input.cnf or formal preparation.
    fixture = degree_fixture()
    cases = [compare(model, fixture, 'prescribed-uncolored-double-packing')]
    assert cases[0]['degree_split_passed']
    altered = {key: list(value) if isinstance(value, list) else value for key, value in fixture.items()}
    altered['edges'] = list(fixture['edges'])
    removable = next(ab for ab in fixture['edges'] if ab in model['free'] and ab[0] in encode.P)
    altered['edges'].remove(removable)
    cases.append(compare(model, altered, 'delete-one-P-R-edge'))
    assert not cases[-1]['degree_split_passed']
    rng = random.Random(610018)
    for index in range(3):
        data = degree_fixture()
        if index:
            data['edges'] = sorted(model['fixed'] | {ab for ab in model['free'] if rng.random() < (0.12+0.08*index)})
        for name in ('f', 'g'):
            movable = (encode.AP+encode.R) if name == 'f' else (encode.A+encode.AP+encode.R)
            for v in movable:
                data[name][v] = rng.randrange(5)
        s_pool = [2]*5+[3]*6+[4]*6+[5]*6
        t_pool = [x for x in range(1, 6) for _ in range(6)]
        rng.shuffle(s_pool)
        rng.shuffle(t_pool)
        for v, color in zip(encode.P+encode.R, s_pool):
            data['S'][v] = color
        for v, color in zip(encode.A+encode.AP+encode.R, t_pool):
            data['T'][v] = color
        cases.append(compare(model, data, f'actual-assignment-{index}'))
    negative = check.inspect(fixture, include_bfs=True)
    assert not negative['target61_verified']
    result = dict(status='PASSED', solver_calls=0, truth_table_assignments=tables,
                  assignment_cases=cases, original_pairs_per_case=1830,
                  in_memory_variables=model['em'].nv, in_memory_clauses=len(model['em'].clauses),
                  formal_input_written=False, complete_positive_example_available=False,
                  note='All constraint groups, all61 adjacency/coverage literals and both derived '
                       'port arrays compared with independent direct arithmetic. The prescribed '
                       'fixture verifies the uncolored degree split only; no full target is claimed.')
    (HERE/'sanity.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
