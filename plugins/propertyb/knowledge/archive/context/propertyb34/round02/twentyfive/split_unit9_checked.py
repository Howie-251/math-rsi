"""Split only Unit9Checked; preserve all checked Data and Rows modules."""
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent;F=ROOT/'formal/Aris4Math/ThirtyFour'
p=F/'TwentyFiveUnit9Checked.lean';backup=HERE/'TwentyFiveUnit9Checked.before-parent-split.lean'
if not backup.exists():backup.write_text(p.read_text())
s=backup.read_text();names=[]
for i in range(65):
 name=f'TwentyFiveUnit9CheckedParent{i}';names.append(name)
 imports=re.findall(r'^import (Aris4Math\.ThirtyFour\.TwentyFiveUnit9Rows'+str(i)+r'Batch\d+)$',s,re.M)
 start=s.index(f'theorem selected{i} :');end=s.index(f'theorem selected{i+1} :',start) if i<64 else s.index('end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked',start)
 out=''.join('import '+x+'\n' for x in imports)+'''namespace Aris4Math.ThirtyFour.TwentyFiveUnit9Checked
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitRows TwentyFiveUnit9Data
set_option maxRecDepth 100000
set_option maxHeartbeats 0
'''+s[start:end]+'end Aris4Math.ThirtyFour.TwentyFiveUnit9Checked\n'
 (F/f'{name}.lean').write_text(out)
p.write_text(''.join('import Aris4Math.ThirtyFour.'+n+'\n' for n in names)+'''
/-! Parent coverage proofs are checked separately. The final actual caller
performs only a case split on the 65 parents and uses these named theorems. -/
''')
(HERE/'UNIT9_CHECKED_PARENT_BUILD_ORDER.json').write_text(json.dumps(['Aris4Math.ThirtyFour.'+n for n in names]+['Aris4Math.ThirtyFour.TwentyFiveUnit9Checked','Aris4Math.ThirtyFour.TwentyFiveUnit9Actual'],indent=2)+'\n')
q=HERE/'Q9_COMPLETE_BUILD_ORDER.json';d=json.loads(q.read_text());seq=d['targets'];needle='Aris4Math.ThirtyFour.TwentyFiveUnit9Checked';seq=[x for x in seq if 'TwentyFiveUnit9CheckedParent' not in x];i=seq.index(needle);seq[i:i]=['Aris4Math.ThirtyFour.'+n for n in names];d['targets']=seq;q.write_text(json.dumps(d,indent=2)+'\n')
print('65 independent CheckedParent modules; Checked aggregate import-only; Actual unchanged')
