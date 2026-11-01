"""Complete four-point domains: three actual degree6 points plus a degree7/8 point, all shared pair/triple data."""
from pathlib import Path
import sys,itertools,json,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path[:0]=[str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations')]
from subset_position_dp import SubsetEngine
from multilock import json_value

def main():
 st=time.time();src=json.loads((HERE/'TWO_SIXES_TRIPLES.json').read_text())['cases'];allow={}
 for r in src:
  if not r['strict'] and r['codegrees'][0]==2:allow.setdefault((r['degrees'][2],tuple(r['codegrees'][1:])),set()).add(r['triple'])
 out=[]
 for d in (7,8):
  for cs in itertools.combinations_with_replacement((1,2),3):
   pair={(i,j):2 for i,j in itertools.combinations(range(3),2)}|{(i,3):cs[i] for i in range(3)};trs=list(itertools.combinations(range(4),3));opts=[(0,1,2)]+[allow[(d,tuple(sorted((cs[i],cs[j]))))] for i,j in itertools.combinations(range(3),2)]
   for ts in itertools.product(*opts):
    for q in range(min(ts)+1):
     inc={0:35}|{1<<i:6 if i<3 else d for i in range(4)}|{sum(1<<i for i in ij):v for ij,v in pair.items()}|{sum(1<<i for i in S):v for S,v in zip(trs,ts)}|{15:q};ns={m:sum((-1)**(u.bit_count()-m.bit_count())*v for u,v in inc.items() if u&m==m) for m in range(16)}
     if min(ns.values())<0:continue
     eng=SubsetEngine(21,4,ns);z=eng.verify(eng.solve());z.update(degrees=[6,6,6,d],codegrees=[pair[ij] for ij in itertools.combinations(range(4),2)],triples=ts,four=q,strict=z['bound']<1);out.append(z)
  rr=[z for z in out if z['degrees'][3]==d];print(d,'domain',len(rr),'strict',sum(z['strict'] for z in rr),'max',max(z['bound'] for z in rr),flush=True)
  for z in rr:
   if not z['strict']:print('residual',z['codegrees'],z['triples'],z['four'],z['bound'])
 (HERE/'THREE_SIXES_FOUR.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st)
if __name__=='__main__':main()
