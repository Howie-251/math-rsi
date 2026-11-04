"""Check positive E3 witnesses independently of the cut/reconnect search.

Negative EXHAUSTED reports are deliberately not certified here.
"""
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def edges(seq):
    return {tuple(sorted(e)) for e in zip(seq, seq[1:] + seq[:1])}


def main():
    source = ROOT/'a4_edge_elimination_probe.json'
    raw = source.read_bytes()
    data = json.loads(raw)
    counts = Counter()
    for c in data['cases']:
        a, b, v, t = (c[key] for key in ('a', 'b', 'v', 't'))
        f = {tuple(sorted(e)) for e in c['matching']}
        assert len(f) == 14 and len({x for e in f for x in e}) == 28
        assert set(range(32)) - {x for e in f for x in e} == {a, b, v, t}
        assert a.bit_count() % 2 == 0
        assert all(x.bit_count() % 2 == 1 for x in (b, v, t))
        aux = tuple(sorted((a, b)))
        assert (a ^ b).bit_count() == 3
        old = c['cycle_with_aux']
        oe = edges(old)
        assert len(old) == 31 and set(old) == set(range(32)) - {v}
        assert f | {aux} <= oe
        assert all((x ^ y).bit_count() == 1 for x, y in oe - f - {aux})
        found = [r for name, r in c.items() if name.startswith('eliminate') and r['status'] == 'FOUND']
        assert found
        for r in found:
            new = r['cycle']
            ne = edges(new)
            assert len(new) == 31 and set(new) == set(old)
            assert f <= ne and aux not in ne
            assert all((x ^ y).bit_count() == 1 for x, y in ne - f)
            assert len(oe - ne) == r['deleted_old_edges']
            counts[r['deleted_old_edges']] += 1
    out = dict(status='PASS', verified=len(data['cases']),
               scope='positive E3 replacement witnesses only; EXHAUSTED claims not independently certified',
               old_deleted_histogram=dict(counts), input_sha256=hashlib.sha256(raw).hexdigest(),
               a4_proved=False, full_p6_proved=False)
    (ROOT/'a4_edge_elimination_verification.json').write_text(json.dumps(out, indent=2), encoding='utf8')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
