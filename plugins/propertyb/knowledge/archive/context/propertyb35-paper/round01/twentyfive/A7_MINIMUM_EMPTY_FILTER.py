"""Apply only new minimum-empty private-star necessity to all7059 existing
core19 triangle inputs. No new domain enumeration, layouts or probability DP.
Use previously computed exact fixed-screen bounds for the retained residuals.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();domain=json.loads((P/'A7_TRIANGLE_DOMAIN.json').read_text());screen=json.loads((P/'A7_TRIANGLE_FIXED_SCREEN.json').read_text());out=[]
def check(star,i):
 pp={int(t):n for t,n in star.items()};r=7-sum(pp.values());s=pp.get(1<<i,0);a=pp.get(112,0);qout=sum(n for t,n in pp.items() if t.bit_count()==2 and not t>>i&1);inside=bool(112>>i&1)
 assert r+s==1+qout+(a if inside else 2*a)
 new_empty=(7-qout-a) if inside else (6-qout-2*a)
 assert new_empty==6-r+(2 if inside else 1)-s
 keep=new_empty>=6
 assert keep==(a+qout<=1 if inside else a==qout==0)
 return dict(keep=keep,r=r,s=s,a=a,q_out=qout,new_empty=new_empty)
for f in domain['results']:
 if f['base']!=19:continue
 i=f['partner'];sc=next(z for z in screen['families'] if (z['base'],z['partner'])==(19,i));res={z['case_index']:z for z in sc['residual']};kept=[];why=[]
 for idx,z in enumerate(f['cases']):
  x=check(z['P'],i);y=check(z['Q'],i)
  if x['keep'] and y['keep']:kept.append(dict(case_index=idx,P=x,Q=y,was_fixed_residual=idx in res,minimum_raw=res[idx]['minimum_raw'] if idx in res else None))
  else:why.append(dict(case_index=idx,failed_x=not x['keep'],failed_y=not y['keep']))
 retained_res=[z for z in kept if z['was_fixed_residual']];maximum=max((Q(z['minimum_raw']) for z in retained_res),default=None)
 out.append(dict(base=19,partner=i,original=len(f['cases']),original_fixed_residual=len(res),retained=len(kept),retained_fixed_strict=len(kept)-len(retained_res),retained_fixed_residual=len(retained_res),maximum_minimum_raw=str(maximum) if maximum is not None else None,maximum_exact_if_any_residual=bool(retained_res),retained_cases=kept,deleted=why));print(i,len(f['cases']),len(kept),len(retained_res),maximum,flush=True)
summary=dict(scope=__doc__,original=sum(z['original'] for z in out),retained=sum(z['retained'] for z in out),original_fixed_residual=sum(z['original_fixed_residual'] for z in out),retained_fixed_residual=sum(z['retained_fixed_residual'] for z in out),elapsed_seconds=time.perf_counter()-st)
(P/'A7_MINIMUM_EMPTY_FILTER.json').write_text(json.dumps(dict(summary=summary,results=out),indent=2)+'\n');print(json.dumps(summary,indent=2))
