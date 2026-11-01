"""Three P4 trace multiset orbits under the unique internal five-edge stabilizer."""
from itertools import permutations,combinations_with_replacement
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent
start=time.process_time()
quad=[x for x in range(128) if x.bit_count()==4];rank={q:i for i,q in enumerate(quad)}
group=[tuple(a)+tuple(b) for a in permutations(range(5)) for b in permutations((5,6))]
assert len(group)==len(set(group))==240
def move(mask,p):return sum(1<<p[i] for i in range(7) if mask&(1<<i))
actions=[[rank[move(q,p)] for q in quad] for p in group]
allkeys=list(combinations_with_replacement(range(35),3));assert len(allkeys)==7770
seen=set();jobs=[];images=[]
for key in allkeys:
    if key in seen:continue
    orbit={tuple(sorted(action[i] for i in key)) for action in actions}
    rep=min(orbit);assert rep==key
    job=len(jobs);jobs.append(dict(job=job,quad_masks=[quad[i] for i in rep],orbit_size=len(orbit)))
    transports={}
    for index,action in enumerate(actions):
        im=tuple(sorted(action[i] for i in rep));transports.setdefault(im,index)
    assert set(transports)==orbit and not seen&orbit
    for im in sorted(orbit):images.append(dict(quad_masks=[quad[i] for i in im],job=job,transport_index=transports[im]))
    seen|=orbit
assert seen==set(allkeys) and len(images)==7770
result=dict(scope=__doc__,internal_mask=31,group=[list(p) for p in group],jobs=jobs,
            all_7770_images=images,raw_quad_multisets=7770,orbit_count=len(jobs),cpu_seconds=time.process_time()-start)
(HERE/'QUAD_ORBITS.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
(HERE/'JOBS.tsv').write_text(''.join(' '.join(map(str,[r['job']]+r['quad_masks']))+'\n' for r in jobs))
print('quad raw',7770,'orbits',len(jobs),'group',240,'cpu',result['cpu_seconds'])
