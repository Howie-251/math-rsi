from pathlib import Path
import json,time
P=Path(__file__).resolve().parent;started=time.process_time();D=json.loads((P/'construction.json').read_text());W=json.loads((P/'wide_C10_functions.json').read_text());es=D['base_edges'];inv=D['inverse_labels'];words=[[]]+W['reduced2_words']+W['good4_words'];free=[3,7,8,9,10,11];tree=[0,2,4,6,12,13,14];fixed=[0]*16;fixed[1]=fixed[5]=5
adj=[[None]*4 for _ in range(8)]
for e,r in enumerate(es):
 u,v,t=r['tail'],r['head'],r['label'];adj[u][t]=(v,e,1);adj[v][inv[t]]=(u,e,-1)
slots=[]
for root in range(8):
 functions=[set() for _ in range(8)]
 for w in words:
  u=root;c=[0]*6;constant=0
  for t in w:
   u,e,s=adj[u][t];constant=(constant+s*fixed[e])%10
   if e in free:c[free.index(e)]+=s
  functions[u].add((tuple(x%10 for x in c),constant))
 for v in range(8):slots.append(dict(source=root,target=v,functions=[list(c)+[k] for c,k in sorted(functions[v])],symbolic_capacity=len(functions[v]),required10=10))
# Project the source integer voltages to the prescribed internal factor, then gauge its tree.
gamma=[r['voltage']%10 for r in es];gamma[1]=(gamma[0]+5)%10;gamma[5]=(gamma[4]+5)%10;gamma[15]=(gamma[13]+gamma[14]-gamma[12])%10
pot=[None]*8;pot[0]=0
while any(x is None for x in pot):
 for e in tree:
  r=es[e];u,v=r['tail'],r['head']
  if pot[u] is not None and pot[v] is None:pot[v]=(pot[u]+gamma[e])%10
  if pot[v] is not None and pot[u] is None:pot[u]=(pot[v]-gamma[e])%10
gauged=[(gamma[e]+pot[r['tail']]-pot[r['head']])%10 for e,r in enumerate(es)]
assert all(gauged[e]==0 for e in tree) and gauged[1]==gauged[5]==5 and gauged[15]==0
minimum=min(s['symbolic_capacity'] for s in slots)
out=dict(status='C4_WIDE_C10_CAPACITY_ALLOWS_COMPLETE_FINITE_TRIAL' if minimum>=10 else 'C4_WIDE_C10_CAPACITY_OBSTRUCTION',criterion='source identity OR reduced2 OR100 good reduced4; not exactNB4',controller_vertices=80,candidate_order=6480,candidate_degree=12,internal_C4_components=20,tree_edges=tree,fixed_edge_voltages=fixed,free_edge_ids=free,free_variables=6,total_assignments=1000000,minimum_symbolic_capacity=minimum,source_projected_and_gauged_full_voltages=gauged,source_projected_free_voltages=[gauged[e] for e in free],slots=slots,CPU_seconds=time.process_time()-started,search_started=False)
(P/'C4_wide_C10_capacity.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='slots'},indent=2));print('capacities',[[slots[8*u+v]['symbolic_capacity'] for v in range(8)] for u in range(8)])
