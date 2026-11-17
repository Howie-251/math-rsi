"""Check a text DRUP trace using only incremental MiniSat22 unit propagation."""

from argparse import ArgumentParser
from hashlib import file_digest
import json
import os
from pathlib import Path
import tempfile
from time import monotonic, process_time


HERE = Path(__file__).resolve().parent
for name in ('TMP', 'TEMP', 'TMPDIR'):
    os.environ[name] = str(HERE)
tempfile.tempdir = str(HERE)

from pysat.solvers import Minisat22


def parse_clause(tokens, num_vars):
    fields = tuple(map(int, tokens))
    if not fields or fields[-1] != 0 or any(x == 0 or abs(x) > num_vars for x in fields[:-1]):
        raise ValueError('invalid clause or literal outside the declared CNF domain')
    return fields[:-1]


def read_cnf(stream):
    header = None
    clauses = []
    for line in stream:
        fields = line.split()
        if not fields or fields[0] == 'c':
            continue
        if header is None:
            if len(fields) != 4 or fields[:2] != ['p', 'cnf']:
                raise ValueError('invalid DIMACS header')
            header = tuple(map(int, fields[2:]))
            continue
        clauses.append(parse_clause(fields, header[0]))
    if header is None or len(clauses) != header[1]:
        raise ValueError('incorrect DIMACS clause count')
    return header[0], clauses


def check(num_vars, clauses, stream):
    additions = deletions = 0
    with Minisat22(bootstrap_with=clauses) as propagator:
        for line_number, line in enumerate(stream, 1):
            fields = line.split()
            if not fields or fields[0] == 'c':
                continue
            if fields[0] == 'd':
                parse_clause(fields[1:], num_vars)
                # All retained clauses have already been proved or were in DIMACS.
                # Ignoring deletions can only make the RUP premise stronger.
                deletions += 1
                continue
            clause = parse_clause(fields, num_vars)
            consistent, _ = propagator.propagate(assumptions=[-lit for lit in clause])
            if consistent:
                raise ValueError(f'Line {line_number}: not RUP: {clause}')
            additions += 1
            if not clause:
                return {'verified_additions': additions, 'ignored_deletions': deletions,
                        'empty_clause_line': line_number}
            propagator.add_clause(list(clause))
    raise ValueError('trace has no verified terminating empty clause')


def self_test():
    square = [(1, 2), (1, -2), (-1, 2), (-1, -2)]
    valid = check(2, square, ['d 1 2 0', '1 0', '0'])
    assert valid == {'verified_additions': 2, 'ignored_deletions': 1, 'empty_clause_line': 3}
    assert check(1, [(1,), (-1,)], ['0'])['empty_clause_line'] == 1
    for malformed in (['0'], ['1 0'], ['3 0', '0']):
        try:
            check(2, square, malformed)
        except ValueError:
            pass
        else:
            raise AssertionError(f'accepted invalid trace {malformed}')
    print('PASS: checker rejects non-RUP, missing empty clause, out-of-domain literal', flush=True)


def digest(path):
    with path.open('rb') as stream:
        return file_digest(stream, 'sha256').hexdigest()


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('test', 'check'), default='check', nargs='?')
    parser.add_argument('--receipt', choices=('prove.json', 'prove_900.json'), default='prove.json')
    args = parser.parse_args()
    self_test()
    if args.mode == 'test':
        return

    wall = monotonic()
    cpu = process_time()
    cnf = HERE / 'even.cnf'
    proof = HERE / 'even.drup'
    production = json.loads((HERE / args.receipt).read_text(encoding='utf-8'))
    cnf_sha, proof_sha = digest(cnf), digest(proof)
    assert cnf_sha == production['cnf_sha256']
    assert proof_sha == production['proof_sha256']
    with cnf.open('r', encoding='ascii') as stream:
        num_vars, clauses = read_cnf(stream)
    result = {'cnf_sha256': cnf_sha, 'proof_sha256': proof_sha, 'checker_sha256': digest(Path(__file__)),
              'num_cnf_vars': num_vars, 'num_cnf_clauses': len(clauses)}
    try:
        with proof.open('r', encoding='ascii') as stream:
            result.update(check(num_vars, clauses, stream), status='VERIFIED_RUP_UNSAT')
    except ValueError as exc:
        result.update(status='REJECTED', reason=str(exc))
    result.update(wall_seconds=monotonic() - wall, cpu_seconds=process_time() - cpu)
    check_receipt = 'check_900.json' if args.receipt == 'prove_900.json' else 'check.json'
    (HERE / check_receipt).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2), flush=True)
    if result['status'] != 'VERIFIED_RUP_UNSAT':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
