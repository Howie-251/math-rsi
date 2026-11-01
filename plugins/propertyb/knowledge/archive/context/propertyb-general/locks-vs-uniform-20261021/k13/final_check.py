import json,time,itertools
from scan import *
from propertyB_k10_k11_certified import FixedCertificate
start=time.monotonic();m=9544;v=972;d=e=81
cal=FixedCertificate(K,m)
vals={'none':cal.unlocked(v),'one_d81':cal.one(v,d),'two_d81_e81':cal.two(v,d,e)}
for z in vals.values():assert z>=S
Ds=[(2*KM1*((D+1)*v-K*m)-(KM1*(D+1)-v+2)**2,D,(D+1)*v-K*m) for D in range(CEIL(v-1,KM1),m+1) if (D+1)*v>K*m]
best=max(Ds);assert best[0]<=0
proof={'k':K,'M':m,'v':v,'d':d,'e':e,'S':S,'exact_scalar':vals,'gaps':{k:S-z for k,z in vals.items()},'three_complete_D_domain':[CEIL(v-1,KM1),m],'three_max_strict_difference':best[0],'three_best_D':best[1],'three_Z':best[2],'wall_seconds':time.monotonic()-start}
print(json.dumps(proof),flush=True)
(OUT/'FINAL_FAILURE_SCALAR.json').write_text(json.dumps(proof,indent=2))
x=json.loads((OUT/'M9544-hybrid.json').read_text());x['uncovered_v']=972;x['total_profiles_selected_prefix']=sum(r['profiles'] for r in x['rows']);x['remaining_v']=[972,max(x['candidate_v'])];x['actual_prefix_certified_v']=[min(x['candidate_v']),971]
for r in x['rows']:
 v=r['v'];d0=CEIL(v-1,KM1);hi=K*m//v;r['d0']=d0;r['minimum_degree_upper']=hi
 if r['mode']=='one':r['degree_range']=[d0,hi];assert r['profiles']==hi-d0+1
 if r['mode']=='hybrid':
  assert [b['d'] for b in r['branches']]==list(range(d0,hi+1))
  assert r['profiles']==sum(b['profiles'] for b in r['branches'])
  for b in r['branches']:
   if b['mode']=='two':assert b['e_min']==b['d'] and b['profiles']==b['e_max']-b['d']+1
x['phases']=[]
for mode,g in itertools.groupby(x['rows'],key=lambda r:r['mode']):
 rs=list(g);x['phases'].append({'mode':mode,'v_min':rs[0]['v'],'v_max':rs[-1]['v'],'profiles':sum(r['profiles'] for r in rs),'worst':max(rs,key=lambda r:r['worst_z'])})
(OUT/'M9544-hybrid.json').write_text(json.dumps(x,indent=2))
print('phases',[(r['mode'],r['v_min'],r['v_max'],r['profiles']) for r in x['phases']],flush=True)
