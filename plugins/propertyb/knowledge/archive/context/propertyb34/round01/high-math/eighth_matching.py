"""Complete eighth-lock extensions of the seven-lock matching residues."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
from collections import Counter
import sys,json,time
sys.dont_write_bytecode=True
HERE=Path(__file__).parent;sys.path.insert(0,str(HERE))
from seven_matching import canonical
from subset_position_dp import SubsetEngine
from multilock import json_value

def extensions(ns,n,degree,partner=None):
 blocks=sorted(t for t,c in ns.items() if t and c and t.bit_count()<=4)
 initial=tuple(1+int(i==partner) for i in range(n));new=1<<n
 def visit(rem,picked):
  if sum(picked.values())>degree:return
  if not any(rem):
   nc=ns.copy()
   for t,c in picked.items():nc[t]-=c;nc[t|new]=nc.get(t|new,0)+c
   pure=degree-sum(picked.values());nc[new]=pure;nc[0]-=pure
   if min(nc.values())>=0:yield {t:c for t,c in nc.items() if c}
   return
  i=next(i for i,r in enumerate(rem) if r)
  for t in blocks:
   if not t&(1<<i) or picked[t]>=ns[t]:continue
   inds=[j for j in range(n) if t&(1<<j)]
   if any(not rem[j] for j in inds):continue
   nxt=list(rem)
   for j in inds:nxt[j]-=1
   picked[t]+=1;yield from visit(tuple(nxt),picked);picked[t]-=1
 def unique():
  seen=set()
  for nc in visit(initial,Counter()):
   key=tuple(sorted(nc.items()))
   if key not in seen:seen.add(key);yield nc
 yield from unique()

def graph(ns,n):
 return [(i,j) for i,j in combinations(range(n),2) if sum(c for t,c in ns.items() if t&(1<<i) and t&(1<<j))==2]

if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)>1 else 'q0';start=time.perf_counter()
 if mode=='q0':
  source=json.loads((HERE/'SEVEN_MATCHING_QMAX0_BOUNDS.json').read_text())['results']
  improved=json.loads((HERE/'SEVEN_MATCHING_QMAX0_JOINT.json').read_text())['results']
  done={x['group'] for x in improved if Fraction(x['bound'])<1}
  source=[x for x in source if Fraction(x['bound'])>=1 and x['group'] not in done]
 else:
  source=json.loads((HERE/'SEVEN_HOMOGENEOUS_MATCHING_BOUNDS.json').read_text())['results']
  source=[x for x in source if Fraction(x['bound'])>=1 and 1<=x['low_count']<=3]
 seen={};raw=0;parents=[]
 for x in source:
  ns={int(t):c for t,c in x['counts'].items()};d=[sum(c for t,c in ns.items() if t&(1<<i)) for i in range(7)]
  matched={i for p in graph(ns,7) for i in p}
  for degree in ([6,7] if mode=='q0' else [6]):
   partners=[None]+[i for i in range(7) if i not in matched and d[i]==degree]
   for partner in partners:
    nr=0
    for nc in extensions(ns,7,degree,partner):
     nr+=1;raw+=1;key=canonical(nc,8)
     if key not in seen:seen[key]=dict(counts=dict(key),source_group=x['group'],new_degree=degree,partner=partner)
    parents.append(dict(group=x['group'],new_degree=degree,partner=partner,raw=nr))
 print('generate',mode,'parents',len(source),'raw',raw,'orbits',len(seen),time.perf_counter()-start,flush=True)
 out=[]
 for j,x in enumerate(seen.values()):
  e=SubsetEngine(24,8,x['counts']);z=e.verify(e.solve());z.update(group=j,source_group=x['source_group'],new_degree=x['new_degree'],partner=x['partner']);out.append(z)
  if len(out)%100==0:print(len(out),sum(z['bound']<1 for z in out),time.perf_counter()-start,flush=True)
  if len(out)%100==0 or len(out)==len(seen):
   result=dict(scope=__doc__,mode=mode,complete=len(out)==len(seen),source_groups=[x['group'] for x in source],raw=raw,parents=parents,orbits=len(seen),elapsed=time.perf_counter()-start,results=out)
   (HERE/f'EIGHTH_MATCHING_{mode.upper()}.json').write_text(json.dumps(json_value(result),indent=2)+'\n')
