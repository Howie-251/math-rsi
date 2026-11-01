"""Independent actual-d1 conditional scalar: tau/t/m generation for S1/S2/S3.
All three exact degree lists, costs, top-six sums and P1 rebuilt without imports.
C3<=12n3 remains a hypothesis; no extra n4/wedge/T bound.
"""
from pathlib import Path
from math import comb
from collections import Counter
import json,time

P=Path(__file__).resolve().parent
START=time.process_time()
inputs=[('S1',[7]*8+[8]+[9]*9+[10]*3),
        ('S2',[7]*9+[9]*8+[10]*4),
        ('S3',[7]*7+[8]*3+[9]*8+[10]*3)]
# Explicit34 ordinary boxes: exceptional q3 edge contributes31 mass and381.
f=[]
for s in range(31):
    groups=[s//5+int(i<s%5) for i in range(5)]
    f.append(sum(groups[i]*groups[j] for i in range(5) for j in range(i)))
P1={}
for n1 in range(397,526):
    mass=2*n1-31
    assert 0<=mass<=34*30
    full,remainder=divmod(mass,30)
    assert full<34 or remainder==0
    P1[n1]=381+full*f[30]+f[remainder]
jobs=[]
for name,ds in inputs:
    assert len(ds)==21 and sum(ds)==175
    W=sum(d*(d-1)//2 for d in ds)
    top6=sum(sorted(ds,reverse=True)[:6])
    c2=(top6-6)//2
    bydegree=Counter(ds)
    costs={}
    for n1 in range(397,526):
        rem=n1;price=0
        for d,multiplicity in sorted(bydegree.items()):
            take=min(rem,multiplicity*comb(d,2))
            rem-=take;price+=take*d
        assert rem==0
        costs[n1]=price
    count=0;survivors=[];maximum=-1;maxkey=None
    for tau in range(2,141):
        for t in range((140+tau)//6+1):
            for m in range((140+tau-6*t)//3+1):
                n1=W-280-2*tau+3*m+8*t
                if not 397<=n1<=525:continue
                n2=140+tau-3*m-6*t
                n0=735-W+tau-m-3*t
                if n0<0:continue
                assert n2>=0 and sum((n0,n1,n2,m,t))==595
                assert n1+2*n2+3*m+4*t==W
                count+=1
                caps=[33*n0,35*n1-costs[n1],c2*n2,12*m,4*t]
                budget=P1[n1];value=6864*n1;allocation=[0]*5
                for weight,j in sorted(zip((36,120,330,792,1716),range(5)),reverse=True):
                    allocation[j]=min(budget,caps[j]);budget-=allocation[j]
                    value+=weight*allocation[j]
                z={'n':[n0,n1,n2,m,t],'tau':tau,'actual_d':1,'P':P1[n1],
                   'caps':caps,'allocation':allocation,'twice_L':value}
                if value>maximum:maximum=value;maxkey=z
                if value>=5445440:survivors.append(z)
        assert time.process_time()-START<2,'two CPU-second cutoff'
    jobs.append({'name':name,'degrees':ds,'W':W,'actual_S6':top6,'C2_coefficient':c2,
                 'tau_min':2,'tau_max':140,'actual_d':1,'complete_domain':count,
                 'survivor_count':len(survivors),'maximum_twice_L':maximum,
                 'maximum_L':str(maximum//2) if maximum%2==0 else str(maximum)+'/2',
                 'strict_margin_twice':5445440-maximum,'maximum_witness':maxkey,
                 'survivors':survivors})

# The only prior actual-d1 primary run was S2; compare after all new answers exist.
old=json.loads((P.parent/'TAU_TWO/UNIQUENESS_CHECK.json').read_text())['S2_actual_d1_tau2_scalar']
new=next(j for j in jobs if j['name']=='S2')
for key in ('complete_domain','survivor_count','maximum_twice_L','strict_margin_twice','maximum_witness'):
    assert new[key]==old[key]
assert all(j['survivor_count']==0 for j in jobs)
result={'status':'PASS_COMPLETE_CONDITIONAL_ACTUAL_D1','scope':__doc__,
        'review_independence':'same-family','acceptance_status':'provisional',
        'method':'Independent tau/n4/n3 generation; degree-group capacity costs; actual top6; direct balanced f and exceptional381+34 ordinary boxes.',
        'C3_cap12_is_assumed':True,
        'other_inputs':['H21/35simple5/paircover/exact degree spectra','allpointpairlambda<=4',
                        'one actual q3B node of groups4,7,7,7,6; all other Gamma nodesdegree>=4',
                        'tau>=2 and<=140; general single/two-flip imports'],
        'no_extra_n4_wedge_T_or_criticality':True,'new_layouts':False,
        'complete_domain':sum(j['complete_domain'] for j in jobs),'jobs':jobs,
        'S2_primary_full_count_maximum_and_witness_equal':True,
        'all_survivor_counts_zero':True,'cpu_seconds':time.process_time()-START}
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
for j in jobs:print(j['name'],j['complete_domain'],j['survivor_count'],j['maximum_L'],j['strict_margin_twice'])
print('CPU',result['cpu_seconds'])
