"""Independent exact small arithmetic for the uniform-root completion."""
from pathlib import Path
from fractions import Fraction
from math import comb
import json,time

HERE=Path(__file__).resolve().parent
start=time.process_time()

def partitions(total,k,minimum=1):
    if k==0:
        if total==0:yield ()
        return
    for x in range(minimum,total//k+1):
        for tail in partitions(total-x,k-1,x):yield (x,)+tail

def support(a):return 4 if a==1 else 6 if a<=3 else 7

rows=[]
for r in (3,4,5):
    k=9-r
    partitions_checked=[]
    for parts in partitions(9,k):
        us=sum(support(a) for a in parts)
        partitions_checked.append({'sizes':parts,'support_lower_sum':us,'cross_edges_lower':us-17})
    M=min(x['cross_edges_lower'] for x in partitions_checked)
    pairs=[]
    for a in range(1,r+2):
        for b in range(1,r+3-a):
            c=(90-3*k)-7*(r-a-b+2)
            assert c==13+4*k+7*(a+b)
            total=0
            for rootA in range(a):
                for rootB in range(b):
                    if rootA==0 and rootB==0:total+=c
                    elif (rootA==0) != (rootB==0):total+=56
            expected=Fraction(total,a*b)
            closed=Fraction(63*(a+b)+4*k-99,a*b)
            assert expected==closed
            pairs.append({'a':a,'b':b,'root_root_coefficient':c,'expected_cross_edge_gain':str(expected)})
    f=min(Fraction(x['expected_cross_edge_gain']) for x in pairs)
    B=36*comb(k,2)+r*(330+28*(k-1)-comb(k-1,2))
    deduction=B+M*f
    integer=(deduction.numerator+deduction.denominator-1)//deduction.denominator
    assert deduction>2288
    rows.append({'rank':r,'components':k,'base':B,'all_size_partitions':partitions_checked,
                 'all_component_pair_sizes':pairs,'minimum_cross_edges':M,
                 'minimum_expected_gain':str(f),'deduction_lower':str(deduction),
                 'integer_deduction_lower':integer})
assert [x['base'] for x in rows]==[1920,2104,2271]
assert [x['minimum_cross_edges'] for x in rows]==[10,6,2]
assert [x['minimum_expected_gain'] for x in rows]==['40','299/9','179/6']
assert [x['deduction_lower'] for x in rows]==['2320','6910/3','6992/3']
global_deduction=min(2328,2346,2376,2463,*(x['integer_deduction_lower'] for x in rows))
assert global_deduction==2304
D=comb(17,10);red=9*comb(13,6)-global_deduction;blue=22*comb(13,10)
assert (D,red,blue,D-red-blue)==(19448,13140,6292,16)
out={'status':'PASS_COMPLETE_NINE_RED_LEMMA_SCALARS',
     'review_independence':'same-family','acceptance_status':'provisional',
     'fourset_families_enumerated':0,'H_enumerated':0,'rank3_to5':rows,
     'global_deduction_lower':global_deduction,'red_union_upper':red,
     'blue_union_upper':blue,'minimum_successful_samples':D-red-blue,
     'actual_scope':'Universal9 distinct red4sets/22 indexed blue4sets on17;22 q3 source24 caller given prior complete classification imports.',
     'cpu_seconds':time.process_time()-start}
(HERE/'ALTERNATIVE_COMPONENT_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rank3_to5'},indent=2))
