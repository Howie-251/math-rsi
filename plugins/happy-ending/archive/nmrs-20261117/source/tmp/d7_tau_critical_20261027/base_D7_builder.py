"""One complete D7 decision; all scientific execution is Linux-only."""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import os
import platform
import resource
import signal
import subprocess
import time

from semantic_check import fixture_checks, check_assignment

HERE = Path(__file__).resolve().parent
SOLVER = Path('/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat')
N = 30


def sha(p):
    with p.open('rb') as stream: return hashlib.file_digest(stream, 'sha256').hexdigest()


def save(name, data):
    with (HERE / name).open('x') as out: json.dump(data, out, indent=2)


def build():
    ledger, ids, groups = [], {}, Counter()
    def variable(key):
        key = tuple(key)
        if key not in ids:
            ids[key] = len(ledger) + 1
            ledger.append({'id': ids[key], 'key': key})
        return ids[key]
    triples = {t: variable(('triple', *t)) for t in combinations(range(N), 3)}
    def color(c, t): return triples[tuple(t)] * (1 if c == 'R' else -1)
    def reach(c, a, i, j, length):
        if length == 3: return color(c, (a, i, j))
        return variable(('reach', c, a, i, j, length))
    def q(c, a, j, length): return variable(('endpoint', c, a, j, length))
    body = HERE / 'decision.body'
    with body.open('x') as out:
        def clause(group, lits):
            values = set(lits)
            if any(-v in values for v in values): return
            out.write(' '.join(map(str, sorted(values, key=lambda v: (abs(v), v)))) + ' 0\n')
            groups[group] += 1
        for packet in combinations(range(N), 4):
            vs = [triples[t] for t in combinations(packet, 3)]
            for bits in product((False, True), repeat=4):
                if sum(x != y for x, y in zip(bits, bits[1:])) > 1:
                    clause('packets', [-v if b else v for v, b in zip(vs, bits)])
        for c, maximum in [('R', 7), ('B', 5)]:
            for length in range(4, maximum + 1):
                for a, i, j in combinations(range(N), 3):
                    if i - a < length - 2: continue
                    dst = reach(c, a, i, j, length)
                    for h in range(a + length - 3, i):
                        prev = reach(c, a, h, i, length - 1)
                        clause('reach_' + c + str(length), [-prev, -color(c, (h, i, j)), dst])
                    if length == maximum: clause('no_' + c + str(maximum), [-dst])
        for c, length in [('R', 5), ('R', 6), ('B', 3), ('B', 4)]:
            for a, i, j in combinations(range(N), 3):
                if i - a < length - 2: continue
                literal = reach(c, a, i, j, length)
                clause('endpoint_' + c + str(length), [-literal, q(c, a, j, length)])
                if (c, length) == ('R', 5): clause('EndR5', [-literal, variable(('EndR5', j))])
                if (c, length) == ('B', 4): clause('SrcB4', [-literal, variable(('SrcB4', a))])
        for a, j in combinations(range(N), 2):
            if j - a >= 4: clause('no_weak_R5B4', [-q('R', a, j, 5), -q('B', a, j, 4)])
            if j - a >= 5: clause('no_weak_R6B3', [-q('R', a, j, 6), -q('B', a, j, 3)])
        for v in range(N): clause('D7_no_joint', [-variable(('EndR5', v)), -variable(('SrcB4', v))])
    cnf = HERE / 'decision.cnf'
    with cnf.open('xb') as out, body.open('rb') as src:
        out.write(f'p cnf {len(ledger)} {sum(groups.values())}\n'.encode())
        import shutil
        shutil.copyfileobj(src, out)
    save('variable_ledger.json', ledger)
    binding = {'schema': 'complete_D7_forward_reach_order30_v1', 'n': N,
               'variables': len(ledger), 'clauses': sum(groups.values()), 'groups': dict(groups),
               'triple_colors': len(triples), 'packets': 27405,
               'no_extra_criticality_or_template': True,
               'source_bindings': {p.name: sha(p) for p in [Path(__file__), HERE / 'semantic_check.py',
                   HERE / 'MATHEMATICAL_ENCODING_SPEC.md', SOLVER]},
               'cnf_sha256': sha(cnf), 'ledger_sha256': sha(HERE / 'variable_ledger.json'),
               'theorem_credit': False, 'production_accepted': False}
    save('decision_binding.json', binding)
    return triples, binding


def controlled(command, label, seconds, memory_gib=3):
    def limits():
        resource.setrlimit(resource.RLIMIT_CPU, (seconds, seconds))
        resource.setrlimit(resource.RLIMIT_AS, (memory_gib * 1024**3,) * 2)
        os.sched_setaffinity(0, sorted(os.sched_getaffinity(0))[:2])
    start = time.monotonic()
    with (HERE / (label + '.stdout')).open('x') as out, (HERE / (label + '.stderr')).open('x') as err:
        proc = subprocess.Popen(command, stdout=out, stderr=err, start_new_session=True, preexec_fn=limits)
        save(label + '_launch.json', {'pid': proc.pid, 'pgid': proc.pid, 'command': command,
             'budget_seconds': seconds, 'memory_gib': memory_gib, 'start_epoch': time.time()})
        timeout = False
        try: proc.wait(timeout=seconds)
        except subprocess.TimeoutExpired:
            timeout = True
            os.killpg(proc.pid, signal.SIGTERM)
            try: proc.wait(timeout=2)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                proc.wait(timeout=2)
    return {'command': command, 'exit_code': proc.returncode, 'timed_out': timeout,
            'elapsed_seconds': time.monotonic() - start,
            'stdout_sha256': sha(HERE / (label + '.stdout')),
            'stderr_sha256': sha(HERE / (label + '.stderr'))}


def main():
    if platform.system() != 'Linux': raise RuntimeError('Linux scientific execution required')
    if (HERE / 'decision_result.json').exists() or (HERE / 'solver_launch.json').exists():
        raise FileExistsError('one-shot decision already started')
    save('fixture_checks.json', fixture_checks())
    triples, binding = build()
    report = {'schema': 'D7_order30_single_decision_result_v1', 'binding': binding,
              'theorem_credit': False, 'independent_review': False, 'production_accepted': False,
              'max_solver_invocations': 1, 'status': 'STARTING'}
    save('prepared.json', report)
    run = controlled([str(SOLVER), '--time=300', str(HERE / 'decision.cnf'),
                      str(HERE / 'decision.drat')], 'solver', 300)
    report['solver'] = run
    raw = (HERE / 'solver.stdout').read_text()
    if run['exit_code'] == 10 and 's SATISFIABLE' in raw:
        model = {}
        for line in raw.splitlines():
            if line.startswith('v '):
                for token in line.split()[1:]:
                    value = int(token)
                    if value: model[abs(value)] = value > 0
        if set(model) != set(range(1, binding['variables'] + 1)): raise ValueError('incomplete SAT assignment')
        checked = 0
        with (HERE / 'decision.cnf').open() as src:
            for line in src:
                if line.startswith('p'): continue
                lits = [int(v) for v in line.split()[:-1]]
                if not any(model[abs(v)] == (v > 0) for v in lits): raise ValueError('CNF assignment violation')
                checked += 1
        assignment = {'n': N, 'colors': [{'triple': t, 'red': model[v]} for t, v in triples.items()]}
        save('sat_assignment.json', assignment)
        save('full_model.json', model)
        semantic = check_assignment(HERE / 'sat_assignment.json')
        save('sat_semantic_result.json', semantic)
        report.update(status='SAT_SEMANTIC_CHECKED' if semantic['D7_valid'] else 'SAT_INVALID',
                      clausewise_checked=checked, semantic_valid=semantic['D7_valid'])
    elif run['exit_code'] == 20 and 's UNSATISFIABLE' in raw:
        report['status'] = 'RAW_UNSAT_UNACCEPTED'
        proof = HERE / 'decision.drat'
        report['proof'] = {'exists': proof.is_file(), 'bytes': proof.stat().st_size if proof.exists() else 0,
                           'sha256': sha(proof) if proof.exists() else None}
        candidates = [Path('/data/ktqiu_hdd/math_agent/drat-trim/drat-trim'),
            Path('/data/ktqiu_hdd/math_agent/cadical-sc2025/test/cnf/drat-trim'),
            HERE.parent / 'balanced49_saturated_exchange_20261026/drat-trim']
        checker = next((p for p in candidates if p.is_file() and os.access(p, os.X_OK)), None)
        if checker and report['proof']['bytes']:
            report['proof_checker'] = {'path': str(checker), 'sha256': sha(checker)}
            checked = controlled([str(checker), str(HERE / 'decision.cnf'), str(proof), '-t', '60'],
                                 'proof_check', 65)
            report['proof_check'] = checked
            verified = checked['exit_code'] == 0 and 's VERIFIED' in (HERE / 'proof_check.stdout').read_text()
            if verified: report['status'] = 'UNSAT_PROOF_CHECKED_UNACCEPTED'
        else: report['proof_check'] = {'status': 'UNAVAILABLE', 'reason': 'retained checker or nonempty proof absent'}
    else: report['status'] = 'TIMEOUT_UNDECIDED' if run['timed_out'] or run['exit_code'] in (0, -9, -15, -24) else 'EXECUTION_ERROR'
    report['final_cnf_sha256'] = sha(HERE / 'decision.cnf')
    assert report['final_cnf_sha256'] == binding['cnf_sha256']
    save('decision_result.json', report)
    print(json.dumps({'status': report['status'], 'solver': run, 'variables': binding['variables'],
                      'clauses': binding['clauses']}, indent=2), flush=True)


if __name__ == '__main__': main()
