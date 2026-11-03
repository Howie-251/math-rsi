"""Prepare/decode the order61 adjacent-double CNF with proven port counts.

All 1830 actual adjacency pairs and all 107970 actual two-edge paths are
represented. Seven selectors retain every independent U/V type of C=I+P.
The original full61 CNF is retained as a prefix, followed by additional
actual-B port equations and proven S/T-parent independence clauses.
"""
import argparse
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
HELPER = ROOT / 'context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/code/n62/n62_ab_cnf.py'
N = 61
u, v, s, t = 0, 1, 2, 3
U, V = tuple(range(4, 9)), tuple(range(9, 14))
S, T = tuple(range(14, 20)), tuple(range(20, 26))
q, p = S[0], T[0]
Z = tuple(range(26, 61))
LAYERS = dict(u=[u], v=[v], s=[s], t=[t], U=U, V=V, S=S, T=T, Z=Z)
CYCLE_PARTITIONS = ((5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1),
                    (2, 1, 1, 1), (1, 1, 1, 1, 1))
SCOPE = ('Necessary full61 template for every actual degree8 diameter2 graph '
         'with an adjacent double defect, using inherited connected defect '
         'and B<=2, plus proved port propagation; all seven C types, '
         'no fixed S-T pattern or q transversal')


def save(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def pair(a, b):
    assert a != b
    return (a, b) if a < b else (b, a)


def load_helpers():
    # Import generic definitions only: no ABEncoder or historical main call.
    spec = importlib.util.spec_from_file_location('adjacent_double_ports61_generic_cnf', HELPER)
    helper = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = helper
    spec.loader.exec_module(helper)
    return helper


def c_types():
    """Canonical multigraph types; return their exact 35 Z-to-V parents."""
    cases = []
    for partition in CYCLE_PARTITIONS:
        sigma = list(range(5))
        start = 0
        for length in partition:
            for i in range(start, start + length):
                sigma[i] = start + (i - start + 1) % length
            start += length
        assert start == 5 and sorted(sigma) == list(range(5))
        C = [[int(i == j) + int(sigma[i] == j) for j in range(5)] for i in range(5)]
        H = [[1 + entry for entry in row] for row in C]
        assert [sum(row) for row in C] == [2] * 5
        assert [sum(C[i][j] for i in range(5)) for j in range(5)] == [2] * 5
        parents = []
        for row in H:
            row_parents = [V[j] for j, count in enumerate(row) for _ in range(count)]
            assert len(row_parents) == 7
            parents.extend(row_parents)
        assert len(parents) == 35
        cases.append(dict(name='+'.join(map(str, partition)), cycle_partition=partition,
                          sigma=sigma, C=C, H=H, Z_to_V_parent=parents))
    return cases


def fixed_adjacencies():
    fixed, reasons = {}, {}

    def set_edge(a, b, value, reason):
        ab = pair(a, b)
        assert ab not in fixed or fixed[ab] == value, (ab, reasons.get(ab), reason)
        fixed[ab] = value
        reasons.setdefault(ab, reason)

    neighborhoods = {u: {v, s, t, *U}, v: {u, s, t, *V},
                     s: {u, v, *S}, t: {u, v, *T}}
    for a, neighbors in neighborhoods.items():
        assert len(neighbors) == 8 and a not in neighbors
        for b in range(N):
            if b != a:
                set_edge(a, b, int(b in neighbors), 'complete proven core neighborhood')
    for layer in (U, V, S, T):
        for a, b in combinations(layer, 2):
            set_edge(a, b, 0, 'independent layer: local proof section 2')
    for a in U:
        for b in V:
            set_edge(a, b, 0, 'A[U,V]=0 from Ag=5f')
    for a in U + V:
        for b in S + T:
            set_edge(a, b, 0, 'S/T points have no U/V adjacency')
    for i, a in enumerate(U):
        for k, z in enumerate(Z):
            set_edge(a, z, int(k // 7 == i), 'Z labels grouped by their unique U parent')
    return fixed, reasons


def fixed_defects():
    """Values of the ACTUAL B=A²+A-7I-J; no independent B variables."""
    fixed, reasons = {}, {}

    def set_defect(a, b, value, reason):
        ab = pair(a, b)
        assert ab not in fixed or fixed[ab] == value, (ab, reasons.get(ab), reason)
        fixed[ab] = value
        reasons.setdefault(ab, reason)

    core_rows = {u: {v: 2, s: 1, t: 1}, v: {u: 2, s: 1, t: 1},
                 s: {u: 1, v: 1, t: 1, p: 1},
                 t: {u: 1, v: 1, s: 1, q: 1}}
    for a, row in core_rows.items():
        assert sum(row.values()) == 4
        for b in range(N):
            if b != a:
                set_defect(a, b, row.get(b, 0), 'complete core B row, equations (2),(3)')
    for layer in (U, V):
        for a, b in combinations(layer, 2):
            set_defect(a, b, 0, 'B[U]=B[V]=0, equation (5)')
    for a in U + V:
        for z in Z:
            set_defect(a, z, 0, 'B[U/V,Z]=0, equation (7)')
        for b in (q, p):
            set_defect(a, b, 0, 'p/q have no U/V defect, equation (7)')
    for i, a in enumerate(U):
        for layer in (S[1:], T[1:]):
            for j, b in enumerate(layer):
                set_defect(a, b, int(i == j), 'ordinary S/T labels by their unique U defect endpoint')
    return fixed, reasons


def prepare():
    start_cpu, start_wall = time.process_time(), time.monotonic()
    assert not (HERE / 'input.cnf').exists(), 'Preserve the already generated CNF'
    assert not (HERE / 'encoding.json').exists(), 'Preserve the existing encoding record'
    helper = load_helpers()
    em = helper.CNFEmitter(HERE / 'input.cnf')
    edges = {ab: em.new_var('A_edge') for ab in combinations(range(N), 2)}
    assert len(edges) == em.variable_count == 1830
    cases = c_types()
    for case in cases:
        case['selector_variable'] = em.new_var('C_type_selector')
    groups, degree_records, coverage, defect_records = [], [], [], []
    port_pairs = {pair(a, b) for a in S for b in T}
    port_pairs.update(pair(a, z) for a in S + T for z in Z)
    assert len(port_pairs) == 456
    port_bits, port_third_thresholds, port_count_records = {}, {}, []

    def edge(a, b):
        return edges[pair(a, b)]

    def mark(name, before):
        groups.append(dict(name=name, first_clause=before + 1,
                           last_clause=em.clause_count, clauses=em.clause_count - before))

    def degree(a, vertices, target, reason, condition=None):
        vertices = tuple(b for b in vertices if b != a)
        before = em.clause_count
        literals = [edge(a, b) for b in vertices]
        if condition is None:
            helper.enforce_exact(em, literals, target, 'exact_degree_threshold')
        else:
            thresholds = helper.unary_thresholds(
                em, literals, min(len(literals), target + 1), 'conditional_fiber_threshold')
            helper.enforce_exact_under_condition(em, [condition], thresholds, target, len(literals))
        degree_records.append(dict(vertex=a, neighbors=vertices, target=target, reason=reason,
                                   condition=condition, first_clause=before + 1, last_clause=em.clause_count))

    def port_bit(a, b):
        return port_bits[pair(a, b)]

    def port_count(a, vertices, reason, target=None, guard=None,
                   target_if_true=None, target_if_false=None):
        """Count exact actual-B unit indicators, already defined by real paths."""
        vertices = tuple(vertices)
        literals = [port_bit(a, b) for b in vertices]
        before = em.clause_count
        if guard is None:
            assert target is not None
            helper.enforce_exact(em, literals, target, 'port_count_threshold')
        else:
            assert target is None and target_if_true is not None and target_if_false is not None
            maximum = min(len(literals), max(target_if_true, target_if_false) + 1)
            thresholds = helper.unary_thresholds(em, literals, maximum, 'guarded_port_count_threshold')
            helper.enforce_exact_under_condition(em, [guard], thresholds, target_if_true, len(literals))
            helper.enforce_exact_under_condition(em, [-guard], thresholds, target_if_false, len(literals))
        port_count_records.append(dict(vertex=a, other_vertices=vertices, actual_B_unit_literals=literals,
                                       target=target, guard=guard, target_if_true=target_if_true,
                                       target_if_false=target_if_false, reason=reason,
                                       first_clause=before + 1, last_clause=em.clause_count))

    try:
        fixed, fixed_reasons = fixed_adjacencies()
        defects, defect_reasons = fixed_defects()
        assert not port_pairs.intersection(defects)
        before = em.clause_count
        for (a, b), value in sorted(fixed.items()):
            em.add_clause(edge(a, b) if value else -edge(a, b))
        mark('fixed_actual_neighborhoods_and_U_parent_labels', before)

        before = em.clause_count
        selectors = [case['selector_variable'] for case in cases]
        em.add_clause(*selectors)
        for left, right in combinations(selectors, 2):
            em.add_clause(-left, -right)
        for case in cases:
            selector = case['selector_variable']
            for z, parent in zip(Z, case['Z_to_V_parent']):
                for b in V:
                    literal = edge(z, b) if b == parent else -edge(z, b)
                    em.add_clause(-selector, literal)
        mark('exactly_one_of_all_seven_C_types_and_its_actual_V_parents', before)

        before = em.clause_count
        for a in range(N):
            degree(a, range(N), 8, 'all original graph vertices have degree eight')
        mark('all_61_exact_degrees', before)

        before = em.clause_count
        for z in Z:
            for layer_name, layer in (('U', U), ('V', V), ('S', S), ('T', T)):
                degree(z, layer, 1, 'Z has exactly one ' + layer_name + ' neighbor')
            degree(z, Z, 4, 'A[Z] is four-regular, equation (9)')
        for a in U + V:
            degree(a, Z, 7, 'one core parent leaves seven Z neighbors')
        for a in S:
            degree(a, T, 1 + int(a == q), 'S-T interface: only q row has degree two')
            degree(a, Z, 6 - int(a == q), 'S layer degree table')
        for a in T:
            degree(a, S, 1 + int(a == p), 'S-T interface: only p column has degree two')
            degree(a, Z, 6 - int(a == p), 'T layer degree table')
        mark('all_proven_layer_degrees_with_unfixed_S_T_pattern', before)

        before = em.clause_count
        for i in range(5):
            fiber = Z[7 * i:7 * (i + 1)]
            for a in (p, q):
                degree(a, fiber, 1, 'p/q transversal of U fibers: actual B(U_i,p/q)=0')
            for layer in (S[1:], T[1:]):
                for j, a in enumerate(layer):
                    degree(a, fiber, 1 + int(i == j),
                           'ordinary S/T fiber count: actual B(U_i,S_j/T_j)=delta_ij')
        for case in cases:
            for b in V:
                fiber = tuple(z for z, parent in zip(Z, case['Z_to_V_parent']) if parent == b)
                assert len(fiber) == 7
                for a in (p, q):
                    degree(a, fiber, 1, 'p/q transversal of actual selected V fibers',
                           condition=case['selector_variable'])
        mark('redundant_actual_U_fiber_counts_and_selected_V_transversals', before)

        before = em.clause_count
        for k, z in enumerate(Z):
            for i in range(5):
                degree(z, Z[7 * i:7 * (i + 1)], int(i != k // 7),
                       'actual B(U_i,z)=0 gives d_U_fiber_i(z)=1-A_Ui,z')
        for case in cases:
            for z, parent in zip(Z, case['Z_to_V_parent']):
                for b in V:
                    fiber = tuple(w for w, other_parent in zip(Z, case['Z_to_V_parent'])
                                  if other_parent == b)
                    degree(z, fiber, int(parent != b),
                           'actual B(V_j,z)=0 gives d_V_fiber_j(z)=1-A_Vj,z',
                           condition=case['selector_variable'])
        mark('redundant_actual_Z_matching_degrees_between_U_and_selected_V_fibers', before)

        before = em.clause_count
        for a, b in combinations(range(N), 2):
            first = em.variable_count + 1
            paths = []
            for w in range(N):
                if w in (a, b):
                    continue
                out = em.new_var('actual_two_edge_path')
                helper.add_iff_and(em, out, edge(a, w), edge(w, b))
                paths.append(out)
            assert len(paths) == 59
            actual_count_inputs = [edge(a, b), *paths]
            em.add_clause(*actual_count_inputs)
            coverage.append(dict(pair=[a, b], direct=edge(a, b), first_path_variable=first,
                                 path_count=59, coverage_clause=em.clause_count))
            first_count_clause = em.clause_count + 1
            if (a, b) in defects:
                defect = defects[a, b]
                helper.enforce_exact(em, actual_count_inputs, 1 + defect, 'actual_B_exact_threshold')
                record = dict(pair=[a, b], actual_B=defect, mode='exact',
                              target_mu_plus_A=1 + defect, reason=defect_reasons[a, b])
            else:
                # Coverage gives mu+A >= 1; inherited B<=2 gives mu+A <= 3.
                thresholds = helper.unary_thresholds(em, actual_count_inputs, 4, 'actual_B_upper_threshold')
                assert thresholds[3] is not None
                em.add_clause(-thresholds[3])
                if (a, b) in port_pairs:
                    # Read existing equivalence thresholds without changing
                    # any original variable or clause. Later c<=2 makes
                    # threshold(c>=2) precisely actual B=c-1 in {0,1}.
                    assert thresholds[1] is not None and thresholds[2] is not None
                    port_bits[a, b] = thresholds[1]
                    port_third_thresholds[a, b] = thresholds[2]
                record = dict(pair=[a, b], mode='upper', maximum_mu_plus_A=3,
                              reason='inherited actual B<=2; no independent B selector')
            record.update(first_clause=first_count_clause, last_clause=em.clause_count)
            defect_records.append(record)
        mark('all_actual_paths_all_pair_coverage_and_actual_B_counts', before)
        assert len(coverage) == len(defect_records) == 1830
        assert em.kind_counts['actual_two_edge_path'] == 107970
        baseline_prefix = dict(variables=em.variable_count, clauses=em.clause_count,
                               source_directory='computations/dd82/n61/adjacent_double_full61_run',
                               relationship='Every baseline variable and clause is retained in its original order')
        assert set(port_bits) == set(port_third_thresholds) == port_pairs

        before = em.clause_count
        strengthened = {}
        for ab in sorted(port_pairs):
            em.add_clause(-port_third_thresholds[ab])
            strengthened[ab] = em.clause_count
        for record in defect_records:
            ab = tuple(record['pair'])
            if ab in port_pairs:
                record.update(baseline_maximum_mu_plus_A=3, maximum_mu_plus_A=2,
                              actual_B_unit_variable=port_bits[ab],
                              strengthened_upper_clause=strengthened[ab])
        mark('actual_S_T_and_S_T_Z_defects_are_units_using_existing_path_thresholds', before)

        before = em.clause_count
        for a in S:
            port_count(a, T, 'P=B[S,T] has row sum one, local equation (11)', target=1)
        for b in T:
            port_count(b, S, 'P=B[S,T] has column sum one, local equation (11)', target=1)
        mark('actual_P_permutation_row_and_column_counts', before)

        before = em.clause_count
        for a in S:
            for b in T:
                if (a, b) != (q, p):
                    em.add_clause(-edge(a, b), -port_bit(a, b))
        mark('K_P_overlap_only_at_q_p', before)

        before = em.clause_count
        for z in Z:
            port_count(z, S, 'sum_S B_xz=A_pz, local equation (14)',
                       guard=edge(p, z), target_if_true=1, target_if_false=0)
            port_count(z, T, 'sum_T B_yz=A_qz, local equation (14)',
                       guard=edge(q, z), target_if_true=1, target_if_false=0)
        for a in S:
            base_count = 1 + int(a == q)
            port_count(a, Z, 'sum_Z B_xz=1+[x=q]-A_xp, local equation (16)',
                       guard=edge(a, p), target_if_true=base_count-1, target_if_false=base_count)
        for b in T:
            base_count = 1 + int(b == p)
            port_count(b, Z, 'sum_Z B_yz=1+[y=p]-A_yq, local equation (16)',
                       guard=edge(b, q), target_if_true=base_count-1, target_if_false=base_count)
        mark('actual_S_T_Z_port_column_and_row_equations', before)

        before = em.clause_count
        for a in S + T:
            for left, right in combinations(Z, 2):
                em.add_clause(-edge(a, left), -edge(a, right), -edge(left, right))
        mark('all_actual_S_T_parent_classes_are_independent_in_Z', before)
        em.finish()
    except BaseException:
        em.abort()
        raise

    save(HERE / 'edge_variables.json', dict(format=['u', 'v', 'variable'],
                                          rows=[[a, b, var] for (a, b), var in edges.items()]))
    save(HERE / 'degree_constraints.json', degree_records)
    save(HERE / 'coverage.json', dict(path_order='increasing actual middle w, omitting endpoints',
                                     records=coverage))
    save(HERE / 'defect_constraints.json', dict(definition='actual B_ab=mu(a,b)+A_ab-1',
                                               records=defect_records))
    save(HERE / 'port_constraints.json', dict(
        unit_definition='Existing threshold(mu+A>=2), with appended mu+A<=2 and baseline mu+A>=1',
        unit_pairs=[dict(pair=list(ab), actual_B_unit_variable=port_bits[ab],
                         existing_third_threshold=port_third_thresholds[ab],
                         strengthened_upper_clause=strengthened[ab]) for ab in sorted(port_pairs)],
        count_records=port_count_records, overlap_exception=[q, p],
        independent_parent_vertices=S+T, independence_clauses=len(S+T)*len(Z)*(len(Z)-1)//2))
    result = dict(status='PREPARED_NOT_RUN', solver_calls=0, scope=SCOPE, n=N,
                  layers=LAYERS, p=p, q=q, C_types=cases,
                  baseline_prefix=baseline_prefix,
                  added_variables=em.variable_count-baseline_prefix['variables'],
                  added_clauses=em.clause_count-baseline_prefix['clauses'],
                  variables=em.variable_count, clauses=em.clause_count,
                  primary_edge_variables=1830, variable_kinds=em.kind_counts,
                  clause_groups=groups, degree_constraints=len(degree_records),
                  fixed_adjacencies=[dict(pair=[a, b], value=fixed[a, b], reason=fixed_reasons[a, b])
                                     for a, b in sorted(fixed)],
                  exact_actual_B_pairs=len(defects), upper_only_actual_B_pairs=1830-len(defects),
                  upper_only_actual_B_unit_pairs=len(port_pairs),
                  upper_only_actual_B_bound_two_pairs=1830-len(defects)-len(port_pairs),
                  reused_actual_B_unit_thresholds=len(port_bits), port_count_constraints=len(port_count_records),
                  all_pair_coverage_count=1830, actual_middle_vertices_per_pair=59,
                  cnf_bytes=(HERE / 'input.cnf').stat().st_size,
                  helper_reuse='CNFEmitter, enforce_exact, unary_thresholds, enforce_exact_under_condition, add_iff_and only; no n62 branch execution',
                  mathematical_dependencies=['proofs/dd82/n61/CONNECTED_TRIPLE_EXCLUSION.md',
                                             'proofs/dd82/n61/ADJACENT_DOUBLE_REPEAT_LOCAL.md',
                                             'proofs/dd82/n61/ADJACENT_DOUBLE_FULL_GRAPH_MODEL.md',
                                             'proofs/dd82/n61/ADJACENT_DOUBLE_PORT_PROPAGATION.md'],
                  intentionally_unencoded=['B double-support path forest',
                                           'B[S]/B[T] variable internal defect edges',
                                           'B support connectivity'],
                  source_review_status='root-managed independent source review; implementation does not attest acceptance',
                  mathematical_review_status='root-managed; implementation does not attest acceptance',
                  preparation_cpu_seconds=time.process_time() - start_cpu,
                  preparation_wall_seconds=time.monotonic() - start_wall)
    save(HERE / 'encoding.json', result)
    print(json.dumps({key: result[key] for key in ('status', 'variables', 'clauses', 'primary_edge_variables',
                     'cnf_bytes', 'preparation_cpu_seconds', 'preparation_wall_seconds')}, indent=2))


def decode(log_path):
    """Validate all actual DIMACS clauses, then save the full graph and case."""
    enc = json.loads((HERE / 'encoding.json').read_text())
    values, sat = {}, False
    with log_path.open() as source:
        for line in source:
            if line.strip() == 's SATISFIABLE':
                sat = True
            if line.startswith('v '):
                for literal in map(int, line.split()[1:]):
                    if literal:
                        var, value = abs(literal), literal > 0
                        assert var not in values or values[var] == value
                        values[var] = value
    assert sat and set(values) == set(range(1, enc['variables'] + 1))
    false_ids, count, header = [], 0, None
    with (HERE / 'input.cnf').open() as source:
        for line in source:
            if not line.strip() or line.startswith('c'):
                continue
            if line.startswith('p '):
                header = line.split()
                continue
            literals = list(map(int, line.split()))
            assert literals[-1] == 0
            count += 1
            if not any(values[abs(var)] == (var > 0) for var in literals[:-1]):
                false_ids.append(count)
    assert header == ['p', 'cnf', str(enc['variables']), str(enc['clauses'])]
    assert count == enc['clauses']
    save(HERE / 'model_check.json', dict(assigned_variables=len(values), clauses_checked=count,
                                       false_clause_ids=false_ids, all_clauses_satisfied=not false_ids))
    assert not false_ids
    mapping = json.loads((HERE / 'edge_variables.json').read_text())['rows']
    assert {(a, b) for a, b, var in mapping} == set(combinations(range(N), 2))
    edges = [(a, b) for a, b, var in mapping if values[var]]
    assert len(edges) == 244
    selected = [case for case in enc['C_types'] if values[case['selector_variable']]]
    assert len(selected) == 1
    selected = selected[0]
    save(HERE / 'candidate.json', dict(n=N, edges=edges, C_type=selected,
                                      source_solver_log=str(log_path),
                                      status='SAT_CANDIDATE_PENDING_INDEPENDENT_BFS'))
    (HERE / 'candidate.edges').write_text('61 244\n' + ''.join(f'{a} {b}\n' for a, b in edges))
    with (HERE / 'model.assignment.txt').open('w') as output:
        for start in range(1, enc['variables'] + 1, 100):
            signed = [var if values[var] else -var
                      for var in range(start, min(start + 100, enc['variables'] + 1))]
            output.write('v ' + ' '.join(map(str, signed)) + ' 0\n')
    print(json.dumps(dict(status='SAT_CANDIDATE_PENDING_INDEPENDENT_BFS', n=N,
                          edges=len(edges), C_type=selected['name']), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode'))
    parser.add_argument('--log', type=Path, default=HERE / 'solver.log')
    args = parser.parse_args()
    prepare() if args.action == 'prepare' else decode(args.log)
