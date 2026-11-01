from pathlib import Path
from collections import Counter,defaultdict
from fractions import Fraction as Q
import json
P=Path(__file__).resolve().parent;D=json.loads((P/'DOMAIN.json').read_text())['records'];G=defaultdict(list)
for i,z in enumerate(D):G[(tuple(z['canonical_large']),z['canonical_lowmask'])].append(i)
candidates=[]
for key,ids in G.items():
 if any(Q(D[i]['old_bound'])<1 for i in ids):continue
 i=min(ids,key=lambda j:(Q(D[j]['old_bound']),j));z=D[i];ns={int(t):n for t,n in z['counts'].items()}
 candidates.append({**z,'domain_record':i,'orbit_records':ids,'orbit_size':len(ids),'type_count':len(ns),'large_size_histogram':[sum(n for t,n in ns.items() if t.bit_count()==k) for k in (2,3,4,5)]})
assert len(candidates)==3004
for rank,z in enumerate(sorted(candidates,key=lambda z:(Q(z['old_bound']),z['domain_record']))):z['old_bound_rank_bin']=min(4,5*rank//len(candidates))
def features(z):return [('private',tuple(z['seven_private_signature'])),('maxblock',z['max_block']),('empty',z['empty']),('oldbin',z['old_bound_rank_bin']),('joint',tuple(z['seven_private_signature']),z['max_block'],z['empty']),('hist',tuple(z['large_size_histogram']))]
chosen=[];seen=Counter();remaining=list(candidates)
# Five dense-type, structurally varied pilots first; remaining35 maximize novelty.
for k in range(40):
 def score(z):
  if k<5:return (len(z['counts'])+int(not seen[('private',tuple(z['seven_private_signature']))]),Q(z['old_bound']),-z['domain_record'])
  return (sum((2 if f[0] in ('private','maxblock','empty','oldbin') else 1)/(1+seen[f]) for f in features(z)),Q(z['old_bound']),-z['domain_record'])
 z=max(remaining,key=score);remaining.remove(z);chosen.append(z)
 for f in features(z):seen[f]+=1
out={'scope':'Forty predetermined genuinely old-uncovered four-low/five-seven colored orbits. First5 have dense type support; no r5 private-block identity imported.','all_uncovered_orbits':3004,'selected':40,'private_signatures':sorted({tuple(z['seven_private_signature']) for z in chosen}),'maxblocks':sorted({z['max_block'] for z in chosen}),'empties':sorted({z['empty'] for z in chosen}),'old_bins':sorted({z['old_bound_rank_bin'] for z in chosen}),'records':chosen}
(P/'SELECTION.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='records'}))
