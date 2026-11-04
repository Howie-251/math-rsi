"""Producer geometry exploration of new twelve-local-hole inputs at Q6 h14."""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parent
types={(4,8,2):'T48',(3,9,3):'T39',(2,10,4):'T2_10',(1,11,5):'T1_11',(0,12,6):'T0_12'}
PERM=[tuple(sum(((x>>i)&1)<<p[i] for i in range(5)) for x in range(32)) for p in permutations(range(5))]
cache={}
def canonical(M,J,U):
    shift=min(M if M else U)
    raw=tuple(sorted(x^shift for x in M)),tuple(sorted(x^shift for x in J)),tuple(sorted(x^shift for x in U))
    if raw not in cache:
        m,j,u=raw
        cache[raw]=min((tuple(sorted(t[x^s] for x in m)),tuple(sorted(t[x^s] for x in j)),tuple(sorted(t[x^s] for x in u))) for s in (m if m else u) for t in PERM)
    return cache[raw]
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
counts=Counter();reports=[];hashes={}
for v in (1,7,31):
    for free in (False,True):
        name=f'FOURTEEN_CACHED_remaining_h14_v{v}_{"free" if free else "covered"}.bin'
        raw=(R/name).read_bytes();assert len(raw)%13==0;hashes[name]=hashlib.sha256(raw).hexdigest();coverage=Counter()
        for off in range(0,len(raw),13):
            Z=raw[off:off+6];W=raw[off+6:off+13];seen=set()
            for d in range(6):
                za=[x for x in Z if (x>>d&1)==(v>>d&1)];wa=[x for x in W if (x>>d&1)==(v>>d&1)]
                s=len(za)+1-len(wa)
                if s>=2:pool=za;minor=[x for x in Z if x not in za];major=[x for x in W if x not in wa];omit=s
                elif s<=-2:pool=[x for x in wa if x!=(1<<d) and (not free or x!=v)];minor=[x for x in W if x not in wa];major=[x for x in Z if x not in za];omit=-s
                else:continue
                typ=types.get((len(minor),len(major)+omit,omit))
                if typ is None or not wa:continue
                for sources in combinations(pool,omit):
                    M=[project(x,d) for x in minor];U=[project(x,d) for x in sources];J=[project(x,d) for x in major]+U
                    assert len(set(M+J))==12 and set(U)<=set(J)
                    seen.add((typ,canonical(M,J,U)))
            counts.update(seen);coverage.update({typ for typ,g in seen})
            if seen:coverage['any']+=1
        reports.append({'v':v,'free_target':free,'input':len(raw)//13,'coverage_by_type':dict(coverage)})
        print(reports[-1],flush=True)
rows=[]
for i,((typ,g),count) in enumerate(sorted(counts.items(),key=lambda x:(-x[1],x[0]))):
    rows.append({'index':i,'type':typ,'minority':g[0],'majority':g[1],'omitted':g[2],'actual_records':count})
(R/'FOURTEEN_NEW_TYPES_profile.json').write_text(json.dumps({'status':'PRODUCER_ONLY','input_hashes':hashes,'reports':reports,'marked_orbits':len(rows),'rows':rows,'full_fourteen_hole_proved':False,'full_P6_proved':False},indent=2)+'\n')
print('orbits',len(rows),'top',rows[:8])
