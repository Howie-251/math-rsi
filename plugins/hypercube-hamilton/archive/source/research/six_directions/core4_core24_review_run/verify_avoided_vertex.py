"""Independent stdlib checks of N11/Z9/Z10 certificates, including long cross edges."""
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def edge(a, b):
    return tuple(sorted((a, b)))


def edge_set(raw):
    return {edge(a, b) for a, b in raw}


def path_edges(p):
    return {edge(a, b) for a, b in zip(p, p[1:])}


def check_matching(raw, vertices, holes):
    es = edge_set(raw)
    assert len(es) == len(raw)
    used = [q for e in es for q in e]
    assert len(used) == len(set(used))
    assert set(used) == set(vertices) - set(holes)
    return es


def check_extension(p, vertices, required, start=None, end=None, cycle=False):
    assert len(p) == len(vertices) and set(p) == set(vertices)
    if cycle:
        es = path_edges(p + p[:1])
    else:
        assert p[0] == start and p[-1] == end
        es = path_edges(p)
    assert required <= es
    assert all((a ^ b).bit_count() == 1 for a, b in es - required)
    return es


def symmetry(q):
    q ^= 3
    return (q & ~3) | ((q & 1) << 1) | ((q & 2) >> 1)


def main():
    source = ROOT / 'avoided_vertex_results.json'
    data = json.loads(source.read_text(encoding='utf8'))
    A, B = set(range(0, 64, 2)), set(range(1, 64, 2))
    counts = Counter()
    for c in data['cases']:
        assert c['status'] == 'FOUND'
        v, h, a, b, k = (c[key] for key in ('v', 'h', 'a', 'b', 'k'))
        m = check_matching(c['matching'], range(64), {0, 3, 13, 49})
        assert all((p ^ q).bit_count() == 1 for p, q in m)
        assert edge(v, h) in m and v in A and v.bit_count() % 2 == 1
        star = check_matching(c['M_star'], range(64), {v, 3, 13, 49})
        assert star == (m - {edge(v, h)}) | {edge(0, h)}
        ma = {e for e in star if set(e) <= A}
        mb = {e for e in star if set(e) <= B}
        cross = star - ma - mb
        assert edge_set(c['cross_star']) == cross
        xa = {q for e in cross for q in e if q in A}
        xb = {q for e in cross for q in e if q in B}
        assert len(xa) % 2 == 1 and b not in xa and edge(b, k) in ma
        d = check_matching(c['D'], xa, {a})
        la = ma | d
        tb = check_matching(c['T_b'], A, {v, b})
        assert tb == (la - {edge(b, k)}) | {edge(a, k)}
        for j in range(1, 6):
            for parity in (0, 1):
                half = {edge(q, q ^ (1 << j)) for q in A if not q & (1 << j)
                        and (q & ~(1 << j)).bit_count() % 2 == parity}
                assert not half <= tb
        ce = check_extension(c['C_A0'], A - {v, b}, tb, cycle=True)
        ke = check_extension(c['K_A'], A - {v}, la, a, b)
        assert ke == (ce - {edge(a, k)}) | {edge(b, k)}
        segments = c['transferred_paths']
        all_a, se, endpoint_list = [], set(), []
        for p in segments:
            assert len(p) == len(set(p)) and p[0] in B and p[-1] in B
            assert all(q in A - {v} for q in p[1:-1])
            all_a += p[1:-1]
            endpoint_list += [p[0], p[-1]]
            se |= path_edges(p)
        assert sorted(all_a) == sorted(A - {v})
        assert len(endpoint_list) == len(set(endpoint_list))
        w = b ^ 1
        t = next(q for q in (13, 49) if q != w)
        assert set(endpoint_list) == xb | {w}
        assert se == (ke - d) | cross | {edge(b, w)}
        rp = {edge(p[0], p[-1]): p for p in segments}
        lb = check_matching(c['L_B'], B, {3, t})
        assert not mb & set(rp) and lb == mb | set(rp)
        check_extension(c['C_B'], B, lb, cycle=True)
        expanded = [c['C_B'][0]]
        for x, y in zip(c['C_B'], c['C_B'][1:] + c['C_B'][:1]):
            p = rp.get(edge(x, y), [x, y])
            if p[0] != x:
                p = p[::-1]
            assert p[-1] == y
            expanded += p[1:]
        assert expanded[-1] == expanded[0]
        assert expanded[:-1] == c['C_global']
        ge = check_extension(c['C_global'], set(range(64)) - {v}, star, cycle=True)
        final = check_extension(c['path'], set(range(64)), m, 0, v)
        assert final == (ge - {edge(0, h)}) | {edge(h, v)}
        transformed_m = {edge(symmetry(x), symmetry(y)) for x, y in m}
        transformed_path = [symmetry(q) for q in c['path']]
        assert {symmetry(q) for q in (0, 3, 13, 49)} == {0, 3, 13, 49}
        check_extension(transformed_path, set(range(64)), transformed_m, 3, symmetry(v))
        counts[c['branch']] += 1
        counts['target_partner_equals_bridge'] += h == b
    result = dict(status='PASS', scope=data['scope'], verified=len(data['cases']),
                  root3_symmetry_checks=len(data['cases']), branches=dict(counts),
                  input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  full_p6_proved=False, exhaustive_q6=False)
    (ROOT/'avoided_vertex_verification.json').write_text(json.dumps(result, indent=2), encoding='utf8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
