"""Shared tau costs: four cross pairs plus both actual high-point rows.
Only filter the112 archived unique-lambda5 residual keys, no spectrum rescan.
"""
from pathlib import Path
from itertools import product
from math import comb
from collections import Counter
import json,time

P=Path(__file__).resolve().parent;START=time.process_time()
archive=json.loads((P/'ALL_EIGHTEEN_SCALAR_RESULT.json').read_text())
remaining=[(job,z) for job in archive['jobs'] for z in job['survivors']]
assert len(remaining)==112
CROSS=((0,2),(0,3),(1,2),(1,3))

def minimum_remaining_cost(slots,total_lambda):
    if not slots:
        return 0 if total_lambda==0 else None
    if not slots<=total_lambda<=4*slots:
        return None
    q,r=divmod(total_lambda,slots)
    return (slots-r)*comb(q-1,2)+r*comb(q,2)

# Place each high point either at one of four actual K labels or outside K.
# Both outside means distinct actual labels4 and5, not the same point.
roles=[]
for pu,pv in product(range(5),repeat=2):
    if pu==pv and pu<4:continue
    u=pu if pu<4 else 4
    v=pv if pv<4 else 5
    assert u!=v
    roles.append((u,v))
assert len(roles)==21

models={}
for du,dv in ((10,12),(11,11)):
    inputs=[]
    for u,v in roles:
        uv=tuple(sorted((u,v)))
        ranges=[(5,) if p==uv else range(1,5) for p in CROSS]
        for lambdas in product(*ranges):
            fixed={uv:5,**dict(zip(CROSS,lambdas))}
            assert fixed[uv]==5
            fixed_cost=sum(comb(lam-1,2) for lam in fixed.values())
            row_residual=[]
            for x,d in ((u,du),(v,dv)):
                known=[lam for pair,lam in fixed.items() if x in pair]
                cost=minimum_remaining_cost(20-len(known),4*d-sum(known))
                if cost is None:break
                row_residual.append(cost)
            if len(row_residual)!=2:continue
            kappa=fixed_cost+sum(row_residual)
            # Only uv belongs to both high rows and is in fixed exactly once.
            inputs.append({'u':u,'v':v,'cross_lambdas':lambdas,
                           'fixed_cost':fixed_cost,'remaining_row_costs':row_residual,
                           'minimum_global_tau':kappa,'cross_sum':sum(lambdas)})
    maxtau=max(z['tau'] for job,z in remaining if tuple(job['exception_pair'])==(du,dv))
    tables={}
    for tau in range(6,maxtau+1):
        feasible=[z for z in inputs if z['minimum_global_tau']<=tau]
        if feasible:
            witness=max(feasible,key=lambda z:z['cross_sum'])
            tables[tau]={'g':witness['cross_sum'],'cap_with_existing_c14':min(13,witness['cross_sum']),
                         'maximizer':witness,'feasible_role_assignments':len(feasible)}
    models[(du,dv)]={'high_degrees':[du,dv],'roles':roles,'complete_role_assignments':len(inputs),
                    'tables':tables,'inputs':inputs}

jobs=[];eliminated=[];still=[]
for job in archive['jobs']:
    if not job['survivors']:continue
    high=tuple(job['exception_pair']);model=models[high];newcases=[]
    for old in job['survivors']:
        tau=old['tau'];g=model['tables'][tau]['cap_with_existing_c14']
        caps=old['caps'][:];caps[3]=g*old['n'][3]
        rem=old['P'];value=6864*old['n'][1];allocation=[0]*5
        for j,w in ((4,1716),(3,792),(2,330),(1,120),(0,36)):
            take=min(rem,caps[j]);allocation[j]=take;rem-=take;value+=w*take
        z={'n':old['n'],'tau':tau,'old_twice_L':old['twice_L'],'new_C3_coefficient':g,
           'new_caps':caps,'new_allocation':allocation,'P':old['P'],'new_twice_L':value,
           'strict':value<5445440}
        newcases.append(z)
        (eliminated if z['strict'] else still).append({'spectrum_id':job['spectrum_id'],**z})
    jobs.append({'spectrum_id':job['spectrum_id'],'high_degrees':list(high),
                 'old_survivor_count':len(newcases),'new_survivor_count':sum(not z['strict'] for z in newcases),
                 'cases':newcases})
out={'status':'COMPLETE112_RESIDUAL_HIGH_ROW_REFINEMENT',
     'scope':__doc__,'review_independence':'same-family','acceptance_status':'provisional',
     'actual_assumptions':['H21/M35simple5/paircover','one specified highpairlambda5 with degrees10/12 or11/11, all other pairs<=4',
                           'old proven C3cap13, same archived P and other capacities'],
     'roles_per_high_pair':21,'models':list(models.values()),'old_keys':112,
     'eliminated_count':len(eliminated),'remaining_count':len(still),
     'newly_strict_spectrum_ids':[j['spectrum_id'] for j in jobs if j['new_survivor_count']==0],
     'eliminated':eliminated,'remaining':still,'jobs':jobs,
     'no_full_spectrum_scan_or_new_layouts':True,'cpu_seconds':time.process_time()-START}
(P/'HIGH_ROW_REFINEMENT.json').write_text(json.dumps(out,indent=2)+'\n')
for m in models.values():print('MODEL',m['high_degrees'],'assignments',m['complete_role_assignments'],
                              'g',[(t,z['g'],z['cap_with_existing_c14']) for t,z in m['tables'].items()])
for j in jobs:print(j['spectrum_id'],j['old_survivor_count'],'->',j['new_survivor_count'])
print('TOTAL',len(eliminated),len(still),'CPU',out['cpu_seconds'])
assert out['cpu_seconds']<10,'10 CPU budget'
