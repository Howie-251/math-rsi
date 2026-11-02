"""Bounded truth tables and actual61 assignments; no solving or formal input."""
from itertools import combinations, product
import json
from pathlib import Path
import random
import check
import encode

HERE = Path(__file__).resolve().parent


def clauses_hold(em, values):
    return all(any(encode.truth(x, values) for x in row) for row in em.clauses)


def counter_checks():
    checks = 0
    for relation, bound in product(('at_least', 'at_most', 'exact'), range(10)):
        em = encode.CNF()
        x = [em.var() for _ in range(6)]
        inputs = x+[-x[0], x[1], True, False]
        getattr(em, relation)(inputs, bound)
        for bits in product((False, True), repeat=6):
            values = em.extend(dict(zip(x, bits)))
            count = sum(encode.truth(v, values) for v in inputs)
            want = count >= bound if relation == 'at_least' else count <= bound if relation == 'at_most' else count == bound
            assert clauses_hold(em, values) == want, (relation, bound, bits)
            checks += 1
    for kind in ('and', 'or'):
        em = encode.CNF()
        x = [em.var() for _ in range(3)]
        out = em.gate(kind, [x[0], -x[1], x[2]])
        for bits in product((False, True), repeat=4):
            values = dict(zip(x+[out], bits))
            want = all((bits[0], not bits[1], bits[2])) if kind == 'and' else any((bits[0], not bits[1], bits[2]))
            assert clauses_hold(em, values) == (bits[3] == want)
            checks += 1
    return checks


def shared_count_checks():
    checks = 0
    # Include empty/constant lists, repeated and complementary literals,
    # offsets above the requested maximum and requested levels above length.
    for pattern in range(5):
        em = encode.CNF()
        x = [em.var() for _ in range(5)]
        inputs = (x if pattern == 0 else x+[-x[0], x[1], True, False] if pattern == 1
                  else [True]*6+x if pattern == 2 else [False, True] if pattern == 3 else [])
        output = encode.count_thresholds(em, inputs, 7)
        for bits in product((False, True), repeat=5):
            values = em.extend(dict(zip(x, bits)))
            count = sum(encode.truth(v, values) for v in inputs)
            assert clauses_hold(em, values)
            assert [encode.truth(lit, values) for lit in output] == [count >= j for j in range(8)]
            checks += 1
    return checks


def conditional_cap_checks():
    checks = 0
    for restricted in (False, True):
        em = encode.CNF()
        common = [em.var() for _ in range(5)]
        edge = em.var()
        output = encode.count_thresholds(em, common, 4)
        for kind in ('global', 'adjacent') + (('root',) if restricted else ()):
            encode.common_cap_constraint(em, output, edge, kind)
        for bits in product((False, True), repeat=6):
            count, adjacent = sum(bits[:5]), bits[5]
            values = em.extend(dict(zip(common+[edge], bits)))
            want = count <= 3 and (not adjacent or count <= 1) and (not restricted or count <= 2)
            assert clauses_hold(em, values) == want, (restricted, bits)
            checks += 1
    return checks


def lex_checks():
    checks = 0
    for width in (0, 1, 4, 13):
        em = encode.CNF()
        left, right = [[em.var() for _ in range(width)] for _ in range(2)]
        encode.lex_nonincreasing(em, left, right)
        if width < 13:
            cases = product((False, True), repeat=2*width)
        else:
            cases = [tuple([False]*(2*width)), tuple([True]*(2*width))]
            for first_difference in range(width):
                prefix = [bool(i % 2) for i in range(first_difference)]
                a = prefix+[True]+[False]*(width-first_difference-1)
                b = prefix+[False]+[True]*(width-first_difference-1)
                cases += [tuple(a+b), tuple(b+a)]
        for bits in cases:
            a, b = tuple(bits[:width]), tuple(bits[width:])
            values = em.extend(dict(zip(left+right, bits)))
            assert clauses_hold(em, values) == (a >= b), (width, a, b)
            checks += 1
    return checks


def circulant_degree_fixture():
    """8-regular circulant on61, roots0/8; not a diameter2 target."""
    edges = {(min(x, (x+d) % 61), max(x, (x+d) % 61))
             for x in range(61) for d in (1, 4, 7, 10)}
    adj = [set() for _ in range(61)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    s = sorted(adj[0] & adj[8])
    u, v = sorted(adj[0]-set(s)), sorted(adj[8]-set(s))
    assert s == [1, 4, 7] and len(u) == len(v) == 5 and 8 not in adj[0]
    parents = s+u+v
    remaining = set(range(61))-set([0, 8]+parents)
    r = sorted(remaining, key=lambda x: tuple(int(p in adj[x]) for p in parents), reverse=True)
    old_to_new = {old: new for new, old in enumerate([0, 8]+parents+r)}
    renamed = sorted((min(old_to_new[a], old_to_new[b]), max(old_to_new[a], old_to_new[b]))
                     for a, b in edges)
    return dict(n=61, edges=renamed)


def compare(model, data, label):
    direct = check.inspect(data)
    assert direct['fixed_branch_structure'], label
    values = encode.assignment(model, data)
    rejected = encode.rejected_groups(model, values)
    expected = sorted(name for name, passed in direct['groups'].items() if not passed)
    assert rejected == expected, (label, rejected, expected)
    for ab, lit in model['full_edges'].items():
        assert encode.truth(lit, values) == (ab in direct['original_edges']), ('adjacency', label, ab)
        common_count = sum(encode.truth(x, values) for x in model['common_terms'][ab])
        assert common_count == direct['common'][ab], ('common count', label, ab)
        for j, threshold in enumerate(model['thresholds'][ab]):
            assert encode.truth(threshold, values) == (direct['common'][ab] >= j), ('threshold', label, ab, j)
        assert encode.truth(model['covered'][ab], values) == direct['covered'][ab], ('coverage', label, ab)
    return dict(label=label, rejected_groups=rejected, original_edges=direct['edges'],
                degree_group_passed=direct['groups']['all_original_degrees_8'],
                covered_pairs=sum(direct['covered'].values()),
                fixed_branch_structure=True, target_candidate=False)


def main():
    counters = counter_checks()
    shared = shared_count_checks()
    caps = conditional_cap_checks()
    lex = lex_checks()
    model = encode.build()  # In memory only; no formal preparation.
    assert len(model['full_edges']) == len(model['covered']) == len(model['thresholds']) == 1830
    cases = []
    fixed, free = model['fixed'], set(model['free'])
    cases.append(compare(model, dict(n=61, edges=sorted(fixed)), 'all-free-edges-absent'))
    rng = random.Random(610219)
    for density, label in ((0.06, 'sparse-actual-assignment'), (0.65, 'dense-actual-assignment')):
        edges = fixed | {ab for ab in sorted(free) if rng.random() < density}
        cases.append(compare(model, dict(n=61, edges=sorted(edges)), label))
    fixture = circulant_degree_fixture()
    cases.append(compare(model, fixture, '8-regular-circulant-roots-0-8-sorted-R'))
    assert cases[-1]['degree_group_passed']
    assert 'R_parent_vectors_nonincreasing_lex' not in cases[-1]['rejected_groups']
    # Reverse the R names only: same graph degrees, an explicitly bad lex order.
    rename = {x: x if x < 15 else 75-x for x in range(61)}
    reverse = dict(n=61, edges=sorted((min(rename[a], rename[b]), max(rename[a], rename[b]))
                                    for a, b in fixture['edges']))
    cases.append(compare(model, reverse, 'same-8-regular-graph-reversed-R-names'))
    assert cases[-1]['degree_group_passed'] and 'R_parent_vectors_nonincreasing_lex' in cases[-1]['rejected_groups']
    negative = check.inspect(fixture, include_bfs=True)
    assert not negative['target61_verified'] and negative['pairs_beyond_two']
    assert negative['uv_nonadjacent_double'] and negative['root_triangle_counts'] == [0, 0]
    assert not negative['groups']['selected_roots_no_other_double']
    result = dict(status='PASSED', solver_calls=0, counter_gate_truth_assignments=counters,
                  shared_threshold_assignments=shared, conditional_cap_assignments=caps,
                  lex_assignments=lex, assignment_cases=cases, original_pairs_per_case=1830,
                  in_memory_variables=model['em'].nv, in_memory_clauses=len(model['em'].clauses),
                  primary_edge_variables=model['primary_count'], fixed_original_edges=len(fixed),
                  formal_input_written=False, complete_positive_example_available=False,
                  circulant_bfs_diameter=negative['bfs_diameter'],
                  note='All groups and all1830 actual adjacency/common-count/threshold/coverage values '
                       'agree with independent integer checks on five graph assignments. '
                       'The circulant certifies only fixed root structure and degree8; '
                       'it fails diameter2 and isolated-double requirements. No target is claimed.')
    (HERE/'sanity.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
