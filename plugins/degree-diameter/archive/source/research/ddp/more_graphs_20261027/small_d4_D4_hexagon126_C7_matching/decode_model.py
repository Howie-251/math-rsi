"""Verify a future SAT model and its literal graph; does not invoke a solver."""
from pathlib import Path
from collections import deque,Counter
import json,argparse
p=argparse.ArgumentParser();p.add_argument('solution');args=p.parse_args();OUT=Path(__file__).resolve().parent;text=Path(args.solution).read_text();assert 'UNSATISFIABLE' not in text;values={}
for line in text.splitlines():
 if line.startswith('v '):
  for s in line[2:].split():
   z=int(s)
   if z:values[abs(z)]=z>0
stats=json.loads((OUT/'MODEL_STATS.json').read_text());assert all(v in values for v in range(1,stats['CNF_variables']+1))
for line in (OUT/'model.cnf').read_text().splitlines():
 if not line or line[0] in 'cp':continue
 lits=[int(x) for x in line.split() if x!='0'];assert any(values[abs(x)]==(x>0) for x in lits)
source=json.loads((OUT/'INPUT.json').read_text());atoms=json.loads((OUT/'MATCHING_SELECTORS.json').read_text())['selectors'];selected=[a for a in atoms if values[a['variable']]];assert len(selected)==9
new=[tuple(e) for a in selected for e in a['actual_edges']];assert len(new)==len(set(new))==63 and len({u for e in new for u in e})==126
edges={tuple(e) for e in source['source_edges']};assert not edges&set(new);edges|=set(new);assert len(edges)==252
adj=[[] for _ in range(126)]
for u,v in edges:assert u!=v;adj[u].append(v);adj[v].append(u)
assert all(len(a)==4 and len(set(a))==4 for a in adj)
# Check newgraphgirth>=6 once, withsimplecycle search only throughlength5.
def shortcycle(root,u,path):
 for v in adj[u]:
  if v==root and len(path)>=3:return path+[root]
  if len(path)<5 and v>root and v not in path:
   bad=shortcycle(root,v,path+[v])
   if bad:return bad
 return None
for r in range(126):assert shortcycle(r,r,[r]) is None
assert {tuple(sorted(((u+18)%126,(v+18)%126))) for u,v in edges}==edges
roots=[]
for root in range(18):
 d=[-1]*126;d[root]=0;q=deque([root])
 while q:
  u=q.popleft()
  if d[u]==4:continue
  for v in adj[u]:
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 assert min(d)==0 and max(d)<=4;roots.append({'root':root,'R4_histogram':[d.count(k) for k in range(5)],'eccentricity':max(d)})
assert max(r['eccentricity'] for r in roots)==4
(OUT/'candidate126.edges').write_text('126 252\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
params={'status':'PRODUCER_SAT_LITERAL_PENDING_PARENT','n':126,'m':252,'degree':4,'D':4,'girth_atleast6_checked':True,'selected_atom_variables':[a['variable'] for a in selected],'selected_atoms':selected,'root_R4_checks':roots,'roots_count':18,'all126_BFS_by_producer':False,'oldedges_preserved':189,'newmatching_edges':63,'C7edgeinvariance_checked':True,'parent_independent_acceptance_pending':True}
(OUT/'CANDIDATE_PARAMETERS.json').write_text(json.dumps(params,indent=2)+'\n');print(json.dumps(params))
