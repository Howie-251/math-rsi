"""Independent positive-certificate audit for the zero-crossing residual.

Rebuilds the exceptional B list from all 13!! pairings and the independently
checked Q4 negative classification, then checks every residual full Q5 cycle.
"""
import collections
import hashlib
import itertools
import json
from pathlib import Path

R = Path(__file__).resolve().parent
def edge(a, b):
    return tuple(sorted((a, b)))
def pairings(vs):
    if not vs:
        yield ()
        return
    a, *tail = vs
    for i, b in enumerate(tail):
        for f in pairings(tail[:i] + tail[i+1:]):
            yield ((a, b),) + f
def swap(x):
    return (x & ~6) | ((x & 2) << 1) | ((x & 4) >> 1)
def main():
    q4 = json.loads((R/'q4_three_avoided_verification.json').read_text())
    neg = {tuple(sorted(r['omitted'][:2])):
           {frozenset(map(tuple,t['matching'])) for t in r['negative_records']}
           for r in q4['families']}
    neg[5, 6] = {frozenset(edge(swap(a),swap(b)) for a,b in f)
                 for f in neg[3, 6]}
    hist = collections.Counter()
    failures = []
    for f in pairings([v for v in range(16) if v not in (0,1)]):
        fs = frozenset(f)
        mate = {a:b for e in f for a,b in (e,e[::-1])}
        good = 0
        for s,t in ((3,5),(3,6),(5,6)):
            if mate[s] == t:
                continue
            suppressed = fs - {edge(s,mate[s]),edge(t,mate[t])}
            suppressed |= {edge(mate[s],mate[t])}
            good += suppressed not in neg[s,t]
        hist[good] += 1
        if not good:
            failures.append(f)
    recorded = json.loads((R/'t15_core0_three_avoid_choice.json').read_text())
    assert failures == [tuple(map(tuple,f)) for f in recorded['failures']]
    assert len(failures) == 18
    data = (R/'t15_core0_double_bridge_residual.bin').read_bytes()
    count = 0
    expected_support = set(range(32)) - {1,2}
    for fa in pairings([v for v in range(16) if v not in (0,3,5,6)]):
        for fb in failures:
            expected = tuple((2*a+1,2*b+1) for a,b in fa)
            expected += tuple((2*a,2*b) for a,b in fb)
            rec = data[count*56:(count+1)*56]
            assert len(rec) == 56
            required = tuple(zip(rec[:26:2],rec[1:26:2]))
            assert required == expected
            cycle = tuple(rec[26:])
            assert len(cycle) == len(set(cycle)) == 30
            assert set(cycle) == expected_support
            ce = {edge(cycle[i-1],cycle[i]) for i in range(30)}
            re = {edge(a,b) for a,b in required}
            assert re <= ce
            assert all((a^b).bit_count() == 1 for a,b in ce-re)
            count += 1
    assert count == 187110
    assert len(data) == count*56
    report = dict(status='PASS', scope='core0 zero original crossings only',
                  all_B_matchings=sum(hist.values()), good_pair_histogram=dict(hist),
                  exceptional_B_matchings=len(failures), A_matchings=10395,
                  full_Q5_positive_certificates=count,
                  certificate_sha256=hashlib.sha256(data).hexdigest(),
                  positive_crossing_core0_proved=False, full_T15_proved=False,
                  full_P6_proved=False)
    (R/'t15_core0_double_bridge_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__ == '__main__':
    main()
