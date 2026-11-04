from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
pre='TWELVE_ROOT_STAR_MIXED_probe'
d=json.loads((R/(pre+'.json')).read_text());assert d['rank_GF2']==8128
names=['TWELVE_MIXED_HALF_LAYER_PROOF.md','TWELVE_MIXED_HALF_LAYER_freeze.py',
       'TWELVE_ROOT_STAR_MIXED_probe_prepare.py','TWELVE_ROOT_STAR_MIXED_probe_search.cpp',
       'A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md']
names.extend(pre+s for s in ['_forests.bin','_pairs.bin','_columns.bin','_matrix.bin','_pivots.bin','_combos.bin','_config.txt','.json'])
manifest={'status':'FROZEN_CANDIDATE_INDEPENDENT_REVIEW_PENDING',
          'rank':8128,'ambient_rank':8192,'bad_column_rank':64,
          'files':{n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in names},
          'opening_edge_theorem_proved':False,'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'TWELVE_MIXED_HALF_LAYER_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Frozen exact ordinary mixed classification candidate; opening interface remains OPEN.')
