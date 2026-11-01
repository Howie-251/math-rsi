"""Independent 48-element groups from structural factors, rather than S7 filtering."""
from itertools import permutations,product
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
d=json.loads((HERE/'QUAD_ORBITS.json').read_text())
def image(mask,p):return sum(1<<p[i] for i in range(7) if mask&(1<<i))
groups=[]
g=[]
for leaves in permutations((0,2)):
    for common in permutations((3,4,5,6)):
        p=[None]*7;p[1]=1
        for a,b in zip((0,2),leaves):p[a]=b
        for a,b in zip((3,4,5,6),common):p[a]=b
        g.append(tuple(p))
groups.append(set(g));g=[]
for blocks in permutations(((0,1),(2,3))):
    for swap0,swap1 in product((False,True),repeat=2):
        for common in permutations((4,5,6)):
            p=[None]*7
            for source,target,swap in zip(((0,1),(2,3)),blocks,(swap0,swap1)):
                for a,b in zip(source,target[::-1] if swap else target):p[a]=b
            for a,b in zip((4,5,6),common):p[a]=b
            g.append(tuple(p))
groups.append(set(g))
allquad={m for m in range(128) if m.bit_count()==4};checked=0
for shape,(entry,group) in enumerate(zip(d['shapes'],groups)):
    assert len(group)==48 and group==set(map(tuple,entry['automorphisms']))
    missing=tuple(entry['missing'])
    assert all(sorted(image(f,p) for f in missing)==sorted(missing) for p in group)
    expected={}
    for q in allquad:
        rep=min(image(q,p) for p in group)
        expected[q]=rep
    assert len(set(expected.values()))==(6 if shape==0 else 5)
    actual=entry['all_quad_images']
    assert len(actual)==35 and {x['quad']:x['representative'] for x in actual}==expected
    for row in actual:
        p=tuple(row['transport']);assert p in group
        assert image(row['representative'],p)==row['quad']
        checked+=1
    assert {r['representative']:set(r['images']) for r in entry['orbits']}=={
        rep:{q for q in allquad if expected[q]==rep} for rep in set(expected.values())}
assert checked==70
result=dict(PASS=True,group_orders=[48,48],quad_orbits=[6,5],full_quad_image_and_transport_keys_checked=70)
(HERE/'QUAD_TRANSPORT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS independent factor groups; all70 image keys, orbit sets and actual transports')
