"""Necessary polarity73 deletion and unit-deficit choice screen; no solver."""
import argparse
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('polarity73_baseline', PARENT / 'screen.py')
baseline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(baseline)
save = baseline.save
SCOPE = ('All polarity73 deletion sets at the specified order, with necessary '
         'unit-deficit new-neighbor choices; partial choices, not a target graph. '
         'Incoming capacity at higher-deficit vertices is not constrained.')


def direct_screen(deleted, choices, n, data=None):
    """Evaluate actual saved-H predicates without using CNF definitions."""
    data = data or baseline.geometry()
    result = baseline.direct_screen(deleted, n, data)
    deleted, choices = set(deleted), set(map(tuple, choices))
    adj = data['adj']
    survivors, sat = set(result['survivors']), set(result['saturated'])
    one = {x for x in survivors if result['retained_degrees'][x] == 7}
    outgoing = {x: {y for u, y in choices if u == x} for x in range(73)}
    invalid = sorted((x, y) for x, y in choices if x == y or y in adj[x]
                     or x not in one or y not in survivors or y in sat)
    missing = sorted(x for x in one if not outgoing[x])
    multiple = sorted(x for x in range(73) if len(outgoing[x]) > 1)
    unreciprocated = sorted((x, y) for x, y in choices
                           if y in one and (y, x) not in choices)
    uncovered = []
    for x in sorted(one):
        for s in sorted(sat):
            if x == s or s in adj[x]:
                continue
            common = adj[x] & adj[s]
            assert len(common) == 1
            m = next(iter(common))
            if m in deleted and not outgoing[x] & adj[s]:
                uncovered.append([x, s, m])
    result['groups'].update(choice_guards=not invalid, unit_choice_exists=not missing,
                            at_most_one_choice=not multiple,
                            unit_reciprocity=not unreciprocated,
                            unit_saturated_cover=not uncovered)
    result['passes_screen'] = all(result['groups'].values())
    result.update(unit_deficit_vertices=sorted(one), directed_choices=sorted(choices))
    result['violations'].update(choice_guards=invalid, unit_choice_missing=missing,
                                multiple_choices=multiple, reciprocity=unreciprocated,
                                unit_saturated_cover=uncovered)
    return result


def build(case):
    # Reuse the complete baseline in memory. Its finish(None) writes nothing.
    model = baseline.build(case)
    em, data = model['emitter'], model['geometry']
    helper, _ = baseline.load_helpers()
    adj, deleted, sat = data['adj'], model['deleted'], model['sat']
    model['baseline_variables'] = em.variable_count
    model['baseline_clauses'] = em.clause_count
    model['baseline_variable_kinds'] = dict(em.kind_counts)
    choice = {(x, y): em.new_var('directed_unit_neighbor_choice')
              for x in range(73) for y in range(73) if x != y and y not in adj[x]}
    one, one_thresholds, choice_thresholds = {}, {}, {}
    for x in range(73):
        target = len(adj[x]) - 7
        thresholds = helper.unary_thresholds(
            em, [deleted[y] for y in sorted(adj[x])], target + 1,
            'unit_deleted_neighbor_threshold')
        one_thresholds[x] = list(thresholds)
        out = em.new_var('retained_unit_deficit_iff')
        one[x] = out
        conditions = [-deleted[x], thresholds[target - 1], -thresholds[target]]
        for literal in conditions:
            em.add_clause(-out, literal)
        em.add_clause(out, *(-literal for literal in conditions))
        choice_thresholds[x] = list(helper.unary_thresholds(
            em, [choice[x, y] for y in range(73) if (x, y) in choice], 2,
            'outgoing_choice_threshold'))
    model['definition_ranges'] = [[1, model['definition_end']],
                                  [model['baseline_clauses'] + 1, em.clause_count]]

    def group(name, clauses):
        first = em.clause_count + 1
        for clause in clauses:
            em.add_clause(*clause)
        model['groups'][name] = dict(first_clause=first, last_clause=em.clause_count,
                                     clauses=em.clause_count-first+1)

    group('choice_guards', [clause for (x, y), var in choice.items()
                           for clause in [(-var, one[x]), (-var, -deleted[y]),
                                          (-var, -sat[y])]])
    group('unit_choice_exists', [(-one[x], choice_thresholds[x][0]) for x in range(73)])
    group('at_most_one_choice', [(-choice_thresholds[x][1],) for x in range(73)])
    group('unit_reciprocity', [(-var, -one[y], choice[y, x])
                               for (x, y), var in choice.items()])
    covers = []
    for x, s in choice:
        common = adj[x] & adj[s]
        assert len(common) == 1
        m = next(iter(common))
        ys = sorted(y for y in adj[s] if (x, y) in choice)
        covers.append([x, s, m, ys])
    group('unit_saturated_cover', [tuple([-one[x], -sat[s], -deleted[m]] +
                                         [choice[x, y] for y in ys])
                                  for x, s, m, ys in covers])
    model.update(choice=choice, one=one, one_thresholds=one_thresholds,
                 choice_thresholds=choice_thresholds, cover_records=covers)
    return model


def explicit_assignments(n, data):
    """A fixed saved D plus deliberately true/false choice guards; no search."""
    row = json.loads((PARENT / f'n{n}' / 'deletion_candidate.json').read_text())
    deleted = set(row['deleted'])
    direct = baseline.direct_screen(deleted, n, data)
    one = {x for x, d in direct['retained_degrees'].items() if d == 7}
    sat = set(direct['saturated'])
    adj = data['adj']
    nonedges = [(x, y) for x in range(73) for y in range(73)
                if x != y and y not in adj[x]]
    unit_pair = next((x, y) for x, y in nonedges if x in one and y in one)
    another_target = next(y for x, y in nonedges if x == unit_pair[0] and y != unit_pair[1])
    wrong_source = next((x, y) for x, y in nonedges if x not in one)
    deleted_target = next((x, y) for x, y in nonedges if x in one and y in deleted)
    sat_target = next((x, y) for x, y in nonedges if x in one and y in sat)
    return [('empty_D_empty_choices', set(), set()),
            ('all_D_empty_choices', set(range(73)), set()),
            ('saved_D_empty_choices', deleted, set()),
            ('unit_pair_one_way', deleted, {unit_pair}),
            ('unit_pair_reciprocal', deleted, {unit_pair, unit_pair[::-1]}),
            ('two_outgoing_choices', deleted, {unit_pair, (unit_pair[0], another_target)}),
            ('source_guard_false', deleted, {wrong_source}),
            ('retained_target_guard_false', deleted, {deleted_target}),
            ('unsaturated_target_guard_false', deleted, {sat_target})]


def semantic_sanity(model):
    em, support = model['emitter'], model['support']
    rows, cover_guards = [], set()
    for label, deleted, choices in explicit_assignments(model['n'], model['geometry']):
        direct = direct_screen(deleted, choices, model['n'], model['geometry'])
        values = {var: x in deleted for x, var in model['deleted'].items()}
        values.update({var: pair in choices for pair, var in model['choice'].items()})
        false_ids = {i for i, clause in enumerate(em.clauses, 1)
                     if support.evaluate_clause(clause, values, i)}
        assert len(values) == em.variable_count
        assert not any(first <= i <= last for first, last in model['definition_ranges']
                       for i in false_ids)
        assert all(values[var] == (x in direct['saturated']) for x, var in model['sat'].items())
        assert all(values[var] == (x in direct['unit_deficit_vertices'])
                   for x, var in model['one'].items())
        for name, bounds in model['groups'].items():
            satisfied = not any(bounds['first_clause'] <= i <= bounds['last_clause'] for i in false_ids)
            assert satisfied == direct['groups'][name], (label, name)
        first = model['groups']['unit_saturated_cover']['first_clause']
        for offset, (x, s, m, ys) in enumerate(model['cover_records']):
            guard = (x in direct['unit_deficit_vertices'], s in direct['saturated'], m in deleted)
            cover_guards.add(guard)
            expected = not all(guard) or any((x, y) in choices for y in ys)
            assert (first + offset not in false_ids) == expected
        assert false_ids == {i for i, clause in enumerate(em.clauses, 1)
                             if not any(values[abs(lit)] == (lit > 0) for lit in clause)}
        rows.append(dict(label=label, deleted=sorted(deleted), directed_choices=sorted(choices),
                         groups=direct['groups'], false_clauses=len(false_ids)))
    assert (True, True, True) in cover_guards
    assert any(not all(guard) for guard in cover_guards)
    return dict(status='PASSED_EXPLICIT_ASSIGNMENT_SEMANTICS', solver_calls=0,
                assignments=len(rows), all_sat_and_one_equivalences_checked=True,
                every_constraint_group_compared=True, every_cover_clause_compared=True,
                cover_guard_patterns=sorted(cover_guards), records=rows)


def prepare(case):
    target = HERE / case
    target.mkdir(exist_ok=True)
    assert not any((target / name).exists() for name in ('input.cnf', 'encoding.json', 'variable_map.json'))
    cpu, wall = time.process_time(), time.monotonic()
    model = build(case)
    sanity = semantic_sanity(model)
    em = model['emitter']
    with (target / 'input.cnf').open('w') as output:
        output.write(f'p cnf {em.variable_count} {em.clause_count}\n')
        for clause in em.clauses:
            output.write(' '.join(map(str, clause)) + ' 0\n')
    parent_map = json.loads((PARENT / case / 'variable_map.json').read_text())
    assert parent_map['deleted'] == {str(x): var for x, var in model['deleted'].items()}
    assert parent_map['sat'] == {str(x): var for x, var in model['sat'].items()}
    assert parent_map['deleted_neighbor_thresholds'] == {
        str(x): ts for x, ts in model['neighbor_thresholds'].items()}
    save(target / 'variable_map.json', dict(
        parent_baseline_map=parent_map, parent_variable_range=[1, model['baseline_variables']],
        parent_source='../screen.py', parent_case=case,
        deleted=parent_map['deleted'], sat=parent_map['sat'],
        one={str(x): var for x, var in model['one'].items()},
        choice={str(x): {str(y): model['choice'][x, y] for y in range(73)
                         if (x, y) in model['choice']} for x in range(73)},
        one_deleted_neighbor_thresholds=model['one_thresholds'],
        outgoing_choice_thresholds=model['choice_thresholds'],
        one_definition='not D[x] AND deleted_H_neighbors[x] == degree_H[x]-7',
        choice_definition='directed new neighbor of a retained unit-deficit vertex'))
    save(target / 'sanity.json', sanity)
    record = dict(status='PREPARED_NOT_RUN', scope=SCOPE, n=model['n'], case=case,
                  variables=em.variable_count, clauses=em.clause_count,
                  variable_kinds=em.kind_counts, primary_deletion_variables=73,
                  directed_choice_variables=len(model['choice']), one_variables=73, sat_variables=73,
                  baseline_prefix_variables=model['baseline_variables'],
                  baseline_prefix_clauses=model['baseline_clauses'],
                  baseline_variable_kinds=model['baseline_variable_kinds'],
                  constraint_groups=model['groups'], definition_ranges=model['definition_ranges'],
                  cover_records=model['cover_records'], baseline_source='../screen.py',
                  source_geometry=['../geometry.edges', '../geometry.json'],
                  higher_deficit_incoming_capacity_constrained=False,
                  necessary_only=True, target_graph=False, solver_calls=0,
                  elapsed_cpu=time.process_time()-cpu, elapsed_wall=time.monotonic()-wall)
    save(target / 'encoding.json', record)
    print(json.dumps({key: record[key] for key in ('status', 'n', 'variables', 'clauses',
                                                  'elapsed_cpu', 'elapsed_wall')}, indent=2))


def decode(case, log=None):
    target = HERE / case
    log = log or target / 'solver.log'
    record = json.loads((target / 'encoding.json').read_text())
    mapping = json.loads((target / 'variable_map.json').read_text())
    values, saw_sat = {}, False
    for line in log.read_text().splitlines():
        if line.strip() == 's SATISFIABLE':
            saw_sat = True
        if line.startswith('v '):
            for literal in map(int, line.split()[1:]):
                if literal:
                    var, value = abs(literal), literal > 0
                    assert var not in values or values[var] == value
                    values[var] = value
    assert saw_sat, 'A terminal SAT model is required'
    _, support = baseline.load_helpers()
    check = support.check_dimacs(target / 'input.cnf', values, record['variables'], record['clauses'])
    assert check['all_clauses_satisfied']
    deleted = {int(x) for x, var in mapping['deleted'].items() if values[var]}
    choices = {(int(x), int(y)) for x, row in mapping['choice'].items()
               for y, var in row.items() if values[var]}
    data = baseline.geometry()
    direct = direct_screen(deleted, choices, baseline.CASES[case], data)
    assert direct['passes_screen'], direct['violations']
    for key, field in [('sat', 'saturated'), ('one', 'unit_deficit_vertices')]:
        assert all(values[var] == (int(x) in direct[field]) for x, var in mapping[key].items())
    S = set(direct['survivors'])
    edges = [(u, v) for u, v in data['edges'] if u in S and v in S]
    bad = [[u, v] for u, v in combinations(sorted(S), 2)
           if v not in data['adj'][u] and not (data['adj'][u] & data['adj'][v] & S)]
    partial = sorted({tuple(sorted(pair)) for pair in choices})
    incoming = {x: sum(x in pair for pair in partial) for x in sorted(S)}
    edge_deficit = 4*len(S)-len(edges)
    assert sum(direct['deficits'].values()) == 2*edge_deficit
    result = dict(status='SAT_REFINED_SCREEN_PARTIAL_CANDIDATE_ONLY', scope=SCOPE,
                  target_graph=False, monotone_completion_found=False, **direct,
                  retained_H_edges_original_labels=edges, all_bad_pairs_original_labels=bad,
                  bad_pair_count=len(bad), edge_deficit=edge_deficit,
                  retained_edge_count=len(edges), compact_to_original=sorted(S),
                  partial_added_edges_original_labels=partial, partial_added_degrees=incoming,
                  unconstrained_capacity_overflow=[x for x in sorted(S)
                                                   if incoming[x] > direct['deficits'][x]],
                  higher_deficit_incoming_capacity_constrained=False,
                  source_solver_log=str(log), model_check=check)
    save(target / 'deletion_candidate.json', result)
    compact = {x: i for i, x in enumerate(sorted(S))}
    (target / 'retained_H.edges').write_text(f'{len(S)} {len(edges)}\n' +
        ''.join(f'{compact[u]} {compact[v]}\n' for u, v in edges))
    print(json.dumps(dict(status=result['status'], n=baseline.CASES[case], target_graph=False,
                         bad_pairs=len(bad), partial_added_edges=len(partial)), indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode', 'sanity'))
    parser.add_argument('--n', type=int, choices=(58, 59), required=True)
    parser.add_argument('--log', type=Path)
    args = parser.parse_args()
    case = f'n{args.n}'
    if args.action == 'prepare':
        prepare(case)
    elif args.action == 'decode':
        decode(case, args.log)
    else:
        print(json.dumps(semantic_sanity(build(case)), indent=2))
