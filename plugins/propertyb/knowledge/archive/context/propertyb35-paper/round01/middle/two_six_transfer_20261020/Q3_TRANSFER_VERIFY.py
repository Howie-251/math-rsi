from pathlib import Path
from fractions import Fraction
from math import comb
from collections import Counter
import json,time,sys
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
source=json.loads((P.parent/'three_nonunit_direct_repair_20261020/RESULT.json').read_text())
threshold={tuple(t['types']):set(t['failure_a']) for t in source['residual_types']}
def comp(n,k):
 if k==1:yield (n,);return
 for v in range(n+1):
  for rest in comp(n-v,k-1):yield(v,)+rest
generic=[];rows=[]
for r in source['remaining']:
 h=[sum(t>>v&1 for t in r['traces']) for v in range(5)]
 for inc in comp(31-r['sum_k'],5):
  a=[x+y for x,y in zip(r['k_by_v'],inc)]
  if any(x not in threshold[tuple(t)] for x,t in zip(a,r['types_by_v'])):continue
  d=[1+x+y for x,y in zip(a,h)];e=sum(max(x-9,0) for x in d)
  generic.append((tuple(r['traces']),tuple(a)))
  for n7 in (0,1):
   if min(d)>=6 and d.count(6)<=2 and d.count(7)<=n7 and e<=2*n7+1:
    rows.append(dict(a=n7,traces=r['traces'],attachments=a,original_F_degrees=d,F_high_excess=e))
assert len(generic)==119
(P/'Q3_TAIL.json').write_text(json.dumps(rows,indent=2)+'\n')
unique={(tuple(z['traces']),tuple(z['attachments'])) for z in rows}
certs=json.loads((P/'Q3_FIVE_LOCK_FULL69.json').read_text())['cases']
assert unique=={(tuple(z['traces']),tuple(z['attachments'])) for z in certs}
strict=[z for z in certs if z['best']['strict']];residual=[z for z in certs if not z['best']['strict']]
assert len(strict)==66 and len(residual)==3
double=next(z for z in certs if z['selected_degrees'].count(6)==2)
assert double['traces']==[0,0,7] and double['best']['strict']
old=json.loads((P.parent/'three_nonunit_direct_repair_20261020/SIX_LOCK_COMMON_STAR47.json').read_text())
chosen=[z for z in old['cases'] if z['source'] in ('A','C') and not z['picked_multi']]
assert Counter(z['source'] for z in chosen)=={'A':5,'C':5}
for z in chosen:
 masks=z['expanded35_masks'];assert len(masks)==35
 types=[frozenset(v+1 for v in range(6) if m>>v&1) for m in masks]
 ir=independent_rows(21,tuple(z['best']['positions']),types)
 bound=sum((min(r['A'],r['B'],r['C']) for r in ir),Fraction())
 assert bound==Fraction(z['best']['bound'])<1
out=dict(status='PASS',scope='Rebuild the whole119 generic q3 attachment tail from prior complete91-orbit source; allow at most two F degree6 points, actual seven count0/1 and high excess<=1/3. All fixed69 original35-index certificates were independently replayed by Q3_FIVE_LOCK_FULL69.py; this run independently replays ten transferred A/C singleton-star certificates. B is excluded by the separate actual star argument in PROOF.md.',generic_q3_tails=len(generic),a0_keys=sum(z['a']==0 for z in rows),a1_keys=sum(z['a']==1 for z in rows),unique_necessary_keys=len(unique),five_lock_strict=66,residual=[dict(traces=z['traces'],attachments=z['attachments'],degrees=z['selected_degrees']) for z in residual],new_double_six_certificate=double['best'],transferred_six_lock_certificates=10,transferred_max=str(max(Fraction(z['best']['bound']) for z in chosen)),cpu_seconds=time.process_time()-st)
(P/'Q3_TRANSFER_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
