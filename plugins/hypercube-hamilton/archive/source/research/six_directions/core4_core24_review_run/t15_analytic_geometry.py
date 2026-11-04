"""Independent geometric census; no cycle existence assertions."""
import itertools as it
import json
from collections import Counter
from pathlib import Path

odd = [v for v in range(32) if v.bit_count() % 2]
even = [v for v in range(32) if not v.bit_count() % 2]
perms = list(it.permutations(range(5)))
maps = [[sum(((v >> i) & 1) << p[i] for i in range(5)) for v in range(32)] for p in perms]

def t44_canonical(banned, included):
    ans = []
    for a in banned:
        for m in maps:
            ans.append((tuple(sorted(m[v ^ a] for v in banned)), tuple(sorted(m[v ^ a] for v in included))))
    return min(ans)

result = {'scope': 'Geometry only; original matching edges may be arbitrary.'}
def forces_positive(holes, coords):
    if not coords:
        return False
    counts = Counter(tuple((v >> j) & 1 for j in coords) for v in holes)
    size = 1 << (5-len(coords))
    return any((size-counts[p]) % 2 for p in it.product((0,1), repeat=len(coords)))

t44 = []
for y in (3, 15):
    counts = Counter()
    bad = Counter()
    forced = 0
    for included in it.combinations([v for v in even if v not in (0, y)], 2):
        split = bool(y & (included[0] ^ included[1]))
        same = any(not any((v >> j) & 1 for v in (0, y, *included)) for j in range(5))
        counts[(split, same)] += 1
        coords = [j for j in range(5) if ((y & (included[0] ^ included[1])) >> j) & 1
                  or not any((v >> j) & 1 for v in (0, y, *included))]
        forced += forces_positive((0,y,*included), coords)
        if not split:
            bad[t44_canonical((0, y), included)] += 1
    t44.append({'other_avoided': y, 'positive_good_cut_forced': forced, 'counts': [{'split': a, 'same': b, 'count': n} for (a,b), n in sorted(counts.items())],
                'no_split_orbits': [{'avoided': k[0], 'included': k[1], 'count': n} for k,n in sorted(bad.items())]})
result['T44'] = t44

counts = Counter()
residual = Counter()
forced = 0
for included in it.combinations([v for v in odd if v.bit_count() > 1], 3):
    for banned in it.combinations([v for v in odd if v not in included], 2):
        holes = (*included, *banned)
        split = []
        same = []
        for j in range(5):
            colsum = sum((v >> j) & 1 for v in holes)
            if colsum == 2 and ((banned[0] ^ banned[1]) >> j) & 1:
                split.append(j)
            if colsum == 4 and all((v >> j) & 1 for v in banned):
                same.append(j)
        counts[(bool(split), bool(same))] += 1
        forced += forces_positive((0,*holes), sorted(set(split+same)))
        if not split and not same:
            key = min((tuple(sorted(m[v] for v in banned)), tuple(sorted(m[v] for v in included))) for m in maps)
            residual[key] += 1
result['T15'] = {'normalized_configurations': sum(counts.values()),
                 'positive_good_cut_forced': forced,
                 'counts': [{'split': a, 'same': b, 'count': n} for (a,b),n in sorted(counts.items())],
                 'residual_orbit_count': len(residual),
                 'residual_orbits': [{'avoided': k[0], 'included': k[1], 'count': n} for k,n in sorted(residual.items())]}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps({'T44': t44, 'T15': {k:v for k,v in result['T15'].items() if k != 'residual_orbits'}}, indent=2))
