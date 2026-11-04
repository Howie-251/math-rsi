"""Independent certificate audit; no imports from producers or their checkers.

Coverage uses independently generated sets of unordered pair partitions, not ranks.
Only writes A6_FINITE_INPUTS_REVIEW.json. Run with normal Python (assert enabled).
"""
from pathlib import Path
from itertools import permutations, combinations
from collections import Counter
import hashlib
import json

ROOT = Path(__file__).resolve().parent
V = frozenset(range(16))
parity = lambda v: v.bit_count() % 2
short = lambda x, y: (x ^ y).bit_count() == 1


def partitions(vertices):
    """All partitions into unordered pairs, by an independent recursive definition."""
    if not vertices:
        yield ()
        return
    a, *tail = vertices
    for i, b in enumerate(tail):
        for suffix in partitions(tuple(tail[:i] + tail[i+1:])):
            yield (16*a+b,) + suffix


def matching_key(m, holes):
    assert len(m) == 16
    assert frozenset(x for x, y in enumerate(m) if y == 255) == holes
    pairs = []
    for x in sorted(V-holes):
        y = m[x]
        assert y in V-holes and y != x and m[y] == x
        if x < y:
            pairs.append(16*x+y)
    return tuple(pairs)


def edges(seq, closed=False):
    pairs = list(zip(seq, seq[1:]))
    if closed:
        pairs.append((seq[-1], seq[0]))
    result = frozenset(16*min(a,b)+max(a,b) for a,b in pairs)
    assert len(result) == len(pairs)
    return result


def new_edges(seq, required, vertices, closed=False):
    assert len(seq) == len(vertices) and frozenset(seq) == vertices
    ee = edges(seq, closed)
    assert required <= ee
    extra = ee-required
    assert all(short(e//16,e%16) for e in extra)
    return extra


def audit_file(name, holes, avoid, threshold=None, root=None, excluded_end=None):
    holes = frozenset(holes)
    expected = set(partitions(tuple(sorted(V-holes))))
    total = len(expected)
    assert total == (10395 if len(holes)==4 else 135135)
    seen = set()
    data = (ROOT/name).read_bytes()
    vertices = V-({avoid} if avoid is not None else set())
    size = len(vertices)
    pos = nc = 0
    minimum = 33
    while pos < len(data):
        assert pos+16 <= len(data)
        m = data[pos:pos+16]
        pos += 16
        key = matching_key(m, holes)
        assert key in expected and key not in seen
        seen.add(key)
        required = frozenset(key)
        if threshold is None:
            seq = data[pos:pos+size]
            pos += size
            new_edges(seq, required, vertices)
            assert seq[0] == root and parity(seq[-1]) == parity(root)
            assert seq[-1] != excluded_end
            nc += 1
        else:
            assert pos < len(data)
            count = data[pos]
            pos += 1
            assert count and pos+count*size <= len(data)
            union = set()
            for _ in range(count):
                seq = data[pos:pos+size]
                pos += size
                union.update(new_edges(seq, required, vertices, True))
                nc += 1
            minimum = min(minimum,len(union))
            assert len(union) >= threshold
    assert pos == len(data) and seen == expected
    return dict(file=name,matchings=len(seen),witnesses=nc,
                certified_union_minimum=None if threshold is None else minimum,
                sha256=hashlib.sha256(data).hexdigest())


def geometry():
    # Explicitly build all 2^4 * 4! cube automorphisms.
    maps=[]
    for p in permutations(range(4)):
        base=[sum(((x>>i)&1)<<p[i] for i in range(4)) for x in range(16)]
        for shift in range(16):
            maps.append(tuple(y^shift for y in base))
    assert len(set(maps)) == 384
    assert all(all(short(t[x],t[y]) == short(x,y) for x in V for y in V) for t in maps)
    fixing=[t for t in maps if t[0]==0]
    path_orbits=Counter()
    for b in V-{0}:
        if parity(b): continue
        for z in V:
            if not parity(z) or short(b,z): continue
            for d in V-{z}:
                if parity(d):
                    path_orbits[min((t[b],t[z],t[d]) for t in fixing)]+=1
    config=[tuple(map(int,l.split())) for l in (ROOT/'q4_balanced_avoid_path_configs.txt').read_text().splitlines() if l.strip()]
    supplied=json.loads((ROOT/'q4_balanced_avoid_path_orbits.json').read_text())
    listed={(r['b'],r['z'],r['root']):r['multiplicity'] for r in supplied['orbits']}
    assert len(config)==len(set(config))==13 and set(config)==set(path_orbits)
    assert listed==dict(path_orbits) and supplied['configurations']==sum(path_orbits.values())==196
    # Build residual configuration orbit membership directly from each representative.
    ao={}
    for h in (1,4,13):
        orbit={(tuple(sorted(t[x] for x in (0,7,11,h))),t[h]) for t in maps}
        assert not set(ao)&orbit
        ao.update({key:h for key in orbit})
    bo={tuple(sorted(t[x] for x in (0,3,13,14))) for t in maps}
    ac=Counter(); bc=Counter(); residual_a=Counter()
    for holes in combinations(range(16),4):
        hh=set(holes)
        colors=Counter(parity(x) for x in holes)
        if sorted(colors.values())==[1,3]:
            majority=next(p for p,n in colors.items() if n==3)
            for avoided in holes:
                if parity(avoided)!=majority: continue
                useful=[(a,b) for a,b in combinations(hh-{avoided},2) if short(a,b)]
                if useful:
                    # Adding this short edge leaves two same-parity holes;
                    # old A spectrum avoids exactly the designated majority hole.
                    a,b=useful[0]
                    remaining=hh-{a,b}
                    assert avoided in remaining and len({parity(x) for x in remaining})==1
                    assert (next(iter(remaining))^next(iter(remaining-{next(iter(remaining))}))).bit_count() in (2,4)
                    ac['adjacent_reduction']+=1
                else:
                    assert (holes,avoided) in ao
                    residual_a[str(ao[holes,avoided])]+=1
                    ac['residual']+=1
        elif colors==Counter({0:2,1:2}):
            useful=[(a,b) for a,b in combinations(holes,2) if short(a,b)]
            if useful:
                a,b=useful[0]
                remaining=hh-{a,b}
                assert len({parity(x) for x in remaining})==2
                bc['adjacent_reduction']+=1
            else:
                assert holes in bo
                bc['residual']+=1
    assert sum(ac.values())==2688 and sum(bc.values())==784
    assert ac['residual']==len(ao) and bc['residual']==len(bo)
    return sorted(path_orbits),dict(automorphisms=384,path_normalized_configurations=196,
        path_orbit_sizes={','.join(map(str,k)):v for k,v in sorted(path_orbits.items())},
        marked_unbalanced=dict(ac),unbalanced_residual_by_rep=dict(residual_a),
        balanced=dict(bc))


def main():
    configs,geo=geometry()
    files=[]
    for b,z,d in configs:
        files.append(audit_file(f'q4_balanced_avoid_path_{b}_{z}_{d}.bin',
                               (0,b,z,d),0,root=d,excluded_end=z))
    for h in (1,4,13):
        files.append(audit_file(f'q4_four_spectrum_A_{h}.bin',(0,7,11,h),h,15))
    files.append(audit_file('q4_four_spectrum_balanced.bin',(0,3,13,14),None,18))
    for mode,choices in [('A',(3,15)),('B',(1,7))]:
        for s in choices:
            files.append(audit_file(f'q4_spectrum_{mode}_{s}.bin',(0,s),
                                   0 if mode=='A' else None,15 if mode=='A' else 18))
    sources=['q4_balanced_avoid_path.cpp','q4_balanced_avoid_path_configs.txt',
             'q4_balanced_avoid_path_orbits.json','verify_q4_balanced_avoid_path.py',
             'q4_four_hole_spectrum.cpp','verify_q4_four_hole_spectrum.py',
             'verify_q4_spectrum_certificates.py',Path(__file__).name]
    result=dict(status='PASS',review_independence='same-family',acceptance_status='provisional',
                scope='Two Q4 finite inputs and old two-hole spectrum dependencies only',
                geometry=geo,files=files,total_matchings=sum(f['matchings'] for f in files),
                total_witnesses=sum(f['witnesses'] for f in files),
                source_sha256={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in sources},
                a6_proved=False,p6_proved=False)
    (ROOT/'A6_FINITE_INPUTS_REVIEW.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['status','total_matchings','total_witnesses','geometry']}))


if __name__=='__main__':
    main()
