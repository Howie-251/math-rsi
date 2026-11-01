"""Independent actual-domain audit: restricted growth strings, explicit residual rules, direct Mobius sums.
Does not import either pilot or its partition / stock generator; does not search positions.
"""
from pathlib import Path
from itertools import product,combinations
import json,time
HERE=Path(__file__).parent

def parts(s):
 for a in product(range(s),repeat=s):
  if a[0] or any(a[i]>1+max(a[:i]) for i in range(1,s)):continue
  yield tuple(tuple(i for i in range(s) if a[i]==b) for b in range(max(a)+1))

def canonical(p):return tuple(sorted(tuple(sorted(b)) for b in p))
def restriction(p,tr):return canonical([tuple(tr.index(i) for i in b if i in tr) for b in p if any(i in tr for i in b)])
def residual(ds,p,t):
 singles=len(p)==3
 if ds==(8,8,8):return t==0 and max(map(len,p))<=2
 if ds==(8,8,9):return (singles and t==1) or (canonical(p)==((0,1),(2,)) and t==0)
 if ds==(8,9,9):return singles and t==0
 if ds==(9,9,9):return singles and t in (0,1)
 if ds==(9,9,10):return singles and t==1
 raise ValueError(ds)

def stock(ds,p,ts,q=None):
 s=len(ds);I={0:35};I.update({1<<i:ds[i] for i in range(s)})
 for i,j in combinations(range(s),2):I[(1<<i)|(1<<j)]=2 if min(ds[i],ds[j])==8 else 3
 for tr,t in zip(combinations(range(s),3),ts):I[sum(1<<i for i in tr)]=t
 if s==4:I[15]=q
 J={0:27}
 for m in range(1,1<<s):J[m]=I[m]-int(any(all(not(m>>i&1) or i in b for i in range(s)) for b in p))
 m={T:sum((-1)**(U.bit_count()-T.bit_count())*J[U] for U in range(1<<s) if U&T==T) for T in range(1<<s)}
 ns={T<<1:n for T,n in m.items()};ns[1]=8-len(p)
 for b in p:ns[1|sum(1<<(i+1) for i in b)]=1
 for T in range(1<<(s+1)):ns.setdefault(T,0)
 return ns

def key(ds,p,ts,q,ns):return (tuple(ds),canonical(p),tuple(ts),q,tuple(ns[i] for i in range(1<<(len(ds)+1))))

def main():
 start=time.time();first=set();second=set()
 for ds in [(8,8,8),(8,8,9),(8,9,9),(9,9,9),(9,9,10)]:
  for p in parts(3):
   for t in range(4):
    ns=stock(ds,p,(t,))
    if min(ns.values())>=0:first.add(key(ds,p,(t,),None,ns))
 for ds in [(8,8,8,8),(8,8,8,9),(8,8,9,9),(8,9,9,9),(9,9,9,9),(9,9,9,10)]:
  for p in parts(4):
   trs=list(combinations(range(4),3))
   for ts in product(range(4),repeat=4):
    if not all(residual(tuple(ds[i] for i in tr),restriction(p,tr),t) for tr,t in zip(trs,ts)):continue
    for q in range(min(ts)+1):
     ns=stock(ds,p,ts,q)
     if min(ns.values())>=0:second.add(key(ds,p,ts,q,ns))
 p1=json.loads((HERE/'UNIT_STAR_PILOT.json').read_text())['profiles']
 saved1={key(z['degrees'][1:],z['partition'],(z['t'],),None,{int(k):v for k,v in z['counts'].items()}) for z in p1}
 p2=json.loads((HERE/'FOUR_NEIGHBOR_PILOT.json').read_text())['profiles']
 saved2={key(z['degrees'][1:],z['partition'],z['triples'],z['quadruple'],{int(k):v for k,v in z['counts'].items()}) for z in p2}
 result=dict(scope=__doc__,partition_counts=[sum(1 for _ in parts(s)) for s in [3,4]],first_count=len(first),first_matches_saved=first==saved1,second_count=len(second),second_matches_saved=second==saved2,all_counts_nonnegative=True,elapsed_seconds=time.time()-start)
 assert first==saved1 and second==saved2
 (HERE/'DOMAIN_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
