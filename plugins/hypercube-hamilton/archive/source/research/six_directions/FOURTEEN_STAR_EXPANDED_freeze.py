from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
names=['FOURTEEN_STAR_EXPANDED_PROOF.md','FOURTEEN_STAR_EXPANDED_prepare.py','FOURTEEN_STAR_EXPANDED_transport.json','FOURTEEN_STAR_B_EXPAND_profile.json','FOURTEEN_STAR_B_EXPAND_selected.json','FOURTEEN_STAR_B_REDUCED_prepare.py','FOURTEEN_STAR_B_REDUCED_candidate_classes.json','FOURTEEN_STAR_B_REDUCED_summary.json','FOURTEEN_STAR_B_EXPAND_A_prepare.py','FOURTEEN_STAR_B_EXPAND_A_pilot.cpp','FOURTEEN_STAR_B_EXPAND_A_options.json','FOURTEEN_MAXIMAL_A_REVIEW.json','TWELVE_STAR_MAXIMAL_A_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.json','A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md','FOURTEEN_RESIDUAL_STRUCTURE.json','TWELVE_ROOT_STAR_NONADJACENT_OPTIONS.json']
for i in range(5):names.append(f'TWELVE_ROOT_STAR_OPENING_case_{i:02}_forests.bin')
for i in (79,87):
 names += [f'FOURTEEN_STAR_B_EXPAND_A_{s}' for s in (f'full_{i}.json',f'full_{i}_certificates.bin',f'full_{i}_unhit.jsonl',f'count_{i}.py',f'count_{i}.json',f'options_{i}.bin',f'T_{i}.txt')]
for row in json.loads((R/'FOURTEEN_STAR_B_REDUCED_summary.json').read_text())['reports']:
 pre=row['prefix'];names += [pre+s for s in ('.json','_config.txt','_forests.bin','_full_pairs.bin','_pairs.bin','_columns.bin','_matrix.bin','_pivots.bin','_combos.bin')]
 src=row['source_prefix'];names += [src+s for s in ('_columns.bin','_pairs.bin','_matrix.bin')]
for v in (1,7,31):
 names += [f'FOURTEEN_RESIDUAL_STRUCTURE_maxA_remaining_v{v}_covered.bin',f'FOURTEEN_STAR_EXPANDED_remaining_v{v}_covered.bin',f'FOURTEEN_STAR_EXPANDED_positive_v{v}_covered.bin']
files={}
for n in names:
 h=hashlib.sha256()
 with (R/n).open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 files[n]={'sha256':h.hexdigest(),'bytes':(R/n).stat().st_size}
(R/'FOURTEEN_STAR_EXPANDED_MANIFEST.json').write_text(json.dumps({'status':'PRODUCER_ONLY','files':files,'selected_B_classes':10,'A_certificates':574944,'positive_actual_records':120,'covered_remaining':2407,'free_remaining':0,'full_fourteen_hole_proved':False,'full_P6_proved':False},indent=2)+'\n')
print('Frozen',len(files),'files')
