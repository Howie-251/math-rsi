"""Joint fractional negative-cover diagnostic for the residual six-label families."""
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1'
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
import json,time,argparse
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix
HERE=Path(__file__).resolve().parent

def mask(q):return sum(1<<v for v in q)
def frac(x):return F(float(x)).limit_denominator(1000000)
def fs(x):return str(x)

def build(row):
 A=list(map(set,row['sets']));U=sorted(set().union(*A));assert U==list(range(len(U)))
 freq=[sum(v in a for a in A) for v in U];cap=[7-x for x in freq]
 R=[tuple(q) for k in (3,4) for q in combinations(U,k) if all(set(q)&a for a in A)]
 RM=[mask(q) for q in R];V=[]
 for size,types in ((2,('N2',)),(3,('T3','Bx3')),(4,('N4',))):
  for q in combinations(U,size):
   qm=mask(q)
   covered=[i for i,m in enumerate(RM) if m&qm==qm]
   if covered:
    for typ in types:V.append((typ,q,covered))
 # budgets: original T count, negative degree at x, all negative count,
 # then each actual U point's remaining occurrence capacity.
 B=[3,4,20]+cap;D=[]
 rr=[];cc=[];vv=[]
 for col,(typ,q,covered) in enumerate(V):
  for i in covered:rr.append(i);cc.append(col);vv.append(-1.)
  cost=[int(typ in ('N2','T3')),int(typ in ('N2','Bx3')),1]+[int(v in q) for v in U]
  D.append(cost)
  for a,c in enumerate(cost):
   if c:rr.append(len(R)+a);cc.append(col);vv.append(float(c))
 # Maximize common candidate coverage lambda.
 for i in range(len(R)):rr.append(i);cc.append(len(V));vv.append(1.)
 mat=csc_matrix((vv,(rr,cc)),shape=(len(R)+len(B),len(V)+1))
 return R,V,D,B,mat

def dual_certificate(res,R,V,D,B):
 n=len(R);m=len(V)
 alpha=[max(F(0),frac(-x)) for x in res.ineqlin.marginals[:n]]
 beta=[max(F(0),frac(-x)) for x in res.ineqlin.marginals[n:]]
 gamma=[max(F(0),frac(-x)) for x in res.upper.marginals[:m]]
 weight=sum(alpha);assert weight>0
 alpha=[x/weight for x in alpha];beta=[x/weight for x in beta];gamma=[x/weight for x in gamma]
 # Any rounding violation is repaired exactly by the universal total-count
 # budget coefficient, present with coefficient one in every variable.
 deficit=max([F(0)]+[sum(alpha[i] for i in covered)-sum(F(c)*b for c,b in zip(cost,beta))-ga for (_,_,covered),cost,ga in zip(V,D,gamma)])
 beta[2]+=deficit
 for (_,_,covered),cost,ga in zip(V,D,gamma):
  assert sum(alpha[i] for i in covered)<=sum(F(c)*b for c,b in zip(cost,beta))+ga
 bound=sum(F(c)*b for c,b in zip(B,beta))+sum(gamma)
 assert sum(alpha)==1
 return {'kind':'exact_rational_dual_cover_bound','coverage_weights':[{'red_set':R[i],'weight':fs(x)} for i,x in enumerate(alpha) if x],
 'budget_weights':list(map(fs,beta)),
 'upper_bound_weights':[{'type':V[i][0],'negative_set':V[i][1],'weight':fs(x)} for i,x in enumerate(gamma) if x],
 'rounding_repair_on_total_budget':fs(deficit),'coverage_upper_bound':fs(bound),'strict_below_one':bound<1}

def primal_witness(res,R,V,D,B):
 lam=float(res.x[-1]);divisor=(1+lam)/2 if lam>1+1e-6 else 1.
 x=[max(F(0),min(F(1),frac(v/divisor))) for v in res.x[:-1]]
 covered=[sum(z for z,(_,_,inds) in zip(x,V) if i in inds) for i in range(len(R))]
 use=[sum(z*cost[k] for z,cost in zip(x,D)) for k in range(len(B))]
 valid=all(z>=1 for z in covered) and all(z<=b for z,b in zip(use,B))
 return {'exact_feasible':valid,'minimum_coverage':fs(min(covered)),
         'budget_use':list(map(fs,use)),
         'weights':[{'type':typ,'negative_set':q,'weight':fs(z)} for z,(typ,q,_) in zip(x,V) if z]}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--cases',type=int,default=2);ap.add_argument('--prefix',default='PROFILE');args=ap.parse_args()
 source=json.loads((HERE.parent/'CENSUS_PROFILE.json').read_text())
 rows=[r for r in source['rows'] if r['unresolved_by_bounds_and_analytic']]
 rows.sort(key=lambda r:max(-p['C4_margin'] for p in r['nongated_maximal_b_rows']),reverse=True)
 start=time.process_time();outputs=[]
 for i,row in enumerate(rows[:args.cases]):
  t=time.process_time();R,V,D,B,mat=build(row)
  c=np.zeros(len(V)+1);c[-1]=-1
  res=linprog(c,A_ub=mat,b_ub=np.array([0.]*len(R)+B),bounds=[(0.,1.)]*len(V)+[(0.,None)],method='highs',options={'time_limit':20.,'threads':1})
  out={'index_in_severity_order':i,'graph':row['vector'],'E':row['E'],'M3':row['M3'],'sets':row['sets'],
       'C3':row['C3'],'C4':row['C4'],'candidate_rows':len(R),'negative_variables':len(V),'budgets':B,
       'solver_status':int(res.status),'solver_message':str(res.message),'cpu_seconds':time.process_time()-t}
  if res.success:
   lam=float(res.x[-1]);out['maximum_common_coverage']=lam
   if lam<1-1e-8:out['dual_certificate']=dual_certificate(res,R,V,D,B)
   else:out['primal_witness']=primal_witness(res,R,V,D,B)
  outputs.append(out)
  print('CASE',i,'lambda',out.get('maximum_common_coverage'),'exactdual',out.get('dual_certificate',{}).get('strict_below_one'),'exactprimal',out.get('primal_witness',{}).get('exact_feasible'),'cpu',out['cpu_seconds'],flush=True)
  if time.process_time()-start>85:break
 out={'model':'N2(original T contains x),T3(original T avoids x),Bx3(original B contains x),N4(original B avoids x); all variables in [0,1]. Simultaneous C3/C4 covering, T<=3,xdegree<=4,total<=20,pointnegative<=7-remainingpositivefreq.',
      'source_residual_orbits':77,'requested_cases':args.cases,'completed_cases':len(outputs),'cpu_seconds':time.process_time()-start,'rows':outputs,
      'scope':'Fractional negative layouts only, not original H or integer negative-layout enumeration.'}
 (HERE/(args.prefix+'.json')).write_text(json.dumps(out,indent=2)+'\n')
 print('TOTAL',out['cpu_seconds'])
if __name__=='__main__':main()
