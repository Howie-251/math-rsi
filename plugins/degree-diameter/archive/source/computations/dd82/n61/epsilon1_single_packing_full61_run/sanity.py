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


def port_truth_checks():
    """All local c/b cases; x[0] can be the vertex's own-parent incidence."""
    em = encode.CNF()
    x = [em.var() for _ in range(5)]
    blocked = em.var()
    port = encode.closed_count_port(em, x, blocked)
    checks, own_one_cases = 0, 0
    for bits in product((False, True), repeat=6):
        values = em.extend(dict(zip(x+[blocked], bits)))
        count, b = sum(bits[:5]), int(bits[5])
        accepted = all(any(encode.truth(v, values) for v in row) for row in em.clauses)
        assert accepted == (count+b in (1, 2)), (bits, count, b)
        if accepted:
            assert encode.truth(port, values) == bool(count+b-1)
        if bits[0] and b and count == 1:
            assert accepted and encode.truth(port, values)
            own_one_cases += 1
        checks += 1
    assert own_one_cases == 1
    return dict(assignments=checks, blocked_own_port_one_accepted=True,
                legal_pairs_c_b=[[1, 0], [2, 0], [0, 1], [1, 1]])


def degree_fixture():
    """A prescribed uncolored single packing, not a complete target example."""
    edges = {(a, 11+4*a+j) for a in range(6) for j in range(4)}
    # First 20 leaves have one P neighbor, all 24 form a cycle; the last four
    # receive two additional disjoint chords. Each leaf residual degree is 3.
    edges |= {(6+i, 11+4*i+j) for i in range(5) for j in range(4)}
    edges |= {encode.pair(11+i, 11+(i+1) % 24) for i in range(24)}
    edges |= {(31, 33), (32, 34)}
    f = [0, 0, 1, 2, 3, 4]+list(range(5))
    for center_color in [0, 0, 1, 2, 3, 4]:
        f.extend(b for b in range(5) if b != center_color)
    s = [0]*6+[1]*5+[2]*6+[3]*6+[4]*6+[5]*6
    t = [None]*35
    for z in range(6, 11):
        t[z] = 0
    others = list(range(6))+list(range(11, 35))
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
    # This independently stated K is not imported from encode.py.
    k = [[int(y in row) for y in range(6)] for row in ([0], [0, 1], [2], [3], [4], [5])]
    own_port_one = 0
    for name, parent, other, transposed in (('beta', 'S', 'T', False), ('gamma', 'T', 'S', True)):
        for x, row in enumerate(model['ports'][name]):
            for z, lit in enumerate(row):
                count = sum(data[parent][v] == x for v in adj[z] | {z})
                b = k[data[other][z]][x] if transposed else k[x][data[other][z]]
                total_gate_value = count >= 2 or (b and count >= 1)
                assert encode.truth(lit, values) == bool(total_gate_value), (name, label, x, z)
                if count+b in (1, 2):
                    assert encode.truth(lit, values) == bool(count+b-1)
                    if data[parent][z] == x and b and count == 1:
                        assert encode.truth(lit, values)
                        own_port_one += 1
    return dict(label=label, rejected_groups=rejected,
                H_edges=len(data['edges']), target_candidate=False,
                original_covered=sum(direct['covered'].values()),
                degree_split_passed=direct['groups']['single_packing_degree_split'],
                locally_valid_blocked_own_port_one=own_port_one)


def main():
    tables = counter_checks()
    ports = port_truth_checks()
    model = encode.build()  # Memory only: no input.cnf or formal preparation.
    fixture = degree_fixture()
    cases = [compare(model, fixture, 'prescribed-uncolored-single-packing')]
    assert cases[0]['degree_split_passed'] and cases[0]['locally_valid_blocked_own_port_one'] > 0
    altered = {key: list(value) if isinstance(value, list) else value for key, value in fixture.items()}
    altered['edges'] = list(fixture['edges'])
    removable = next(ab for ab in fixture['edges'] if ab in model['free'] and ab[0] in encode.P)
    altered['edges'].remove(removable)
    cases.append(compare(model, altered, 'delete-one-P-L-edge'))
    assert not cases[-1]['degree_split_passed']
    rng = random.Random(610124)
    for index in range(3):
        data = degree_fixture()
        if index:
            data['edges'] = sorted(model['fixed'] | {ab for ab in model['free'] if rng.random() < (0.12+0.08*index)})
        for v in encode.A+encode.L:
            data['g'][v] = rng.randrange(5)
        s_pool = [1]*5+[2]*6+[3]*6+[4]*6+[5]*6
        t_pool = [x for x in range(1, 6) for _ in range(6)]
        rng.shuffle(s_pool)
        rng.shuffle(t_pool)
        for v, color in zip(encode.P+encode.L, s_pool):
            data['S'][v] = color
        for v, color in zip(encode.A+encode.L, t_pool):
            data['T'][v] = color
        cases.append(compare(model, data, f'actual-assignment-{index}'))
    negative = check.inspect(fixture, include_bfs=True)
    assert not negative['target61_verified']
    result = dict(status='PASSED', solver_calls=0, truth_table_assignments=tables,
                  port_truth_table=ports, assignment_cases=cases, original_pairs_per_case=1830,
                  in_memory_variables=model['em'].nv, in_memory_clauses=len(model['em'].clauses),
                  primary_variables=model['primary_count'], fixed_H_edges=len(model['fixed']),
                  free_H_edge_variables=len(model['free']),
                  formal_input_written=False, complete_positive_example_available=False,
                  note='All groups, all61 adjacency/coverage literals and both derived port arrays '
                       'compared with independent arithmetic. Both blocked=1, own=1, port=1 and '
                       'unblocked repeat ports are covered by exhaustive local tables. The prescribed '
                       'fixture verifies only the uncolored single-packing degree split; no target is claimed.')
    (HERE/'sanity.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
