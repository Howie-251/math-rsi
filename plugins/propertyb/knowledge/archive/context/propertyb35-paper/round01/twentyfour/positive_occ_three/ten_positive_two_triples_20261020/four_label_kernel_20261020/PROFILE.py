"""Complete four-label capacity domain; no negative-layout generation."""
from itertools import combinations,combinations_with_replacement,permutations
from collections import Counter
from pathlib import Path
import json,time

HERE=Path(__file__).resolve().parent;EDGES=tuple(combinations(range(4),2))

def graphs(cap):
 d=[0]*4;v=[0]*6
 def go(i):
  if i==6:yield tuple(v);return
  a,b=EDGES[i]
  for x in range(min(cap[a]-d[a],cap[b]-d[b])+1):
   v[i]=x;d[a]+=x;d[b]+=x
   yield from go(i+1)
   d[a]-=x;d[b]-=x
 yield from go(0)

def main():
 st=time.process_time();jobs=[];keys=[]
 for n in range(3):
  caps=[c for c in combinations_with_replacement(range(4-n,5),4)
        if sum(c)>=(16,13,10)[n]]
  for cap in caps:
   perms=[p for p in permutations(range(4)) if all(cap[p[i]]==cap[i] for i in range(4))]
   maps=[tuple(EDGES.index(tuple(sorted((p[a],p[b])))) for a,b in EDGES) for p in perms]
   def image(v,mp):
    out=[0]*6
    for i,j in enumerate(mp):out[j]=v[i]
    return tuple(out)
   reps={};labelled=0
   for g in graphs(cap):
    if sum(cap)-sum(g)>16-n:continue
    labelled+=1;key=min(image(g,mp) for mp in maps)
    reps[key]=reps.get(key,0)+1
   for g,mult in sorted(reps.items()):
    assert len({image(g,mp) for mp in maps})==mult
    keys.append(dict(n=n,capacities=cap,graph=g,orbit_size=mult,U=sum(cap)-sum(g)))
   jobs.append(dict(n=n,capacities=cap,group_order=len(perms),labelled=labelled,orbits=len(reps)))
 out=dict(complete=True,domain='n0 capacities4444; n1 sizes3/4 sum>=13; n2 sizes2..4 sum>=10; maxdegree<=capacity; U=sumcapacity-E<=16-n',
          edges=EDGES,jobs=jobs,labelled=sum(j['labelled'] for j in jobs),orbits=len(keys),
          representatives=keys,process_seconds=time.process_time()-st)
 (HERE/'PROFILE.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k!='representatives'},indent=2))

if __name__=='__main__':main()
