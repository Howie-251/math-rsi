from itertools import permutations,combinations_with_replacement
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent;start=time.process_time()
quad=[x for x in range(128) if x.bit_count()==4];rank={q:i for i,q in enumerate(quad)}
def move(mask,p):return sum(1<<p[i] for i in range(7) if mask&(1<<i))
cases=[([31],4),([124,121],2),([124,115],2)]
allperms=list(permutations(range(7)));entries=[];jobs=[]
for case,(internal,nq) in enumerate(cases):
    group=[p for p in allperms if sorted(move(T,p) for T in internal)==sorted(internal)]
    assert len(group)==(240 if case==0 else 48)
    actions=[[rank[move(q,p)] for q in quad] for p in group]
    allkeys=list(combinations_with_replacement(range(35),nq));assert len(allkeys)==(73815 if case==0 else 630)
    seen=set();images=[];localjobs=[]
    for key in allkeys:
        if key in seen:continue
        transports={}
        for pi,action in enumerate(actions):
            image=tuple(sorted(action[i] for i in key));transports.setdefault(image,pi)
        orbit=set(transports);assert key==min(orbit) and not seen&orbit
        job=len(jobs);row=dict(job=job,case=case,quad_masks=[quad[i] for i in key],orbit_size=len(orbit));jobs.append(row);localjobs.append(row)
        for image in sorted(orbit):images.append(dict(quad_masks=[quad[i] for i in image],job=job,transport_index=transports[image]))
        seen|=orbit
    assert seen==set(allkeys) and len(images)==len(allkeys)
    entries.append(dict(case=case,internal_masks=internal,nquad=nq,group=[list(p) for p in group],
                        raw_quad_multisets=len(allkeys),orbit_count=len(localjobs),jobs=localjobs,all_quad_images=images))
result=dict(scope='complete quad multiset orbit jobs and every labelled image/transport for the two one-J inventories',
            cases=entries,jobs=jobs,job_count=len(jobs),cpu_seconds=time.process_time()-start)
(HERE/'QUAD_ORBITS.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
(HERE/'JOBS.tsv').write_text(''.join(' '.join(map(str,[r['job'],r['case'],len(r['quad_masks'])]+r['quad_masks']))+'\n' for r in jobs))
print('case orbit counts',[x['orbit_count'] for x in entries],'total jobs',len(jobs),'raw',[x['raw_quad_multisets'] for x in entries],'cpu',result['cpu_seconds'])
