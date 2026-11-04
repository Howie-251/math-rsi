"""Accept finalized twelve-hole reviews only; preserve full-P6 open status."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
cache={}
def sha(p):
    p=p.resolve();s=p.stat();key=(str(p),s.st_size,s.st_mtime_ns)
    if key not in cache:
        h=hashlib.sha256()
        with p.open('rb') as f:
            for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
        cache[key]=h.hexdigest()
    return cache[key]
def checked(name):
    p=R/name
    if not p.exists():return None
    d=json.loads(p.read_text(encoding='utf-8'))
    if d.get('verdict')!='PASS':return None
    assert d.get('audited_input_hashes'),name
    for key in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes',
                'audit_artifact_hashes','producer_comparison_hashes','accepted_import_source_bindings','evidence_hashes']:
        for filename,digest in d.get(key,{}).items():
            q=Path(filename)
            if not q.is_absolute():q=R/q
            assert sha(q)==digest.removeprefix('sha256:'),(name,filename)
    if d.get('report_hash'):
        assert sha(R/name.replace('.json','.md'))==d['report_hash'].removeprefix('sha256:'),name
    return d
names=['HIGHER_Q5_FULL_REVIEW.json','HIGHER_Q5_FULL_REUSE_REVIEW.json',
       'HIGHER_FORCED_CHERRY_REVIEW.json','Q5_T37_INDEPENDENT_REVIEW.json',
       'HIGHER_Q5_FULL_T37_APPLICATION_REVIEW.json','TWELVE_HOLE_FREE_REVIEW.json',
       'TWELVE_NEW_TYPES_LOCAL_REVIEW.json','TWELVE_NEW_FORCED_REVIEW.json',
       'TWELVE_NEW_TYPES_APPLICATION_REVIEW.json','TWELVE_NEW_FORCED_HALL_REVIEW.json',
       'TWELVE_EXTRA_TYPES_REVIEW.json','TWELVE_EXTRA_FORCED_REVIEW.json',
       'TWELVE_MIXED_HALF_LAYER_REVIEW.json','TWELVE_STAR_B_REVIEW.json',
       'TWELVE_STAR_MAXIMAL_A_REVIEW.json','TWELVE_STAR_MAXIMAL_A_FINITE_REVIEW.json',
       'TWELVE_HOLE_FULL_REVIEW.json']
reviews={n:checked(n) for n in names}
near,reuse,cherry,t37,app,free,newlocal,newforced,newapp,forcedhall,extra,extraforced,mixed,starb,maximal,finite,full=(reviews[n] for n in names)
assert near and reuse and cherry and t37 and app
ad=app['details'];assert ad['remaining']==ad['remaining_covered']==215243 and ad['remaining_free']==0
if free:
    fd=free['details'];assert fd['twelve_hole_free_targets_proved'] is True
    assert fd['remaining_free_target_geometries']==0 and fd['full_twelve_hole_proved'] is False and fd['full_P6_proved'] is False
remaining=215243;bytarget={'1':59684,'7':68385,'31':87174};latest=names[4]
if newapp:
    assert newlocal
    nd=newapp['details'];assert nd['remaining_covered_target_geometries']==37405
    assert nd['full_twelve_hole_proved'] is False and nd['full_P6_proved'] is False
    remaining=37405;bytarget={'1':8032,'7':11661,'31':17712};latest=names[8]
if forcedhall:
    assert newapp and newforced
    hd=forcedhall['details'];assert hd['remaining_covered_target_geometries']==29370
    assert hd['full_twelve_hole_proved'] is False and hd['full_P6_proved'] is False
    remaining=29370;bytarget={'1':6315,'7':9828,'31':13227};latest=names[9]
if extra:
    assert forcedhall
    ed=extra['details'];assert ed['local_11_marked_inputs_proved'] is True
    assert ed['remaining_covered_target_geometries']==1281 and ed['full_twelve_hole_proved'] is False and ed['full_P6_proved'] is False
    remaining=1281;bytarget={'1':0,'7':504,'31':777};latest=names[10]
if extraforced:
    assert extra
    xd=extraforced['details'];assert xd['local_15_forced_inputs_proved'] is True
    assert xd['remaining_covered_target_geometries']==235 and xd['full_twelve_hole_proved'] is False and xd['full_P6_proved'] is False
    remaining=235;bytarget={'1':0,'7':0,'31':235};latest=names[11]
if full:
    assert free and extraforced and starb and maximal and finite
    full_details=full['details'];assert full_details['full_twelve_hole_proved'] is True
    assert full_details['remaining_covered_target_geometries']==full_details['remaining_free_target_geometries']==0
    assert full_details['full_P6_proved'] is False
    remaining=0;bytarget={'1':0,'7':0,'31':0};latest='TWELVE_HOLE_FULL_REVIEW.json'
for name in ['RUN_STATE.json','PROOF_CHECK_STATE.json']:
    p=R/name;d=json.loads(p.read_text(encoding='utf-8'))
    assert d['full_ten_hole_proved'] and not d['full_p6_proved']
    d.update(higher_q5_full_nearbalanced_reduction_proved=True,
             higher_q5_full_nearbalanced_review=names[0],
             higher_forced_cherry_transfer_proved=True,higher_forced_cherry_review=names[2],
             q5_t37_55_marked_inputs_proved=True,q5_t37_review=names[3],
             twelve_hole_free_targets_proved=bool(free),twelve_hole_covered_targets_proved=False,
             full_twelve_hole_proved=False,full_p6_proved=False,
             remaining_full_p6_hole_levels=[12,14,16,18],
             twelve_hole_geometry_residual={'review':latest,'covered_remaining':remaining,
                 'covered_by_target':bytarget,'free_remaining_after_accepted_routes':0,
                 'full_free_branch_assembly_accepted':bool(free),
                 'status':'Exact remaining domain for accepted routes; covered configurations remain OPEN'},
             twelve_hole_accepted_reviews={n:sha(R/n) for n,v in reviews.items() if v})
    if free:d['twelve_hole_free_review']=names[5]
    d['q5_twelve_new_111_marked_inputs_proved']=bool(newlocal)
    d['q5_twelve_new_27_forced_classifications_proved']=bool(newforced)
    d['q5_twelve_extra_11_marked_inputs_proved']=bool(extra)
    d['q5_twelve_extra_15_forced_inputs_proved']=bool(extraforced)
    d['q5_mixed_ordinary_half_layer_classification_proved']=bool(mixed)
    d['q5_star_B_10_forced_inputs_proved']=bool(starb)
    d['q6_star_maximal_A_conditional_reduction_proved']=bool(maximal)
    d['q6_star_maximal_A_finite_premise_proved']=bool(finite)
    if full:
        d['full_twelve_hole_proved']=True
        d['twelve_hole_covered_targets_proved']=True
        d['full_twelve_hole_review']='TWELVE_HOLE_FULL_REVIEW.json'
        d['remaining_full_p6_hole_levels']=[14,16,18]
        d['twelve_hole_geometry_residual']['status']='Complete twelve-hole prescribed endpoint theorem accepted relative to explicit imports and exact finite certificates'
    if name=='RUN_STATE.json':
        d['last_goal_turn_classification']='progress'
        d['latest_proof_package']='TWELVE_HOLE_FREE_CLOSURE.md' if free else 'HIGHER_Q5_FULL_T37_APPLICATION.md'
        d['active_research_priority']='Close remaining twelve-hole covered-target geometries using exact marked Q5 rank and forced-cherry inputs, then complete14/16/18.'
        d['remaining_structure']=f'Full Q6 2/4/6/8/10 accepted; twelve-hole free branch {"accepted" if free else "assembly pending"}; twelve-hole covered route remaining{remaining}; full12/14/16/18 and P6 OPEN.'
        if full:
            d['latest_proof_package']='TWELVE_HOLE_FULL_CLOSURE.md'
            d['active_research_priority']='Complete14/16/18-hole layers using accepted full12 predecessor, all marked Q5 registries and higher-layer exact witnesses.'
            d['remaining_structure']='Full Q6 2/4/6/8/10/12-hole levels accepted. Full14/16/18 and full P6 remain OPEN.'
    p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'twelve_free_proved':bool(free),'full_twelve_hole_proved':bool(full),'covered_remaining':remaining,'full_P6_proved':False}))
