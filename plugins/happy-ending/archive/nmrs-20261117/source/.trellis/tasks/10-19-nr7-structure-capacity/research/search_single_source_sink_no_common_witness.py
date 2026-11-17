#!/usr/bin/env python3
"""Controlled fixed-order SAT search requiring no common point outside C.

python3 -B search_single_source_sink_no_common_witness.py --output no_common.json
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


def legacy_orders():
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


def orders():
    """Nine targeted free-label templates, then eight missing reuse cases.

    This is a designed finite search family, not an exhaustive reduction.
    Unlike legacy_orders, the reuse branch allows either v2 in Q or k1 in P.
    """
    successful = list(legacy_orders())[9][0]
    placements = [
        (('hu', 'u1'), ('hj', 'j1')),
        (('hu', 'u1'),), (('hj', 'j1'),),
        (('hl', 'e'),), (('hr', 'y'),),
        (('hl', 'e'), ('hr', 'y')),
        (('hc', 'v2'),),
        (('hu', 'u1'), ('hr', 'y')),
        (('hl', 'e'), ('hj', 'j1')),
    ]
    for placement in placements:
        seq = list(successful)
        for new_label, after in placement:
            seq.insert(seq.index(after) + 1, new_label)
        yield tuple(seq), {'v2': 'v2', 'k1': 'k1'}
    for gap in range(BASE.index('e'), BASE.index('w')):
        seq = list(BASE)
        seq.insert(gap + 1, 'k1')
        yield finish(seq), {'v2': 'e', 'k1': 'k1'}
    for gap in range(BASE.index('x'), BASE.index('f')):
        seq = list(BASE)
        seq.insert(gap + 1, 'v2')
        yield finish(seq), {'v2': 'v2', 'k1': 'f'}


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
        # The complete disjoint-pair condition is separated lazily by CEGAR.
        # Every final SAT assignment is checked against ALL actual R6 pairs.
        C = {idx[v] for v in ('u1', 'u2', 'j1', 'j2')}
        for z in sorted(set(range(n)) - C):
            clause([v for path, v in r6_vars.items()
                    if set(path).isdisjoint(C | {z})])
    with cnf_path.open('w') as out, spool.open() as body:
        out.write(f'p cnf {var_count} {clause_count}\n')
        for line in body:
            out.write(line)
    spool.unlink()
    return triples, {'variables': var_count, 'clauses': clause_count,
                     'cnf_sha256': hashlib.sha256(cnf_path.read_bytes()).hexdigest()}, r6_vars


def append_clauses(cnf_path, clauses):
    with cnf_path.open() as source:
        header = source.readline().split()
        body = source.read()
    with cnf_path.open('w') as target:
        target.write(f'p cnf {header[2]} {int(header[3]) + len(clauses)}\n')
        target.write(body)
        for clause in clauses:
            target.write(' '.join(map(str, clause)) + ' 0\n')


def actual_r6_and_disjoint(colors, n):
    r6 = [p for p in combinations(range(n), 6)
          if all(colors[t] for t in combinations(p, 3))]
    masks = {p: sum(1 << v for v in p) for p in r6}
    disjoint = [(p, q) for i, p in enumerate(r6) for q in r6[i + 1:]
                if not masks[p] & masks[q]]
    return r6, disjoint


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
    avoiding_C = [p for p in r6 if set(p).isdisjoint(C)]
    common_intersection = sorted(set.intersection(*(set(p) for p in avoiding_C))) if avoiding_C else None
    remaining = sorted(set(range(n)) - C)
    remaining_minimum_transversals = []
    for k in range(7):
        remaining_minimum_transversals = [s for s in combinations(remaining, k)
                                        if all(set(s) & set(p) for p in avoiding_C)]
        if remaining_minimum_transversals:
            break
    one_point_escape_witnesses = {
        str(z): next((p for p in avoiding_C if z not in p), None)
        for z in sorted(set(range(n)) - C)}
    checks = {'ordered_packets': not packets,
              'strict_ten_point_colors': all(colors[t] == c for t, c in forced.items()),
              'no_R7': not any(len(p) >= 7 for p in paths[True]),
              'no_B6': not any(len(p) >= 6 for p in paths[False]),
              'no_weak7': not weak, 'nu_R6_equals_1': bool(r6) and disjoint is None,
              'exact_four_endpoint_pools': pools == expected,
              'given_paths_avoid_C': all(set(p).isdisjoint(C) for p in given.values()),
              'avoiding_C_family_nonempty_and_no_common_point': bool(avoiding_C) and not common_intersection,
              'tau_after_deleting_C_equals_2': len(remaining_minimum_transversals[0]) == 2,
              'given_paths_red': all(mono(p, True) for p in given.values())}
    return {'checks': checks, 'all_pass': all(checks.values()), 'actual_endpoint_pools': pools,
            'R6': r6, 'tau_R6': len(hits[0]), 'all_minimum_transversals': hits,
            'P_Q': given, 'P_Q_intersection': sorted(set(given['P']) & set(given['Q'])),
            'C': sorted(C), 'all_R6_avoiding_C': [p for p in r6 if set(p).isdisjoint(C)],
            'intersection_of_all_R6_avoiding_C': common_intersection,
            'tau_after_deleting_C': len(remaining_minimum_transversals[0]),
            'all_minimum_transversals_after_deleting_C': remaining_minimum_transversals,
            'avoiding_C_and_each_z_witnesses': one_point_escape_witnesses,
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
    parser.add_argument('--stop', type=int, default=17)
    parser.add_argument('--family', choices=['targeted', 'legacy'], default='targeted')
    args = parser.parse_args()
    assert platform.system() == 'Linux', 'Research workloads must run on Linux'
    cases = list(orders() if args.family == 'targeted' else legacy_orders())
    expected_count = 17 if args.family == 'targeted' else 27
    assert len(cases) == expected_count
    assert len({(o, r['v2'], r['k1']) for o, r in cases}) == expected_count
    for number, (order, roles) in enumerate(cases):
        if not args.start <= number < args.stop:
            continue
        began = time.monotonic()
        with tempfile.TemporaryDirectory(prefix='single_source_sink_') as directory:
            cnf = Path(directory) / 'fixed.cnf'
            triples, binding, r6_vars = build(order, roles, cnf)
            cegar = []
            while True:
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
                if status != 'SAT':
                    break
                literals = [int(v) for line in stdout.splitlines() if line.startswith('v ')
                            for v in line[2:].split() if int(v)]
                positive = {v for v in literals if v > 0}
                assert set(triples.values()) <= {abs(v) for v in literals}
                colors = {t: v in positive for t, v in triples.items()}
                actual, disjoint = actual_r6_and_disjoint(colors, len(order))
                cegar.append({'round': len(cegar), 'actual_R6_count': len(actual),
                              'disjoint_pairs': len(disjoint)})
                if not disjoint:
                    break
                append_clauses(cnf, [(-r6_vars[p], -r6_vars[q]) for p, q in disjoint])
            binding['final_cnf_sha256'] = hashlib.sha256(cnf.read_bytes()).hexdigest()
            binding['separation_clauses_added'] = sum(row['disjoint_pairs'] for row in cegar)
            row = {'order_number': number, 'order': order, 'roles': roles, 'n': len(order),
                   'status': status, 'exit_code': proc.returncode, 'binding': binding,
                   'family': args.family, 'cegar': cegar,
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
