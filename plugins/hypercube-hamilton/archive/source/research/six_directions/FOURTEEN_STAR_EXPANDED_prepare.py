from pathlib import Path
from itertools import permutations
from collections import Counter
import json,hashlib
R=Path(__file__).resolve().parent
profile=json.loads((R/'FOURTEEN_STAR_B_EXPAND_profile.json').read_text())
selected=json.loads((R/'FOURTEEN_STAR_B_EXPAND_selected.json').read_text())['used_local_indices']
classes=[]
for i in selected:
 g=profile['rows'][i];classes.append({'index':i,'geometry':g,'forced_cherries':[[0,*g['forced_pair']]],'forced_pairs':[g['forced_pair']],'covered_endpoints':22,'reduced_endpoints':20,'target_rank':512,'source_prefix':f'FOURTEEN_STAR_B_EXPAND_orbit_{i:03d}'})
(R/'FOURTEEN_STAR_B_REDUCED_candidate_classes.json').write_text(json.dumps({'classes':classes},indent=2)+'\n')
s=(R/'FOURTEEN_FORCED_prepare.py').read_text();s=s[:s.index('plain=next(')].replace('FOURTEEN_FORCED','FOURTEEN_STAR_B_REDUCED')
s+="(R/'FOURTEEN_STAR_B_REDUCED_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY','reports':out},indent=2)+'\\n')\nprint('Extracted',len(out),'reduced B certificates')\n"
(R/'FOURTEEN_STAR_B_REDUCED_prepare.py').write_text(s)
# Separate auxiliary counts; do not mutate the accepted orbit85 artifacts.
base=(R/'FOURTEEN_RESIDUAL_STRUCTURE_count.py').read_text().split('# a compact check')[0]
for orbit in (79,87):
 code=base.replace("r=j['orbit_rows'][85]",f"r=j['orbit_rows'][{orbit}]").replace("'orbit_index':85",f"'orbit_index':{orbit}").replace('FOURTEEN_RESIDUAL_STRUCTURE_maxA_count_85',f'FOURTEEN_STAR_B_EXPAND_A_count_{orbit}')
 (R/f'FOURTEEN_STAR_B_EXPAND_A_count_{orbit}.py').write_text(code)
# Exact positive input transports under permutations fixing0 and31.
structure=json.loads((R/'FOURTEEN_RESIDUAL_STRUCTURE.json').read_text())
maps=[tuple(sum(((x>>p[d])&1)<<d for d in range(5))|(x&32) for x in range(64)) for p in permutations(range(5))]
orbits={};wits={}
for orbit in (79,87):
 row=structure['orbit_rows'][orbit];rep=row['Z']+row['W'];orb=set()
 for pi,tr in enumerate(maps):
  rec=tuple(sorted(tr[x] for x in rep[:6]))+tuple(sorted(tr[x] for x in rep[6:]));orb.add(rec);wits.setdefault(rec,(orbit,pi))
 assert len(orb)==60;orbits[orbit]=orb
assert not orbits[79]&orbits[87];union=orbits[79]|orbits[87];reports=[];transports=[]
for v in (1,7,31):
 name=f'FOURTEEN_RESIDUAL_STRUCTURE_maxA_remaining_v{v}_covered.bin';raw=(R/name).read_bytes();assert len(raw)%13==0;positive=bytearray();remaining=bytearray()
 for idx in range(len(raw)//13):
  rec=raw[13*idx:13*(idx+1)]
  if v==31 and tuple(rec) in union:
   orbit,pi=wits[tuple(rec)];positive.extend(rec);transports.append({'v':v,'source_index':idx,'orbit':orbit,'permutation':pi})
  else:remaining.extend(rec)
 (R/f'FOURTEEN_STAR_EXPANDED_remaining_v{v}_covered.bin').write_bytes(remaining)
 (R/f'FOURTEEN_STAR_EXPANDED_positive_v{v}_covered.bin').write_bytes(positive)
 reports.append({'v':v,'source':name,'source_sha256':hashlib.sha256(raw).hexdigest(),'input':len(raw)//13,'positive':len(positive)//13,'remaining':len(remaining)//13})
assert len(transports)==120
(R/'FOURTEEN_STAR_EXPANDED_transport.json').write_text(json.dumps({'status':'PRODUCER_ONLY','reports':reports,'transports':transports,'remaining':2407,'full_fourteen_hole_proved':False,'full_P6_proved':False},indent=2)+'\n')
print('Prepared ten B extractions, two auxiliary counters,120 actual transports')
