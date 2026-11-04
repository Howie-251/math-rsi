from itertools import combinations,permutations
from collections import Counter
import json
from pathlib import Path
P=Path(__file__).resolve().parent
E=[x for x in range(16) if x.bit_count()%2==0]
tr=[]
for a in E:
 for p in permutations(range(4)):
  tr.append([sum((((x^a)>>i)&1)<<p[i] for i in range(4)) for x in range(16)])
def canon(h,f):return min((tuple(sorted(t[x] for x in h)),tuple(sorted(t[x] for x in f))) for t in tr)
orb=Counter(canon(h,f) for h in combinations(E,6) for f in combinations(h,3))
def pairings(v):
 if not v:yield ();return
 a=v[0]
 for j in range(1,len(v)):
  for tail in pairings(v[1:j]+v[j+1:]):yield ((a,v[j]),)+tail

def solve(F,H,forbid):
 free=sorted(set(H)-set(forbid));blocks=[(v,) for v in free]+list(F);root=free[0];n=len(blocks);dead=set();path=[root]
 def dfs(end,mask):
  if not mask:return (end^root).bit_count()==1
  key=(end,mask)
  if key in dead:return False
  for j,B in enumerate(blocks):
   if not mask>>j&1:continue
   for seq in (B,B[::-1]) if len(B)>1 else (B,):
    if (end^seq[0]).bit_count()==1:
     path.extend(seq)
     if dfs(seq[-1],mask^(1<<j)):return True
     del path[-len(seq):]
  dead.add(key);return False
 return tuple(path) if dfs(root,((1<<n)-1)^1) else None
rows=[]
for (h,f),size in sorted(orb.items()):
 pos=neg=0;examples=[];cert=[]
 for F in pairings(tuple(v for v in range(16) if v not in h)):
  cycle=solve(F,h,f)
  if cycle:pos+=1;cert.append((F,cycle))
  else:
   neg+=1
   if len(examples)<3:examples.append(F)
 rows.append(dict(holes=h,forbidden=f,orbit=size,positive=pos,negative=neg,negative_examples=examples))
 print(rows[-1],flush=True)
(P/'A8_Q4_T63_probe.json').write_text(json.dumps({'status':'EXPLORATION_ONLY','rows':rows},indent=2))
