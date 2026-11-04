"""Reconstruct remaining Q6 geometry choices directly from raw records.

Uses no saved core-map JSON. This is geometry bookkeeping; the arbitrary
matching theorem is separately supplied by T15_BALANCED_BRIDGE_REVIEW.
"""
import itertools,json,collections,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
NEW={2,7,10,44};OLD={13,14,19,31,32,35,37,38}
def main():
    reps=json.loads((R/'t15_analytic_geometry.json').read_text())['T15']['residual_orbits']
    lookup={}
    for perm in itertools.permutations(range(5)):
        tr=[sum(((x>>j)&1)<<perm[j] for j in range(5)) for x in range(32)]
        for i,r in enumerate(reps):
            key=tuple(sorted(tr[v] for v in r['avoided'])),tuple(sorted(tr[v] for v in r['included']))
            assert key not in lookup or lookup[key]==i;lookup[key]=i
    remaining=[];newcount=collections.Counter();oldcount=collections.Counter();cuts=0;inputs={}
    for v in (1,7,31):
        filename=f'remaining_eight_after_single_face_{v}.bin';raw=(R/filename).read_bytes();inputs[filename]=hashlib.sha256(raw).hexdigest()
        assert len(raw)%7==0;seen=set();after=[]
        for i in range(0,len(raw),7):
            rec=raw[i:i+7];assert rec not in seen;seen.add(rec);Z=list(rec[:3]);W=list(rec[3:]);choices=set()
            assert Z==sorted(Z) and W==sorted(W) and len(set(Z+W))==7
            for j in range(6):
                za=[z for z in Z if (z>>j&1)==(v>>j&1)];wa=[w for w in W if (w>>j&1)==(v>>j&1)]
                if len(za)!=2 or len(wa)!=1:continue
                cuts+=1;q=next(z for z in Z if z not in za)
                def project(x):
                    x^=q;return (x&((1<<j)-1))|((x>>(j+1))<<j)
                key=tuple(sorted(project(z^(1<<j)) for z in za)),tuple(sorted(project(w) for w in W if w not in wa))
                assert key in lookup;choices.add(lookup[key])
            assert not choices&OLD
            oldcount[v]+=1
            if choices&NEW:newcount[v]+=1
            else:
                after.append(rec);remaining.append(dict(target=v,Z=Z,W=W,core_choices=sorted(choices)))
        (R/f'remaining_eight_after_balanced_bridge_{v}.bin').write_bytes(b''.join(after))
    patterns={tuple(r['core_choices']) for r in remaining if r['core_choices']}
    forced={p[0] for p in patterns if len(p)==1}
    residual={p for p in patterns if not forced&set(p)}
    assert forced=={0,1,4,5,8,15,23,24,27}
    assert residual=={(18,26),(21,26),(25,26)}
    selected=forced|{26};assert all(set(p)&selected for p in patterns)
    without=[r for r in remaining if not r['core_choices']]
    out=dict(status='PASS_RAW_COORDINATE_RECONSTRUCTION',source_hashes=inputs,
        previous_remaining=sum(oldcount.values()),newly_covered=sum(newcount.values()),
        newly_by_target=dict(newcount),remaining=len(remaining),
        remaining_by_target=dict(collections.Counter(r['target'] for r in remaining)),
        remaining_with_a2b1=len(remaining)-len(without),remaining_without_a2b1=len(without),
        coordinate_projections=cuts,proved_T15_core_orbits=sorted(NEW|OLD),
        additional_sufficient_cores=sorted(selected),minimum_additional_whole_orbit_cover=10,
        lower_bound='9 forced singleton cores plus one disjoint nonempty group {18,21,25,26}',
        remaining_choice_patterns=[list(p) for p in sorted(patterns)],
        full_eight_hole_proved=False,full_p6_proved=False,
        scope='Marked normalized hole configurations, not matching counts or realizability certificates')
    (R/'eight_after_balanced_bridge_check.json').write_text(json.dumps(out,indent=2)+'\n')
    (R/'eight_after_balanced_bridge_candidates.json').write_text(json.dumps({**out,'rows':remaining})+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
