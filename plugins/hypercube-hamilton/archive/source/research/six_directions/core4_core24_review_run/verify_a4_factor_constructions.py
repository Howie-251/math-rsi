"""Independent certificate check: no imports from the constructor."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
source = ROOT / 'a4_factor_construction_results.json'
data = json.loads(source.read_text(encoding='utf-8'))
for c in data['cases']:
    f = {frozenset(e) for e in c['matching']}
    covered = [x for e in f for x in e]
    assert len(f) == 14 and len(set(covered)) == len(covered) == 28
    holes = set(range(32)) - set(covered)
    assert c['forbidden'] in holes
    majority = [x for x in holes if x.bit_count() % 2 == c['forbidden'].bit_count() % 2]
    assert len(majority) == 3
    minority, = holes - set(majority)
    assert all((minority ^ x).bit_count() != 1 for x in majority if x != c['forbidden'])
    seen = []
    edges = set()
    for cycle in c['cycles']:
        assert len(cycle) >= 3 and len(set(cycle)) == len(cycle)
        seen.extend(cycle)
        for x, y in zip(cycle, cycle[1:] + cycle[:1]):
            e = frozenset((x, y))
            assert len(e) == 2 and e not in edges
            assert e in f or (x ^ y).bit_count() == 1
            edges.add(e)
    assert len(seen) == 31 and set(seen) == set(range(32)) - {c['forbidden']}
    assert f <= edges and frozenset(c['prescribed']) in edges
result = {'status': 'PASS', 'certificates_checked': len(data['cases']),
          'scope': 'spanning cycle factors with one prescribed edge, not Hamilton cycles',
          'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'full_p6_proved': False}
(ROOT / 'a4_factor_construction_verification.json').write_text(
    json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result))
