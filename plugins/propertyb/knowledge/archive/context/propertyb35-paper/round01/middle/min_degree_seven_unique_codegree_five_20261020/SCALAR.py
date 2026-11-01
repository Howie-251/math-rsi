"""Seven actual min7 spectra, unique actual pairlambda5, corrected tau and C4.
C3<=13n3 is a conditional input to this scalar calculation.
"""
from pathlib import Path
from collections import Counter
from math import comb
import json,time,sys

P=Path(__file__).resolve().parent
START=time.process_time()
source=json.loads((P.parent/'min_degree_seven_low_excess_strong_pairs_20261020/RESULT.json').read_text())
IDS=(56,57,61,62,66,71,72)
ALL_EIGHTEEN='--all-eighteen' in sys.argv[1:]
if ALL_EIGHTEEN:
    IDS=tuple(j['spectrum_id'] for j in source['jobs'] if j['exceptional_pair_types'])
    assert len(IDS)==18
f=[]
for s in range(31):
    q,r=divmod(s,5);f.append((s*s-(5-r)*q*q-r*(q+1)**2)//2)
boxes={n:(2*n//30)*f[30]+f[2*n%30] for n in range(397,526)}
jobs=[]
for sid in IDS:
    old=next(j for j in source['jobs'] if j['spectrum_id']==sid)
    ds=old['degrees'];du,dv=old['exceptional_pair_types'][0]['degrees']
    W=sum(comb(d,2) for d in ds)
    # One lambda5 contributes6 to each endpoint row. On its19 other pairs,
    # sum(lambda-1)=4d-24 and C(lambda-1,2)>=lambda-2 give max(0,4d-43).
    L_u=6+max(0,4*du-43);L_v=6+max(0,4*dv-43)
    taulower=max(L_u,L_v,L_u+L_v-6)
    assert taulower==(11 if du==10 else 8)
    histogram=Counter(ds);cost={}
    for n1 in range(397,526):
        rem=n1;v=0
        for d,mul in sorted(histogram.items()):
            take=min(rem,mul*comb(d,2));rem-=take;v+=take*d
        assert rem==0;cost[n1]=v
    C2=(sum(sorted(ds)[-6:])-6)//2
    count=0;survivors=[];maximum=-1;maxkey=None
    for tau in range(taulower,143):
        for t in range((140+tau)//6+1):
            for m in range((140+tau-6*t)//3+1):
                n1=W-280-2*tau+3*m+8*t;n2=140+tau-3*m-6*t
                n0=735-W+tau-m-3*t
                if n0<0 or not 397<=n1<=525:continue
                count+=1
                # The unique lambda5 pair already contributes6 to tau. If
                # tau<=8, no other lambda4 is possible (it would cost3).
                # At most min(du,dv)-5 exclusive-pair outer flags use lambda5.
                othercap=3 if tau<=8 else 4
                c4=othercap*t+(5-othercap)*min(t,min(du,dv)-5)
                caps=[33*n0,35*n1-cost[n1],C2*n2,13*m,c4]
                rem=boxes[n1];value=6864*n1;allocation=[0]*5
                for j,w in ((4,1716),(3,792),(2,330),(1,120),(0,36)):
                    take=min(rem,caps[j]);rem-=take;allocation[j]=take;value+=w*take
                z={'n':[n0,n1,n2,m,t],'tau':tau,'P':boxes[n1],'caps':caps,
                   'allocation':allocation,'twice_L':value,'other_pair_cap_from_tau':othercap}
                if value>maximum:maximum=value;maxkey=z
                if value>=5445440:survivors.append(z)
        assert time.process_time()-START<5,'5 CPU scalar cutoff'
    job={'spectrum_id':sid,'degrees':ds,'exception_pair':[du,dv],'tau_min':taulower,
         'tau_max':142,'row_bounds':[L_u,L_v],'C4_bonus':min(du,dv)-5,
         'complete_domain':count,'survivor_count':len(survivors),
         'maximum_twice_L':maximum,'strict_margin_twice':5445440-maximum,
         'maximum_witness':maxkey,'survivors':survivors}
    jobs.append(job)
    print(sid,'DOMAIN',count,'SURVIVE',len(survivors),'MAX2',maximum,'MARGIN2',5445440-maximum,flush=True)
out={'status':'COMPLETE_EIGHTEEN_CONDITIONAL_SCALAR' if ALL_EIGHTEEN else 'COMPLETE_SEVEN_CONDITIONAL_SCALAR','C3_cap13_is_assumed':True,
     'scope':__doc__,'actual_lambda5_required_for_tau_lower':True,
     'no_extra_n4_wedge_T_or_criticality':True,'jobs':jobs,
     'all_strict':all(z['survivor_count']==0 for z in jobs),
     'total_domain':sum(z['complete_domain'] for z in jobs),'cpu_seconds':time.process_time()-START}
(P/('ALL_EIGHTEEN_SCALAR_RESULT.json' if ALL_EIGHTEEN else 'SCALAR_RESULT.json')).write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE',out['all_strict'],'CPU',out['cpu_seconds'])
