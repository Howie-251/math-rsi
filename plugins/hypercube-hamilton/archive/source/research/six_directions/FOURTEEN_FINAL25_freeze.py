"""Single immutable producer freeze; independent review remains external."""
from pathlib import Path
import json,hashlib,datetime
P=Path(__file__).resolve().parent;dest=P/'FOURTEEN_FINAL25_MANIFEST.json';assert not dest.exists()
names={'FOURTEEN_FINAL25_PROOF.md','FOURTEEN_FINAL25_APPLICATION.md','FOURTEEN_FINAL25_freeze.py',
'FOURTEEN_FINAL25_A_search.cpp','FOURTEEN_FINAL25_B0_search.cpp','FOURTEEN_FINAL25_B1_search.cpp',
'FOURTEEN_FINAL25_prepare.py','FOURTEEN_FINAL25_make_A.py','FOURTEEN_FINAL25_extract.py','FOURTEEN_FINAL25_B_extract.py',
'FOURTEEN_FINAL25_B_candidate_classes.json','FOURTEEN_FINAL25_B_summary.json','FOURTEEN_FINAL25_B_author_check.py','FOURTEEN_FINAL25_B_author_check.json',
'FOURTEEN_FINAL25_FORMAL_options.json','FOURTEEN_FINAL25_checked_options.json','FOURTEEN_FINAL25_author_finite.py','FOURTEEN_FINAL25_author_finite.json','FOURTEEN_FINAL25_actual_witnesses.bin',
'FOURTEEN_MID_SELECTED_PROOF.md','FOURTEEN_MID_SELECTED_MANIFEST.json',
'HIGHER_FORCED_CHERRY_TRANSFER.md','HIGHER_FORCED_CHERRY_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.md',
'TWELVE_STAR_MAXIMAL_A_REDUCTION.md','TWELVE_STAR_MAXIMAL_A_REVIEW.json','TWELVE_STAR_MAXIMAL_A_REVIEW.md',
'TWELVE_ROOT_STAR_OPENING_case_00_forests.bin','TWELVE_ROOT_STAR_OPENING_case_03_forests.bin',
'SIXTEEN_STAR_author_finite.py','A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md'}
for orbit,classes in [(0,[0,1,7]),(1,[0,1])]:
 for i in classes:
  for prefix in [f'FOURTEEN_FINAL25_B{orbit}_{i:03d}',f'FOURTEEN_FINAL25_B_reduced_{100*orbit+i:03d}']:
   names|={p.name for p in P.glob(prefix+'*') if p.is_file()}
 for suffix in ['.json','_certificates.bin','_unhit.jsonl']:names.add(f'FOURTEEN_FINAL25_A_full_{orbit}'+suffix)
 names.add(f'FOURTEEN_FINAL25_options_{orbit}.bin')
for v in [1,7,31]:
 names.add(f'FOURTEEN_MID_SELECTED_remaining_v{v}_covered.bin');names.add(f'FOURTEEN_FINAL25_remaining_v{v}_covered.bin')
assert hashlib.sha256((P/'FOURTEEN_MID_SELECTED_PROOF.md').read_bytes()).hexdigest()=='2fb632aa4ba65d469c1790badcb3b815cd72ee840a5e787dd4d8cd383a00d282'
assert hashlib.sha256((P/'FOURTEEN_MID_SELECTED_MANIFEST.json').read_bytes()).hexdigest()=='399ec9d673724ff8202e3b546a1ee9e6be97cad3ddaaa1643dc0ea42b4871c93'
source_review=P/'FOURTEEN_MID_SELECTED_REVIEW.json';source_status='PENDING_AT_FREEZE'
if source_review.exists():
 review=json.loads(source_review.read_text());assert review['verdict']=='PASS';source_status='FINAL_PASS_AT_FREEZE';names|={source_review.name,'FOURTEEN_MID_SELECTED_REVIEW.md'}
 for v in [1,7,31]:
  name=f'FOURTEEN_MID_SELECTED_remaining_v{v}_covered.bin';assert review['audited_input_hashes'][name].removeprefix('sha256:')==hashlib.sha256((P/name).read_bytes()).hexdigest()
hashes={name:hashlib.sha256((P/name).read_bytes()).hexdigest() for name in sorted(names)}
out={'status':'FROZEN_PRODUCER_POSITIVE_PACKAGE_PENDING_INDEPENDENT_REVIEW','generated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
'proof':'FOURTEEN_FINAL25_PROOF.md','application':'FOURTEEN_FINAL25_APPLICATION.md','input_hashes':hashes,
'required_source_gate':'FOURTEEN_MID_SELECTED_REVIEW.json','source_gate_status_at_freeze':source_status,
'details':{'local_indices':[0,1,7,100,101],'local_forests':2560,'local_matrix_bits':1310720,'maximal_A_domain_by_orbit':[291743,513263],'positive_A_records':805006,'input_covered_geometries':25,'positive_geometries':25,'remaining_covered_target_geometries':0,'independent_acceptance':False,'full_fourteen_hole_assembly_in_this_package':False,'full_fourteen_hole_proved':False,'full_P6_proved':False}}
dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for name in ['FOURTEEN_FINAL25_PROOF.md','FOURTEEN_FINAL25_APPLICATION.md',dest.name]:print(name,hashlib.sha256((P/name).read_bytes()).hexdigest())
print('bound_files',len(hashes),'source_gate',source_status)
