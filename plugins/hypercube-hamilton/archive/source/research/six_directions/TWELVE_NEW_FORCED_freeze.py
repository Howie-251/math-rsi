from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
summary=json.loads((R/'TWELVE_NEW_FORCED_summary.json').read_text())
assert summary['count']==27
names=['TWELVE_NEW_FORCED_PROOF.md','TWELVE_NEW_FORCED_summary.json',
       'TWELVE_NEW_FORCED_prepare.py','TWELVE_NEW_FORCED_freeze.py',
       'A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md','HIGHER_FORCED_CHERRY_REVIEW.json']
for row in summary['reports']:
    names.extend(row['prefix']+s for s in ['_forests.bin','_full_pairs.bin','_pairs.bin','_columns.bin',
        '_matrix.bin','_pivots.bin','_combos.bin','_config.txt','.json'])
manifest={'status':'FROZEN_CANDIDATE_INDEPENDENT_REVIEW_PENDING',
          'files':{n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in names},
          'claimed_indices':[r['index'] for r in summary['reports']],
          'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'TWELVE_NEW_FORCED_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Frozen',len(names),'inputs for27 conditional local claims.')
