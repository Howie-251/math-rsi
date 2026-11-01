from pathlib import Path
from collections import defaultdict,Counter
from fractions import Fraction as Q
from time import process_time
import json
P=Path(__file__).resolve().parent;start=process_time();D=json.loads((P/'DOMAIN.json').read_text())['records'];groups=defaultdict(list)
def move(m,p):return sum(1<<p[i] for i in range(9) if m>>i&1)
for i,z in enumerate(D):
 p=z['old_to_canonical'];assert sorted(p)==list(range(9));assert move(sum(1<<i for i in z['low']),p)==z['canonical_lowmask']
 ns={move(int(t),p):n for t,n in z['counts'].items()}
 assert sorted(t for t in ns if t.bit_count()>2)==z['canonical_large']
 groups[(tuple(z['canonical_large']),z['canonical_lowmask'])].append((i,ns))
counts=Counter()
for items in groups.values():
 assert all(ns==items[0][1] for _,ns in items)
 flags=[Q(D[i]['old_bound'])<1 for i,_ in items];counts['old_all_strict' if all(flags) else 'old_some_strict' if any(flags) else 'old_none_strict']+=1
r={'status':'PASS','markings':len(D),'colored_orbits':len(groups),'all_transported_exact_counts_equal':True,**counts,'cpu_seconds':process_time()-start}
(P/'TRANSPORT_RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
