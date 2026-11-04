"""Independent spectra audit: full mate-set subtraction and edge-bit unions."""
from pathlib import Path
from itertools import combinations, permutations
import hashlib
import json
from q4_core_independent_audit import all_mates, require

ROOT = Path(__file__).resolve().parent
SHORT = {(x, x ^ (1 << i)) for x in range(16) for i in range(4) if x < (x ^ (1 << i))}
EDGE_BIT = {edge: 1 << i for i, edge in enumerate(sorted(SHORT))}


def spectrum(mode, s):
    name = f'q4_spectrum_{mode}_{s}.bin'
    data = (ROOT / name).read_bytes()
    universe = set(all_mates(set(range(16)) - {0, s}))
    require(len(universe) == 135135 and len(EDGE_BIT) == 32, 'universe')
    length, bound = (15, 15) if mode == 'A' else (16, 18)
    support = list(range(1, 16)) if mode == 'A' else list(range(16))
    cursor = records = circles = 0
    minimum = 33
    while cursor < len(data):
        require(cursor + 17 <= len(data), 'truncated header')
        mate = data[cursor:cursor+16]
        count = data[cursor+16]
        cursor += 17
        require(mate in universe, 'invalid/duplicate matching')
        universe.remove(mate)
        require(count > 0 and cursor + count * length <= len(data), 'truncated circles')
        mask = 0
        for _ in range(count):
            cycle = list(data[cursor:cursor+length])
            cursor += length
            require(sorted(cycle) == support, 'incorrect circle support')
            positions = {v: i for i, v in enumerate(cycle)}
            for x, y in enumerate(mate):
                if y != 255:
                    require((positions[x] - positions[y]) % length in (1, length-1), 'matching edge omitted')
            for i, x in enumerate(cycle):
                y = cycle[(i+1) % length]
                if mate[x] != y:
                    bit = EDGE_BIT.get((min(x, y), max(x, y)), 0)
                    require(bit != 0, 'long added edge')
                    mask |= bit
            circles += 1
        require(mask.bit_count() >= bound, 'insufficient optional-edge union')
        minimum = min(minimum, mask.bit_count())
        records += 1
    require(cursor == len(data) and not universe and records == 135135, 'incomplete coverage')
    return {'file': name, 'records': records, 'circles': circles, 'bound': bound,
            'minimum_certified_union': minimum, 'sha256': hashlib.sha256(data).hexdigest()}


def geometry():
    odds = [x for x in range(32) if x.bit_count() % 2]
    residual = [x for x in odds if x.bit_count() >= 3]
    stats = {'S2D': 0, 'S3D': 0, 'both': 0, 'solved_union': 0, 'remaining': 0}
    leftovers = []
    perms = list(permutations(range(5)))
    for b, t in combinations(residual, 2):
        for v in odds:
            if v in (b, t):
                continue
            s2 = bool(v & (b ^ t))
            s3 = bool(v & b & t)
            stats['S2D'] += s2
            stats['S3D'] += s3
            stats['both'] += s2 and s3
            stats['solved_union'] += s2 or s3
            stats['remaining'] += not(s2 or s3)
            if s2 or s3:
                continue
            require(v & (b | t) == 0, 'disjoint support reduction')
            require(v.bit_count() == 1 and b.bit_count() == t.bit_count() == 3, 'weight reduction')
            def image(x, perm):
                return sum((x >> i & 1) << perm[i] for i in range(5))
            require(any(image(v, p) == 1 and {image(b, p), image(t, p)} == {14, 22} for p in perms), 'uncovered residual orbit')
            leftovers.append([b, t, v])
    require(stats['solved_union'] == 740 and stats['remaining'] == 30, 'geometry totals')
    return {'counts': stats, 'remaining_configurations': leftovers, 'representative': {'a': 0, 'v': 1, 'b': 14, 't': 22}}


def main():
    reports = [spectrum(mode, s) for mode, choices in [('A', (3, 15)), ('B', (1, 7))] for s in choices]
    result = {'status': 'PASS', 'matchings': sum(r['records'] for r in reports),
              'circles': sum(r['circles'] for r in reports), 'files': reports,
              'method': 'explicit matching-set subtraction; positional edge containment; 32-bit optional edge union',
              'geometry': geometry(),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'helper_sha256': hashlib.sha256((ROOT / 'q4_core_independent_audit.py').read_bytes()).hexdigest()}
    (ROOT / 'a4_single_geometry_independent_audit.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'matchings', 'circles')}, indent=2))
    print(json.dumps(result['geometry']['counts']))


if __name__ == '__main__':
    main()
