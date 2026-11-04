from pathlib import Path
from itertools import combinations,product
import json
R=Path(__file__).resolve().parent
g=json.loads((R/'FOURTEEN_NEW_TYPES_profile.json').read_text())['rows'][9]
K=set(range(32))-set(g['minority']+g['majority']);assert {x for x in K if x.bit_count()%2==0}=={23,24,29,30}
tasks=[]
for size in (1,2,3):
 for T in combinations((24,29,30),size):
  for partners in product(*[sorted({x^(1<<d) for d in range(5)}&K-{19,23}) for x in T]):
   if len(set(partners))!=len(partners):continue
   edges=[(19,23),*zip(T,partners)]
   tasks.append('9 '+str(len(edges))+' '+' '.join(str(x) for e in edges for x in e))
(R/'FOURTEEN_FIXED_INTERNAL_tasks.txt').write_text('\n'.join(tasks)+'\n')
print('Tasks',len(tasks))
