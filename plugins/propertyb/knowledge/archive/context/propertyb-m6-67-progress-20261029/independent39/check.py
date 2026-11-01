"""Independent full v39 necessary-domain audit and injection-count replay."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement
from collections import Counter
import importlib.util
import json
import signal
import time

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
START = time.process_time()
WALL_START = time.monotonic()


def timeout(signum, frame):
    raise TimeoutError('60 CPU-second / 150 wall-second replay budget exceeded')


signal.signal(signal.SIGPROF, timeout)
signal.signal(signal.SIGALRM, timeout)
signal.setitimer(signal.ITIMER_PROF, 60)
signal.alarm(150)

spec = importlib.util.spec_from_file_location('independent_injections', BASE / 'root/independent40_41.py')
injection = importlib.util.module_from_spec(spec)
spec.loader.exec_module(injection)  # module main is guarded; runs no old replay
bound = injection.bound
PAIRS = list(combinations(range(4), 2))
CLIQUE_PAIRS = {b: tuple(i for i, (x, y) in enumerate(PAIRS) if b >> x & 1 and b >> y & 1)
                for b in range(1, 16) if b.bit_count() >= 2}


def multiset_patterns(target):
    # Independent forward DP over all eleven clique masks, retaining every
    # permitted multiplicity. Unlike the submitted recursive generator, the
    # state is used pair capacities; each clique is processed exactly once.
    states = {(0,) * 6: {()}}
    for block, indices in CLIQUE_PAIRS.items():
        updates = {}
        for used, prefixes in states.items():
            limit = min(target[i] - used[i] for i in indices)
            for count in range(limit + 1):
                new = tuple(c + (count if i in indices else 0) for i, c in enumerate(used))
                tails = updates.setdefault(new, set())
                tails.update(prefix + (block,) * count for prefix in prefixes)
        states = updates
    return states[tuple(target)]


def key(degrees, double, blocks):
    return tuple(degrees), double, tuple(sorted(blocks))


def main():
    cert = json.loads((BASE / 'tail39_41/CERT39.json').read_text())
    assert cert['v'] == 39 and cert['M'] == 66
    degree0 = (38 + 4) // 5
    assert degree0 == 8
    products = [(5 * d - 37) * (11 - d) for d in range(8, 11)]
    Z = 11 * 39 - 396
    assert products == [9, 16, 13] and Z == 33 and Z > 2 * max(products)
    patterns = {}
    pattern_summary = []
    for double in (-1, 0, 1, 2):
        target = [1] * 6
        if double >= 0:
            target[PAIRS.index((double, 3))] = 2
        pp = multiset_patterns(target)
        assert len(pp) == (6 if double == -1 else 7)
        # At least-three traces can never repeat; the only repeatable mask
        # is the doubled two-point trace itself.
        for bs in pp:
            counts = Counter(bs)
            assert all(n == 1 or (double >= 0 and b == ((1 << double) | 8) and n == 2)
                       for b, n in counts.items())
        patterns[double] = pp
        pattern_summary.append(dict(double=double, target=target, count=len(pp), patterns=sorted(pp)))
    domain = set()
    degree_rows = []
    for first3 in combinations_with_replacement(range(8, 11), 3):
        t = sum(first3)
        E = 5 * t - 114
        p = 36 - E // 2
        excess = 108 - t
        D = 8 + excess // p
        assert p > 0 and E >= 0 and excess >= 0
        assert p * (D + 1 - 8) > excess
        expected_D = 10 if t <= 26 else 11 if t <= 29 else 12
        assert D == expected_D
        degree_rows.append(dict(first3=first3, t=t, external_conflict_excess=E,
                                eligible_external_count=p, external_degree_surplus=excess,
                                fourth_degree_maximum=D))
        for d4 in range(8, D + 1):
            for double, pp in patterns.items():
                domain.update(key(first3 + (d4,), double, bs) for bs in pp)
    assert len(domain) == 999
    rows = cert['rows']
    keys = [key(r['degrees'], r['double'], r['blocks']) for r in rows]
    assert len(rows) == len(keys) == len(set(keys)) == 999
    assert set(keys) == domain
    replay = []
    permuted_positions = 0
    for r in rows:
        ds = r['degrees']
        assert ds[:3] == sorted(ds[:3])  # Fourth vertex is a distinguished extra lock.
        ell = dict(Counter(r['blocks']))
        for i, d in enumerate(ds):
            ell[1 << i] = d - sum(n for b, n in ell.items() if b >> i & 1)
        ell[0] = 66 - sum(ell.values())
        assert min(ell.values()) >= 0 and sum(ell.values()) == 66
        assert ell == {int(b): n for b, n in r['ell'].items()}
        ell = {b: n for b, n in ell.items() if n}
        for i in range(4):
            assert sum(n for b, n in ell.items() if b >> i & 1) == ds[i]
        for i, j in PAIRS:
            expected = 1 + (r['double'] >= 0 and (i, j) == (r['double'], 3))
            assert sum(n for b, n in ell.items() if b >> i & 1 and b >> j & 1) == expected
        pos = r['positions']
        assert len(pos) == len(set(pos)) == 4 and all(1 <= x <= 39 for x in pos)
        permuted_positions += (pos != sorted(pos))
        # Do not sort slots, degrees or masks here: label j must stay attached
        # to the same position and to the same original edge traces.
        actual = bound(39, pos, ell)
        assert actual == Q(r['U']) < 1, (ds, r['double'], r['blocks'], actual, r['U'])
        assert r['strict'] is True
        replay.append(dict(degrees=ds, double=r['double'], blocks=r['blocks'],
                           positions=pos, U=str(actual), matches_original=True, strict=True))
    maximum = max(Q(r['U']) for r in replay)
    assert maximum == Q(cert['maximum']) == Q('113467943/113476275')
    result = dict(status='PASS', review_independence='same-family', acceptance_status='provisional',
                  scope='Complete v39/66-edge/pair-covering branch: selection arithmetic, entire distinguished-fourth degree and multiset-trace domain, all 999 recorded successful actual layouts replayed.',
                  selection=dict(Z=Z,Q=max(products),integer_products=products,rows=degree_rows),
                  classification=pattern_summary, complete_profiles=len(domain),
                  independently_replayed=len(replay), rows_with_nonmonotone_positions=permuted_positions,
                  maximum=str(maximum),
                  method='Independent forward pair-capacity multiset DP; existing independent falling-factorial uniform injections; separate maximum-over-R avoidance-quota deletion',
                  imported_probability='root/independent40_41.py bound; AST extraction of old independent/check.py probs; guarded main not executed',
                  submitted_class_generator_imported=False, submitted_probability_module_imported=False,
                  cpu_seconds=time.process_time()-START,wall_seconds=time.monotonic()-WALL_START,
                  rows=replay)
    (HERE/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','classification','selection')},indent=2))


if __name__ == '__main__':
    main()
