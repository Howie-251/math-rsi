from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import *
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent

def orbit(ns,s):
 return min(tuple(sorted((sum(1<<pm[i] for i in range(s) if t&(1<<i)),c) for t,c in ns.items() if c)) for pm in permutations(range(s)))
res={orbit({int(t):n for t,n in r['counts'].items()},4) for r in json.loads((HERE/'FOUR_SEVENS_RESIDUES.json').read_text())['representatives']}
def survives(ns):
 for sub in combinations(range(5),4):
  p={}
  for t,n in ns.items():
   mask=sum(1<<j for j,i in enumerate(sub) if t&(1<<i));p[mask]=p.get(mask,0)+n
  if orbit(p,4) not in res:return False
 return True
start=time.time();out=[];scanned=0;complete=True;ds=(7,)*5
for family in ['clique',0,1,2]:
 ls=tuple(1 if family=='clique' or ((i<family)!=(j<family)) else 2 for i,j in combinations(range(5),2))
 for ns in profiles(5,ds,ls):
  scanned+=1
  if not survives(ns):continue
  z=SubsetEngine(21,5,ns).solve();r=calc_counts(21,ds,ns,z['positions']);assert z['bound']==r['bound'];r['family']=family;out.append(r)
  print(family,'index',len(out)-1,r['bound'],flush=True)
  if time.time()-start>90:complete=False;break
 if not complete:break
(HERE/'FIVE_SEVENS.json').write_text(json.dumps(json_value(dict(complete=complete,scanned=scanned,cases=out,seconds=time.time()-start)),indent=2))
print('strict',sum(r['bound']<1 for r in out),'/',len(out),'scanned',scanned,'complete',complete,'seconds',time.time()-start)
