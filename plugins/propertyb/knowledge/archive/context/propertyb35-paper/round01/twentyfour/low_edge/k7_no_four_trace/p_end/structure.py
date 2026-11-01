from pathlib import Path
from collections import Counter,defaultdict
from itertools import combinations,permutations
import json
H=Path(__file__).parent;d=json.loads((H/'EXTENDED_COVERAGE.json').read_text());rs=d['survivors']['ABCDEF'];missing={(0,1),(0,2),(3,4),(5,6)}
def hits(r,s,t,h):
 co=Counter(tuple(e) for e in r['edges']);return [list((i,j)) for i,j in combinations(range(1,7),2) if (i,j) not in missing and sorted((r['degrees'][i],r['degrees'][j]))==sorted((s,t)) and co[i,j]==h]
new={str((s,t,h)):[] for s,t,h in [(3,2,0),(3,2,2),(2,2,1),(2,2,2),(3,1,1),(2,1,1),(1,1,0)]}
coverfamilies=defaultdict(list);topologies=defaultdict(list);samplecells={}
for r in rs:
 cell=str((r['num_degree3'],r['num_degree2']));samplecells.setdefault(cell,r)
 for q in new:
  if hits(r,*eval(q)):new[q].append(r)
 cs=r['two_vertex_covers']
 if cs:
  desc=[]
  for i,j in cs:
   desc.append(('center' if 0 in (i,j) else 'paired',tuple(sorted((r['degrees'][i],r['degrees'][j]),reverse=True)),sum(tuple(e)==(i,j) for e in r['edges'])))
  coverfamilies[str(sorted(desc))].append(r)
 # all-vertex topology is just diagnostic compression, NOT an admissible transport
 canon=min(tuple(sorted(tuple(sorted((p[i],p[j]))) for i,j in r['edges'])) for p in permutations(range(7)))
 topologies[str(canon)].append(r)
out=dict(candidate_new_callers={k:dict(orbits=len(v),labels=sum(r['labelled_count'] for r in v),witness_representative=None if not v else v[0]['edges']) for k,v in new.items()},all_covers_missing_families={k:dict(orbits=len(v),labels=sum(r['labelled_count'] for r in v),representative=v[0]['edges']) for k,v in coverfamilies.items()},abstract_weighted_graph_shapes=len(topologies),abstract_shapes=[dict(edges=eval(k),orbits=len(v),labels=sum(r['labelled_count'] for r in v),representative=v[0]['edges']) for k,v in topologies.items()],cell_examples={k:v['edges'] for k,v in samplecells.items()})
(H/'STRUCTURE.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='abstract_shapes'})
