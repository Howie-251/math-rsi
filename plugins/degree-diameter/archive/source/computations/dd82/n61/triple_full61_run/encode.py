"""Prepare/decode the full order61 triple-defect template; never run a solver.

All 1830 adjacency pairs are primary variables. Necessary layer constraints
are added to degree eight and genuine distance-at-most-two clauses. The two
port-position cases share one CNF; no C, sigma, or simple-B model is selected.
Use runner.py for bounded execution. Preparation has not run at source delivery.
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
U, V = tuple(range(7, 11)), tuple(range(11, 15))
TA, TB = tuple(range(15, 20)), tuple(range(20, 25))
TC, TD = tuple(range(25, 31)), tuple(range(31, 37))
Z, F = tuple(range(37, 61)), tuple(range(37, 41))
LAYERS = dict(u=[0], v=[1], w=[2], S=[3, 4, 5, 6], U=U, V=V,
              Ta=TA, Tb=TB, Tc=TC, Td=TD, Z=Z)
SCOPE = ('Necessary full61 template for every actual connected weighted-defect '
         'graph having a triple entry, up to the documented vertex labels; '
         'no fixed C/sigma, no B simplicity, and no B-connectivity constraint')


def save(path, value):
    path.write_text(json.dumps(value, indent=2) + '\n')


def pair(u, v):
    assert u != v
    return (u, v) if u < v else (v, u)


def load_helpers():
    # Import definitions only. The historical module's guarded main and
    # ABEncoder are never called; its n62 constants/branches are not used.
    spec = importlib.util.spec_from_file_location('triple61_generic_cnf', HELPER)
    helper = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = helper
    spec.loader.exec_module(helper)
    return helper


def fixed_adjacencies():
    fixed, reasons = {}, {}

    def set_edge(u, v, value, reason):
        uv = pair(u, v)
        assert uv not in fixed or fixed[uv] == value, (uv, reasons.get(uv), reason)
        fixed[uv] = value
        reasons.setdefault(uv, reason)

    neighborhoods = {
        0: {3, 4, 5, 6, *U},
        1: {3, 4, 5, 6, *V},
        2: {3, 4, TC[0], TD[0], *F},
        3: {0, 1, 2, *TA},
        4: {0, 1, 2, *TB},
        5: {0, 1, *TC},
        6: {0, 1, *TD},
    }
    for u, neighbors in neighborhoods.items():
        assert len(neighbors) == 8 and u not in neighbors
        for v in range(N):
            if v != u:
                set_edge(u, v, int(v in neighbors), 'complete inherited neighborhood')
    for layer in (U, V, TA, TB, TC, TD):
        for u, v in combinations(layer, 2):
            set_edge(u, v, 0, 'independent layer: triangle-free S parents and u/v')
    for u in U + V:
        for v in TA + TB + TC + TD:
            set_edge(u, v, 0, 'T layers have one S parent and no U/V neighbor')
    for left, right, offset, reason in (
        (U, V, 0, 'normalize the actual U-V perfect matching'),
        (TA, TB, 0, 'normalize the actual Ta-Tb perfect matching'),
        (TA, TC, 1, 'label the five non-special Tc points by the Ta-Tc bijection'),
        (TA, TD, 1, 'independently label non-special Td by the Ta-Td bijection'),
    ):
        for i, u in enumerate(left):
            for j, v in enumerate(right):
                set_edge(u, v, int(j == i + offset), reason)
    for u in TB:
        for v in (TC[0], TD[0]):
            set_edge(u, v, 0, 'gamma/delta have no Ta or Tb neighbor')
    # Layer-interface lemma 4: each F point is adjacent to w with B_wz=0.
    # It has no other neighbor in N(w), so F is independent and avoids gamma/delta.
    for u, v in combinations(F, 2):
        set_edge(u, v, 0, 'F independent: actual B_wz=0 on the w edges')
    for u in F:
        for v in (TC[0], TD[0]):
            set_edge(u, v, 0, 'F avoids gamma/delta by the same w triangle restriction')
    return fixed, reasons


def prepare():
    start_cpu, start_wall = time.process_time(), time.monotonic()
    assert not (HERE / 'input.cnf').exists(), 'Preserve the already generated CNF'
    assert not (HERE / 'encoding.json').exists(), 'Preserve the existing encoding record'
    helper = load_helpers()
    em = helper.CNFEmitter(HERE / 'input.cnf')
    edges = {uv: em.new_var('A_edge') for uv in combinations(range(N), 2)}
    assert len(edges) == em.variable_count == 1830
    case_ii = em.new_var('port_position_case_II')
    groups, degree_records = [], []

    def edge(u, v):
        return edges[pair(u, v)]

    def mark(name, before):
        groups.append(dict(name=name, first_clause=before + 1,
                           last_clause=em.clause_count, clauses=em.clause_count - before))

    def degree(u, vertices, target, condition=None, reason=''):
        """Exact count, optionally required when one signed case literal holds."""
        vertices = tuple(v for v in vertices if v != u)
        literals = [edge(u, v) for v in vertices]
        before = em.clause_count
        if condition is None:
            helper.enforce_exact(em, literals, target, 'exact_degree_threshold')
        else:
            thresholds = helper.unary_thresholds(
                em, literals, min(len(literals), target + 1), 'conditional_layer_threshold')
            helper.enforce_exact_under_condition(em, [condition], thresholds,
                                                 target, len(literals))
        degree_records.append(dict(vertex=u, neighbors=vertices, target=target,
                                   condition=condition, reason=reason,
                                   first_clause=before + 1, last_clause=em.clause_count))

    try:
        fixed, reasons = fixed_adjacencies()
        before = em.clause_count
        for (u, v), value in sorted(fixed.items()):
            em.add_clause(edge(u, v) if value else -edge(u, v))
        mark('fixed_actual_neighborhoods_and_proved_label_normalizations', before)

        before = em.clause_count
        for u in range(N):
            degree(u, range(N), 8, reason='all original graph vertices have degree eight')
        mark('all_61_exact_degrees', before)

        before = em.clause_count
        for z in Z:
            degree(z, U, 1, reason='Z has exactly one U neighbor')
            degree(z, V, 1, reason='Z has exactly one V neighbor')
        for u in U + V:
            degree(u, Z, 6, reason='one root neighbor and one matching neighbor leave six Z neighbors')
        for t in TA + TB:
            for layer in (TC, TD):
                degree(t, layer, 1, reason='each Ta/Tb-to-Tc/Td interface is a proved bijection')
            degree(t, Z, 4, reason='Ta/Tb layer-degree table')
        for t in TC + TD:
            degree(t, TB, int(t not in (TC[0], TD[0])),
                   reason='Tb bijections stay free on the five non-special points')
        for z in Z:
            for layer in (TA, TB):
                degree(z, layer, int(z not in F), reason='d_Ta(z)=d_Tb(z)=1-A_wz')
        mark('unconditional_proved_layer_degrees', before)

        before = em.clause_count
        # Case I: r=Z0, s=Z1 by relabeling F. Case II: r=delta, s=gamma.
        # F has no preassigned U/V port labels, so this uses no C/sigma choice.
        for is_ii in (False, True):
            guard = case_ii if is_ii else -case_ii
            for i, t in enumerate(TC):
                degree(t, TD, 1 + int(is_ii and i == 0), guard,
                       'Tc/Td interface: row gamma has degree two only in Case II')
                degree(t, Z, 4 + int(not is_ii and i == 0), guard,
                       'Tc-to-Z degree from the exact c/d rows')
            for i, t in enumerate(TD):
                degree(t, TC, 1 + int(is_ii and i == 0), guard,
                       'Tc/Td interface: column delta has degree two only in Case II')
                degree(t, Z, 4 + int(not is_ii and i == 0), guard,
                       'Td-to-Z degree from the exact c/d rows')
            for z in Z:
                is_r = not is_ii and z == Z[0]
                is_s = not is_ii and z == Z[1]
                degree(z, TC, 1 + int(is_r), guard, 'd_Tc(z)=1+[z=r]')
                degree(z, TD, 1 + int(is_s), guard, 'd_Td(z)=1+[z=s]')
                degree(z, Z, 2 + int(z in F) - int(is_r) - int(is_s), guard,
                       'd_Z(z)=2+A_wz-[z=r]-[z=s]')
        mark('both_port_position_cases', before)

        before = em.clause_count
        coverage = []
        for u, v in combinations(range(N), 2):
            first = em.variable_count + 1
            paths = []
            for w in range(N):
                if w in (u, v):
                    continue
                out = em.new_var('actual_two_edge_path')
                helper.add_iff_and(em, out, edge(u, w), edge(w, v))
                paths.append(out)
            assert len(paths) == 59
            em.add_clause(edge(u, v), *paths)
            coverage.append(dict(pair=[u, v], direct=edge(u, v), first_path_variable=first,
                                 path_count=59, coverage_clause=em.clause_count))
        mark('all_actual_two_edge_paths_and_all_1830_pair_coverage', before)
        assert len(coverage) == 1830 and em.kind_counts['actual_two_edge_path'] == 107970
        em.finish()
    except BaseException:
        em.abort()
        raise

    save(HERE / 'edge_variables.json', dict(format=['u', 'v', 'variable'],
                                          rows=[[u, v, q] for (u, v), q in edges.items()]))
    save(HERE / 'degree_constraints.json', degree_records)
    save(HERE / 'coverage.json', dict(path_order='increasing actual middle w, omitting the two endpoints',
                                     records=coverage))
    result = dict(status='PREPARED_NOT_RUN', solver_calls=0, scope=SCOPE, n=N,
                  layers=LAYERS, F=F, gamma=TC[0], delta=TD[0], case_II_variable=case_ii,
                  case_I_ports=dict(r=Z[0], s=Z[1]), case_II_ports=dict(r=TD[0], s=TC[0]),
                  variables=em.variable_count, clauses=em.clause_count,
                  primary_edge_variables=1830, variable_kinds=em.kind_counts,
                  clause_groups=groups, degree_constraints=len(degree_records),
                  fixed_adjacencies=[dict(pair=[u, v], value=fixed[u, v], reason=reasons[u, v])
                                     for u, v in sorted(fixed)],
                  all_pair_coverage_count=1830, actual_middle_vertices_per_pair=59,
                  cnf_bytes=(HERE / 'input.cnf').stat().st_size,
                  helper_reuse='CNFEmitter, enforce_exact, unary_thresholds, enforce_exact_under_condition, add_iff_and only; no n62 branch execution',
                  mathematical_dependencies=['proofs/dd82/n61/CONNECTED_TRIPLE_REPEAT_LOCAL.md',
                                             'proofs/dd82/n61/CONNECTED_TRIPLE_LAYER_INTERFACES.md'],
                  source_review_status='pending independent source review at initial delivery',
                  layer_derivation_review_status='root-managed; no acceptance claimed by this implementation',
                  preparation_cpu_seconds=time.process_time() - start_cpu,
                  preparation_wall_seconds=time.monotonic() - start_wall)
    save(HERE / 'encoding.json', result)
    print(json.dumps({k: result[k] for k in ('status', 'variables', 'clauses', 'primary_edge_variables',
                     'cnf_bytes', 'preparation_cpu_seconds', 'preparation_wall_seconds')}, indent=2))


def decode(log_path):
    """Validate every emitted clause, then save the full SAT graph and assignment."""
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
            if not any(values[abs(q)] == (q > 0) for q in literals[:-1]):
                false_ids.append(count)
    assert header == ['p', 'cnf', str(enc['variables']), str(enc['clauses'])]
    assert count == enc['clauses']
    save(HERE / 'model_check.json', dict(assigned_variables=len(values), clauses_checked=count,
                                       false_clause_ids=false_ids, all_clauses_satisfied=not false_ids))
    assert not false_ids
    mapping = json.loads((HERE / 'edge_variables.json').read_text())['rows']
    assert {(u, v) for u, v, q in mapping} == set(combinations(range(N), 2))
    edges = [(u, v) for u, v, q in mapping if values[q]]
    assert len(edges) == 244
    case = 'II' if values[enc['case_II_variable']] else 'I'
    save(HERE / 'candidate.json', dict(n=N, edges=edges, port_position_case=case,
                                      source_solver_log=str(log_path),
                                      status='SAT_CANDIDATE_PENDING_INDEPENDENT_BFS'))
    (HERE / 'candidate.edges').write_text('61 244\n' + ''.join(f'{u} {v}\n' for u, v in edges))
    with (HERE / 'model.assignment.txt').open('w') as output:
        for start in range(1, enc['variables'] + 1, 100):
            signed = [q if values[q] else -q for q in range(start, min(start + 100, enc['variables'] + 1))]
            output.write('v ' + ' '.join(map(str, signed)) + ' 0\n')
    print(json.dumps(dict(status='SAT_CANDIDATE_PENDING_INDEPENDENT_BFS', n=N,
                          edges=len(edges), port_position_case=case), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode'))
    parser.add_argument('--log', type=Path, default=HERE / 'solver.log')
    args = parser.parse_args()
    prepare() if args.action == 'prepare' else decode(args.log)
