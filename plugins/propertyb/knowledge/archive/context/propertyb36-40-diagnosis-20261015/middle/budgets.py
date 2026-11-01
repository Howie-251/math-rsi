"""Exact degree-budget arithmetic only; no Lean or hypergraph enumeration."""
from pathlib import Path
import json
from math import ceil
OUT = Path(__file__).parent

def core(h, D, k):
    if h < k:
        return None
    delta = min(D, (k-1)*D//(h-k+1))
    W = min(k*(k-1)*D//(2*(h-1)), k*delta//2)
    return {'k':k, 'h_lower':h, 'D':D, 'maximum_internal_excess_upper':delta, 'W_upper':W,
            'exchange_coefficient_at_h_lower':h-k-1, 'exchange_rhs':(k-1)*D}

rows=[]
for M in range(35,40):
    for v in range(19,24):
        low=(v+2)//4
        top=5*M//v
        D=4*top-v+1
        h=max(1,(top+1)*v-5*M)
        rows.append({'M':M,'target_lower_bound':M+1,'v':v,'degree_minimum':low,
                     'degree_maximum_for_min_degree':top,
                     'top_min_degree_branch': {'d':top,'surplus_above_regular':5*M-v*top,
                      'count_exact_d_lower':h,'cores':[core(h,D,k) for k in (4,6)]},
                     'weighted_low_budget_6_7':8*v-5*M if v>=22 else None})
selected=[]
for v in (22,23):
    for M in range(35,40):
        B=8*v-5*M; D=25-v
        for r in range(0,7):
            t=max(0,B-2*r)
            N=v-r; extra=5*M-7*v+r
            # Formula is conditional on exactly r six-degree vertices.
            q78=max(0,N-extra//2)
            k=min(r,4)
            selected.append({'M':M,'v':v,'six_count':r,'seven_count_lower':t,
                 'seven_common_unit_all_sixes_lower':max(0,t-r*D),
                 'seven_or_eight_outside_all_sixes_lower':q78,
                 'common_unit_7_or_8_to_k_sixes':max(0,q78-k*D),'k':k})
extra=[]
for M in range(35,40):
    E=5*M-155
    extra.append({'M':M,'assumption':'v=23, exactly six degree-6 vertices; no internal unit-pair assumption needed',
       'outside_surplus_above_degree_7':E,
       'options':[{'maximum_new_degree':q,'candidate_count_lower':max(0,17-E//(q-6)),
                  'new_total_excess_upper':12//(17-E//(q-6)) if 17-E//(q-6)>0 else None}
                  for q in (8,9,10)]})
result={'scope':'necessary integer inequalities and deterministic weighted-subset selection; not a colorability proof or a counterexample search',
        'M_range':[35,39],'v_range':[19,23], 'rows':rows,'low_point_selection':selected,
        'six_low_extra_point':extra,
        'notable_new_cores':[{'v':23,'M':37,'d':8,**core(22,10,6)},
                              {'v':22,'M':36,'d':8,**core(18,11,4)},
                              {'v':21,'M':38,'d':9,**core(20,16,4)}]}
(OUT/'BUDGETS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
for v in range(19,24):
    rr=[x for x in rows if x['v']==v]
    print(v, [(x['M'],x['degree_maximum_for_min_degree'],x['top_min_degree_branch']['count_exact_d_lower']) for x in rr])
print('new_cores',result['notable_new_cores'])
print('six_low_extra',extra)
