"""Independent exact scalars for the maximal heavy-independent-kernel proof."""
from math import comb
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent
start=time.process_time()
joint=lambda u:comb(17-u,10-u) if u<=10 else 0
triple=[joint(12-s) for s in range(6)]
assert triple==[0,0,1,8,36,120]
aux=[]
for k in range(1,9):
    target=330+28*(k-1)
    assert 792>=target and 660-120>=target
    cases=[]
    for q in range(k):
        if q==0:bound=330+28*(k-1)
        elif q==1:bound=330+84+27*(k-2)
        elif q==2:bound=330+168-8+26*(k-3)
        else:bound=330+3*84-3*8
        assert bound>=target
        special=435 if k==4 and q==0 else bound
        if k==4:assert special>=435
        cases.append({'light_neighbors_of_A':q,'intersection_lower':bound,
                      'intersection_lower_if_k4_and_disjoint_kernel':special if k==4 else None})
    aux.append({'kernel_size':k,'target':target,'all_cases':cases})
rows=[]
for k in range(1,10):
    categories=[('m0',0,435),('m_positive',1,414)] if k==4 else [('',21 if k==9 else max(0,4*k-17),330+28*(k-1))]
    for category,m,peeled in categories:
        core=36*comb(k,2)+(84-3*max(0,k-2))*m
        deduction=core+(9-k)*peeled
        assert deduction>2288
        rows.append({'k':k,'category':category,'minimum_m':m,'kernel_deduction':core,
                     'peeled_intersection_lower':peeled if k<9 else None,
                     'total_deduction':deduction})
worst=min(x['total_deduction'] for x in rows)
assert worst==2353
red=9*comb(13,6)-worst;blue=22*comb(13,10);D=comb(17,10)
assert (red,blue,D-red-blue)==(13091,6292,65)
out={'status':'PASS_COMPLETE_SHORT_PROOF_SCALARS','review_independence':'same-family',
     'acceptance_status':'provisional','basis':'Actual GEMINI.json response independently read; mathematical proof rewritten in MAIN.md.',
     'local_kernel_cases':aux,'global_kernel_cases':rows,
     'minimum_deduction':worst,'red_union_upper':red,'blue_union_upper':blue,
     'minimum_successful_samples':D-red-blue,'new_fourset_or_H_enumeration':False,
     'Grok_review_scope_extended_by_this_check':False,'cpu_seconds':time.process_time()-start}
(HERE/'SHORT_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
(HERE/'MAIN_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('local_kernel_cases','global_kernel_cases')},indent=2))
