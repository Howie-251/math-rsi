"""Small actual-role intersection checks and S2 scalar with actual d=1.
The scalar still assumes the hypothetical C3<=12n3 capacity.
"""
from pathlib import Path
from itertools import combinations,product
from math import comb
import json,time

P=Path(__file__).resolve().parent
START=time.process_time()
ten=set(range(4));sevens=(4,5);nines=(6,7)
marked=[]
for T in combinations(ten,3):
    for p,n in product(sevens,nines):
        for pair in combinations(T,2):
            third=next(iter(set(T)-set(pair)))
            F=frozenset(set(T)|{p,n})
            exceptions=(frozenset({p,*pair}),frozenset({p,third,n}),frozenset({*T,n}))
            marked.append({'T':frozenset(T),'p':p,'n':n,'red':frozenset(pair),
                           'third':third,'F':F,'exceptions':exceptions})
counts={'marked_nodes':len(marked),'distinct_actual_edge_mark_pairs':0,
        'mutually_compatible_pairs':0,'same_T_pairs':0,'different_T_pairs':0,
        'different_T_six_point_contradictions':0,'same_T_shared_exception_checks':0}
ordinary_patterns=0
for a,b in combinations(marked,2):
    if a['F']==b['F']:continue
    counts['distinct_actual_edge_mark_pairs']+=1
    inter=a['F']&b['F']
    if inter not in a['exceptions'] or inter not in b['exceptions']:continue
    # Local codegree values on any pair selected in both F and F' must agree.
    def local_lambda(node,pair):
        return 1+sum(set(pair)<=set(t) for t in node['exceptions'])
    if any(local_lambda(a,pair)!=local_lambda(b,pair) for pair in combinations(inter,2)):continue
    counts['mutually_compatible_pairs']+=1
    if a['T']!=b['T']:
        counts['different_T_pairs']+=1
        assert a['p']==b['p'] and a['n']!=b['n']
        assert a['T']&b['T']==a['red']==b['red']
        required_union=a['exceptions'][2]|b['exceptions'][2]
        assert len(required_union)==6
        assert a['p'] not in required_union
        counts['different_T_six_point_contradictions']+=1
    else:
        counts['same_T_pairs']+=1
        assert a['n']==b['n'] and a['p']!=b['p'] and a['red']==b['red']
        shared7=a['exceptions'][0]|b['exceptions'][0]
        shared25=a['exceptions'][1]|b['exceptions'][1]
        assert len(shared7)==len(shared25)==4
        assert {a['p'],b['p']}<=shared7&shared25
        universe=a['F']|b['F'];assert len(universe)==6
        # Exhaust all possible incidence traces on F union F' (external points irrelevant).
        U=sorted(universe)
        for mask in range(1<<6):
            R={U[i] for i in range(6) if mask>>i&1}
            if len(R&a['F'])==len(R&b['F'])==1:
                ordinary_patterns+=1
                assert (a['p'] in R)==(b['p'] in R)
        counts['same_T_shared_exception_checks']+=1
assert counts['different_T_pairs'] and counts['same_T_pairs']

source=json.loads((P.parent/'RESULT.json').read_text())
job=next(z for z in source['jobs'] if z['name']=='S2')
ds=job['degrees'];W=job['W'];units=sorted(d for d in ds for _ in range(comb(d,2)));prefix=[0]
for d in units:prefix.append(prefix[-1]+d)
boxes={int(n):next(z['P'] for z in b['all_feasible_d_bounds'] if z['d']==1)
       for n,b in job['box_by_n1'].items() if any(z['d']==1 for z in b['all_feasible_d_bounds'])}
domain=0;survivors=[];maximum=-1;maxkey=None
for n1 in range(397,526):
    for t in range(47):
        for m in range(max(-1,min((W-n1-4*t)//3,(280-6*t)//3))+1):
            num=W-280+3*m+8*t-n1
            if num%2:continue
            tau=num//2
            if not 2<=tau<=140:continue
            n2=140+tau-3*m-6*t;n0=595-n1-n2-m-t
            if min(n0,n2)<0:continue
            domain+=1
            caps=[33*n0,35*n1-prefix[n1],26*n2,12*m,4*t]
            rem=boxes[n1];value=6864*n1;allocation=[0]*5
            for j,w in ((4,1716),(3,792),(2,330),(1,120),(0,36)):
                take=min(rem,caps[j]);rem-=take;allocation[j]=take;value+=w*take
            key={'n':[n0,n1,n2,m,t],'tau':tau,'P':boxes[n1],'caps':caps,
                 'allocation':allocation,'twice_L':value,'actual_d':1}
            if value>maximum:maximum=value;maxkey=key
            if value>=5445440:survivors.append(key)
    assert time.process_time()-START<3,'three CPU cutoff'
out={'status':'PASS_ACTUAL_INTERSECTION_AND_COMPLETE_CONDITIONAL_SCALAR',
     'review_independence':'same-family','acceptance_status':'provisional',
     'scope':__doc__,'pair_actual_role_checks':counts,
     'ordinary_singleton_union_trace_patterns_checked':ordinary_patterns,
     'same_T_degree7_pair_codegree_forced':6,
     'same_T_contradiction_import':'Selected degrees7/7, codegree6 fixed zero-quota certificate200844/230945<1 at(10,21)',
     'q3_uniqueness_depends_on':'At most4 global degree10 points, all q3 nodes exactly B tail; degree roles7/9/10 are actual',
     'S2_actual_d1_tau2_scalar':{'complete_domain':domain,'C3_coefficient':12,
                               'survivor_count':len(survivors),'maximum_twice_L':maximum,
                               'maximum_L':str(maximum//2) if maximum%2==0 else str(maximum)+'/2',
                               'strict_margin_twice':5445440-maximum,'maximum_witness':maxkey,
                               'survivors':survivors},
     'C3_coefficient12_is_hypothetical':True,'cpu_seconds':time.process_time()-START}
(P/'UNIQUENESS_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
