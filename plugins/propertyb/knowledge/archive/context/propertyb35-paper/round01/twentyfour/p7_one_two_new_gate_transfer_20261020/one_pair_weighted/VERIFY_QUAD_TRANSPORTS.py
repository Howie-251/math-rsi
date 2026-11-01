from itertools import permutations,product,combinations_with_replacement
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent;d=json.loads((HERE/'QUAD_ORBITS.json').read_text())
def move(mask,p):return sum(1<<p[i] for i in range(7) if mask&(1<<i))
groups=[]
groups.append({tuple(a)+tuple(b) for a in permutations(range(5)) for b in permutations((5,6))})
g=set()
for leaves in permutations((0,2)):
    for common in permutations((3,4,5,6)):
        p=list(range(7))
        for x,y in zip((0,2),leaves):p[x]=y
        for x,y in zip((3,4,5,6),common):p[x]=y
        g.add(tuple(p))
groups.append(g);g=set()
for blocks in permutations(((0,1),(2,3))):
    for s0,s1 in product((False,True),repeat=2):
        for common in permutations((4,5,6)):
            p=list(range(7))
            for src,tgt,swap in zip(((0,1),(2,3)),blocks,(s0,s1)):
                for x,y in zip(src,tgt[::-1] if swap else tgt):p[x]=y
            for x,y in zip((4,5,6),common):p[x]=y
            g.add(tuple(p))
groups.append(g)
quad=[x for x in range(128) if x.bit_count()==4];checked=0;alljobs=[]
for cas,(entry,group) in enumerate(zip(d['cases'],groups)):
    assert len(group)==(240 if cas==0 else 48) and group==set(map(tuple,entry['group']))
    assert all(sorted(move(T,p) for T in entry['internal_masks'])==sorted(entry['internal_masks']) for p in group)
    raw=set(combinations_with_replacement(quad,entry['nquad']))
    assert len(raw)==(73815 if cas==0 else 630)
    jobs={r['job']:r for r in entry['jobs']};assert len(jobs)==(615 if cas==0 else (46 if cas==1 else 41))
    actual={};byjob={j:set() for j in jobs}
    for row in entry['all_quad_images']:
        key=tuple(row['quad_masks']);assert key not in actual
        p=tuple(entry['group'][row['transport_index']]);assert p in group
        rep=jobs[row['job']]['quad_masks'];assert tuple(sorted(move(q,p) for q in rep))==key
        actual[key]=row['job'];byjob[row['job']].add(key);checked+=1
    assert set(actual)==raw
    for job,r in jobs.items():
        rep=tuple(r['quad_masks']);orbit={tuple(sorted(move(q,p) for q in rep)) for p in group}
        assert min(orbit)==rep and len(orbit)==r['orbit_size'] and orbit==byjob[job]
        alljobs.append(r)
assert len(alljobs)==702 and alljobs==d['jobs'] and [r['job'] for r in alljobs]==list(range(702))
assert checked==75075
result=dict(PASS=True,group_orders=[240,48,48],quad_orbit_counts=[615,46,41],
            all_quad_multiset_image_keys_and_actual_transports_checked=checked,all702_job_keys_checked=True)
(HERE/'QUAD_TRANSPORT_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS 240/48/48 factor groups, all702 jobs, all75075 keys and actual transports')
