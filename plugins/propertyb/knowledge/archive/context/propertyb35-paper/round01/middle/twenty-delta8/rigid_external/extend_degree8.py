"""Same actual five-eight core, external pivot degree8 rather than9. The weighted K5 domain is unchanged.
Delta>=8 and outside degree sum135 guarantee some external8/9 with mixed incidence<=4.
"""
from pathlib import Path
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value
start=time.time();domain=json.loads((HERE/'DOMAIN.json').read_text());out=[]
for r in domain['orbits']:
 ns={int(t):n for t,n in r['counts'].items()};ns[0]+=1;ns[32]-=1;eng=SubsetEngine(20,6,ns);z=eng.verify(eng.solve());z.update(id=r['id'],degrees=[8]*6,weighted_pairs=r['weighted_pairs'],mixed_incidence=r['mixed_incidence'],y_low_codegrees=r['y_low_codegrees']);z['strict']=z['bound']<1;out.append(z);print(r['id'],z['bound'],flush=True)
(HERE/'DEGREE8_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,all_strict=all(r['strict'] for r in out),max_bound=max(r['bound'] for r in out),elapsed_seconds=time.time()-start)),indent=2)+'\n');print('all strict',all(r['strict'] for r in out),'max',max(r['bound'] for r in out),'seconds',time.time()-start)
