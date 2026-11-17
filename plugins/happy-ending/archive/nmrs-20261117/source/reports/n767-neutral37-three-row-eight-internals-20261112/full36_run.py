"""Run all 36 exterior label orders, at most two controlled jobs at once.

Run only on the authoritative Linux host in a fresh evidence directory.
The directory must also contain full36_schema.py and full36_semantic_check.py.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
from itertools import permutations
import json
import os
from pathlib import Path
import platform
import re
import signal
import socket
import subprocess
import sys
import threading
import time

import full36_schema as schema
from full36_semantic_check import check_dimacs, inspect_sat

SOLVER = '/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat'
CHECKER = '/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim'
ROOT = Path(__file__).resolve().parent
STOP = threading.Event()


def sha256(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for data in iter(lambda: stream.read(1024*1024), b''):
            digest.update(data)
    return digest.hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2)+'\n', encoding='utf-8')


def controlled(command, prefix, limit):
    stdout_path = Path(str(prefix)+'.stdout')
    stderr_path = Path(str(prefix)+'.stderr')
    began = time.monotonic()
    killed = False
    with stdout_path.open('w') as stdout, stderr_path.open('w') as stderr:
        process = subprocess.Popen(command, stdout=stdout, stderr=stderr,
                                   start_new_session=True)
        try:
            process.wait(timeout=limit)
        except subprocess.TimeoutExpired:
            killed = True
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
    return {'command': command, 'exit_code': process.returncode,
            'timeout_killed': killed, 'elapsed_seconds': time.monotonic()-began,
            'stdout_path': str(stdout_path), 'stderr_path': str(stderr_path),
            'stdout_sha256': sha256(stdout_path), 'stderr_sha256': sha256(stderr_path),
            'stdout': stdout_path.read_text(), 'stderr': stderr_path.read_text()}


def prepare(index, sources, terminals):
    directory = ROOT/('case-%02d' % index)
    directory.mkdir()
    cnf = directory/'formula.cnf'
    text, metadata = schema.build(sources, terminals)
    cnf.write_text(text, encoding='ascii')
    write_json(directory/'schema-map.json', metadata)
    semantic = check_dimacs(cnf, sources, terminals)
    write_json(directory/'semantic-check.json', semantic)
    result = {'index': index, 'sources': sources, 'terminals': terminals,
              'pool': tuple(range(3, 11)), 'cnf': str(cnf),
              'cnf_sha256': sha256(cnf), 'cnf_bytes': cnf.stat().st_size,
              'variables': metadata['variables'], 'clauses': metadata['clauses'],
              'schema_map_sha256': sha256(directory/'schema-map.json'),
              'semantic_check': semantic, 'attempts': [], 'proof_checked': False,
              'status': 'PREPARED' if semantic['pass'] else 'SCHEMA_MISMATCH'}
    write_json(directory/'result.json', result)
    return result


def run_case(result):
    if STOP.is_set():
        result['status'] = 'SKIPPED_AFTER_SAT'
        return result
    if not result['semantic_check']['pass']:
        STOP.set()
        return result
    directory = Path(result['cnf']).parent
    cnf = Path(result['cnf'])
    for attempt, seconds in enumerate((60, 180), 1):
        proof = directory/('proof-attempt-%d.drat' % attempt)
        command = [SOLVER, '--no-binary', '--time='+str(seconds), str(cnf), str(proof)]
        solve = controlled(command, directory/('solve-%d' % attempt), seconds+8)
        status = ('SAT' if re.search(r'^s SATISFIABLE\s*$', solve['stdout'], re.M)
                  else 'RAW_UNSAT' if re.search(r'^s UNSATISFIABLE\s*$', solve['stdout'], re.M)
                  else 'UNKNOWN')
        item = {'solver': solve, 'solver_status': status,
                'proof_path': str(proof), 'proof_bytes': proof.stat().st_size if proof.exists() else None,
                'proof_sha256': sha256(proof) if proof.exists() else None,
                'checker_attempts': []}
        result['attempts'].append(item)
        if status == 'SAT':
            model = {int(v) for line in solve['stdout'].splitlines() if line.startswith('v ')
                     for v in line[2:].split() if int(v) != 0}
            clause_ok = True
            for line in cnf.read_text().splitlines():
                if line and not line.startswith(('p', 'c')):
                    clause_ok &= any(int(v) in model for v in line.split()[:-1])
            witness = inspect_sat(model, result['sources'], result['terminals'])
            write_json(directory/'sat-witness.json', witness)
            result['model_satisfies_actual_dimacs'] = clause_ok
            result['sat_witness'] = witness
            result['status'] = 'SAT_WITNESS_VERIFIED' if clause_ok and witness['all_checks_pass'] else 'SAT_CHECK_FAILED'
            STOP.set()
            break
        if status == 'RAW_UNSAT':
            if solve['exit_code'] != 20 or not proof.is_file():
                result['status'] = 'UNSAT_PROOF_MISSING_OR_BAD_EXIT'
                break
            for check_attempt, check_seconds in enumerate((120, 600), 1):
                before = {'cnf': sha256(cnf), 'proof': sha256(proof)}
                check = controlled([CHECKER, str(cnf), str(proof), '-t', str(check_seconds)],
                                   directory/('check-%d-%d' % (attempt, check_attempt)), check_seconds+8)
                after = {'cnf': sha256(cnf), 'proof': sha256(proof)}
                check['input_hashes_before'] = before
                check['input_hashes_after'] = after
                check['bound_to_prepared_cnf'] = before['cnf'] == result['cnf_sha256']
                check['input_hashes_unchanged'] = before == after
                check['verified_line_count'] = len(re.findall(r'^s VERIFIED\s*$', check['stdout'], re.M))
                check['success'] = (check['exit_code'] == 0 and check['verified_line_count'] == 1
                                    and check['bound_to_prepared_cnf'] and check['input_hashes_unchanged'])
                item['checker_attempts'].append(check)
                if check['success']:
                    result['proof_checked'] = True
                    result['status'] = 'CHECKED_UNSAT'
                    result['accepted_proof_path'] = str(proof)
                    result['accepted_proof_sha256'] = before['proof']
                    result['accepted_checker_stdout_path'] = check['stdout_path']
                    break
                # Extend only a genuine timeout, never hide checker rejection.
                if not check['timeout_killed'] and 'time limit' not in (check['stdout']+check['stderr']).lower():
                    break
            if not result['proof_checked']:
                result['status'] = 'CHECKER_INCOMPLETE_OR_REJECTED'
            break
        result['status'] = 'UNKNOWN'
    result['cnf_sha256_after'] = sha256(cnf)
    if result['cnf_sha256_after'] != result['cnf_sha256']:
        result['status'] = 'CNF_CHANGED'
        result['proof_checked'] = False
    write_json(directory/'result.json', result)
    return result


def main():
    began = time.monotonic()
    source_files = [ROOT/name for name in
                    ('full36_schema.py', 'full36_semantic_check.py', 'full36_run.py')]
    tool_before = {path: sha256(path) for path in (SOLVER, CHECKER)}
    source_before = {path.name: sha256(path) for path in source_files}
    branches = [(sources, terminals) for sources in permutations((0,1,2))
                for terminals in permutations((11,12,13))]
    write_json(ROOT/'progress.json', {'phase': 'preparing', 'prepared': 0, 'completed': 0})
    prepared = []
    for index, (sources, terminals) in enumerate(branches):
        case = prepare(index, sources, terminals)
        prepared.append(case)
        write_json(ROOT/'progress.json', {'phase': 'preparing', 'prepared': len(prepared), 'completed': 0})
        if not case['semantic_check']['pass']:
            break
    results = []
    if len(prepared) == 36 and all(c['semantic_check']['pass'] for c in prepared):
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(run_case, case) for case in prepared]
            for future in as_completed(futures):
                result = future.result()
                results.append(result)
                write_json(ROOT/'progress.json', {
                    'phase': 'solve_and_check', 'prepared': 36, 'completed': len(results),
                    'checked_unsat': sum(c['status'] == 'CHECKED_UNSAT' for c in results),
                    'statuses': [{'index': c['index'], 'status': c['status']} for c in sorted(results, key=lambda c:c['index'])]})
    else:
        results = prepared
    results.sort(key=lambda case: case['index'])
    tool_after = {path: sha256(path) for path in (SOLVER, CHECKER)}
    source_after = {path.name: sha256(path) for path in source_files}
    checked = (len(results) == 36 and all(c['status'] == 'CHECKED_UNSAT' for c in results)
               and tool_before == tool_after and source_before == source_after)
    report = {'scope': 'Only external three sources, eight middle pool vertices, external three terminals; all 36 logical label orders. Abstract ordered rank-3 signotopes, no global 767 bound.',
              'status': 'ALL_36_CHECKED_UNSAT' if checked else 'SAT_WITNESS_VERIFIED' if any(c['status'] == 'SAT_WITNESS_VERIFIED' for c in results) else 'INCOMPLETE',
              'execution': {'root': str(ROOT), 'host': socket.gethostname(), 'platform': platform.platform(),
                            'python_executable': sys.executable, 'python_version': sys.version,
                            'concurrency': 2, 'elapsed_seconds': time.monotonic()-began,
                            'tool_sha256_before': tool_before, 'tool_sha256_after': tool_after,
                            'source_sha256_before': source_before, 'source_sha256_after': source_after},
              'planned_branch_count': len(branches), 'branch_count': len(results),
              'schema_semantics_all_pass': len(results) == 36 and all(c['semantic_check']['pass'] for c in results),
              'checked_unsat_count': sum(c['status'] == 'CHECKED_UNSAT' for c in results),
              'proof_total_bytes': sum(Path(c['accepted_proof_path']).stat().st_size for c in results if c.get('accepted_proof_path')),
              'interleaved_or_internal_endpoint_orders_not_covered': True,
              'cases': results}
    write_json(ROOT/'full36-result.json', report)
    write_json(ROOT/'progress.json', {'phase': 'finished', 'status': report['status'],
                                     'completed': len(results), 'checked_unsat': report['checked_unsat_count']})
    print(json.dumps(report, indent=2))
    return 0 if checked or report['status'] == 'SAT_WITNESS_VERIFIED' else 1


if __name__ == '__main__':
    sys.exit(main())
