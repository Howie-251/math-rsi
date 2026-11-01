"""Second parameterization of all seven corrected unique-lambda5 scalar domains.
Independent n1/n4/n3 parity generation; direct balanced group boxes and costs.
"""
from pathlib import Path
from math import comb
import json,time,sys

P=Path(__file__).resolve().parent;START=time.process_time()
NEW_ELEVEN='--new-eleven' in sys.argv[1:]
saved=json.loads((P/('ALL_EIGHTEEN_SCALAR_RESULT.json' if NEW_ELEVEN else 'SCALAR_RESULT.json')).read_text())
if NEW_ELEVEN:
    saved['jobs']=[j for j in saved['jobs'] if j['spectrum_id'] not in (56,57,61,62,66,71,72)]
    assert len(saved['jobs'])==11
f=[]
for s in range(31):
    groups=[s//5+int(i<s%5) for i in range(5)]
    f.append(sum(groups[i]*groups[j] for i in range(5) for j in range(i)))
boxes={}
for n1 in range(397,526):
    zero,r=divmod(1050-2*n1,30)
    boxes[n1]=(35-zero)*f[30]+(f[30-r]-f[30] if r else 0)
jobs=[]
for primary in saved['jobs']:
    ds=primary['degrees'];du,dv=primary['exception_pair'];W=sum(d*(d-1)//2 for d in ds)
    # Minimum conditional endpoint-row tau by distributing its remaining excess
    # over19 nonexceptional pairs. This is different from primary's linear bound.
    row=[]
    for d in (du,dv):
        q,r=divmod(4*d-24,19)
        row.append(6+(19-r)*comb(q,2)+r*comb(q+1,2))
    lower=row[0]+row[1]-6
    assert lower==primary['tau_min']
    costunits=sorted(d for d in ds for _ in range(comb(d,2)));prefix=[0]
    for d in costunits:prefix.append(prefix[-1]+d)
    c2=(sum(sorted(ds,reverse=True)[:6])-6)//2
    count=0;maximum=-1;maxkey=None;survivors=[]
    for n1 in range(397,526):
        for t in range(48):
            for m in range(max(-1,min((W-n1-4*t)//3,(282-6*t)//3))+1):
                num=W-280+3*m+8*t-n1
                if num%2:continue
                tau=num//2
                if not lower<=tau<=142:continue
                n2=140+tau-3*m-6*t;n0=595-n1-n2-m-t
                if min(n0,n2)<0:continue
                count+=1
                # Determine remaining pair cap by its individual tau contribution.
                beta=max(lam for lam in range(1,5) if comb(lam-1,2)<=tau-6)
                c4=beta*t+(5-beta)*min(t,min(du,dv)-5)
                caps=[33*n0,35*n1-prefix[n1],c2*n2,13*m,c4]
                rem=boxes[n1];value=6864*n1;allocation=[0]*5
                for weight,j in sorted(zip((36,120,330,792,1716),range(5)),reverse=True):
                    allocation[j]=min(caps[j],rem);rem-=allocation[j];value+=weight*allocation[j]
                key={'n':[n0,n1,n2,m,t],'tau':tau,'P':boxes[n1],'caps':caps,
                     'allocation':allocation,'twice_L':value,'other_pair_cap_from_tau':beta}
                if value>maximum:maximum=value;maxkey=key
                if value>=5445440:survivors.append(key)
        assert time.process_time()-START<3,'three CPU secondary scalar cutoff'
    assert count==primary['complete_domain'] and maximum==primary['maximum_twice_L']
    # Multiple maximizing keys may be traversed in another order; compare the
    # objective and complete count, not an artificial tie-breaking convention.
    assert len(survivors)==primary['survivor_count']
    if not NEW_ELEVEN:assert not survivors
    own={(tuple(z['n']),z['tau'],z['twice_L']) for z in survivors}
    archived={(tuple(z['n']),z['tau'],z['twice_L']) for z in primary['survivors']}
    assert own==archived
    jobs.append({'spectrum_id':primary['spectrum_id'],'degrees':ds,'endpoint_row_minima':row,
                 'tau_min':lower,'complete_domain':count,'survivor_count':len(survivors),
                 'maximum_twice_L':maximum,'maximum_witness':maxkey,
                 'strict_margin_twice':5445440-maximum,'survivors':survivors})
out={'status':'PASS_COMPLETE_SECOND_NEW_ELEVEN_SCALAR_GENERATION' if NEW_ELEVEN else 'PASS_COMPLETE_SECOND_SEVEN_SCALAR_GENERATION',
     'method':__doc__,'total_domain':sum(z['complete_domain'] for z in jobs),
     'all_per_spectrum_counts_and_maxima_equal':True,'all_survivor_key_sets_equal':True,
     'all_survivor_counts_zero':all(j['survivor_count']==0 for j in jobs),
     'C3_cap13_input_discharged_by_separate_new415_and_old425_local_gates':True,
     'jobs':jobs,'minimum_strict_margin_twice':min(z['strict_margin_twice'] for z in jobs),
     'cpu_seconds':time.process_time()-START}
(P/('NEW_ELEVEN_SCALAR_VERIFY_RESULT.json' if NEW_ELEVEN else 'SCALAR_VERIFY_RESULT.json')).write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='jobs'})
