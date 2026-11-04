"""Independent exhaustive positive-certificate verification.

Every 31-byte record has a 16-byte mate array (255=hole), then a 15-vertex
circle. A bijective perfect-matching rank certifies coverage independently
of the producer's recursion or search algorithm.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def pairings(n):
    result = 1
    for k in range(n - 1, 0, -2):
        result *= k
    return result


def rank_matching(mate, vertices):
    remaining = sorted(vertices)
    rank = 0
    while remaining:
        x = remaining.pop(0)
        index = remaining.index(mate[x])
        rank += index * pairings(len(remaining) - 1)
        remaining.pop(index)
    return rank


def check(name, holes, forbidden):
    p = ROOT / name
    raw = p.read_bytes()
    assert len(raw) % 31 == 0
    count = pairings(16 - len(holes))
    assert len(raw) // 31 == count
    covered = set(range(16)) - set(holes)
    seen = bytearray(count)
    for offset in range(0, len(raw), 31):
        mate, circle = raw[offset:offset + 16], raw[offset + 16:offset + 31]
        assert {x for x in range(16) if mate[x] == 255} == set(holes)
        for x in covered:
            assert mate[x] in covered and mate[x] != x and mate[mate[x]] == x
        rank = rank_matching(mate, covered)
        assert 0 <= rank < count and seen[rank] == 0
        seen[rank] = 1
        assert len(set(circle)) == 15 and set(circle) == set(range(16)) - {forbidden}
        edges = {frozenset((x, y)) for x, y in zip(circle, circle[1:] + circle[:1])}
        f = {frozenset((x, mate[x])) for x in covered}
        assert f <= edges and len(edges) == 15
        for e in edges - f:
            x, y = e
            assert (x ^ y).bit_count() == 1
    assert all(seen)
    return {'file': name, 'holes': holes, 'forbidden': forbidden,
            'records': count, 'distinct_matching_ranks': sum(seen),
            'sha256': hashlib.sha256(raw).hexdigest()}


def main():
    reports = [check(f'q4_two_hole_{s}.bin', [0, s], 0) for s in (3, 15)]
    reports += [check(f'q4_four_hole_{v}.bin', [0, 7, 11, v], v) for v in (1, 4, 13)]
    result = {'status': 'PASS', 'scope': 'Q4 two-hole and residual A4 orbit representatives',
              'records_verified': sum(r['records'] for r in reports), 'orbits': reports,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'q5_a4_proved': False, 'full_p6_proved': False}
    (ROOT / 'q4_extension_certificate_verification.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': result['status'], 'records_verified': result['records_verified']}))


if __name__ == '__main__':
    main()
