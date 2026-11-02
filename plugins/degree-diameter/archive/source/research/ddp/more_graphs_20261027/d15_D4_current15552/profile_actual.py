from pathlib import Path
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;START=time.process_time()
rows=[]
for line in (P/'source15552.author.adjlist.txt').read_text().splitlines():
 if not line.strip()or line.startswith('#'):continue
 a=list(map(int,line.split()));rows.append(a)
n=len(rows);assert n==15552 and all(a[0]==i for i,a in enumerate(rows))
adj=[set(a[1:])for a in rows]
assert all(len(rows[u])-1==len(adj[u])and u not in adj[u]for u in range(n))
assert all(u in adj[v]for u in range(n)for v in adj[u])
deg=[len(a)for a in adj];free=[u for u,d in enumerate(deg)if d<15]
assert max(deg)<=15
sat=[sum(deg[v]==15 for v in a)for a in adj]
blocks=[]
for b in range(192):
 V=range(81*b,81*(b+1));targetsets={tuple(sorted({v//81 for v in adj[u]if v//81!=b}))for u in V}
 patterns={tuple(sorted(Counter(v//81 for v in adj[u]if v//81!=b).values()))for u in V}
 blocks.append({'block':b,'internal_degree_histogram':dict(Counter(sum(v//81==b for v in adj[u])for u in V)),
 'external_degree_histogram':dict(Counter(sum(v//81!=b for v in adj[u])for u in V)),
 'fixed_external_neighbors':list(next(iter(targetsets)))if len(targetsets)==1 else None,
 'external_targetset_count':len(targetsets),'external_multiplicity_patterns':[list(x)for x in sorted(patterns)],
 'free_vertices':[u for u in V if deg[u]<15]})
profile={'status':'ACTUAL15552_SOURCE_DEGREE_AND81BLOCK_PROFILE_COMPLETE','n':n,'m':sum(deg)//2,
 'degree_histogram':dict(Counter(deg)),'Delta':max(deg),'free_vertices':free,'free_count':len(free),
 'free_slots':sum(15-deg[u]for u in free),'minSatN':min(sat),'saturated_neighbor_histogram':dict(Counter(sat)),
 'zero_fault_prototypes':[u for u,z in enumerate(sat)if z==0],'onefault_prototypes':[u for u,z in enumerate(sat)if z==1],
 'minSatN_prototypes':[u for u,z in enumerate(sat)if z==min(sat)],'blocks':blocks,
 'source_BFS':0,'candidate_graphs':0,'actual_D':None,'reported_D':4,'ordinary_bad_unordered_pairs':None,
 'CPU_seconds':time.process_time()-START}
(P/'SOURCE_PROFILE.json').write_text(json.dumps(profile,indent=2)+'\n')
with(P/'source15552.header.edges').open('w')as f:
 f.write(f'{n} {sum(deg)//2}\n')
 for u,a in enumerate(adj):
  for v in sorted(a):
   if u<v:f.write(f'{u} {v}\n')
print(json.dumps({k:v for k,v in profile.items()if k not in ['blocks','free_vertices','minSatN_prototypes','zero_fault_prototypes','onefault_prototypes']},indent=2))
print('block0',json.dumps(blocks[0]))
print('zero',len(profile['zero_fault_prototypes']),'onefault',len(profile['onefault_prototypes']))
