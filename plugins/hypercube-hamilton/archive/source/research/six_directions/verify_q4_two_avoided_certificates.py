"""Check all 311850 explicit 14-cycles and matching-rank coverage."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def count_matchings(n):
    value = 1
    for k in range(1, n, 2):
        value *= k
    return value


def check(p, b, t):
    name = f'q4_two_avoided_{p}_{b}_{t}.bin'
    raw = (ROOT / name).read_bytes()
    count = 10395
    assert len(raw) == 30 * count
    holes = {0, p, b, t}
    covered = set(range(16)) - holes
    visited = bytearray(count)
    for offset in range(0, len(raw), 30):
        mate = raw[offset:offset + 16]
        cycle = raw[offset + 16:offset + 30]
        assert {x for x in range(16) if mate[x] == 255} == holes
        for x in covered:
            assert mate[x] in covered and mate[x] != x and mate[mate[x]] == x
        remaining = sorted(covered)
        rank = 0
        while remaining:
            x = remaining.pop(0)
            i = remaining.index(mate[x])
            rank += i * count_matchings(len(remaining) - 1)
            remaining.pop(i)
        assert 0 <= rank < count and visited[rank] == 0
        visited[rank] = 1
        assert len(set(cycle)) == 14 and set(cycle) == set(range(16)) - {0, p}
        edges = {frozenset((x, y)) for x, y in zip(cycle, cycle[1:] + cycle[:1])}
        required = {frozenset((x, mate[x])) for x in covered}
        assert len(edges) == 14 and required <= edges
        for e in edges - required:
            x, y = e
            assert (x ^ y).bit_count() == 1
    assert all(visited)
    return {'file': name, 'holes': sorted(holes), 'avoided': [0, p],
            'records': count, 'sha256': hashlib.sha256(raw).hexdigest()}


def main():
    even = [x for x in range(16) if x.bit_count() % 2 == 0]
    reports = []
    for p in (3, 15):
        rest = [x for x in even if x not in (0, p)]
        for i, b in enumerate(rest):
            for t in rest[i + 1:]:
                reports.append(check(p, b, t))
    result = {'status': 'PASS', 'configurations': len(reports),
              'records_verified': sum(r['records'] for r in reports),
              'scope': 'Q4 four same-parity holes with two prescribed avoided holes',
              'files': reports,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'q5_a4_proved': False, 'full_p6_proved': False}
    (ROOT / 'q4_two_avoided_verification.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'configurations', 'records_verified')}))


if __name__ == '__main__':
    main()
