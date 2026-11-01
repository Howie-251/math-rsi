"""Exact small scalars for the common low-point source reduction; no H search."""
from fractions import Fraction
from math import comb
from pathlib import Path
import json,time

HERE=Path(__file__).resolve().parent
start=time.process_time()
ceil=lambda q:(q.numerator+q.denominator-1)//q.denominator
jobs=[]
for n,r0,wanted in ((22,5,14),(23,6,17),(24,5,17),(25,5,19)):
    s=25-n
    p=Fraction(comb(n//2,5)+comb(n-n//2,5),comb(n,5))
    threshold=next(L for L in range(36) if L*p-2*(35*p-1)>0)
    assert threshold==wanted
    values=[]
    for r in range(1,n+1):
        pair_extra=(r*s)//2
        inclusion=6*r-comb(r,2)-pair_extra
        cauchy=ceil(Fraction(36*r,r+5+s))
        L=max(inclusion,cauchy)
        if r>=r0:assert L>=threshold
        values.append({'r':r,'induced_extra_upper':pair_extra,
                       'inclusion_lower':inclusion,'Cauchy_lower':cauchy,
                       'L_lower':L,'forces_unique_low_source':L>=threshold,
                       'probability_lower':str(L*p-2*(35*p-1))})
    assert not values[r0-2]['forces_unique_low_source']
    jobs.append({'n':n,'repeat_total':s,'balanced_mono_probability':str(p),
                 'sufficient_L':threshold,'strict_margin_at_threshold':str(threshold*p-2*(35*p-1)),
                 'all_r_at_least':r0,'necessary_scalar_domain':values})

# A single explicit24-point profile defeats a direct copy of25's
# private-owner/cross-budget argument. This is not an actual hypergraph.
u=[1,1,0,0,4,4] # p red in the first two blocks, other blocks disjoint
R=sum(u)-1; B=23-R
N1,N2,N3,N4=14,0,4,11
E=N1+N4
cross=4*E+6*(29-E)
W=sum(x*(4-x) for x in u)
red_inc=4*N1+3*N2+2*N3+N4
blue_inc=N1+2*N2+3*N3+4*N4
assert (R,B,E,W,cross,red_inc,blue_inc)==(9,14,25,6,124,75,70)
assert cross>=R*B-W and red_inc>=5*R-1 and blue_inc>=5*B
assert E>=4*4-1 and N1>=14 and N4>=9
witness={'scope':'Color-profile integer relaxation only, not an actual H.',
         'p_color':'red','block_red_counts':u,'R':R,'B':B,'mono_blocks':4,
         'single_flip_lex_forced_private_red':8,'single_flip_lex_forced_private_blue':14,
         'N1_N2_N3_N4':[N1,N2,N3,N4],'E':E,'star_cross_pairs':W,
         'Hbar_cross_incidence':cross,'required_Hbar_cross_pairs':R*B-W,
         'Hbar_red_incidence':red_inc,'Hbar_blue_incidence':blue_inc,
         'all23_vertices_may_have_private_owner':True}
out={'status':'PASS_EXACT_COMMON_SOURCE_SCALARS',
     'review_independence':'same-family','acceptance_status':'provisional',
     'probability_tables_or_layouts':False,'actual_H_search':False,
     'L6_repair_proved':False,'jobs':jobs,'transfer_obstruction':witness,
     'majority_protected_color_upper_all_s_le3':(116+3)//8,
     'cpu_seconds':time.process_time()-start}
(HERE/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('jobs','transfer_obstruction')},indent=2))
