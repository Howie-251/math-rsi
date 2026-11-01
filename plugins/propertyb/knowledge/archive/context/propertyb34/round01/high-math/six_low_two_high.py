"""Complete second-high promotions of the five residual six-low/one-high types.
Both high vertices have degree seven, unit with all lows, mutual codegree 1 or 2.
"""
from pathlib import Path
from itertools import permutations
from fractions import Fraction
import sys,json,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path[:0]=[str(HERE),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value

def extensions(ns,c):
 blocks=sorted(t for t,n in ns.items() if t&63 and n and t.bit_count()<5)
 def rec(left,chosen,xcount):
  if xcount>c:return
  if not left:
   k=c-xcount
   if k>ns.get(64,0):return
   count=len(chosen)+k
   if count>7:return
   nc=ns.copy()
   for t in chosen:nc[t]-=1;nc[t|128]=1
   if k:nc[64]-=k;nc[192]=k
   nc[128]=7-count;nc[0]-=nc[128]
   if min(nc.values())>=0:yield {t:n for t,n in nc.items() if n}
   return
  bit=left&-left
  for t in blocks:
   low=t&63
   if low&bit and low&left==low:yield from rec(left^low,chosen+[t],xcount+int(bool(t&64)))
 yield from rec(63,[],0)

def canonical7(ns):
 return min(tuple(sorted(((t&64)|sum(1<<p[i] for i in range(6) if t&(1<<i)),n) for t,n in ns.items() if n)) for p in permutations(range(6)))

def remove_first_high(ns):
 out={}
 for t,n in ns.items():
  u=(t&63)|((t&128)>>1);out[u]=out.get(u,0)+n
 return out

if __name__=='__main__':
 source=json.loads((HERE/'SIX_EXTENSION_JOINT.json').read_text())['results'];bad=[x for x in source if Fraction(x['bound'])>=1]
 keys={canonical7({int(t):n for t,n in x['counts'].items()}):x for x in bad}
 out=[];start=time.perf_counter()
 for x in bad:
  ns={int(t):n for t,n in x['counts'].items()};cases=[];covered=0;total=0
  for c in (1,2):
   for j,nc in enumerate(extensions(ns,c)):
    total+=1
    if canonical7(remove_first_high(nc)) not in keys:covered+=1;continue
    eng=SubsetEngine(24,8,nc);z=eng.verify(eng.solve());z.update(codegree=c,id=j);cases.append(z)
  out.append(dict(graph=x['graph'],group=x['group'],complete_extensions=total,covered_by_second_high_projection=covered,cases=cases))
  print(x['graph'],x['group'],'total',total,'secondcovered',covered,'8-residues',len(cases),'strict',sum(z['bound']<1 for z in cases),'sec',time.perf_counter()-start,flush=True)
  (HERE/'SIX_LOW_TWO_HIGH.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed=time.perf_counter()-start,complete=len(out)==len(bad),results=out)),indent=2)+'\n')
