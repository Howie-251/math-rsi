"""Independent stdlib checks of new geometry witnesses and a rotation stall.

No solver/search modules are imported. These are finite explicit instances;
they do not prove the conditional S7 theorem, A4, or full P6.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def edges(seq, cycle=False):
    pairs = list(zip(seq, seq[1:]))
    if cycle:
        pairs.append((seq[-1], seq[0]))
    return {tuple(sorted(e)) for e in pairs}


def matching(raw):
    f = {tuple(sorted(e)) for e in raw}
    assert len(f) == len(raw) and len({x for e in f for x in e}) == 2*len(f)
    return f


def main():
    names = ['six_hole_geometry_witnesses.json', 'a4_endpoint_rotation_probe.json',
             'a4_edge_elimination_probe.json']
    raw = {name: (ROOT/name).read_bytes() for name in names}
    hashes = {name: hashlib.sha256(data).hexdigest() for name, data in raw.items()}
    six = json.loads(raw[names[0]])['cases']
    assert len(six) == 6
    for c in six:
        f = matching(c['matching'])
        assert len(f) == 29 and all((x ^ y).bit_count() == 1 for x, y in f)
        assert len({x ^ y for x, y in f}) == 6
        holes = set(range(64)) - {x for e in f for x in e}
        assert holes == set(c['holes']) and c['u'] in holes and c['v'] not in holes
        assert c['u'].bit_count() % 2 == 0 and c['v'].bit_count() % 2 == 1
        star_holes = holes - {c['u']} | {c['v']}
        for i in range(6):
            face_holes = [x for x in star_holes if (x >> i) & 1 == (c['v'] >> i) & 1]
            counts = (sum(x.bit_count() % 2 == 0 for x in face_holes),
                      sum(x.bit_count() % 2 == 1 for x in face_holes))
            assert counts not in {(1, 2), (1, 3), (0, 3), (1, 1)}
        p = c['path']
        assert c['status'] == 'FOUND'
        assert len(p) == 64 and set(p) == set(range(64))
        assert (p[0], p[-1]) == (c['u'], c['v'])
        assert f <= edges(p) and all((x ^ y).bit_count() == 1 for x, y in edges(p))
    stall = json.loads(raw[names[1]])['cases'][-1]
    original = json.loads(raw[names[2]])['cases'][stall['source_index']]
    f = matching(stall['matching'])
    assert f == matching(original['matching'])
    p, v = stall['initial_path'], stall['v']
    assert len(p) == 31 and set(p) == set(range(32)) - {v}
    assert f <= edges(p) and all((x ^ y).bit_count() == 1 for x, y in edges(p) - f)
    assert (p[0] ^ p[-1]).bit_count() == 3
    blockers = []
    for oriented in (p, p[::-1]):
        a = oriented[0]
        records = []
        for i in range(5):
            y = a ^ (1 << i)
            if y == v:
                records.append(dict(neighbor=y, reason='forbidden_vertex'))
                continue
            pos = oriented.index(y)
            assert pos != len(p)-1
            if pos == 1:
                records.append(dict(neighbor=y, reason='identity_move'))
                continue
            cut = tuple(sorted((oriented[pos-1], y)))
            assert cut in f
            records.append(dict(neighbor=y, reason='would_delete_required_edge', edge=cut))
        blockers.append(dict(endpoint=a, neighbors=records))
    c = original['eliminate3']['cycle']
    assert len(c) == 31 and set(c) == set(p)
    ce = edges(c, cycle=True)
    assert f <= ce and all((x ^ y).bit_count() == 1 for x, y in ce - f)
    out = dict(status='PASS', scope='six explicit Q6 paths and one exact endpoint-rotation stall with a valid A4 cycle',
               input_hashes=hashes, six_exceptional_rows_realized=6, six_paths_verified=6,
               rotation_stall=blockers, rotation_stall_is_a4_counterexample=False,
               a4_proved=False, full_p6_proved=False)
    (ROOT/'six_geometry_and_rotation_verification.json').write_text(json.dumps(out, indent=2), encoding='utf8')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
