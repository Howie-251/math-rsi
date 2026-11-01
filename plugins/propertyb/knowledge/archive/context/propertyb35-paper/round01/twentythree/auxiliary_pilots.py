"""Eight-degree unit-neighbour pairs and two actual repeated partners in the rare-low-unit domain."""
from pair_pilot import *
def scan(specs,filename,scope):
 pos=set()
 for k in range(1,22):pos.update(itertools.permutations(range(k,k+3)))
 for p in [(1,2,12),(1,11,12),(1,7,13),(6,12,18)]:pos.update(itertools.permutations(p))
 out=[]
 for ds,cs,t in specs:
  ns=triple(23,ds,cs,t)
  if min(ns.values())<0:continue
  z=min((evaluate(23,ns,p) for p in pos),key=lambda z:z['bound'])
  out.append(dict(degrees=ds,codegrees=cs,triple=t,**z))
 (HERE/filename).write_text(json.dumps(json_value(dict(scope=scope,profiles=out)),indent=2)+'\n')
if __name__=='__main__':
 scan([([6,8,8],[1,1,c],t) for c in range(1,9) for t in (0,1)],'EIGHT_PAIR_STAR.json','Actual unit-star neighbour degree8 pair domain')
 scan([(ds,[2,2,c],t) for ds in ([6,6,6],[6,6,7]) for c in (1,2) for t in (0,1,2) if t<=c],'RARE_LOW_DEFECT_TRIPLES.json','Actual x plus its two codegree2 partners in the exactly-two-low-unit branch')
