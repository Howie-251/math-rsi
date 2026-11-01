"""Fixed-position certificate replay for the373/1469/255 unit-star inventories.
Independent expanded35-stub injection arithmetic only; no DP or position search.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,time
from audit_core import verify
HERE=Path(__file__).parent
start=time.time();results=[]
for name in ['STAR_FOUR_DP.json','STAR_FIVE_DP.json','STAR_SIX_DP.json']:
 data=json.loads((HERE/name).read_text());assert data['complete'];rows=data['cases'];vals=[]
 for r in rows:vals.append(verify(dict(r,quotas=r['certificates'])))
 result=dict(source=name,cases=len(rows),strict=sum(z<1 for z in vals),max_strict=str(max(z for z in vals if z<1)),all_fixed_positions_verified=True)
 results.append(result);print(result,flush=True)
answer=dict(status='PASS',scope=__doc__,results=results,elapsed_seconds=time.time()-start)
(HERE/'FIXED_POSITION_REPLAY.json').write_text(json.dumps(answer,indent=2)+'\n');print('seconds',time.time()-start)
