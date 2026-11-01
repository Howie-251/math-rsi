from pathlib import Path
from itertools import permutations,combinations
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import calc_counts,json_value
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent
base=json.loads((HERE/'SIX_RESIDUES.json').read_text())['cases']
def partitions(ns,left=63,chosen=()):
 if not left:
  zero=8-len(chosen)
  if ns.get(0,0)>=zero:
   cs={};split={t:1 for t in chosen};split[0]=zero
   for t,n in ns.items():
    a=split.get(t,0)
    if n-a:cs[t]=n-a
    if a:cs[t|64]=a
   yield cs
  return
 b=left&-left
 for t,n in ns.items():
  if t&b and not t&~left and t.bit_count()<=4 and n:
   yield from partitions(ns,left^t,chosen+(t,))
start=time.time();out=[];seen=set();complete=True
for r in base:
 ns={int(t):n for t,n in r['counts'].items() if n}
 ws=[sum(n for t,n in ns.items() if t&(1<<a) and t&(1<<b))-1 for a,b in combinations(range(6),2)]
 if sum(ws)!=6:continue
 autom=[]
 for p in permutations(range(6)):
  if all(ws[j]==sum(n for t,n in ns.items() if t&(1<<p[a]) and t&(1<<p[b]))-1 for j,(a,b) in enumerate(combinations(range(6),2))):
   autom.append(tuple(sum(1<<p[i] for i in range(7) if t&(1<<i)) for t in range(128)) if False else tuple(sum(1<<p[i] for i in range(6) if t&(1<<i))+(t&64) for t in range(128)))
 ncase=0
 for cs in partitions(ns):
  key=min(tuple(sorted((mp[t],n) for t,n in cs.items())) for mp in autom)
  if key in seen:continue
  seen.add(key);ncase+=1;z=SubsetEngine(23,7,cs).solve();c=calc_counts(23,(7,7,7,7,7,7,8),cs,z['positions']);assert c['bound']==z['bound'];c['parent']=r['index'];out.append(c)
  if time.time()-start>180:complete=False;break
 print('parent',r['index'],'admit',ncase,'total',len(out),'strict',sum(z['bound']<1 for z in out),'seconds',time.time()-start,flush=True)
 if not complete:break
(HERE/'EQUALITY_SEVEN.json').write_text(json.dumps(json_value(dict(cases=out,complete=complete,seconds=time.time()-start)),indent=2))
