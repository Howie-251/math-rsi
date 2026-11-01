"""Two actual six-degree locks, lambda1/2, plus two actual degree7/8 locks: common four-lock census."""
from pathlib import Path
from itertools import product, combinations
from fractions import Fraction
import sys,json,time,argparse
HERE=Path(__file__).parent;BASE=HERE.parent;ROOT=HERE.parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine

def serial(v):
 if isinstance(v,Fraction):return str(v)
 if isinstance(v,dict):return {k:serial(w) for k,w in v.items()}
 if isinstance(v,(list,tuple)):return [serial(w) for w in v]
 return v

def recover(ds,pair,triples,q):
 inc={0:35}|{1<<i:d for i,d in enumerate(ds)}|{sum(1<<i for i in ij):v for ij,v in pair.items()}|{sum(1<<i for i in ij):v for ij,v in zip(combinations(range(4),3),triples)}|{15:q}
 ns={m:sum((-1)**(u.bit_count()-m.bit_count())*v for u,v in inc.items() if u&m==m) for m in range(16)}
 return ns if min(ns.values())>=0 else None

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--pilot',type=int,default=0);args=parser.parse_args();st=time.time()
 prev=json.loads((BASE/'TWO_SIXES_TRIPLES.json').read_text())['cases'];allowed={}
 for r in prev:
  if not r['strict'] and r['codegrees'][0] in (1,2):allowed.setdefault((r['degrees'][2],tuple(r['codegrees'])),set()).add(r['triple'])
 dom=[]
 for a,b,cap in [(7,7,3),(7,8,3),(8,8,4)]:
  for c in (1,2):
   for ax,bx,ay,by in product((1,2),repeat=4):
    opts1=allowed.get((a,(c,*sorted((ax,ay)))),());opts2=allowed.get((b,(c,*sorted((bx,by)))),())
    if not opts1 or not opts2:continue
    for zw in range(1,cap+1):
     pair={(0,1):c,(0,2):ax,(0,3):bx,(1,2):ay,(1,3):by,(2,3):zw}
     for ts in product(opts1,opts2,range(min(ax,bx,zw)+1),range(min(ay,by,zw)+1)):
      for q in range(min(ts)+1):
       ns=recover((6,6,a,b),pair,ts,q)
       if ns is not None:dom.append(dict(degrees=[6,6,a,b],codegrees=list(pair.values()),triples=ts,four=q,counts=ns))
 print('domain',len(dom),flush=True)
 (HERE/'FOUR_DOMAIN.json').write_text(json.dumps(serial(dict(scope=__doc__,complete=True,cases=dom)),indent=2)+'\n')
 selected=list(range(len(dom)))
 if args.pilot:selected=sorted(set(round(i*(len(dom)-1)/(args.pilot-1)) for i in range(args.pilot)))
 old={}
 if not args.pilot and (HERE/'FOUR_PILOT.json').exists():old={r['source_id']:r for r in json.loads((HERE/'FOUR_PILOT.json').read_text())['cases']}
 out=[]
 for i in selected:
  r=dom[i]
  if i in old:z=old[i];z['bound']=Fraction(z['bound'])
  else:
   eng=SubsetEngine(21,4,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(source_id=i,strict=z['bound']<1)
  out.append(z)
 for ds in [(6,6,7,7),(6,6,7,8),(6,6,8,8)]:
  for c in (1,2):
   rr=[r for r in out if tuple(r['degrees'])==ds and r['codegrees'][0]==c];res=[r for r in rr if not r['strict']]
   print(ds,c,'tested',len(rr),'strict',len(rr)-len(res),'residual_mixed_patterns',sorted(set(tuple(r['codegrees'][1:5]) for r in res)),flush=True)
 fname='FOUR_PILOT.json' if args.pilot else 'FOUR_DP.json'
 (HERE/fname).write_text(json.dumps(serial(dict(scope=__doc__,complete=not args.pilot,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st,flush=True)
if __name__=='__main__':main()
