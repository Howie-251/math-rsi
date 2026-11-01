"""Shared five-lock projections for two actual six-degree centers plus a mixed four-point low pool."""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction
import sys,json,time,argparse
HERE=Path(__file__).parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
from four_views import serial
from six_views import moments,lift,recover

def main():
 parser=argparse.ArgumentParser();parser.add_argument('pattern');parser.add_argument('--max-cases',type=int,default=1200);args=parser.parse_args();ds=(6,6)+tuple(map(int,args.pattern));assert len(ds)==6;st=time.time();dom=[];out=[];joins={}
 for c in (1,2):
  options=[]
  for S in [(0,1)+P for P in combinations(range(2,6),3)]:
   pat=''.join(str(ds[i]) for i in S[2:]);f='FIVE_SEVENS_DP.json' if pat=='777' else f'FIVE_{pat}_DP.json';src=json.loads((HERE/f).read_text())['cases'];rows=[moments(r) for r in src if r['center_codegree']==c and not r['strict']];options.append([lift(r,S) for r in rows])
  njoin=0
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
      if ns is not None:dom.append(dict(degrees=ds,center_codegree=c,counts=ns))
  joins[c]=njoin
 (HERE/f'SIX_{args.pattern}_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,joins=joins,cases=dom)),indent=2)+'\n');print('domain',len(dom),'joins',joins,flush=True)
 if len(dom)>args.max_cases:print('Not expanding DP: domain exceeds max-cases',flush=True);return
 for i,r in enumerate(dom):
  eng=SubsetEngine(21,6,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(strict=z['bound']<1,source_id=i);out.append(z)
 for c in (1,2):
  rr=[r for r in out if r['center_codegree']==c];print(c,'cases',len(rr),'strict',sum(r['strict'] for r in rr),'max',max((r['bound'] for r in rr),default=None),flush=True)
  for r in rr:
   if not r['strict']:print('residual',r['source_id'],r['counts'],r['bound'],flush=True)
 (HERE/f'SIX_{args.pattern}_DP.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
