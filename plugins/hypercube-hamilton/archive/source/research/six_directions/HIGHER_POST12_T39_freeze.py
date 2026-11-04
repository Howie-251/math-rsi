from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
names=['HIGHER_POST12_T39_PROOF.md','HIGHER_POST12_FORCED_prepare.py','HIGHER_POST12_REUSE_MANIFEST.json','FOURTEEN_FORCED_MANIFEST.json','FOURTEEN_NEW_TYPES_profile.json']
for stem in ('SIXTEEN_POST12','EIGHTEEN_POST12'):
 names += [stem+s for s in ('_FORCED_profile.py','_FORCED_candidate_classes.json','_FORCED_coverage.json','_FORCED_witnesses.bin')]
 for v in (1,7,31):names += [stem+f'_{s}_remaining_v{v}_covered.bin' for s in ('HALL','FORCED')]
files={n:{'sha256':hashlib.sha256((R/n).read_bytes()).hexdigest(),'bytes':(R/n).stat().st_size} for n in names}
(R/'HIGHER_POST12_T39_MANIFEST.json').write_text(json.dumps({'status':'CONDITIONAL_PRODUCER_ONLY','files':files,'sixteen_remaining':1012,'eighteen_remaining_conditional_on_full16':0,'full_sixteen_hole_proved':False,'full_eighteen_hole_proved':False,'full_P6_proved':False},indent=2)+'\n')
print('Frozen',len(files),'files')
