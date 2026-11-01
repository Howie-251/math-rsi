"""Exact binomial/finite scalar scan only; no positive-set or H search."""
from math import comb
from fractions import Fraction as F
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
def C(n,k):return comb(n,k) if 0<=k<=n else 0
def params(n,a):
 N=n-5;b=N-a;D=C(N,a)
 alpha=F(C(a,4),C(N,4));beta=F(C(b,4),C(N,4));gamma=F(C(a,5)+C(b,5),C(N,5));delta=F(C(N-8,a-8),D)
 return N,b,D,alpha,beta,gamma,delta
def value(n,a,s,cmax,extra=F(0),hunter=False):
 N,b,D,A,B,G,d=params(n,a)
 return max(c*A+(s-c)*B-(max(c-1,0)*d if hunter else 0)+extra for c in range(cmax+1))
rows=[]
for n in range(21,26):
 N=n-5
 def best(kind,hunter):
  vals=[]
  for a in range((N+1)//2,N+1):
   extra=params(n,a)[5] if kind=='q1_disjoint' else F(0)
   s=34 if kind=='q0' else 33;c=7 if kind=='q1_overlap_D9' else 6
   vals.append((value(n,a,s,c,extra,hunter),a))
  bound,a=min(vals)
  return {'outside_red':a,'outside_blue':N-a,'bound':str(bound),'strict':bound<1}
 row={'n':n,'sample_space':'one red andfour blue onF;outside uniformly colored','union':{k:best(k,False) for k in ['q0','q1_disjoint','q1_overlap_D9']},'red_tree_baseline':{k:best(k,True) for k in ['q0','q1_disjoint','q1_overlap_D9']}}
 rows.append(row)
# Concrete22point shared-event strict equality case.
N22,b22,D22,A22,B22,G22,d22=params(22,10)
assert (N22,b22,D22)==(17,7,19448) and 7*A22+26*B22==1
assert d22==F(36,D22) and 7*A22+26*B22-6*d22==F(2404,2431)<1
certs=[]
selected=[(21,10,34,6,False,'259/286'),(22,10,34,6,False,'4531/4862'),(23,11,34,6,False,'3773/3978'),(24,12,34,6,False,'12425/12597'),(25,12,34,6,False,'25141/25194'),(21,10,33,6,True,'7659/8008'),(22,10,33,6,True,'2337/2431'),(23,11,33,6,True,'5269/5304'),(21,9,33,7,False,'701/715'),(22,10,33,7,False,'2404/2431'),(23,11,33,6,False,'2485/2652'),(24,11,33,6,False,'12440/12597'),(25,12,33,6,False,'8259/8398')]
for n,a,s,cmax,extra,expected in selected:
 N=n-5;D=C(N,a);red=C(N-4,a-4);blue=C(N-4,a);pair=C(N-8,a-8);G=C(N-5,a-5)+C(N-5,a) if extra else 0
 worst=max(c*red+(s-c)*blue-max(c-1,0)*pair+G for c in range(cmax+1))
 assert F(worst,D)==F(expected)==value(n,a,s,cmax,params(n,a)[5] if extra else F(0),True)<1
 certs.append({'n':n,'outside_red':a,'singleton_edges':s,'red_group_cap':cmax,'exception_disjoint':extra,'sample_count':D,'red_bad_count':red,'blue_bad_count':blue,'red_pair_min_count':pair,'exception_mono_count':G,'max_failure_count':worst,'bound':expected,'successful_samples_lower':D-worst})
out={'scope':__doc__,'rows':rows,'integer_certificates':certs,'n22_equality':{'N':N22,'outside_blue':b22,'D':D22,'red_bad_count':str(A22*D22),'blue_bad_count':str(B22*D22),'union_count':str((7*A22+26*B22)*D22),'red_pair_min_count':36,'six_edge_red_tree_deduction':216,'final_bound':'2404/2431'},'overlap_degree8_explicit':[{'n':n,'a':a,'b':n-5-a,'bound':str(value(n,a,33,6,hunter=True)),'strict':value(n,a,33,6,hunter=True)<1} for n,a in [(21,9),(22,10),(23,11),(24,11),(25,12)]],'cpu_seconds':time.process_time()-st}
(P/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
for r in rows:print(r)
print('CPU',out['cpu_seconds'])
