from pathlib import Path
import importlib.util,sys,json,time,itertools,signal
from fractions import Fraction as Q
HERE=Path(__file__).resolve().parent;BASE=HERE.parent
spec=importlib.util.spec_from_file_location('own_ind',BASE/'independent31_33/check.py');a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
start=time.process_time();rows=[]
for ds,lam in [((11,11),1),((11,11),2),((11,12),1),((11,13),1)]:
 ell=a.two(*ds,lam);best=None
 for pos in itertools.permutations(range(9,24),2):
  val=a.bound(34,pos,ell)
  if best is None or val<best[0]:best=(val,pos)
  if val<1:break
 rows.append(dict(degrees=ds,lam=lam,ell=ell,U=str(best[0]),positions=best[1],strict=best[0]<1))
 print(rows[-1],flush=True)
(HERE/'PAIR_PROBE.json').write_text(json.dumps(dict(rows=rows,cpu_seconds=time.process_time()-start),indent=2)+'\n')
