from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
names=['HIGHER_POST12_REUSE_PROOF.md','HIGHER_POST12_REUSE_prepare.py','HIGHER_POST12_HALL_prepare.py','HIGHER_POST12_REUSE_registry.txt','FOURTEEN_REUSE_registry.txt',
 'HIGHER_Q5_FULL_REVIEW.json','FOURTEEN_REUSE_REVIEW.json','FOURTEEN_CACHED_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.json','Q5_HIGHER_HOLE_REDUCTION_REVIEW.json']
names += [f'HIGHER_Q5_FULL_{t}_lookup.txt' for t in ('T26','T15','T17','T63')]
for h,stem in ((16,'SIXTEEN_POST12'),(18,'EIGHTEEN_POST12')):
 names += [stem+x for x in ('_REUSE_scan.cpp','_REUSE_result.json','_HALL_filter.py','_HALL_summary.json','_HALL_witnesses.bin')]
 for v in (1,7,31):
  for status in ('covered','free'):
   tag=f'h{h}_v{v}_{status}.bin'
   names += ['HIGHER_Q5_FULL_residual_'+tag,stem+'_REUSE_remaining_'+tag,stem+'_REUSE_witness_'+tag,stem+f'_HALL_remaining_v{v}_{status}.bin']
files={}
for n in names:
 h=hashlib.sha256()
 with (R/n).open('rb') as f:
  for b in iter(lambda:f.read(8*1024*1024),b''):h.update(b)
 files[n]={'sha256':h.hexdigest(),'bytes':(R/n).stat().st_size}
(R/'HIGHER_POST12_REUSE_MANIFEST.json').write_text(json.dumps({'status':'CONDITIONAL_PRODUCER_ONLY','files':files,'sixteen_covered_remaining':1211,'eighteen_covered_remaining':150,'full_sixteen_hole_proved':False,'full_eighteen_hole_proved':False,'full_P6_proved':False},indent=2)+'\n')
print('Frozen',len(files),'files')
