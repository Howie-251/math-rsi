from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import *
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent
base=json.loads((HERE/'SEVEN_UNIT_FIVE.json').read_text())['cases'];joint=json.loads((HERE/'SEVEN_UNIT_FIVE_JOINT.json').read_text())['results'];remaining={z['graph'] for z in joint if Fraction(z['bound'])>=1}
pmaps=[{t:sum(1<<p[i] for i in range(5) if t&(1<<i)) for t in range(32)} for p in [(0,)+q for q in permutations((1,2,3,4))]]
def orbit(ns):return min(tuple(sorted((mp[t],c) for t,c in ns.items() if c)) for mp in pmaps)
allowed={orbit({int(t):n for t,n in base[j]['counts'].items()}) for j in remaining}
def survives(ns):
 for us in combinations(range(1,6),4):
  sub=(0,)+us;p={}
  for t,n in ns.items():
   mask=sum(1<<j for j,i in enumerate(sub) if t&(1<<i));p[mask]=p.get(mask,0)+n
  if orbit(p) not in allowed:return False
 return True
start=time.time();out=[];scanned=0;complete=True
for ns in profiles(5,(8,)*5,(2,)*10):
 split={0:4,3:1,12:1,16:1}
 if any(ns.get(t,0)<c for t,c in split.items()):continue
 scanned+=1;cs={}
 for t,c in ns.items():
  a=split.get(t,0)
  if c-a:cs[t<<1]=c-a
  if a:cs[(t<<1)|1]=a
 if not survives(cs):continue
 z=SubsetEngine(21,6,cs).solve();r=calc_counts(21,(7,8,8,8,8,8),cs,z['positions']);assert z['bound']==r['bound'];out.append(r)
 if len(out)%25==0:print('done',len(out),'strict',sum(t['bound']<1 for t in out),'sec',time.time()-start,flush=True)
 if time.time()-start>90:complete=False;break
(HERE/'UNIQUE_SEVEN_SIX.json').write_text(json.dumps(json_value(dict(cases=out,scanned=scanned,complete=complete,seconds=time.time()-start)),indent=2))
print('strict',sum(r['bound']<1 for r in out),'/',len(out),'scanned',scanned,'complete',complete,'seconds',time.time()-start)
