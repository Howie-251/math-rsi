from fractions import Fraction
from math import comb
from pathlib import Path
import json
p=Fraction(2*comb(11,5),comb(22,5));assert p==Fraction(2,57)
rows=[]
for h in range(14,20):
    margin=8*h*p-10*(35*p-1)
    t=int(margin)+1
    event_lower=(margin-(t-1))/(6-t)
    assert event_lower>0 and 2<=t<=4
    rows.append({'unit_pool':h,'weighted_margin':str(margin),'guaranteed_unit_points_in_unique_bad_edge':t,'event_probability_lower':str(event_lower)})
assert rows[0]['guaranteed_unit_points_in_unique_bad_edge']==2
# Exact necessary-degree/swap-count relaxation; not an H or signed-family construction.
b=11;N=[4,15,6,9];A=6;J=[4,17,8,A];c=4
assert sum(N)==34
assert sum((i+1)*v for i,v in enumerate(N))==88
assert sum((4-i)*v for i,v in enumerate(N))==82
assert sum(J)==35
assert all(0<=J[i]<=(4-i)*N[i] for i in range(4))
assert A>=5 and c<=min(b,N[0])
assert sum((i+1)*v for i,v in enumerate(J))>=5*b
swap_rhs=(b-4)*A+5*N[0]-J[0]
assert swap_rhs>=5*b
assert 10-A==4 and c>=4
assert 3*(5-1)>4*8-(22-1)
out={'status':'PASS_NECESSARY_SCALARS_ONLY','balanced_edge_probability':str(p),'weighted_source_rows':rows,'moment_relaxation_witness':{'blue_count':b,'x_color':'red','source_degrees':[8]*5,'N1_N2_N3_N4':N,'G_incidence_J1_J2_J3_A':J,'red_private_counts_on_G':[2,1,1,1,1],'blue_private_vertex_count':c,'blue_degree_total':88,'proper_red_degree_total':82,'G_proper_degree_total':35,'outside_G_red_degree_total':47,'G_blue_pair_associations':sum((i+1)*v for i,v in enumerate(J)),'G_blue_pair_requirement':55,'swap_cover_rhs':swap_rhs,'swap_cover_requirement':55,'is_actual_H_or_signed_counterexample':False},'five_common_private_kernel_exclusion':{'required_row_excess':12,'allowed_max_degree8_n22':11}}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],'p=',p,'min unit intersection=',rows[0]['guaranteed_unit_points_in_unique_bad_edge'],'swap slack=',swap_rhs-55)
