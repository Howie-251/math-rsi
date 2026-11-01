from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
def ways(n,k):return comb(n,k)*factorial(k) if 0<=k<=n else 0
def calc(ns,pos):
 s=len(pos);N=21-s;rows=[]
 for k in range(1,22):
  center=sum(1<<i for i,p in enumerate(pos) if p==k);free=not center
  before=sum(1<<i for i,p in enumerate(pos) if p<k)
  after=sum(1<<i for i,p in enumerate(pos) if p>k)
  a=k-1-sum(p<k for p in pos);b=21-k-sum(p>k for p in pos)
  def prob(left,right):
   demand=left+right+int(free)
   if min(left,right)<0 or demand>N:return F(0)
   return F(ways(a,left)*ways(b,right),factorial(N)//factorial(N-demand))
  L=[];R=[];A=F(0);B=F(0);C=F(0)
  for m,n in ns.items():
   r=5-m.bit_count()
   if free:
    first=m&~before==0 and r>0;last=m&~after==0 and r>0
   else:
    first=(m&center)==center and (m^center)&~before==0
    last=(m&center)==center and (m^center)&~after==0
   if first:L.append((m,n,r));A+=n*(r if free else 1)*prob(r-int(free),0)
   if last:R.append((m,n,r));B+=n*(r if free else 1)*prob(0,r-int(free))
  for m,n,r in L:
   for u,z,q in R:
    assert m&u==center
    multiplicity=n*z-(n if m==u else 0)
    C+=multiplicity*prob(r-int(free),q-int(free))
  rows.append({'A':A,'B':B,'C':C,'bound':min(A,B,C)})
 return rows
checked=[];strict=[]
for filename in ('FULL.json','ACTUAL_A3_TRIPLES.json','ACTUAL_A3_TAIL.json','REFINE.json'):
 data=json.loads((P/filename).read_text())
 for r in data['cases']:
  if filename=='REFINE.json' and r['degrees']!=[6,9]:continue
  ns={int(m):n for m,n in r['counts'].items()};assert sum(ns.values())==35
  assert Counter(r['original35_trace_masks'])==Counter({m:n for m,n in ns.items() if n})
  assert [sum(n for m,n in ns.items() if m>>i&1) for i in range(len(r['degrees']))]==r['degrees']
  row=calc(ns,r['best_positions']);v=sum((z['bound'] for z in row),F(0))
  assert v==F(r['best_bound']) and (v<1)==r['strict']
  selected=next(z for z in r['layouts'] if z['positions']==r['best_positions'])
  if 'rows' in selected:
   for a,b in zip(row,selected['rows']):
    assert all(a[key]==F(b[key]) for key in ('A','B','C','bound'))
  checked.append({'source':filename,'degrees':r['degrees'],'codegree':r.get('codegree'),
    'triple':r.get('triple'),'bound':str(v),'strict':v<1})
  if filename=='FULL.json' and v<1:strict.append(v)
assert len(checked)==125
assert sum(r['strict'] for r in checked if r['source']=='FULL.json')==110
out={'status':'PASS','implementation':'independent binomial/factorial type aggregation; no injection-row or DP imports',
 'checked_best_layouts':len(checked),'checked_ABC_rows':21*len(checked),'generic_pair_domain':118,
 'generic_strict':110,'maximum_generic_strict_bound':str(max(strict)),
 'checked':checked,'cpu_seconds':time.process_time()-st}
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checked'},indent=2))
