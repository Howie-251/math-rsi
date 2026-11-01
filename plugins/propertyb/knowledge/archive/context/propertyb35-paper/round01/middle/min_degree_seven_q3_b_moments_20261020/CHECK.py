"""Three fixed spectra: shared middle budget with at most c B-type q3 boxes.

Conditional on lambda<=4, C3<=13n3, Gamma minimum3, and every q3 node B-type.
The actual q3-count bounds c=4/8/4 are supplied by parent, not proved here.
"""
from pathlib import Path
from math import comb
from collections import Counter
import json, time

P = Path(__file__).resolve().parent
START = time.process_time()
THRESH2 = 5445440
SPECS = [('S1',[7]*8+[8]+[9]*9+[10]*3,4),
         ('S2',[7]*9+[9]*8+[10]*4,8),
         ('S3',[7]*7+[8]*3+[9]*8+[10]*3,4)]

def f(s):
    q,r=divmod(s,5)
    return (s*s-(5-r)*q*q-r*(q+1)**2)//2

assert sum(a*b for i,a in enumerate((4,7,7,7,6)) for b in (4,7,7,7,6)[:i])==381
jobs=[]
for name,ds,c in SPECS:
    assert len(ds)==21 and sum(ds)==175
    W=sum(comb(d,2) for d in ds)
    assert W=={'S1':655,'S2':657,'S3':654}[name]
    c2=(sum(sorted(ds)[-6:])-6)//2
    rowlow=max(0,4*max(ds)-40)
    capacities=Counter()
    for degree in ds:
        capacities[degree]+=comb(degree,2)
    n1max=(1050+c)//2
    cost={}
    for n1 in range(397,n1max+1):
        rem=n1;total=0
        for degree,capacity in sorted(capacities.items()):
            take=min(rem,capacity);rem-=take;total+=take*degree
        assert rem==0
        cost[n1]=total
    boxes={}
    for n1 in range(397,n1max+1):
        by_d=[]
        for d in range(c+1):
            remaining_mass=2*n1-31*d
            ordinary=35-d
            if not 0<=remaining_mass<=30*ordinary:
                continue
            q,r=divmod(remaining_mass,30)
            assert q<=ordinary and (q<ordinary or r==0)
            by_d.append({'d':d,'ordinary_mass':remaining_mass,
                         'P':381*d+q*f(30)+f(r)})
        assert by_d
        bound=max(z['P'] for z in by_d)
        boxes[n1]={'P':bound,'maximizing_d':[z['d'] for z in by_d if z['P']==bound],
                   'all_feasible_d_bounds':by_d}
    count=0;survivors=[];maxL2=-1;maxkey=None
    Edist=Counter();ddist=Counter();d_profile_count=Counter()
    for n1 in range(397,n1max+1):
        pb=boxes[n1]['P']
        for t in range(47):
            mmax=min((W-n1-4*t)//3,(280-6*t)//3)
            for m in range(max(-1,mmax)+1):
                numerator=W-280+3*m+8*t-n1
                if numerator%2:continue
                tau=numerator//2
                if not rowlow<=tau<=140:continue
                n2=140+tau-3*m-6*t;n0=595-n1-n2-m-t
                if min(n0,n2)<0:continue
                assert n1+2*n2+3*m+4*t==W
                count+=1
                caps=[33*n0,35*n1-cost[n1],c2*n2,13*m,4*t]
                rem=pb;allocation=[0]*5;L2=6864*n1
                for j,w in ((4,1716),(3,792),(2,330),(1,120),(0,36)):
                    amount=min(rem,caps[j]);allocation[j]=amount;rem-=amount;L2+=w*amount
                z={'n':[n0,n1,n2,m,t],'tau':tau,'P':pb,'C_caps':caps,
                   'allocation':allocation,'twice_L':L2,'box_maximizing_d':boxes[n1]['maximizing_d']}
                if L2>maxL2:maxL2=L2;maxkey=z
                if L2>=THRESH2:
                    survivors.append(z);Edist[595-n1]+=1
                    ddist[','.join(map(str,z['box_maximizing_d']))]+=1
                    # This is the precise per-d scalar diagnostic as well:
                    # count which individual d budgets still fail, not actual H.
                    for db in boxes[n1]['all_feasible_d_bounds']:
                        resources=db['P'];value=6864*n1
                        for j,w in ((4,1716),(3,792),(2,330),(1,120),(0,36)):
                            take=min(resources,caps[j]);resources-=take;value+=w*take
                        if value>=THRESH2:d_profile_count[db['d']]+=1
        assert time.process_time()-START<10,'ten CPU-second cutoff'
    job={'name':name,'degrees':ds,'W':W,'C2_coefficient':c2,'q3_count_cap':c,
         'n1_max':n1max,'row_tau_min':rowlow,'complete_domain':count,
         'survivor_count':len(survivors),'maximum_twice_L':maxL2,
         'maximum_L':str(maxL2//2) if maxL2%2==0 else str(maxL2)+'/2',
         'strict_margin_twice':THRESH2-maxL2,'maximum_witness':maxkey,
         'survivor_E_distribution':dict(sorted(Edist.items())),
         'survivor_box_maximizing_d_set_distribution':dict(ddist),
         'survivor_counts_using_individual_d_budget':dict(sorted(d_profile_count.items())),
         'box_by_n1':boxes,'survivors':survivors}
    jobs.append(job)
    print(name,'DOMAIN',count,'SURVIVE',len(survivors),'MAX2',maxL2,
          'MARGIN2',THRESH2-maxL2,'E',dict(Edist),'D',dict(ddist),flush=True)
result={'status':'COMPLETE_CONDITIONAL_DIAGNOSTIC','scope':__doc__,
        'review_independence':'same-family','acceptance_status':'provisional',
        'assumptions':['Exact listed H21/M35/simple5/paircover degree spectra',
                       'All pointpairs lambda<=4 (conditional in this computation)',
                       'Gamma minimum>=3; every Gamma-degree3 node has B-tail F degrees(7,10,10,10,9) and singleton groups(4,7,7,7,6)',
                       'Number of Gamma-degree3 nodes<=c=4/8/4 respectively (parent-supplied structural bound)',
                       'C3<=13n3 (generic gate, conditional caller not re-proved here)',
                       'tau<=140; tau>=max(0,4Delta-40); n1>=397',
                       'C0<=33n0,C1<=35n1-Kd,C2<=floor((S6-6)/2)n2,C4<=4n4',
                       'Shared P bound maximizes over all feasible d0..c, with d exceptional31-mass boxes of cost381 and remaining boxes0..30'],
        'no_extra_n4_wedge_T_or_criticality':True,'no_new_layouts':True,
        'total_domain':sum(j['complete_domain'] for j in jobs),
        'all_strict':all(j['survivor_count']==0 for j in jobs),'jobs':jobs,
        'cpu_seconds':time.process_time()-START}
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('COMPLETE','ALLSTRICT',result['all_strict'],'CPU',result['cpu_seconds'])
