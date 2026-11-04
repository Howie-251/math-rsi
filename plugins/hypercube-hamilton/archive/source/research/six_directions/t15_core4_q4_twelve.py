import json,itertools
from pathlib import Path
root=Path(__file__).parent
omit={1,2,3,15}; free={0,7}; vs=set(range(16))-omit

def pairings(v):
 if not v: yield (); return
 a=min(v)
 for b in sorted(v-{a}):
  for p in pairings(v-{a,b}): yield ((a,b),)+p

def cycle(m):
 mate={a:b for e in m for a,b in (e,e[::-1])}
 def dfs(path,rem):
  end=path[-1]
  if not rem:return path if (end^path[0]).bit_count()==1 else None
  for j in range(4):
   x=end^(1<<j)
   if x not in rem:continue
   if x in mate:
    z=mate[x]
    if z not in rem:continue
    r=dfs(path+[x,z],rem-{x,z})
   else:r=dfs(path+[x],rem-{x})
   if r:return r
  return None
 return dfs([0],vs-{0})
rec=[]
for m in pairings(vs-free):rec.append({'matching':m,'cycle':cycle(m)})
out={'omitted':sorted(omit),'retained_free':sorted(free),'records':rec,'positive':sum(bool(r['cycle']) for r in rec),'negative':sum(not r['cycle'] for r in rec)}
(root/'t15_core4_q4_twelve_table.json').write_text(json.dumps(out))
print({k:v for k,v in out.items() if k!='records'})
