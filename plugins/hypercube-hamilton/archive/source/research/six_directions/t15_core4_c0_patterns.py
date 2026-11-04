from pathlib import Path
from itertools import combinations
import json
p=Path(__file__).parent
V=set(range(16));VB=V-{1,2}
def gen(deg):
 if not any(deg):yield ();return
 a=next(v for v,d in enumerate(deg) if d)
 cand=[a^(1<<j) for j in range(4) if deg[a^(1<<j)]]
 for nn in combinations(cand,deg[a]):
  d=deg[:];d[a]=0
  for b in nn:d[b]-=1
  for r in gen(d):yield tuple((a,b) for b in nn)+r
lines=[];count=0
for u,v in combinations(sorted(VB-{3,15}),2):
 if (u^v).bit_count()%2!=1:continue
 da=[int(z not in {u,v}) for z in range(16)]
 db=[(2 if z in {0,7} else 1) if z in VB else 0 for z in range(16)]
 for z in (3,15,u,v):db[z]-=1
 aa=list(gen(da));bb=list(gen(db));count+=1
 lines.append(f'{u} {v} {len(aa)} {len(bb)}')
 for arr in (aa,bb):
  for es in arr:lines.append(str(len(es))+' '+' '.join(str(z) for e in es for z in e))
d=[(2 if z in {0,7} else 1) if z in VB else 0 for z in range(16)]
for z in (3,15):d[z]-=1
bb=list(gen(d));lines.append(str(len(bb)))
for es in bb:lines.append(str(len(es))+' '+' '.join(str(z) for e in es for z in e))
(p/'t15_core4_c0_patterns.txt').write_text(str(count)+'\n'+'\n'.join(lines)+'\n')
print(count,len(bb))
