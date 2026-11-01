from itertools import combinations
from collections import Counter
from time import process_time
from pathlib import Path
import json,sys
P=Path(__file__).resolve().parent
U=int(sys.argv[1]) if len(sys.argv)>1 else 7; restrict='--r13' in sys.argv
start=process_time();A=list(combinations(range(5),2))+list(combinations(range(5),3));caps=[2,2,2,4*U-22]
if restrict:A=[e for e in A if sum(z<3 for z in e)<=1]
seen={()};todo=[()]
while todo:
 t=todo.pop();s=[sum(len(e)-1 for e in t if z in e) for z in range(4)]
 for e in A:
  if any(s[z]+len(e)-1>caps[z] for z in e if z<4):continue
  nt=tuple(sorted(t+(e,)))
  if nt not in seen:seen.add(nt);todo.append(nt)
rows=[]
for t in sorted(seen):
 c=Counter(z for e in t for z in e);K=21-U+sum(len(e)-1 for e in t)
 if c[3]>U-1:continue
 lowhigh=sum(len(e)-1 for e in t if 4 in e)
 lo=max(7,1+c[4],(22+lowhigh+3)//4)
 if lo>K:continue
 r13=not any(sum(z<3 for z in e)>=2 for e in t)
 rows.append((t,lo,K,r13))
out={'inventories':len(rows),'keys':sum(hi-lo+1 for t,lo,hi,r in rows),'r13_inventories':sum(r for t,lo,hi,r in rows),'r13_keys':sum(hi-lo+1 for t,lo,hi,r in rows if r),'cpu_seconds':process_time()-start}
(P/('DOMAIN_PROFILE_U'+str(U)+('_R13' if restrict else '')+'.json')).write_text(json.dumps(out,indent=2)+'\n');(P/('DOMAIN_U'+str(U)+('_R13' if restrict else '')+'.json')).write_text(json.dumps(rows)+'\n');print(json.dumps(out))
