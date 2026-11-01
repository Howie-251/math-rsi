"""Conditional C3=12 sensitivity with actual q3 present: d>=1 and tau>=2.
Also reconstruct B-tail pair codegrees and exhaust tiny K4 weight conditions.
"""
from pathlib import Path
from itertools import combinations, product
from math import comb
import json,time

P=Path(__file__).resolve().parent
START=time.process_time()
SOURCE=json.loads((P.parent/'RESULT.json').read_text())
traces=(7,25,30)
local_pairs={f'{i},{j}':1+sum(bool(m&(1<<i)) and bool(m&(1<<j)) for m in traces)
             for i,j in combinations(range(5),2)}
assert sorted(local_pairs.values())==[2]*8+[3]*2
assert local_pairs['1,2']==3 and local_pairs['3,4']==3
assert sum(comb(lam-1,2) for lam in local_pairs.values())==2

# Finite sanity check of the exact root K4 weighted-triangle argument.
pairlist=list(combinations(range(4),2))
triangles=list(combinations(range(4),3))
patterns=[];weight_cases=0;max_weight=0
for values in product((2,3),repeat=6):
    lam=dict(zip(pairlist,values))
    active_ok=[sum(lam[p]==3 for p in combinations(t,2))==1 for t in triangles]
    for weights in product((0,1,2),repeat=4):
        if not any(weights):continue
        if any(w and not ok for w,ok in zip(weights,active_ok)):continue
        if any(sum(w for t,w in zip(triangles,weights) if set(p)<=set(t))>lam[p] for p in pairlist):continue
        weight_cases+=1;max_weight=max(max_weight,sum(weights))
        if all(weights):patterns.append({'lambda3_edges':[p for p in pairlist if lam[p]==3],
                                         'weights':weights})
assert max_weight==4
assert len(patterns)==3 and all(z['weights']==(1,1,1,1) for z in patterns)
assert all(set(z['lambda3_edges'][0]).isdisjoint(z['lambda3_edges'][1]) for z in patterns)

jobs=[]
for job in SOURCE['jobs']:
    ds=job['degrees'];name=job['name'];c=job['q3_count_cap']//2;W=job['W'];upper=(1050+c)//2
    costs=sorted(d for d in ds for _ in range(comb(d,2)));prefix=[0]
    for d in costs:prefix.append(prefix[-1]+d)
    boxes={}
    for n1,box in job['box_by_n1'].items():
        valid=[z for z in box['all_feasible_d_bounds'] if 1<=z['d']<=c]
        if valid:
            value=max(z['P'] for z in valid)
            boxes[int(n1)]={'P':value,'maximizing_d':[z['d'] for z in valid if z['P']==value],
                             'all_feasible_d_bounds':valid}
    count=0;maximum=-1;maximum_witness=None;survivors=[]
    for n1 in range(397,upper+1):
        if n1 not in boxes:continue
        for t in range(47):
            for m in range(max(-1,min((W-n1-4*t)//3,(280-6*t)//3))+1):
                numerator=W-280+3*m+8*t-n1
                if numerator%2:continue
                tau=numerator//2
                if not 2<=tau<=140:continue
                n2=140+tau-3*m-6*t;n0=595-n1-n2-m-t
                if min(n0,n2)<0:continue
                count+=1
                caps=[33*n0,35*n1-prefix[n1],job['C2_coefficient']*n2,12*m,4*t]
                rem=boxes[n1]['P'];value=6864*n1;allocation=[0]*5
                for j,w in ((4,1716),(3,792),(2,330),(1,120),(0,36)):
                    take=min(rem,caps[j]);rem-=take;allocation[j]=take;value+=w*take
                key={'n':[n0,n1,n2,m,t],'tau':tau,'P':boxes[n1]['P'],'caps':caps,
                     'allocation':allocation,'twice_L':value,'box_maximizing_d':boxes[n1]['maximizing_d']}
                if value>maximum:maximum=value;maximum_witness=key
                if value>=5445440:survivors.append(key)
        assert time.process_time()-START<3,'3 CPU-second cutoff'
    answer={'name':name,'degrees':ds,'q3_count_min':1,'q3_count_max':c,
            'C3_coefficient':12,'tau_min':2,'tau_max':140,'complete_domain':count,
            'survivor_count':len(survivors),'maximum_twice_L':maximum,
            'maximum_L':str(maximum//2) if maximum%2==0 else str(maximum)+'/2',
            'strict_margin_twice':5445440-maximum,'maximum_witness':maximum_witness,
            'survivors':survivors}
    jobs.append(answer)
    print(name,'DOMAIN',count,'SURVIVE',len(survivors),'MAXL',answer['maximum_L'],
          'MARGIN2',answer['strict_margin_twice'],flush=True)
    for z in survivors:print('SURVIVOR',name,z,flush=True)
out={'status':'COMPLETE_CONDITIONAL_SENSITIVITY','scope':__doc__,
     'review_independence':'same-family','acceptance_status':'provisional',
     'B_tail_internal_pair_codegrees':local_pairs,'B_tail_internal_tau_contribution':2,
     'K4_weight_check':{'feasible_labeled_assignments':weight_cases,'maximum_q3_count':max_weight,
                        'all_four_active_patterns':patterns},
     'C3_coefficient12_is_hypothetical':True,'all_other_primary_assumptions_retained':True,
     'no_extra_n4_wedge_T_or_layouts':True,'jobs':jobs,'cpu_seconds':time.process_time()-START}
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print('CPU',out['cpu_seconds'])
