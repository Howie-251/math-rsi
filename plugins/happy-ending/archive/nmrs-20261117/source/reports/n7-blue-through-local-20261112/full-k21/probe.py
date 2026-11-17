"""One literal twenty-one-point actual blue-through probe; execute on Linux only."""
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
VERTICES = tuple(range(1, 22))


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
    blue_paths = tuple(combinations(VERTICES, 5))
    blue_selectors = {}
    for path in blue_paths:
        count += 1
        blue_selectors[path] = count
        for v in terms(path):
            add('exact_B5_selector_forward', (-count, -v))
        add('exact_B5_selector_reverse', (count,) + terms(path))
    source, terminal, through = {}, {}, {}
    for table in (source, terminal, through):
        for v in VERTICES:
            count += 1
            table[v] = count
    for path, selector in blue_selectors.items():
        add('B5_implies_source', (-selector, source[path[0]]))
        add('B5_implies_terminal', (-selector, terminal[path[-1]]))
    for v in VERTICES:
        add('exact_B5_source', (-source[v],) + tuple(s for path, s in blue_selectors.items() if path[0] == v))
        add('exact_B5_terminal', (-terminal[v],) + tuple(s for path, s in blue_selectors.items() if path[-1] == v))
        add('K_requires_source', (-through[v], source[v]))
        add('K_requires_terminal', (-through[v], terminal[v]))
        add('source_terminal_implies_K', (through[v], -source[v], -terminal[v]))
    choices = []
    for path, selector in blue_selectors.items():
        count += 1
        choices.append(count)
        add('central_witness_requires_B5', (-count, selector))
        for v in path:
            add('central_witness_requires_K', (-count, through[v]))
    add('actual_B5_inside_actual_K', choices)
    for path in combinations(VERTICES, 5):
        add('no_R5_between_K', (-through[path[0]], -through[path[-1]]) + tuple(-v for v in terms(path)))
    for path in combinations(VERTICES, 6):
        for v in (path[0], path[-1]):
            add('K_no_R6_endpoint', (-through[v],) + tuple(-x for x in terms(path)))
    ordered = sorted(clauses)
    formula = 'p cnf %d %d\n' % (count, len(ordered))
    formula += ''.join(' '.join(map(str, clause)) + ' 0\n' for clause in ordered)
    spec = dict(n=21, numbering='true=red; lex triples, weak red endpoint flags, exact B5 path selectors, B5 source/end/K, central witnesses',
                color_variables=len(color), variables=count, clauses=len(ordered), group_emissions=groups,
                K_flags=through, B5_source_flags=source, B5_terminal_flags=terminal,
                scope='A real B5 inside the actual finite blue-five-through set. No virtual anchors, no position restriction, no 75-point extension claim.')
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
