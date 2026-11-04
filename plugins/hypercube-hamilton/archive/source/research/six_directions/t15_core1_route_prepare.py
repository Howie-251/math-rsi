from pathlib import Path
import itertools,json
from r4_boundary_blocking_probe import negative_table
R=Path('.')
us=(3,5,9);lines=[]
for f in range(3):
 s,t=[z for z in us if z!=us[f]]
 for L in negative_table(s,t,1):lines.append(str(f)+' '+' '.join(str(z) for e in sorted(L) for z in e))
(R/'t15_core1_route_negative.txt').write_text('\n'.join(lines)+'\n')
d=json.loads((R/'r4_joint_blocking_check.json').read_text())
for c in (4,6,8,10,12):
 row=next(r for r in d['reports'] if r['core']==1 and r['c']==c)
 (R/f't15_core1_route_B{c}.txt').write_text('\n'.join(' '.join(str(z) for e in F for z in e) for F in row['matchings'])+'\n')
print(len(lines))
