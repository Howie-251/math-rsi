"""Fresh two-avoided certificate audit using explicit mate-set subtraction."""
from pathlib import Path
from itertools import combinations, permutations
import hashlib
import json
from q4_core_independent_audit import all_mates, require

ROOT = Path(__file__).resolve().parent


def check_file(p, b, t):
    name = f'q4_two_avoided_{p}_{b}_{t}.bin'
    data = (ROOT / name).read_bytes()
    expected = set(all_mates(set(range(16)) - {0, p, b, t}))
    require(len(expected) == 10395 and len(data) == 30 * len(expected), 'universe/size')
    for offset in range(0, len(data), 30):
        mate = data[offset:offset+16]
        require(mate in expected, 'invalid/duplicate mate array')
        expected.remove(mate)
        cycle = list(data[offset+16:offset+30])
        require(sorted(cycle) == [v for v in range(16) if v not in (0, p)], 'cycle support')
        pos = {v: i for i, v in enumerate(cycle)}
        for x, y in enumerate(mate):
            if y != 255:
                require((pos[x] - pos[y]) % 14 in (1, 13), 'missing prescribed edge')
        for i, x in enumerate(cycle):
            y = cycle[(i+1) % 14]
            require(mate[x] == y or (x ^ y) in (1, 2, 4, 8), 'long added edge')
    require(not expected, 'incomplete coverage')
    return {'file': name, 'records': 10395, 'sha256': hashlib.sha256(data).hexdigest()}


def geometry_check(configs):
    perms = list(permutations(range(4)))
    def image(x, p):
        return sum((x >> k & 1) << p[k] for k in range(4))
    checked = 0
    for parity in (0, 1):
        vertices = [x for x in range(16) if x.bit_count() % 2 == parity]
        for holes in combinations(vertices, 4):
            for avoided in combinations(holes, 2):
                x, y = avoided
                others = [h ^ x for h in holes if h not in avoided]
                valid = False
                for perm in perms:
                    pp = image(y ^ x, perm)
                    bb, tt = sorted(image(h, perm) for h in others)
                    if (pp, bb, tt) in configs:
                        valid = True
                        break
                require(valid, 'T44 uncovered symmetry case')
                checked += 1
    require(checked == 840, 'T44 geometry count')
    counts = {'G4D': 0, 'G2D': 0, 'intersection': 0, 'union': 0, 'neither': 0}
    odds = [x for x in range(32) if x.bit_count() % 2]
    residual = [x for x in odds if x.bit_count() != 1]
    for b, t in combinations(residual, 2):
        for v in odds:
            if v in (b, t):
                continue
            g4 = bool(v & b & (31 ^ t)) and bool(v & t & (31 ^ b))
            g2 = (b & t & v).bit_count() >= 2
            counts['G4D'] += g4
            counts['G2D'] += g2
            counts['intersection'] += g4 and g2
            counts['union'] += g4 or g2
            counts['neither'] += not(g4 or g2)
            if g2:
                for i, j in combinations([k for k in range(5) if b & t & v & (1 << k)], 2):
                    require(all((h >> i & 1, h >> j & 1) == (1, 1) for h in (b, t, v)), 'majority cell')
                    require((1 << i) not in (b, t, v) and (1 << j) not in (b, t, v), 'bridge hole')
    require(counts == {'G4D': 255, 'G2D': 120, 'intersection': 30, 'union': 345, 'neither': 425}, 'geometry partition')
    return {'all_T44_hole_and_unordered_avoided_configurations': checked, 'Q5_counts': counts}


def main():
    even = [x for x in range(16) if x.bit_count() % 2 == 0]
    configs = {(p, b, t) for p in (3, 15) for b, t in combinations([x for x in even if x not in (0, p)], 2)}
    require(len(configs) == 30, 'certificate configuration count')
    reports = [check_file(*config) for config in sorted(configs)]
    result = {'status': 'PASS', 'records': sum(r['records'] for r in reports),
              'method': 'explicit complete mate-set subtraction and position-based cycle validation',
              'certificates': reports, 'geometry': geometry_check(configs),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'helper_sha256': hashlib.sha256((ROOT / 'q4_core_independent_audit.py').read_bytes()).hexdigest()}
    (ROOT / 'q4_two_avoided_independent_audit.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'records', 'geometry')}, indent=2))


if __name__ == '__main__':
    main()
