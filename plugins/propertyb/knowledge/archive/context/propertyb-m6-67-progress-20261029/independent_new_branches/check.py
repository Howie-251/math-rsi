"""Separate domain/selection and injection replay of three new branches."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,itertools,json,time
OUT=Path(__file__).resolve().parent;BASE=OUT.parent
s=importlib.util.spec_from_file_location('inj',BASE/'independent36_38/check.py');i=importlib.util.module_from_spec(s);s.loader.exec_module(i)


def main():
 start=time.process_time();replay=[];arithmetic=[]
 # Complete35/min9 integer budgets, not just its six-type table.
 assert 396-35*9==81
 for u in range(23,28):
  n=34-u;lmin=2*n-11
  assert lmin==57-2*u and 3*u+2*lmin>=87>81
  for e in(9,10):
   available=81-3*u-(e-9);pool=u+35-5*e
   assert pool>0
   if available<0:continue
   upper=12+available//pool
   assert upper==(12 if e==9 else upper)and upper<=(12 if e==9 else 13)
   arithmetic.append(dict(u=u,e=e,lambda2_count_lower=lmin,common_unit_pool_lower=pool,remaining_degree_excess=available,center_upper=upper))
 expected={(ds,t)for ds in((12,9,9),(12,9,10),(13,9,10))for t in(0,1)}
 data=json.loads((BASE/'root/LOW_PAIR_CENTER35.json').read_text());assert{(tuple(r['ds']),r['tau'])for r in data['rows']}==expected
 for r in data['rows']:
  ds=r['ds'];t=r['tau'];blocks=[7]*t+[3]*(1-t)+[5]*(1-t)+[6]*(2-t)
  ell=i.ell_for(ds,blocks);assert ell=={int(T):n for T,n in r['ell'].items()if n}
  u=i.bound(35,r['pos'],ell,True);assert u==Q(r['U'])<1
  replay.append(dict(branch='v35_min9_new',degrees=ds,tau=t,U=str(u),submitted_U=r['U'],positions=r['pos']))
 # Imported adaptive cases minunitpartner9/10/11: reconstruct complete ranges.
 A=json.loads((BASE/'mid34_38/ADAPTIVE_COMPONENT.json').read_text());original_quota=i.linkquota.quota
 i.linkquota.quota=lambda v,f:max(0,-(-(5*f-(v-1))//4))
 for e in(9,10,11):
  n=23;t=n-1-(5*e-34);fmax=e+(81-n*(e-9))//t;assert t>0
  rr=[r for r in A['rows']if r['v']==35 and r['degrees'][:2]==[9,e]and len(r['degrees'])==3]
  assert{(tuple(r['degrees']),tuple(r['blocks']))for r in rr}=={((9,e,f),bs)for f in range(e,fmax+1)for bs in((3,5,6),(7,))}
  for r in rr:
   assert sorted(r['assigned'])==sorted(r['degrees']);ell=i.ell_for(r['assigned'],r['blocks']);u=i.bound(35,r['positions'],ell,False)
   if u>=1:u=i.bound(35,r['positions'],ell,False,True)
   if u>=1:
    i.linkquota.quota=original_quota
    u=i.bound(35,r['positions'],ell,True,True)
    i.linkquota.quota=lambda v,f:max(0,-(-(5*f-(v-1))//4))
   assert u<1,(r,u)
   replay.append(dict(branch='v35_min9_adaptive',degrees=r['degrees'],blocks=r['blocks'],U=str(u),submitted_U=r['U'],positions=r['positions']))
 i.linkquota.quota=original_quota
 # Complete35/min11 actual Rdegree11 set and specified unit edge.
 assert 35*12-396==24 and 24-1-(55-34)>=1 and 110<70+48-6
 data=json.loads((BASE/'mid34_38/MIN11_35.json').read_text());rows=data['three']
 assert{(r['double'],r['tau'])for r in rows}=={(a,t)for a in(-1,0,1,2)for t in(0,1)}
 for r in rows:
  target=[1,1,1]
  if r['double']>=0:target[r['double']]=2
  t=r['tau'];blocks=([7]if t else[])
  for (a,b),l in zip(itertools.combinations(range(3),2),target):blocks +=[(1<<a)|(1<<b)]*(l-t)
  assert sorted(blocks)==sorted(r['blocks']);ell=i.ell_for((11,11,11),blocks);u=i.bound(35,r['positions'],ell)
  assert u==Q(r['U'])<1
  replay.append(dict(branch='v35_min11',double=r['double'],tau=t,U=str(u),submitted_U=r['U'],positions=r['positions']))
 #34/min11 harmonic cardinality envelope and rigid equality case.
 relaxed=[]
 for r in range(12,35):
  b=34-r
  for c in range(b+1):
   a=b-c
   if not(a>0 and a+3*c<=22 and b>=11):continue
   # a >= sum_x (u_x-c)/(u_x-10) >= r*a/(b-10).
   if b-10>=r:relaxed.append((r,a,c))
 assert relaxed==[(12,22,0)]
 for b in range(11,23):
  for c in range(min(7,b)+1):
   for u in range(11,b+1):
    assert Q(u-c,u-10)>=Q(b-c,b-10)
 data=json.loads((BASE/'34_min11/CERTIFICATE.json').read_text());rows=data['rows']
 expected={('unit_pair',11,None)}|{('low_center_wedge',d,t)for d in(12,13)for t in(0,1)}|{('rigid_special_four',11,t)for t in range(4)}
 assert{(r['kind'],r['degrees'][0],r.get('tau'))for r in rows}==expected
 for r in rows:
  kind=r['kind'];ds=r['degrees'];t=r.get('tau')
  if kind=='unit_pair':ell=i.ell_for(ds,[3])
  elif kind=='low_center_wedge':ell=i.ell_for(ds,[7]*t+[3]*(1-t)+[5]*(1-t)+[6]*(2-t))
  else:ell=i.ell_for(ds,[7]*t+[3]*(3-t)+[5]*(3-t)+[6]*(3-t)+[9,10,12])
  assert ell=={int(T):n for T,n in r['ell'].items()if n};u=i.bound(34,r['positions'],ell,True);assert u==Q(r['U'])<1
  replay.append(dict(branch='v34_min11',kind=kind,degrees=ds,tau=t,U=str(u),submitted_U=r['U'],positions=r['positions']))
 summaries=[]
 for name in('v35_min9_new','v35_min9_adaptive','v35_min11','v34_min11'):
  rr=[r for r in replay if r['branch']==name];summaries.append(dict(branch=name,profiles=len(rr),maximum=str(max(Q(r['U'])for r in rr))))
 out=dict(status='PASS_WITH_DECLARED_IMPORTS',review_independence='same-family',acceptance_status='provisional',declared_imports=['minimalcounterexample reduction and original conditional probability mechanism','component quota: auditor authored lemma; independent mathematical audit and table reconstruction exist elsewhere'],rows=summaries,complete35min9_budget=arithmetic,harmonic_relaxation=relaxed,cpu_seconds=time.process_time()-start,replay=replay)
 (OUT/'CHECK.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items()if k not in('replay','complete35min9_budget')},indent=2))
if __name__=='__main__':main()
