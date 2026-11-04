from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
names=['FOURTEEN_MID_SELECTED_PROOF.md','FOURTEEN_MID_SELECTED_prepare.py','FOURTEEN_MID_SELECTED_profile.py','FOURTEEN_MID_SELECTED_candidate_classes.json','FOURTEEN_MID_SELECTED_coverage.json','FOURTEEN_MID_SELECTED_witnesses.bin','FOURTEEN_MID_SELECTED_all_hit_sets.json','FOURTEEN_MID_REDUCED_prepare.py','FOURTEEN_MID_REDUCED_candidate_classes.json','FOURTEEN_MID_REDUCED_summary.json','FOURTEEN_MID_TYPES_profile.json','FOURTEEN_STAR_B_GLOBAL35_MANIFEST.json','HIGHER_HOLE_UNIFIED_TRANSFER_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.json','Q5_HIGHER_HOLE_REDUCTION_REVIEW.json','A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md']
for row in json.loads((R/'FOURTEEN_MID_REDUCED_summary.json').read_text())['reports']:
 pre=row['prefix'];names += [pre+s for s in ('.json','_config.txt','_forests.bin','_pairs.bin','_columns.bin','_matrix.bin','_pivots.bin','_combos.bin')]
 if row['forced_pairs']:names += [pre+'_full_pairs.bin']+[row['source_prefix']+s for s in ('_columns.bin','_pairs.bin','_matrix.bin')]
for v in (1,7,31):names += [f'FOURTEEN_STAR_B_GLOBAL35_remaining_v{v}_covered.bin',f'FOURTEEN_MID_SELECTED_remaining_v{v}_covered.bin']
files={}
for n in names:
 h=hashlib.sha256()
 with (R/n).open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 files[n]={'sha256':h.hexdigest(),'bytes':(R/n).stat().st_size}
(R/'FOURTEEN_MID_SELECTED_MANIFEST.json').write_text(json.dumps({'status':'PRODUCER_ONLY','files':files,'selected_local_inputs':3,'input':2287,'positive':2262,'remaining_covered':25,'remaining_free':0,'full_fourteen_hole_proved':False,'full_P6_proved':False},indent=2)+'\n')
print('Frozen',len(files),'files')
