#!/usr/bin/env python3
"""Integer case arithmetic and final previously generated inventory caller map."""
from pathlib import Path
from math import comb
from collections import Counter
from time import process_time
import json
P=Path(__file__).resolve().parent

def deduction_cases(q,color,m):
    if q==8 and color=='R':pair0,pair1,pair2,pair3,tri0,tri1=45,165,495,1287,9,45
    elif q==8:pair0,pair1,pair2,pair3,tri0,tri1=1,11,66,286,0,1
    else:pair0,pair1,pair2,pair3,tri0,tri1=10,55,220,715,1,10
    answer={'intersection_at_least_3':pair3+(m-2)*pair0}
    for h in (0,1):
        u=max(0,4*m-18-2*h)
        s2=comb(m,2)*pair0+(pair1-pair0)*u+(pair2-pair0)*h
        s3=comb(m,3)*tri0+h*(m-2)*(tri1-tri0)
        answer['heavy_'+str(h)]=s2-s3
    if m>=3:answer['at_least_two_heavy']=2*pair2+(m-3)*pair0
    return answer

def main():
    start=process_time();tables={}
    expected={'8R':[45,126,234,600,1125],'8B':[1,3,6,30,75],'9':[10,29,56,180,400]}
    for q,color,key in [(8,'R','8R'),(8,'B','8B'),(9,'R','9')]:
        values=[]
        for m in range(2,7):
            cases=deduction_cases(q,color,m);values.append(min(cases.values()))
            tables[key+str(m)]=cases
        assert values==expected[key]
    blue10={'intersection_at_least_3':286+8,'heavy_forest_rank_at_least_3':3*66+6,
            'no_heavy':45+10*22,
            'unique_heavy':45+65+10*20-8,
            'rank2_two_disjoint':45+2*65+10*18-16,
            'rank2_path':45+2*65+10*18-16-9,
            'rank2_triangle':45+3*65+10*16-24-63}
    assert min(blue10.values())==204
    assert 4*3003+10*1001+10*1573+2910+3567-270-204==43755
    assert 4*3003+4*1001+11*1573+2910+3567+3186==42982
    assert 8*2002+11*1430+2*3984+3996==43710
    old=json.loads((P/'HUNTER_RESULT.json').read_text());keys=[];counts=Counter()
    assert old['degree_keys']==10209 and old['unresolved']==8
    for r in old['records']:
        if r['total']<r['sample_space']:method='two_free_singleton_deductions'
        elif not r['traces']:method='old_three_free_external_gate'
        else:
            ts=r['traces'];assert len(ts)==2 and all(len(t)==2 and max(t)<4 for t in ts)
            assert len(set(ts[0]+ts[1]))==4 and r['d'] in (6,7)
            method='three_free_all_six' if r['d']==6 else 'two_free_red4_blue10'
        counts[method]+=1;keys.append({'inventory':r['inventory'],'d':r['d'],'method':method})
    assert counts=={'two_free_singleton_deductions':10201,'old_three_free_external_gate':2,
                    'three_free_all_six':3,'two_free_red4_blue10':3}
    out={'status':'PASS','scope':'integer proof branches and complete caller map on existing732 necessary internal trace inventories',
         'low_row_excess_budget':2,'inventories':732,'degree_keys':10209,'resolution_counts':dict(counts),
         'deduction_case_tables':tables,'blue10_deduction_cases':blue10,
         'red4_stronger_deduction':270,'blue10_stronger_deduction':204,
         'special_d6_quota8_total':42982,'special_d6_quota9_total':43710,'special_d7_quota8_total':43755,
         'cpu_seconds':process_time()-start,'keys':keys}
    (P/'CLOSURE_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('keys','deduction_case_tables')}))
if __name__=='__main__':main()
