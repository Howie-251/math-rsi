"""Actual smaller-hole Q5 input types not yet closed on the new residual."""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parent
types={(2,6,2):'T26',(1,5,2):'T15',(1,7,3):'T17',(0,6,3):'T63'}
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
    name=f'TWELVE_NEW_FORCED_HALL_union_remaining_v{v}.bin';raw=(R/name).read_bytes();hashes[name]=hashlib.sha256(raw).hexdigest();coverage=Counter()
    for off in range(0,len(raw),11):
        Z=raw[off:off+5];W=raw[off+5:off+11];seen=set()
        for d in range(6):
            za=[x for x in Z if (x>>d&1)==(v>>d&1)];wa=[x for x in W if (x>>d&1)==(v>>d&1)]
            s=len(za)+1-len(wa)
            if s>=2:pool=za;minor=[x for x in Z if x not in za];major=[x for x in W if x not in wa];omit=s
            elif s<=-2:pool=[x for x in wa if x!=(1<<d)];minor=[x for x in W if x not in wa];major=[x for x in Z if x not in za];omit=-s
            else:continue
            typ=types.get((len(minor),len(major)+omit,omit))
            if typ is None or not wa:continue
            for sources in combinations(pool,omit):
                M=[project(x,d) for x in minor];U=[project(x,d) for x in sources];J=[project(x,d) for x in major]+U
                seen.add((typ,canonical(M,J,U)))
        counts.update(seen);coverage.update({typ for typ,g in seen})
        if seen:coverage['any']+=1
    reports.append({'v':v,'input':len(raw)//11,'coverage_by_type':dict(coverage)});print(reports[-1],flush=True)
rows=[]
for i,((typ,g),count) in enumerate(sorted(counts.items(),key=lambda x:(-x[1],x[0]))):
    rows.append({'index':i,'type':typ,'minority':g[0],'majority':g[1],'omitted':g[2],'actual_records':count})
(R/'TWELVE_EXTRA_TYPES_profile.json').write_text(json.dumps({'status':'PRODUCER_ONLY','input_hashes':hashes,'reports':reports,'marked_orbits':len(rows),'rows':rows},indent=2)+'\n')
print('orbits',len(rows),'top',rows[:8])
