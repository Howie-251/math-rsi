"""Verify positive edge-spectrum lower bounds and full matching coverage."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def matching_count(n):
    answer = 1
    for x in range(1, n, 2):
        answer *= x
    return answer


def check(mode, s):
    name = f'q4_spectrum_{mode}_{s}.bin'
    data = (ROOT / name).read_bytes()
    holes = {0, s}
    covered = set(range(16)) - holes
    required_vertices = set(range(16)) - ({0} if mode == 'A' else set())
    length = len(required_vertices)
    threshold = 15 if mode == 'A' else 18
    seen = bytearray(135135)
    pos = records = circles = 0
    min_union = 33
    while pos < len(data):
        assert pos + 17 <= len(data)
        mate = data[pos:pos + 16]
        count = data[pos + 16]
        pos += 17
        assert count > 0 and pos + count * length <= len(data)
        assert {x for x in range(16) if mate[x] == 255} == holes
        for x in covered:
            assert mate[x] in covered and mate[x] != x and mate[mate[x]] == x
        rest = sorted(covered)
        rank = 0
        while rest:
            x = rest.pop(0)
            i = rest.index(mate[x])
            rank += i * matching_count(len(rest) - 1)
            rest.pop(i)
        assert 0 <= rank < len(seen) and seen[rank] == 0
        seen[rank] = 1
        required = {frozenset((x, mate[x])) for x in covered}
        union = set()
        for _ in range(count):
            cycle = data[pos:pos + length]
            pos += length
            assert len(set(cycle)) == length and set(cycle) == required_vertices
            edges = {frozenset((x, y)) for x, y in zip(cycle, cycle[1:] + cycle[:1])}
            assert len(edges) == length and required <= edges
            optional = edges - required
            for e in optional:
                x, y = e
                assert (x ^ y).bit_count() == 1
            union.update(optional)
            circles += 1
        assert len(union) >= threshold
        min_union = min(min_union, len(union))
        records += 1
    assert pos == len(data) and records == 135135 and all(seen)
    return {'file': name, 'records': records, 'cycle_certificates': circles,
            'lower_bound': threshold, 'minimum_certified_union': min_union,
            'sha256': hashlib.sha256(data).hexdigest()}


def main():
    reports = [check(mode, s) for mode, choices in [('A', (3, 15)), ('B', (1, 7))]
               for s in choices]
    result = {'status': 'PASS', 'scope': 'Q4 optional-edge lower bounds A>=15, B>=18',
              'matchings_verified': sum(r['records'] for r in reports),
              'cycles_verified': sum(r['cycle_certificates'] for r in reports),
              'files': reports,
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'q5_a4_proved': False, 'full_p6_proved': False}
    (ROOT / 'q4_spectrum_verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'matchings_verified', 'cycles_verified')}))


if __name__ == '__main__':
    main()
