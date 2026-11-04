"""Freeze positive producer evidence once; never marks independent acceptance."""
from pathlib import Path
import hashlib,json,datetime
P=Path(__file__).resolve().parent;dest=P/'SIXTEEN_STAR_MANIFEST.json';assert not dest.exists()
names={
'SIXTEEN_STAR_PROOF.md','SIXTEEN_STAR_APPLICATION.md','SIXTEEN_STAR_freeze.py',
'SIXTEEN_STAR_A_search.cpp','SIXTEEN_STAR_B_search.cpp','SIXTEEN_STAR_author_finite.py',
'SIXTEEN_STAR_finalize_inputs.py','SIXTEEN_STAR_B_extract.py','SIXTEEN_STAR_make_author_checks.py','SIXTEEN_STAR_B_author_check.py',
'SIXTEEN_STAR_B_author_check.json','SIXTEEN_STAR_author_finite.json','SIXTEEN_STAR_B_summary.json',
'SIXTEEN_STAR_B_candidate_classes.json','SIXTEEN_STAR_FORMAL_options.json','SIXTEEN_STAR_checked_options.json','SIXTEEN_STAR_options_0.bin',
'SIXTEEN_STAR_A_full.json','SIXTEEN_STAR_A_full_certificates.bin','SIXTEEN_STAR_A_full_unhit.jsonl','SIXTEEN_STAR_actual_witnesses.bin',
'SIXTEEN_LOCAL_REVIEW.json','SIXTEEN_LOCAL_REVIEW.md','SIXTEEN_LOCAL_MANIFEST.json',
'HIGHER_FORCED_CHERRY_TRANSFER.md','HIGHER_FORCED_CHERRY_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.md',
'TWELVE_ROOT_STAR_OPENING_case_00_forests.bin','TWELVE_ROOT_STAR_OPENING_case_03_forests.bin',
'A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md'}
for i in [5,6,7]:
 for prefix in [f'SIXTEEN_STAR_B_{i:03d}',f'SIXTEEN_STAR_B_reduced_{i:03d}']:
  names|={p.name for p in P.glob(prefix+'*') if p.is_file()}
for v in [1,7,31]:
 names.add(f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin');names.add(f'SIXTEEN_STAR_remaining_v{v}_covered.bin')
src=json.loads((P/'SIXTEEN_LOCAL_REVIEW.json').read_text());assert src['verdict']=='PASS'
for v in [1,7,31]:
 name=f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin';h=hashlib.sha256((P/name).read_bytes()).hexdigest()
 assert src['audited_input_hashes'][name].removeprefix('sha256:')==h
hashes={name:hashlib.sha256((P/name).read_bytes()).hexdigest() for name in sorted(names)}
out={'status':'FROZEN_PRODUCER_POSITIVE_PACKAGE_PENDING_INDEPENDENT_REVIEW','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
'proof':'SIXTEEN_STAR_PROOF.md','application':'SIXTEEN_STAR_APPLICATION.md','input_hashes':hashes,
'details':{'exact_local_indices':[5,6,7],'local_forests':768,'local_matrix_bits':196608,'maximal_A_domain':120463,'positive_A_certificates':120463,'input_covered_geometries':148,'positive_geometries':30,'remaining_covered_target_geometries':118,'complete_fourteen_hole_dependency_discharged':False,'full_sixteen_hole_proved':False,'full_P6_proved':False,'independent_acceptance':False}}
dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for name in ['SIXTEEN_STAR_PROOF.md','SIXTEEN_STAR_APPLICATION.md',dest.name]:print(name,hashlib.sha256((P/name).read_bytes()).hexdigest())
print('bound_files',len(hashes))
