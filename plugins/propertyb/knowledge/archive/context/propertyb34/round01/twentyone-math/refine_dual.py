from pathlib import Path
from fractions import Fraction
from itertools import permutations
import sys,json,time
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'computations'),str(ROOT/'computations/propertyb33/round01')]
from multilock import *
from avoided_lock_quotas import certificate

def dual(p,i):
 s=len(p.positions);bit=1<<i
 qs=[max(0,(4*sum(c for t,c in p.counts.items() if t&bit and not t&R)-(p.v-1-R.bit_count())+2)//3) for R in range(1<<s) if not R&bit]
 return certificate(p,i) if max(qs)>0 else dict(loss=Fraction(0),dual=[],inventory=[],note='all quota zero')

def refine(r):
 ns={int(t):n for t,n in r['counts'].items()};s=len(r['ds']);opts=[];poses=[tuple(r['pos'])]+[p for k in [8,9,7,10,11] for p in permutations(range(k,k+s))]
 for pos in dict.fromkeys(poses):
  p=Profile(r['v'],5,pos,ns);cs=[dual(p,i) for i in range(s)];rr=rows(p,deductions={pos[i]:cs[i]['loss'] for i in range(s)})
  z=dict(r,pos=pos,counts=ns,cs=cs,rows=rr,bound=total_bound(rr));opts.append(z)
  if z['bound']<1:break
 return min(opts,key=lambda z:z['bound'])
if __name__=='__main__':
 source=Path(sys.argv[1]);out=[];start=time.time()
 for i,r in enumerate(json.loads(source.read_text())['cases']):
  if Fraction(r['bound'])<1:out.append(r);continue
  z=refine(r);out.append(z);print(i,r['bound'],'->',z['bound'],flush=True)
  if time.time()-start>180:break
 source.with_name(source.stem+'_DUAL.json').write_text(json.dumps(json_value(dict(cases=out,seconds=time.time()-start)),indent=2))
 print('complete',len(out),'seconds',time.time()-start)
