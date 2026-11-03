"""One exact joint completion of saved seed3 F5; prepare/decode, no solver.

All 1508 nonedges are free and each vertex receives three new edges. No
constraint preserves the old last three matchings, their colors, or polarity.
Only the generic fixed-graph functions of completion.py are reused.
"""
import argparse
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'pilot/seed3/rounds.json'
COMPLETION = HERE.parent.parent / 'polarity73_reduction_run/refined/completion.py'
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('joint_tail_generic_completion', COMPLETION)
generic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generic)
save = generic.save
SCOPE = ('All degree-eight diameter-two completions containing the actual seed3 '
         'first-five-round graph F5. Exactly its 145 edges are fixed; all 1508 '
         'nonedges are free, with added degree three at every vertex. '
         'No matching colors, old M6/M7/M8, geometry, or symmetry constraints. '
         'This fixed-prefix family is not all 58-vertex graphs.')
EXPECTED_CNF = (56004, 173002)


def load_prefix():
    source = json.loads(SOURCE.read_text())
    assert source['n'] == 58 and source['seed'] == 3
    assert source['status'] == 'COMPLETE' and source['completed_rounds'] == 8
    labels = source['ambient_labels']
    assert len(labels) == len(set(labels)) == 58
    old, tail, seen = set(), set(), set()
    assert len(source['rounds']) == 8
    for index, row in enumerate(source['rounds'], 1):
        assert row['round'] == index
        matching = list(map(tuple, row['matching_edges']))
        assert len(matching) == 29 and all(0 <= x < y < 58 for x, y in matching)
        assert sorted(x for xy in matching for x in xy) == list(range(58))
        assert not seen.intersection(matching)
        seen.update(matching)
        (old if index <= 5 else tail).update(matching)
    assert len(old) == 145 and len(tail) == 87
    prefix, _ = generic.graph_check(58, old, degree_target=8)
    assert prefix['degrees'] == [5]*58 and len(prefix['bad_pairs']) == 930
    assert prefix['bad_pairs'] == source['rounds'][4]['bad_pairs']
    saved = json.loads((SOURCE.parent / 'candidate.json').read_text())
    assert saved['n'] == 58 and saved['ambient_labels'] == labels
    assert seen == set(map(tuple, saved['edges'])) and len(seen) == 232
    return labels, old, tail, prefix


def tiny_odd_cycle_sanity():
    # The new graph consists of two odd triangles, so it cannot be split
    # into two perfect matchings. The completed triangular prism is valid.
    old = {(0, 3), (1, 4), (2, 5)}
    added = {(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5)}
    model = generic.build(6, old, degree_target=3)
    row = generic.check_explicit_assignment(model, 'triangular_prism_new_odd_triangles', added)
    assert row['valid_graph'] and row['exact_degrees'] and row['bad_pairs'] == 0
    assert row['false_clauses'] == 0
    return row


def prepare():
    assert not any((HERE / name).exists() for name in
                   ('input.cnf', 'encoding.json', 'variable_map.json', 'sanity.json'))
    cpu, wall = time.process_time(), time.monotonic()
    labels, old, tail, prefix = load_prefix()
    model = generic.build(58, old, degree_target=8)
    em = model['emitter']
    assert model['deficits'] == [3]*58
    assert len(model['free']) == 1508
    assert set(model['free']) == set(combinations(range(58), 2)) - old
    assert (em.variable_count, em.clause_count) == EXPECTED_CNF
    # Existing explicit full-adjacency sanity includes tiny positive/negative
    # graphs and this exact F5 with no additions / all eligible additions.
    sanity = generic.semantic_sanity(model)
    actual = generic.check_explicit_assignment(model, 'saved_seed3_M6_M7_M8_full_graph', tail)
    assert actual['exact_degrees'] and not actual['valid_graph']
    assert actual['bad_pairs'] == actual['false_clauses'] == 177
    sanity['records'].extend([actual, tiny_odd_cycle_sanity()])
    sanity.update(source_prefix_rounds=5, saved_final_graph_bad_pairs=177,
                  new_odd_cycles_allowed=True, saved_tail_is_sanity_only=True)
    with (HERE / 'input.cnf').open('w') as output:
        output.write(f'p cnf {em.variable_count} {em.clause_count}\n')
        for clause in em.clauses:
            output.write(' '.join(map(str, clause)) + ' 0\n')
    save(HERE / 'variable_map.json', dict(n=58, seed=3, prefix_rounds=5,
         ambient_labels=labels, fixed_edges=sorted(old),
         added_edge_variables=[dict(edge=xy, variable=var) for xy, var in model['free'].items()]))
    save(HERE / 'sanity.json', sanity)
    record = dict(status='PREPARED_NOT_RUN', scope=SCOPE, n=58, seed=3, prefix_rounds=5,
                  degree_target=8, added_degree=3, fixed_edges=145, required_added_edges=87,
                  source_prefix=str(SOURCE), source_bad_pairs=prefix['bad_pairs'],
                  source_bad_pair_count=930, variables=em.variable_count, clauses=em.clause_count,
                  variable_kinds=em.kind_counts, free_edge_variables=len(model['free']),
                  degree_records=model['degrees'], coverage_records=model['coverage'],
                  saved_tail_fixed=False, matching_factorization_required=False,
                  geometry_constraints_added=False, solver_calls=0,
                  elapsed_cpu=time.process_time()-cpu, elapsed_wall=time.monotonic()-wall)
    save(HERE / 'encoding.json', record)
    print(json.dumps({key: record[key] for key in ('status', 'scope', 'variables', 'clauses',
                                                  'elapsed_cpu', 'elapsed_wall')}, indent=2))


def decode(log=None):
    log = log or HERE / 'solver.log'
    record = json.loads((HERE / 'encoding.json').read_text())
    mapping = json.loads((HERE / 'variable_map.json').read_text())
    assert record['n'] == mapping['n'] == 58 and record['degree_target'] == 8
    assert record['seed'] == mapping['seed'] == 3
    assert record['prefix_rounds'] == mapping['prefix_rounds'] == 5
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
    _, support = generic.baseline.load_helpers()
    clause_check = support.check_dimacs(HERE / 'input.cnf', values, record['variables'], record['clauses'])
    assert clause_check['all_clauses_satisfied'], 'Saved DIMACS assignment fails clauses'
    labels, old, _, _ = load_prefix()
    assert labels == mapping['ambient_labels'] and old == set(map(tuple, mapping['fixed_edges']))
    free = {tuple(row['edge']): row['variable'] for row in mapping['added_edge_variables']}
    assert set(free) == set(combinations(range(58), 2)) - old
    assert len(free) == len(mapping['added_edge_variables']) == len(set(free.values())) == 1508
    added = {xy for xy, var in free.items() if values[var]}
    edges = old | added
    verification, _ = generic.graph_check(58, edges, degree_target=8)
    target_graph = verification['valid'] and len(edges) == 232 and len(added) == 87
    result = dict(status='SAT_JOINT_TAIL_TARGET_CHECKED' if target_graph else 'SAT_DECODE_VALIDATION_FAILED',
                  scope=SCOPE, n=58, edges=sorted(edges), ambient_labels=labels,
                  seed=3, prefix_rounds=5, target_graph=target_graph,
                  fixed_edges=145, added_edges=sorted(added),
                  verification=verification, model_check=clause_check,
                  all_bad_pairs=verification['bad_pairs'], source_solver_log=str(log),
                  independent_external_verification_performed=False)
    (HERE / 'candidate.edges').write_text(f'58 {len(edges)}\n' +
        ''.join(f'{x} {y}\n' for x, y in sorted(edges)))
    save(HERE / 'candidate.json', result)
    print(json.dumps(dict(status=result['status'], n=58, edges=len(edges),
                         bad_pairs=len(verification['bad_pairs']), target_graph=target_graph), indent=2))
    if not target_graph:
        raise SystemExit(2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode'))
    parser.add_argument('--log', type=Path)
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare()
    else:
        decode(args.log)
