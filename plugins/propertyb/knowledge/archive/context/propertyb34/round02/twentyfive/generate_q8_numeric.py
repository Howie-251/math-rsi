"""Copy all saved q=8 layouts after exact bare-bound replay; no layout search."""
from pathlib import Path
from fractions import Fraction
import json,sys
HERE=Path(__file__).resolve().parent
from generate_q9_numeric import SOURCE,generate
sys.path.insert(0,str(SOURCE));from bare_layout import BareLayout
q8=json.loads((SOURCE/'V25_NINE_Q8_BOUNDS.json').read_text())['results']
tenth=[c for g in json.loads((SOURCE/'V25_Q8_TENTH_BOUNDS.json').read_text())['results'] for c in g['cases']]
for row in q8+tenth:
 b=BareLayout(25,row['positions']).bound({int(t):v for t,v in row['counts'].items()})
 assert b==Fraction(row['bound'])
manifest=[generate('EightLow',q8,9,True),generate('EightLowTenth',tenth,10,True)]
(HERE/'Q8_NUMERIC_BUILD_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
