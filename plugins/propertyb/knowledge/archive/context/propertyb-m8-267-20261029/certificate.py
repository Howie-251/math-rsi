"""Complete M266 k8 certificate, fixed successful layouts, no layout search.
Uses the existing binomial probability engine and the new seven-link
component quota. This is an author-side replay, not an independent checker.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations,combinations_with_replacement
from collections import Counter
import importlib.util,json,time,signal
HERE=Path(__file__).resolve().parent
START=time.process_time()
spec=importlib.util.spec_from_file_location('seven_link_components',HERE/'component_trial.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
m=p.m
signal.setitimer(signal.ITIMER_PROF,35)
signal.alarm(90)
used_quotas=set();old_quota=p.quota

def recorded_quota(f,N):
 q=old_quota(f,N);used_quotas.add((f,N,q));return q
p.quota=recorded_quota
strong=p.Strong(8,266)
original=m.Calculator(8,266)


def norm(ell):return {int(t):n for t,n in ell.items()if n}

def triple(ds,tri):
 d,e,f=ds
 return {0:268-d-e-f,1:d-1,2:e-1,4:f-1,7:1}if tri else{0:269-d-e-f,1:d-2,2:e-2,4:f-2,3:1,5:1,6:1}


def main():
 initial=json.loads((HERE/'INITIAL.json').read_text())
 trial=json.loads((HERE/'COMPONENT_TRIAL.json').read_text())
 adapt=json.loads((HERE/'ADAPTIVE_TRIAL.json').read_text())
 rows=[];coverage=[];balanced=[]
 for v in range(15,47):
  value=Q(266*(m.C(v//2,8)+m.C(v-v//2,8)),m.C(v,8));assert value<1
  balanced.append(dict(v=v,U=str(value)))
 assert 121*m.CEIL(120,7)==2178>2128
 assert all(v*m.CEIL(v-1,7)<=2128 for v in range(47,121))
 assert m.C(47,8)>=266

 def add(row,method,ell=None):
  v=row['v']
  if method=='zero':value=original.unlocked(v);actual_ell={0:266}
  else:
   actual_ell=norm(ell if ell is not None else row['ell'])
   assert sum(actual_ell.values())==266 and min(actual_ell.values())>=0
   value=(original if method=='old_pool'else strong).bound(v,tuple(row['positions']),actual_ell)
   for j,d in enumerate(row['degrees']):assert sum(n for t,n in actual_ell.items()if t>>j&1)==d
  assert value==Q(row['U'])<1,(row,value)
  rows.append(dict(row,ell=actual_ell,U=str(value),strict=True,deletion=method))
 for v in range(47,83):
  rr=[r for r in initial['rows']if r['v']==v and r['kind']=='zero'];assert len(rr)==1;add(rr[0],'zero')
  coverage.append(dict(v=v,method='zero',profiles=1))
 for v in range(83,90):
  ds=list(range(m.CEIL(v-1,7),2128//v+1))
  rr=[r for r in trial['rows']if r['v']==v and r['kind']=='one']
  assert sorted(r['degrees'][0]for r in rr)==ds
  for r in rr:add(r,'component_max_R')
  coverage.append(dict(v=v,method='all_minimum_degrees_one_lock',profiles=len(rr),minimum_degrees=ds))
 for v in range(90,108):
  pair_rows=[r for r in trial['rows']if r['v']==v and r['kind']=='two']
  expected={(d,e)for d in range(m.CEIL(v-1,7),2128//v+1)for e in range(d,d+(2128-v*d)//(2*(v-1)-7*d)+1)}
  assert len(pair_rows)==len(expected)and{tuple(r['degrees'])for r in pair_rows}==expected
  for r in pair_rows:
   d,e=r['degrees'];n=2*(v-1)-7*d;assert n>0
   if r['strict']:
    add(r,'component_max_R');coverage.append(dict(v=v,d=d,e=e,method='two',profiles=1))
   else:
    t=n-1-(7*e-(v-1));assert t>0
    excess=2128-v*d-n*(e-d);fmax=e+excess//t
    rr=[z for z in adapt['rows']if z['v']==v and z['kind']=='adaptive_three'and z['degrees'][:2]==[d,e]]
    expected3={(f,tri)for f in range(e,fmax+1)for tri in(0,1)}
    assert len(rr)==len(expected3)and{(z['degrees'][2],z['tri'])for z in rr}==expected3
    for z in rr:
     ell=triple(z['degrees'],z['tri']);assert norm(ell)==norm(z['ell']);add(z,'component_max_R',ell)
    coverage.append(dict(v=v,d=d,e=e,method='adaptive_three',n=n,t=t,degree_surplus=excess,fmax=fmax,profiles=len(rr)))
 for v in range(108,120):
  d0=m.CEIL(v-1,7);Z=21*v-2128;T=149-v
  assert Z>0 and 14*Z>T*T
  rr=[r for r in initial['rows']if r['v']==v and r['kind']=='three']
  expected={(ds,tri)for ds in combinations_with_replacement(range(d0,21),3)for tri in(0,1)}
  assert len(rr)==len(expected)and{(tuple(r['degrees']),r['tri'])for r in rr}==expected
  for r in rr:
   ell=triple(r['degrees'],r['tri']);assert norm(ell)==norm(r['ell']);add(r,'old_pool',ell)
  coverage.append(dict(v=v,method='three_low_unit',D=20,Z=Z,T=T,CW_gap=14*Z-T*T,profiles=len(rr)))
 # v120 all degree>=17; at least32 have degree17, hence are globally unit.
 assert 18*120-2128==32 and 7*17==119
 masks=[b for b in range(1,16)if b.bit_count()>=2];pairs=list(combinations(range(4),2));patterns=set()
 for chosen in range(1<<len(masks)):
  bs=tuple(b for i,b in enumerate(masks)if chosen>>i&1)
  if all(sum(bool(b>>i&1 and b>>j&1)for b in bs)==1 for i,j in pairs):patterns.add(bs)
 assert len(patterns)==6
 rr=[r for r in adapt['rows']if r['kind']=='four17'];assert len(rr)==6
 assert {tuple(sorted(r['blocks']))for r in rr}==patterns
 for r in rr:add(r,'component_max_R')
 coverage.append(dict(v=120,method='four17',low17_count_lower=32,globally_unit=True,profiles=6))
 assert len(rows)==2094
 counts=Counter(r['kind']for r in rows)
 summary=[]
 for kind in sorted(counts):
  rr=[r for r in rows if r['kind']==kind];worst=max(rr,key=lambda r:Q(r['U']))
  summary.append(dict(kind=kind,profiles=len(rr),maximum=worst['U'],worst_v=worst['v'],worst_degrees=worst.get('degrees')))
 out=dict(status='COMPLETE_PAPER_CANDIDATE',k=8,M=266,conclusion='m(8)>=267',vertex_domain=[47,120],degree_budget=2128,
          role='Author-side complete exact-rational local certificate; no independent verification, cross-family review or Lean claimed',
          profiles=len(rows),all_strict=True,maximum=str(max(Q(r['U'])for r in rows)),
          component_link_uniformity=7,component_support_bounds=['7*ceil(t^2/(t+2e))','7*ceil((2t-e-1)/2)','8 for t>=2','15 if e<C(t,2)-floor(t/2)'],
          component_DP_scope=dict(maximum_family_size=p.FMAX,maximum_intersection_budget=p.QMAX),
          quotas=[dict(f=f,N=N,q=q)for f,N,q in sorted(used_quotas)],balanced=balanced,coverage=coverage,summary=summary,rows=rows,
          cpu_seconds=time.process_time()-START)
 (HERE/'CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
 (HERE/'SUMMARY.json').write_text(json.dumps({k:v for k,v in out.items()if k not in('rows','quotas','balanced','coverage')},indent=2)+'\n')
 print(json.dumps({k:v for k,v in out.items()if k not in('rows','quotas','balanced','coverage')},indent=2))


if __name__=='__main__':main()
