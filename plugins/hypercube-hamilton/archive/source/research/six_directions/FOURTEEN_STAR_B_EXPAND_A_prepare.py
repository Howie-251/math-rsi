from pathlib import Path
from itertools import permutations
import json
R=Path(__file__).resolve().parent
d=json.loads((R/'FOURTEEN_STAR_B_EXPAND_profile.json').read_text())
summary=json.loads((R/'FOURTEEN_STAR_B_EXPAND_summary.json').read_text());assert len(summary['reports'])==42 and all(x['forced_rank_reached'] for x in summary['reports'])
seeds=json.loads((R/'TWELVE_ROOT_STAR_NONADJACENT_OPTIONS.json').read_text())['opening_cases']
maps=[tuple(sum(((x>>p[i])&1)<<i for i in range(5)) for x in range(32)) for p in permutations(range(5))]
# The pilot uses this bit-extraction convention; preserve its exact permutation IDs.
out=[]
for orbit in (79,87):
 opts=[]
 for op in d['actual_options']:
  if op['orbit']!=orbit:continue
  for case,seed in enumerate(seeds):
   for pi,tr in enumerate(maps):
    q,b,t=map(tr.__getitem__,seed)
    if (t,b)==(op['t'],op['b']):opts.append(dict(op,q=q,case=case,A_permutation=pi))
 (R/f'FOURTEEN_STAR_B_EXPAND_A_options_{orbit}.bin').write_bytes(b''.join(bytes([o['q'],o['t'],o['w'],o['b'],o['case'],o['A_permutation']]) for o in opts))
 (R/f'FOURTEEN_STAR_B_EXPAND_A_T_{orbit}.txt').write_bytes((R/f'FOURTEEN_RESIDUAL_STRUCTURE_maxA_T_{orbit}.txt').read_bytes())
 out.append({'orbit':orbit,'options':opts})
(R/'FOURTEEN_STAR_B_EXPAND_A_options.json').write_text(json.dumps(out,indent=2)+'\n')
s=(R/'FOURTEEN_RESIDUAL_STRUCTURE_maxA_pilot.cpp').read_text().replace('FOURTEEN_RESIDUAL_STRUCTURE_maxA','FOURTEEN_STAR_B_EXPAND_A')
(R/'FOURTEEN_STAR_B_EXPAND_A_pilot.cpp').write_text(s)
print([(x['orbit'],len(x['options'])) for x in out])
