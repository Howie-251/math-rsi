"""M35/v21 delta5 preliminary unit-star necessary double/triple inputs."""
from pathlib import Path
import sys,itertools,time,json
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/middle'))
from pilot import evaluate,best,double,triple,json_value
from fractions import Fraction as Q

def main():
 st=time.time();pairs=[];triples=[]
 for b in range(5,32):
  z=best(21,double(21,5,b,1),True);pairs.append(dict(degrees=[5,b],codegree=1,**z));print('pair',b,z['bound'],z['positions'],flush=True)
 pos=set()
 for k in range(1,20):pos.update(itertools.permutations(range(k,k+3)))
 for p in [(1,2,11),(1,10,11),(1,6,12),(5,11,17)]:pos.update(itertools.permutations(p))
 for a in range(5,9):
  for b in range(a,9):
   if a+19*b>170:continue
   for c in range(1,a+1):
    for t in (0,1):
     ns=triple(21,[5,a,b],[1,1,c],t)
     if min(ns.values())<0:continue
     z=min((evaluate(21,ns,p) for p in pos),key=lambda z:z['bound'])
     triples.append(dict(degrees=[5,a,b],codegrees=[1,1,c],triple=t,counts=ns,positions=z['positions'],bound=z['bound'],strict=z['strict']))
   rr=[r for r in triples if r['degrees']==[5,a,b]];print('triple',a,b,sum(r['strict'] for r in rr),len(rr),'resid',[(r['codegrees'][2],r['triple']) for r in rr if not r['strict']],flush=True)
 out=dict(scope=__doc__,elapsed_seconds=time.time()-st,pairs=pairs,triples=triples);(HERE/'PILOT.json').write_text(json.dumps(json_value(out),indent=2)+'\n');print('seconds',out['elapsed_seconds'])
if __name__=='__main__':main()
