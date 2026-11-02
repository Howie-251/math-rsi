"""Prepare seven C cases, ordering Z labels inside their existing U/V cells.

Each case retains the whole parent CNF, selects one type, and sorts each
cell lexicographically by its actual (S,T) parents. No other labels change.
This prepares files only; it never invokes an encoder or a solver.
"""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import time

HERE = Path(__file__).resolve().parent

ENCODE_WRAPPER = '''"""Decode this case with the prepared parent encoder; no generation."""
import argparse
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('adjacent_ports_case_encode', PARENT / 'encode.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
base.HERE = HERE
# Keep base.ROOT and its generic helper path anchored to the parent project.

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('decode',))
    parser.add_argument('--log', type=Path, default=HERE / 'solver.log')
    args = parser.parse_args()
    base.decode(args.log)
'''

RUNNER_WRAPPER = '''"""Run/check this already prepared case with the existing bounded runner."""
import argparse
import importlib.util
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('adjacent_ports_case_runner', PARENT / 'runner.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
base.HERE = HERE
# ROOT, SOLVER, CHECKER and BFS retain the correct project paths established
# when the parent runner was imported; only this case's output path changes.

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'solve', 'check'))
    parser.add_argument('--cpu', type=int, default=1)
    parser.add_argument('--solver-cpu', type=int, default=50)
    parser.add_argument('--solver-wall', type=int, default=70)
    args = parser.parse_args()
    if args.action == 'prepare':
        raise SystemExit('Cases are prepared only by parent prepare_cases.py; this wrapper does not regenerate CNF.')
    if args.action == 'solve':
        base.solve(args.cpu, args.solver_cpu, args.solver_wall)
    else:
        base.check(args.cpu)
'''


def save(path, record):
    path.write_text(json.dumps(record, indent=2) + '\n')


def case_additions(case, encoding, edges):
    """Use only remaining permutations of labels inside each actual U/V cell."""
    layers = encoding['layers']
    U, S, T, Z = (layers[name] for name in ('U', 'S', 'T', 'Z'))

    def edge(a, b):
        return edges[min(a, b), max(a, b)]

    cells = {}
    for index, (z, parent) in enumerate(zip(Z, case['Z_to_V_parent'])):
        cells.setdefault((U[index // 7], parent), []).append(z)
    assert len(cells) == 25 and sum(map(len, cells.values())) == 35
    clauses = [(case['selector_variable'],)]
    pairs = []
    for (u_parent, v_parent), vertices in sorted(cells.items()):
        for left, right in zip(vertices, vertices[1:]):
            pairs.append(dict(U_parent=u_parent, V_parent=v_parent, ordered_pair=[left, right]))
            # Every Z point has exactly one S and one T parent already.
            # Forbid a descending S parent, then a descending T parent
            # when the S parents agree. Equal (S,T) keys remain unordered.
            for i in range(6):
                for j in range(i):
                    clauses.append((-edge(S[i], left), -edge(S[j], right)))
            for parent in S:
                for k in range(6):
                    for ell in range(k):
                        clauses.append((-edge(parent, left), -edge(parent, right),
                                        -edge(T[k], left), -edge(T[ell], right)))
    assert len(pairs) == 10 and len(clauses) == 1051
    return clauses, pairs


def prepare_cases():
    started_cpu, started_wall = time.process_time(), time.monotonic()
    assert not (HERE / 'case_preparation.json').exists(), 'Preserve the previous case preparation'
    encoding = json.loads((HERE / 'encoding.json').read_text())
    assert encoding['status'] == 'PREPARED_NOT_RUN' and encoding['solver_calls'] == 0
    assert encoding['primary_edge_variables'] == 1830 and len(encoding['C_types']) == 7
    assert not (HERE / 'launch.json').exists(), 'Prepare branches before any parent solver launch'
    cases = encoding['C_types']
    assert len({case['selector_variable'] for case in cases}) == 7
    edge_rows = json.loads((HERE / 'edge_variables.json').read_text())['rows']
    edges = {(a, b): var for a, b, var in edge_rows}
    assert len(edges) == 1830
    expected_header = ['p', 'cnf', str(encoding['variables']), str(encoding['clauses'])]
    with (HERE / 'input.cnf').open('r', encoding='ascii') as source:
        assert source.readline().split() == expected_header
    for index in range(7):
        assert not (HERE / f'case_{index}').exists(), 'Preserve every already prepared case'

    records = []
    for index, case in enumerate(cases):
        case_cpu, case_wall = time.process_time(), time.monotonic()
        target = HERE / f'case_{index}'
        target.mkdir()
        selector = case['selector_variable']
        additions, ordering_pairs = case_additions(case, encoding, edges)
        with (HERE / 'input.cnf').open('r', encoding='ascii') as source:
            assert source.readline().split() == expected_header
            with (target / 'input.cnf').open('w', encoding='ascii') as output:
                output.write(f"p cnf {encoding['variables']} {encoding['clauses'] + len(additions)}\n")
                shutil.copyfileobj(source, output, length=1024*1024)
                for clause in additions:
                    output.write(' '.join(map(str, clause)) + ' 0\n')
        shutil.copyfile(HERE / 'edge_variables.json', target / 'edge_variables.json')
        (target / 'encode.py').write_text(ENCODE_WRAPPER)
        (target / 'runner.py').write_text(RUNNER_WRAPPER)

        record = deepcopy(encoding)
        record['scope'] = (encoding['scope'] + '; selected C cycle type ' + case['name']
                           + '; Z labels within each U/V cell ordered by actual S/T parents')
        record['selected_case'] = dict(index=index, name=case['name'], selector_variable=selector,
                                       cycle_partition=case['cycle_partition'])
        record['case_split'] = dict(
            parent_cnf='../input.cnf', parent_encoding='../encoding.json',
            parent_variables=encoding['variables'], parent_clauses=encoding['clauses'],
            retained_parent_clauses=encoding['clauses'], appended_unit=selector,
            exhaustive_disjoint_reason=('Parent has exactly one of seven selectors. Every original target '
                'can additionally sort its Z labels within each fixed U/V cell, preserving its selected type.'),
            coverage_is_original_graphs_up_to_proved_cell_relabeling=True,
            further_label_normalization='Only independent Z label permutations within existing U/V cells',
            within_cell_order='lexicographic by (S parent index, T parent index)',
            ordering_pairs=ordering_pairs, ordering_clause_count=len(additions)-1,
            parent_detail_records=['../degree_constraints.json', '../coverage.json',
                                   '../defect_constraints.json', '../port_constraints.json'])
        record['clauses'] += len(additions)
        record['parent_added_clauses'] = encoding['added_clauses']
        record['added_clauses'] += len(additions)
        record['clause_groups'].append(dict(name='selected_C_type_unit',
            first_clause=encoding['clauses']+1, last_clause=encoding['clauses']+1, clauses=1))
        record['clause_groups'].append(dict(name='within_UV_cell_lexicographic_S_T_parent_order',
            first_clause=encoding['clauses']+2, last_clause=record['clauses'], clauses=len(additions)-1))
        record['cnf_bytes'] = (target / 'input.cnf').stat().st_size
        record['parent_preparation_cpu_seconds'] = record.pop('preparation_cpu_seconds')
        record['parent_preparation_wall_seconds'] = record.pop('preparation_wall_seconds')
        record['case_preparation_cpu_seconds'] = time.process_time() - case_cpu
        record['case_preparation_wall_seconds'] = time.monotonic() - case_wall
        record['source_dependencies'] = ['../encode.py', '../runner.py', '../prepare_cases.py']
        save(target / 'encoding.json', record)
        records.append(dict(index=index, directory=target.name, C_type=case['name'],
                            selector_unit=selector, variables=record['variables'], clauses=record['clauses'],
                            appended_clauses=len(additions), within_cell_ordering_clauses=len(additions)-1,
                            cnf_bytes=record['cnf_bytes'], solver_calls=0,
                            preparation_cpu_seconds=record['case_preparation_cpu_seconds'],
                            preparation_wall_seconds=record['case_preparation_wall_seconds']))
    result = dict(status='ALL_SEVEN_CASES_PREPARED_NOT_RUN', solver_calls=0,
                  parent_solver_launched=False, cases=records,
                  cpu_seconds=time.process_time() - started_cpu,
                  wall_seconds=time.monotonic() - started_wall)
    save(HERE / 'case_preparation.json', result)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    prepare_cases()
