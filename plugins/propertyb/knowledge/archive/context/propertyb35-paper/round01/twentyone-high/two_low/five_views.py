"""Same-actual-inclusion joins of the three two-six/two-seven residual views, completed to five locks."""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction
import sys,json,time,argparse
HERE=Path(__file__).parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
from four_views import serial

def moments(r):
 ns={int(t):n for t,n in r['counts'].items()}
 return {m:sum(n for t,n in ns.items() if t&m==m) for m in range(1,16)}
def lift(inc,S):return {sum(1<<S[i] for i in range(4) if m>>i&1):v for m,v in inc.items()}
def recover(inc):
 ns={m:sum((-1)**(u.bit_count()-m.bit_count())*v for u,v in inc.items() if u&m==m) for m in range(32)}
 return ns if min(ns.values())>=0 else None

def main():
 st=time.time();src=json.loads((HERE/'FOUR_DP.json').read_text())['cases'];out=[];dom=[];joins={}
 for c in (1,2):
  rows=[r for r in src if r['degrees']==[6,6,7,7] and r['codegrees'][0]==c and not r['strict']]
  options=[[lift(moments(r),S) for r in rows] for S in [(0,1,2,3),(0,1,2,4),(0,1,3,4)]];njoin=0
  for a,b,d in product(*options):
   if any(a[k]!=v for k,v in b.items() if k in a):continue
   inc=a|b
   if any(inc[k]!=v for k,v in d.items() if k in inc):continue
   inc|=d;njoin+=1
   assert set(inc)==set(range(1,32))-{28,29,30,31}
   for t in range(min(inc[m] for m in (12,20,24))+1):
    for qx in range(min(inc[m] for m in (13,21,25))+1):
     for qy in range(min(inc[m] for m in (14,22,26))+1):
      for full in range(min(1,min(inc[m] for m in (15,23,27)),qx,qy)+1):
       ns=recover({0:35}|inc|{28:t,29:qx,30:qy,31:full})
       if ns is None:continue
       dom.append(dict(degrees=[6,6,7,7,7],center_codegree=c,counts=ns))
  joins[c]=njoin
 (HERE/'FIVE_SEVENS_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,joins=joins,cases=dom)),indent=2)+'\n');print('domain',len(dom),'joins',joins,flush=True)
 for i,r in enumerate(dom):
  eng=SubsetEngine(21,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(strict=z['bound']<1,source_id=i);out.append(z)
 for c in (1,2):
  rr=[r for r in out if r['center_codegree']==c];print(c,'cases',len(rr),'strict',sum(r['strict'] for r in rr),'max',max((r['bound'] for r in rr),default=None),flush=True)
  for r in rr:
   if not r['strict']:print('residual',r['source_id'],r['counts'],r['bound'],flush=True)
 (HERE/'FIVE_SEVENS_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
