"""Complete small matrix lemma: 4x4 nonnegative integer matrices with every row/column sum4."""
from pathlib import Path
from itertools import product,permutations,combinations
import json,time
HERE=Path(__file__).parent

def permanent(A):
 n=len(A);return sum(prod(A[i][p[i]] for i in range(n)) for p in permutations(range(n)))
def prod(xs):
 v=1
 for x in xs:v*=x
 return v
def ryser(A):
 n=len(A);return sum((-1)**(n-S.bit_count())*prod(sum(A[i][j] for j in range(n) if S>>j&1) for i in range(n)) for S in range(1,1<<n))

def main():
 st=time.time();rows=[x for x in product(range(5),repeat=4) if sum(x)==4];assert len(rows)==35
 count=0;mins=[10**9,10**9];minimizers=[[],[]];stats={}
 for a in rows:
  for b in rows:
   if any(a[j]+b[j]>4 for j in range(4)):continue
   for c in rows:
    d=tuple(4-a[j]-b[j]-c[j] for j in range(4))
    if min(d)<0:continue
    assert sum(d)==4
    A=(a,b,c,d);count+=1;P=permanent(A);assert P==ryser(A)
    M=max(map(max,A));T=max(A[i][j]*A[k][l]+A[i][l]*A[k][j] for i,k in combinations(range(4),2) for j,l in combinations(range(4),2))
    values=(P-T,P-2*M)
    assert min(values)>=22
    z=stats.setdefault(M,dict(count=0,min_permanent=10**9,min_per_minus_max_minor=10**9,min_per_minus_twice_max_entry=10**9))
    z['count']+=1;z['min_permanent']=min(z['min_permanent'],P);z['min_per_minus_max_minor']=min(z['min_per_minus_max_minor'],values[0]);z['min_per_minus_twice_max_entry']=min(z['min_per_minus_twice_max_entry'],values[1])
    for i,v in enumerate(values):
     if v<mins[i]:mins[i]=v;minimizers[i]=[A]
     elif v==mins[i]:minimizers[i].append(A)
 assert count==10147 and mins==[22,22]
 assert all(len(z)==1 and z[0]==((1,1,1,1),)*4 for z in minimizers)
 result=dict(status='PASS',scope=__doc__,complete_domain='each first three rows is one of35 weak compositions of4 into4; fourth row uniquely forced by columns; keep iff nonnegative',matrix_count=count,permanent_crosscheck='24-term expansion equals independent 15-term Ryser inclusion-exclusion at every input',min_per_minus_max_2x2_permanent=mins[0],min_per_minus_twice_max_entry=mins[1],unique_equality_matrix=((1,1,1,1),)*4,by_max_entry=stats,elapsed_seconds=time.time()-st)
 (HERE/'MATCHING_CORE.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
if __name__=='__main__':main()
