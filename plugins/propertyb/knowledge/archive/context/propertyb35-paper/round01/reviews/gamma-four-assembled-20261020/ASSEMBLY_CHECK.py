from pathlib import Path
from itertools import combinations
from collections import Counter
from math import comb
from fractions import Fraction
import json,time
P=Path(__file__).resolve().parent
ROOT=P.parents[4]; M=ROOT/'context/propertyb35-paper/round01/middle';start=time.process_time()
def read(name):return json.loads((M/name).read_text())
spectra=[[7]*8+[8]+[9]*9+[10]*3,[7]*9+[9]*8+[10]*4,[7]*7+[8]*3+[9]*8+[10]*3]
assert all(len(d)==21 and sum(d)==175 for d in spectra)
# Only independent per-key pair certificates: deliberately do not read any derived Gamma_min4 jobs.
pairs=read('min_degree_seven_low_excess_strong_pairs_20261020/RESULT.json')
keys={(tuple(z['degrees']),z['codegree']):z for z in pairs['keys']}
required=set()
for ds in spectra:
 for u,v in combinations(ds,2):
  for c in range(5,min(u,v)+1):required.add((tuple(sorted((u,v))),c))
for key in required:
 z=keys[key]; cert=z['selected_certificate'];assert z['strict'] and cert['strict']
 assert Fraction(cert['bound'])<1 and not cert['uses_paircover_quotas']
rigid=read('min_degree_seven_low_pair_rigidity_20261020/RESULT.json')
r77=next(z for z in rigid['pairs'] if z['counts']['3']==6)
assert r77['zero_quota'] and r77['independent_35_index_bound']=='200844/230945'
quads=set(q for ds in spectra for q in combinations(ds,4))
assert len(quads)==34
small=read('c13_remaining_actual_quads_20261020/ALL_RESULT.json')
assert {tuple(z['quad']) for z in small['quad_support']}==quads-{(9,10,10,10),(10,10,10,10)}
assert small['labels']==7977 and small['strict_count']==small['representatives']==1073 and not small['nonstrict']
vr=read('c13_remaining_actual_quads_20261020/VERIFY_RESULT.json');assert vr['strict']==1073 and vr['empty_quad_count']==4
low=read('c13_three_ten_nine_seven_pool_20261020/VERIFY_RESULT.json')
assert low['domain']==low['strict']==470 and low['zero_quota_also_strict_all470']
assert low['maximum_zero_same_selected_positions']=='33937/34320'
ten=read('generic_c3_thirteen_pilot_20261020/audit/VERIFY_304.json')
assert ten['complete_domain']==310 and ten['strict_certificates']==304 and ten['remaining_six_types']==6
for dirname,total,lowcount in [('shared_views',2908,2054),('shared_views_orbit2',2820,1967)]:
 d=read('c13_four_ten_seven_pool_20261020/'+dirname+'/VERIFY_DUAL.json')
 assert d['status']=='PASS_COMPLETE_ACTUAL_DOMAIN_AND_EXACT_CHARGING_CLOSURE'
 assert d['complete_views']==total and d['low_charge_strict_views']==lowcount
 assert d['charging_actual_sum']==192 and d['charging_if_all_failed_minimum']==204
transport=read('c13_four_ten_seven_pool_20261020/SIX_SOURCE_TRANSPORT.json')
assert transport['status']=='PASS_ALL_SIX_ACTUAL_SOURCE_TRANSPORTS' and len(transport['sources'])==6
for mu,co in [([14,0,1,3,0,4,3,0,1,3,3,0,3,0,0,0],{0:2,2:1,3:1,8:3,12:3}),([14,0,1,3,1,4,2,0,0,3,4,0,3,0,0,0],{0:2,2:1,3:1,4:3,12:3})]:
 assert sum(mu)==35 and all(sum(n for mask,n in enumerate(mu) if mask>>v&1)==10 for v in range(4))
 assert sum(mu[m]*(5-m.bit_count())*c for m,c in co.items())==192
clean=read('min_degree_seven_clean_star_20261020/VERIFY_RESULT.json')
assert (clean['generic119'],clean['minF7_inputs'],clean['minF7_strict'],clean['minF7_nonstrict'],clean['clean_star_inputs'])==(119,102,97,5,1171)
assert clean['all1273_fixed_best_bounds_equal']
high=read('min_degree_seven_clean_star_20261020/high_clean_11_12/RESULT.json')
assert high['checked']==high['strict_count']==481 and high['maximum']=='4947/5005'
f=lambda s:sum((s//5+(i<s%5))*(s//5+(j<s%5)) for i in range(5) for j in range(i))
assert f(30)==360 and sum(a*b for a,b in combinations([4,7,7,7,6],2))==381
assert 381+33*f(30)+f(29)==12597
# General two-flip probabilities at n21,k5,a10; no maximum-degree hypothesis.
D=comb(21,10);pn=comb(16,5)+comb(16,10);qn=comb(12,5)+comb(12,6)
rn=[comb(8+j,1+j)+comb(8+j,6) for j in range(5)]
assert (D,qn,rn)==(352716,1716,[36,120,330,792,1716])
assert 40*D-700*pn==5445440 and 4*qn==6864
scalar=read('min_degree_seven_q3_b_moments_20261020/ACTUAL_D1/RESULT.json')
assert scalar['complete_domain']==252278 and scalar['all_survivor_counts_zero']
for j,ds,w,s6,count,maxL in zip(scalar['jobs'],spectra,[655,657,654],[57,58,57],[83833,85441,83004],[2717052,2721924,2715645]):
 assert j['degrees']==ds and sum(comb(d,2) for d in ds)==w==j['W']
 assert sum(sorted(ds)[-6:])==s6==j['actual_S6'] and j['complete_domain']==count
 assert j['maximum_twice_L']==2*maxL<5445440 and j['survivor_count']==0
result={'status':'PASS_BOUNDED_ASSEMBLY_INTERFACE_CHECK','review_independence':'same-family','acceptance_status':'provisional','not_a_fresh_proof_checker':True,'no_large_certificate_replays':True,'actual_strong_pair_keys_checked':len(required),'actual_quad_multisets':len(quads),'scalar_keys_receipt_bound':252278,'tiny_two_flip_numerators_verified':True,'shared_column_sums':[192,192],'cpu_seconds':time.process_time()-start}
assert result['cpu_seconds']<3
(P/'ASSEMBLY_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
