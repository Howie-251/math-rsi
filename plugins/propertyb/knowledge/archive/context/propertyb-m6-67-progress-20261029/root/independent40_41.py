"""Reconstruct all selected traces and replay retained rows via injection probabilities."""
import ast
import json
import time
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, combinations_with_replacement
from math import comb, factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / 'context/propertyb-m6-66-20261029/independent/check.py'
ns = dict(Q=Q, lru_cache=lru_cache, factorial=factorial, comb=comb)
names = {'ceildiv', 'fall', 'probs'}
functions = [n for n in ast.parse(SOURCE.read_text()).body
             if isinstance(n, ast.FunctionDef) and n.name in names]
assert {n.name for n in functions} == names
exec(compile(ast.Module(body=functions, type_ignores=[]), str(SOURCE), 'exec'), ns)
prob = ns['probs']


def partitions(s):
    pairs = list(combinations(range(s), 2))
    blocks = [(b, sum(1 << i for i, (x, y) in enumerate(pairs)
                      if b >> x & 1 and b >> y & 1))
              for b in range(1 << s) if b.bit_count() >= 2]
    states = {0: {()}}
    # Independent subset dynamic program; each clique can occur at most once.
    for block, used in blocks:
        updates = {}
        for mask, choices in states.items():
            if not mask & used:
                updates.setdefault(mask | used, set()).update(t + (block,) for t in choices)
        for mask, choices in updates.items():
            states.setdefault(mask, set()).update(choices)
    return states[(1 << len(pairs)) - 1]


def deduction(v, pos, ell, j):
    types = [t for t in ell if t >> j & 1]
    cells = []
    for a, t in enumerate(types):
        for u in types[a:]:
            cap = comb(ell[t], 2) if t == u else ell[t] * ell[u]
            if cap:
                weight = prob(v, pos, pos[j], t, u) + prob(v, pos, pos[j], u, t)
                cells.append((weight, cap, t | u))
    costs = []
    for R in range(1 << len(pos)):
        if R >> j & 1:
            continue
        f = sum(n for t, n in ell.items() if t >> j & 1 and not t & R)
        need = max(0, -(-(5*f - (v-1-R.bit_count())) // 4))
        cost = Q(0)
        for weight, cap, union in sorted(cells):
            if not union & R:
                take = min(need, cap)
                cost += take * weight
                need -= take
        assert need == 0
        costs.append(cost)
    return max(costs)


def bound(v, pos, ell):
    pos = tuple(pos)
    assert len(set(pos)) == len(pos) and all(1 <= h <= v for h in pos)
    deletes = {pos[j]: deduction(v, pos, ell, j) for j in range(len(pos))}
    result = Q(0)
    for h in range(1, v+1):
        A = sum(n * prob(v, pos, h, t)[0] for t, n in ell.items())
        B = sum(n * prob(v, pos, h, t)[1] for t, n in ell.items())
        C = sum(n * (m - (t == u)) * prob(v, pos, h, t, u)
                for t, n in ell.items() for u, m in ell.items())
        assert C >= deletes.get(h, 0)
        result += min(A, B, C - deletes.get(h, 0))
    return result


def main():
    start = time.process_time()
    data = json.loads((HERE.parent/'tail39_41/CERT40_41.json').read_text())
    summaries = []
    for v, s in [(40, 4), (41, 5)]:
        domain = {(ds, bs) for ds in combinations_with_replacement(range(8, 11), s)
                  for bs in partitions(s)}
        rows = [r for r in data['rows'] if r['v'] == v]
        assert len(rows) == len(domain)
        assert {(tuple(r['degrees']), tuple(sorted(r['blocks']))) for r in rows} == domain
        passed, excluded, maxima = 0, 0, []
        for r in rows:
            ds, blocks = r['degrees'], r['blocks']
            ell = {b: 1 for b in blocks}
            for i, d in enumerate(ds):
                ell[1 << i] = d - sum(b >> i & 1 for b in blocks)
            ell[0] = 66 - sum(ell.values())
            ell = {t: n for t, n in ell.items() if n}
            assert min(ell.values()) >= 0 and sum(ell.values()) == 66
            assert ell == {int(t): n for t, n in r['ell'].items() if n}
            for i, j in combinations(range(s), 2):
                assert sum(n for t, n in ell.items() if t >> i & 1 and t >> j & 1) == 1
            omit = ((v == 40 and ds == [8,8,8,10] and blocks == [15])
                    or (v == 41 and sum(ds) <= 49 and blocks == [31]))
            assert omit == r['structural_excluded']
            if omit:
                excluded += 1
                continue
            actual = bound(v, r['positions'], ell)
            assert actual == Q(r['U']) < 1, (v, ds, blocks, actual, r['U'])
            passed += 1
            maxima.append(actual)
        summaries.append(dict(v=v, complete_domain=len(domain), independently_replayed=passed,
                              structurally_excluded=excluded, maximum=str(max(maxima))))
    result = dict(status='PASS', review_independence='same-family', acceptance_status='provisional',
                  scope='Complete v40/v41 degree-and-trace domains; all structurally retained rows replayed with independent injection probabilities and max-of-avoidance-quota deletion.',
                  mathematical_selection='Root read PROOF40_41.md; selection proof is separate from this arithmetic program.',
                  rows=summaries, cpu_seconds=time.process_time()-start)
    (HERE/'INDEPENDENT40_41.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
