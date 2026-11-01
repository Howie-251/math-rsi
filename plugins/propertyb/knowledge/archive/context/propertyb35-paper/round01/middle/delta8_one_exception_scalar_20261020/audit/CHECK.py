"""Independent tau/t/m generation of the four one-exception scalar domains.

No primary functions imported. The C3<=13n3 hypothesis remains explicit.
"""
from pathlib import Path
from math import comb
from collections import Counter
import json, time

P = Path(__file__).resolve().parent
START = time.process_time()
INPUTS = [(8,[8]*18+[9,10,12]), (9,[8]*18+[9,11,11]),
          (11,[8]*19+[10,13]), (12,[8]*19+[11,12])]
TARGET = 5445440

# Independent direct five-group cross-products, followed by the deficit-box
# endpoint formula: total deficit is1050-2n1, and each zero box consumes30.
fivegroups = []
for mass in range(31):
    sizes = [mass//5+int(i<mass%5) for i in range(5)]
    fivegroups.append(sum(sizes[i]*sizes[j] for i in range(5) for j in range(i)))
boxes = {}
for n1 in range(397,526):
    zero, remainder = divmod(1050-2*n1,30)
    boxes[n1] = (35-zero)*fivegroups[30]
    if remainder:
        boxes[n1] += fivegroups[30-remainder]-fivegroups[30]

jobs = []
for sid, ds in INPUTS:
    assert len(ds)==21 and sum(ds)==175
    W = sum(d*(d-1)//2 for d in ds)
    rowmin = max(0,4*max(ds)-40)
    capacity = Counter()
    for d in ds:
        capacity[d] += comb(d,2)
    degreecost = {}
    for count in range(397,526):
        rest = count
        total = 0
        for d in sorted(capacity):
            selected = min(rest,capacity[d])
            rest -= selected
            total += d*selected
        assert rest==0
        degreecost[count] = total
    scalar_c2 = (sum(sorted(ds,reverse=True)[:6])-6)//2
    bonus = min(ds[-2:])-5
    count = 0
    survivors = 0
    maximum = -1
    witness = None
    maxcount = 0
    # A genuinely different free parameterization from primary n1/t/m.
    for tau in range(143):
        if tau < rowmin:
            continue
        for t in range((140+tau)//6+1):
            for m in range((140+tau-6*t)//3+1):
                n2 = 140+tau-3*m-6*t
                n1 = W-280-2*tau+3*m+8*t
                n0 = 735-W+tau-m-3*t
                if n0<0 or not 397<=n1<=525:
                    continue
                assert n2>=0 and n0+n1+n2+m+t==595
                assert n1+2*n2+3*m+4*t==W
                count += 1
                caps = [33*n0,35*n1-degreecost[n1],scalar_c2*n2,13*m,4*t+bonus]
                resources = boxes[n1]
                value = 6864*n1
                allocation = [0]*5
                for weight,j in sorted(zip((36,120,330,792,1716),range(5)),reverse=True):
                    allocation[j] = min(resources,caps[j])
                    resources -= allocation[j]
                    value += weight*allocation[j]
                if value>maximum:
                    maximum=value
                    maxcount=1
                    witness={'n':[n0,n1,n2,m,t],'tau':tau,'P':boxes[n1],
                             'caps':caps,'allocation':allocation,'twice_L':value}
                elif value==maximum:
                    maxcount+=1
                survivors += int(value>=TARGET)
        assert time.process_time()-START<5,'five CPU-second cutoff'
    jobs.append({'source_spectrum_id':sid,'degrees':ds,'complete_domain':count,
                 'survivor_count':survivors,'maximum_twice_L':maximum,
                 'strict_margin_twice':TARGET-maximum,'maximizer_count':maxcount,
                 'maximum_witness':witness})

# Compare only after the complete independent answers have been generated.
primary=json.loads((P.parent/'RESULT.json').read_text())
for answer in jobs:
    saved=next(z for z in primary['jobs'] if z['source_spectrum_id']==answer['source_spectrum_id'])
    for key in ('degrees','complete_domain','survivor_count','maximum_twice_L','strict_margin_twice'):
        assert answer[key]==saved[key],(answer['source_spectrum_id'],key)
    assert answer['maximum_witness']==saved['maximum_witness']
assert sum(z['complete_domain'] for z in jobs)==315870
assert all(z['survivor_count']==0 for z in jobs)
result={'status':'PASS_CONDITIONAL_SCALAR',
        'scope':__doc__,'review_independence':'same-family','acceptance_status':'provisional',
        'method':'tau/t/m parameterization versus primary n1/t/m parity; direct group products/deficit boxes; grouped cheapest-cost fill; exact integer objective. No primary functions imported.',
        'C3_cap13_assumed':True,'full_domain':315870,'full_spectra':4,
        'all_counts_objectives_and_maximum_witnesses_equal':True,
        'all_survivor_counts_zero':True,'minimum_strict_margin_L':2716,
        'no_extra_n4_wedge_T_or_criticality':True,
        'capacity_note_reviewed':'proofs/propertyb35/ONE_EXCEPTIONAL_POINTPAIR_CAPACITIES.md',
        'capacity_note_verdict':'PASS: paircover givesR140; exactly one lambda5 increases tau allowance by2. Exclusive uv outer pairs inject uniquely into u-only edges (and v-only edges), so at mostmin(du,dv)-5 unordered pairs; no orientation factor2.',
        'jobs':jobs,'cpu_seconds':time.process_time()-START}
(P/'CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='jobs'}))
