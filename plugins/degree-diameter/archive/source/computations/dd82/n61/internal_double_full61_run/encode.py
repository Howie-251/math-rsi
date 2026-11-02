"""Full original-A internal-double model: prepare/decode, never run a solver.

Three losslessly normalized types retain every original vertex and pair.
Only reviewed generic CNF/assignment helpers are imported; no old encoder
constructor, branch conditions, generator main, or solver action is invoked.
"""
import argparse
from bisect import bisect_left
import importlib.util
from itertools import combinations, product
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
N = 61
V, U_ENDPOINT, W_ENDPOINT = 0, 1, 2
T = tuple(range(3, 11))
Z = tuple(range(11, 61))
CASES = {
    'r0_h1_b0': dict(r=0, h=1, beta=0, free_edges=1086),
    'r1_h0_b0': dict(r=1, h=0, beta=0, free_edges=870),
    'r2_h0_b1': dict(r=2, h=0, beta=1, free_edges=800),
}
SCOPE = ('Complete original-A degree8 diameter2 order61 model with an internal '
         'double-defect vertex, in the selected one of three necessary types; '
         'the three types jointly cover that structural target, conditional '
         'on the cited local reductions and lossless labeling proof')
DEPENDENCIES = [
    'proofs/dd82/n61/INTERNAL_DOUBLE_PATH_LOCAL.md',
    'proofs/dd82/n61/INTERNAL_DOUBLE_PATH_FOLLOWUP.md',
    'proofs/dd82/n61/INTERNAL_DOUBLE_ENDPOINT_ADJACENCY_EXCLUSION.md',
    'proofs/dd82/n61/INTERNAL_DOUBLE_FULL_GRAPH_DESIGN.md',
    'proofs/dd82/n61/INTERNAL_DOUBLE_SHARED_TWO_PORTS.md',
]


def save(path, obj):
    path.write_text(json.dumps(obj, indent=2) + '\n')


def pair(a, b):
    assert a != b
    return (a, b) if a < b else (b, a)


def load_modules():
    sys.dont_write_bytecode = True
    path = ROOT / 'computations/dd82/construction/joint_boundary_completion_run/encode.py'
    spec = importlib.util.spec_from_file_location('internal_double_generic_support', path)
    support = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = support
    spec.loader.exec_module(support)
    return support.load_helpers(), support


def layout(case):
    """No CNF generation: original vertices, all constants, and free pairs."""
    spec = CASES[case]
    r, h, beta = spec['r'], spec['h'], spec['beta']
    U = frozenset(T[:3])
    W = frozenset({0: T[3:6], 1: (T[0], T[3], T[4]),
                   2: (T[0], T[1], T[3])}[r])
    groups, parent, next_label = {}, {}, 11
    for t in T:
        size = 7 - int(t in U) - int(t in W)
        groups[t] = tuple(range(next_label, next_label + size))
        parent.update({z: t for z in groups[t]})
        next_label += size
    assert next_label == N and set(parent) == set(Z)
    neutral = tuple(t for t in T if t not in U | W)
    shared_classes = set(neutral[:h])
    P, Q = set(), set()
    for t, group in groups.items():
        if t not in U:
            P.add(group[0])
        if t not in W:
            Q.add(group[0] if t in U or t in shared_classes else group[1])
    ordinary = {t: tuple(z for z in group if z not in P | Q)
                for t, group in groups.items()}
    assert len(P) == len(Q) == 5 and len(P & Q) == h
    assert len(U & W) == r and r + h == 1 + beta
    fixed, reasons = {}, {}

    def fix(a, b, value, reason):
        ab = pair(a, b)
        value = bool(value)
        assert ab not in fixed or fixed[ab] == value, (ab, reason)
        fixed[ab] = value
        reasons.setdefault(ab, []).append(reason)

    # Every core-incident pair, including its nonedges, is a constant.
    core_edges = {pair(V, t) for t in T}
    core_edges.update(pair(U_ENDPOINT, t) for t in U)
    core_edges.update(pair(W_ENDPOINT, t) for t in W)
    core_edges.update(pair(parent[z], z) for z in Z)
    core_edges.update(pair(U_ENDPOINT, z) for z in P)
    core_edges.update(pair(W_ENDPOINT, z) for z in Q)
    for a, b in combinations(range(N), 2):
        if a < 11:
            fix(a, b, (a, b) in core_edges, 'complete_core_and_attachment_blocks')
    assert len(core_edges) == 74
    for t, group in groups.items():
        for a, b in combinations(group, 2):
            if a in ordinary[t] or b in ordinary[t]:
                fix(a, b, False, 'ordinary_own_color_degree_zero')
    if r:
        for t in sorted(U & W):
            for z in groups[t]:
                for attachment in sorted(P | Q):
                    fix(z, attachment, False, 'shared_parent_B_row_saturation')
        reference = T[0]
        assert reference in U & W and all(len(row) == 5 for row in ordinary.values())
        for t in T:
            if t == reference:
                continue
            for i, a in enumerate(ordinary[reference]):
                for j, b in enumerate(ordinary[t]):
                    fix(a, b, i == j, 'seven_reference_matchings_identity')
    if h:
        shared = next(iter(P & Q))
        for z in sorted((P | Q) - {shared}):
            fix(shared, z, False, 'shared_attachment_B_row_saturation')
    if beta:
        for attachments in (P, Q):
            for a, b in combinations(sorted(attachments), 2):
                fix(a, b, False, 'endpoint_one_remaining_B_unit')
    free_pairs = tuple(ab for ab in combinations(range(N), 2) if ab not in fixed)
    assert len(free_pairs) == spec['free_edges']
    assert all(a in Z and b in Z for a, b in free_pairs)
    assert sum(fixed.values()) == 74 + (35 if r else 0)
    for a in range(11):
        assert all(pair(a, b) in fixed for b in range(N) if a != b)
        assert sum(fixed[pair(a, b)] for b in range(N) if a != b) == 8
    if r:
        for a in groups[T[0]]:
            assert all(pair(a, b) in fixed for b in range(N) if a != b)
            assert sum(fixed[pair(a, b)] for b in range(N) if a != b) == 8
    return dict(case=case, **spec, U=U, W=W, groups=groups, parent=parent,
                P=P, Q=Q, ordinary=ordinary, fixed=fixed, reasons=reasons,
                free_pairs=free_pairs)


def evaluated_emitter(helper, support, output=None, retain=False):
    class EvaluatedEmitter(helper.CNFEmitter):
        def __init__(self):
            super().__init__(output)
            self.values = {}
            self.false_clause_ids = []
            self.constraint_ids = []
            self.defining = True
            self.clauses = [] if retain else None

        def add_clause(self, *literals):
            assert all(type(literal) is int for literal in literals)
            super().add_clause(*literals)
            if self.clauses is not None:
                self.clauses.append(tuple(literals))
            failed = support.evaluate_clause(literals, self.values, self.clause_count)
            if self.defining:
                assert not failed, ('false auxiliary definition', self.clause_count)
            else:
                self.constraint_ids.append(self.clause_count)
            if failed:
                self.false_clause_ids.append(self.clause_count)

    return EvaluatedEmitter()


def neg(literal):
    return not literal if isinstance(literal, bool) else -literal


def require_or(em, terms):
    """One asserted clause, after faithfully folding Boolean constants."""
    if any(term is True for term in terms):
        return
    literals = list(dict.fromkeys(term for term in terms if term is not False))
    em.defining = False
    try:
        em.add_clause(*literals)
    finally:
        em.defining = True


def counter(helper, em, terms, maximum, kind):
    fixed = sum(term is True for term in terms)
    inputs = [term for term in terms if not isinstance(term, bool)]
    maximum = max(0, min(len(inputs), maximum - fixed))
    thresholds = helper.unary_thresholds(em, inputs, maximum, kind)

    def at_least(k):
        k -= fixed
        if k <= 0:
            return True
        if k > len(inputs):
            return False
        assert k <= len(thresholds), (k, len(thresholds), kind)
        return thresholds[k - 1]

    return at_least


def exact_count(helper, em, terms, target, kind):
    threshold = counter(helper, em, terms, target + 1, kind)
    require_or(em, [threshold(target)])
    require_or(em, [neg(threshold(target + 1))])


def defect_count(helper, em, terms, offset):
    """B=sum(actual A literals/constants)+offset, with exact threshold bits."""
    threshold = counter(helper, em, terms, 3 - offset, 'actual_short_B_threshold')
    require_or(em, [threshold(-offset)])
    require_or(em, [neg(threshold(3 - offset))])
    return (threshold(1 - offset), threshold(2 - offset))


def build_model(case, helper, support, output=None):
    data = layout(case)
    fixed = data['fixed']
    em = evaluated_emitter(helper, support, output)
    free = {ab: em.new_var('actual_Z_edge') for ab in data['free_pairs']}
    # This deliberately need not be a valid graph. It tests every emitted
    # definition and each constraint family against actual adjacency data.
    em.values.update({var: ((a * 19 + b * 11 + a * b) % 17 < 3)
                      for (a, b), var in free.items()})
    adjacency = [set() for _ in range(N)]
    for ab in combinations(range(N), 2):
        value = fixed[ab] if ab in fixed else em.values[free[ab]]
        if value:
            a, b = ab
            adjacency[a].add(b)
            adjacency[b].add(a)
    actual_B = {(a, b): len(adjacency[a] & adjacency[b]) + int(b in adjacency[a]) - 1
                for a, b in combinations(range(N), 2)}
    U, W, P, Q = data['U'], data['W'], data['P'], data['Q']
    groups, parent, ordinary = data['groups'], data['parent'], data['ordinary']
    exceptional = tuple(sorted(P | Q))
    records, coverage, path_cache, port_bits = [], [], {}, {}

    def edge(a, b):
        if a == b:
            return False
        ab = pair(a, b)
        return fixed[ab] if ab in fixed else free[ab]

    def defect(a, b):
        return actual_B[pair(a, b)]

    def weight(a, b):
        # For invalid sanity assignments this is the two exact threshold
        # bits' sum. Bounds are separately asserted for every such entry.
        return min(2, max(0, defect(a, b)))

    def record(kind, detail, expected, before):
        records.append(dict(kind=kind, **detail, first_clause=before + 1,
                            last_clause=em.clause_count,
                            sanity_semantic_satisfied=bool(expected)))

    def exact(terms, target, kind, detail, expected):
        before = em.clause_count
        exact_count(helper, em, terms, target, kind + '_threshold')
        record(kind, detail, expected, before)

    def short_defect(a, z, terms, offset, kind):
        before = em.clause_count
        bits = defect_count(helper, em, terms, offset)
        port_bits[pair(a, z)] = bits
        record(kind, dict(pair=[a, z], additive_offset=offset,
                          terms=terms, actual_B_threshold_bits=list(bits)),
               0 <= defect(a, z) <= 2, before)

    def paths(a, b):
        ab = pair(a, b)
        if ab in path_cache:
            return path_cache[ab]
        terms, rows = [], []
        for middle in range(N):
            if middle in ab:
                continue
            left, right = edge(a, middle), edge(middle, b)
            if left is False or right is False:
                continue
            if left is True and right is True:
                term, kind = True, 'fixed_actual_path'
            elif left is True or right is True:
                term, kind = (right if left is True else left), 'one_free_actual_edge'
            else:
                term, kind = em.new_var('actual_two_free_edge_path'), 'actual_AND'
                helper.add_iff_and(em, term, left, right)
            terms.append(term)
            rows.append(dict(middle=middle, kind=kind, term=term,
                             actual_edge_inputs=[left, right]))
        path_cache[ab] = dict(terms=terms, records=rows)
        return path_cache[ab]

    try:
        # Complete fixed core identities, checked on the full sanity graph.
        for x in range(1, N):
            assert defect(V, x) == (2 if x in (U_ENDPOINT, W_ENDPOINT) else 0)
        assert defect(U_ENDPOINT, W_ENDPOINT) == data['beta']
        for x, y in combinations(T, 2):
            assert defect(x, y) == int(x in U and y in U) + int(x in W and y in W)
        for x in T:
            assert defect(x, U_ENDPOINT) == defect(x, W_ENDPOINT) == 0

        # Every non-core vertex receives exactly the degrees in the design.
        for z in exceptional:
            exact([edge(z, y) for y in range(N) if y != z], 8,
                  'exceptional_total_degree', dict(vertex=z, target=8),
                  len(adjacency[z]) == 8)
        for t, row in ordinary.items():
            for z in row:
                assert all(edge(z, other) is False for other in groups[t] if other != z)
                for color, group in groups.items():
                    if color == t:
                        continue
                    exact([edge(z, other) for other in group], 1,
                          'ordinary_other_color_degree', dict(vertex=z, color=color, target=1),
                          len(adjacency[z] & set(group)) == 1)

        # T/Z ordinary entries are exactly zero by the color constraints.
        # The two endpoint/Z interfaces require all fifty vertices.
        for x in T:
            for z in exceptional:
                offset = int(x in U and z in P) + int(x in W and z in Q) - 1 + int(parent[z] == x)
                short_defect(x, z, [edge(z, other) for other in groups[x]],
                             offset, 'exceptional_TZ_actual_B_bounds')
        for endpoint, attachment, subset in ((U_ENDPOINT, P, U), (W_ENDPOINT, Q, W)):
            for z in Z:
                offset = int(parent[z] in subset) + int(z in attachment) - 1
                short_defect(endpoint, z, [edge(z, other) for other in sorted(attachment)],
                             offset, 'all_Z_endpoint_actual_B_bounds')
        if data['r'] == 2:
            c, d = next(iter(U - W)), next(iter(W - U))
            q0 = next(iter(Q & set(groups[c])))
            p0 = next(iter(P & set(groups[d])))
            ordinary_ports = set(ordinary[c]) | set(ordinary[d])
            for endpoint, allowed in ((U_ENDPOINT, ordinary_ports | {q0}),
                                      (W_ENDPOINT, ordinary_ports | {p0})):
                assert len(allowed) == 11
                for z in Z:
                    if z in allowed:
                        continue
                    before = em.clause_count
                    for bit in port_bits[pair(endpoint, z)]:
                        require_or(em, [neg(bit)])
                    record('r2_endpoint_port_domain_zero',
                           dict(pair=[endpoint, z], allowed_vertices=sorted(allowed)),
                           weight(endpoint, z) == 0, before)
        for x in T:
            target = 4 - 2 * (int(x in U) + int(x in W))
            exact([bit for z in exceptional for bit in port_bits[pair(x, z)]], target,
                  'T_row_actual_B_port_budget', dict(vertex=x, target=target),
                  sum(weight(x, z) for z in exceptional) == target)
        for z in exceptional:
            target = 2 * (int(z in P) + int(z in Q))
            exact([bit for x in T for bit in port_bits[pair(x, z)]], target,
                  'exceptional_T_column_actual_B_port_budget', dict(vertex=z, target=target),
                  sum(weight(x, z) for x in T) == target)
        for endpoint in (U_ENDPOINT, W_ENDPOINT):
            target = 2 - data['beta']
            exact([bit for z in Z for bit in port_bits[pair(endpoint, z)]], target,
                  'endpoint_all_Z_actual_B_port_budget', dict(vertex=endpoint, target=target),
                  sum(weight(endpoint, z) for z in Z) == target)

        # Every pair is represented. Counts are built when needed, and the
        # same actual path list is reused by the saturated shared-s row.
        shared = next(iter(P & Q)) if data['h'] else None
        for a, b in combinations(range(N), 2):
            direct = edge(a, b)
            fixed_middle = next((m for m in range(N) if m not in (a, b)
                                 and edge(a, m) is True and edge(m, b) is True), None)
            shared_exact = shared in (a, b) and a in Z and b in Z
            before = em.clause_count
            if direct is True or fixed_middle is not None:
                coverage.append(dict(pair=[a, b], status='fixed_actual_witness',
                                     direct=direct, fixed_middle=fixed_middle, coverage_clause=None))
                assert b in adjacency[a] or adjacency[a] & adjacency[b]
            else:
                actual_paths = paths(a, b)
                require_or(em, [direct] + actual_paths['terms'])
                coverage.append(dict(pair=[a, b], status='emitted', direct=direct,
                                     coverage_clause=em.clause_count))
                record('actual_original_pair_coverage', dict(pair=[a, b]),
                       b in adjacency[a] or bool(adjacency[a] & adjacency[b]), before)
            if shared_exact:
                actual_paths = paths(a, b)
                exact([direct] + actual_paths['terms'], 1,
                      'shared_attachment_actual_B_zero', dict(pair=[a, b], target_mu_plus_A=1),
                      defect(a, b) == 0)

        assert len(coverage) == N * (N - 1) // 2
        assert set(em.values) == set(range(1, em.variable_count + 1))
        for ab, bits in port_bits.items():
            for threshold, bit in enumerate(bits, 1):
                value = bit if isinstance(bit, bool) else em.values[bit]
                assert value == (actual_B[ab] >= threshold), (ab, threshold)
        false_ids = em.false_clause_ids
        for item in records:
            index = bisect_left(false_ids, item['first_clause'])
            failed = index < len(false_ids) and false_ids[index] <= item['last_clause']
            assert failed == (not item['sanity_semantic_satisfied']), item
        assert set(false_ids).issubset(em.constraint_ids)
        # Every degree is either fixed or implied by checked exact row rules.
        graph_degree_valid = all(len(row) == 8 for row in adjacency)
        degree_groups_valid = all(item['sanity_semantic_satisfied'] for item in records
                                  if item['kind'] in ('exceptional_total_degree', 'ordinary_other_color_degree'))
        # Ordinary color constraints are stronger than degrees alone; their
        # conjunction must imply all degrees, not conversely.
        assert not degree_groups_valid or graph_degree_valid
        em.finish()
    except BaseException:
        em.abort()
        raise
    return dict(data=data, emitter=em, free=free, adjacency=adjacency,
                actual_B=actual_B, records=records, coverage=coverage,
                path_cache=path_cache, port_bits=port_bits,
                sanity_scope='Deterministic possibly-invalid full graph; exact emitted auxiliary '
                             'definitions and every asserted family checked against original '
                             'degrees/common-neighbors. Budget threshold weights are clipped '
                             'only for this invalid-assignment comparison; asserted B bounds '
                             'make those weights equal actual B in every satisfying model.')


def small_sanity(helper, support):
    """Only new constant-folded short-B/count glue, exhaustively Boolean."""
    checked, instances = 0, 0
    for length in range(8):
        for fixed_true in range(3):
            for offset in (-1, 0, 1, 2):
                em = evaluated_emitter(helper, support, retain=True)
                inputs = [em.new_var('tiny_actual_edge') for _ in range(length)]
                em.values.update({var: False for var in inputs})
                bits = defect_count(helper, em, [True] * fixed_true + [False] + inputs, offset)
                for assignment in product((False, True), repeat=length):
                    values = dict(zip(inputs, assignment))
                    false_ids = []
                    for clause_id, clause in enumerate(em.clauses, 1):
                        if support.evaluate_clause(clause, values, clause_id):
                            false_ids.append(clause_id)
                    value = sum(assignment) + fixed_true + offset
                    assert (not false_ids) == (0 <= value <= 2)
                    for k, bit in enumerate(bits, 1):
                        actual = bit if isinstance(bit, bool) else values[bit]
                        assert actual == (value >= k)
                    assert set(values) == set(range(1, em.variable_count + 1))
                    assert false_ids == [i for i, clause in enumerate(em.clauses, 1)
                        if not any(values[abs(literal)] == (literal > 0) for literal in clause)]
                    checked += 1
                em.finish()
                instances += 1
    layouts = {case: dict(primary_edge_variables=len(layout(case)['free_pairs']),
                         fixed_edges=sum(layout(case)['fixed'].values())) for case in CASES}
    return dict(status='PASSED', scope='New short-B/count constant-folding glue and all three '
                'finite label maps only; no target CNF or solver',
                tiny_instances=instances, primary_assignments_checked=checked,
                layouts=layouts, solver_calls=0)


def prepare(case):
    started_cpu, started_wall = time.process_time(), time.monotonic()
    target = HERE / case
    target.mkdir(exist_ok=True)
    assert not (target / 'input.cnf').exists() and not (target / 'encoding.json').exists(), 'Preserve prepared input'
    helper, support = load_modules()
    model = build_model(case, helper, support, target / 'input.cnf')
    em, data, free = model['emitter'], model['data'], model['free']
    check = support.check_dimacs(target / 'input.cnf', em.values, em.variable_count, em.clause_count)
    assert check['false_clause_ids'] == em.false_clause_ids
    check.update(status='PASSED_EXACT_EMITTED_SEMANTIC_SANITY', scope=model['sanity_scope'],
                 full_graph_degrees=[len(row) for row in model['adjacency']],
                 all_original_pair_count=1830, is_target_witness=False, solver_calls=0,
                 failed_semantic_constraints=sum(not item['sanity_semantic_satisfied'] for item in model['records']))
    save(target / 'semantic_sanity.json', check)
    support.write_assignment(target / 'sanity.assignment.txt', em.values)
    save(target / 'edge_variables.json', dict(format=['u', 'v', 'variable'],
         rows=[[a, b, var] for (a, b), var in free.items()],
         fixed_format=['u', 'v', 'value'],
         fixed_rows=[[a, b, int(value)] for (a, b), value in sorted(data['fixed'].items())]))
    save(target / 'normalization.json', dict(case=case, r=data['r'], h=data['h'], beta=data['beta'],
         v=V, u=U_ENDPOINT, w=W_ENDPOINT, T=T, Z=Z, U=sorted(data['U']), W=sorted(data['W']),
         P=sorted(data['P']), Q=sorted(data['Q']), groups=data['groups'], ordinary=data['ordinary'],
         fixed_pair_reasons=[dict(pair=list(ab), value=data['fixed'][ab], reasons=reasons)
                            for ab, reasons in sorted(data['reasons'].items())],
         labeling_proof='proofs/dd82/n61/INTERNAL_DOUBLE_FULL_GRAPH_DESIGN.md'))
    save(target / 'constraints.json', dict(records=model['records']))
    save(target / 'coverage.json', dict(records=model['coverage'],
         path_lists=[dict(pair=list(ab), **entry) for ab, entry in sorted(model['path_cache'].items())]))
    result = dict(status='PREPARED_NOT_RUN', solver_calls=0, n=N, case=case, scope=SCOPE,
         degree_target=8, r=data['r'], h=data['h'], beta=data['beta'], epsilon=0,
         variables=em.variable_count, clauses=em.clause_count, variable_kinds=em.kind_counts,
         primary_edge_variables=len(free), fixed_pairs=len(data['fixed']),
         fixed_edges=sum(data['fixed'].values()), all_original_pair_count=1830,
         coverage_clauses=sum(item['status'] == 'emitted' for item in model['coverage']),
         actual_short_B_entries=len(model['port_bits']),
         shared_attachment_exact_B_zero_pairs=sum(item['kind'] == 'shared_attachment_actual_B_zero'
                                                   for item in model['records']),
         global_all_Z_pair_B_upper_counters=False, r2_port_subbranching=False,
         r2_endpoint_port_domain_zero_pairs=sum(item['kind'] == 'r2_endpoint_port_domain_zero'
                                                for item in model['records']),
         degree_coverage_model_complete=True, source_semantic_sanity=check['status'],
         small_sanity='Separate source-stage sanity command; not silently rerun by preparation',
         mathematical_dependencies=DEPENDENCIES,
         generic_helper_reuse='CNFEmitter, unary_thresholds, add_iff_and; emitted assignment evaluator '
                              'and complete DIMACS/decode support; imported definitions only',
         review_status='External and fresh local review receipts are root-managed, not inferred here',
         cnf_bytes=(target / 'input.cnf').stat().st_size,
         preparation_cpu_seconds=time.process_time() - started_cpu,
         preparation_wall_seconds=time.monotonic() - started_wall)
    save(target / 'encoding.json', result)
    print(json.dumps(result, indent=2))


def decode(case, log_path=None):
    # The generic decoder checks every actual saved CNF clause, reconstructs
    # all constants and primary edges, and writes a full 61-vertex candidate.
    # Its independent BFS remains the runner's separate obligation.
    _, support = load_modules()
    support.HERE = HERE
    support.decode(case, log_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode', 'sanity'))
    parser.add_argument('--case', choices=tuple(CASES))
    parser.add_argument('--log', type=Path)
    args = parser.parse_args()
    if args.action == 'sanity':
        helpers, support_module = load_modules()
        print(json.dumps(small_sanity(helpers, support_module), indent=2))
    else:
        parser.error('--case is required for prepare/decode') if args.case is None else None
        prepare(args.case) if args.action == 'prepare' else decode(args.case, args.log)
