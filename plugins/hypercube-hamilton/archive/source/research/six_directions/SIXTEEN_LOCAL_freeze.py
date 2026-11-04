"""Freeze producer local/application evidence only; no review or state promotion."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
target=R/'SIXTEEN_LOCAL_MANIFEST.json';assert not target.exists(),'Already frozen; do not overwrite.'
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
cert=json.loads((R/'SIXTEEN_LOCAL_CERT_summary.json').read_text());cover=json.loads((R/'SIXTEEN_LOCAL_coverage.json').read_text())
gate=json.loads((R/'HIGHER_POST12_T39_REVIEW.json').read_text());assert gate['verdict']=='PASS'
names=['SIXTEEN_LOCAL_PROOF.md','SIXTEEN_LOCAL_APPLICATION.md','SIXTEEN_LOCAL_prepare.py','SIXTEEN_LOCAL_CERT_summary.json','SIXTEEN_LOCAL_make_author_checks.py','SIXTEEN_LOCAL_author_cert.py','SIXTEEN_LOCAL_author_cert.json','SIXTEEN_LOCAL_author_actual.py','SIXTEEN_LOCAL_author_actual.json','SIXTEEN_LOCAL_author_scan.py','SIXTEEN_LOCAL_author_scan.json','SIXTEEN_LOCAL_author_scan_coverage.json','SIXTEEN_LOCAL_freeze.py','SIXTEEN_LOCAL_profile.py','SIXTEEN_LOCAL_candidate_classes.json','SIXTEEN_LOCAL_coverage.json','SIXTEEN_LOCAL_witnesses.bin','SIXTEEN_LOCAL_all_hit_sets.json','SIXTEEN_NEW_TYPES_profile.json','SIXTEEN_NEW_TYPES_summary.json','HIGHER_POST12_REUSE_PROOF.md','HIGHER_POST12_REUSE_MANIFEST.json','HIGHER_POST12_REUSE_REVIEW.json','HIGHER_POST12_T39_PROOF.md','HIGHER_POST12_T39_MANIFEST.json','HIGHER_POST12_T39_REVIEW.json','HIGHER_FORCED_CHERRY_TRANSFER.md','HIGHER_FORCED_CHERRY_REVIEW.json','HIGHER_HOLE_UNIFIED_TRANSFER.md','HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json','Q5_A10_FULL_REVIEW.json','A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md','FOURTEEN_FORCED_author_check.py','FOURTEEN_FORCED_application_author_check.py']
for v in (1,7,31):
 n=f'SIXTEEN_POST12_FORCED_remaining_v{v}_covered.bin';assert sha(n)==cover['input_hashes'][n] and sha(n)==gate['audited_input_hashes'][n].removeprefix('sha256:')
 names.extend([n,f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin'])
for row in cert['reports']:
 suffixes=['_forests.bin','_pairs.bin','_columns.bin','_matrix.bin','_pivots.bin','_combos.bin','_config.txt','.json']
 if row['forced_pairs']:suffixes.append('_full_pairs.bin')
 names.extend(row['prefix']+s for s in suffixes)
names=list(dict.fromkeys(names))
out={'status':'FROZEN_CONDITIONAL_PRODUCER_LOCAL_AND_ACTUAL_APPLICATION_PENDING_INDEPENDENT_REVIEW','selected_indices':cert['selected_indices'],'forced_indices':[9,11,1,2],'ordinary_indices':[33,7,12,14,15],'complete_fourteen_hole_theorem_required_for_complete_sixteen_domain':True,'predecessor_requirement_discharged_here':False,'source_conditional_application_reviews_final_PASS':True,'source':1012,'producer_sufficient':864,'producer_remaining':148,'remaining_by_target':[0,18,130],'witness_record_bytes':40,'source_record_bytes':15,'local_forests':3328,'local_connectivity_bits':1474560,'hashes':{n:sha(n) for n in names},'sizes':{n:(R/n).stat().st_size for n in names},'full_sixteen_hole_proved':False,'full_P6_proved':False}
target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'manifest_sha256':sha(target.name),'local_proof_sha256':sha('SIXTEEN_LOCAL_PROOF.md'),'application_sha256':sha('SIXTEEN_LOCAL_APPLICATION.md'),'files':len(names)},indent=2))
