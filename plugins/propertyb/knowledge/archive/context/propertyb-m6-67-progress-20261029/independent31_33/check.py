"""Reconstruct all 143 local types; independent component DP and injection replay."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from collections import Counter
import importlib.util
import json
import signal
import time

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
START = time.process_time()
WALL = time.monotonic()


def timeout(signum, frame):
    raise TimeoutError('60 CPU-second / 180 wall-second independent replay budget exceeded')


signal.signal(signal.SIGPROF, timeout)
signal.signal(signal.SIGALRM, timeout)
signal.setitimer(signal.ITIMER_PROF, 60)
signal.alarm(180)
spec = importlib.util.spec_from_file_location('injection_kernel', BASE/'root/independent40_41.py')
injection = importlib.util.module_from_spec(spec)
spec.loader.exec_module(injection)
prob = injection.prob


def ceil(n, d):
    return -(-n // d)


def component_support(t, e):
    assert t - 1 <= e <= comb(t, 2)
    if t == 1:
        return 5
    cw = ceil(t*t, t+2*e)
    forest = ceil(2*t-e-1, 2)
    unique_complement = 11 if comb(t, 2)-e > t//2 else 0
    return max(6, 5*cw, 5*forest, unique_complement)


# Independent bottom-up EXACT-edge component-knapsack. Prefix minima then
# give the at-most-edge support relaxation; no submitted quota/DP imported.
MAXF, MAXQ = 24, 80
INF = 100000
exact = [[INF] * (MAXQ+1) for _ in range(MAXF+1)]
exact[0][0] = 0
for f in range(1, MAXF+1):
    for t in range(1, f+1):
        for e in range(t-1, min(comb(t, 2), MAXQ)+1):
            u = component_support(t, e)
            tail = exact[f-t]
            for q in range(e, MAXQ+1):
                cost = u + tail[q-e]
                if cost < exact[f][q]:
                    exact[f][q] = cost
at_most = []
for row in exact:
    current = INF
    prefix = []
    for x in row:
        current = min(current, x)
        prefix.append(current)
    at_most.append(prefix)


def quota(f, N):
    assert 0 <= f <= MAXF
    # Start at zero, independently checking all smaller budgets too.
    return next(q for q in range(MAXQ+1) if at_most[f][q] <= N)


def ell_case(degrees, paircounts=None, tau=0):
    s = len(degrees)
    ell = {}
    if s == 3:
        ell[7] = tau
    for (i, j), count in (paircounts or {}).items():
        ell[(1 << i) | (1 << j)] = count - tau
    for i, d in enumerate(degrees):
        ell[1 << i] = d - sum(n for t, n in ell.items() if t >> i & 1)
    ell[0] = 66 - sum(ell.values())
    assert min(ell.values()) >= 0
    assert sum(ell.values()) == 66
    return {t: n for t, n in ell.items() if n}


def two(d, e, lam=1):
    return ell_case((d, e), {(0, 1): lam})


def triple(degrees, lam, tau):
    return ell_case(degrees, {(0, 1): 1, (0, 2): 1, (1, 2): lam}, tau)


def signature(branch, v, ell):
    return branch, v, tuple(sorted((int(t), n) for t, n in ell.items() if n))


def deletion(v, slots, ell, j):
    types = [t for t in ell if t >> j & 1]
    d = sum(ell[t] for t in types)
    need = quota(d, v-1)
    cells = []
    for index, t in enumerate(types):
        for u in types[index:]:
            cap = comb(ell[t], 2) if t == u else ell[t] * ell[u]
            if cap:
                w = prob(v, slots, slots[j], t, u) + prob(v, slots, slots[j], u, t)
                cells.append((w, cap))
    out = Q(0)
    for w, cap in sorted(cells):
        take = min(need, cap)
        out += take * w
        need -= take
    assert need == 0
    return out


def bound(v, positions, ell):
    slots = tuple(positions)
    assert len(slots) == len(set(slots)) and all(1 <= h <= v for h in slots)
    delete = {h: deletion(v, slots, ell, j) for j, h in enumerate(slots)}
    out = Q(0)
    for h in range(1, v+1):
        end = sum(n * prob(v, slots, h, t)[0] for t, n in ell.items())
        begin = sum(n * prob(v, slots, h, t)[1] for t, n in ell.items())
        pair = sum(n * (m-(t==u)) * prob(v, slots, h, t, u)
                   for t, n in ell.items() for u, m in ell.items())
        assert pair >= delete.get(h, 0)
        out += min(end, begin, pair-delete.get(h, 0))
    return out


def main():
    cert = json.loads((BASE/'small31_33/CERTIFICATE.json').read_text())
    assert cert['M'] == 66 and cert['complete_vertex_branches'] == [31, 32, 33]
    expected = set()
    def add(branch, v, ell):
        entry = signature(branch, v, ell)
        assert entry not in expected
        expected.add(entry)
    for d in range(6, 12):
        add('v31_min6_11', 31, ell_case((d,)))
    assert 31*12+25 > 396 and 6*6 > 30
    for lam in range(1, 7):
        add('v31_min12', 31, two(12, 12, lam))
    intervals = []
    for v, first, last, branch in [(32, 7, 11, 'v32_min7_11'), (33, 7, 12, 'v33_adaptive_pass')]:
        for d in range(first, last+1):
            n = 2*(v-1)-5*d
            assert n > 0
            upper = d + (396-v*d)//n
            assert v*d+n*(upper+1-d) > 396
            intervals.append(dict(v=v, minimum=d, unit_neighbor_lower=n, partner_upper=upper))
            for e in range(d, upper+1):
                if v == 33 and d in (9, 10, 11) and e == 14:
                    continue
                add(branch, v, two(d, e))
    assert 396-32*12 == 12 and 32-12 == 20 and 12+12 == 24
    for e in (12, *range(14, 25)):
        add('v32_min12_pair', 32, two(12, e))
    for lam in (1, 2):
        for tau in (0, 1):
            add('v32_min12_wedge', 32, triple((13, 12, 12), lam, tau))
    # delta9: exactly nineteen unit neighbors, all degree>=14, leave <=4
    # degree-surplus units among fourteen other vertices, >=10 degree9.
    assert 396-33*9 == 99 and 19*5 == 95 and 20*5 > 99
    assert 45-32 == 13 and 14-4 >= 10
    add('v33_delta9_special', 33, two(9, 9, 2))
    delta14 = []
    for d in (10, 11):
        n = 64-5*d
        surplus = 396-33*d
        lower14 = (15-d)*n-surplus
        assert lower14 == (4 if d == 10 else 3)
        delta14.append(dict(minimum=d, unit_neighbor_lower=n, degree14_neighbor_lower=lower14))
        count = 0
        for lam in range(1, 15):
            for tau in (0, 1):
                if 13-lam+tau >= 0:
                    add(f'v33_delta{d}_two14', 33, triple((d, 14, 14), lam, tau))
                    count += 1
        assert count == 27
    assert len(expected) == 143
    actual_keys = [signature(r['branch'], r['v'], r['ell']) for r in cert['rows']]
    assert len(actual_keys) == len(set(actual_keys)) == len(expected)
    assert set(actual_keys) == expected
    quotas = []
    assert len(cert['quotas']) == 125
    assert {(r['support'], r['f']) for r in cert['quotas']} == {(N, f) for N in range(28, 33) for f in range(25)}
    for row in cert['quotas']:
        q = quota(row['f'], row['support'])
        assert q == row['q'], (row, q)
        quotas.append(dict(support=row['support'], f=row['f'], q=q,
                           relaxed_support_at_quota=at_most[row['f']][q],
                           relaxed_support_below_quota=(at_most[row['f']][q-1] if q else None)))
    replay = []
    for row in cert['rows']:
        ell = {int(t): n for t, n in row['ell'].items() if n}
        value = bound(row['v'], row['positions'], ell)
        assert value == Q(row['U']) < 1, (row, value)
        assert row['strict']
        replay.append(dict(branch=row['branch'], v=row['v'], positions=row['positions'],
                           ell=ell, U=str(value), exact_match=True, strict=True))
    summaries = []
    for branch in sorted({r['branch'] for r in replay}):
        rr = [r for r in replay if r['branch']==branch]
        summaries.append(dict(branch=branch, profiles=len(rr), maximum=str(max(Q(r['U']) for r in rr))))
    result = dict(status='PASS', review_independence='same-family', acceptance_status='provisional',
                  scope='Full v31/v32/v33 necessary selection/degree/trace domains, component support/quota table, all 143 actual recorded layouts',
                  method='Independent bottom-up exact-edge component knapsack and prefix minima; existing independent falling-factorial injection kernel; independently implemented full-pool component-quota deletion',
                  quota_deletion_scope='Full link pool only, matching certificate.py; avoided.avoid_delete is not installed by its guarded import',
                  submitted_generator_or_quota_imported=False, old_source_main_executed=False,
                  reconstructed_profiles=len(expected), independently_replayed=len(replay),
                  quota_entries=quotas, intervals=intervals, degree14_selection=delta14,
                  summaries=summaries, maximum=str(max(Q(r['U']) for r in replay)),
                  cpu_seconds=time.process_time()-START, wall_seconds=time.monotonic()-WALL, rows=replay)
    (HERE/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','quota_entries')},indent=2))


if __name__ == '__main__':
    main()
