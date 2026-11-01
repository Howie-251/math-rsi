"""Filter the frozen cap13 necessary relaxation, not a classification of H."""
from pathlib import Path
from fractions import Fraction
import json
P=Path(__file__).resolve().parent
src=json.loads((P/'RESIDUAL_CAP13.json').read_text())
rows=src['survivors'];assert len(rows)==80
kept=[]
for row in rows:
 n=row['n'];tau=row['tau'];assert sum(n)==595
 assert sum(j*n[j] for j in range(5))==648
 assert sum(j*(j-1)//2*n[j] for j in range(5))==140+tau
 assert Fraction(row['L'])>=2722720
 if n[4]<=8:kept.append(row)
assert len(kept)==25
assert min(r['n'][3] for r in kept)==29
assert min(r['n'][3]+r['n'][4] for r in kept)==37
w=next(r for r in kept if r['n']==[34,519,5,29,8] and r['tau']==0)
assert w['C']==['0','12545','120','377','32'] and w['L']=='2730456'
out={'status':'PASS_FILTER_ONLY','scope':'exact filtering of saved80 cap13 necessary aggregate profiles by proven n4<=8; not H generation or universal feasibility','source':'RESIDUAL_CAP13.json','source_count':80,'count':25,'minimum_n3':29,'minimum_high_pairs':37,'witness':w,'survivors':kept}
(P/'FILTER_N4_8_INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS saved80 ->25;min n3=29,high37;exact witness verified')
