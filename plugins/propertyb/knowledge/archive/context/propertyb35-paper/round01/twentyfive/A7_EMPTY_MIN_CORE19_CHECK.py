"""Pure star-transition check for a minimum-empty seven-unit core19.
Independently generates stars as all4140 partitions of eight labelled incidences.
No probability/DP call. Checks exact exchanged traces and the analytic21/95 counts.
"""
from pathlib import Path
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();src=json.loads((P/'UNIT7_SCREEN.json').read_text());mu={int(t):n for t,n in next(z['counts'] for z in src['results'] if z['base']==19).items()};C=112
parts={()}
for k in range(8):
 nn=set()
 for pp in parts:
  nn.add(tuple(sorted(pp+(1<<k,))))
  for j,t in enumerate(pp):nn.add(tuple(sorted(pp[:j]+pp[j+1:]+(t|(1<<k),))))
 parts=nn
assert len(parts)==4140
out=[]
for i,expected_original,expected_retained in [(0,231,21),(4,227,95)]:
 labels=list(range(7))+[i];stars=set()
 for pp in parts:
  p=Counter();ok=True
  for t in pp:
   vs=[labels[k] for k in range(8) if t>>k&1]
   if len(vs)!=len(set(vs)):ok=False;break
   mask=sum(1<<v for v in vs)
   if mask.bit_count()>4 or not mu.get(mask):ok=False;break
   p[mask]+=1
  if ok and all(v<=mu[t] for t,v in p.items()) and 0<=7-len(pp)<=mu[0]:stars.add(tuple(sorted(p.items())))
 assert len(stars)==expected_original;retained=[];patterns=Counter()
 for key in stars:
  p=dict(key);r=7-sum(p.values());p[0]=r;s=p.get(1<<i,0);a=p.get(C,0);q=sum(v for t,v in p.items() if t.bit_count()==2);qout=sum(v for t,v in p.items() if t.bit_count()==2 and not t>>i&1)
  assert q+2*a-r==1
  new=Counter()
  for t,n in mu.items():
   old=t&~(1<<i);v=p.get(t,0);new[old]+=n-v;new[old|(1<<i)]+=v
  new={t:n for t,n in new.items() if n};assert new.get(0,0)==6-r+mu[1<<i]-s
  large=[t for t,n in new.items() for _ in range(n) if t.bit_count()>=3]
  valid=new.get(0,0)>=6
  if not valid:continue
  assert not large or len(large)==1 and large[0].bit_count()==3
  assert r+s<=mu[1<<i]
  if not C>>i&1:assert a==0 and qout==0 and r+s==1
  else:assert a+qout<=1
  patterns[(a,qout,s,r,q)]+=1;retained.append(dict(nonempty_star=dict(key),empty_degree=r,single_partner=s,on_old_triple=a,pair_degree=q,pair_not_through_partner=qout,new_empty=new.get(0,0),new_large=large))
 assert len(retained)==expected_retained
 out.append(dict(partner=i,inside_triple=bool(C>>i&1),original_stars=len(stars),retained_stars=len(retained),patterns=[dict(on_triple=k[0],pair_out=k[1],single_partner=k[2],empty_degree=k[3],pair_degree=k[4],multiplicity=n) for k,n in sorted(patterns.items())],stars=retained));print(i,len(stars),len(retained),out[-1]['patterns'],flush=True)
result=dict(scope=__doc__,passed=True,results=out,elapsed_seconds=time.perf_counter()-st)
(P/'A7_EMPTY_MIN_CORE19_CHECK.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(dict(passed=True,elapsed_seconds=result['elapsed_seconds']),indent=2))
