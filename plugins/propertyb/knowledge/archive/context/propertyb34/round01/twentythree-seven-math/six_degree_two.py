from pathlib import Path
import sys,time,json
from itertools import permutations,combinations
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import calc_counts,json_value
from subset_position_dp import SubsetEngine
from fractions import Fraction
HERE=Path(__file__).resolve().parent
base=json.loads((HERE/'FIVE_DEGREE_TWO.json').read_text())['cases'];joint=json.loads((HERE/'FIVE_DEGREE_TWO_JOINT.json').read_text())['results'];remaining={z['graph'] for z in joint if Fraction(z['bound'])>=1}
pmaps=[tuple(sum(1<<p[i] for i in range(5) if t&(1<<i)) for t in range(32)) for p in permutations(range(5))]
def key(ns):return tuple(sorted((t,n) for t,n in ns.items() if n))
allowed=set()
for i in remaining:
 ns={int(t):n for t,n in base[i]['counts'].items() if n}
 for mp in pmaps:allowed.add(tuple(sorted((mp[t],n) for t,n in ns.items())))
subs=list(combinations(range(6),5));projmaps=[tuple(sum(1<<j for j,i in enumerate(sub) if t&(1<<i)) for t in range(64)) for sub in subs]
def survives(ns):
 for mp in projmaps[:-1]:
  p={}
  for t,n in ns.items():p[mp[t]]=p.get(mp[t],0)+n
  if key(p) not in allowed:return False
 return True
# Each old pair weight is lambda-1. Its within-class weighted degree bounds sixth-point excess.
def lifts(ns):
 old=[sum(n for t,n in ns.items() if t&(1<<i) and t&(1<<j))-1 for i,j in combinations(range(5),2)]
 budgets=[2-sum(w for (i,j),w in zip(combinations(range(5),2),old) if v in (i,j)) for v in range(5)]
 lim=[1+b for b in budgets]
 items=sorted([(t,n) for t,n in ns.items() if t and t.bit_count()<=4],key=lambda a:(-a[0].bit_count(),a[0]))
 bits={t:[i for i in range(5) if t&(1<<i)] for t,n in items};suffix=[]
 for j in range(len(items)+1):suffix.append([sum(n for t,n in items[j:] if t&(1<<i)) for i in range(5)])
 chosen={};inc=[0]*5
 def rec(j,used,total):
  if used>7 or total>7:return
  if any(inc[i]>lim[i] or inc[i]+suffix[j][i]<1 for i in range(5)):return
  if j==len(items):
   zero=7-used
   if zero<0 or zero>ns.get(0,0) or min(inc)<1:return
   cs={};chosen[0]=zero
   for t,n in ns.items():
    a=chosen.get(t,0)
    if n-a:cs[t]=n-a
    if a:cs[t|32]=a
   yield cs
   return
  t,n=items[j];bb=bits[t];mx=min(n,7-used,(7-total)//len(bb),*(lim[i]-inc[i] for i in bb))
  for a in range(mx+1):
   chosen[t]=a
   for i in bb:inc[i]+=a
   yield from rec(j+1,used+a,total+a*len(bb))
   for i in bb:inc[i]-=a
  chosen.pop(t,None)
 yield from rec(0,0,0)
start=time.time();out=[];seen=set();scanned=0;complete=True
for idx in sorted(remaining):
 ns={int(t):n for t,n in base[idx]['counts'].items() if n};admit=0
 for cs in lifts(ns):
  scanned+=1
  if not survives(cs):continue
  k=key(cs)
  if k in seen:continue
  seen.add(k);admit+=1
  z=SubsetEngine(23,6,cs).solve();r=calc_counts(23,(7,)*6,cs,z['positions']);assert z['bound']==r['bound'];r['parent']=idx;out.append(r)
  if time.time()-start>150:complete=False;break
 print('parent',idx,'admit',admit,'total',len(out),'strict',sum(r['bound']<1 for r in out),'scanned',scanned,'sec',time.time()-start,flush=True)
 if not complete:break
(HERE/'SIX_DEGREE_TWO.json').write_text(json.dumps(json_value(dict(cases=out,scanned=scanned,complete=complete,seconds=time.time()-start)),indent=2))
