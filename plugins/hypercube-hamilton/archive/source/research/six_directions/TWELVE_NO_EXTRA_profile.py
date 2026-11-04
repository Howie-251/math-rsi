"""Profile records with no smaller-hole local-type cut, without proof claims."""
from pathlib import Path
from itertools import permutations
from collections import Counter
import json
R=Path(__file__).resolve().parent
rows={(3,2),(1,4),(4,3),(2,5),(4,2),(1,5),(5,3),(2,6)}
reports=[]
for v in (1,7,31):
    raw=(R/f'TWELVE_NEW_FORCED_HALL_union_remaining_v{v}.bin').read_bytes();left=[]
    for off in range(0,len(raw),11):
        rec=raw[off:off+11];Z=rec[:5];W=rec[5:];cuts=[]
        for d in range(6):cuts.append((sum((x>>d&1)==(v>>d&1) for x in Z),sum((x>>d&1)==(v>>d&1) for x in W)))
        if not any(c in rows for c in cuts):left.append(rec)
    perm=[]
    for p in permutations(range(6)):
        t=tuple(sum(((x>>i)&1)<<p[i] for i in range(6)) for x in range(64))
        if t[v]==v:perm.append(t)
    canon=Counter()
    for rec in left:
        c=min(tuple(sorted(t[x] for x in rec[:5]))+tuple(sorted(t[x] for x in rec[5:])) for t in perm)
        canon[c]+=1
    representatives=[]
    for rec,count in sorted(canon.items()):
        Z,W=rec[:5],rec[5:]
        cuts=[(sum((x>>d&1)==(v>>d&1) for x in Z),sum((x>>d&1)==(v>>d&1) for x in W)) for d in range(6)]
        representatives.append({'Z':Z,'W':W,'records':count,'cut_counts':cuts})
    (R/f'TWELVE_NO_EXTRA_remaining_v{v}.bin').write_bytes(b''.join(left))
    reports.append({'v':v,'records':len(left),'orbits':len(canon),'representatives':representatives})
(R/'TWELVE_NO_EXTRA_profile.json').write_text(json.dumps({'status':'PRODUCER_DIAGNOSTIC_ONLY','reports':reports},indent=2)+'\n')
print(json.dumps(reports))
