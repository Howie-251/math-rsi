"""Use the complete 18,624-matching table in a single joint fixed-root design.

One new bounded input; no change of seed or extension of an earlier SAT run.
Root fiber 5 is P, outer fibers 0..4 are Q, root matchings are identity.
"""
from hs_augmentation import ROOT, ARCHIVE, dump, verify
import importlib.util
import itertools
import json
import os
import resource
import subprocess
import sys
import time


def main():
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    start = time.monotonic()
    out = ROOT / 'computations/dd82/construction/petersen_fixed_root_table_sat'
    out.mkdir(exist_ok=True)
    assert not (out / 'result.json').exists(), 'No unchanged rerun'
    spec = importlib.util.spec_from_file_location('table_counter', ARCHIVE)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    A = [5, 9, 8, 7, 6, 3, 2, 1, 0, 4]
    P = [set() for _ in range(10)]
    for u in range(5):
        P[u].update(((u + 1) % 5, (u - 1) % 5, u + 5))
        P[u + 5].update((5 + (u + 2) % 5, 5 + (u - 2) % 5, u))
    Q = [{v for v in range(10) if A[v] in P[A[u]]} for u in range(10)]
    T = [set(range(10)) - {u} - P[u] - Q[u] for u in range(10)]
    assert all(len(s) == 3 for s in T)
    table_path = ROOT / 'computations/dd82/construction/petersen_fixed_root_catalog.perms.txt'
    table = [tuple(map(int, line.split())) for line in table_path.read_text().splitlines()]
    assert len(table) == 18624 and len(set(table)) == len(table)
    for m in table:
        assert sorted(m) == list(range(10))
        inv = tuple(m.index(u) for u in range(10))
        for f in (m, inv):
            assert all(len({u, f[u]} | Q[f[u]] | {f[v] for v in Q[u]}) >= 7 for u in range(10))
    fixed = {(10 * i + u, 10 * i + v) for i in range(6)
             for u in range(10) for v in (P if i == 5 else Q)[u] if u < v}
    fixed |= {(10 * i + u, 50 + u) for i in range(5) for u in range(10)}
    assert len(fixed) == 140
    adj = [set() for _ in range(60)]
    for u, v in fixed:
        adj[u].add(v)
        adj[v].add(u)
    em = mod.CNFEmitter(out / 'input.cnf')
    variables = {(10 * i + u, 10 * j + v): em.new_var('matching_edge')
                 for i, j in itertools.combinations(range(5), 2)
                 for u in range(10) for v in range(10)}

    def edge(u, v):
        return variables.get(tuple(sorted((u, v))))

    def exactly_one(row):
        em.add_clause(*row)
        for a, b in itertools.combinations(row, 2):
            em.add_clause(-a, -b)

    # Table selectors imply their ten matching edges. Because every edge row
    # is exactly one, two distinct selectors cannot be true simultaneously.
    # Reverse support clauses make eliminated table values propagate to edges.
    selector_ranges = []
    for i, j in itertools.combinations(range(5), 2):
        for u in range(10):
            exactly_one([edge(10 * i + u, 10 * j + v) for v in range(10)])
            exactly_one([edge(10 * i + v, 10 * j + u) for v in range(10)])
        support = {(u, v): [] for u in range(10) for v in range(10)}
        selectors = []
        for m in table:
            s = em.new_var('allowed_table_entry')
            selectors.append(s)
            for u, v in enumerate(m):
                em.add_clause(-s, edge(10 * i + u, 10 * j + v))
                support[u, v].append(s)
        em.add_clause(*selectors)
        for (u, v), choices in support.items():
            em.add_clause(-edge(10 * i + u, 10 * j + v), *choices)
        selector_ranges.append(dict(fibers=[i, j], first=selectors[0], last=selectors[-1]))
    # Entrywise root residual sum_j M_ij >= T. The permutation residual and
    # off-T cost <=25 follow because the remaining row/column sum is one.
    for i in range(5):
        for u in range(10):
            for v in sorted(T[u]):
                em.add_clause(*(edge(10 * i + u, 10 * j + v) for j in range(5) if j != i))
    off_t = [q for (u, v), q in variables.items() if v % 10 not in T[u % 10]]
    thresholds = mod.unary_thresholds(em, off_t, 26, 'global_off_T_budget')
    em.add_clause(-thresholds[25])
    conjunctions = {}
    coverage_count = cap_count = 0
    for u, v in itertools.combinations(range(60), 2):
        if u // 10 == v // 10:
            continue  # Each internal Petersen graph already has diameter two.
        constants = int(v in adj[u]) + len(adj[u] & adj[v])
        terms = set()
        if edge(u, v):
            terms.add(edge(u, v))
        for w in range(60):
            if w in (u, v):
                continue
            left, right = edge(u, w), edge(v, w)
            if w in adj[u] and right:
                terms.add(right)
            elif w in adj[v] and left:
                terms.add(left)
            elif left and right:
                key = tuple(sorted((left, right)))
                if key not in conjunctions:
                    q = em.new_var('two_variable_path')
                    mod.add_iff_and(em, q, *key)
                    conjunctions[key] = q
                terms.add(conjunctions[key])
        terms = sorted(terms)
        if constants == 0:
            em.add_clause(*terms)
            coverage_count += 1
        # There are exactly eleven direct/two-step slots per source and
        # other fiber. Covering its ten vertices leaves at most two per pair.
        assert constants <= 2
        cap = 2 - constants
        counts = mod.unary_thresholds(em, terms, cap + 1, 'pair_route_cap')
        if len(counts) > cap and counts[cap] is not None:
            em.add_clause(-counts[cap])
            cap_count += 1
    em.finish()
    dump(out / 'encoding.json', dict(
        scope='Fixed A root family only; normalized P root, five Q outer fibers; all ten outer matchings independent.',
        fixed_edges=sorted(fixed), P=[sorted(s) for s in P], Q=[sorted(s) for s in Q],
        T=[sorted(s) for s in T], table=str(table_path), table_entries=len(table),
        edge_variables=[[u, v, q] for (u, v), q in variables.items()], selector_ranges=selector_ranges,
        variables=em.variable_count, clauses=em.clause_count,
        coverage_clauses=coverage_count, pair_route_caps=cap_count,
        encoding_wall_seconds=time.monotonic() - start))
    print('Encoded', em.variable_count, em.clause_count, 'in', time.monotonic() - start, flush=True)
    command = [str(ROOT / '.tools/lean-4.24.0-linux/bin/cadical'), '--lrat', '-t', '60',
               str(out / 'input.cnf'), str(out / 'proof.lrat')]

    def limits():
        resource.setrlimit(resource.RLIMIT_CPU, (60, 61))
        resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
        resource.setrlimit(resource.RLIMIT_FSIZE, (256 * 1024**2, 256 * 1024**2))

    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    started = time.monotonic()
    with (out / 'solver.log').open('w') as log:
        try:
            rc = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                preexec_fn=limits, timeout=65).returncode
        except subprocess.TimeoutExpired:
            rc = None
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = dict(status={10: 'SAT_CANDIDATE', 20: 'RAW_UNSAT', 0: 'UNKNOWN',
                          -24: 'CPU_LIMIT', -25: 'OUTPUT_LIMIT'}.get(rc, 'PROCESS_FAILURE'),
                  exit_code=rc, command=command, cpu_budget_seconds=60,
                  cpu_seconds=after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime,
                  wall_seconds=time.monotonic() - started, pinned_cpu=min(os.sched_getaffinity(0)),
                  variables=em.variable_count, clauses=em.clause_count)
    if rc == 10:
        values = {abs(lit): lit > 0 for line in (out / 'solver.log').read_text().splitlines()
                  if line.startswith('v ') for lit in map(int, line.split()[1:]) if lit}
        edges = fixed | {e for e, q in variables.items() if values[q]}
        dump(out / 'candidate.json', dict(n=60, edges=sorted(edges)))
        result['independent_graph_check'] = json.loads(verify(out / 'candidate.json'))
    elif rc == 20:
        check_command = [str(ROOT / '.tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim'),
                         '--no-trim', str(out / 'input.cnf'), str(out / 'proof.lrat')]
        checked = subprocess.run(check_command, capture_output=True, text=True, timeout=30)
        (out / 'certificate_check.log').write_text(checked.stdout + checked.stderr)
        result['certificate_check'] = dict(exit_code=checked.returncode,
             verified=checked.returncode == 20 and 's VERIFIED' in checked.stdout.splitlines())
        if result['certificate_check']['verified']:
            result['status'] = 'CHECKED_UNSAT'
    dump(out / 'result.json', result)
    print(json.dumps(result), flush=True)


if __name__ == '__main__':
    main()
