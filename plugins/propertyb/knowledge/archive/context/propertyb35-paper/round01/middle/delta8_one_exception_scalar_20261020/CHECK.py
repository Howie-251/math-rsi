"""Four-spectrum scalar diagnostic with at most one codegree-five pointpair.

Conditional on actual C3<=13n3 and Gamma minimum degree four. No extra n4,
wedge, criticality, threshold-graph or T bound. Only these four spectra run.
"""
from pathlib import Path
from math import comb
import json, time

P = Path(__file__).resolve().parent
START = time.process_time()
THRESHOLD2 = 5445440
SPECS = [(8, [8]*18+[9,10,12], 5), (9, [8]*18+[9,11,11], 6),
         (11, [8]*19+[10,13], 5), (12, [8]*19+[11,12], 6)]

def f(s):
    q, r = divmod(s, 5)
    return (s*s-(5-r)*q*q-r*(q+1)*(q+1))//2

def box(n1):
    q, r = divmod(2*n1, 30)
    return q*f(30)+f(r)

jobs = []
for sid, ds, bonus in SPECS:
    assert len(ds) == 21 and sum(ds) == 175
    W = sum(comb(d,2) for d in ds)
    rowlow = max(0, 4*max(ds)-40)
    c2coef = (sum(ds[-6:])-6)//2
    costunits = [d for d in ds for _ in range(comb(d,2))]
    prefix = [0]
    for d in costunits:
        prefix.append(prefix[-1]+d)
    domain = 0
    maximum = -1
    maximum_witness = None
    survivors = []
    # Independent integer choices n1,t,m; all other moments are recovered.
    # t<=47 is only the nonnegative second-moment bound 6t<=140+142.
    for n1 in range(397, 526):
        pb = box(n1)
        for t in range(48):
            mmax = min((W-n1-4*t)//3, (282-6*t)//3)
            for m in range(max(-1, mmax)+1):
                numerator = W-280+3*m+8*t-n1
                if numerator % 2:
                    continue
                tau = numerator//2
                if not rowlow <= tau <= 142:
                    continue
                n2 = 140+tau-3*m-6*t
                n0 = 595-n1-n2-m-t
                if min(n0,n2) < 0:
                    continue
                assert n1+2*n2+3*m+4*t == W
                domain += 1
                caps = [33*n0, 35*n1-prefix[n1], c2coef*n2, 13*m, 4*t+bonus]
                allocation = [0]*5
                remaining = pb
                twice = 6864*n1
                for j, w in ((4,1716),(3,792),(2,330),(1,120),(0,36)):
                    take = min(caps[j], remaining)
                    allocation[j] = take
                    remaining -= take
                    twice += take*w
                z = {'n':[n0,n1,n2,m,t], 'tau':tau, 'P':pb, 'caps':caps,
                     'allocation':allocation, 'twice_L':twice}
                if twice > maximum:
                    maximum = twice
                    maximum_witness = z
                if twice >= THRESHOLD2:
                    survivors.append(z)
        assert time.process_time()-START < 10, 'ten CPU-second cutoff'
    jobs.append({'source_spectrum_id':sid, 'degrees':ds, 'exception_pair':ds[-2:],
                 'C4_bonus':bonus, 'W':W, 'C2_coefficient':c2coef, 'row_tau_min':rowlow,
                 'complete_domain':domain, 'strict_domain':domain-len(survivors),
                 'survivor_count':len(survivors), 'maximum_twice_L':maximum,
                 'maximum_L':str(maximum//2) if maximum%2==0 else str(maximum)+'/2',
                 'strict_margin_twice':THRESHOLD2-maximum,
                 'maximum_witness':maximum_witness, 'survivors':survivors})
    print('SPEC',sid,'DOMAIN',domain,'SURVIVE',len(survivors),'MAX2',maximum,
          'MARGIN2',THRESHOLD2-maximum,flush=True)

result = {'status':'COMPLETE_CONDITIONAL_DIAGNOSTIC', 'scope':__doc__,
          'assumptions':['H21/M35/simple5/paircover/exact listed degree multiset',
                         'All pointpairs lambda<=4 except at most the displayed unique high pair, which may have lambda5; no lambda>=6',
                         'Gamma minimum degree at least4', 'C3<=13n3 (unproved input hypothesis for this diagnostic)',
                         '397<=n1<=525; 0<=tau<=142; row tau>=max(0,4Delta-40)',
                         'C0<=33n0; C1<=35n1-Kd; C2<=floor((S6-6)/2)n2; C4<=4n4+bonus',
                         'All Cj share same P bounded by35 convex boxes0<=s<=30'],
          'no_extra_n4_bound':True, 'no_wedge_or_T_or_criticality':True,
          'no_H_realizability_claim':True, 'completed_spectra':len(jobs),
          'all_strict':all(j['survivor_count']==0 for j in jobs), 'jobs':jobs,
          'total_domain':sum(j['complete_domain'] for j in jobs),
          'minimum_strict_margin_twice':min(j['strict_margin_twice'] for j in jobs),
          'cpu_seconds':time.process_time()-START}
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('COMPLETE',result['all_strict'],'CPU',result['cpu_seconds'])
