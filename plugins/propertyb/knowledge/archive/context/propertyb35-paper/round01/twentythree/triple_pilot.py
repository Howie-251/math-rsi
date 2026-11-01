"""A low unit neighbour (degree6/7) paired with any degree6..16 unit neighbour."""
from pair_pilot import *
def main():
 st=time.time();out=[];pos=set()
 for q in range(1,22):pos.update(itertools.permutations(range(q,q+3)))
 for p in [(1,2,12),(1,11,12),(1,7,13),(6,12,18)]:pos.update(itertools.permutations(p))
 for a in (6,7):
  for b in range(a,17):
   for c in range(1,a+1):
    for t in (0,1):
     ns=triple(23,[6,a,b],[1,1,c],t)
     if min(ns.values())<0:continue
     z=min((evaluate(23,ns,p) for p in pos),key=lambda z:z['bound'])
     out.append(dict(degrees=[6,a,b],codegrees=[1,1,c],triple=t,counts=ns,positions=z['positions'],bound=z['bound'],strict=z['strict']))
   rr=[z for z in out if z['degrees']==[6,a,b]]
   print(a,b,'strict',sum(z['strict'] for z in rr),'/',len(rr),'residual',[(z['codegrees'][2],z['triple']) for z in rr if not z['strict']],flush=True)
 (HERE/'TRIPLE_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,layout_count=len(pos),elapsed_seconds=time.time()-st,profiles=out)),indent=2)+'\n')
 print('time',time.time()-st)
if __name__=='__main__':main()
