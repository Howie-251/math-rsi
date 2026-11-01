"""New simultaneous ten pair moments on the same fifteen external9 points.
Each allowed cross-codegree profile receives weight x>=0; sum x=15, five degree marginals,
and all twenty min/max inclusive-triple moment inequalities. Exact feasible witnesses retained.
"""
from pathlib import Path
from itertools import product,combinations
from fractions import Fraction as Q
import json,time,sys
import numpy as np
from scipy.optimize import linprog
HERE=Path(__file__).parent;sys.dont_write_bytecode=True

def rational_solution(columns,b):
 # Solve the exact overdetermined marginal system on the support proposed by HiGHS.
 n=len(columns);rows=[[Q(columns[j][i]) for j in range(n)]+[Q(v)] for i,v in enumerate(b)];pivots=[];row=0
 for col in range(n):
  pivot=next((h for h in range(row,len(rows)) if rows[h][col]),None)
  if pivot is None:continue
  rows[row],rows[pivot]=rows[pivot],rows[row];v=rows[row][col];rows[row]=[x/v for x in rows[row]]
  for h in range(len(rows)):
   if h==row or not rows[h][col]:continue
   v=rows[h][col];rows[h]=[a-v*c for a,c in zip(rows[h],rows[row])]
  pivots.append((row,col));row+=1
 assert all(any(r[:-1]) or not r[-1] for r in rows)
 out=[Q()]*n
 for row,col in pivots:out[col]=rows[row][-1]
 assert min(out)>=0 and all(sum(columns[j][i]*out[j] for j in range(n))==b[i] for i in range(len(b)))
 return out

def main():
 start=time.time();rs=json.loads((HERE.parent/'five_join/FIVE_REMAINDERS.json').read_text())['cases'];g=json.loads((HERE/'mixed_triples/GENERAL_GATE.json').read_text())['cases'];allowed={}
 for r in g:
  if not r['strict']:allowed.setdefault(tuple(r['codegrees']),[]).append(r['triple'])
 assert len(allowed)==12 and all(0 in v and 1 in v for v in allowed.values());pairs=list(combinations(range(5),2));out=[]
 for r in rs:
  ns={int(t):n for t,n in r['counts'].items()};cs=[sum(n for t,n in ns.items() if t>>i&1 and t>>j&1) for i,j in pairs];marg=[32-sum(c for ij,c in zip(pairs,cs) if i in ij) for i in range(5)];moments=[sum((5-t.bit_count())*n for t,n in ns.items() if t>>i&1 and t>>j&1) for i,j in pairs]
  # Check the identical moment formula stated in the mathematical task.
  assert moments==[3*c-sum(sum(n for t,n in ns.items() if t>>i&1 and t>>j&1 and t>>k&1) for k in range(5) if k not in (i,j)) for (i,j),c in zip(pairs,cs)]
  patterns=[p for p in product((1,2,3),repeat=5) if all((c,*sorted((p[i],p[j]))) in allowed for (i,j),c in zip(pairs,cs))];cols=[(1,*p) for p in patterns];mins=[];maxs=[]
  for (i,j),c in zip(pairs,cs):
   tt=[allowed[(c,*sorted((p[i],p[j])))] for p in patterns];mins.append([min(t) for t in tt]);maxs.append([max(t) for t in tt])
  Aeq=np.array(cols,dtype=float).T;b=[15,*marg];Aub=np.array(mins+[[-a for a in v] for v in maxs],dtype=float);bub=np.array(moments+[-a for a in moments],dtype=float)
  z=linprog(np.zeros(len(patterns)),A_eq=Aeq,b_eq=np.array(b,dtype=float),A_ub=Aub,b_ub=bub,bounds=(0,None),method='highs');assert z.success
  support=[i for i,v in enumerate(z.x) if v>1e-8];qq=rational_solution([cols[i] for i in support],b);w=[dict(profile=list(patterns[i]),weight=str(a)) for i,a in zip(support,qq) if a]
  lower=[sum(Q(v['weight'])*min(allowed[(c,*sorted((v['profile'][i],v['profile'][j])))]) for v in w) for (i,j),c in zip(pairs,cs)];upper=[sum(Q(v['weight'])*max(allowed[(c,*sorted((v['profile'][i],v['profile'][j])))]) for v in w) for (i,j),c in zip(pairs,cs)]
  assert all(lo<=q<=hi for lo,q,hi in zip(lower,moments,upper));out.append(dict(core_id=r['id'],counts=r['counts'],pairs=pairs,pair_codegrees=cs,external_cross_marginals=marg,inclusive_triple_moments=moments,pattern_count=len(patterns),weights=w,lower_moment_bounds=list(map(str,lower)),upper_moment_bounds=list(map(str,upper)),all_new_constraints_redundant=True,lp_status=z.message))
  print(r['id'],'patterns',len(patterns),'rational_support',len(w),'pair_moments',moments,flush=True)
 result=dict(scope=__doc__,complete=True,core_count=len(out),feasible_count=len(out),exact_feasible_count=len(out),pair_inequalities_per_core=20,gate_nonempty_interval_types=len(allowed),all_gate_intervals_contain_zero_one=True,moment_min=min(q for r in out for q in r['inclusive_triple_moments']),moment_max=max(q for r in out for q in r['inclusive_triple_moments']),cases=out,elapsed_seconds=time.time()-start);(HERE/'PAIR_MOMENT_PILOT.json').write_text(json.dumps(result,indent=2)+'\n');print('exact_feasible',len(out),'of49','seconds',time.time()-start)
if __name__=='__main__':main()
