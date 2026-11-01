"""Bounded seven-label shared-capacity LP pilot. Candidates have all sizes 1..5.
Relaxation T<=2, x-negative<=4, total-negative<=20, point<=7-remaining-positive-frequency.
No full seven-label census and no original ten-positive realization assertion.
"""
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1'
from pathlib import Path
from itertools import combinations
from collections import defaultdict,Counter
from fractions import Fraction as Q
import json,time,warnings
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix
warnings.filterwarnings('ignore',message='Unrecognized options detected')
HERE=Path(__file__).resolve().parent;EDGES=list(combinations(range(7),2));START=time.process_time()

def vector(es):
 g=[0]*21
 for i,j,m in es:g[EDGES.index(tuple(sorted((i,j))))]=m
 return tuple(g)

DETERMINISTIC=[('two_double_triangles_and_isolate',vector([(0,1,2),(0,2,2),(1,2,2),(3,4,2),(3,5,2),(4,5,2)])),
 ('double_triangle_and_double_four_cycle',vector([(0,1,2),(0,2,2),(1,2,2),(3,4,2),(4,5,2),(5,6,2),(3,6,2)]))]

def first_graphs(limit):
 d=[0]*7;g=[0]*21;emitted=0
 def visit(k,E):
  nonlocal emitted
  if emitted>=limit:return
  if E>14 or E+sum(4-a for a in d)//2<11:return
  if k==21:
   if E>=11:emitted+=1;yield tuple(g)
   return
  i,j=EDGES[k]
  for m in range(min(4-d[i],4-d[j],14-E)+1):
   g[k]=m;d[i]+=m;d[j]+=m
   yield from visit(k+1,E+m)
   d[i]-=m;d[j]-=m
  g[k]=0
 yield from visit(0,0)

def build(g):
 masks=[];d=[0]*7;A=[[] for _ in range(7)]
 def point(labels):
  p=len(masks);mask=0
  for v in labels:mask|=1<<v;A[v].append(p)
  masks.append(mask)
 for (i,j),m in zip(EDGES,g):
  d[i]+=m;d[j]+=m
  for _ in range(m):point((i,j))
 for i in range(7):
  for _ in range(4-d[i]):point((i,))
 assert max(d)<=4 and 11<=sum(g)<=14 and len(masks)<=17
 U=list(range(len(masks)));freq=[m.bit_count() for m in masks]
 R=[];counts={}
 for size in range(1,6):
  first=len(R)
  for S in combinations(U,size):
   covered=0
   for p in S:covered|=masks[p]
   if covered==127:R.append(S)
  counts[size]=len(R)-first
 assert R
 cover=defaultdict(list)
 for i,S in enumerate(R):
  for size in (2,3,4):
   for F in combinations(S,size):cover[(size,F)].append(i)
 V=[]
 for (size,F),ids in sorted(cover.items()):
  for typ in ({2:('N2',),3:('T3','Bx3'),4:('N4',)}[size]):V.append((typ,F,ids))
 budgets=[2,4,20]+[7-f for f in freq];costs=[];rr=[];cc=[];vv=[]
 for j,(typ,F,ids) in enumerate(V):
  for i in ids:rr.append(i);cc.append(j);vv.append(-1.)
  cost=[int(typ in ('N2','T3')),int(typ in ('N2','Bx3')),1]+[int(p in F) for p in U];costs.append(cost)
  for k,c in enumerate(cost):
   if c:rr.append(len(R)+k);cc.append(j);vv.append(c)
 for i in range(len(R)):rr.append(i);cc.append(len(V));vv.append(1.)
 matrix=csc_matrix((vv,(rr,cc)),shape=(len(R)+len(budgets),len(V)+1))
 return A,R,V,costs,budgets,matrix,counts

def rat(x):return Q(float(x)).limit_denominator(1000000)
def certificate(res,R,V,D,B):
 n=len(R);m=len(V);a=[max(Q(),rat(-x)) for x in res.ineqlin.marginals[:n]]
 beta=[max(Q(),rat(-x)) for x in res.ineqlin.marginals[n:]]
 gamma=[max(Q(),rat(-x)) for x in res.upper.marginals[:m]]
 total=sum(a);assert total>0;a=[x/total for x in a];beta=[x/total for x in beta];gamma=[x/total for x in gamma]
 deficit=max([Q()]+[sum(a[i] for i in ids)-sum(c*b for c,b in zip(cost,beta))-ga for (_,_,ids),cost,ga in zip(V,D,gamma)])
 beta[2]+=deficit
 assert sum(a)==1
 for (_,_,ids),cost,ga in zip(V,D,gamma):assert sum(a[i] for i in ids)<=sum(c*b for c,b in zip(cost,beta))+ga
 bound=sum(c*b for c,b in zip(B,beta))+sum(gamma)
 return dict(exact_checked=True,strict=bound<1,bound=str(bound),coverage_weights=[dict(S=S,weight=str(w)) for S,w in zip(R,a) if w],budget_weights=list(map(str,beta)),upper_weights=[dict(type=typ,F=F,weight=str(w)) for (typ,F,_),w in zip(V,gamma) if w],rounding_repair=str(deficit),target_inequalities=len(V))

def witness(res,R,V,D,B):
 lam=float(res.x[-1]);scale=(1+lam)/2 if lam>1+1e-6 else 1
 weights=[max(Q(),min(Q(1),rat(w/scale))) for w in res.x[:-1]]
 covered=[Q() for _ in R]
 for w,(_,_,ids) in zip(weights,V):
  if w:
   for i in ids:covered[i]+=w
 use=[sum(w*cost[k] for w,cost in zip(weights,D)) for k in range(len(B))]
 exact=min(covered)>=1 and all(v<=b for v,b in zip(use,B))
 return dict(exact_feasible=exact,minimum_coverage=str(min(covered)),budget_use=list(map(str,use)),weights=[dict(type=typ,F=F,weight=str(w)) for (typ,F,_),w in zip(V,weights) if w])

rows=[];seen=set();cases=DETERMINISTIC+[(f'first_edge_recursion_{i}',g) for i,g in enumerate(first_graphs(6))]
for name,g in cases:
 if g in seen:continue
 if time.process_time()-START>=15:break
 seen.add(g);begin=time.process_time();A,R,V,D,B,mat,counts=build(g)
 remaining=15-(time.process_time()-START)
 if remaining<=0:break
 objective=np.zeros(len(V)+1);objective[-1]=-1
 res=linprog(objective,A_ub=mat,b_ub=np.array([0.]*len(R)+B),bounds=[(0,1)]*len(V)+[(0,None)],method='highs',options={'time_limit':remaining,'threads':1})
 row=dict(name=name,graph=g,E=sum(g),sets=A,union_size=len(B)-3,candidates_by_size=counts,candidates=len(R),negative_variables=len(V),budgets=B,solver_status=int(res.status),solver_message=str(res.message),cpu_seconds=time.process_time()-begin)
 if res.success:
  row['common_coverage_float']=float(res.x[-1])
  if res.x[-1]<1-1e-8:row['dual']=certificate(res,R,V,D,B)
  else:row['fractional_witness']=witness(res,R,V,D,B)
 rows.append(row)
 result=dict(scope=__doc__,sample_rows=rows,requested_sample_graphs=len(cases),completed_samples=len(rows),cpu_seconds=time.process_time()-START,complete_seven_label_domain=False,stopped_at_fractional_feasible=('fractional_witness' in row))
 (HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
 print(name,counts,'lambda',row.get('common_coverage_float'),'exactdual',row.get('dual',{}).get('bound'),'exactprimal',row.get('fractional_witness',{}).get('exact_feasible'),'cpu',row['cpu_seconds'],flush=True)
 if 'fractional_witness' in row:break
print('TOTAL_CPU',time.process_time()-START)
