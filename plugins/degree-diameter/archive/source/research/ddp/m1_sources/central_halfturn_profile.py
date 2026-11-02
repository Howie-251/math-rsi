"""Necessary projected capacity conditions; never a diameter certificate."""
from itertools import combinations_with_replacement
from collections import Counter
from pathlib import Path
import json
P=Path(__file__).resolve().parent

def idx(r,t):return (r%6)*3+(t%3)
def sub(q,p):return idx(q//3-p//3,q%3-p%3)
def caps(c,a,b):
 out=[]
 for q in range(18):
  z=c[q]-(4 if q==0 else 0)
  qa=sub(q,a);qb=sub(q,b)
  z+=(c[qa]-(4 if qa==0 else 0)) if q%3==0 else 2*c[qa]
  z+=c[qb]-(2 if qb==0 else 0)
  if a==b and q==a:z-=1
  out.append(z)
 return out
ans={}
for a,b in [(0,0),(0,9),(9,9)]:
 survivors=[];total=0
 for tail in combinations_with_replacement(range(18),4):
  s=(0,)+tail
  if max(Counter(s).values())>4:continue
  total+=1;c=[0]*18
  for x in s:
   for y in s:c[sub(x,y)]+=1
  if min(caps(c,a,b))>=4 and min(caps(c,b,a))>=4:
   survivors.append(s)
 ans[f'{a//3},{b//3}']={'normalized_projected_multisets_checked':total,'necessary_condition_survivors':len(survivors),'projected_survivors':[[[x//3,x%3] for x in s] for s in survivors]}
print({k:v['necessary_condition_survivors'] for k,v in ans.items()})
(P/'central_halfturn_profile.json').write_text(json.dumps(ans,indent=2)+'\n')
