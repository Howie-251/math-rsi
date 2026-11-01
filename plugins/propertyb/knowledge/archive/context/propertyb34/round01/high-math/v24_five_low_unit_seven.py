"""Complete seven-unit-lock profiles of degrees 6^5 7^2 for the r=5 branch."""
from pathlib import Path
from itertools import combinations
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from unit_catalogue import canonical,fullblocks
from subset_position_dp import SubsetEngine
from multilock import json_value

if __name__=='__main__':
 source=json.loads((HERE/'UNIT_CATALOGUE_7.json').read_text());seen={};raw=0;start=time.perf_counter()
 for big in source['orbits']:
  for low in combinations(range(7),5):
   key,p=canonical(big,7,[0 if i in low else 1 for i in range(7)],True)
   if key in seen:continue
   assert sum(1<<p[i] for i in low)==31
   bs=fullblocks(key,7);ns={t:1 for t in bs}
   for i in range(7):ns[1<<i]=(6 if i<5 else 7)-sum(bool(t&(1<<i)) for t in bs)
   ns[0]=34-sum(ns.values())
   if min(ns.values())<0:continue
   seen[key]={t:n for t,n in ns.items() if n}
 out=[]
 for j,(key,ns) in enumerate(seen.items()):
  e=SubsetEngine(24,7,ns);z=e.verify(e.solve());z.update(group=j,large_blocks=key);out.append(z)
 (HERE/'V24_FIVE_LOW_UNIT_SEVEN.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,orbits=len(out),elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
 print(len(out),sum(z['bound']<1 for z in out),max(z['bound'] for z in out),time.perf_counter()-start,flush=True)
