from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import *
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent
source=json.loads((HERE/'THREE_SEVEN_TWO_EIGHT.json').read_text())['cases'];indices=[1355,1356,1358]
perms=[a+b for a in permutations(range(3)) for b in permutations((3,4))]
maps=[{t:sum(1<<p[i] for i in range(5) if t&(1<<i)) for t in range(32)} for p in perms]
def orbit(ns):return min(tuple(sorted((move[t],c) for t,c in ns.items() if c)) for move in maps)
allowed={orbit({int(t):n for t,n in source[j]['counts'].items()}) for j in indices}
def extensions(ns):
 ts=sorted((t for t,n in ns.items() if t and n),key=lambda t:-t.bit_count());wanted=[1,1,1,2,2]
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
 for uv in combinations((3,4,5),2):
  sub=(0,1,2)+uv;p={}
  for t,n in ns.items():
   mask=sum(1<<j for j,i in enumerate(sub) if t&(1<<i));p[mask]=p.get(mask,0)+n
  if orbit(p) not in allowed:return False
 return True
start=time.time();out=[];scanned=0
for idx in indices:
 for ns in extensions({int(t):n for t,n in source[idx]['counts'].items() if n}):
  scanned+=1
  if not survives(ns):continue
  z=SubsetEngine(21,6,ns).solve();r=calc_counts(21,(7,7,7,8,8,8),ns,z['positions']);assert z['bound']==r['bound'];r['base_index']=idx;out.append(r)
  print(idx,len(out)-1,r['bound'],flush=True)
(HERE/'THREE_SEVEN_THREE_EIGHT.json').write_text(json.dumps(json_value(dict(cases=out,scanned=scanned,seconds=time.time()-start)),indent=2))
print('strict',sum(r['bound']<1 for r in out),'/',len(out),'scanned',scanned,'seconds',time.time()-start)
