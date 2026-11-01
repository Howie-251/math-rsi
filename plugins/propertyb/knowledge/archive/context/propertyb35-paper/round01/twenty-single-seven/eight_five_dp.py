from pilot import *
from fractions import Fraction as Q
from collections import Counter
start=time.time();cpu=time.process_time();source=json.loads((HERE/'EIGHT_FIVE_DOMAIN.json').read_text())['cases'];out=[]
for i,r in enumerate(source):
 eng=SubsetEngine(20,6,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(source_id=i,strict=z['bound']<1);out.append(z)
 if len(out)%50==0:print(len(out),'strict',sum(z['strict'] for z in out),'secs',time.time()-start,flush=True)
 if len(out)%50==0 or len(out)==len(source):(HERE/'EIGHT_FIVE_DP.json').write_text(json.dumps(json_value(dict(cases=out,domain_size=len(source),complete=len(out)==len(source),cpu_seconds=time.process_time()-cpu,wall_seconds=time.time()-start)),indent=2)+'\n')
print('remaining',Counter(tuple(r['neighbor_degrees']) for r in out if not r['strict']),flush=True)
