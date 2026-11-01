"""Independent exhaustive FULL-cell minimization, with integer-scaled weights.
Unlike verify.py, this enumerates the core variable too and uses no core-fill formula.
"""
import importlib.util,itertools,json,time,math
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('original',ROOT/'propertyB_small_k/propertyB_m6_certificate.py');c=importlib.util.module_from_spec(sp);sp.loader.exec_module(c);c.M=65
rows=json.loads((OUT/'V37_THREE.json').read_text())['rows'];start=time.process_time();vectors=0;centers=0
results=[]
for row in rows:
 v=37;pos=tuple(row['best_positions']);ds=row['ordered_degrees']
 if row['tri']:ell={0:67-sum(ds),1:ds[0]-1,2:ds[1]-1,4:ds[2]-1,7:1}
 else:ell={0:68-sum(ds),1:ds[0]-2,2:ds[1]-2,4:ds[2]-2,3:1,5:1,6:1}
 delh={};detail=[]
 for j,h in enumerate(pos):
  bit=1<<j;typs=sorted(T for T,n in ell.items() if n and T&bit);cells=[]
  for T,U in itertools.combinations_with_replacement(typs,2):
   cap=math.comb(ell[T],2) if T==U else ell[T]*ell[U]
   if cap:cells.append((T|U,cap,c.weight(v,pos,h,T,U)+c.weight(v,pos,h,U,T)))
  scale=math.lcm(*(w.denominator for _,_,w in cells));cost=[int(w*scale) for _,_,w in cells]
  quotas=[]
  for R in range(8):
   if R&bit:continue
   f=sum(n for T,n in ell.items() if T&bit and not T&R)
   q=max(0,-(-(5*f-(v-1-R.bit_count()))//4))
   idx=[i for i,(mask,_,_) in enumerate(cells) if not mask&R]
   quotas.append((q,idx))
  best=None;witness=None
  for z in itertools.product(*(range(cap+1) for _,cap,_ in cells)):
   vectors+=1
   value=sum(a*b for a,b in zip(z,cost))
   if best is not None and value>=best:continue
   if all(sum(z[i] for i in idx)>=q for q,idx in quotas):best=value;witness=z
  assert best is not None
  d=F(best,scale);delh[h]=d;centers+=1;detail.append(dict(h=h,D=str(d),minimizer=witness))
 total=F(0)
 for h in range(1,38):
  a=sum(n*c.endpoint(v,pos,h,T,True) for T,n in ell.items());b=sum(n*c.endpoint(v,pos,h,T,False) for T,n in ell.items())
  q=sum(n*(m-(T==U))*c.weight(v,pos,h,T,U) for T,n in ell.items() for U,m in ell.items())
  assert q>=delh.get(h,0)
  total+=min(a,b,q-delh.get(h,0))
 assert str(total)==row['U'] and total<1
 results.append(dict(degrees=row['degrees'],tri=row['tri'],ordered_degrees=ds,positions=pos,U=str(total),centers=detail))
result=dict(status='PASS',profiles=len(results),centers=centers,full_integer_vectors=vectors,cpu_seconds=time.process_time()-start,arithmetic='integer-scaled exhaustive objective; Fraction final bounds',rows=results)
(OUT/'REPLAY_V37.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
