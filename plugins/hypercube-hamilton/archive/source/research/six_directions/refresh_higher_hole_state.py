"""Accept the fresh ten-hole free-endpoint review with frozen hash checks."""
import hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parent
hash_cache={}
def sha(p):
    stat=p.stat();key=(str(p.resolve()),stat.st_size,stat.st_mtime_ns)
    if key in hash_cache:return hash_cache[key]
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
    hash_cache[key]=h.hexdigest()
    return hash_cache[key]
def check_map(d):
    for name,digest in d.items():
        p=Path(name)
        if not p.is_absolute():p=R/p
        assert sha(p)==digest.removeprefix('sha256:'),name
review=json.loads((R/'TEN_HOLE_FREE_REVIEW.json').read_text(encoding='utf-8'))
assert review['verdict']=='PASS'
for key in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
    assert review[key]
    check_map(review[key])
detail=review['details']['independent_check']
assert detail['status']=='PASS' and detail['census']['remaining']==0
check_map(detail['hashes'])
assert sha(R/'TEN_HOLE_FREE_REVIEW.md')==review['report_hash'].removeprefix('sha256:')
assert {x['v']:x['eligible'] for x in detail['census']['targets']}=={7:2919186,31:3575055}
conditional=json.loads((R/'Q5_HIGHER_HOLE_REDUCTION_REVIEW.json').read_text(encoding='utf-8'))
assert conditional['verdict']=='PASS'
for key in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
    check_map(conditional[key])
new_aux_reviews=['A8_PARTIAL_REVIEW.json','A8_DELTA4_FIRST_ORBIT_REVIEW.json','Q5_K8_REVIEW.json']
for name in new_aux_reviews:
    package=json.loads((R/name).read_text(encoding='utf-8'))
    assert package['verdict']=='PASS',name
    assert package['audited_input_hashes'],name
    for key in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
        check_map(package.get(key,{}))
def accepted_report(name):
    p=R/name
    if not p.exists():return False
    package=json.loads(p.read_text(encoding='utf-8'))
    if package.get('verdict')!='PASS':return False
    assert package.get('audited_input_hashes'),name
    for key in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes','audit_artifact_hashes','producer_comparison_hashes','accepted_import_source_bindings','evidence_hashes']:
        check_map(package.get(key,{}))
    evidence=package.get('evidence',{})
    if isinstance(evidence,dict) and evidence and all(isinstance(v,str) and len(v.removeprefix('sha256:'))==64 for v in evidence.values()):
        check_map(evidence)
    return True
a8_closed=2600;a8_orbits_left=4;a8_reviews=new_aux_reviews[:2]
for name,count,orbits in [('A8_ORBIT4_FULL_REVIEW.json',30,1),('A8_ORBITS2_3_REVIEW.json',50,2),('A8_ORBIT5_FULL_REVIEW.json',20,1)]:
    if accepted_report(name):a8_closed+=count;a8_orbits_left-=orbits;a8_reviews.append(name)
a8_full=accepted_report('Q5_A8_FULL_REVIEW.json')
if a8_full:assert a8_closed==2700 and a8_orbits_left==0
covered_partial=accepted_report('TEN_HOLE_COVERED_PARTIAL_REVIEW.json')
a8_consequences=accepted_report('Q5_A8_CONSEQUENCES_REVIEW.json')
a10_first=accepted_report('A10_FIRST_ORBIT_REVIEW.json')
a10_second=accepted_report('A10_ORBIT2_REVIEW.json')
a10_last=accepted_report('A10_ORBIT3_UNIVERSAL_REVIEW.json')
a10_full=accepted_report('Q5_A10_FULL_REVIEW.json')
a10_closed=30*int(a10_first)+20*int(a10_second)+5*int(a10_last)
if a10_full:assert a8_full and a10_closed==55
t63_split=accepted_report('Q5_T63_COMPLETE_SPLIT_REVIEW.json')
t63_application=accepted_report('TEN_COVERED_T63_SPLIT_REVIEW.json')
endpoint_application=accepted_report('TEN_COVERED_Q5_ENDPOINT_REVIEW.json')
t26_batch=accepted_report('Q5_T26_RANK_BATCH_REVIEW.json')
if t26_batch:assert endpoint_application
t63_rank=accepted_report('Q5_T63_RANK_REVIEW.json')
if t63_rank:assert t26_batch
t15_rank=accepted_report('Q5_T15_RANK_BATCH_REVIEW.json')
if t15_rank:assert t26_batch and t63_rank
t17_rank=accepted_report('Q5_T17_RANK_BATCH_REVIEW.json')
ten_full=accepted_report('TEN_HOLE_FULL_REVIEW.json')
if ten_full:
    assert t15_rank and t17_rank and t26_batch
    td=json.loads((R/'TEN_HOLE_FULL_REVIEW.json').read_text(encoding='utf-8'))['details']
    assert td['full_ten_hole_proved'] is True and td['full_P6_proved'] is False
    assert td['remaining_covered_target_geometries']==td['remaining_free_target_geometries']==0
if t63_application:assert t63_split and a8_consequences
if endpoint_application:assert a10_full and t63_application
if a8_consequences:assert a8_full and covered_partial
closure={
 'scope':'Every short 27-edge Q6 matching and every pair of free opposite-parity endpoints',
 'proof':'TEN_HOLE_FREE_CLOSURE.md','review':'TEN_HOLE_FREE_REVIEW.json',
 'review_sha256':sha(R/'TEN_HOLE_FREE_REVIEW.json'),
 'geometry_count':6494241,'nonbasic_geometry_witnesses':47271,
 'remaining_free_target_geometries':0,'assurance':'same-family/provisional; explicit imports; not formalized'}
for name in ['RUN_STATE.json','PROOF_CHECK_STATE.json']:
    p=R/name;d=json.loads(p.read_text(encoding='utf-8'))
    assert d['full_eight_hole_proved'] and not d['full_p6_proved']
    d.update(ten_hole_free_targets_proved=True,full_ten_hole_proved=False,
             ten_hole_covered_targets_proved=False,ten_hole_free_closure=closure,
             higher_hole_unified_transfer_proved=True,
             higher_hole_unified_transfer_review='HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json',
             q5_a8_a10_conditional_reduction_proved=True,
             q5_a8_a10_conditional_reduction_review='Q5_HIGHER_HOLE_REDUCTION_REVIEW.json',
             q5_a8_proved=a8_full,q5_a10_proved=a10_full,
             q5_k8_cycle_proved=True,q5_k8_review='Q5_K8_REVIEW.json',
             q5_a8_partial={'independent_geometry_domain':2700,'closed_geometries':a8_closed,
                           'remaining_geometries':2700-a8_closed,'remaining_orbits':a8_orbits_left,
                           'reviews':a8_reviews,
                           'scope':'Only finalized independent reviews counted; full A8 requires separate assembly acceptance'},
             remaining_full_p6_hole_levels=[10,12,14,16,18],full_p6_proved=False)
    if a8_full:d['q5_a8_final_review']='Q5_A8_FULL_REVIEW.json'
    d['q5_balanced_eight_endpoint_proved']=a8_consequences
    d['q5_a10_partial']={'closed_geometries':a10_closed,'domain':55,
        'remaining_geometries':55-a10_closed,'remaining_orbits':3-int(a10_first)-int(a10_second)-int(a10_last),
        'reviews':([ 'A10_FIRST_ORBIT_REVIEW.json'] if a10_first else [])+(['A10_ORBIT2_REVIEW.json'] if a10_second else [])+(['A10_ORBIT3_UNIVERSAL_REVIEW.json'] if a10_last else []),
        'full_A10_proved':a10_full}
    d['q5_all_balanced_hole_endpoints_proved']=a10_full
    d['q5_all_balanced_hole_cycles_proved']=a10_full
    d['q5_all_imbalance_two_avoid_one_proved']=a10_full
    d['q5_t63_marked_split_proved']=t63_split
    if a10_full:d['q5_a10_final_review']='Q5_A10_FULL_REVIEW.json'
    if t63_split:d['q5_t63_marked_split_review']='Q5_T63_COMPLETE_SPLIT_REVIEW.json'
    if covered_partial:
        d['covered_ten_geometry_residual']={'review':'TEN_HOLE_COVERED_PARTIAL_REVIEW.json',
             'eligible_normalized_geometries':145248180,'remaining':91225,'by_target':{'1':26880,'7':29955,'31':34390},
             'status':'Exact remaining domain for the audited partial route; all remaining configurations OPEN'}
    if a8_consequences:
        d['q5_balanced_eight_endpoint_review']='Q5_A8_CONSEQUENCES_REVIEW.json'
        d['covered_ten_geometry_residual']={'review':'Q5_A8_CONSEQUENCES_REVIEW.json',
             'eligible_normalized_geometries':145248180,'remaining':54222,'by_target':{'1':16920,'7':17022,'31':20280},
             'newly_covered_by_full_A8':37003,
             'status':'Exact remaining domain for the audited route; all remaining configurations OPEN'}
    if t63_application:
        d['covered_ten_geometry_residual']={'review':'TEN_COVERED_T63_SPLIT_REVIEW.json',
             'eligible_normalized_geometries':145248180,'remaining':41306,'by_target':{'1':12920,'7':12726,'31':15660},
             'newly_covered_by_T63_split':12916,'status':'Exact remaining domain; full ten-hole covered branch OPEN'}
    if endpoint_application:
        d['covered_ten_geometry_residual']={'review':'TEN_COVERED_Q5_ENDPOINT_REVIEW.json',
             'eligible_normalized_geometries':145248180,'remaining':41236,'by_target':{'1':12910,'7':12696,'31':15630},
             'newly_covered_by_full_Q5_endpoints':70,'status':'Exact combined remaining domain; full ten-hole covered branch OPEN'}
    if t26_batch:
        d['q5_t26_actual_55_marked_orbits_proved']=True
        d['q5_t26_actual_review']='Q5_T26_RANK_BATCH_REVIEW.json'
        d['covered_ten_geometry_residual']={'review':'Q5_T26_RANK_BATCH_REVIEW.json',
             'eligible_normalized_geometries':145248180,'remaining':4096,'by_target':{'1':910,'7':1476,'31':1710},
             'newly_covered_by_T26_rank_inputs':37140,'status':'Exact combined remaining domain; full ten-hole covered branch OPEN'}
    if t63_rank:
        d['q5_t63_actual_7_rank_orbits_proved']=True
        d['covered_ten_geometry_residual']={'review':'Q5_T63_RANK_REVIEW.json',
             'eligible_normalized_geometries':145248180,'remaining':2353,'by_target':{'1':580,'7':783,'31':990},
             'newly_covered_by_T63_rank_inputs':1743,'status':'Exact combined remaining domain; full ten-hole covered branch OPEN'}
    if t15_rank:
        d['q5_t15_actual_15_rank_orbits_proved']=True
        d['covered_ten_geometry_residual']={'review':'Q5_T15_RANK_BATCH_REVIEW.json',
             'eligible_normalized_geometries':145248180,'remaining':889,'by_target':{'1':280,'7':279,'31':330},
             'status':'Exact T15/T63 union remaining domain; full ten-hole covered branch OPEN'}
    if t17_rank:d['q5_t17_actual_17_rank_classifications_and_safe_transfer_proved']=True
    if ten_full:
        d['full_ten_hole_proved']=True
        d['ten_hole_covered_targets_proved']=True
        d['full_ten_hole_review']='TEN_HOLE_FULL_REVIEW.json'
        d['remaining_full_p6_hole_levels']=[12,14,16,18]
        d['covered_ten_geometry_residual']={'review':'TEN_HOLE_FULL_REVIEW.json',
             'eligible_normalized_geometries':145248180,'remaining':0,'by_target':{'1':0,'7':0,'31':0},
             'status':'Complete ten-hole arbitrary prescribed endpoint theorem accepted relative to explicit imports'}
    if name=='RUN_STATE.json':
        d['last_goal_turn_classification']='progress'
        d['latest_proof_package']='Q5_A10_FULL_CLOSURE.md' if a10_full else ('A10_ORBIT2_REDUCTION.md' if a10_second else ('Q5_A8_FULL_CLOSURE.md' if a8_full else 'TEN_HOLE_FREE_CLOSURE.md'))
        d['active_research_priority']='Develop full-rank short-forest certificates for actual marked multiple-omission Q5 inputs; finish ten-hole covered targets and remaining higher P6 layers.' if a10_full else ('Prove the last A10 orbit and Q5 marked multiple-omission inputs; develop four-bridge zero-crossing gluing for ten-hole covered targets.' if a8_consequences else ('Apply full A8 to ten-hole covered targets; prove remaining marked multiple-omission inputs and A10.' if a8_full else 'Prove ten-hole covered targets; develop shared Q5 A8/A10 inputs for remaining higher layers.'))
        d['remaining_structure']='Full eight-hole and ten-hole free-target branches accepted. Ten-hole covered targets and full 12/14/16/18-hole layers remain open.'
        d['current_exploration']={'A8':('COMPLETE relative to imports, same-family/provisional' if a8_full else f'OPEN; {a8_closed}/2700 geometries closed; remaining{2700-a8_closed} in{a8_orbits_left}orbits'),
                                  'A10':('COMPLETE relative to imports and independently verified rank certificate' if a10_full else f'OPEN; {a10_closed}/55 geometries closed, remaining{55-a10_closed} in{3-int(a10_first)-int(a10_second)-int(a10_last)}orbits'),
                                  'higher_Q5_reduction':('All Q5 balanced endpoint/cycle and imbalance-two avoid-one inputs accepted; no complete higher Q6 layer inferred' if a10_full else 'Conditional on A8 and A10; no complete higher Q6 layer inferred')}
        if ten_full:
            d['latest_proof_package']='TEN_HOLE_FULL_CLOSURE.md'
            d['active_research_priority']='Prove the 12/14/16/18-hole reduced independent domains using all-balanced Q5 endpoint and marked short-forest rank certificates.'
            d['remaining_structure']='Full Q6 2/4/6/8/10-hole levels accepted. Full 12/14/16/18-hole levels and full P6 remain open.'
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(closure,ensure_ascii=False))
