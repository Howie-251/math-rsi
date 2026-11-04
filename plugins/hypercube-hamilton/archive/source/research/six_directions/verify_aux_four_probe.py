"""Independent stdlib cycle certificate and geometry-census validation."""
import hashlib
import json
from collections import Counter
from pathlib import Path

R = Path(__file__).resolve().parent
out = []
for name in ('auxiliary_four_hole_probe.json', 'half_layer_four_hole_probe.json'):
    raw = (R/name).read_bytes()
    data = json.loads(raw)
    count = Counter()
    for c in data['cases']:
        assert c['status'] == 'FOUND'
        m = {tuple(sorted(e)) for e in c['matching']}
        assert len(m) == 14 and len({v for e in m for v in e}) == 28
        assert all(0 <= a < b < 32 for a, b in m)
        holes = set(range(32))-{v for e in m for v in e}
        assert holes == set(c['holes']) and len(holes) == 4
        v = c['forbidden']
        wanted = set(range(32))-({v} if v is not None else set())
        if v is None:
            assert sum(x.bit_count() % 2 for x in holes) == 2
        else:
            assert v in holes and v.bit_count() % 2 == 1
            assert sum(x.bit_count() % 2 for x in holes) == 3
        cyc = c['cycle']
        assert len(cyc) == len(wanted) and set(cyc) == wanted
        es = {tuple(sorted(e)) for e in zip(cyc, cyc[1:]+cyc[:1])}
        assert m <= es
        assert all((a ^ b).bit_count() == 1 or (a, b) in m for a, b in es)
        count['A4_avoid' if v is not None else 'balanced_cycle'] += 1
    out.append(dict(input=name, sha256=hashlib.sha256(raw).hexdigest(), counts=dict(count)))

rows = json.loads((R/'remaining_samples_after_Z5.json').read_text(encoding='utf8'))['remaining']
census = []
for c in rows:
    holes = set(range(64))-{q for e in c['matching'] for q in e}
    u, v = c['u'], c['v']
    if len(holes) != 6 or v in holes:
        continue
    hs = holes-{u} | {v}
    cuts = []
    for i in range(6):
        ah = {q for q in hs if ((q ^ v) >> i) & 1 == 0}
        p = (sum(q.bit_count() % 2 == 0 for q in ah), sum(q.bit_count() % 2 == 1 for q in ah))
        if p in {(1, 2), (1, 3), (0, 3)}:
            cuts.append(dict(cut=i, shape=p))
    assert cuts
    census.append(dict(u=u, v=v, holes=sorted(holes), eligible_cuts=cuts))
assert len(census) == 153
result = dict(status='PASS', probe_checks=out, S4_old_sample_census=census,
              S4_old_sample_cases=len(census), A4_proved=False, full_p6_proved=False)
(R/'aux_four_probe_verification.json').write_text(json.dumps(result, indent=2), encoding='utf8')
print(json.dumps(dict(status='PASS', probe_checks=out, S4_cases=len(census),
                     A4_proved=False, full_p6_proved=False), indent=2))
