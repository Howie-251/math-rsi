"""Exact new-row filtering of independently audited covered-target residuals."""
import json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
GOOD={(0,1),(1,1),(0,2),(3,4),(4,4),(3,5)}
reports=[]
for v in (1,7,31):
    inp=R/f'TEN_HOLE_COVERED_PARTIAL_REVIEW_remaining_v{v}.bin'
    data=inp.read_bytes();assert len(data)%9==0
    kept=bytearray();witness=[]
    for off in range(0,len(data),9):
        rec=data[off:off+9];z,w=rec[:4],rec[4:]
        assert len(set(rec))==9 and v not in rec and 0 not in rec
        chosen=None
        for d in range(6):
            a=sum(((x^v)>>d)&1==0 for x in z);b=sum(((x^v)>>d)&1==0 for x in w)
            if (a,b) in GOOD:chosen=[d,a,b];break
        if chosen is None:kept.extend(rec)
        else:witness.append({'input_index':off//9,'cut':chosen[0],'a':chosen[1],'b':chosen[2]})
    target=R/f'ten_covered_after_full_A8_v{v}.bin';target.write_bytes(kept)
    reports.append({'v':v,'input_file':inp.name,'input_sha256':hashlib.sha256(data).hexdigest(),
        'input_count':len(data)//9,'newly_covered':len(witness),'remaining':len(kept)//9,
        'remaining_file':target.name,'remaining_sha256':hashlib.sha256(kept).hexdigest(),'witnesses':witness})
out={'scope':'Consequences conditional on complete A8 acceptance and independent application review',
     'input_count':sum(x['input_count'] for x in reports),'newly_covered':sum(x['newly_covered'] for x in reports),
     'remaining':sum(x['remaining'] for x in reports),'reports':reports,'full_ten_hole_proved':False,'full_p6_proved':False}
(R/'ten_covered_after_full_A8.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='reports'}))
