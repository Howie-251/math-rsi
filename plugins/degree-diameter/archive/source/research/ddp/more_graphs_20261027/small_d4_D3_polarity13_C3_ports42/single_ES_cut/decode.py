"""Check a later supplied SAT solution; no solver invocation."""
from pathlib import Path
from collections import deque,Counter
import json,argparse
p=argparse.ArgumentParser();p.add_argument('solution');args=p.parse_args();out=Path(__file__).resolve().parent
text=Path(args.solution).read_text();assert 'UNSATISFIABLE' not in text;values={}
for line in text.splitlines():
 if line.startswith('v '):
  for word in line[2:].split():
   x=int(word)
   if x:values[abs(x)]=x>0
stats=json.loads((out/'MODEL_STATS.json').read_text());assert all(i in values for i in range(1,stats['CNF_variables']+1))
for line in (out/'model.cnf').read_text().splitlines():
 if not line or line[0] in 'cp':continue
 lits=[int(x) for x in line.split() if x!='0'];assert any(values[abs(x)]==(x>0) for x in lits)
inp=json.loads((out/'INPUT.json').read_text());edges=[]
for rec in inp['potential_edges']:
 v=rec['literal']
 if v is True or(v is not False and values[v]):edges.append((rec['u'],rec['v']))
assert len(edges)==len(set(edges))==84 and tuple(inp['deleted_old_lift_edge']) not in edges
adj=[[] for _ in range(42)]
for u,v in edges:assert u!=v;adj[u].append(v);adj[v].append(u)
assert all(len(a)==4 for a in adj)
hist=Counter()
for root in range(42):
 d=[-1]*42;d[root]=0;q=deque([root])
 while q:
  u=q.popleft()
  for v in adj[u]:
   if d[v]<0:d[v]=d[u]+1;q.append(v)
 assert min(d)==0 and max(d)<=3;hist[max(d)]+=1
assert max(hist)==3
params={'model':'INPUT.json','deleted_old_lift_edge':inp['deleted_old_lift_edge'],'fixed_T_base':inp['leaf_c_absolute_base'],'chord_shifts':[],'selected_port_edges':[],'n':42,'m':84,'degree':4,'actual_D':3,'allroot_eccentricity_histogram':dict(hist),'acceptance':'PRODUCER_LITERAL_PENDING_PARENT'}
for rec in inp['shift_selectors']:
 z=[i for i,v in enumerate(rec['selector_ids']) if values[v]];assert len(z)==1;params['chord_shifts'].append({'base_edge':rec['base_edge'],'shift':z[0]})
for rec in inp['potential_edges']:
 v=rec['literal']
 if v is not True and v in inp['port_variable_ids'] and values[v]:params['selected_port_edges'].append([rec['u'],rec['v']])
(out/'candidate42.edges').write_text('42 84\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
(out/'CANDIDATE_PARAMETERS.json').write_text(json.dumps(params,indent=2)+'\n');print(json.dumps(params))
