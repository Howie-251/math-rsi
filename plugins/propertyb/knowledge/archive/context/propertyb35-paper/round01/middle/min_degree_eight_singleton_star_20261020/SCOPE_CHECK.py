from pathlib import Path
from collections import Counter
from itertools import product
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();old=P.parent/'three_nonunit_direct_repair_20261020'
d=json.loads((old/'TAIL_RESULT.json').read_text());full=json.loads((old/'FIVE_LOCK_FULL83.json').read_text());rows=[];generic=0
for r in d['rows']:
 tr=tuple(r['traces']);h=[sum(T>>v&1 for T in tr) for v in range(5)]
 budget=31-sum(r['k_by_v'])
 for ds in product(range(budget+1),repeat=5):
  if sum(ds)!=budget:continue
  a=tuple(x+y for x,y in zip(r['k_by_v'],ds));generic+=1
  deg=[1+x+y for x,y in zip(a,h)]
  if min(deg)<8:continue
  rows.append({'traces':tr,'attachments':a,'degrees':deg,'F_high_excess':sum(max(x-9,0) for x in deg)})
assert generic==119 and len(rows)==25
keys={(tuple(z['traces']),tuple(z['attachments'])) for z in rows}
assert keys=={(tuple(z['traces']),tuple(z['attachments'])) for z in full['cases'] if min(z['selected_degrees'])>=8}
hist=Counter(z['F_high_excess'] for z in rows);assert hist=={0:1,1:11,2:11,3:1,4:1}
out={'status':'PASS','scope':'All119 generic safe-prefix failed attachment keys, filtered only by minFdegree>=8. No global/F high-excess filter, no unique6 or seven-count hypothesis. Existing independently certified25+70 keys are exactly unchanged.','generic_keys':generic,'min8_keys':len(rows),'F_high_excess_histogram':dict(hist),'all_F_excess_le4_is_conclusion':True,'global_high_excess_not_assumed':True,'cases':rows,'cpu_seconds':time.process_time()-st}
(P/'SCOPE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
