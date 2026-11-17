"""One literal nineteen-point necessary-domain probe; execute on Linux only."""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import os
import platform
import signal
import socket
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
SOLVER = Path('/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat')
CHECKER = Path('/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim')
VERTICES = tuple(range(1, 26))


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def write(name, value):
    path = ROOT / name
    temporary = path.with_name(path.name + '.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.replace(path)


def build():
    triples = tuple(combinations(VERTICES, 3))
    color = {triple: i + 1 for i, triple in enumerate(triples)}
    count = len(triples)
    flags = {}
    for length in (4, 5, 6):
        for edge in combinations(VERTICES, 2):
            count += 1
            flags[length, edge] = count
    clauses = set()
    groups = {}

    def add(group, literals):
        clause = frozenset(literals)
        assert not any(-x in clause for x in clause)
        normalized = tuple(sorted(clause))
        groups[group] = groups.get(group, 0) + 1
        clauses.add(normalized)

    def terms(path):
        return tuple(color[path[i:i + 3]] for i in range(len(path) - 2))

    for four in combinations(VERTICES, 4):
        variables = tuple(color[triple] for triple in combinations(four, 3))
        for mask in range(16):
            bits = tuple((mask >> i) & 1 for i in range(4))
            if sum(x != y for x, y in zip(bits, bits[1:])) > 1:
                add('packet', (-v if b else v for v, b in zip(variables, bits)))
    for path in combinations(VERTICES, 7):
        add('no_R7', (-v for v in terms(path)))
    for path in combinations(VERTICES, 6):
        add('no_B6', terms(path))
    for length in (4, 5, 6):
        for path in combinations(VERTICES, length):
            add('R%d_implies_endpoint_flag' % length,
                tuple(-v for v in terms(path)) + (flags[length, (path[0], path[-1])],))
        for blue in combinations(VERTICES, 9 - length):
            add('weak_R%d_B%d' % (length, 9 - length),
                (-flags[length, (blue[0], blue[-1])],) + terms(blue))
    count += 1
    truth = count
    add('true_constant', (truth,))
    def conjunction(x, y):
        nonlocal count
        count += 1
        z = count
        add('and_gate', (-z, x)); add('and_gate', (-z, y)); add('and_gate', (z, -x, -y))
        return z
    def disjunction(xs):
        nonlocal count
        count += 1
        z = count
        for x in xs: add('or_gate', (-x, z))
        add('or_gate', (-z,) + tuple(xs))
        return z
    roles = {}
    for red, height, name in ((True, 6, 'R6'), (False, 5, 'B5')):
        for direction in ('out', 'in'):
            state = {(2, edge): truth for edge in combinations(VERTICES, 2)}
            for length in range(3, height+1):
                for first, last in combinations(VERTICES, 2):
                    terms_here = []
                    for third in VERTICES:
                        if direction == 'out' and third > last:
                            edge, triple = (last, third), (first, last, third)
                        elif direction == 'in' and third < first:
                            edge, triple = (third, first), (third, first, last)
                        else: continue
                        literal = color[triple] if red else -color[triple]
                        terms_here.append(literal if length == 3 else conjunction(state[length-1, edge], literal))
                    state[length, (first, last)] = disjunction(terms_here)
            roles[name+'_'+direction] = {}
            for x in VERTICES:
                ids = [state[height, edge] for edge in combinations(VERTICES, 2)
                       if edge[0 if direction=='out' else 1] == x]
                roles[name+'_'+direction][x] = disjunction(ids)
    through, active = {}, {}
    for x in VERTICES:
        through[x] = conjunction(roles['B5_out'][x], roles['B5_in'][x])
        active[x] = disjunction([roles[name][x] for name in ('R6_out','R6_in','B5_out','B5_in')])
        add('H_no_R6_source', (-through[x], -roles['R6_out'][x]))
        add('H_no_R6_terminal', (-through[x], -roles['R6_in'][x]))
    inputs = list(through.values()) + list(active.values())
    threshold = len(VERTICES)+11
    counters = {(0,0): truth}
    for j,x in enumerate(inputs,1):
        counters[j,0] = truth
        for k in range(1,min(j,threshold)+1):
            same = counters.get((j-1,k),-truth)
            lower = counters.get((j-1,k-1),-truth)
            counters[j,k] = disjunction((same,conjunction(lower,x)))
    add('h_minus_i_at_least_11', (counters[len(inputs),threshold],))
    for path in combinations(VERTICES,5):
        add('no_R5_between_H', (-through[path[0]],-through[path[-1]])+tuple(-v for v in terms(path)))
    ordered = sorted(clauses)
    formula = 'p cnf %d %d\n' % (count, len(ordered))
    formula += ''.join(' '.join(map(str, clause)) + ' 0\n' for clause in ordered)
    spec = dict(n=25, variables=count, clauses=len(ordered), color_variables=len(color),
                group_emissions=groups, exact_roles=roles, H_flags=through, active_flags=active,
                scope='One free physical model; exact R6 and B5 source/end DP circuits; h-i>=11.')
    return formula, spec


def controlled(command, prefix, seconds):
    begin = time.monotonic()
    killed = False
    out_path, err_path = ROOT / (prefix + '.stdout'), ROOT / (prefix + '.stderr')
    with out_path.open('w') as out, err_path.open('w') as err:
        process = subprocess.Popen([str(x) for x in command], stdout=out, stderr=err,
                                   start_new_session=True)
        try:
            process.wait(timeout=seconds)
        except subprocess.TimeoutExpired:
            killed = True
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
    return dict(command=[str(x) for x in command], exit_code=process.returncode,
                timeout_killed=killed, seconds=time.monotonic() - begin,
                stdout_sha256=sha(out_path), stderr_sha256=sha(err_path))


def main():
    assert platform.system() == 'Linux'
    assert not (ROOT / 'formula.cnf').exists(), 'Create-only probe: refuse rerun'
    begin = time.monotonic()
    write('runtime.json', dict(host=socket.gethostname(), platform=platform.platform(),
          python=sys.executable, bindings={str(p): sha(p) for p in
          (Path(__file__), ROOT / 'verify.py', SOLVER, CHECKER)}))
    write('status.json', dict(stage='building'))
    formula, spec = build()
    cnf = ROOT / 'formula.cnf'
    cnf.write_text(formula, encoding='ascii')
    write('spec.json', spec)
    result = dict(status='PRECHECK', cnf_sha256=sha(cnf), source_sha256=sha(__file__),
                  verifier_sha256=sha(ROOT / 'verify.py'))
    result['schema_audit'] = controlled([sys.executable, '-B', ROOT / 'verify.py', '--schema'],
                                        'schema-audit', 90)
    assert result['schema_audit']['exit_code'] == 0, 'Independent schema audit rejected'
    write('status.json', dict(stage='solving', variables=spec['variables'], clauses=spec['clauses']))
    result['solve'] = controlled([SOLVER, '--no-binary', '--time=60', cnf, ROOT / 'proof.drat'],
                                 'solve', 75)
    stdout = (ROOT / 'solve.stdout').read_text()
    if '\ns SATISFIABLE\n' in '\n' + stdout:
        result['status'] = 'SAT_PENDING_INDEPENDENT_CHECK'
        write('result.json', result)
        write('status.json', dict(stage='independent_sat_audit'))
        result['sat_audit'] = controlled([sys.executable, '-B', ROOT / 'verify.py', '--sat'],
                                         'sat-audit', 120)
        if (result['sat_audit']['exit_code'] == 0 and not result['sat_audit']['timeout_killed']
                and result['solve']['exit_code'] == 10 and not result['solve']['timeout_killed']):
            result['status'] = 'VERIFIED_SAT_NECESSARY_SUBDOMAIN'
    elif '\ns UNSATISFIABLE\n' in '\n' + stdout:
        result['status'] = 'RAW_UNSAT'
        write('result.json', result)
        write('status.json', dict(stage='drat_check'))
        result['check'] = controlled([CHECKER, cnf, ROOT / 'proof.drat', '-t', '180'], 'check', 190)
        checked = (ROOT / 'check.stdout').read_text()
        if (result['check']['exit_code'] == 0 and not result['check']['timeout_killed']
                and result['solve']['exit_code'] == 20 and not result['solve']['timeout_killed']
                and '\ns VERIFIED\n' in '\n' + checked):
            result['status'] = 'CHECKED_UNSAT_NECESSARY_SUBDOMAIN'
    else:
        result['status'] = 'UNKNOWN'
    result['elapsed_seconds'] = time.monotonic() - begin
    result['bindings'] = {p.name: dict(bytes=p.stat().st_size, sha256=sha(p))
                          for p in sorted(ROOT.iterdir()) if p.is_file()
                          and p.name not in ('result.json', 'status.json', 'done.json')}
    write('result.json', result)
    write('status.json', dict(stage='done', result=result['status']))
    write('done.json', dict(status=result['status'], elapsed_seconds=time.monotonic() - begin))
    print(json.dumps(dict(status=result['status'], elapsed_seconds=time.monotonic() - begin)), flush=True)


if __name__ == '__main__':
    main()
