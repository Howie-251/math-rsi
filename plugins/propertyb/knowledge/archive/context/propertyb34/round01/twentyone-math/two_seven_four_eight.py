from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import *
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent
raw=json.loads((HERE/'TWO_SEVEN_THREE_EIGHT_RESIDUES.json').read_text())['cases'];source=[r for r in raw if r['ls'][4]==1]
perms5=[a+b for a in permutations((0,1)) for b in permutations((2,3,4))];maps5=[{t:sum(1<<p[i] for i in range(5) if t&(1<<i)) for t in range(32)} for p in perms5]
perms6=[a+b for a in permutations((0,1)) for b in permutations((2,3,4,5))];maps6=[{t:sum(1<<p[i] for i in range(6) if t&(1<<i)) for t in range(64)} for p in perms6]
def orbit(ns,maps):return min(tuple(sorted((move[t],c) for t,c in ns.items() if c)) for move in maps)
allowed={orbit({int(t):n for t,n in r['counts'].items()},maps5) for r in source};bases={}
for r in source:
 ns={int(t):n for t,n in r['counts'].items() if n};bases.setdefault(orbit(ns,maps5),(ns,r['ls'][0]))
def extensions(ns):
 ts=sorted((t for t,n in ns.items() if t and n),key=lambda t:-t.bit_count());wanted=[1,1,2,2,2]
 def rec(j,left,chosen,cs):
  if j==len(ts):
   if cs!=wanted or not 0<=left<=ns.get(0,0):return
   c={}
   for t,n in ns.items():
    a=left if t==0 else chosen.get(t,0)
    if n-a:c[t]=n-a
    if a:c[t|32]=a
   yield c;return
  t=ts[j];cap=0 if t.bit_count()==5 else min(ns[t],left,min(wanted[i]-cs[i] for i in range(5) if t&(1<<i)))
  for n in range(cap+1):
   chosen[t]=n;cc=[a+n*bool(t&(1<<i)) for i,a in enumerate(cs)];yield from rec(j+1,left-n,chosen,cc)
 yield from rec(0,8,{},[0]*5)
def survives(ns):
 for xyz in combinations((2,3,4,5),3):
  sub=(0,1)+xyz;p={}
  for t,n in ns.items():
   mask=sum(1<<j for j,i in enumerate(sub) if t&(1<<i));p[mask]=p.get(mask,0)+n
  if orbit(p,maps5) not in allowed:return False
 return True
start=time.time();out=[];seen=set();scanned=0;complete=True
for ns,a in bases.values():
 for cs in extensions(ns):
  scanned+=1
  if not survives(cs):continue
  key=orbit(cs,maps6)
  if key in seen:continue
  seen.add(key);z=SubsetEngine(21,6,cs).solve();r=calc_counts(21,(7,7,8,8,8,8),cs,z['positions']);assert z['bound']==r['bound'];r['xy']=a;out.append(r)
  if len(out)%50==0:print('done',len(out),'strict',sum(t['bound']<1 for t in out),'sec',time.time()-start,flush=True)
  if time.time()-start>90:complete=False;break
 if not complete:break
(HERE/'TWO_SEVEN_FOUR_EIGHT.json').write_text(json.dumps(json_value(dict(cases=out,scanned=scanned,complete=complete,seconds=time.time()-start)),indent=2))
print('strict',sum(r['bound']<1 for r in out),'/',len(out),'scanned',scanned,'complete',complete,'seconds',time.time()-start)
