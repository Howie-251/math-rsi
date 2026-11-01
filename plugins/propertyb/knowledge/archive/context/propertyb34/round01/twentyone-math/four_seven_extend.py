from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import *
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent

def extensions(ns):
 ts=sorted((t for t,n in ns.items() if t and n),key=lambda t:-t.bit_count())
 def rec(j,left,chosen,cs):
  if j==len(ts):
   if not all(1<=n<=2 for n in cs):return
   if not 0<=left<=ns.get(0,0):return
   c={}
   for t,n in ns.items():
    a=left if t==0 else chosen.get(t,0)
    if n-a:c[t]=n-a
    if a:c[t|16]=a
   yield c;return
  t=ts[j];cap=min(ns[t],left,min(2-cs[i] for i in range(4) if t&(1<<i)))
  for n in range(cap+1):
   chosen[t]=n;cc=[a+n*bool(t&(1<<i)) for i,a in enumerate(cs)]
   yield from rec(j+1,left-n,chosen,cc)
 yield from rec(0,8,{},[0]*4)

start=time.time();out=[];ds=(7,7,7,7,8);complete=True
for orbit,r in enumerate(json.loads((HERE/'FOUR_SEVENS_RESIDUES.json').read_text())['representatives']):
 ns={int(t):n for t,n in r['counts'].items() if n};cnt=0
 for cs in extensions(ns):
  z=SubsetEngine(21,5,cs).solve();rr=calc_counts(21,ds,cs,z['positions']);assert z['bound']==rr['bound'];rr['orbit']=orbit;out.append(rr);cnt+=1
  if time.time()-start>90:complete=False;break
 print('orbit',orbit,'count',cnt,'strict',sum(z['bound']<1 for z in out if z['orbit']==orbit),'seconds',time.time()-start,flush=True)
 if not complete:break
(HERE/'FOUR_SEVEN_EXTEND.json').write_text(json.dumps(json_value(dict(complete=complete,cases=out,seconds=time.time()-start)),indent=2))
print('strict',sum(r['bound']<1 for r in out),'/',len(out),'complete',complete,'seconds',time.time()-start)
