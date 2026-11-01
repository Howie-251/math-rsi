from itertools import permutations,combinations_with_replacement
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time()
quad=[x for x in range(128) if x.bit_count()==4];rank={q:i for i,q in enumerate(quad)}
def move(mask,p):return sum(1<<p[i] for i in range(7) if mask&(1<<i))
entries=[];jobs=[]
for case,internal in enumerate(([124,121],[124,115])):
    group=[p for p in permutations(range(7)) if sorted(move(T,p) for T in internal)==sorted(internal)]
    assert len(group)==48
    actions=[[rank[move(q,p)] for q in quad] for p in group]
    allkeys=list(combinations_with_replacement(range(35),3));seen=set();images=[];local=[]
    for key in allkeys:
        if key in seen:continue
        transforms={}
        for pi,act in enumerate(actions):transforms.setdefault(tuple(sorted(act[i] for i in key)),pi)
        orbit=set(transforms);assert min(orbit)==key and not seen&orbit
        job=len(jobs);r=dict(job=job,case=case,quad_masks=[quad[i] for i in key],orbit_size=len(orbit));jobs.append(r);local.append(r)
        for im in sorted(orbit):images.append(dict(quad_masks=[quad[i] for i in im],job=job,transport_index=transforms[im]))
        seen|=orbit
    assert len(seen)==len(images)==7770
    entries.append(dict(case=case,internal_masks=internal,group=[list(p) for p in group],raw_quad_multisets=7770,orbit_count=len(local),jobs=local,all_quad_images=images))
result=dict(scope='I2 zero pair n1=28 inventory(0,2,3), full triple-quad multiset orbits and transports',cases=entries,jobs=jobs,cpu_seconds=time.process_time()-start)
(HERE/'QUAD_ORBITS.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
(HERE/'JOBS.tsv').write_text(''.join(' '.join(map(str,[r['job'],r['case']]+r['quad_masks']))+'\n' for r in jobs))
print('orbits',[e['orbit_count'] for e in entries],'total',len(jobs),'images',15540,'cpu',result['cpu_seconds'])
