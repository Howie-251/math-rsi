from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import *
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent
start=time.time();out=[];seen=set();scanned=0;complete=True;ds=(7,7,7,8,8)
perms=[a+b for a in permutations(range(3)) for b in permutations((3,4))]
maps=[{t:sum(1<<p[i] for i in range(5) if t&(1<<i)) for t in range(32)} for p in perms]
for aa in product((1,2),repeat=3):
 for bb in product((1,2),repeat=3):
  if bb==(2,2,2):continue
  for uv in [1,2]:
   ls=(aa[0],aa[1],bb[0],bb[0],aa[2],bb[1],bb[1],bb[2],bb[2],uv)
   for ns in profiles(5,ds,ls):
    scanned+=1;key=min(tuple(sorted((move[t],c) for t,c in ns.items() if c)) for move in maps)
    if key in seen:continue
    seen.add(key);z=SubsetEngine(21,5,ns).solve();r=calc_counts(21,ds,ns,z['positions']);assert z['bound']==r['bound'];r['ls']=ls;out.append(r)
    if len(out)%100==0:print('done',len(out),'scanned',scanned,'strict',sum(z['bound']<1 for z in out),'sec',time.time()-start,flush=True)
    if time.time()-start>90:complete=False;break
   if not complete:break
  if not complete:break
 if not complete:break
(HERE/'THREE_SEVEN_TWO_EIGHT.json').write_text(json.dumps(json_value(dict(complete=complete,scanned=scanned,cases=out,seconds=time.time()-start)),indent=2))
print('strict',sum(r['bound']<1 for r in out),'/',len(out),'scanned',scanned,'complete',complete,'seconds',time.time()-start)
