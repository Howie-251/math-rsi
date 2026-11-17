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
VERTICES = tuple(range(1, 20))
A = frozenset(range(6, 11))
B = frozenset(range(10, 15))
T = A | B


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
    for path in combinations(VERTICES, 4):
        if path[-1] in A:
            add('A_no_in_B4', terms(path))
        if path[0] in B:
            add('B_no_out_B4', terms(path))
        if path[0] in T and path[-1] in T:
            add('no_T_to_T_B4', terms(path))
    for path in combinations(VERTICES, 5):
        if path[0] in T or path[-1] in T:
            add('T_no_B5_endpoints', terms(path))
    for path in combinations(VERTICES, 6):
        if path[-1] < 10 and path[-2] in T:
            add('early_R6_no_T_penultimate', (-v for v in terms(path)))
        if path[0] > 10 and path[1] in T:
            add('late_R6_no_T_second', (-v for v in terms(path)))
    frozen = (tuple(range(1, 7)), tuple(range(14, 20)),
              tuple(range(6, 11)), tuple(range(10, 15)))
    for path in frozen:
        for variable in terms(path):
            add('frozen_R_paths', (variable,))
    for x in range(1, 5):
        add('left_ambient_B5_red_fan', (color[x, 5, 6],))
    for y in range(16, 20):
        add('right_ambient_B5_red_fan', (color[14, 15, y],))
    ordered = sorted(clauses)
    formula = 'p cnf %d %d\n' % (count, len(ordered))
    formula += ''.join(' '.join(map(str, clause)) + ' 0\n' for clause in ordered)
    spec = dict(n=19, numbering='one-based physical vertices, true=red; lexicographic triple colors then R4/R5/R6 endpoint flags',
                vertices=VERTICES, L=list(range(1, 6)), A=sorted(A), pivot=10, B=sorted(B),
                R=list(range(15, 20)), T=sorted(T), frozen_red_paths=frozen,
                color_variables=len(color), variables=count, clauses=len(ordered),
                group_emissions=groups,
                scope='Only the explicitly requested induced-domain necessary conditions; no local full T anchors, no no-B5 assumption, no ambient extension claim.')
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
