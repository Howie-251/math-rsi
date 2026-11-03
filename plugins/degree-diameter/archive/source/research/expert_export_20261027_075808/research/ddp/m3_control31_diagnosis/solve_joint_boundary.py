"""One bounded SAT attempt in the already specified 88-position boundary model.

No dependency installation, proof output, restarts, or enlargement of the model.
Every ordered pair, including the diagonal, must admit an exact three-edge walk.
"""
from collections import deque
from itertools import combinations
from pathlib import Path
import json
import os
import resource
import subprocess
import time

from joint_boundary import build

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
SOLVER = PROJECT / '.tools/lean-4.24.0-linux/bin/cadical'
PREFIX = HERE / 'joint_boundary_sat'


def save(suffix, value):
    PREFIX.with_suffix(suffix).write_text(json.dumps(value, indent=2) + '\n')


def main():
    started = time.monotonic()
    spec = json.loads((HERE / 'joint_boundary_spec.json').read_text())
    n = spec['control_order']
    ports = spec['ports']
    targets = sorted(map(int, spec['target_multiplicity']))
    positions = [(p, t) for p in ports for t in targets]
    primary = {tuple(sorted(e)): i + 1 for i, e in enumerate(positions)}
    assert len(primary) == 88
    fixed = {tuple(e) for e in spec['fixed_edges']}
    assert len(fixed) == 46 and not (fixed & set(primary))
    clauses = []

    def exact(literals, count):
        # At most count; at least count, with no extra cardinality variables.
        clauses.extend([-v for v in group] for group in combinations(literals, count + 1))
        clauses.extend(list(group) for group in combinations(literals, len(literals) - count + 1))

    for p in ports:
        exact([primary[tuple(sorted((p, t)))] for t in targets], 2)
    for t in targets:
        exact([primary[tuple(sorted((p, t)))] for p in ports], spec['target_multiplicity'][str(t)])
    degree_clause_count = len(clauses)

    possible = [set() for _ in range(n)]
    for u, v in fixed | set(primary):
        possible[u].add(v)
        possible[v].add(u)
    terms = [[set() for _ in range(n)] for _ in range(n)]
    fixed_witness = {}
    possible_walk_count = 0
    for u in range(n):
        for a in sorted(possible[u]):
            for b in sorted(possible[a]):
                for v in sorted(possible[b]):
                    possible_walk_count += 1
                    term = tuple(sorted({primary[e] for e in
                                         [tuple(sorted((u, a))), tuple(sorted((a, b))), tuple(sorted((b, v)))]
                                         if e in primary}))
                    terms[u][v].add(term)
                    if not term:
                        fixed_witness.setdefault((u, v), [u, a, b, v])

    aux = {}
    routes = []
    for u in range(n):
        for v in range(n):
            if () in terms[u][v]:
                routes.append(dict(pair=[u, v], fixed_walk=fixed_witness[u, v]))
                continue
            literals = []
            for term in sorted(terms[u][v]):
                if len(term) == 1:
                    literals.append(term[0])
                else:
                    if term not in aux:
                        aux[term] = 89 + len(aux)
                        clauses.extend([-aux[term], edge] for edge in term)
                    literals.append(aux[term])
            routes.append(dict(pair=[u, v], clause_index=len(clauses), term_count=len(literals)))
            clauses.append(literals)

    variable_count = 88 + len(aux)
    cnf = PREFIX.with_suffix('.cnf')
    cnf.write_text('c fixed 31-vertex joint boundary: 88 primary edge variables, 46 fixed edges\n'
                   'c all 961 ordered pairs have an exact length-three walk; no proof output\n'
                   f'p cnf {variable_count} {len(clauses)}\n'
                   + ''.join(' '.join(map(str, clause)) + ' 0\n' for clause in clauses))

    baseline_edges, baseline_missing = build(spec, spec['baseline_assignment'])
    baseline_values = {i: edge in baseline_edges for edge, i in primary.items()}
    baseline_values.update({i: all(baseline_values[e] for e in term) for term, i in aux.items()})
    false_indices = {i for i, clause in enumerate(clauses)
                     if not any(baseline_values[abs(lit)] == (lit > 0) for lit in clause)}
    expected_false = {row['clause_index'] for row in routes
                      if row['pair'] in baseline_missing}
    assert false_indices == expected_false and len(false_indices) == 4
    metadata = dict(
        source='joint_boundary_spec.json', primary_variables=88, fixed_edges=46,
        selected_variable_edges=16, auxiliary_variables=len(aux), total_variables=variable_count,
        total_clauses=len(clauses), degree_clauses=degree_clause_count,
        ordered_pairs=n*n, pairs_with_fixed_walk=len(fixed_witness),
        possible_three_walks_enumerated=possible_walk_count,
        primary_map=[dict(variable=i+1, edge=list(e)) for i, e in enumerate(positions)],
        auxiliary_map=[dict(variable=i, positive_edge_conjunction=list(term)) for term, i in aux.items()],
        routes=routes, baseline_false_route_pairs=baseline_missing,
        encoding='For each nonconstant positive route conjunction C, y_C implies every edge in C; '
                 'each uncovered ordered pair requires the OR of its route variables. '
                 'Existential auxiliary assignment is equivalent to at least one actual three-edge walk. '
                 'Repeated undirected edges in a walk use a single edge variable.')
    save('.encoding.json', metadata)

    help_text = subprocess.run([str(SOLVER), '--help'], text=True, capture_output=True, check=True).stdout
    version = subprocess.run([str(SOLVER), '--version'], text=True, capture_output=True, check=True).stdout.strip()
    assert '-t <sec>       set wall clock time limit' in help_text
    PREFIX.with_suffix('.solver_help.txt').write_text(help_text)
    cpu = min(os.sched_getaffinity(0))
    command = [str(SOLVER), '-t', '60', '-w', str(PREFIX.with_suffix('.model.sol')), str(cnf)]
    run = dict(command=command, solver_version=version, cpu_affinity=[cpu],
               cpu_hard_limit_seconds=60, solver_wall_limit_seconds=60,
               proof_output=False, attempts=1, dependency_installation=False)
    save('.run.json', run)

    def restrict_child():
        os.sched_setaffinity(0, {cpu})
        resource.setrlimit(resource.RLIMIT_CPU, (60, 60))

    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    run_started = time.monotonic()
    with PREFIX.with_suffix('.solver.log').open('w') as out:
        result = subprocess.run(command, stdout=out, stderr=subprocess.STDOUT, preexec_fn=restrict_child)
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    log = PREFIX.with_suffix('.solver.log').read_text()
    # With -w CaDiCaL writes the competition status to this file, not stdout.
    solution_path = PREFIX.with_suffix('.model.sol')
    solution = solution_path.read_text() if solution_path.exists() else ''
    status_output = solution + '\n' + log
    status = 'UNKNOWN'
    if 's SATISFIABLE' in status_output:
        status = 'SAT'
    elif 's UNSATISFIABLE' in status_output:
        status = 'UNSAT'
    terminal = dict(status=status, returncode=result.returncode,
                    status_source=solution_path.name if solution else 'solver stdout',
                    solver_wall_seconds=time.monotonic()-run_started,
                    solver_cpu_seconds=(after.ru_utime+after.ru_stime)-(before.ru_utime+before.ru_stime),
                    scope='Exactly the saved 88-position, 16-edge boundary; 46 edges remain fixed. '
                          'One discovery-mode run; no proof log and no family-wide certification.',
                    attempts=1)
    if status == 'SAT':
        values = {abs(lit): lit > 0 for line in solution.splitlines() if line.startswith('v ')
                  for lit in map(int, line.split()[1:]) if lit}
        assert all(any(values[abs(lit)] == (lit > 0) for lit in clause) for clause in clauses)
        assignment = {p: [t for t in targets if values[primary[tuple(sorted((p, t)))]]] for p in ports}
        save('.assignment.json', assignment)
        edges, missing = build(spec, assignment)
        assert not missing
        edge_path = HERE / 'control_joint_boundary_n31.edges'
        edge_path.write_text(f'{n} {len(edges)}\n' + ''.join(f'{u} {v}\n' for u, v in sorted(edges)))

        # Independent expansion check: reread the saved graph, ordinary integer
        # matrix multiplication and all-root BFS, not the route-term encoding.
        data = [tuple(map(int, line.split())) for line in edge_path.read_text().splitlines()]
        assert data[0] == (31, 62)
        A = [[0]*n for _ in range(n)]
        for u, v in data[1:]:
            assert u != v and A[u][v] == 0
            A[u][v] = A[v][u] = 1
        assert all(sum(row) == 4 for row in A)
        A2 = [[sum(A[i][k]*A[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        A3 = [[sum(A2[i][k]*A[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        zeros = [[i, j] for i in range(n) for j in range(n) if A3[i][j] == 0]
        adj = [[j for j in range(n) if A[i][j]] for i in range(n)]
        profiles = []
        for root in range(n):
            distance = [-1]*n
            distance[root] = 0
            queue = deque([root])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if distance[v] == -1:
                        distance[v] = distance[u]+1
                        queue.append(v)
            assert -1 not in distance
            profiles.append(dict(root=root, eccentricity=max(distance),
                                 layer_sizes=[distance.count(d) for d in range(max(distance)+1)]))
        assert not zeros and max(row['eccentricity'] for row in profiles) <= 3
        verification = dict(order=n, size=len(edges), degree=4, simple=True,
                            A3_minimum=min(map(min, A3)), A3_zero_pairs=zeros,
                            diameter=max(row['eccentricity'] for row in profiles), all_root_BFS=profiles)
        save('.verification.json', verification)
        terminal.update(valid_controller=True, control_file=edge_path.name,
                        A3_minimum=verification['A3_minimum'], diameter=verification['diameter'])
    else:
        terminal.update(valid_controller=False, continued_search=False,
                        limitation='UNSAT, if returned, is an unproved solver result for this finite model only. '
                                   'UNKNOWN is terminal for this authorized attempt.')
    terminal['total_wall_seconds'] = time.monotonic()-started
    save('.terminal.json', terminal)
    print(json.dumps(terminal, indent=2), flush=True)


if __name__ == '__main__':
    main()
