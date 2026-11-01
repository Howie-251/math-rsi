"""Seven existing twenty-partition witnesses only: forced outer-group graph.
A witness failing this necessary test does not eliminate its inventory type.
No search over twenty-point arrangements or hypergraphs is performed.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();src=json.loads((P/'GROUP5_EXTERNAL_STAR_REPLAY.json').read_text());cat=json.loads((P/'GROUP5_CATALOGUE.json').read_text());out=[]
for ww in src['remaining_partition_relaxation_witnesses']:
 ident=ww['id'];mu={int(t):c for t,c in cat['representatives'][ident]['counts'].items()};parts=[]
 for z in ww['partition_multiset']:
  parts += [set(z['blocks']) for _ in range(z['multiplicity'])]
 assert len(parts)==20
 single_capacity={t for t,c in mu.items() if t and c==1};edges=[];triples=[];parent=list(range(20))
 def find(a):
  while parent[a]!=a:a=parent[a]
  return a
 for a,b in combinations(range(20),2):
  common=sorted(parts[a]&parts[b]&single_capacity)
  if len(common)>=2:
   parent[find(a)]=find(b);edges.append(dict(vertices=[a,b],common_unique_traces=common))
  if len(common)>=3:triples.append(dict(vertices=[a,b],common_unique_traces=common))
 comps={}
 for v in range(20):comps.setdefault(find(v),[]).append(v)
 comps=sorted(comps.values(),key=lambda c:(-len(c),c));sizes=[len(c) for c in comps]
 bins=[0]*4;assignment=[[] for _ in range(4)]
 def pack(i):
  if i==len(sizes):return bins==[5]*4
  used=set()
  for j in range(4):
   if bins[j] in used or bins[j]+sizes[i]>5:continue
   used.add(bins[j]);bins[j]+=sizes[i];assignment[j].append(i)
   if pack(i+1):return True
   bins[j]-=sizes[i];assignment[j].pop()
  return False
 packing=pack(0) if max(sizes)<=5 else False
 out.append(dict(id=ident,twenty_partitions=[sorted(p) for p in parts],single_capacity_traces=sorted(single_capacity),forced_same_group_edges=edges,impossible_three_shared_unique_blocks=triples,components=comps,component_sizes=sizes,max_component=max(sizes),packable_into_four_groups_of_five=packing,component_packing=assignment if packing else None,witness_passes=not triples and packing))
summary=dict(scope=__doc__,witnesses=7,passes=sum(r['witness_passes'] for r in out),failed_ids=[r['id'] for r in out if not r['witness_passes']],type_elimination_claimed=False,elapsed_seconds=time.perf_counter()-st)
(P/'GROUP5_EXTERNAL_STAR_COMPONENT_PILOT.json').write_text(json.dumps(dict(summary=summary,results=out),indent=2)+'\n');print(json.dumps(summary,indent=2));print([(r['id'],r['component_sizes'],len(r['impossible_three_shared_unique_blocks'])) for r in out])
