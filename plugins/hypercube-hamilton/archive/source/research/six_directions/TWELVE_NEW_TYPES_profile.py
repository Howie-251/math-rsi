"""Explore actual residual cuts for new independent-hole marked local types."""
from pathlib import Path
from itertools import combinations,permutations
from collections import Counter,defaultdict
import json,hashlib,sys
R=Path(__file__).resolve().parent
stem=sys.argv[1] if len(sys.argv)>1 else 'HIGHER_Q5_FULL_T37_remaining'
types={(2,8,3):'T28',(1,9,4):'T19',(0,8,4):'T84',(0,10,5):'T105'}
PERM=[tuple(sum(((x>>i)&1)<<p[i] for i in range(5)) for x in range(32)) for p in permutations(range(5))]
canonical_cache={}
def canonical(M,J,U):
    shift=min(M if M else U)
    raw=tuple(sorted(x^shift for x in M)),tuple(sorted(x^shift for x in J)),tuple(sorted(x^shift for x in U))
    if raw in canonical_cache:return canonical_cache[raw]
    m,j,u=raw
    result=min((tuple(sorted(t[x^s] for x in m)),tuple(sorted(t[x^s] for x in j)),tuple(sorted(t[x^s] for x in u)))
               for s in (m if m else u) for t in PERM)
    canonical_cache[raw]=result
    return result
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
counts=Counter();reports=[];hashes={};rows_seen=[]
for v in (1,7,31):
    name=f'{stem}_h12_v{v}_covered.bin'
    raw=(R/name).read_bytes();assert len(raw)%11==0;hashes[name]=hashlib.sha256(raw).hexdigest()
    covered=Counter()
    for off in range(0,len(raw),11):
        Z=raw[off:off+5];W=raw[off+5:off+11];seen=set()
        for d in range(6):
            za=[x for x in Z if (x>>d&1)==(v>>d&1)];wa=[x for x in W if (x>>d&1)==(v>>d&1)]
            s=len(za)+1-len(wa)
            if s>=3:
                pool=za;minor=[x for x in Z if x not in za];major=[x for x in W if x not in wa];omit=s
            elif s<=-3:
                pool=[x for x in wa if x!=(1<<d)];minor=[x for x in W if x not in wa];major=[x for x in Z if x not in za];omit=-s
            else:continue
            typ=types.get((len(minor),len(major)+omit,omit))
            if typ is None or not wa:continue
            for sources in combinations(pool,omit):
                M=[project(x,d) for x in minor];U=[project(x,d) for x in sources];J=[project(x,d) for x in major]+U
                assert len(set(M+J))==len(M)+len(J)
                assert all((x^y).bit_count()!=1 for x in M for y in set(J)-set(U))
                seen.add((typ,canonical(M,J,U)))
        counts.update(seen)
        covered.update({typ for typ,g in seen})
        if seen:covered['any']+=1
    reports.append({'v':v,'input':len(raw)//11,'coverage_by_type':dict(covered)})
    print(reports[-1],flush=True)
rows=[]
for i,((typ,g),count) in enumerate(sorted(counts.items(),key=lambda x:(-x[1],x[0]))):
    rows.append({'index':i,'type':typ,'minority':g[0],'majority':g[1],'omitted':g[2],'actual_records':count})
out={'status':'PRODUCER_DIAGNOSTIC_ONLY','input_stem':stem,'input_hashes':hashes,'reports':reports,'raw_canonical_cache':len(canonical_cache),'marked_orbits':len(rows),'rows':rows,'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'TWELVE_NEW_TYPES_profile.json').write_text(json.dumps(out,indent=2)+'\n')
print('orbits',len(rows),'top',rows[:8],flush=True)
