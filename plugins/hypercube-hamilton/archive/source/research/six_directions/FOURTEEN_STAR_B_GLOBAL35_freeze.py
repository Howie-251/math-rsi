from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
names=['FOURTEEN_STAR_B_GLOBAL35_PROOF.md','FOURTEEN_STAR_B_GLOBAL35_prepare.py','FOURTEEN_STAR_B_GLOBAL35_profile.py','FOURTEEN_STAR_B_GLOBAL35_candidate_classes.json','FOURTEEN_STAR_B_GLOBAL35_coverage.json','FOURTEEN_STAR_B_GLOBAL35_witnesses.bin','FOURTEEN_STAR_EXPANDED_MANIFEST.json','HIGHER_FORCED_CHERRY_REVIEW.json']
for v in (1,7,31):names += [f'FOURTEEN_STAR_EXPANDED_remaining_v{v}_covered.bin',f'FOURTEEN_STAR_B_GLOBAL35_remaining_v{v}_covered.bin']
files={n:{'sha256':hashlib.sha256((R/n).read_bytes()).hexdigest(),'bytes':(R/n).stat().st_size} for n in names}
(R/'FOURTEEN_STAR_B_GLOBAL35_MANIFEST.json').write_text(json.dumps({'status':'PRODUCER_ONLY','files':files,'positive':120,'remaining_covered':2287,'remaining_free':0,'full_fourteen_hole_proved':False,'full_P6_proved':False},indent=2)+'\n')
print('Frozen',len(files),'files')
