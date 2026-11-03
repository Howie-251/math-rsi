"""Bounded source-derived controls; m25 output is free-capacity only."""
import collections,json,math,pathlib,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(299,300))
from analyze import route_forms,order
P=pathlib.Path(__file__).resolve().parent;start=time.process_time()
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
pred={'prediction_id':'P_DHAR_FIXED_R4_P127','frozen_before_target_capacity_or_endpoint_tests':True,'target':[10,4],'savedL':2485,'m':35,'p':127,'r':4,'action_order':7,'n':{'actual':None,'hypothetical':4445},
 'fixed_positive_phases':[1,3,6,7,9],'fixed_translation_rule':['0','r^2-1','-r^2-1','-r','1'],
 'falsifiable_prediction':'The fixed source-derived quadratic lift at r4 mod127 will fail complete4-step coverage already in phase15 orphase20.',
 'reason':'Source thin phases15/20 have215 raw words for71 endpoints and7 singly covered source endpoints each; at127 the same raw route/endpoint margin shrinks from3.03 to1.69. A clean polynomial representation is not itself a uniform covering proof.',
 'scope':'One canonical integer-action transfer, no free offsets or numeric parameter search. Additional controls are free-form capacity only.',
 'm25_rule':'Root owns allm25 fixed-quadratic numerical tests. This process computes m25 free-form capacity only and no polynomial endpoint evaluation.',
 'no_BFS_or_old_graph_regeneration':True}
save('PREDICTION.json',pred)
controls=[]
for p,k,rr in [(101,5,None),(113,7,None),(127,7,4),(211,35,None)]:
 roots=[r for r in range(2,p)if pow(r,k,p)==1 and all(pow(r,d,p)!=1 for d in range(1,k)if k%d==0)]
 r=rr if rr else min(roots)
 rows,forms,counts=route_forms(p,r)
 thin=min(x['distinct_free4_forms']for x in rows)
 a={'m':35,'p':p,'r':r,'order':order(r,p),'group_order':35*p,'all_roots_of_this_exact_order':roots,'action_tested':'Only the declared representative root','minimum_free4_form_capacity':thin,'thin_phases':[x['phase']for x in rows if x['distinct_free4_forms']==thin],
 'capacity_by_phase':[x['distinct_free4_forms']for x in rows],'phase15_capacity':rows[15]['distinct_free4_forms'],'phase20_capacity':rows[20]['distinct_free4_forms'],'capacity_passed':thin>=p}
 if p==127:
  v=[(r*r-1)%p,(-r*r-1)%p,(-r)%p,1];ends=[{sum(a*b for a,b in zip(f,v))%p for f in fs}for fs in forms]
  a.update({'fixed_translations':[0]+v,'fixed_quadratic_coverage_by_phase':[len(s)for s in ends],'fixed_quadratic_missing_states':sum(p-len(s)for s in ends),'full_hit':all(len(s)==p for s in ends),'phase15_missing':sorted(set(range(p))-ends[15]),'phase20_missing':sorted(set(range(p))-ends[20])})
  pred['actual_verdict']='SUPPORTED'if len(ends[15])<p or len(ends[20])<p else'REFUTED'
 controls.append(a)
save('M35_CONTROLS.json',{'status':'FOUR_DECLARED_CONTROLS_COMPLETE','controls':controls,'source_BFS':0,'new_graphs_generated':0,'CPU_seconds':time.process_time()-start,'prediction_verdict':pred['actual_verdict']})
# Independent free-form capacity for root-owned C25 comparison; no fixed values.
m=25;p=101;roots=[r for r in range(2,p)if pow(r,25,p)==1 and pow(r,5,p)!=1]
cap25=[]
for r in roots:
 rows,_,_=route_forms(p,r,m=m)
 cap25.append({'r':r,'minimum_capacity':min(x['distinct_free4_forms']for x in rows),'thin_phases':[x['phase']for x in rows if x['distinct_free4_forms']==min(a['distinct_free4_forms']for a in rows)],'capacity_by_phase':[x['distinct_free4_forms']for x in rows],'raw_words_by_phase':[x['raw_words_total']for x in rows]})
save('M25_CAPACITY_ONLY.json',{'status':'FREE_FORM_CAPACITY_ONLY_20_ACTIONS','m':25,'p':101,'hypothetical_order':2525,'roots':roots,'actions':cap25,'all_actions_capacity_passed':all(min(a['capacity_by_phase'])>=101 for a in cap25),'numeric_offset_cases':0,'root_owns_numeric_polynomial_tests':True,'CPU_seconds_cumulative':time.process_time()-start})
# Arithmetic candidate list, no generator/offset evaluation.
primes=[p for p in range(72,216)if all(p%d for d in range(2,math.isqrt(p)+1))and math.gcd(35,p-1)>1]
save('ORDER_ARITHMETIC.json',{'fixed_quotient':35,'degree10_D4_Moore':8201,'strict_baseline':2485,'phase15_raw_word_upper_bound':215,'field_size_range_from_both_bounds':[72,215],
 'prime_fields_with_nontrivial_legal_action':[{'p':p,'order':35*p,'possible_action_orders':[d for d in [5,7,35]if(p-1)%d==0]}for p in primes],
 'r1_abelian_Lee_radius4_dimension5_bound':681,'r1_excluded_reason':'681<2485; no numeric enumeration',
 'scope':'Arithmetic options only, not a list of executed parameter searches or recommended additional runs.'})
print('M35',[(a['p'],a['r'],a['minimum_free4_form_capacity'],a['thin_phases'],a.get('fixed_quadratic_missing_states'))for a in controls])
print('P127',pred['actual_verdict'],'phase15/20 coverage',controls[2]['fixed_quadratic_coverage_by_phase'][15],controls[2]['fixed_quadratic_coverage_by_phase'][20])
print('M25 capacity only',len(roots),'allpass',all(a['minimum_capacity']>=101 for a in cap25),'min',min(a['minimum_capacity']for a in cap25),'maxmin',max(a['minimum_capacity']for a in cap25),'CPU',time.process_time()-start)
