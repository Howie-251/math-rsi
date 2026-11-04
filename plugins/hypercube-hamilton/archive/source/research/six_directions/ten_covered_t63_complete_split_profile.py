"""Producer-only coverage for a proposed Q5 T63 complete marked split lemma.

No proof acceptance is inferred from this diagnostic. Frozen inputs are read only.
"""
import hashlib,itertools,json
from collections import Counter
from functools import lru_cache
from pathlib import Path
R=Path(__file__).resolve().parent
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
@lru_cache(None)
def signature(H,U):
    good=tuple(d for d in range(5) if (sum(not(x>>d&1) for x in H),sum(not(x>>d&1) for x in U)) in ((2,1),(4,2)))
    if not good:return None
    return [list(good)]

def route(rec,v):
    z,w=rec[:4],rec[4:]
    for d in range(6):
        za=[x for x in z if not((x^v)>>d&1)];wa=[x for x in w if not((x^v)>>d&1)]
        if (len(za),len(wa))==(4,2):
            candidates=za;base=[x for x in w if (x^v)>>d&1]
        elif (len(za),len(wa))==(1,5):
            candidates=[x for x in wa if x!=(1<<d)];base=[x for x in z if (x^v)>>d&1]
        else:continue
        for S in itertools.combinations(candidates,3):
            U=tuple(sorted(project(x^(1<<d),d) for x in S))
            H=tuple(sorted([project(x,d) for x in base]+list(U)))
            assert len(set(H))==6 and len({x.bit_count()%2 for x in H})==1
            hit=signature(H,U)
            if hit is not None:return {'cut':d,'row':[len(za),len(wa)],'S':list(S),'H':list(H),'U':list(U),'split_witness':hit}
    return None
def main():
    reports=[]
    for v in (1,7,31):
        p=R/f'ten_covered_after_full_A8_v{v}.bin';data=p.read_bytes();witness=[];remaining=bytearray()
        for off in range(0,len(data),9):
            rec=data[off:off+9];hit=route(rec,v)
            if hit is None:remaining.extend(rec)
            else:witness.append({'input_index':off//9,**hit})
        target=R/f'ten_covered_t63_complete_split_remaining_v{v}.bin';target.write_bytes(remaining)
        reports.append({'v':v,'input_count':len(data)//9,'input_sha256':hashlib.sha256(data).hexdigest(),
                        'conditionally_covered':len(witness),'remaining':len(remaining)//9,'witnesses':witness,
                        'remaining_sha256':hashlib.sha256(remaining).hexdigest()})
        print(v,len(data)//9,len(witness),len(remaining)//9,flush=True)
    out={'status':'PRODUCER ONLY: conditional on unreviewed complete T63 split lemma including zero crossing and application',
         'full_ten_hole_proved':False,'full_p6_proved':False,'reports':reports,
         'conditionally_covered':sum(x['conditionally_covered'] for x in reports),'remaining':sum(x['remaining'] for x in reports)}
    (R/'ten_covered_t63_complete_split_profile.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
