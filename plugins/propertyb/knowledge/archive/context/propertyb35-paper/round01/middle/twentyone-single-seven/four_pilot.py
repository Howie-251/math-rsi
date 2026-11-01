"""Spread fixed-layout DP pilot of1076 shared four-neighbor inventories."""
from three import *
start=time.time();rs=json.loads((HERE/'FOUR_DOMAIN.json').read_text())['orbits'];ids={round(i*(len(rs)-1)/17) for i in range(18)};out=[]
for i in sorted(ids):
 r=rs[i];en=SubsetEngine(21,5,r['counts']);z=en.verify(en.solve());z.update(r);z['strict']=z['bound']<1;out.append(z);print(i,r['neighbor_degrees'],z['bound'],z['strict'],flush=True)
(HERE/'FOUR_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,domain_count=len(rs),cases=out,sample_count=len(out),fixed_strict=sum(r['strict'] for r in out),elapsed_seconds=time.time()-start)),indent=2)+'\n');print('strict',sum(r['strict'] for r in out),'of',len(out),'seconds',time.time()-start)
