from pathlib import Path
import json
R=Path(__file__).resolve().parent
d=json.loads((R/'FOURTEEN_NEW_TYPES_summary.json').read_text())
lines=[]
for row in d['reports']:
 if row['rank']<256 or row['index']==54:continue
 g=row['geometry'];K=set(range(32))-set(g['minority']+g['majority'])
 for a in sorted(K):
  for b in sorted(K):
   if a<b and (a^b).bit_count()==1:lines.append(f'{row["index"]} {a} {b}')
(R/'FOURTEEN_FIXED_EDGE_tasks.txt').write_text('\n'.join(lines)+'\n')
print('Conditional fixed-required-short-edge probes',len(lines))
