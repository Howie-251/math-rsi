"""Four shared two-six/three-seven residual views, completed to two-six/four-seven six-lock traces."""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction
import sys,json,time
HERE=Path(__file__).parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
from four_views import serial

def moments(r):
 ns={int(t):n for t,n in r['counts'].items()}
 return {m:sum(n for t,n in ns.items() if t&m==m) for m in range(1,32)}
def lift(inc,S):return {sum(1<<S[i] for i in range(5) if m>>i&1):v for m,v in inc.items()}
def recover(inc):
 ns={m:sum((-1)**(u.bit_count()-m.bit_count())*v for u,v in inc.items() if u&m==m) for m in range(64)}
 return ns if min(ns.values())>=0 else None

def main():
 st=time.time();src=json.loads((HERE/'FIVE_SEVENS_DP.json').read_text())['cases'];dom=[];out=[];joins={}
 for c in (1,2):
  rows=[moments(r) for r in src if r['center_codegree']==c and not r['strict']];options=[[lift(r,(0,1)+S) for r in rows] for S in combinations(range(2,6),3)];njoin=0
  def rec(i,inc):
   if i==len(options):yield inc;return
   for vals in options[i]:
    if all(inc.get(k,v)==v for k,v in vals.items()):yield from rec(i+1,inc|vals)
  for inc in rec(0,{}):
   njoin+=1;assert set(inc)==set(range(1,64))-{60,61,62,63}
   for t in range(min(inc[m] for m in (28,44,52,56))+1):
    for qx in range(min(1,t,min(inc[m] for m in (29,45,53,57)))+1):
     for qy in range(min(1,t,min(inc[m] for m in (30,46,54,58)))+1):
      ns=recover({0:35}|inc|{60:t,61:qx,62:qy,63:0})
      if ns is not None:dom.append(dict(degrees=[6,6,7,7,7,7],center_codegree=c,counts=ns))
  joins[c]=njoin
 (HERE/'SIX_SEVENS_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,joins=joins,cases=dom)),indent=2)+'\n');print('domain',len(dom),'joins',joins,flush=True)
 for i,r in enumerate(dom):
  eng=SubsetEngine(21,6,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(strict=z['bound']<1,source_id=i);out.append(z)
 for c in (1,2):
  rr=[r for r in out if r['center_codegree']==c];print(c,'cases',len(rr),'strict',sum(r['strict'] for r in rr),'max',max((r['bound'] for r in rr),default=None),flush=True)
  for r in rr:
   if not r['strict']:print('residual',r['source_id'],r['counts'],r['bound'],flush=True)
 (HERE/'SIX_SEVENS_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
