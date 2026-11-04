from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
names=['FOURTEEN_HALL_PROOF.md','FOURTEEN_HALL_filter.py','FOURTEEN_HALL_summary.json','FOURTEEN_HALL_witnesses.bin','FOURTEEN_CACHED_MANIFEST.json','FOURTEEN_REUSE_MANIFEST.json']
for v in (1,7,31):
 for status in ('covered','free'):
  names += [f'FOURTEEN_CACHED_remaining_h14_v{v}_{status}.bin',f'FOURTEEN_HALL_remaining_v{v}_{status}.bin']
files={n:{'sha256':hashlib.sha256((R/n).read_bytes()).hexdigest(),'bytes':(R/n).stat().st_size} for n in names}
(R/'FOURTEEN_HALL_MANIFEST.json').write_text(json.dumps({'status':'PRODUCER_ONLY','files':files,'input_records':12546,'explicit_exclusions':8623,'remaining_covered':3923,'remaining_free':0,'full_fourteen_hole_proved':False,'full_P6_proved':False},indent=2)+'\n')
print('Frozen',len(files),'files')
