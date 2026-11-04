"""Actual cut/source witnesses for seven positive T63 rank inputs; producer."""
import itertools,json,functools,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
registry=json.loads((R/'Q5_T63_RANK_batch_summary.json').read_text())['reports']
assert len(registry)==7 and all(r['full_rank'] and r['rank']==4096 for r in registry)
good={(tuple(r['geometry']['holes']),tuple(r['geometry']['omitted'])):r['orbit_index'] for r in registry}
PERMS=[tuple(sum(((x>>i)&1)<<p[i] for i in range(5)) for x in range(32)) for p in itertools.permutations(range(5))]
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
@functools.lru_cache(None)
def canon(H,U):return min((tuple(sorted(t[x^s] for x in H)),tuple(sorted(t[x^s] for x in U))) for s in U for t in PERMS)
reports=[];witnesses=[]
for v in (1,7,31):
    p=R/f'Q5_T26_RANK_BATCH_REVIEW_remaining_v{v}.bin';data=p.read_bytes();remaining=bytearray();count=0
    for off in range(0,len(data),9):
        rec=data[off:off+9];z,w=set(rec[:4]),set(rec[4:]);hit=None
        for d in range(6):
            za={x for x in z if not((x^v)>>d&1)};wa={x for x in w if not((x^v)>>d&1)}
            if (len(za),len(wa))==(4,2):sources=za;other=w-wa
            elif (len(za),len(wa))==(1,5):sources=wa-{1<<d};other=z-za
            else:continue
            for S in itertools.combinations(sorted(sources),3):
                U=tuple(sorted(project(x^(1<<d),d) for x in S));H=tuple(sorted([project(x,d) for x in other]+list(U)))
                key=canon(H,U)
                if key in good:
                    hit={'v':v,'input_index':off//9,'cut':d,'row':[len(za),len(wa)],'sources':list(S),'holes':H,'omitted':U,'orbit_index':good[key]};break
            if hit:break
        if hit:witnesses.append(hit);count+=1
        else:remaining.extend(rec)
    out=R/f'Q5_T63_RANK_remaining_v{v}.bin';out.write_bytes(remaining)
    reports.append({'v':v,'input':len(data)//9,'input_file':p.name,'input_sha256':hashlib.sha256(data).hexdigest(),'newly_covered':count,'remaining':len(remaining)//9,'remaining_file':out.name,'remaining_sha256':hashlib.sha256(remaining).hexdigest()})
out={'status':'PRODUCER_ONLY_PENDING_INDEPENDENT_REVIEW','input':sum(r['input'] for r in reports),'newly_covered':len(witnesses),'remaining':sum(r['remaining'] for r in reports),'reports':reports,'witnesses':witnesses,'full_ten_hole_proved':False,'full_P6_proved':False}
(R/'Q5_T63_RANK_coverage.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(reports))
