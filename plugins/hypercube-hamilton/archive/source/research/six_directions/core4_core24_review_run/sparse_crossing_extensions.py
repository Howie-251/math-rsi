"""S5/S6 constructions on the old residual sample list; not exhaustive Q6."""
import json
from collections import Counter
from pathlib import Path
from avoided_vertex_transfer import cycle_on
from single_bridge_probe import verify
from split_transfer import local_path
from unbalanced_transfer import edge, path_edges

R = Path(__file__).resolve().parent
V = set(range(64))


def eligible(raw):
    m = {edge(*p) for p in raw['matching']}
    u, v = raw['u'], raw['v']
    holes = V-{q for p in m for q in p}
    mate = {a: b for p in m for a, b in (p, p[::-1])}
    options = []
    for i in range(6):
        aa = {q for q in V if ((q ^ v) >> i) & 1 == 0}
        bb = V-aa
        cross = [p for p in m if len(set(p) & aa) == 1]
        if u in aa and len(cross) == 2:
            ports = [q for p in cross for q in p if q in aa]
            if (ports[0] ^ ports[1]).bit_count() == 1:
                options.append(('S6', i))
        if len(holes) == 6 and v in mate:
            h = mate[v]
            star = m-{edge(v, h)} | {edge(u, h)}
            cs = [p for p in star if len(set(p) & aa) == 1]
            ah = (holes-{u} | {v}) & aa
            shape = (sum(q.bit_count() % 2 == 0 for q in ah), sum(q.bit_count() % 2 == 1 for q in ah))
            if len(cs) == 1 and not {u, h} <= bb and shape in {(1, 2), (0, 3)}:
                options.append(('S5', i))
    return options


def construct(raw, mode, i):
    m = {edge(*p) for p in raw['matching']}
    u, v = raw['u'], raw['v']
    aa = {q for q in V if ((q ^ v) >> i) & 1 == 0}
    bb = V-aa
    side = (v >> i) & 1
    base = dict(mode=mode, cut=i, matching=sorted(m), u=u, v=v)
    if mode == 'S6':
        ma = {p for p in m if set(p) <= aa}
        mb = {p for p in m if set(p) <= bb}
        cross = m-ma-mb
        ports = sorted(q for p in cross for q in p if q in aa)
        a, c = ports
        b, d = a ^ (1 << i), c ^ (1 << i)
        ra = local_path(6, i, side, sorted(ma | {edge(a, c)}), u, v)
        rb = local_path(6, i, 1-side, sorted(mb), b, d)
        if ra['status'] != 'FOUND' or rb['status'] != 'FOUND':
            return dict(base, status='UNKNOWN', A=ra, B=rb)
        ka, kb = ra['path'], rb['path']
        segment = [a]+kb+[c]
        path = [ka[0]]
        for x, y in zip(ka, ka[1:]):
            p = segment if edge(x, y) == edge(a, c) else [x, y]
            if p[0] != x:
                p = p[::-1]
            path += p[1:]
        verify(6, sorted(m), u, v, path)
        return dict(base, status='FOUND', ports=ports, K_A=ka, K_B=kb, path=path)
    h = next(q for p in m if v in p for q in p if q != v)
    star = m-{edge(v, h)} | {edge(u, h)}
    ma = {p for p in star if set(p) <= aa}
    mb = {p for p in star if set(p) <= bb}
    cross = star-ma-mb
    assert len(cross) == 1 and all((x ^ y).bit_count() == 1 for x, y in mb)
    a = next(q for p in cross for q in p if q in aa)
    b = next(q for p in cross for q in p if q in bb)
    ah = aa-{q for p in star for q in p}
    even = sorted(q for q in ah if q.bit_count() % 2 == 0)
    if even:
        terminal = even[0]
    else:
        covered_b = {q for p in mb for q in p}
        terminal = next(q for q in ah-{v} if q ^ (1 << i) in covered_b)
    y = terminal ^ (1 << i)
    la = ma | {edge(a, terminal)}
    ra = cycle_on(aa-{v}, la)
    rb = local_path(6, i, 1-side, sorted(mb), b, y)
    if ra['status'] != 'FOUND' or rb['status'] != 'FOUND':
        return dict(base, status='UNKNOWN', A=ra, B=rb)
    ca, kb = ra['cycle'], rb['path']
    pos = ca.index(a)
    step = -1 if ca[(pos+1) % len(ca)] == terminal else 1
    assert ca[(pos-step) % len(ca)] == terminal
    ka = [ca[(pos+step*j) % len(ca)] for j in range(len(ca))]
    segment = [b]+ka+[y]
    cyc = kb+segment[-2:0:-1]
    assert len(cyc) == 63 and set(cyc) == V-{v}
    pos = cyc.index(u)
    step = -1 if cyc[(pos+1) % len(cyc)] == h else 1
    assert cyc[(pos-step) % len(cyc)] == h
    path = [cyc[(pos+step*j) % len(cyc)] for j in range(len(cyc))]+[v]
    verify(6, sorted(m), u, v, path)
    return dict(base, status='FOUND', h=h, M_star=sorted(star), a=a, b=b,
                terminal=terminal, y=y, L_A=sorted(la), C_A=ca,
                transferred_path=segment, K_B=kb, C_global=cyc, path=path)


def main():
    rows = json.loads((R/'remaining_samples_after_Z5.json').read_text(encoding='utf8'))['remaining']
    out, remaining = [], []
    for idx, raw in enumerate(rows):
        opts = eligible(raw)
        if not opts:
            remaining.append(raw)
            continue
        attempts = []
        for mode, cut in opts:
            c = construct(raw, mode, cut)
            attempts.append((mode, cut, c['status']))
            if c['status'] == 'FOUND':
                break
        out.append(dict(c, old_index=idx, attempts=attempts))
        (R/'sparse_crossing_results.json').write_text(json.dumps(dict(
            scope='Eligible old residual samples only; not exhaustive Q6', cases=out,
            full_p6_proved=False), indent=2), encoding='utf8')
        print(len(out), idx, c['mode'], c['status'], flush=True)
    (R/'remaining_samples_after_S5_S6.json').write_text(json.dumps(dict(
        scope='Old samples not classified by existing S5/S6 sufficient hypotheses',
        remaining=remaining, count=len(remaining), full_p6_proved=False), indent=2), encoding='utf8')
    print(dict(Counter(c['mode'] for c in out)), 'remaining', len(remaining))


if __name__ == '__main__':
    main()
