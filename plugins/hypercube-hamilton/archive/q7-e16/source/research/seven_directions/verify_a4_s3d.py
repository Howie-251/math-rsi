"""Standard-library exhaustive geometry verification; not a matching enumeration."""
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def signature(z, a, b):
    def cols(x, y):
        c = Counter(((z >> j) & 1, (x >> j) & 1, (y >> j) & 1) for j in range(6))
        return tuple(c[(i >> 2, (i >> 1) & 1, i & 1)] for i in range(8))
    return min(cols(a, b), cols(b, a))

def oddblock(z, a, b):
    good = [j for j in range(6) if (z >> j) & 1 and ((a ^ b) >> j) & 1]
    counts = Counter(tuple((v >> j) & 1 for j in good) for v in range(64) if v not in (0, z, a, b))
    return any(c % 2 for c in counts.values())

def main():
    source = json.loads((ROOT / 'Q6_A4_GEOMETRY.json').read_text(encoding='utf-8'))
    lookup = {signature(*r['representative']): (i, r) for i, r in enumerate(source['orbits'])}
    assert len(lookup) == 52
    observed = Counter()
    statuses = {}
    aug = 0
    odd = [v for v in range(64) if v.bit_count() % 2]
    for z in odd:
        for a, b in combinations([v for v in odd if v != z], 2):
            if a.bit_count() == 1 or b.bit_count() == 1:
                aug += 1
                continue
            key = signature(z, a, b)
            observed[key] += 1
            closed = oddblock(z, a, b) or bool(z & a & b)
            if key in statuses:
                assert statuses[key] == closed
            statuses[key] = closed
    remaining = []
    for key, count in observed.items():
        i, r = lookup[key]
        assert count == r['size']
        if not statuses[key]:
            remaining.append(dict(index=i, representative=r['representative'], size=count, good_directions=r['good_directions']))
    remaining.sort(key=lambda x: x['index'])
    result = dict(verification='PASS', full_P7_proved=False, full_A6_4_proved=False,
                  normalized_geometries=aug + sum(observed.values()), augmentation_closed=aug,
                  post_augmentation_orbits=len(observed), closed_orbits=sum(statuses.values()),
                  closed_post_augmentation_geometries=sum(v for k, v in observed.items() if statuses[k]),
                  remaining_orbits=len(remaining), remaining_geometries=sum(r['size'] for r in remaining),
                  remaining=remaining)
    assert (aug, result['closed_orbits'], result['remaining_orbits'], result['remaining_geometries']) == (5130, 38, 14, 1800)
    (ROOT / 'A4_S3D_COUNTS.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k != 'remaining'}, ensure_ascii=False))

if __name__ == '__main__':
    main()
