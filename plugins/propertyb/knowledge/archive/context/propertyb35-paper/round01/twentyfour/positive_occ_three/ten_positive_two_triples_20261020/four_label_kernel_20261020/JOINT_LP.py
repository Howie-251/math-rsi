"""Bounded five-origin shared-capacity LP; exact acceptance via rational dual only."""
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1'
from pathlib import Path
from itertools import combinations
from collections import Counter
from fractions import Fraction as Q
import json,time,argparse
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix

HERE=Path(__file__).resolve().parent;EDGES=tuple(combinations(range(4),2))
TYPES={'Tpair':(2,(1,0,1)),'Ttriple':(3,(1,0,0)),
       'Bpair':(2,(0,1,2)),'Btriple':(3,(0,1,1)),'B4':(4,(0,1,0))}

def recover(cap,graph):
 sets=[set() for _ in range(4)];pid=0
 for (a,b),m in zip(EDGES,graph):
  for _ in range(m):sets[a].add(pid);sets[b].add(pid);pid+=1
 for i,s in enumerate(sets):
  while len(s)<cap[i]:s.add(pid);pid+=1
 return sets

def solve(row):
 st=time.process_time();sets=recover(row['capacities'],row['graph'])
 U=sorted(set().union(*sets));freq=Counter(v for s in sets for v in s)
 candidates=[tuple(s) for k in range(1,5) for s in combinations(U,k) if all(set(s)&a for a in sets)]
 targets={k:sorted({s for c in candidates for s in combinations(c,k)}) for k in (2,3,4)}
 variables=[(typ,f) for typ,(k,_) in TYPES.items() for f in targets[k]]
 budget=[2-row['n'],18,8-2*row['n']]+[7-freq[v] for v in U]
 cover=[set(s) for s in candidates]
 rr=[];cc=[];vv=[];nr=len(candidates)
 for j,(typ,f) in enumerate(variables):
  fs=set(f)
  for i,s in enumerate(cover):
   if fs<=s:rr.append(i);cc.append(j);vv.append(-1)
  for k,cost in enumerate(TYPES[typ][1]):
   if cost:rr.append(nr+k);cc.append(j);vv.append(cost)
  for v in f:rr.append(nr+3+v);cc.append(j);vv.append(1)
 for i in range(nr):rr.append(i);cc.append(len(variables));vv.append(1)
 A=csc_matrix((vv,(rr,cc)),shape=(nr+len(budget),len(variables)+1),dtype=float)
 cost=np.zeros(len(variables)+1);cost[-1]=-1
 lp=linprog(cost,A_ub=A,b_ub=np.array([0]*nr+budget),bounds=[(0,1)]*len(variables)+[(0,None)],method='highs')
 out={**row,'sets':[sorted(s) for s in sets], 'candidate_counts':dict(Counter(map(len,candidates))),
      'candidate_count':nr,'negative_variable_count':len(variables),'budgets':budget,
      'solver_status':int(lp.status),'floating_common_coverage':float(lp.x[-1]) if lp.success else None}
 if lp.success and lp.x[-1]<1-1e-8:
  lam=[Q(float(-v)).limit_denominator(10**6) for v in lp.ineqlin.marginals[:nr]]
  total=sum(lam,Q());lam=[v/total for v in lam]
  beta=[Q(float(-v)).limit_denominator(10**6) for v in lp.ineqlin.marginals[nr:]]
  gamma=[Q(float(-v)).limit_denominator(10**6) for v in lp.upper.marginals[:-1]]
  assert min(lam+beta+gamma)>=0
  W={k:Counter() for k in (2,3,4)}
  for s,w in zip(candidates,lam):
   if not w:continue
   for k in (2,3,4):
    for f in combinations(s,k):W[k][f]+=w
  deficit=Q()
  for (typ,f),g in zip(variables,gamma):
   v=sum(beta[k]*c for k,c in enumerate(TYPES[typ][1]))+sum(beta[3+x] for x in f)+g
   deficit=max(deficit,W[len(f)][f]-v)
  beta[0]+=deficit;beta[1]+=deficit
  for (typ,f),g in zip(variables,gamma):
   rhs=sum(beta[k]*c for k,c in enumerate(TYPES[typ][1]))+sum(beta[3+x] for x in f)+g
   assert W[len(f)][f]<=rhs
  bound=sum(v*b for v,b in zip(beta,budget))+sum(gamma,Q())
  if bound<1:
   out['dual_certificate']=dict(candidate_weights=[dict(red_set=s,weight=str(w)) for s,w in zip(candidates,lam) if w],
       budget_weights=list(map(str,beta)),upper_bound_weights=[dict(type=typ,negative_set=f,weight=str(g)) for (typ,f),g in zip(variables,gamma) if g],
       rounding_repair=str(deficit),bound=str(bound))
 if lp.success and 'dual_certificate' not in out:
  weights=[Q(float(v)).limit_denominator(10**6) for v in lp.x[:-1]]
  use=[Q() for _ in budget]
  for (typ,f),w in zip(variables,weights):
   for k,c in enumerate(TYPES[typ][1]):use[k]+=w*c
   for v in f:use[3+v]+=w
  scale=min([Q(1)]+[Q(b)/u for b,u in zip(budget,use) if u]+[1/w for w in weights if w])
  weights=[w*scale for w in weights]
  coverage=[sum(w for (_,f),w in zip(variables,weights) if set(f)<=s) for s in cover]
  out['fractional_diagnostic']=dict(exact_budget_feasible=True,minimum_coverage=str(min(coverage)),
      exact_cover_at_least_one=min(coverage)>=1,weights=[dict(type=t,negative_set=f,weight=str(w)) for (t,f),w in zip(variables,weights) if w])
 out['process_seconds']=time.process_time()-st
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--all',action='store_true');ap.add_argument('--cpu-limit',type=float,default=85)
 args=ap.parse_args();started=time.process_time()
 data=json.loads((HERE/'PROFILE.json').read_text());rows=data['representatives']
 if not args.all:rows=[r for r in rows if r['n']==2 and tuple(r['capacities']) in ((2,2,2,4),(2,2,3,3)) and not any(r['graph'])]
 out=[];complete=True
 for i,row in enumerate(rows):
  if time.process_time()-started>args.cpu_limit:complete=False;break
  out.append(solve(row))
  if (i+1)%100==0:print('done',i+1,'dual',sum('dual_certificate' in r for r in out),flush=True)
 result=dict(complete=complete,requested=len(rows),processed=len(out),strict_duals=sum('dual_certificate' in r for r in out),
             noncertified=sum('dual_certificate' not in r for r in out),process_seconds=time.process_time()-started,rows=out,
             scope='Small four-label necessary signed relaxation; fractional feasibility is not an integer obstruction or an H realization.')
 (HERE/('ALL_LP.json' if args.all else 'TWO_LP_PROFILE.json')).write_text(json.dumps(result,indent=2)+'\n')
 print({k:v for k,v in result.items() if k!='rows'},flush=True)

if __name__=='__main__':main()
