"""Decode/verify a later supplied SAT model; never invokes a solver itself."""
from pathlib import Path
from collections import deque,Counter
import argparse,json
p=argparse.ArgumentParser();p.add_argument('solution');args=p.parse_args();out=Path(__file__).resolve().parent
text=Path(args.solution).read_text();assert 'UNSATISFIABLE' not in text
values={}
for line in text.splitlines():
 if line.startswith('v '):
  for s in line[2:].split():
   v=int(s)
   if v:values[abs(v)]=v>0
stats=json.loads((out/'MODEL_STATS.json').read_text());assert all(v in values for v in range(1,stats['CNF_variables']+1))
for line in (out/'model.cnf').read_text().splitlines():
 if not line or line[0] in 'cp':continue
 lits=[int(s) for s in line.split() if s!='0'];assert any(values[abs(v)]==(v>0) for v in lits)
inputs=json.loads((out/'INPUT.json').read_text());edges=[]
for e in inputs['potential_edges']:
 lit=e['literal']
 if lit is True or (lit is not False and values[lit]):edges.append((e['u'],e['v']))
assert len(edges)==len(set(edges))==84
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
shifts=[]
for rec in inputs['shift_selectors']:
 selected=[s for s,var in enumerate(rec['selector_ids']) if values[var]];assert len(selected)==1
 shifts.append({'base_edge':rec['base_edge'],'shift':selected[0]})
params={'source_model':'INPUT.json','chord_shifts':shifts,'selected_port_edges':[[e['u'],e['v']] for e in inputs['potential_edges'] if e['literal'] is not True and e['literal'] in inputs['port_variable_ids'] and values[e['literal']]],'n':42,'m':84,'degree':4,'actual_D':3,'allroot_eccentricity_histogram':dict(hist),'acceptance':'PRODUCER_LITERAL_PENDING_PARENT'}
(out/'candidate42.edges').write_text('42 84\n'+''.join(f'{u} {v}\n' for u,v in sorted(edges)))
(out/'CANDIDATE_PARAMETERS.json').write_text(json.dumps(params,indent=2)+'\n');print(json.dumps(params))
