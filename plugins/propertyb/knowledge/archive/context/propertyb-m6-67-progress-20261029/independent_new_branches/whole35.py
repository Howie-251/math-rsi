"""Incremental audit completing35-point coverage; prior audited rows are loaded."""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,itertools,json,time
OUT=Path(__file__).resolve().parent;BASE=OUT.parent
s=importlib.util.spec_from_file_location('prior',OUT/'check.py');prior=importlib.util.module_from_spec(s);s.loader.exec_module(prior);i=prior.i

def replay_adaptive_row(r,branch):
 ell=i.ell_for(r['assigned'],r['blocks']);u=i.bound(35,r['positions'],ell,True)
 if u>=1:u=i.bound(35,r['positions'],ell,True,True)
 assert u<1,(r,u)
 return dict(branch=branch,degrees=r['degrees'],blocks=r['blocks'],assigned=r['assigned'],positions=r['positions'],U=str(u),submitted_U=r['U'])

def initial():
 start=time.process_time();A=json.loads((BASE/'mid34_38/ADAPTIVE_COMPONENT.json').read_text());rows=[];domains=[]
 for delta in(7,8):
  n=68-5*delta;emax=delta+(396-35*delta)//n;branches=[b for b in A['branches']if b['v']==35 and b['d']==delta];assert{b['e']for b in branches}==set(range(delta,emax+1))
  for b in branches:
   e=b['e'];rr=[r for r in A['rows']if r['v']==35 and r['degrees'][:2]==[delta,e]]
   if b['status']=='two_pass':
    rr=[r for r in rr if len(r['degrees'])==2];assert len(rr)==1
   else:
    t=n-1-(5*e-34);assert t>0;fmax=e+(396-35*delta-n*(e-delta))//t
    rr=[r for r in rr if len(r['degrees'])==3];assert{(tuple(r['degrees']),tuple(r['blocks']))for r in rr}=={((delta,e,f),bs)for f in range(e,fmax+1)for bs in((3,5,6),(7,))}
   domains.append(dict(delta=delta,e=e,profiles=len(rr),status=b['status']))
   for r in rr:rows.append(replay_adaptive_row(r,f'v35_min{delta}'))
 out=dict(status='delta7/8PASS;delta10pending',domains=domains,replay=rows,cpu_seconds=time.process_time()-start)
 (OUT/'WHOLE35_INCREMENT.json').write_text(json.dumps(out,indent=2));print(len(rows),out['cpu_seconds'])

def finish():
 start=time.process_time();previous=json.loads((OUT/'CHECK.json').read_text());increment=json.loads((OUT/'WHOLE35_INCREMENT.json').read_text());data=json.loads((BASE/'mid34_38/CERT35_MIN10.json').read_text());rows=[]
 assert 7==-(-34//5) and 396//35==11
 A=[r for r in data['rows']if r['group']=='exclude_unit_10_pair'];B=[r for r in data['rows']if r['group']=='exclude_two_unit_11_neighbors'];C=[r for r in data['rows']if r['group']=='low_pair_degree12_center']
 expected={(f,trace)for trace,upper in(('separate',49),('triple',48))for f in range(10,upper+1)}
 assert{(r['input_third_degree'],r['trace'])for r in A}==expected and len(A)==79
 # Original broad degreebound56 is not itself a nonnegative actualtrace bound.
 assert 396-20-32*10==56
 original_quota=i.linkquota.quota;old_quota=lambda v,f:max(0,-(-(5*f-(v-1))//4))
 for r in A:
  f=r['input_third_degree'];assert sorted(r['assigned_degrees'])==sorted((10,10,f))
  blocks=[3,5,6]if r['trace']=='separate'else[7];ell=i.ell_for(r['assigned_degrees'],blocks);assert ell=={int(T):n for T,n in r['ell'].items()if n}
  i.linkquota.quota=old_quota;u=i.bound(35,r['positions'],ell,False)
  if u>=1:u=i.bound(35,r['positions'],ell,False,True)
  if u>=1:
   i.linkquota.quota=original_quota;u=i.bound(35,r['positions'],ell,True,True)
  assert u<1,(r,u);rows.append(dict(branch='v35_min10_A',f=f,trace=r['trace'],U=str(u),submitted_U=r['U'],positions=r['positions']))
 i.linkquota.quota=original_quota
 expected={(l,t)for l in range(1,12)for t in(0,1)if 10-l+t>=0}
 assert{(r['lam_other'],r['tau'])for r in B}==expected and len(B)==21
 for r in B+C:
  l,t=r['lam_other'],r['tau'];ds=r['assigned_degrees'];ell=i.ell_for(ds,[7]*t+[3]*(1-t)+[5]*(1-t)+[6]*(l-t));assert ell=={int(T):n for T,n in r['ell'].items()if n}
  assert (ds==[10,11,11]and r in B)or(ds==[12,10,10]and r in C)
  u=i.bound(35,r['positions'],ell,True);assert u==Q(r['U'])<1;rows.append(dict(branch='v35_min10_B'if r in B else'v35_min10_C',lambda_other=l,tau=t,U=str(u),submitted_U=r['U'],positions=r['positions']))
 assert len(C)==2 and{r['tau']for r in C}=={0,1}
 # Complete actualdegree budgets for the contradiction-based lowpair selection.
 budget=[]
 for u in range(18,24):
  l=52-2*u;assert 2*u-1+l==51>46;budget.append(dict(u=u,lambda2_partner_lower=l,degree_excess_if_all_partners_high=51))
 for c in range(17,24):assert 34-c>0 and  2*c+(34-c)>=51>46
 retained=[r for r in previous['replay'] if not r['branch'].startswith(('v35_min7','v35_min8','v35_min10'))]
 allrows=retained+increment['replay']+rows
 summaries=[]
 for d in range(7,12):
  rr=[r for r in allrows if r['branch'].startswith(f'v35_min{d}')];assert rr
  summaries.append(dict(minimum=d,profiles=len(rr),maximum=str(max(Q(r['U'])for r in rr))))
 previous.update(status='PASS_WITH_DECLARED_IMPORTS',scope='Complete35pointbranch minimum7..11 plus34/min11 harmonic branch; prior verified rows retained, only incremental rows recomputed.',complete35_vertex=True,complete35_minimum_domain=list(range(7,12)),complete35_summary=summaries,complete35_profiles=sum(r['profiles']for r in summaries),minimum10_budget=budget,incremental_cpu_seconds=increment['cpu_seconds']+time.process_time()-start,replay=allrows)
 (OUT/'CHECK.json').write_text(json.dumps(previous,indent=2));print(json.dumps({k:previous[k]for k in('status','complete35_vertex','complete35_profiles','complete35_summary','incremental_cpu_seconds')},indent=2))

if __name__ == "__main__":
 initial()
 finish()
