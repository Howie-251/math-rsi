"""One bounded continuation of exact nine-lock DP; reuse PROFILE cases.
Stop at the first nonstrict corrected optimum or 45 CPU seconds.
"""
from pathlib import Path
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[5]
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from subset_position_dp import SubsetEngine
from bare_layout import BareLayout
D=json.loads((P/'DOMAIN.json').read_text());profile=json.loads((P/'PROFILE.json').read_text());records=D['records']
oldprofile={(z['base'],tuple(z['low'])):z for z in profile['records']}
groups={}
for z in records:groups.setdefault((tuple(z['canonical_large']),z['canonical_lowmask']),[]).append(z)
def convert(x):
 if isinstance(x,Fraction):return str(x)
 if isinstance(x,dict):return {str(k):convert(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)):return [convert(v) for v in x]
 return x
start=time.process_time();done=[];reason='complete';first_fail=None;processed=set()
for key,zz in groups.items():
 if time.process_time()-start>=45:reason='cpu_budget';break
 z=zz[0];ns={int(t):n for t,n in z['counts'].items()}
 tm=time.process_time()
 if Fraction(z['old_17_layout_bound'])<1:
  eng=SubsetEngine(25,9,ns)
  w=eng.verify({'bound':Fraction(z['old_17_layout_bound']),'positions':z['old_positions'],'counts':ns})
  entry={'base':z['base'],'low':z['low'],'source':'old_q6_affine_layout_actual_row_replay','new_cpu_seconds':time.process_time()-tm,**w}
 elif (z['base'],tuple(z['low'])) in oldprofile:
  entry=dict(oldprofile[(z['base'],tuple(z['low']))]);entry['source']='reused_PROFILE_exact_DP';entry['new_cpu_seconds']=0
 else:
  eng=SubsetEngine(25,9,ns);w=eng.verify(eng.solve())
  entry={'base':z['base'],'low':z['low'],'source':'new_bounded_exact_DP','new_cpu_seconds':time.process_time()-tm,**w}
 entry['raw_witness_bound']=BareLayout(25,entry['positions']).bound(ns)
 entry['colored_orbit_labels']=[z0['low'] for z0 in zz]
 entry['orbit_size']=len(zz);entry['canonical_large']=key[0];entry['canonical_lowmask']=key[1]
 done.append(entry);processed.add(key)
 print('orbit',len(done),'base',z['base'],'low',z['low'],'bound',entry['bound'],'source',entry['source'],'CPU',entry['new_cpu_seconds'],flush=True)
 if Fraction(entry['bound'])>=1:
  reason='first_nonstrict_exact_DP';first_fail=entry;break
remaining=[{'base':zz[0]['base'],'low':zz[0]['low'],'low_labels':[z['low'] for z in zz],
            'canonical_large':key[0],'canonical_lowmask':key[1]} for key,zz in groups.items() if key not in processed]
out={'complete_domain_imported':True,'complete_probability_pass':not remaining and first_fail is None,
     'stop_reason':reason,'domain_marked_inputs':140,'domain_colored_orbits':105,
     'processed_orbits':len(done),'processed_labels':sum(z['orbit_size'] for z in done),
     'strict_processed_orbits':sum(Fraction(z['bound'])<1 for z in done),
     'remaining_orbits':len(remaining),'remaining_labels':sum(len(z['low_labels']) for z in remaining),
     'first_nonstrict':first_fail,'remaining':remaining,'records':done,
     'new_cpu_seconds':time.process_time()-start,'prior_profile_cpu_seconds':profile['profile_cpu_seconds']}
(P/'RESULT.json').write_text(json.dumps(convert(out),indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['records','remaining','first_nonstrict']},indent=2))
