from pathlib import Path
import sys,time,json
from itertools import permutations,combinations,combinations_with_replacement
from collections import Counter
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import profiles,calc_counts,json_value
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent
pairs=list(combinations(range(6),2));pidx={p:i for i,p in enumerate(pairs)};perms=list(permutations(range(6)))
emaps=[tuple(pidx[tuple(sorted((p[i],p[j])))] for i,j in pairs) for p in perms]
def graphkey(ws):return min(tuple(ws[k] for k in m) for m in emaps)
graphs=set()
for W in (3,4):
 for es in combinations_with_replacement(range(15),W):
  cnt=Counter(es)
  if max(cnt.values())>2:continue
  ws=tuple(cnt[j] for j in range(15));ds=[sum(w for (i,j),w in zip(pairs,ws) if x in (i,j)) for x in range(6)]
  if max(ds)!=3:continue
  graphs.add(graphkey(ws))
print('graphs',len(graphs),flush=True)
allowed4=set();allowed5=set()
for n,filename,out in [(4,'FOUR_RESIDUES',allowed4),(5,'FIVE_DEGREE_TWO',allowed5)]:
 maps=[tuple(sum(1<<p[i] for i in range(n) if t&(1<<i)) for t in range(1<<n)) for p in permutations(range(n))]
 data=json.loads((HERE/(filename+'.json')).read_text())['cases']
 if n==5:
  joint=json.loads((HERE/'FIVE_DEGREE_TWO_JOINT.json').read_text())['results'];ids={z['graph'] for z in joint if __import__('fractions').Fraction(z['bound'])>=1};data=[r for j,r in enumerate(data) if j in ids]
 for r in data:
  ns={int(t):c for t,c in r['counts'].items() if c}
  for m in maps:out.add(tuple(sorted((m[t],c) for t,c in ns.items())))
def project(ns,sub):
 d={}
 for t,c in ns.items():
  if not c:continue
  k=sum(1<<j for j,i in enumerate(sub) if t&(1<<i));d[k]=d.get(k,0)+c
 return tuple(sorted(d.items()))
start=time.time();out=[];scanned=0;complete=True
for gi,ws in enumerate(sorted(graphs)):
 am=[tuple(sum(1<<p[i] for i in range(6) if t&(1<<i)) for t in range(64)) for p,em in zip(perms,emaps) if tuple(ws[k] for k in em)==ws]
 five_subs=[sub for sub in combinations(range(6),5) if all(sum(ws[pidx[tuple(sorted((i,j)))]] for j in sub if j!=i)<=2 for i in sub)]
 seen=set();gc=0
 for ns in profiles(6,(7,)*6,tuple(1+w for w in ws)):
  scanned+=1
  if any(project(ns,sub) not in allowed4 for sub in combinations(range(6),4)):continue
  if any(project(ns,sub) not in allowed5 for sub in five_subs):continue
  key=min(tuple(sorted((m[t],n) for t,n in ns.items() if n)) for m in am)
  if key in seen:continue
  seen.add(key);gc+=1;z=SubsetEngine(23,6,ns).solve();r=calc_counts(23,(7,)*6,ns,z['positions']);assert z['bound']==r['bound'];r['graph']=gi;r['weights']=ws;out.append(r)
  if time.time()-start>300:complete=False;break
 print('graph',gi,'weights',ws,'cases',gc,'total',len(out),'strict',sum(r['bound']<1 for r in out),'scanned',scanned,'sec',time.time()-start,flush=True)
 if not complete:break
(HERE/'SIX_DEGREE_THREE.json').write_text(json.dumps(json_value(dict(cases=out,graphs=list(sorted(graphs)),scanned=scanned,complete=complete,seconds=time.time()-start)),indent=2))
