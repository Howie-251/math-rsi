"""Independent retained815 inside-partner domain and raw fixed-layout replay.
Uses the separately generated95 minimum-potential stars from the complete
4140-partition check; no original triangle generator or coefficient code imported.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations,product
from collections import Counter
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();N=16
orig=json.loads((P/'A7_TRIANGLE_DOMAIN.json').read_text());f=next(z for z in orig['results'] if z['base']==19 and z['partner']==4);mu={int(t):n for t,n in f['core_counts'].items()}
cut=json.loads((P/'A7_EMPTY_MIN_CORE19_CHECK.json').read_text());assert cut['passed'];stars={tuple(sorted((int(t),n) for t,n in z['nonempty_star'].items())) for r in cut['results'] if r['partner']==4 for z in r['stars']};assert len(stars)==95
fil=json.loads((P/'A7_MINIMUM_EMPTY_FILTER.json').read_text());indices=[z['case_index'] for r in fil['results'] if r['partner']==4 for z in r['retained_cases']]
screen=json.loads((P/'A7_MINIMUM_EMPTY_TEMPLATE_SCREEN.json').read_text());positions=screen['positions'];selected={z['case_index']:z for z in screen['results']}
def act(pp,g):return tuple(sorted((g[t],n) for t,n in pp))
def C(n,k):return comb(n,k) if 0<=k<=n else 0

def raw(ns,pos):
 total=Q(0)
 for k in range(1,26):
  left=sum(1<<i for i,p in enumerate(pos) if p<k);right=sum(1<<i for i,p in enumerate(pos) if p>k);pivot=next((1<<i for i,p in enumerate(pos) if p==k),0);a=k-1-left.bit_count();b=25-k-right.bit_count()
  def ew(t,side,slots):
   r=5-t.bit_count()
   if pivot:
    if not t&pivot or (t^pivot)&~side:return Q(0)
    return Q(C(slots,r),C(N,r))
   if not r or t&~side:return Q(0)
   return Q(r*C(slots,r-1),N*C(N-1,r-1))
  def pw(t,u):
   r=5-t.bit_count();q=5-u.bit_count()
   if pivot:
    if t&u!=pivot or (t^pivot)&~left or (u^pivot)&~right or r+q>N:return Q(0)
    return Q(C(a,r)*C(b,q),C(N,r)*C(N-r,q))
   if not r or not q or t&u or t&~left or u&~right or r+q-1>N:return Q(0)
   return Q(C(a,r-1)*C(b,q-1),N*C(N-1,r-1)*C(N-r,q-1))
  A=sum(n*ew(t,left,a) for t,n in ns.items());B=sum(n*ew(t,right,b) for t,n in ns.items());D=sum(n*(m-(t==u))*pw(t,u) for t,n in ns.items() for u,m in ns.items());total+=min(A,B,D)
 return total

groups=[]
for mm in permutations(range(7)):
 if mm[4]!=4 or {mm[j] for j in range(4,7)}!=set(range(4,7)):continue
 groups.append([sum(1<<mm[j] for j in range(7) if t>>j&1) for t in range(128)])
assert len(groups)==48
roots={min(act(p,g) for g in groups) for p in stars};expected=set()
for ps in roots:
 p=dict(ps);p[0]=7-sum(p.values());stab=[g for g in groups if act(ps,g)==ps]
 for rs in stars:
  r=dict(rs);r[0]=7-sum(r.values());common=sorted(set(p)&set(r))
  for vv in product(*(range(max(0,p[t]+r[t]-mu[t]),min(p[t],r[t])+1) for t in common)):
   q=dict(zip(common,vv))
   if not 2<=sum(q.values())<=4:continue
   ns={};ok=True
   for t,n in mu.items():
    a=p.get(t,0);b=r.get(t,0);c=q.get(t,0);cells=[n-a-b+c,a-c,b-c,c]
    if min(cells)<0:ok=False;break
    for mask,z in enumerate(cells):
     if z:ns[t+128*mask]=z
   if not ok or any(t.bit_count()>5 for t in ns):continue
   expected.add(min(tuple(sorted(((t&384)|g[t&127],n) for t,n in ns.items())) for g in stab))
actual={tuple(sorted((int(t),n) for t,n in f['cases'][idx]['counts'].items())) for idx in indices};assert len(indices)==len(actual)==815 and actual==expected
records=[]
for idx in indices:
 ns={int(t):n for t,n in f['cases'][idx]['counts'].items()};z=selected[idx];pos=positions[z['position_index']];bound=raw(ns,pos);assert bound==Q(z['minimum_raw']) and bound<1;records.append(dict(case_index=idx,positions=pos,raw_ABC_bound=str(bound)))
# Bind the structural re-rooting and the transported exceptional layout.
rr=json.loads((P/'A7_MINIMUM_EMPTY_REROOT.json').read_text());m=rr['old_to_new'];assert sorted(m)==list(range(9))
a={int(t):n for t,n in f['cases'][rr['source_case']]['counts'].items()};b={int(t):n for t,n in f['cases'][rr['target_case']]['counts'].items()}
assert {sum(1<<m[i] for i in range(9) if t>>i&1):n for t,n in a.items()}==b
assert rr['source_positions']==[rr['target_positions'][m[i]] for i in range(9)]
assert raw(a,rr['source_positions'])==raw(b,rr['target_positions'])==Q('38583/40040')
out=dict(scope=__doc__,passed=True,domain_complete=True,independent_stars=95,independent_joint_inputs=len(expected),all_raw_strict=True,maximum_raw=str(max(Q(z['raw_ABC_bound']) for z in records)),records=records,elapsed_seconds=time.perf_counter()-st)
(P/'A7_MINIMUM_EMPTY_INSIDE_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['passed','domain_complete','independent_stars','independent_joint_inputs','all_raw_strict','maximum_raw','elapsed_seconds']},indent=2))
