"""Conditional producer: full balanced Q5 endpoints permit row (4,5)."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent
reports=[]
for v in (1,7,31):
    inp=R/f'ten_covered_after_full_A8_v{v}.bin';raw=inp.read_bytes()
    t63path=R/f'ten_covered_t63_complete_split_remaining_v{v}.bin'
    t63=t63path.read_bytes();t63set={t63[i:i+9] for i in range(0,len(t63),9)}
    kept=bytearray();combined=bytearray();witness=[]
    for off in range(0,len(raw),9):
        rec=raw[off:off+9]
        cut=next((d for d in range(6) if all(not((x^v)>>d&1) for x in rec)),None)
        if cut is not None:
            witness.append({'input_index':off//9,'cut':cut})
            assert rec in t63set,'New endpoint coverage unexpectedly overlaps T63'
        else:
            kept.extend(rec)
            if rec in t63set:combined.extend(rec)
    (R/f'ten_covered_full_q5_endpoint_remaining_v{v}.bin').write_bytes(kept)
    (R/f'ten_covered_q5_and_t63_remaining_v{v}.bin').write_bytes(combined)
    reports.append({'v':v,'input_sha256':hashlib.sha256(raw).hexdigest(),
         't63_remaining_sha256':hashlib.sha256(t63).hexdigest(),
         'input_count':len(raw)//9,'newly_covered':len(witness),'witnesses':witness,
         'endpoint_only_remaining':len(kept)//9,'combined_remaining':len(combined)//9,
         'endpoint_remaining_sha256':hashlib.sha256(kept).hexdigest(),
         'combined_remaining_sha256':hashlib.sha256(combined).hexdigest()})
out={'scope':'Conditional on full Q5 endpoint and T63 application acceptance; no full ten/P6 claim',
     'newly_covered':sum(x['newly_covered'] for x in reports),
     'endpoint_only_remaining':sum(x['endpoint_only_remaining'] for x in reports),
     'combined_remaining':sum(x['combined_remaining'] for x in reports),'reports':reports}
(R/'ten_covered_full_q5_endpoint_filter.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='reports'}))
