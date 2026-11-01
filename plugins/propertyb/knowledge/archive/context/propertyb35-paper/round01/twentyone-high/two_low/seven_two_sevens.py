"""Two actual sixes, two sevens and three eights: shared six-lock residual views, full necessary completion."""
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
 return {m:sum(n for t,n in ns.items() if t&m==m) for m in range(1,64)}
def lift(inc,S):return {sum(1<<S[i] for i in range(6) if m>>i&1):v for m,v in inc.items()}
def recover(inc):
 out={}
 for m in sorted(range(128),key=int.bit_count,reverse=True):out[m]=inc[m]-sum(v for u,v in out.items() if u&m==m)
 return out if min(out.values())>=0 else None

def main():
 st=time.time();src=json.loads((HERE/'SIX_7788_DP.json').read_text())['cases'];dom=[];out=[];joins={}
 for c in (1,2):
  rows=[moments(r) for r in src if r['center_codegree']==c and not r['strict']];options=[[lift(r,(0,1,2,3)+S) for r in rows] for S in combinations(range(4,7),2)];njoin=0
  def rec(i,inc):
   if i==len(options):yield inc;return
   for vals in options[i]:
    if all(inc.get(k,v)==v for k,v in vals.items()):yield from rec(i+1,inc|vals)
  for inc in rec(0,{}):
   njoin+=1;missing=sorted(set(range(1,128))-set(inc));assert len(missing)==16
   caps=[]
   for m in missing:
    upper=min((inc[u] for u in inc if u&m==u),default=35)
    if m.bit_count()==5:upper=min(upper,1)
    if m.bit_count()>5:upper=0
    caps.append(range(upper+1))
   for vals in product(*caps):
    ns=recover({0:35}|inc|dict(zip(missing,vals)))
    if ns is not None:dom.append(dict(degrees=[6,6,7,7,8,8,8],center_codegree=c,counts=ns))
  joins[c]=njoin
 (HERE/'SEVEN_77888_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,joins=joins,cases=dom)),indent=2)+'\n');print('domain',len(dom),'joins',joins,flush=True)
 if len(dom)>500:print('Stop: domain>500');return
 for i,r in enumerate(dom):
  eng=SubsetEngine(21,7,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(strict=z['bound']<1,source_id=i);out.append(z)
 for c in (1,2):
  rr=[r for r in out if r['center_codegree']==c];print(c,'cases',len(rr),'strict',sum(r['strict'] for r in rr),'max',max((r['bound'] for r in rr),default=None),flush=True)
 (HERE/'SEVEN_77888_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
