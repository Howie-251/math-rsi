"""p occurs in four centre links: exact full colour/edge orbits and necessary aggregate model."""
from pathlib import Path
from itertools import product,permutations
from fractions import Fraction as Q
from math import comb
from functools import lru_cache
import json,time,numpy as np
from scipy.optimize import linprog,milp,LinearConstraint,Bounds
HERE=Path(__file__).resolve().parent
@lru_cache(None)
def perm(x):return tuple(sorted(set(permutations(x))))
def choose(n,k):return comb(n,k)if 0<=k<=n else 0
@lru_cache(None)
def group(n,red,edge):
 # Assign the red-count multiset uniformly to labelled equal-size groups.
 return sum((Q(np_prod(choose(r,e)for r,e in zip(rs,edge)),np_prod(choose(n,e)for e in edge))for rs in perm(red)),Q())/len(perm(red))
def np_prod(xs):
 v=1
 for x in xs:v*=x
 return v

def data():
 A=sorted(x for x in product(range(4),repeat=4)if tuple(sorted(x))==x)
 B=sorted(x for x in product(range(4),repeat=2)if tuple(sorted(x))==x)
 colors=[(pc,a,b)for pc in (0,1)for a in A if not pc or max(a)<=2 for b in B]
 EA=sorted(x for x in product(range(4),repeat=4)if tuple(sorted(x))==x and sum(x)<=5)
 EB=sorted(x for x in product(range(5),repeat=2)if tuple(sorted(x))==x and sum(x)<=5)
 edges=[(ep,a,b)for ep in (0,1)for a in EA for b in EB if ep+sum(a)+sum(b)==5]
 P=[]
 for pc,a,b in colors:
  row=[]
  for ep,c,d in edges:
   red=Q(int(not ep or pc))*group(3,a,c)*group(4,b,d)
   blue=Q(int(not ep or not pc))*group(3,tuple(3-r for r in a),c)*group(4,tuple(4-r for r in b),d)
   row.append(red+blue)
  P.append(row)
 # Every actual H supplies n_e; these are necessary orbit-aggregated consequences.
 names=['external_edge_count','p_external_degree','A_external_incidence','B_external_incidence','AA_cross_pairs','AB_cross_pairs','BB_cross_pairs','pB_pairs']
 rows=[[],[],[],[],[],[],[],[]];caps=[]
 for ep,a,b in edges:
  vals=[1,ep,sum(a),sum(b),sum(a[i]*a[j]for i in range(4)for j in range(i+1,4)),sum(a)*sum(b),b[0]*b[1],ep*sum(b)]
  for row,v in zip(rows,vals):row.append(v)
  caps.append(len(perm(a))*len(perm(b))*np_prod(choose(3,c)for c in a)*np_prod(choose(4,c)for c in b))
 return colors,edges,P,names,rows,caps

def main():
 start=time.process_time();colors,edges,P,names,A,caps=data();build=time.process_time()-start
 mat=np.array([[float(q)for q in r]for r in P]);m=len(edges);lo=[29,2,60,40,54,96,16,8];hi=[29,12]+[np.inf]*6
 constraints=np.vstack((np.column_stack((-mat,np.ones(len(P)))),np.column_stack((-np.array(A),np.zeros(len(A)))),np.column_stack((np.array(A),np.zeros(len(A))))))
 lower_rhs=np.r_[np.zeros(len(P)),-np.array(lo),np.array(hi)]
 finite=np.isfinite(lower_rhs)
 sol=linprog([0]*m+[-1],A_ub=constraints[finite],b_ub=lower_rhs[finite],bounds=[(0,min(29,c))for c in caps]+[(None,None)],method='highs',options={'time_limit':20})
 summary=dict(scope=__doc__,color_families=len(colors),edge_orbits=m,build_cpu_seconds=build,LP_status=sol.message,LP_maximin=(-sol.fun if sol.success else None))
 print(summary,flush=True)
 out=dict(summary=summary,colors=colors,edges=edges,probabilities=[[str(q)for q in r]for r in P],constraint_names=names,constraint_coefficients=A,lower=lo,upper=[None if not np.isfinite(x)else int(x)for x in hi],simple_orbit_capacities=caps)
 (HERE/'MODEL.json').write_text(json.dumps(out,indent=2)+'\n')
 if not sol.success:return
 outLP=[dict(edge=e,count=float(v))for e,v in zip(edges,sol.x[:-1])if v>1e-8]
 summary['LP_support']=outLP
 if -sol.fun>=1-1e-8:
  M=np.vstack((np.array(A),mat));ml=np.r_[lo,np.ones(len(P))];mh=np.r_[hi,np.full(len(P),np.inf)]
  s=milp(np.zeros(m),integrality=np.ones(m),bounds=Bounds(np.zeros(m),np.minimum(29,np.array(caps))),constraints=LinearConstraint(M,ml,mh),options={'time_limit':30})
  summary['MILP_status']=s.message
  if s.x is not None:
   counts=[round(x)for x in s.x];scores=[sum(n*q for n,q in zip(counts,row))for row in P];marg=[sum(n*c for n,c in zip(counts,row))for row in A]
   assert min(scores)>=1 and all(l<=v and (not np.isfinite(h)or v<=h)for l,v,h in zip(lo,marg,hi)) and all(0<=n<=c for n,c in zip(counts,caps))
   witness=dict(status='EXACT_AGGREGATE_OBSTRUCTION',scope='Integer orbit counts only; not a hypergraph or an assertion of pointwise realization.',counts=[dict(edge=e,count=n)for e,n in zip(edges,counts)if n],exact_minimum_score=str(min(scores)),marginals=marg,all_families_checked=len(scores))
   (HERE/'OBSTRUCTION.json').write_text(json.dumps(witness,indent=2)+'\n');summary['integer_obstruction']=witness
 summary['cpu_seconds']=time.process_time()-start
 (HERE/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n');print(summary,flush=True)
if __name__=='__main__':main()
