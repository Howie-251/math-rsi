"""Actual marked T63 inputs in the candidate T26 residual, producer only."""
import itertools,json,functools
from pathlib import Path
from collections import defaultdict
R=Path(__file__).resolve().parent
PERMS=[tuple(sum(((x>>i)&1)<<p[i] for i in range(5)) for x in range(32)) for p in itertools.permutations(range(5))]
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
@functools.lru_cache(None)
def canon(H,U):
    return min((tuple(sorted(t[x^s] for x in H)),tuple(sorted(t[x^s] for x in U))) for s in U for t in PERMS)
coverage=defaultdict(set)
for v in (1,7,31):
    data=(R/f'Q5_T26_RANK_batch_remaining_v{v}.bin').read_bytes()
    for off in range(0,len(data),9):
        z,w=set(data[off:off+4]),set(data[off+4:off+9])
        for d in range(6):
            za={x for x in z if not((x^v)>>d&1)};wa={x for x in w if not((x^v)>>d&1)}
            if (len(za),len(wa))==(4,2):sources=za;other=w-wa
            elif (len(za),len(wa))==(1,5):sources=wa-{1<<d};other=z-za
            else:continue
            for S in itertools.combinations(sources,3):
                U=tuple(sorted(project(x^(1<<d),d) for x in S))
                H=tuple(sorted([project(x,d) for x in other]+list(U)))
                assert len(set(H))==6 and len(set(x.bit_count()%2 for x in H))==1
                coverage[canon(H,U)].add((v,off//9))
rows=[]
for (H,U),records in sorted(coverage.items(),key=lambda x:(-len(x[1]),x[0])):
    rows.append({'holes':H,'omitted':U,'covered_records':len(records),'targets':{str(v):sum(x[0]==v for x in records) for v in (1,7,31)}})
out={'status':'PRODUCER_ONLY','orbits':len(rows),'rows':rows}
(R/'Q5_T63_RANK_profile.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
