#!/usr/bin/env python3
"""Tiny exact arithmetic receipt; no set, partition, coloring or H enumeration."""
from math import comb
from pathlib import Path
from time import process_time
import json
start=process_time()
w={j:comb(11+j,9) for j in range(4)}
assert w=={0:55,1:220,2:715,3:2002}
rows=[]
for m in (6,7):
    pairs=comb(m,2); triples=comb(m,3)
    for h in (0,1):
        unit=4*m-19-2*h
        pair_sum=pairs*55+165*unit+660*h
        triple_upper=triples*10+45*h*(m-2)
        rows.append(dict(m=m,case=f'heavy_count_{h}',unit_min=unit,
                         pair_sum_lower=pair_sum,triple_sum_upper=triple_upper,
                         deduction=pair_sum-triple_upper))
    rows.append(dict(m=m,case='some_intersection_at_least_3',deduction=2002+(m-2)*55))
    rows.append(dict(m=m,case='at_least_two_heavy_tree',deduction=2*715+(m-3)*55))
# Improve m7 when all pair intersections <=2, by heavy-graph forest rank.
m=7
rows.append(dict(m=m,case='heavy_forest_rank_at_least_3',deduction=3*715+(m-4)*55))
for case,h,extra in [('rank2_two_disjoint',2,0),('rank2_path',2,120),('rank2_triangle',3,570)]:
    unit=max(0,4*m-19-2*h)
    pair_sum=comb(m,2)*55+165*unit+660*h
    triple_upper=comb(m,3)*10+45*h*(m-2)+extra
    rows.append(dict(m=m,case=case,unit_min=unit,pair_sum_lower=pair_sum,
                     triple_sum_upper=triple_upper,deduction=pair_sum-triple_upper))
original={(r['m'],r['case']):r['deduction'] for r in rows}
assert [original[(6,f'heavy_count_{h}')] for h in (0,1)]==[1450,1600]
assert [original[(7,f'heavy_count_{h}')] for h in (0,1)]==[2290,2395]
assert original[(6,'at_least_two_heavy_tree')]==1595
assert original[(7,'at_least_two_heavy_tree')]==1650
m7_cases=['heavy_count_0','heavy_count_1','some_intersection_at_least_3',
          'heavy_forest_rank_at_least_3','rank2_two_disjoint','rank2_path','rank2_triangle']
assert min(original[(7,c)] for c in m7_cases)==2035
red6_refined={'no_heavy_unit_at_least_6':55*15+165*6-10*20,
              'no_heavy_unit_5':55*15+165*5-(comb(5,2)+7*2),
              'unique_heavy':1600,'at_least_two_heavy_tree':1595,
              'intersection_at_least_3':2222}
assert red6_refined['no_heavy_unit_at_least_6']==1615
assert red6_refined['no_heavy_unit_5']==1626
assert min(red6_refined.values())==1595
blue_weights={j:comb(11+j,1+j) for j in range(4)}
assert blue_weights=={0:11,1:66,2:286,3:1001}
blue7_cases={'intersection_at_least_3':1001+5*11,
             'at_least_two_heavy_tree':2*286+4*11,
             'no_heavy':21*11+55*9-35,
             'unique_heavy':21*11+275+55*7-(30+5*11)}
assert blue7_cases=={'intersection_at_least_3':1056,
                     'at_least_two_heavy_tree':616,'no_heavy':691,'unique_heavy':806}
assert min(blue7_cases.values())==616
assert 94539-1595-616==92328 and 92378-92328==50
result=dict(status='PASS',pair_intersection_weights=w,rows=rows,
            universal_deduction={'red_m6':1595,'red_m7':2035,'blue_m7':616},
            red6_refined=red6_refined,blue_pair_weights=blue_weights,blue7_cases=blue7_cases,
            conditional_caller_arithmetic={'baseline':94539,'after_deductions':92328,'sample_space':92378,'margin':50},
            coverage='analytic heavy-graph cases; arithmetic only, no object enumeration',
            cpu_seconds=process_time()-start)
Path(__file__).with_name('RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
