"""Search signed counterexamples on all nine-line PG(2,3) families up to automorphism.
Existing scipy/HiGHS only; no package installation, no original H search.
"""
import os
os.environ['OMP_NUM_THREADS']='1';os.environ['OPENBLAS_NUM_THREADS']='1'
from pathlib import Path
from itertools import product,combinations
from collections import deque,Counter
import json,time,argparse
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import csc_matrix
HERE=Path(__file__).resolve().parent

def norm(v):
    x=next(x for x in v if x%3)
    return tuple((y*(1 if x==1 else 2))%3 for y in v)
V=sorted({norm(v) for v in product(range(3),repeat=3) if any(v)})
IDX={v:i for i,v in enumerate(V)}
LINES=[tuple(i for i,v in enumerate(V) if sum(a*b for a,b in zip(v,w))%3==0) for w in V]
LIDX={frozenset(e):i for i,e in enumerate(LINES)}
assert len(V)==len(LINES)==13 and all(len(e)==4 for e in LINES)
assert all(sum(set(p)<=set(e) for e in LINES)==1 for p in combinations(range(13),2))
MATS=[((0,1,0),(1,0,0),(0,0,1)),((1,0,0),(0,0,1),(0,1,0)),((1,1,0),(0,1,0),(0,0,1)),((2,0,0),(0,1,0),(0,0,1))]
GENS=[]
for M in MATS:
 pp=tuple(IDX[norm(tuple(sum(M[i][k]*v[k] for k in range(3))%3 for i in range(3)))] for v in V)
 lp=tuple(LIDX[frozenset(pp[i] for i in e)] for e in LINES)
 assert len(set(pp))==len(set(lp))==13
 GENS.append({'point_permutation':pp,'line_permutation':lp})

def orbits():
 left=set(combinations(range(13),4));out=[]
 while left:
  seed=min(left);seen={seed};q=deque([seed])
  while q:
   t=q.popleft()
   for gen in GENS:
    u=tuple(sorted(gen['line_permutation'][i] for i in t))
    if u not in seen:seen.add(u);q.append(u)
  assert seen<=left
  out.append((seed,sorted(seen)));left-=seen
 assert sum(len(o) for _,o in out)==715
 return out

def mask(c):return sum(1<<v for v in c)

def problem(excluded):
 pos=[e for i,e in enumerate(LINES) if i not in excluded];pm=[mask(e) for e in pos]
 minimal=[]
 for r in range(1<<13):
  if not all(r&e for e in pm):continue
  if all(not all((r^(1<<v))&e for e in pm) for v in range(13) if r>>v&1):minimal.append(r)
 cand=[(c,mask(c)) for k in (3,4) for c in combinations(range(13),k)]
 cand=[(c,m) for c,m in cand if any(r&m==m for r in minimal)]
 a=[sum(v in e for e in pos) for v in range(13)];cap=[7-v for v in a]
 rr=[];cc=[];vv=[];lb=[1.]*len(minimal)+[-np.inf]*15;ub=[np.inf]*len(minimal)+cap+[3,20]
 for j,(c,m) in enumerate(cand):
  for i,r in enumerate(minimal):
   if r&m==m:rr.append(i);cc.append(j);vv.append(1.)
  for v in c:rr.append(len(minimal)+v);cc.append(j);vv.append(1.)
  if len(c)==3:rr.append(len(minimal)+13);cc.append(j);vv.append(1.)
  rr.append(len(minimal)+14);cc.append(j);vv.append(1.)
 A=csc_matrix((vv,(rr,cc)),shape=(len(lb),len(cand)))
 return pos,minimal,cand,a,cap,LinearConstraint(A,np.asarray(lb),np.asarray(ub))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--time-limit',type=float,default=5);ap.add_argument('--prefix',default='PROFILE');args=ap.parse_args()
 start=time.process_time();wall=time.monotonic();rows=[];orb=orbits()
 for cid,(exc,members) in enumerate(orb):
  pos,minimal,cand,a,cap,constraint=problem(exc)
  print('PROFILE',cid,'orbit',len(members),'minimal_sizes',dict(Counter(r.bit_count() for r in minimal)),'negative_candidates',len(cand),flush=True)
  t=time.process_time();res=milp(np.ones(len(cand)),integrality=np.ones(len(cand)),bounds=Bounds(np.zeros(len(cand)),np.ones(len(cand))),constraints=constraint,options={'time_limit':args.time_limit,'presolve':True,'threads':1})
  row={'case':cid,'excluded_line_indices':exc,'excluded_orbit_size':len(members),'excluded_orbit_members':members,
       'positive_sets':pos,'positive_occurrence':a,'negative_occurrence_capacity':cap,
       'minimal_transversal_masks':minimal,'minimal_transversal_size_counts':dict(Counter(r.bit_count() for r in minimal)),
       'negative_candidate_count':len(cand),'solver_status':int(res.status),'solver_message':str(res.message),'cpu_seconds':time.process_time()-t,
       'solver_mip_gap':float(res.mip_gap) if getattr(res,'mip_gap',None) is not None else None}
  if res.x is not None:
   neg=[c for (c,_),v in zip(cand,res.x) if v>0.5]
   occ=[a[v]+sum(v in c for c in neg) for v in range(13)]
   verify=all(not(all(r&mask(e) for e in pos) and all(r&mask(f)!=mask(f) for f in neg)) for r in range(1<<13))
   row.update(negative_sets=neg,total_occurrence=occ,negative_triple_count=sum(len(c)==3 for c in neg),negative_count=len(neg),all_8192_no_repair=verify)
   row['exact_valid_counterexample']=verify and max(occ)<=7 and len(neg)<=20 and sum(len(c)==3 for c in neg)<=3
   if row['exact_valid_counterexample']:
    rows.append(row);break
  rows.append(row)
 out={'points':V,'projective_lines':LINES,'automorphism_generators':GENS,'excluded4_domain':715,'excluded4_orbit_sizes':[len(m) for _,m in orb],
      'scope':'All715 nine-line families are transported to three explicit projective automorphism orbits. MILP statuses concern only each fixed positive representative; no general gate conclusion.',
      'scipy_interpreter':'/tmp/tbs-s01-dev-venv/bin/python (existing environment; no installation)',
      'requested_per_case_time_limit':args.time_limit,'cpu_seconds':time.process_time()-start,'wall_seconds':time.monotonic()-wall,'rows':rows,
      'counterexample_found':any(r.get('exact_valid_counterexample',False) for r in rows)}
 (HERE/(args.prefix+'.json')).write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('points','projective_lines','automorphism_generators','rows')},indent=2))
 print([(r['case'],r['solver_status'],r['solver_message']) for r in rows])
if __name__=='__main__':main()
