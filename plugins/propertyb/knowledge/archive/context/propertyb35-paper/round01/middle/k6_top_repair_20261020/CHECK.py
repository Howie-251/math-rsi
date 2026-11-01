"""Complete four-by-four 15-point partition core; no H enumeration."""
from itertools import product,permutations
from math import prod
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent
perms=list(permutations(range(4)))
def comp(n,k):
 if k==1:return [(n,)]
 return [(i,*v) for i in range(n+1) for v in comp(n-i,k-1)]
def direct(a):return sum(prod(a[i][p[i]] for i in range(4)) for p in perms)
def ryser(a):
 return sum((-1)**(4-len(S))*prod(sum(r[j] for j in S) for r in a) for m in range(1,16) for S in [[j for j in range(4) if m>>j&1]])
st=time.process_time();count=0;minimum=10**9;mins=[];hist={}
for r0,r1,r2 in product(comp(3,4),comp(4,4),comp(4,4)):
 r3=tuple(c-r0[j]-r1[j]-r2[j] for j,c in enumerate((3,4,4,4)))
 if min(r3)<0:continue
 assert sum(r3)==4
 a=(r0,r1,r2,r3);v=direct(a);assert v==ryser(a)
 count+=1;hist[v]=hist.get(v,0)+1
 if v<minimum:minimum=v;mins=[a]
 elif v==minimum:mins.append(a)
assert minimum==18 and mins==[((0,1,1,1),(1,1,1,1),(1,1,1,1),(1,1,1,1))]
out={'status':'PASS','scope':'all4x4 nonnegative integer matrices with row and column sums3,4,4,4; no H','complete_matrices':count,'minimum_permanent':minimum,'equality_matrices':mins,'blocked_candidates_upper_bound':16,'strict_margin':minimum-16,'histogram':hist,'cpu_seconds':time.process_time()-st}
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='histogram'})
