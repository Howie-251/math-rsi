#!/usr/bin/env python3
"""Bounded C9 root-incidence projection; every infeasibility certificate is rationally checked.
This is neither a 59-vertex graph search nor a Lean-certified classification.
"""
import itertools, json, time, warnings
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import linprog, OptimizeWarning
warnings.filterwarnings('ignore', category=OptimizeWarning)
N=9
started=time.monotonic()

def graph(starts):
 A=np.zeros((N,N),dtype=int)
 for i in range(N):A[i,(i+2)%N]=A[(i+2)%N,i]=1
 for i in starts:A[i,(i+3)%N]=A[(i+3)%N,i]=1
 return A

def light_pairs(A):
 C=A@A; allowed=[]; forced=[]
 for i,j in itertools.combinations(range(N),2):
  if A[i,j] or (j-i)%N in (1,8):continue
  if not any(A[j,k] for k in ((i-1)%N,(i+1)%N)) and not any(A[i,k] for k in ((j-1)%N,(j+1)%N)):
   allowed.append((i,j))
   if C[i,j]>=2:forced.append((i,j))
 return allowed,forced

def internal_ok(A):
 C=A@A
 if any(A[i,j] and C[i,j] for i,j in itertools.combinations(range(N),2)):return False
 allowed,forced=light_pairs(A); F=[[] for _ in range(N)]
 for i,j in itertools.combinations(range(N),2):
  if A[i,j]:continue
  if (j-i)%N in (1,8):
   if C[i,j]>3:return False
  elif C[i,j]>=2:
   if C[i,j]>2 or (i,j) not in allowed:return False
   F[i].append(j);F[j].append(i)
 return all(len(f)<=2 and (len(f)<2 or A[f[0],f[1]]) for f in F)

trianglefree=[]; survivors=[]
for mask in range(512):
 starts=[i for i in range(N) if mask>>i&1]; A=graph(starts)
 if any(A[i,j] and (A@A)[i,j] for i,j in itertools.combinations(range(N),2)):continue
 trianglefree.append(starts)
 if internal_ok(A):survivors.append(starts)
assert len(trianglefree)==343
assert all(len(s)<=2 and (len(s)<2 or (s[0]-s[1])%N in (1,8)) for s in survivors)
report={'scope':'Necessary external incidence projection only; 3 rotation representatives after exact finite internal classification',
        'trianglefree_internal_count':len(trianglefree),'local_internal_survivors':survivors,
        'representatives':[],'status':'RUNNING'}
for starts in [[],[0],[0,1]]:
 A=graph(starts); C=A@A; allowed,forced=light_pairs(A)
 entry={'chord_starts':starts,'light_allowed':allowed,'light_forced':forced,'cases':[]}
 for mask in range(1<<len(allowed)):
  L=np.zeros((N,N),dtype=int)
  for k,(i,j) in enumerate(allowed):
   if mask>>k&1:L[i,j]=L[j,i]=1
  if any(not L[i,j] for i,j in forced):continue
  if any(L[i].sum()>2 or any(L[i,j] and L[i,k] and not A[j,k] for j,k in itertools.combinations(range(N),2)) for i in range(N)):continue
  B=L.copy()
  for i in range(N):B[i,(i+1)%N]=B[(i+1)%N,i]=2
  pairlist=list(itertools.combinations(range(N),2))
  need=[int(1+B[i,j]-A[i,j]-C[i,j]) for i,j in pairlist]
  if min(need)<0:continue
  remain=2-L.sum(axis=1);types=[];lower=[]
  for sm in range(512):
   s=np.array([(sm>>i)&1 for i in range(N)],dtype=int)
   if any(s[i] and s[j] and (A[i,j] or need[k]==0) for k,(i,j) in enumerate(pairlist)):continue
   c=A@s; low=np.maximum(c-1,0)
   if max(c)>2:continue
   good=True
   for i in range(N):
    if low[i]:
     if remain[i]==0 or s[(i-1)%N] or s[(i+1)%N] or any(L[i,j] and not s[j] for j in range(N)):good=False
   if good:types.append(s);lower.append(low)
  # Equalities: vertex count, degrees, common-neighbor counts, and lower-repeat inequalities with slacks.
  cols=[]
  for s,low in zip(types,lower):cols.append([1,*s.tolist(),*[int(s[i]*s[j]) for i,j in pairlist],*low.tolist()])
  b=np.array([50,*[int(8-x) for x in A.sum(axis=1)],*need,*remain.tolist()],dtype=int)
  M=np.array(cols,dtype=int).T
  slack=np.zeros((len(b),N),dtype=int)
  for i in range(N):slack[-N+i,i]=1
  M=np.concatenate([M,slack],axis=1)
  opt={'time_limit':2,'threads':1}
  r=linprog(np.zeros(M.shape[1]),A_eq=M,b_eq=b,bounds=(0,None),method='highs',options=opt)
  case={'internal_light_mask':mask,'outside_types':[sum(int(s[i])<<i for i in range(N)) for s in types],'status':int(r.status)}
  if r.status==0:
   # A float feasible projection is only a search clue, never a graph.
   case['state']='FRACTIONAL_PROJECTION_FEASIBLE'
   case['nonzero_projection']=[[case['outside_types'][i],float(x)] for i,x in enumerate(r.x[:len(types)]) if x>1e-8]
  elif r.status==2:
   d=linprog(b.astype(float),A_ub=-M.T,b_ub=np.zeros(M.shape[1]),bounds=[(-1,1)]*len(b),method='highs',options=opt)
   if d.status==0:
    v=[Fraction(float(x)).limit_denominator(100000) for x in d.x]
    dot=sum(v[i]*int(b[i]) for i in range(len(b)))
    valid=dot<0 and all(sum(v[i]*int(M[i,j]) for i in range(len(b)))>=0 for j in range(M.shape[1]))
    if valid:
     case['state']='EXACT_RATIONAL_FARKAS_CHECKED'
     case['farkas']=[str(x) for x in v];case['rhs_dot']=str(dot)
    else:case['state']='NUMERICAL_INFEASIBILITY_NOT_CERTIFIED'
   else:case['state']='NUMERICAL_INFEASIBILITY_NOT_CERTIFIED'
  else:case['state']='UNKNOWN'
  entry['cases'].append(case)
  if time.monotonic()-started>100:break
 report['representatives'].append(entry)
 if time.monotonic()-started>100:break
report['elapsed_seconds']=time.monotonic()-started
report['status']='BOUNDED_PROJECTION_FINISHED'
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'internal_survivors':len(survivors),'elapsed_seconds':report['elapsed_seconds'],
 'states':[{ 'chords':e['chord_starts'],'cases':len(e['cases']),'states':{s:sum(c['state']==s for c in e['cases']) for s in sorted({c['state'] for c in e['cases']})}} for e in report['representatives']]},indent=2))
