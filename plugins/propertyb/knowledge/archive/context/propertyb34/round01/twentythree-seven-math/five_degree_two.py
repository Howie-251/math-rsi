from pathlib import Path
import sys,time,json
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[4]
sys.path[:0]=[str(ROOT/'context/propertyb34-hour1-20261013/low-math'),str(ROOT/'context/propertyb34/round01/high-math')]
from five_general import *
from subset_position_dp import SubsetEngine
HERE=Path(__file__).resolve().parent
pairs=list(combinations(range(5),2));pidx={e:i for i,e in enumerate(pairs)};perms=list(permutations(range(5)))
edgemaps=[[pidx[tuple(sorted((p[i],p[j])))] for i,j in pairs] for p in perms]
pmaps=[{t:sum(1<<p[i] for i in range(5) if t&(1<<i)) for t in range(32)} for p in perms]
fourmaps=[{t:sum(1<<p[i] for i in range(4) if t&(1<<i)) for t in range(16)} for p in permutations(range(4))]
def orbit(ns,maps):return min(tuple(sorted((mp[t],c) for t,c in ns.items() if c)) for mp in maps)
allowed={orbit({int(t):n for t,n in r['counts'].items()},fourmaps) for r in json.loads((HERE/'FOUR_RESIDUES.json').read_text())['cases']}
def survives(ns):
 for sub in combinations(range(5),4):
  p={}
  for t,n in ns.items():
   mask=sum(1<<j for j,i in enumerate(sub) if t&(1<<i));p[mask]=p.get(mask,0)+n
  if orbit(p,fourmaps) not in allowed:return False
 return True
graphs=set();labels=0
def rec(j,weights,ds):
 global labels
 if j==10:
  labels+=1;graphs.add(min(tuple(weights[k] for k in mp) for mp in edgemaps));return
 a,b=pairs[j]
 for w in range(min(2-ds[a],2-ds[b])+1):
  nd=ds.copy();nd[a]+=w;nd[b]+=w;rec(j+1,weights+[w],nd)
rec(0,[],[0]*5);print('graph_labels',labels,'orbits',len(graphs),flush=True)
start=time.time();out=[];seen=set();scanned=0;complete=True
for graph,weights in enumerate(sorted(graphs)):
 ls=tuple(1+w for w in weights);gc=0
 for ns in profiles(5,(7,)*5,ls):
  scanned+=1
  if not survives(ns):continue
  key=orbit(ns,pmaps)
  if key in seen:continue
  seen.add(key);z=SubsetEngine(23,5,ns).solve();r=calc_counts(23,(7,)*5,ns,z['positions']);assert z['bound']==r['bound'];r['graph']=graph;r['weights']=weights;out.append(r);gc+=1
  if time.time()-start>90:complete=False;break
 print('graph',graph,'weights',weights,'profiles',gc,'strict',sum(r['bound']<1 for r in out if r['graph']==graph),'sec',time.time()-start,flush=True)
 if not complete:break
(HERE/'FIVE_DEGREE_TWO.json').write_text(json.dumps(json_value(dict(cases=out,graphs=[list(w) for w in sorted(graphs)],graph_labels=labels,scanned=scanned,complete=complete,seconds=time.time()-start)),indent=2))
