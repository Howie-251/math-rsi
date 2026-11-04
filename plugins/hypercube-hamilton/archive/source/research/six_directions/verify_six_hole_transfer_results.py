"""Independent stdlib verification of saved S9 / free-six transfer witnesses."""
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def edges(p, cycle=False):
    pairs = list(zip(p, p[1:]))
    if cycle:
        pairs.append((p[-1], p[0]))
    return {tuple(sorted(e)) for e in pairs}


def matching(raw):
    f = {tuple(sorted(e)) for e in raw}
    assert len(f) == len(raw) and len({x for e in f for x in e}) == 2*len(f)
    return f


def sequence(p, vs, required, cycle=False):
    assert len(p) == len(vs) and set(p) == vs
    es = edges(p, cycle)
    assert required <= es
    assert all((x ^ y).bit_count() == 1 or (x, y) in required for x, y in es)
    return es


def check(c, free_target):
    assert c['status'] == 'FOUND'
    m = matching(c['matching'])
    u, v, i = c['u'], c['v'], c['cut']
    assert len(m) == 29 and all((x ^ y).bit_count() == 1 for x, y in m)
    holes = set(range(64)) - {x for e in m for x in e}
    assert holes == set(c['holes']) and u in holes
    assert (v in holes) == free_target
    assert u.bit_count() % 2 == 0 and v.bit_count() % 2 == 1
    aa = {x for x in range(64) if ((x ^ v) >> i) & 1 == 0}
    bb = set(range(64)) - aa
    ma = {e for e in m if set(e) <= aa}
    mb = {e for e in m if set(e) <= bb}
    cross = m - ma - mb
    xa = {x for e in cross for x in e if x in aa}
    xb = {x for e in cross for x in e if x in bb}
    assert (u in aa) == (c['root_side'] == 'A')
    odd_holes = {x for x in holes if x.bit_count() % 2}
    other_even = holes - odd_holes - {u}
    assert len(other_even & aa) == len(other_even & bb) == 1
    if free_target:
        assert len((odd_holes - {v}) & aa) == c['shape']
    else:
        assert odd_holes <= aa
        assert c['target_is_cross_port'] == (v in xa)
    d = matching(c['D'])
    la = matching(sorted(ma | d))
    assert len(la) == len(ma) + len(d)
    kae = sequence(c['K_A'], aa, la)
    assert c['K_A'][-1] == v
    if u in aa:
        assert c['K_A'][0] == u and d
    else:
        assert c['K_A'][0] in xa and c['K_A'][0].bit_count() % 2 == 0
    bridge_a = c.get('bridge_a', c.get('w'))
    y = c['y']
    bridge = set()
    if y is not None:
        assert bridge_a in holes and bridge_a in aa and y == bridge_a ^ (1 << i)
        assert y in {x for e in mb for x in e}
        bridge.add(tuple(sorted((bridge_a, y))))
    forest = (kae - d) | cross | bridge
    segments = c['transferred_paths']
    occurrences = Counter(x for p in segments for x in p)
    assert set(occurrences) == aa | xb | ({y} if y is not None else set())
    assert all(n == 1 for n in occurrences.values())
    assert all(len(p) >= 2 for p in segments)
    actual_forest = set().union(*(edges(p) for p in segments))
    assert actual_forest == forest
    assert all((x ^ z).bit_count() == 1 for x, z in forest)
    tv = c['T_v']
    assert tv[-1] == v and any(tv == p or tv == p[::-1] for p in segments)
    tu = c['T_u']
    if u in aa:
        assert tu[0] == u and any(tu == p or tu == p[::-1] for p in segments)
        assert set(tu).isdisjoint(tv)
    else:
        assert tu is None
    middle = [p for p in segments if v not in (p[0], p[-1])
              and (u in bb or u not in (p[0], p[-1]))]
    rr = matching(c['R'])
    assert rr == {tuple(sorted((p[0], p[-1]))) for p in middle}
    start_b, end_b = (u if u in bb else tu[-1]), tv[0]
    lb = matching(c['L_B'])
    if 'C_B' in c:
        required = matching(c['T_B']) if 'T_B' in c else lb
        cvs = bb - {y} if y is not None else bb
        sequence(c['C_B'], cvs, required, cycle=True)
    aux = tuple(c['auxiliary_edge']) if 'auxiliary_edge' in c else None
    kb_required = lb - ({aux} if aux is not None else set())
    kb_vs = bb - {y} if aux is not None and y is not None else bb
    sequence(c['K_B'], kb_vs, kb_required)
    assert (c['K_B'][0], c['K_B'][-1]) == (start_b, end_b)
    if aux is not None:
        assert aux == tuple(sorted((start_b, end_b))) and aux not in edges(c['K_B'])
    full = c['path']
    sequence(full, set(range(64)), m)
    assert (full[0], full[-1]) == (u, v)


def main():
    files = [('six_hole_clustered_results.json', False), ('six_hole_free_transfer_results.json', True)]
    counts, modes, hashes = Counter(), Counter(), {}
    for name, free_target in files:
        raw = (ROOT/name).read_bytes()
        hashes[name] = hashlib.sha256(raw).hexdigest()
        cases = json.loads(raw)['cases']
        for c in cases:
            check(c, free_target)
            counts['free' if free_target else 'covered'] += 1
            modes[c['root_side'] + ':' + c['mode']] += 1
    out = dict(status='PASS', input_hashes=hashes, verified_by_target=dict(counts),
               modes=dict(modes), scope='explicit local and global path/forest/circle certificates only',
               a4_proved=False, full_p6_proved=False, exhaustive_matchings=False)
    (ROOT/'six_hole_transfer_verification.json').write_text(json.dumps(out, indent=2), encoding='utf8')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
