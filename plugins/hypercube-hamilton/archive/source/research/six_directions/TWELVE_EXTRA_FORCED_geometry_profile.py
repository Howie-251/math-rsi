"""Target's possible ORIGINAL short-matching neighbors and exact marked hole orbits."""
from pathlib import Path
from itertools import permutations
from collections import Counter
import json,hashlib
P=Path(__file__).resolve().parent
N0={1<<d for d in range(6)}
def analyze(stem):
 cases=[];orb_counts=Counter();inputs={}
 for v in (1,7,31):
  name=f'{stem}_v{v}.bin';raw=(P/name).read_bytes();inputs[name]=hashlib.sha256(raw).hexdigest()
  maps=[tuple(sum(((x>>q[d])&1)<<d for d in range(6)) for x in range(64)) for q in permutations(range(6)) if sum(((v>>q[d])&1)<<d for d in range(6))==v]
  for off in range(0,len(raw),11):
   Z=set(raw[off:off+5]);W=set(raw[off+5:off+11]);available=sorted({v^(1<<d) for d in range(6)}-(Z|{0}))
   assert v not in W and available
   canonical=min((tuple(sorted(t[x] for x in Z)),tuple(sorted(t[x] for x in W))) for t in maps)
   key=(v,*canonical);orb_counts[key]+=1
   cases.append({'v':v,'input_index':off//11,'record':list(raw[off:off+11]),'target_available_M_neighbors':available,'target_M_degree':len(available),'target_original_edge_forced':len(available)==1,'W_equals_root_neighborhood':W==N0,'canonical_key':[v,list(canonical[0]),list(canonical[1])]})
 keys=sorted(orb_counts);index={key:i for i,key in enumerate(keys)};orbits=[]
 for key in keys:
  v,Z,W=key;available=sorted({v^(1<<d) for d in range(6)}-(set(Z)|{0}))
  orbits.append({'index':index[key],'v':v,'canonical_Z':Z,'canonical_W':W,'records':orb_counts[key],'canonical_target_available_M_neighbors':available,'W_equals_root_neighborhood':set(W)==N0})
 for c in cases:c['orbit_index']=index[(c['v'],tuple(c['canonical_key'][1]),tuple(c['canonical_key'][2]))]
 return {'input_count':len(cases),'marked_coordinate_orbits':len(orbits),'target_M_degree_histogram':dict(Counter(c['target_M_degree'] for c in cases)),'W_equals_N0_targets':dict(Counter(c['v'] for c in cases if c['W_equals_root_neighborhood'])),'forced_target_edge_records':sum(c['target_original_edge_forced'] for c in cases),'orbits':orbits,'records':cases,'input_hashes':inputs}
out={'status':'PRODUCER_EXACT_TARGET_NEIGHBOR_AND_MARKED_GEOMETRY_PROFILE','before_safe_forced':analyze('TWELVE_EXTRA_TYPES_positive_remaining'),'after_safe_forced':analyze('TWELVE_EXTRA_FORCED_safe_remaining'),'full_twelve_hole_proved':False,'full_P6_proved':False}
assert out['before_safe_forced']['W_equals_N0_targets']=={7:12,31:285}
(P/'TWELVE_EXTRA_FORCED_geometry_profile.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({name:{k:v for k,v in data.items() if k not in ('orbits','records','input_hashes')} for name,data in out.items() if isinstance(data,dict)},indent=2))
