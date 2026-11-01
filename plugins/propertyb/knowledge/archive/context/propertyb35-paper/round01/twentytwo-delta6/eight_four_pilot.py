from pathlib import Path
import sys,json,time
P=Path(__file__).resolve();ROOT=P.parents[4];HERE=P.parent
sys.dont_write_bytecode=True;sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
rs=json.loads((HERE/'EIGHT_FOUR_DOMAIN.json').read_text())['cases'];indices=sorted({i*(len(rs)-1)//31 for i in range(32)});start=time.process_time();out=[]
for i in indices:
 r=rs[i];eng=SubsetEngine(22,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(source_id=i,strict=z['bound']<1);z.pop('rows',None);out.append(z)
 print(i,r['weight'],z['bound'],flush=True)
(HERE/'EIGHT_FOUR_PILOT.json').write_text(json.dumps(json_value(dict(cases=out,strict=sum(r['strict']for r in out),domain_size=len(rs),cpu_seconds=time.process_time()-start)),indent=2)+'\n');print('strict',sum(r['strict']for r in out),'/',len(out),'cpu',time.process_time()-start)
