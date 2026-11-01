"""Six minimal-energy seven-lock graphs; a few explicit valid inventories, not a complete catalog."""
from fourlock_pilot import *
GRAPHS={'empty':{},'one':{(0,1):1},'two_matching':{(0,1):1,(2,3):1},'path':{(0,1):1,(1,2):1},'double':{(0,1):2},'three_matching':{(0,1):1,(2,3):1,(4,5):1}}
def profile(edges,blocks):
 pair={(i,j):1+edges.get((i,j),0) for i in range(6) for j in range(i+1,6)}
 ns={m:0 for m in range(64)}
 for block in blocks:
  m=sum(1<<i for i in block);ns[m]+=1
  for ij in itertools.combinations(block,2):pair[ij]-=1
 if min(pair.values())<0:return
 for (i,j),c in pair.items():ns[(1<<i)|(1<<j)]+=c
 for i in range(6):ns[1<<i]=7-sum(c for m,c in ns.items() if m>>i&1)
 ns[0]=35-sum(ns.values())
 if min(ns.values())<0:return
 return ns
def main():
 st=time.time();pos=set()
 seeds=[tuple(range(k,k+6)) for k in range(1,20)]+[(1,2,10,11,12,13),(1,5,9,13,17,21),(6,9,11,13,16,24)]
 for p in seeds:
  for i in range(6):pos.add(p[i:]+p[:i]);pos.add(tuple(reversed(p[i:]+p[:i])))
 out=[]
 for name,edges in GRAPHS.items():
  for blocks in [[],[(0,1,2)],[(0,1,2,3)],[(0,1,2),(3,4,5)]]:
   ns=profile(edges,blocks)
   if ns is None:continue
   z=min((evaluate(24,ns,p) for p in pos),key=lambda z:z['bound'])
   cert=evaluate(24,ns,z['positions'],True)
   out.append(dict(graph=name,extra_weights={str(k):v for k,v in edges.items()},blocks=blocks,counts=ns,bound=z['bound'],strict=z['strict'],positions=z['positions'],rows=cert['rows']))
   print(name,blocks,z['bound'],z['positions'],flush=True)
 (HERE/'SIX_TEMPLATE_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,layout_count=len(pos),elapsed_seconds=time.time()-st,profiles=out)),indent=2)+'\n')
 print('profiles',len(out),'strict',sum(z['strict'] for z in out),'seconds',time.time()-st)
if __name__=='__main__':main()
