#!/usr/bin/env python3
"""Two specified templates only; preserve all preceding positive artifacts.

Linux: python3 -B probe_single_source_sink_two_families.py --directory DIR
The imported source is hash-bound. Negative results distinguish raw solve from
actual DRAT checker completion on the exact persisted final CNF.
"""
from itertools import combinations
import hashlib
import json
import os
from pathlib import Path
import platform
import signal
import socket
import subprocess
import time
import argparse

import search_single_source_sink_no_common_witness as core

CHECKER = '/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(command, seconds):
    began = time.monotonic()
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                            text=True, start_new_session=True)
    timeout = False
    try:
        stdout, _ = proc.communicate(timeout=seconds)
    except subprocess.TimeoutExpired:
        timeout = True
        os.killpg(proc.pid, signal.SIGTERM)
        try:
            stdout, _ = proc.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            stdout, _ = proc.communicate()
    return {'command': command, 'exit_code': proc.returncode, 'timeout': timeout,
            'elapsed_seconds': round(time.monotonic() - began, 3), 'stdout': stdout}


def templates():
    base = list(core.legacy_orders())[9][0]
    base = list(base)
    base.insert(base.index('y') + 1, 'hr')
    first = list(base)
    first[first.index('u1') + 1:first.index('u1') + 1] = ['h1', 'h2']
    yield 'U_gap_two_J_gap_empty', tuple(first)
    both = list(first)
    both[both.index('j1') + 1:both.index('j1') + 1] = ['l1', 'l2']
    yield 'both_gaps_two', tuple(both)


def probe(name, order, root, args):
    folder = root / name
    folder.mkdir(parents=True, exist_ok=False)
    cnf = folder / 'fixed.cnf'
    roles = {'v2': 'v2', 'k1': 'k1'}
    triples, binding, variables = core.build(order, roles, cnf)
    index = {v: i for i, v in enumerate(order)}
    deleted = {
        'U_family': {index[v] for v in ('x', 'v2', 'j1', 'j2', 'b')},
        'J_family': {index[v] for v in ('k1', 'w', 'u1', 'u2', 'a')}}
    existence = [[var for path, var in variables.items() if set(path).isdisjoint(excluded)]
                 for excluded in deleted.values()]
    core.append_clauses(cnf, existence)
    binding['after_two_existence_clauses_sha256'] = digest(cnf)
    rounds, separations = [], []
    began = time.monotonic()
    result = {'template': name, 'order': order, 'roles': roles,
              'n': len(order), 'deleted_sets': {k: sorted(v) for k, v in deleted.items()},
              'existence_clause_lengths': list(map(len, existence)), 'binding': binding}
    status = 'INCOMPLETE'
    while time.monotonic() - began < args.template_seconds:
        solved = run([args.solver, str(cnf)], args.seconds_per_solve)
        (folder / f'solve_{len(rounds):03}.log').write_text(solved['stdout'])
        if solved['timeout'] or solved['exit_code'] not in (10, 20):
            status = 'TIMEOUT' if solved['timeout'] else 'ERROR'
            break
        if solved['exit_code'] == 20:
            status = 'RAW_UNSAT'
            break
        literals = [int(v) for line in solved['stdout'].splitlines() if line.startswith('v ')
                    for v in line[2:].split() if int(v)]
        positive = {v for v in literals if v > 0}
        assert set(triples.values()) <= {abs(v) for v in literals}
        colors = {t: v in positive for t, v in triples.items()}
        actual, disjoint = core.actual_r6_and_disjoint(colors, len(order))
        row = {'round': len(rounds), 'actual_R6_count': len(actual),
               'disjoint_pairs': len(disjoint)}
        rounds.append(row)
        if not disjoint:
            validation = core.verify(order, roles, colors)
            family_checks = {key: bool(value['R6']) for key, value in
                             validation['five_vertex_deletion_families'].items()}
            assert validation['all_pass'] and all(family_checks.values())
            status = 'SAT_EXHAUSTIVELY_VERIFIED'
            model = {'scope': 'One ordered rank-3 signotope, not a geometric realization',
                     'order': order, 'red_triples': [t for t, c in colors.items() if c],
                     'blue_triples': [t for t, c in colors.items() if not c],
                     'solver_signed_assignment': literals,
                     'independent_exhaustive_validation': validation,
                     'two_families_nonempty': family_checks}
            (folder / 'witness.json').write_text(json.dumps(model, indent=2) + '\n')
            result['witness_sha256'] = digest(folder / 'witness.json')
            break
        clauses = [(-variables[p], -variables[q]) for p, q in disjoint]
        core.append_clauses(cnf, clauses)
        separations.extend([list(p), list(q)] for p, q in disjoint)
    (folder / 'separated_disjoint_R6_pairs.json').write_text(json.dumps(separations) + '\n')
    result.update({'status': status, 'cegar': rounds,
                   'separation_clauses_added': len(separations),
                   'elapsed_seconds': round(time.monotonic() - began, 3),
                   'final_cnf_sha256': digest(cnf), 'final_cnf_path': str(cnf)})
    if status == 'RAW_UNSAT':
        proof = folder / 'fixed.drat'
        proof_run = run([args.solver, str(cnf), str(proof)], args.proof_seconds)
        (folder / 'proof_solver.log').write_text(proof_run.pop('stdout'))
        result['proof_solver'] = proof_run
        if proof_run['exit_code'] == 20 and not proof_run['timeout'] and proof.exists():
            result['proof_sha256'] = digest(proof)
            checked = run([args.checker, str(cnf), str(proof)], args.proof_seconds)
            checker_text = checked.pop('stdout')
            (folder / 'drat_checker.log').write_text(checker_text)
            checked['reported_verified'] = 's VERIFIED' in checker_text
            result['drat_checker'] = checked
            if checked['exit_code'] == 0 and not checked['timeout'] and checked['reported_verified']:
                result['status'] = 'FIXED_CNF_DRAT_CHECKED_UNSAT'
    (folder / 'result.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--solver', default=core.SOLVER)
    parser.add_argument('--checker', default=CHECKER)
    parser.add_argument('--seconds-per-solve', type=float, default=45)
    parser.add_argument('--template-seconds', type=float, default=180)
    parser.add_argument('--proof-seconds', type=float, default=90)
    args = parser.parse_args()
    assert platform.system() == 'Linux'
    args.directory.mkdir(parents=True, exist_ok=False)
    metadata = {'scope': 'Only two specified finite templates; no general nonexistence claim',
                'hostname': socket.gethostname(), 'python': platform.python_version(),
                'driver_sha256': digest(__file__), 'imported_core_sha256': digest(core.__file__),
                'solver_sha256': digest(args.solver), 'checker_sha256': digest(args.checker)}
    results = []
    for name, order in templates():
        result = probe(name, order, args.directory, args)
        results.append(result)
        if result['status'] == 'SAT_EXHAUSTIVELY_VERIFIED':
            break
    metadata['results'] = results
    (args.directory / 'SUMMARY.json').write_text(json.dumps(metadata, indent=2) + '\n')


if __name__ == '__main__':
    main()
