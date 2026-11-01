"""All nonunit pairs among usable seven-degree highs above five pairwise-unit lows."""
from pathlib import Path
from fractions import Fraction
from itertools import permutations
import json,sys,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from five_low_second_high import canonical as canonical6,drop_x
from subset_position_dp import SubsetEngine
from multilock import json_value

MAPS=[tuple(((t&32)<<1|(t&64)>>1 if swap else t&96)|sum(1<<p[i] for i in range(5) if t&(1<<i)) for t in range(128)) for p in permutations(range(5)) for swap in (False,True)]
def canonical7(ns):return min(tuple(sorted((p[t],n) for t,n in ns.items())) for p in MAPS)

def extensions(ns,c):
 blocks=sorted(t for t,n in ns.items() if t&31 and n and t.bit_count()<5)
 def visit(left,chosen,xc):
  if xc>c:return
  if not left:
   k=c-xc
   if k>ns.get(32,0) or len(chosen)+k>7:return
   nc=ns.copy()
   for t in chosen:nc[t]-=1;nc[t|64]=1
   if k:nc[32]-=k;nc[96]=k
   nc[64]=7-len(chosen)-k;nc[0]-=nc[64]
   if min(nc.values())>=0:yield {t:n for t,n in nc.items() if n}
   return
  bit=left&-left
  for t in blocks:
   low=t&31
   if low&bit and low&left==low:yield from visit(left^low,chosen+[t],xc+int(bool(t&32)))
 yield from visit(31,[],0)

if __name__=='__main__':
 start=time.perf_counter();source=next(g for g in json.loads((HERE/'MIXED_SIX_JOINT.json').read_text())['sources'] if g['source']=='MIXED_SIX_v24_low5_badnone.json')['results'];bad=[x for x in source if Fraction(x['bound'])>=1];keys={canonical6({int(t):n for t,n in x['counts'].items()}) for x in bad};seen={};raw=covered=0
 for x in bad:
  ns={int(t):n for t,n in x['counts'].items()}
  for c in (2,3,4):
   for nc in extensions(ns,c):
    raw+=1
    if canonical6(drop_x(nc)) not in keys:covered+=1;continue
    key=canonical7(nc)
    if key not in seen:seen[key]=dict(counts=nc,source_group=x['group'],codegree=c)
 print('generated',raw,'covered',covered,'orbits',len(seen),'seconds',time.perf_counter()-start,flush=True)
 out=[]
 for j,x in enumerate(seen.values()):
  e=SubsetEngine(24,7,x['counts']);z=e.verify(e.solve());z.update(group=j,source_group=x['source_group'],codegree=x['codegree']);out.append(z)
  if len(out)%50==0:print('DP',len(out),sum(z['bound']<1 for z in out),time.perf_counter()-start,flush=True)
  if len(out)%20==0 or len(out)==len(seen):
   (HERE/'FIVE_LOW_NONUNIT_HIGH.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=len(out)==len(seen),raw=raw,covered_by_other_projection=covered,orbits=len(seen),elapsed=time.perf_counter()-start,results=out)),indent=2)+'\n')
