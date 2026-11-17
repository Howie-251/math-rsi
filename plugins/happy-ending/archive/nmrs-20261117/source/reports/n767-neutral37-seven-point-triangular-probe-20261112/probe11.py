"""11-point signotope SAT probe; external controlled Kissat only, Linux only.

All points/roles are abstract ordered vertices, not planar coordinates.
Run: python3.12 -B probe11.py > probe11-result.json
"""
import hashlib
from itertools import combinations
import json
import os
from pathlib import Path
import platform
import signal
import socket
import subprocess
import sys
import tempfile
import time

SOLVER = '/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat'
V = tuple(range(11))
TRIPLES = list(combinations(V, 3))
VAR = {t: i+1 for i, t in enumerate(TRIPLES)}


def consecutive(p):
    return [VAR[p[i:i+3]] for i in range(len(p)-2)]


def build(roles):
    p1, p2, q1, q2 = roles
    pool = tuple(v for v in V if v not in roles)
    allowed = {(p1, q1), (p2, q2), (p1, q2)}
    clauses = []
    def add(lits):
        lits = set(lits)
        if any(-v in lits for v in lits):
            return
        clauses.append(sorted(lits, key=lambda v: (abs(v), v)))
    # All 16 packet assignments except the 8 with at most one color change.
    for packet in combinations(V, 4):
        vv = [VAR[t] for t in combinations(packet, 3)]
        for mask in range(16):
            bits = [(mask >> i) & 1 for i in range(4)]
            if sum(a != b for a, b in zip(bits, bits[1:])) > 1:
                add([-v if b else v for v, b in zip(vv, bits)])
    for p in combinations(V, 7):
        add([-v for v in consecutive(p)])
    for p in combinations(V, 6):
        add(consecutive(p))  # no B6
    # No weak7; enumerate all pairs with shared endpoints and length sum 9.
    for a, b in combinations(V, 2):
        middle = tuple(range(a+1, b))
        for nr in range(0, 6):
            nb = 5-nr
            for ri in combinations(middle, nr):
                r = (a,)+ri+(b,)
                for bi in combinations(middle, nb):
                    blue = (a,)+bi+(b,)
                    add([-v for v in consecutive(r)]+consecutive(blue))
    for p in combinations(V, 5):
        if (p[0], p[-1]) == (p2, q1):
            add([-v for v in consecutive(p)])
    candidates = []
    for p in combinations(V, 6):
        if (p[0], p[-1]) not in allowed or not set(p[1:-1]) <= set(pool):
            add([-v for v in consecutive(p)])
        else:
            selector = len(VAR)+len(candidates)+1
            candidates.append((p, selector))
            for v in consecutive(p):
                add([-selector, v])
    for endpoints in ((p1, q1), (p2, q2)):
        add([s for p, s in candidates if (p[0], p[-1]) == endpoints])
    # Select actual R6 avoiding each pool vertex, giving empty total intersection.
    for v in pool:
        add([s for p, s in candidates if v not in p[1:-1]])
    return clauses, len(VAR)+len(candidates), pool


def transversal(edges, universe):
    for k in range(len(universe)+1):
        good = [h for h in combinations(universe, k)
                if all(set(h)&set(e) for e in edges)]
        if good:
            return {'tau': k, 'all_minimum': good}
    return {'tau': None, 'all_minimum': []}


def inspect(model, roles):
    """Direct exhaustive checker; independent of clauses and selectors."""
    color = {t: 'R' if VAR[t] in model else 'B' for t in TRIPLES}
    paths = {c: [] for c in ('R', 'B')}
    for k in range(2, len(V)+1):
        for p in combinations(V, k):
            for c in ('R', 'B'):
                if all(color[p[i:i+3]] == c for i in range(k-2)):
                    paths[c].append(p)
    packets = []
    for p in combinations(V, 4):
        cs = ''.join(color[t] for t in combinations(p, 3))
        packets.append({'vertices': p, 'colors': cs,
                        'valid': sum(a != b for a, b in zip(cs, cs[1:])) <= 1})
    same = []
    weak = []
    for a, b in combinations(V, 2):
        pp = {c: [p for p in paths[c] if (p[0], p[-1]) == (a, b)] for c in paths}
        same.append({'endpoints': (a, b),
                     'maxima': {c: max(map(len, pp[c])) for c in pp},
                     'R5': [p for p in pp['R'] if len(p) == 5]})
        weak.extend({'R': r, 'B': blue,
                     'internal_intersection': sorted(set(r[1:-1])&set(blue[1:-1]))}
                    for r in pp['R'] for blue in pp['B'] if len(r)+len(blue) == 9)
    r6 = [p for p in paths['R'] if len(p) == 6]
    p1, p2, q1, q2 = roles
    pool = tuple(v for v in V if v not in roles)
    common = sorted(set.intersection(*(set(p[1:-1]) for p in r6))) if r6 else None
    endpoint_edges = sorted(set((p[0], p[-1]) for p in r6))
    allowed = {(p1, q1), (p2, q2), (p1, q2)}
    checks = {
        'packet_valid': all(p['valid'] for p in packets),
        'no_R7': max(map(len, paths['R'])) < 7,
        'no_B6': max(map(len, paths['B'])) < 6,
        'no_weak7': not weak,
        'all_R6_allowed_endpoints': set(endpoint_edges) <= allowed,
        'all_R6_internal_in_pool': all(set(p[1:-1]) <= set(pool) for p in r6),
        'both_diagonal_R6_exist': {(p1, q1), (p2, q2)} <= set(endpoint_edges),
        'no_reverse_R5': not any(p[0] == p2 and p[-1] == q1
                                 for p in paths['R'] if len(p) == 5),
        'R6_internal_common_empty': common == [],
    }
    return {'checks': checks, 'all_checks_pass': all(checks.values()),
            'roles': dict(zip(('p1', 'p2', 'q1', 'q2'), roles)), 'pool': pool,
            'colors': [{'vertices': t, 'color': color[t]} for t in TRIPLES],
            'packets': packets, 'all_paths': paths, 'R6': r6,
            'same_endpoint_maxima_and_all_R5': same, 'weak7': weak,
            'longest': {c: max(map(len, paths[c])) for c in paths},
            'R6_endpoint_edges': endpoint_edges, 'R6_internal_common': common,
            'R6_pair_intersections': [
                {'a': a, 'b': b, 'physical': sorted(set(a)&set(b)),
                 'internal': sorted(set(a[1:-1])&set(b[1:-1]))}
                for a, b in combinations(r6, 2)],
            'physical_transversal': transversal(r6, V),
            'internal_transversal': transversal([p[1:-1] for p in r6], pool),
            'endpoint_transversal': transversal(endpoint_edges, V)}


def run_one(roles, directory, seconds):
    clauses, nvars, pool = build(roles)
    stem = 'roles-'+'-'.join(map(str, roles))
    cnf = directory/(stem+'.cnf')
    text = 'p cnf %d %d\n' % (nvars, len(clauses))
    text += ''.join(' '.join(map(str, c))+' 0\n' for c in clauses)
    cnf.write_text(text, encoding='ascii')
    command = [SOLVER, '--time='+str(seconds), str(cnf)]
    began = time.monotonic()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True, start_new_session=True)
    timeout = False
    try:
        out, err = process.communicate(timeout=seconds+5)
    except subprocess.TimeoutExpired:
        timeout = True
        os.killpg(process.pid, signal.SIGTERM)
        try:
            out, err = process.communicate(timeout=3)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            out, err = process.communicate()
    (directory/(stem+'.stdout')).write_text(out)
    (directory/(stem+'.stderr')).write_text(err)
    status = 'SAT' if 's SATISFIABLE' in out else 'RAW_UNSAT' if 's UNSATISFIABLE' in out else 'UNKNOWN'
    result = {'roles': roles, 'pool': pool, 'variables': nvars, 'clauses': len(clauses),
              'cnf': str(cnf), 'cnf_sha256': hashlib.sha256(text.encode('ascii')).hexdigest(),
              'command': command, 'exit_code': process.returncode, 'timeout_killed': timeout,
              'elapsed_seconds': time.monotonic()-began, 'status': status,
              'stdout': out, 'stderr': err, 'proof_checked': False}
    if status == 'SAT':
        assignment = {int(v) for line in out.splitlines() if line.startswith('v ')
                      for v in line[2:].split() if int(v) != 0}
        result['model_variable_count'] = len(assignment)
        result['model_satisfies_all_cnf_clauses'] = all(any(v in assignment for v in c) for c in clauses)
        result['independent_enumeration'] = inspect(assignment, roles)
    return result


def main():
    directory = Path(tempfile.mkdtemp(prefix='n767-seven-pool-20261112-'))
    trials = []
    # Explicit limited branches only; no completeness assertion over role orders.
    branches = [(0, 1, 9, 10), (0, 2, 9, 10), (0, 1, 8, 10), (0, 2, 8, 10)]
    for roles in branches:
        trial = run_one(roles, directory, 40)
        trials.append(trial)
        if trial['status'] == 'SAT':
            break
    source_sha = globals().get('CHECKER_SOURCE_SHA256')
    if source_sha is None:
        source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result = {'scope': 'Finite local abstract 11-point probe, not a 75-point witness or planar realization.',
              'definitions': {'R': 'positive triple variable', 'B': 'negative triple variable',
                              'path': 'increasing sequence; consecutive triples monochromatic; length counts vertices',
                              'weak7': 'same outer endpoints and opposite-color lengths sum to 9'},
              'execution': {'host': socket.gethostname(), 'platform': platform.platform(),
                            'python_executable': sys.executable, 'python_version': sys.version,
                            'source_sha256': source_sha, 'remote_directory': str(directory),
                            'solver': SOLVER},
              'planned_branches': branches, 'trials': trials,
              'status': 'SAT_WITNESS' if any(t['status'] == 'SAT' for t in trials) else 'NO_WITNESS_IN_TRIED_BRANCHES',
              'untried_role_orders_not_excluded': True}
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
