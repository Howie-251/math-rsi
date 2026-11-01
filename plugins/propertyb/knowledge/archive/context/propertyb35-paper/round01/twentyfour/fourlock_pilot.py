"""Complete four-seven-lock trace domains: unit or exactly one codegree-two pair."""
from pathlib import Path
import sys,time,json,itertools
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/middle'))
from pilot import evaluate,json_value
HERE=Path(__file__).parent

def inventory(s,ds,pairs,M=35):
 hi=sorted([m for m in range(1,1<<s) if m.bit_count()>=3],key=lambda m:-m.bit_count())
 edges=[(i,j) for i in range(s) for j in range(i+1,s)]
 masks=[(1<<i)|(1<<j) for i,j in edges]
 cap=[pairs[i,j] for i,j in edges]
 chosen={}
 def rec(k,rem):
  if k==len(hi):
   ns=dict(chosen)
   ns.update({m:r for m,r in zip(masks,rem)})
   for i,d in enumerate(ds):ns[1<<i]=d-sum(n for m,n in ns.items() if m>>i&1)
   ns[0]=M-sum(ns.values())
   if min(ns.values())>=0:yield {m:ns.get(m,0) for m in range(1<<s)}
   return
  m=hi[k];ids=[j for j,p in enumerate(masks) if p&m==p]
  for n in range(min(rem[j] for j in ids)+1):
   chosen[m]=n; nxt=rem[:]
   for j in ids:nxt[j]-=n
   yield from rec(k+1,nxt)
  del chosen[m]
 yield from rec(0,cap)

def main():
 st=time.time();out=[]
 for conflict in [False,True]:
  pairs={(i,j):1+int(conflict and (i,j)==(0,1)) for i in range(4) for j in range(i+1,4)}
  nslist=list(inventory(4,[7]*4,pairs))
  pos=set()
  for k in range(1,22):
   pos.update(itertools.permutations(range(k,k+4)))
  pos=sorted(pos)
  print('domain',conflict,len(nslist),'layouts',len(pos),flush=True)
  for ns in nslist:
   z=min((evaluate(24,ns,p) for p in pos),key=lambda z:z['bound'])
   out.append(dict(conflict=conflict,counts=ns,positions=z['positions'],bound=z['bound'],strict=z['strict']))
  rr=[z for z in out if z['conflict']==conflict]
  print('result',conflict,sum(z['strict'] for z in rr),len(rr),'max',max(z['bound'] for z in rr),'elapsed',time.time()-st,flush=True)
 (HERE/'FOURLOCK_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed_seconds=time.time()-st,profiles=out)),indent=2)+'\n')
if __name__=='__main__':main()
