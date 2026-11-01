"""Exact scalar updates only; unchanged existing local domains are imported."""
from pathlib import Path
from fractions import Fraction as F
import json
HERE=Path(__file__).resolve().parent
P=[(u,v,t,b) for t in range(4) for b in range(24-t) for u in range(t+1) for v in range(min(b,4-u)+1)]
q=F(7,16)
random=max(t*q**3+b*q**4 for u,v,t,b in P)
assert random==F(16121,16384)<1
max5=max(16*u+4*(t-u)+4*v+b-v for u,v,t,b in P if u+v<=2)
max4star=max(16*u+4*(t-u)+4*v+b-v for u,v,t,b in P if u+v<=3)
max4wide=max(46*u+13*(t-u)+13*v+b-v for u,v,t,b in P if u+v<=3)
iso=max(16*u+4*(t-u+v)+b-v for u,v,t,b in P)
isou2=max(16*u+4*(t-u+v)+b-v for u,v,t,b in P if u<=2)
isou3nonmax=max(40+4*v+b-v for u,v,t,b in P if u==t==3)
assert (max5,max4star,max4wide,iso,isou2,isou3nonmax)==(56,68,158,71,62,63)
old=json.loads((HERE.parent/'CHECK_MAX_FOUR.json').read_text())
e3=[]
for r in old['rows']:
 cases=[(r['pair_top_sums'][u]+(t-u+v)*r['h3']+b-v,(u,v,t,b)) for u,v,t,b in P if u+v<=3]
 block,par=max(cases)
 assert block<r['C4']
 e3.append({'graph':r['vector'],'C4':r['C4'],'maximum_block23':block,'max_parameter_uvtb':par,'margin23':r['C4']-block})
assert len(e3)==7 and min(r['margin23'] for r in e3)==20
incidence_maxima=[{'t':t,'b_at_most':(90-3*t)//4,'total_at_most':t+(90-3*t)//4} for t in range(4)]
assert max(r['total_at_most'] for r in incidence_maxima)==23
# Independent payoff check: no clean pure-nine choice exists in the79 records,
# not merely no choice satisfying one chosen totalnegative budget.
sources=[json.loads(s) for s in (HERE.parent/'budget21_difference/P6_REMAINING.jsonl').open()]
clean9=[(i,c['blue'],c['signature']) for i,r in enumerate(sources) for c in r['choices'] if c['signature'][:6]==[9,0,0,0,0,0]]
assert len(sources)==79 and not clean9
out={'status':'PASS','budget_total':23,'random_bound':str(random),
 'maximum_positive_at_least5_disjoint_bound':max5,'maximum_positive4_star_bound':max4star,
 'maximum_positive4_old86_bound':max4wide,'E3_existing7_rows':e3,
 'two_isolates_Kge5_bound':iso,'two_isolates_K4_u_le2_bound':isou2,
 'two_isolates_K4_three_not_distinct_maximal_targets_bound':isou3nonmax,
 'incidence36plus3tplus4b_le126_implies_total23':incidence_maxima,
 'currentP6_sources':len(sources),'clean_pure9_choices':len(clean9),
 'old_allpositive3_remaining_threepoint_and_integer48_branches_use_no_totalB':True,
 'optional_resource86_used_in_certificates':False,
 'scope':'Scalar arithmetic and existing7-row budgetupdate; no new graph or negative-layout classification.'}
(HERE/'CHECK_SCALARS.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
