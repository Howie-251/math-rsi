#!/usr/bin/env python3
"""Controlled fixed-order SAT search; Linux only, no independent review.

python3 -B search_single_source_sink_witness.py --output witness.json
UNSAT is a raw solver result for one explicitly listed order, never a general
nonexistence certificate. Successful assignments are independently exhaustively
checked using ALL triples of ALL subsets, unlike the local-chain SAT encoding.
"""
import argparse
from collections import Counter
from itertools import combinations
import hashlib
import json
import os
from pathlib import Path
import platform
import signal
import socket
import subprocess
import tempfile
import time

SOLVER = '/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat'
BASE = ('a', 'x', 'd', 'e', 'y', 'f', 'g', 'w', 'b')
P = ('a', 'x', 'y', 'f', 'g', 'w')
Q = ('x', 'd', 'e', 'y', 'w', 'b')


def orders():
    """Six 14-point orders, then 21 15-point orders; both-reused is impossible.

    This search deliberately restricts v2 outside Q AND k1 outside P. The
    caller's obstruction only excludes the joint inclusions v2 in Q AND
    k1 in P; the stronger search restriction is a choice, not a necessity or
    an exhaustive reduction. In this chosen branch, reused v2 is f/g and
    reused k1 is d/e, so their required order excludes simultaneous reuse.
    New labels occupy original gaps x-d through g-w.
    """
    for k1 in ('d', 'e'):
        for gap in range(1, BASE.index(k1)):
            seq = list(BASE)
            seq.insert(gap + 1, 'v2')
            yield finish(seq), {'v2': 'v2', 'k1': k1}
    for v2 in ('f', 'g'):
        for gap in range(BASE.index(v2), BASE.index('w')):
            seq = list(BASE)
            seq.insert(gap + 1, 'k1')
            yield finish(seq), {'v2': v2, 'k1': 'k1'}
    for first, second in combinations(range(1, 8), 2):
        # first gap 1..6, second gap first..6 (mapped from strict pair).
        second -= 1
        seq = []
        for i, name in enumerate(BASE):
            seq.append(name)
            if i == first:
                seq.append('v2')
            if i == second:
                seq.append('k1')
        yield finish(seq), {'v2': 'v2', 'k1': 'k1'}


def finish(seq):
    seq = list(seq)
    seq[seq.index('a') + 1:seq.index('a') + 1] = ['u1', 'u2']
    seq[seq.index('w') + 1:seq.index('w') + 1] = ['j1', 'j2']
    return tuple(seq)


def frame_data(order, roles):
    idx = {v: i for i, v in enumerate(order)}
    left = tuple(idx[v] for v in ('a', 'u1', 'u2', 'x', roles['v2']))
    right = tuple(idx[v] for v in (roles['k1'], 'w', 'j1', 'j2', 'b'))
    allowed_left = {tuple(left[i] for i in s) for s in ((0, 1, 2), (1, 3, 4), (2, 3, 4))}
    allowed_right = {tuple(right[i] for i in s) for s in ((0, 1, 2), (0, 1, 3), (2, 3, 4))}
    forced = {}
    for triple in combinations(sorted(left + right), 3):
        within_left, within_right = set(triple) <= set(left), set(triple) <= set(right)
        forced[triple] = ((triple in allowed_left) if within_left else
                          (triple in allowed_right) if within_right else True)
    return idx, left, right, forced


def build(order, roles, cnf_path):
    n = len(order)
    idx, left, right, forced = frame_data(order, roles)
    triples = {t: i + 1 for i, t in enumerate(combinations(range(n), 3))}
    var_count, clause_count = len(triples), 0
    spool = cnf_path.with_suffix('.body')
    with spool.open('w') as out:
        def clause(literals):
            nonlocal clause_count
            out.write(' '.join(map(str, literals)) + ' 0\n')
            clause_count += 1

        def new():
            nonlocal var_count
            var_count += 1
            return var_count

        def chain(seq):
            return [triples[tuple(seq[j:j + 3])] for j in range(len(seq) - 2)]

        for q in combinations(range(n), 4):
            packet = [triples[t] for t in combinations(q, 3)]
            # A binary word has <=1 switch iff it has no ABA subsequence.
            for a, b, c in combinations(packet, 3):
                clause((-a, b, -c))
                clause((a, -b, c))
        for t, red in forced.items():
            clause((triples[t] if red else -triples[t],))
        for path in (P, Q):
            for v in chain(tuple(idx[name] for name in path)):
                clause((v,))
        T = tuple(idx[v] for v in ('u1', 'u2', roles['k1'], 'w'))
        S = tuple(idx[v] for v in ('x', roles['v2'], 'j1', 'j2'))
        exact = [('A_T', T, [idx['a']], True), ('B_T', T, [idx['j1'], idx['j2']], False),
                 ('A_S', S, [idx['u1'], idx['u2']], True), ('B_S', S, [idx['b']], False)]
        for _, middle, expected, front in exact:
            candidates = range(middle[0]) if front else range(middle[-1] + 1, n)
            for v in candidates:
                path = (v,) + middle if front else middle + (v,)
                local = chain(path)
                if v in expected:
                    for literal in local:
                        clause((literal,))
                else:
                    clause([-literal for literal in local])
        for path in combinations(range(n), 7):
            clause([-v for v in chain(path)])
        for path in combinations(range(n), 6):
            clause(chain(path))
        reach = {}
        for color, sizes in [('R', (4, 5, 6)), ('B', (3, 4, 5))]:
            for size in sizes:
                for path in combinations(range(n), size):
                    key = (color, size, path[0], path[-1])
                    if key not in reach:
                        reach[key] = new()
                    literals = chain(path)
                    clause(([-v for v in literals] if color == 'R' else literals) + [reach[key]])
        for a, b in combinations(range(n), 2):
            for r in (4, 5, 6):
                kr, kb = ('R', r, a, b), ('B', 9 - r, a, b)
                if kr in reach and kb in reach:
                    clause((-reach[kr], -reach[kb]))
        r6_vars = {}
        for path in combinations(range(n), 6):
            v = new()
            r6_vars[path] = v
            local = chain(path)
            for t in local:
                clause((-v, t))
            clause([v] + [-t for t in local])
        for path, v in r6_vars.items():
            outside = sorted(set(range(n)) - set(path))
            for other in combinations(outside, 6):
                if path < other:
                    clause((-v, -r6_vars[other]))
    with cnf_path.open('w') as out, spool.open() as body:
        out.write(f'p cnf {var_count} {clause_count}\n')
        for line in body:
            out.write(line)
    spool.unlink()
    return triples, {'variables': var_count, 'clauses': clause_count,
                     'cnf_sha256': hashlib.sha256(cnf_path.read_bytes()).hexdigest()}


def verify(order, roles, colors):
    """Independent all-triples enumeration, not SAT local-chain reuse."""
    n = len(order)
    idx, left, right, forced = frame_data(order, roles)

    def mono(path, color):
        return all(colors[t] == color for t in combinations(path, 3))

    packets = []
    for q in combinations(range(n), 4):
        word = [colors[t] for t in combinations(q, 3)]
        if sum(a != b for a, b in zip(word, word[1:])) > 1:
            packets.append(q)
    paths = {c: [] for c in (True, False)}
    for k in range(2, n + 1):
        for p in combinations(range(n), k):
            for c in paths:
                if mono(p, c):
                    paths[c].append(p)
    r6 = [p for p in paths[True] if len(p) == 6]
    disjoint = next(((p, q) for i, p in enumerate(r6) for q in r6[i + 1:]
                     if set(p).isdisjoint(q)), None)
    weak = []
    for a, b in combinations(range(n), 2):
        maxima = {c: max(len(p) for p in paths[c] if (p[0], p[-1]) == (a, b)) for c in paths}
        if sum(maxima.values()) >= 9:
            weak.append({'endpoints': (a, b), 'R': maxima[True], 'B': maxima[False]})
    T = tuple(idx[v] for v in ('u1', 'u2', roles['k1'], 'w'))
    S = tuple(idx[v] for v in ('x', roles['v2'], 'j1', 'j2'))
    pools = {}
    for name, middle in [('T', T), ('S', S)]:
        pools['A_' + name] = [v for v in range(middle[0]) if mono((v,) + middle, True)]
        pools['B_' + name] = [v for v in range(middle[-1] + 1, n) if mono(middle + (v,), True)]
    expected = {'A_T': [idx['a']], 'B_T': [idx['j1'], idx['j2']],
                'A_S': [idx['u1'], idx['u2']], 'B_S': [idx['b']]}
    hits = []
    for k in range(7):
        hits = [s for s in combinations(range(n), k) if all(set(s) & set(p) for p in r6)]
        if hits:
            break
    given = {name: tuple(idx[v] for v in path) for name, path in [('P', P), ('Q', Q)]}
    deleted_U = {idx[v] for v in ('x', roles['v2'], 'j1', 'j2', 'b')}
    deleted_J = {idx[v] for v in (roles['k1'], 'w', 'u1', 'u2', 'a')}
    C = {idx[v] for v in ('u1', 'u2', 'j1', 'j2')}
    kappa_triple = (idx['u1'], idx['u2'], given['P'][3])
    lambda_triple = (given['Q'][2], idx['j1'], idx['j2'])
    deletion_families = {
        'U_family': {'deleted_V_J_b': sorted(deleted_U),
                     'R6': [p for p in r6 if set(p).isdisjoint(deleted_U)]},
        'J_family': {'deleted_K_U_a': sorted(deleted_J),
                     'R6': [p for p in r6 if set(p).isdisjoint(deleted_J)]}}
    checks = {'ordered_packets': not packets,
              'strict_ten_point_colors': all(colors[t] == c for t, c in forced.items()),
              'no_R7': not any(len(p) >= 7 for p in paths[True]),
              'no_B6': not any(len(p) >= 6 for p in paths[False]),
              'no_weak7': not weak, 'nu_R6_equals_1': bool(r6) and disjoint is None,
              'exact_four_endpoint_pools': pools == expected,
              'given_paths_avoid_C': all(set(p).isdisjoint(C) for p in given.values()),
              'given_paths_red': all(mono(p, True) for p in given.values())}
    return {'checks': checks, 'all_pass': all(checks.values()), 'actual_endpoint_pools': pools,
            'R6': r6, 'tau_R6': len(hits[0]), 'all_minimum_transversals': hits,
            'P_Q': given, 'P_Q_intersection': sorted(set(given['P']) & set(given['Q'])),
            'C': sorted(C), 'all_R6_avoiding_C': [p for p in r6 if set(p).isdisjoint(C)],
            'five_vertex_deletion_families': deletion_families,
            'kappa_P4': {'triple': kappa_triple, 'color': 'R' if colors[kappa_triple] else 'B'},
            'lambda_Q3': {'triple': lambda_triple, 'color': 'R' if colors[lambda_triple] else 'B'},
            'packet_failures': packets, 'weak7_failures': weak, 'disjoint_R6_pair': disjoint,
            'monochromatic_counts': {str(c): dict(Counter(map(len, ps))) for c, ps in paths.items()}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--solver', default=SOLVER)
    parser.add_argument('--seconds-per-order', type=float, default=60)
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--stop', type=int, default=27)
    args = parser.parse_args()
    assert platform.system() == 'Linux', 'Research workloads must run on Linux'
    cases = list(orders())
    assert len(cases) == 27
    assert len({(o, r['v2'], r['k1']) for o, r in cases}) == 27
    for number, (order, roles) in enumerate(cases):
        if not args.start <= number < args.stop:
            continue
        began = time.monotonic()
        with tempfile.TemporaryDirectory(prefix='single_source_sink_') as directory:
            cnf = Path(directory) / 'fixed.cnf'
            triples, binding = build(order, roles, cnf)
            proc = subprocess.Popen([args.solver, str(cnf)], stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, text=True, start_new_session=True)
            try:
                stdout, _ = proc.communicate(timeout=args.seconds_per_order)
                status = 'SAT' if proc.returncode == 10 else 'RAW_UNSAT' if proc.returncode == 20 else 'ERROR'
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGTERM)
                try:
                    stdout, _ = proc.communicate(timeout=5)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid, signal.SIGKILL)
                    stdout, _ = proc.communicate()
                status = 'TIMEOUT'
            row = {'order_number': number, 'order': order, 'roles': roles, 'n': len(order),
                   'status': status, 'exit_code': proc.returncode, 'binding': binding,
                   'elapsed_seconds': round(time.monotonic() - began, 3)}
            if status == 'SAT':
                literals = [int(v) for line in stdout.splitlines() if line.startswith('v ')
                            for v in line[2:].split() if int(v)]
                positive = {v for v in literals if v > 0}
                assigned = {abs(v) for v in literals}
                assert set(triples.values()) <= assigned, 'Incomplete SAT assignment'
                colors = {t: v in positive for t, v in triples.items()}
                checked = verify(order, roles, colors)
                assert checked['all_pass'], checked
                payload = {'scope': 'One actual finite ordered rank-3 signotope; no geometric realization claimed',
                    'execution': {'hostname': socket.gethostname(), 'python': platform.python_version(),
                                  'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
                    'solver_receipt': row, 'solver_stdout': stdout, 'solver_signed_assignment': literals,
                    'red_triples': [t for t, c in colors.items() if c],
                    'blue_triples': [t for t, c in colors.items() if not c],
                    'independent_exhaustive_validation': checked}
                args.output.write_text(json.dumps(payload, indent=2) + '\n', encoding='utf-8')
                row['verified_witness_output'] = str(args.output)
                row['tau_R6'] = checked['tau_R6']
                print(json.dumps(row), flush=True)
                return
            print(json.dumps(row), flush=True)


if __name__ == '__main__':
    main()
