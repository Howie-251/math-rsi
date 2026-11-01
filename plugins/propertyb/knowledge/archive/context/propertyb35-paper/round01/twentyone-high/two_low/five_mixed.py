"""Same-inclusion joins for two six-degree locks and mixed degree7/8 triples."""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction
import sys,json,time,argparse
HERE=Path(__file__).parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
from four_views import serial
from five_views import moments,lift,recover

def main():
 parser=argparse.ArgumentParser();parser.add_argument('pattern');parser.add_argument('--pilot',type=int,default=0);args=parser.parse_args();ds=(6,6)+tuple(map(int,args.pattern));assert len(ds)==5;st=time.time();src=json.loads((HERE/'FOUR_DP.json').read_text())['cases'];dom=[];out=[];joins={}
 for c in (1,2):
  options=[]
  for S in [(0,1)+P for P in combinations(range(2,5),2)]:
   rows=[r for r in src if tuple(r['degrees'])==tuple(ds[i] for i in S) and r['codegrees'][0]==c and not r['strict']];options.append([lift(moments(r),S) for r in rows])
  njoin=0
  def rec(i,inc):
   if i==len(options):yield inc;return
   for vals in options[i]:
    if all(inc.get(k,v)==v for k,v in vals.items()):yield from rec(i+1,inc|vals)
  for inc in rec(0,{}):
   njoin+=1;assert set(inc)==set(range(1,32))-{28,29,30,31}
   for t in range(min(inc[m] for m in (12,20,24))+1):
    for qx in range(min(t,min(inc[m] for m in (13,21,25)))+1):
     for qy in range(min(t,min(inc[m] for m in (14,22,26)))+1):
      for full in range(min(1,min(inc[m] for m in (15,23,27)),qx,qy)+1):
       ns=recover({0:35}|inc|{28:t,29:qx,30:qy,31:full})
       if ns is not None:dom.append(dict(degrees=ds,center_codegree=c,counts=ns))
  joins[c]=njoin
 (HERE/f'FIVE_{args.pattern}_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,joins=joins,cases=dom)),indent=2)+'\n');print('domain',len(dom),'joins',joins,flush=True)
 selected=list(range(len(dom)))
 if args.pilot:selected=sorted(set(round(i*(len(dom)-1)/(args.pilot-1)) for i in range(args.pilot)))
 for i in selected:
  r=dom[i];eng=SubsetEngine(21,5,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(strict=z['bound']<1,source_id=i);out.append(z)
 for c in (1,2):
  rr=[r for r in out if r['center_codegree']==c];print(c,'cases',len(rr),'strict',sum(r['strict'] for r in rr),'max',max((r['bound'] for r in rr),default=None),flush=True)
 name=f'FIVE_{args.pattern}_'+('PILOT.json' if args.pilot else 'DP.json')
 (HERE/name).write_text(json.dumps(serial(dict(scope=__doc__,complete=not args.pilot,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
