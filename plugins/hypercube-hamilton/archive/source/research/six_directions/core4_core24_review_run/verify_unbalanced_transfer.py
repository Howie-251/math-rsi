"""Independent stdlib-only verification of recorded Z7 construction witnesses."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def edges(path):
    return {tuple(sorted((a, b))) for a, b in zip(path, path[1:])}


def matching(raw, vertices, holes):
    m = {tuple(sorted(e)) for e in raw}
    assert len(m) == len(raw)
    covered = [q for e in m for q in e]
    assert len(covered) == len(set(covered))
    assert set(covered) == set(vertices) - set(holes)
    return m


def extension(path, vertices, prescribed, start, end):
    assert path[0] == start and path[-1] == end
    assert len(path) == len(vertices) and set(path) == set(vertices)
    pe = edges(path)
    assert prescribed <= pe
    assert all((a ^ b).bit_count() == 1 for a, b in pe - prescribed)


def main():
    source = ROOT / (sys.argv[1] if len(sys.argv) > 1 else 'unbalanced_transfer_results.json')
    data = json.loads(source.read_text(encoding='utf8'))
    counts = {'verified': 0, 'single_cross': 0, 'q_equals_t': 0, 'q_even': 0,
              'B_matching_has_same_parity_edge': 0}
    for c in data['cases']:
        assert c['status'] == 'FOUND'
        ma_set, mb_set = set(range(0, 64, 2)), set(range(1, 64, 2))
        holes = set(c.get('holes', [0, 3, 13, 49]))
        m = matching(c['matching'], range(64), holes)
        assert all((a ^ b).bit_count() == 1 for a, b in m)
        assert c['v'] & 1 and c['v'].bit_count() % 2 == 1
        assert c['v'] not in holes
        if c.get('branch') == 'D5':
            cross = {e for e in m if e[0] ^ e[1] == 1}
            assert len(cross) == 1
            extension(c['path'], set(range(64)), m, 0, c['v'])
            assert sum((a ^ b) == 1 for a, b in zip(c['path'], c['path'][1:])) == 1
            counts['single_cross'] += 1
            counts['verified'] += 1
            continue
        pa = matching(c['P_A'], ma_set, set())
        extension(c['K_A'], ma_set, pa, 2, c['t'] ^ 1)
        d = {tuple(sorted(e)) for e in c['D']}
        ma = {e for e in m if set(e) <= ma_set}
        assert pa == ma | d and not ma & d
        cross = {e for e in m if e[0] ^ e[1] == 1}
        xa = {a for e in cross for a in e if a in ma_set}
        assert matching(c['D'], xa | {0}, set()) == d
        assert all(a.bit_count() % 2 != b.bit_count() % 2 for a, b in pa)
        segments = c['transferred_paths']
        covered_a, all_segment_edges = [], set()
        for p in segments:
            assert len(p) == len(set(p))
            assert all(q in ma_set for q in p[1:-1])
            covered_a += [q for q in p if q in ma_set]
            all_segment_edges |= edges(p)
        assert sorted(covered_a) == sorted(ma_set)
        assert all_segment_edges == ((edges(c['K_A']) - d) | cross |
                                     {(2, 3), tuple(sorted((c['t'] ^ 1, c['t'])))})
        prefix = c['prefix']
        assert prefix[0] == 0 and prefix[-1] == c['q']
        assert prefix in segments or prefix[::-1] in segments
        assert c['q'] == c['t'] or c['q'].bit_count() % 2 == 0
        rp = {tuple(sorted((p[0], p[-1]))): p for p in segments
              if 0 not in (p[0], p[-1])}
        lb = matching(c['L_B'], mb_set, {c['q'], c['w']})
        mb = {e for e in m if set(e) <= mb_set}
        assert lb == mb | set(rp) and not mb & set(rp)
        extension(c['K_B'], mb_set, lb, c['q'], c['v'])
        rebuilt = list(prefix)
        for a, b in zip(c['K_B'], c['K_B'][1:]):
            p = rp.get(tuple(sorted((a, b))), [a, b])
            if p[0] != a:
                p = p[::-1]
            assert p[-1] == b
            rebuilt += p[1:]
        assert rebuilt == c['path']
        extension(rebuilt, set(range(64)), m, 0, c['v'])
        counts['verified'] += 1
        counts['q_equals_t'] += c['q'] == c['t']
        counts['q_even'] += c['q'].bit_count() % 2 == 0
        counts['B_matching_has_same_parity_edge'] += any(
            a.bit_count() % 2 == b.bit_count() % 2 for a, b in lb)
    result = dict(status='PASS', scope=data['scope'], **counts,
                  input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  full_p6_proved=False, exhaustive_q6=False)
    (ROOT / source.name.replace('_results.json', '_verification.json')).write_text(
        json.dumps(result, indent=2), encoding='utf8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
