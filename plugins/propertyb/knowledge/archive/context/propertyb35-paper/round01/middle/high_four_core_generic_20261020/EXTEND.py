from pathlib import Path
from itertools import product,permutations
import sys,json,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4]
sys.path[:0]=[str(P.parent),str(ROOT/'context/propertyb34/round01/high-math')]
from subset_position_dp import SubsetEngine
from pilot import json_value
st=time.process_time();data=json.loads((P/'FOUR_LOCK.json').read_text());sources=[r for r in data['cases'] if not r['strict']];out=[];domain=[]
for r in sources:
 ns={int(t):n for t,n in r['counts'].items()};ts=[t for t in ns if t]
 maps=[]
 for p in permutations(range(4)):
  mp=[sum(1<<p[i] for i in range(4) if m>>i&1) for m in range(16)]
  if all(ns.get(m,0)==ns.get(mp[m],0) for m in range(16)):maps.append(mp)
 hs=set()
 for vv in product(*(range(min(ns[t],1 if t==15 else 2)+1) for t in ts)):
  hh=[0]*16
  for t,v in zip(ts,vv):hh[t]=v
  hh[0]=6-sum(vv)
  if not 0<=hh[0]<=ns.get(0,0):continue
  margins=[sum(hh[t] for t in ts if t>>i&1) for i in range(4)]
  if any(v not in (1,2) for v in margins):continue
  hs.add(tuple(hh))
 reps={min(tuple(h[mp[m]] for m in range(16)) for mp in maps) for h in hs}
 domain.append({'source_id':r['id'],'stabilizer_order':len(maps),'labeled_h_keys':[list(h) for h in sorted(hs)],'representative_h_keys':[list(h) for h in sorted(reps)]})
 for h in sorted(reps):
  nn={}
  for t,n in ns.items():
   if n-h[t]:nn[t<<1]=n-h[t]
   if h[t]:nn[(t<<1)|1]=h[t]
  assert sum(nn.values())==35 and all(m.bit_count()<=5 for m in nn) and nn.get(31,0)<=1
  assert [sum(v for m,v in nn.items() if m>>i&1) for i in range(5)]==[6,8,8,8,8]
  e=SubsetEngine(21,5,nn);z=e.verify(e.solve())
  out.append(dict(source_id=r['id'],center_counts=h,counts=nn,positions=z['positions'],bound=z['bound'],strict=z['bound']<1))
  if time.process_time()-st>4.0:raise RuntimeError('bounded pilot CPU exceeded')
 print(r['id'],'labels',len(hs),'orbits',len(reps),'nonstrict',sum(not z['strict'] for z in out),flush=True)
result={'complete':True,'scope':'only two four-lock residuals; real six-center margins1/2, six edges,full5simplecap1, true stabilizers','domain':domain,'cases':out,'nonstrict_ids':[i for i,z in enumerate(out) if not z['strict']],'cpu_seconds':time.process_time()-st}
(P/'EXTENDED.json').write_text(json.dumps(json_value(result),indent=2)+'\n');print({'cpu_seconds':result['cpu_seconds'],'cases':len(out),'nonstrict':len(result['nonstrict_ids'])})
