"""Complete649-profile actual three-seven/one-eight shared-star subdomain only."""
from pathlib import Path
import json,time
from star_low import SubsetEngine,json_value
HERE=Path(__file__).parent
st=time.time();src=json.loads((HERE/'GENERIC_FOUR_DOMAIN.json').read_text())['cases'];dom=[(i,r) for i,r in enumerate(src) if r['neighbor_degrees']==[7,7,7,8]];out=[]
for idx,r in dom:
 eng=SubsetEngine(21,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(source_id=idx,strict=z['bound']<1);out.append(z)
 if len(out)%100==0:print(len(out),'strict',sum(z['strict'] for z in out),'seconds',time.time()-st,flush=True)
 assert time.time()-st<55
(HERE/'FOUR_THREE_SEVENS_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(dom),domain_size=len(dom),cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('done',len(out),'strict',sum(z['strict'] for z in out),'max',max(z['bound'] for z in out),'seconds',time.time()-st)
