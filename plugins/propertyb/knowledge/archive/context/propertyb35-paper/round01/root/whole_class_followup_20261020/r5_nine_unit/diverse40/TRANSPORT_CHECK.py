from pathlib import Path
from collections import defaultdict
from time import process_time
from fractions import Fraction as Q
import json
P=Path(__file__).resolve().parent;start=process_time();D=json.loads((P.parent/'DOMAIN.json').read_text())['records'];groups=defaultdict(list)
def move(mask,p):return sum(1<<p[i] for i in range(9) if mask>>i&1)
for i,z in enumerate(D):
 p=z['old_to_canonical'];assert sorted(p)==list(range(9))
 assert move(sum(1<<i for i in z['low']),p)==z['canonical_lowmask']
 transformed={move(int(t),p):n for t,n in z['counts'].items()}
 assert sorted(t for t in transformed if t.bit_count()>2)==z['canonical_large']
 key=(tuple(z['canonical_large']),z['canonical_lowmask']);groups[key].append((i,transformed))
for ids in groups.values():assert all(d==ids[0][1] for _,d in ids)
partial=[]
for key,ids in groups.items():
 strict=[i for i,_ in ids if Q(D[i]['old_bound'])<1]
 if strict and len(strict)<len(ids):partial.append({'canonical_large':key[0],'canonical_lowmask':key[1],'witness_record':strict[0],'orbit_records':[i for i,_ in ids],'old_witness_bound':D[strict[0]]['old_bound']})
assert len(partial)==55
out={'status':'PASS','records':len(D),'colored_orbits':len(groups),'all_transported_counts_equal_within_orbit':True,'partially_old_strict_orbits':55,'scope':'Label transport of stored old-model witnesses; does not change old corrected bounds into ordinary raw bounds','cpu_seconds':process_time()-start,'partial_orbits':partial}
(P/'TRANSPORT_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='partial_orbits'}))
