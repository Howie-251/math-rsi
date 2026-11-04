"""Freeze the new producer package; never promotes a claim or creates a review."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
destination=R/'FOURTEEN_FORCED_MANIFEST.json';assert not destination.exists(),'Frozen manifest already exists; do not overwrite.'
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
s=json.loads((R/'FOURTEEN_FORCED_summary.json').read_text());coverage=json.loads((R/'FOURTEEN_FORCED_coverage.json').read_text());source=json.loads((R/'FOURTEEN_HALL_REVIEW.json').read_text());assert source['verdict']=='PASS'
names=['FOURTEEN_FORCED_PROOF.md','FOURTEEN_FORCED_APPLICATION.md','FOURTEEN_FORCED_prepare.py','FOURTEEN_FORCED_profile.py','FOURTEEN_FORCED_author_check.py','FOURTEEN_FORCED_application_author_check.py','FOURTEEN_FORCED_freeze.py','FOURTEEN_FORCED_candidate_classes.json','FOURTEEN_FORCED_summary.json','FOURTEEN_FORCED_coverage.json','FOURTEEN_FORCED_author_check.json','FOURTEEN_FORCED_application_author_check.json','FOURTEEN_FORCED_witnesses.bin','FOURTEEN_NEW_TYPES_profile.json','FOURTEEN_NEW_TYPES_summary.json','FOURTEEN_HALL_REVIEW.json','FOURTEEN_HALL_REVIEW.md','FOURTEEN_HALL_PROOF.md','FOURTEEN_HALL_MANIFEST.json','HIGHER_FORCED_CHERRY_TRANSFER.md','HIGHER_FORCED_CHERRY_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.md','HIGHER_HOLE_UNIFIED_TRANSFER.md','HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json','Q5_A10_FULL_REVIEW.json','A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md','TWELVE_HOLE_FULL_REVIEW.json']
for v in (1,7,31):
 n=f'FOURTEEN_HALL_remaining_v{v}_covered.bin';assert sha(n)==source['audited_input_hashes'][n].removeprefix('sha256:')
 names.extend([n,f'FOURTEEN_FORCED_remaining_v{v}_covered.bin'])
for r in s['reports']:
 suffixes=['_forests.bin','_pairs.bin','_columns.bin','_matrix.bin','_pivots.bin','_combos.bin','_config.txt','.json']
 if r['forced_pairs']:suffixes.append('_full_pairs.bin')
 names.extend(r['prefix']+suffix for suffix in suffixes)
names=list(dict.fromkeys(names))
out={'status':'FROZEN_PRODUCER_PENDING_INDEPENDENT_LOCAL_AND_APPLICATION_REVIEW','local_indices':[r['index'] for r in s['reports']],'double_cherry_indices':[13,14],'single_cherry_indices':[19,20,27,28,29,30],'unconditional_index54':True,'source_Hall_final_PASS':True,'input':3923,'forced_subset':1326,'unconditional54_subset':10,'intersection':0,'union_covered':1336,'remaining':2587,'remaining_by_target':[240,702,1645],'witness_record_bytes':40,'local_forests':2304,'local_connectivity_bits':688128,'actual_multi_cherry_safety_import':'HIGHER_FORCED_CHERRY_TRANSFER Sections5-6: labelled compressedF+R acyclic, automatic j<=floor(c/2)<d','new_root_in_obstruction_route_used':False,'hashes':{n:sha(n) for n in names},'sizes':{n:(R/n).stat().st_size for n in names},'full_fourteen_hole_proved':False,'full_P6_proved':False}
destination.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'manifest_sha256':sha(destination.name),'proof_sha256':sha('FOURTEEN_FORCED_PROOF.md'),'application_sha256':sha('FOURTEEN_FORCED_APPLICATION.md'),'files':len(names)},indent=2))
