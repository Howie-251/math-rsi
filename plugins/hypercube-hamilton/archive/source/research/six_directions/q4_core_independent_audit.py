"""Fresh audit: explicit matching-set subtraction, cycle positions, and orbit coverage.

This deliberately does not import the producer or its rank-based verifier.
Run with ordinary Python; all checks use explicit exceptions (also under -O).
"""
from pathlib import Path
from itertools import permutations, combinations
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def all_mates(vertices):
    # Largest pivot, descending partner order, unlike the submitted generator.
    work = bytearray([255] * 16)
    def visit(left):
        if not left:
            yield bytes(work)
            return
        x, rest = left[-1], left[:-1]
        for i in range(len(rest) - 1, -1, -1):
            y = rest[i]
            work[x], work[y] = y, x
            yield from visit(rest[:i] + rest[i+1:])
            work[x] = work[y] = 255
    yield from visit(sorted(vertices))


def certificate_audit(filename, holes, forbidden):
    expected = set(all_mates(set(range(16)) - set(holes)))
    count = len(expected)
    data = (ROOT / filename).read_bytes()
    require(len(data) == count * 31, filename + ': size')
    for offset in range(0, len(data), 31):
        mate = data[offset:offset+16]
        require(mate in expected, filename + ': omitted/duplicate/invalid matching')
        expected.remove(mate)
        cycle = list(data[offset+16:offset+31])
        require(sorted(cycle) == [v for v in range(16) if v != forbidden], 'cycle support')
        positions = {v: i for i, v in enumerate(cycle)}
        for x, y in enumerate(mate):
            if y != 255:
                require((positions[x] - positions[y]) % 15 in (1, 14), 'required edge absent')
        for i, x in enumerate(cycle):
            y = cycle[(i+1) % 15]
            require(mate[x] == y or (x ^ y) in (1, 2, 4, 8), 'long added edge')
    require(not expected, 'coverage incomplete')
    return {'file': filename, 'records': count, 'sha256': hashlib.sha256(data).hexdigest()}


PERMS = list(permutations(range(4)))
def transform(x, perm):
    return sum(((x >> i) & 1) << perm[i] for i in range(4))


def geometry_audit():
    odds = [v for v in range(16) if v.bit_count() % 2]
    two = {3: 0, 15: 0}
    for s in range(1, 16):
        if s.bit_count() % 2 == 0:
            images = {transform(s, p) for p in PERMS}
            reps = images & set(two)
            require(len(reps) == 1, 'two-hole orbit failure')
            two[reps.pop()] += 1
    residual = {1: 0, 4: 0, 13: 0}
    adjacent = 0
    for v in odds:
        for b, t in combinations([x for x in odds if x != v], 2):
            if b in (1, 2, 4, 8) or t in (1, 2, 4, 8):
                adjacent += 1
                continue
            target = set()
            for p in PERMS:
                if {transform(b, p), transform(t, p)} == {7, 11}:
                    vp = transform(v, p)
                    if vp in residual:
                        target.add(vp)
            require(len(target) == 1, 'four-hole orbit failure')
            residual[target.pop()] += 1
    counts = [0, 0, 0]
    nonneighbors = [v for v in range(32) if v.bit_count() % 2 and v.bit_count() != 1]
    for b, t in combinations(nonneighbors, 2):
        for v in range(32):
            if not v.bit_count() % 2 or v in (b, t):
                continue
            m1, m2 = v & b & (31 ^ t), v & t & (31 ^ b)
            n = bool(m1) + bool(m2)
            counts[n] += 1
            if n == 2:
                for i in range(5):
                    for j in range(5):
                        if (m1 >> i & 1) and (m2 >> j & 1):
                            patterns = {((x >> i) & 1, (x >> j) & 1) for x in (0, b, t, v)}
                            require(len(patterns) == 4, 'G4D cell failure')
    require(counts == [165, 350, 255], 'geometry counts')
    return {'two_hole_orbit_sizes': two, 'four_hole_adjacent_branch': adjacent,
            'four_hole_residual_orbit_sizes': residual, 'Q5_mask_counts_0_1_2': counts}


def main():
    reports = [certificate_audit(f'q4_two_hole_{s}.bin', (0, s), 0) for s in (3, 15)]
    reports += [certificate_audit(f'q4_four_hole_{v}.bin', (0, 7, 11, v), v) for v in (1, 4, 13)]
    result = {'status': 'PASS', 'records': sum(x['records'] for x in reports),
              'certificates': reports, 'geometry': geometry_audit(),
              'method': 'explicit exhaustive matching-set subtraction; position-based cycle audit',
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT / 'q4_core_independent_audit.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
