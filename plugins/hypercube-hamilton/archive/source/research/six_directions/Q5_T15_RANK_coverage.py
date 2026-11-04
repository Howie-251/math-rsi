"""Producer union/remaining bytes from the complete actual projection witnesses."""
from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
P=Path(__file__).resolve().parent
profile=json.loads((P/'Q5_T15_RANK_profile.json').read_text())
ranks=json.loads((P/'Q5_T15_RANK_batch_summary.json').read_text())
keys={(tuple(r['geometry']['majority']),tuple(r['geometry']['omitted'])):r['orbit_index'] for r in ranks['reports'] if r['full_rank']}
byorbit=defaultdict(set);witness={}
for w in profile['witnesses']:
 key=(tuple(w['canonical_majority']),tuple(w['canonical_omitted']))
 if key not in keys:continue
 i=keys[key];byorbit[i].add(w['record_id']);witness.setdefault(w['record_id'],w)
covered=set(witness);greedy=[];have=set();todo=set(byorbit)
while todo:
 i=max(todo,key=lambda j:(len(byorbit[j]-have),-j));new=byorbit[i]-have
 if not new:break
 greedy.append({'orbit_index':i,'new':len(new),'targets':dict(Counter(profile['records'][k]['v'] for k in new))});have|=new;todo.remove(i)
reports=[]
for v in (1,7,31):
 original=[r for r in profile['records'] if r['v']==v]
 remaining=[r for i,r in enumerate(profile['records']) if r['v']==v and i not in covered]
 raw=bytes(x for r in remaining for x in r['record']);name=f'Q5_T15_RANK_remaining_v{v}.bin';(P/name).write_bytes(raw)
 reports.append({'v':v,'input':len(original),'covered':len(original)-len(remaining),'remaining':len(remaining),'remaining_sha256':hashlib.sha256(raw).hexdigest()})
assert len(covered)==2346 and all(i in covered for i,r in enumerate(profile['records']) if r['no_T17_cut'])
out={'status':'PRODUCER_ONLY_PENDING_INDEPENDENT_RANK_AND_TRANSFER_REVIEW','input_count':4096,'covered':2346,'remaining':1750,
 'no_T17_count':462,'no_T17_all_covered':True,'reports':reports,'greedy':greedy,
 'selected_witnesses':[{'record_id':i,**w} for i,w in sorted(witness.items())],
 'full_T15_proved':False,'full_ten_hole_proved':False,'full_P6_proved':False}
(P/'Q5_T15_RANK_coverage.json').write_text(json.dumps(out,indent=2)+'\n')
print('producer coverage2346, residual1750; no-T17 all462 covered')
