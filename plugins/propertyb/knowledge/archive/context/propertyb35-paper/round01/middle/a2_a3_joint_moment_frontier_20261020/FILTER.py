"""Full A2/A3 degree-spectrum moment relaxation; threshold T only, no A1 n4 cap."""
from pathlib import Path
from functools import lru_cache
from math import comb
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.process_time()
source=json.loads((P.parent/'unique_six_two_three_seven_transfer_20261020/CHECK.json').read_text())
def f(s):
 a,r=divmod(s,5)
 return (s*s-(5-r)*a*a-r*(a+1)**2)//2
@lru_cache(None)
def T(n,m,r):
 if not 0<=m<=n*(n-1)//2:return -10**12
 if n==0:return 0
 return max(f(r)+T(n-1,m,r),f(n-1+r)+T(n-1,m-n+1,r+1))
table={m:T(35,m,0) for m in range(397,596)}
old=json.loads((P.parent/'a1_middle_wedge_capacity_20261020/GRAPH_PILOT.json').read_text())['threshold_Pmax']
assert all(table[int(k)]==int(v) for k,v in old.items())
spectra={};role_rows=0
for row in source['role_parameter_rows']:
 for s in row['spectra']:
  role_rows+=1;a=row['a'];b=row['b'];part=s['positive_high_excess_partition'];h=20-a-b
  ds=tuple(sorted([6]+[7]*a+[8]*b+[9]*(h-len(part))+[9+q for q in part]))
  assert len(ds)==21 and sum(ds)==175 and sum(comb(d,2) for d in ds)==s['W']
  key=','.join(map(str,ds))
  spectra.setdefault(key,{'a':a,'b':b,'partition':part,'e':row['high_excess'],'W':s['W'],'degrees':list(ds),'role_parameters':[]})['role_parameters'].append([a,row['r_nonunit7'],b])
assert role_rows==32 and len(spectra)==16
moment_cache={};jobs=[];all_survivors=[]
for key,spec in spectra.items():
 W=spec['W'];e=spec['e'];degrees=spec['degrees'];assert sum(sorted(degrees)[-6:])==54+e
 caps2=24+e//2;cost={}
 for n1 in range(397,596):
  left=n1;c=0
  for d in degrees:
   take=min(left,comb(d,2));left-=take;c+=d*take
  assert left==0
  cost[n1]=c
 if W not in moment_cache:
  rows=[];before_wedge=0
  for tau in range(141):
   for t in range((140+tau)//6+1):
    a,b=divmod(2*t,35);wedges=(35-b)*comb(a,2)+b*comb(a+1,2)
    for m in range((140+tau-6*t)//3+1):
     n1=W-280-2*tau+3*m+8*t;n2=140+tau-3*m-6*t;n0=735-W+tau-m-3*t
     if min(n0,n1,n2)<0 or not 397<=n1<=595:continue
     before_wedge+=1
     if 3*wedges>4*tau:continue
     rows.append((n0,n1,n2,m,t,tau))
  moment_cache[W]=(before_wedge,rows)
 before,rows=moment_cache[W];survivors=[]
 for n0,n1,n2,m,t,tau in rows:
  cap=(33*n0,35*n1-cost[n1],caps2*n2,14*m,4*t)
  rem=table[n1];cc=[0]*5
  for j in (4,3,2,1,0):cc[j]=min(cap[j],rem);rem-=cc[j]
  L2=sum(c*w for c,w in zip(cc,(36,120,330,792,1716)))+6864*n1
  if L2>=5445440:
   q={'n':[n0,n1,n2,m,t],'tau':tau,'P':table[n1],'C_caps':list(cap),'C':cc,'twice_L':L2}
   survivors.append(q)
 job={**spec,'unique_degree_key':key,'C2_multiplier':caps2,'moment_count_before_wedges':before,'moment_count_after_wedges':len(rows),'survivor_count':len(survivors)}
 if survivors:
  job['t_range']=[min(q['n'][4] for q in survivors),max(q['n'][4] for q in survivors)]
  job['tau_range']=[min(q['tau'] for q in survivors),max(q['tau'] for q in survivors)]
  job['n1_range']=[min(q['n'][1] for q in survivors),max(q['n'][1] for q in survivors)]
  job['minimum_high_witness']=min(survivors,key=lambda q:(q['n'][3]+q['n'][4],q['tau'],q['n'][4],q['n'][3]))
  job['minimum_tau_witness']=min(survivors,key=lambda q:(q['tau'],q['n'][4],q['n'][3]))
  job['closest_margin_witness']=min(survivors,key=lambda q:q['twice_L']-5445440)
 for q in survivors:all_survivors.append({'unique_degree_key':key,**q})
 jobs.append(job)
 print(spec['a'],spec['b'],spec['partition'],'W',W,'e',e,'domain',len(rows),'survivors',len(survivors),'range',job.get('t_range'),job.get('tau_range'),flush=True)
 assert time.process_time()-st<27,'bounded CPU cutoff'
summary={'scope':__doc__,'complete':True,'source_role_spectrum_rows':role_rows,'unique_degree_spectra':len(spectra),'threshold_n1_complete_range':[397,595],'threshold_matches_old_saved_table':True,'threshold_cache_entries':T.cache_info().currsize,'jobs':jobs,'survivor_count_with_spectrum_labels':len(all_survivors),'distinct_moment_keys_surviving':len({(tuple(q['n']),q['tau']) for q in all_survivors}),'cpu_seconds':time.process_time()-st}
(P/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
(P/'SURVIVORS.json').write_text(json.dumps(all_survivors,indent=2)+'\n')
(P/'THRESHOLD_TABLE.json').write_text(json.dumps(table,indent=2)+'\n')
print('SUMMARY',len(all_survivors),summary['distinct_moment_keys_surviving'],summary['cpu_seconds'])
