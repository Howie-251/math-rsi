"""Bounded shared-five-view join for a real six-unit8 pool with co1 graph K1,5.
No position/probability optimization. Reads only frozen proved five-view domains.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations, permutations
import json, time

HERE = Path(__file__).resolve().parent
SRC = HERE.parents[1] / 'unique6_no7'


def main():
    started = time.monotonic()
    domain = json.loads((SRC / 'FIVE_DOMAIN.json').read_text())
    dp = json.loads((SRC / 'FIVE_DP.json').read_text())['cases']
    joint = {r['source_id']: Fraction(r['bound']) for r in
             json.loads((SRC / 'FIVE_JOINT.json').read_text())['results']}
    residual = {r['id'] for r in dp
                if joint.get(r['id'], Fraction(r['bound'])) >= 1}
    base = []
    for r in domain['labelled']:
        if r['orbit'] not in residual:
            continue
        ns = {int(k): v for k, v in r['counts'].items()}
        inc = {m: sum(v for k, v in ns.items() if k & m == m)
               for m in range(1, 64)}
        # Every block has size <=2, already analytically proved for this full pool.
        if any(inc[1 | sum(1 << i for i in ijk)] for ijk in combinations(range(1, 6), 3)):
            continue
        base.append(inc)
    options = []
    for Y in combinations(range(1, 7), 5):
        S = (0,) + Y
        need = {(i, j) for i, j in combinations(range(5), 2)
                if Y[i] == 1 or Y[j] == 1}
        rows = []
        for inc in base:
            actual = {(i, j) for i, j in combinations(range(5), 2)
                      if inc[(1 << (i+1)) | (1 << (j+1))] == 1}
            if actual != need:
                continue
            rows.append({sum(1 << S[i] for i in range(6) if m >> i & 1): v
                         for m, v in inc.items()})
        options.append((Y, rows))
    options.sort(key=lambda row: len(row[1]))
    buckets = []
    known = set()
    for Y, rows in options:
        if not rows:
            buckets.append(((), {}))
            continue
        shared = tuple(sorted(known & rows[0].keys()))
        b = {}
        for row in rows:
            b.setdefault(tuple(row[k] for k in shared), []).append(row)
        buckets.append((shared, b))
        known.update(rows[0])
    joins = 0
    negative = 0
    valid = []
    complete = True

    def go(i, inc):
        nonlocal joins, negative
        if time.monotonic() - started > 10:
            raise TimeoutError('10-second domain-only bound')
        if i == len(options):
            joins += 1
            if joins > 20000:
                raise TimeoutError('20000 shared joins bound')
            assert set(inc) == set(range(1, 128)) - {126, 127}
            ns = [({0: 35, 126: 0, 127: 0} | inc)[m] for m in range(128)]
            for bit in range(7):
                for m in range(128):
                    if not m >> bit & 1:
                        ns[m] -= ns[m | (1 << bit)]
            if min(ns) < 0:
                negative += 1
            else:
                valid.append(ns)
            return
        shared, b = buckets[i]
        for row in b.get(tuple(inc[k] for k in shared), []):
            go(i + 1, inc | row)

    try:
        go(0, {})
    except TimeoutError as e:
        complete = False
        reason = str(e)
    else:
        reason = None
    result = dict(scope=__doc__, complete=complete, stopped_reason=reason,
                  source_residual_orbits=sorted(residual),
                  view_order=[list(Y) for Y, _ in options],
                  option_counts=[len(rows) for _, rows in options],
                  shared_joins=joins, negative_inventory_joins=negative,
                  nonnegative_labelled=len(valid), inventories=valid,
                  elapsed_seconds=time.monotonic() - started)
    (HERE / 'SIX_UNIT8_STAR_JOIN.json').write_text(json.dumps(result, indent=2) + '\n')
    print({k: v for k, v in result.items() if k not in ('scope', 'inventories', 'source_residual_orbits')})


if __name__ == '__main__':
    main()
