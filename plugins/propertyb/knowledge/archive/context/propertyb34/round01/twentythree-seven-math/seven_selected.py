from pathlib import Path
from itertools import permutations,combinations,product
from fractions import Fraction
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import calc_counts,json_value
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent
base=json.loads((HERE/'SIX_RESIDUES.json').read_text())['cases'];joint=json.loads((HERE/'SIX_RESIDUES_JOINT.json').read_text())['results'];remaining={z['graph'] for z in joint if Fraction(z['bound'])>=1};base=[dict(r,residual_index=j) for j,r in enumerate(base) if j in remaining]
pairs=list(combinations(range(6),2));pidx={p:i for i,p in enumerate(pairs)}
maps6=[tuple(sum(1<<p[i] for i in range(6) if t&(1<<i)) for t in range(64)) for p in permutations(range(6))]
allowed6=set()
for r in base:
 ns={int(t):n for t,n in r['counts'].items() if n}
 for m in maps6:allowed6.add(tuple(sorted((m[t],n) for t,n in ns.items())))
allowed4=set();maps4=[tuple(sum(1<<p[i] for i in range(4) if t&(1<<i)) for t in range(16)) for p in permutations(range(4))]
for r in json.loads((HERE/'FOUR_RESIDUES.json').read_text())['cases']:
 ns={int(t):n for t,n in r['counts'].items() if n}
 for m in maps4:allowed4.add(tuple(sorted((m[t],n) for t,n in ns.items())))
def project(ns,sub):
 dd={}
 for t,n in ns.items():
  mask=sum(1<<j for j,i in enumerate(sub) if t&(1<<i));dd[mask]=dd.get(mask,0)+n
 return tuple(sorted((t,n) for t,n in dd.items() if n))
def extensions(ws):
 W=sum(ws);ds=[sum(w for (i,j),w in zip(pairs,ws) if x in (i,j)) for x in range(6)]
 for add in product(range(3),repeat=6):
  T=sum(add)
  if T>(36-2*W)//8 or any(T<ds[i]+add[i] for i in range(6)):continue
  ed=dict(zip(pairs,ws));ed.update({(i,6):add[i] for i in range(6)});small=[];ok=True
  for rem in range(6):
   sub=tuple(i for i in range(7) if i!=rem);ww=[ed[tuple(sorted((i,j)))] for i,j in combinations(sub,2)];dw=[sum(ed[tuple(sorted((i,j)))] for j in sub if j!=i) for i in sub];S=sum(ww)
   if S<W or (max(dw)==3 and S<=4):ok=False;break
   if max(dw)<=2:
    if 2 in ww:ok=False;break
    if any(ed[tuple(sorted((i,j)))]==ed[tuple(sorted((j,k)))]==1 and ed[tuple(sorted((i,k)))]==0 for i,j,k in permutations(sub,3)):ok=False;break
    if sorted(dw) not in [[0,0,1,1,1,1],[0,0,0,2,2,2],[1,1,1,1,1,1],[0,1,1,2,2,2],[2,2,2,2,2,2]]:ok=False;break
    small.append(sub)
  if ok:yield add,small

def lifts(ns,target):
 items=sorted([(t,n) for t,n in ns.items() if t and t.bit_count()<=4],key=lambda a:(-a[0].bit_count(),a[0]));bits={t:[i for i in range(6) if t&(1<<i)] for t,n in items};suffix=[]
 for j in range(len(items)+1):suffix.append([sum(n for t,n in items[j:] if t&(1<<i)) for i in range(6)])
 left=list(target);chosen={}
 def rec(j,used):
  if used>7 or any(left[i]<0 or left[i]>suffix[j][i] for i in range(6)):return
  if j==len(items):
   zero=7-used
   if any(left) or zero<0 or zero>ns.get(0,0):return
   cs={};chosen[0]=zero
   for t,n in ns.items():
    a=chosen.get(t,0)
    if n-a:cs[t]=n-a
    if a:cs[t|64]=a
   yield cs;return
  t,n=items[j];bb=bits[t];mx=min(n,7-used,*(left[i] for i in bb))
  for a in range(mx+1):
   chosen[t]=a
   for i in bb:left[i]-=a
   yield from rec(j+1,used+a)
   for i in bb:left[i]+=a
  chosen.pop(t,None)
 yield from rec(0,0)
start=time.time();out=[];scanned=0;complete=True;seen=set()
for r in base:
 ns={int(t):n for t,n in r['counts'].items() if n};ws=tuple(sum(n for t,n in ns.items() if t&(1<<a) and t&(1<<b))-1 for a,b in pairs)
 if sum(ws)==6:continue
 ac=0;graphs=list(extensions(ws))
 for add,small in graphs:
  for cs in lifts(ns,tuple(1+w for w in add)):
   scanned+=1
   if any(project(cs,sub) not in allowed6 for sub in small):continue
   if any(project(cs,sub+(6,)) not in allowed4 for sub in combinations(range(6),3)):continue
   k=tuple(sorted(cs.items()))
   if k in seen:continue
   seen.add(k);ac+=1;z=SubsetEngine(23,7,cs).solve();c=calc_counts(23,(7,)*7,cs,z['positions']);assert c['bound']==z['bound'];c['parent']=r['index'];c['added_weights']=add;out.append(c)
   if time.time()-start>180:complete=False;break
  if not complete:break
 print('parent',r['index'],'graphs',len(graphs),'cases',ac,'total',len(out),'strict',sum(z['bound']<1 for z in out),'scanned',scanned,'seconds',time.time()-start,flush=True)
 if not complete:break
(HERE/'SEVEN_SELECTED.json').write_text(json.dumps(json_value(dict(cases=out,complete=complete,scanned=scanned,seconds=time.time()-start)),indent=2))
