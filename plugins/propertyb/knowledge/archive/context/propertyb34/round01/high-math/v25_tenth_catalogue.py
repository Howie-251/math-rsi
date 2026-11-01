"""Complete tenth-lock promotion of the three nine-low residual profiles."""
from pathlib import Path
from fractions import Fraction
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from subset_position_dp import SubsetEngine
from six_low_extension import extensions
from unit_catalogue import canonical
from multilock import json_value

if __name__=='__main__':
 source=json.loads((HERE/'V25_NINE_Q9_BOUNDS.json').read_text())['results'];start=time.perf_counter();out=[]
 for x in source:
  if Fraction(x['bound'])<1:continue
  for d in (6,7):
   raw=0;seen={}
   for ns in extensions({int(t):n for t,n in x['counts'].items()},9,d):
    raw+=1;big=[t for t in ns if t.bit_count()>=3];key,p=canonical(big,10,[0]*9+[1],True)
    assert p[9]==9
    move=lambda t:sum(1<<p[i] for i in range(10) if t&(1<<i))
    nc={move(t):n for t,n in ns.items()};key=tuple(sorted(nc.items()))
    if key not in seen:seen[key]=nc
   cases=[]
   for j,nc in enumerate(seen.values()):
    eng=SubsetEngine(25,10,nc);z=eng.verify(eng.solve());z['id']=j;cases.append(z)
   out.append(dict(base=x['id'],new_degree=d,complete=True,labelled_extensions=raw,colored_orbits=len(seen),cases=cases))
   print(x['id'],d,'labelled',raw,'orbits',len(seen),'strict',sum(z['bound']<1 for z in cases),'elapsed',time.perf_counter()-start,flush=True)
   (HERE/'V25_TENTH_BOUNDS.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed=time.perf_counter()-start,complete=len(out)==6,results=out)),indent=2)+'\n')
