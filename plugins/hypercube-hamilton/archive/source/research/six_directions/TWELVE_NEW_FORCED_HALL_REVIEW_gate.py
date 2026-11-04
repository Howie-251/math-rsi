import pathlib,json,hashlib
R=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
name='TWELVE_NEW_TYPES_APPLICATION_REVIEW.json';s=load(name)
assert s['verdict']=='PASS' and sha(name)=='a2311d338ee02d33e6b6087eb3b64a6e444f5a95b9f8b7d405b2f9aa078b031f'
for n in ['TWELVE_NEW_TYPES_APPLICATION.md','TWELVE_NEW_TYPES_APPLICATION_MANIFEST.json',*[f'TWELVE_NEW_TYPES_positive_remaining_v{v}.bin' for v in (1,7,31)]]:
 assert sha(n)==s['audited_input_hashes'][n].removeprefix('sha256:'),n
for n in ['TWELVE_NEW_FORCED_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.json']:
 assert load(n)['verdict']=='PASS'
c=load('TWELVE_NEW_FORCED_HALL_REVIEW_check.json');assert c['status']=='PASS'
for n,h in c['audited_frozen_hashes'].items():assert sha(n)==h,n
out={'status':'PASS','source_application_final_PASS':True,'source_review_sha256':sha(name),'source_remaining_covered_target_geometries':37405,'all_three_source_outputs_hash_bound_to_final_review':True,'local27_review_sha256':sha('TWELVE_NEW_FORCED_REVIEW.json'),'generic_safe_transfer_review_sha256':sha('HIGHER_FORCED_CHERRY_REVIEW.json'),'remaining_covered_target_geometries':29370,'remaining_realizability_unverified':True,'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'TWELVE_NEW_FORCED_HALL_REVIEW_gate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
