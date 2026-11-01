"""Complete small unit-neighbour pair gates; necessary shared three-neighbour domains and a few full-DP witnesses per degree pattern."""
from pathlib import Path
import sys,itertools,json,time
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).parent
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/twentyone-delta5')]
from star_low import recover,parts,SubsetEngine,json_value
from pilot import triple
HERE=Path(__file__).parent
PATTERNS={6:[(6,7,7),(6,8,8),(6,8,9),(6,9,9),(7,7,7),(7,7,8),(7,8,8),(8,8,8),(8,8,9),(8,9,9),(9,9,9)],7:[(7,8,8),(7,8,9),(7,9,9),(8,8,8),(8,8,9),(8,9,9),(9,9,9)]}

def main():
 st=time.time();gates=[]
 for center in (6,7):
  for a in range(center,11):
   for b in range(a,11):
    for c in range(1,a+1):
     for t in (0,1):
      ns=triple(21,[center,a,b],[1,1,c],t)
      if min(ns.values())<0:continue
      eng=SubsetEngine(21,3,ns);z=eng.verify(eng.solve());z.update(degrees=[center,a,b],codegrees=[1,1,c],triple=t,strict=z['bound']<1);gates.append(z)
 (HERE/'UNIT_PAIRS.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=gates,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('gates',len(gates),'strict',sum(z['strict'] for z in gates),'seconds',time.time()-st,flush=True)
 lookup={(r['degrees'][0],tuple(r['degrees'][1:]),r['codegrees'][2],r['triple']):r['strict'] for r in gates};dom=[];witnesses=[]
 for center,patterns in PATTERNS.items():
  for ds in patterns:
   pr=list(itertools.combinations(range(3),2));allowed=[]
   for i,j in pr:allowed.append(sorted({r['codegrees'][2] for r in gates if r['degrees']==[center,ds[i],ds[j]] and not r['strict']}))
   local=[]
   for ps in itertools.product(*allowed):
    if any(sum(c-1 for ij,c in zip(pr,ps) if i in ij)>4*d-20 for i,d in enumerate(ds)):continue
    for pp in parts(3):
     if any(lookup[(center,tuple(ds[i] for i in ij),c,int(any(all(i in b for i in ij) for b in pp)))] for ij,c in zip(pr,ps)):continue
     for t in range(min(ps)+1):
      ns=recover(center,ds,ps,pp,{7:t})
      if ns is not None:local.append(dict(center_degree=center,neighbor_degrees=ds,neighbor_codegrees=ps,center_partition=pp,neighbor_triple=t,counts=ns))
   start=len(dom);dom.extend(local);selected=sorted(set(round(i*(len(local)-1)/9) for i in range(10))) if local else []
   for i in selected:
    r=local[i];eng=SubsetEngine(21,4,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(strict=z['bound']<1,source_id=start+i);witnesses.append(z)
   rr=[z for z in witnesses if z['center_degree']==center and tuple(z['neighbor_degrees'])==ds];print(center,ds,'domain',len(local),'pilot',len(rr),'strict',sum(z['strict'] for z in rr),'max',max((z['bound'] for z in rr),default=None),flush=True)
   assert time.time()-st<55
 (HERE/'STAR_THREE_DOMAIN.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=dom)),indent=2)+'\n');(HERE/'STAR_THREE_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=False,cases=witnesses,elapsed_seconds=time.time()-st)),indent=2)+'\n');print('seconds',time.time()-st)
if __name__=='__main__':main()
