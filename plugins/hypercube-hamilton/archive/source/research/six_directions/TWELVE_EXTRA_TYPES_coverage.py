"""Producer actual positive-orbit sets, complete hit witnesses, and greedy sufficient registry."""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter,defaultdict
import json,struct,hashlib
P=Path(__file__).resolve().parent
profile=json.loads((P/'TWELVE_EXTRA_TYPES_profile.json').read_text())
summary=json.loads((P/'TWELVE_EXTRA_TYPES_summary.json').read_text())
assert summary['completed']==summary['requested']==summary['total_geometries']==308,'Wait for all308 producer runs'
geometries={r['index']:r for r in profile['rows']};positive={}
for r in summary['reports']:
 g=geometries[r['index']]
 assert all(tuple(r['geometry'][name])==tuple(g[name]) for name in ('minority','majority','omitted'))
 if r['full_rank']:
  assert r['rank']==1<<((32-len(g['minority'])-len(g['majority']))//2-1)
  positive[r['index']]=g
PERM=[tuple(sum(((x>>p[i])&1)<<i for i in range(5)) for x in range(32)) for p in permutations(range(5))]
def masks(M,J,U):return sum(1<<x for x in M),sum(1<<x for x in J),sum(1<<x for x in U)
lookup={}
for index,g in positive.items():
 for anchor in (g['minority'] if g['minority'] else g['omitted']):
  for tr in PERM:
   key=masks([tr[x^anchor] for x in g['minority']],[tr[x^anchor] for x in g['majority']],[tr[x^anchor] for x in g['omitted']])
   assert key not in lookup or lookup[key]==index
   lookup[key]=index
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
TYPES={(2,6,2):'T26',(1,5,2):'T15',(1,7,3):'T17',(0,6,3):'T63'}
orbitsets=defaultdict(set);targets=[];sources={};hitbytes=bytearray();recordhits={};input_hashes={};offsets={}
for v in (1,7,31):
 name=f'TWELVE_NEW_FORCED_HALL_union_remaining_v{v}.bin';raw=(P/name).read_bytes()
 assert hashlib.sha256(raw).hexdigest()==profile['input_hashes'][name]
 sources[v]=raw;input_hashes[name]=hashlib.sha256(raw).hexdigest();offsets[v]=len(targets)
 for off in range(0,len(raw),11):
  Z=raw[off:off+5];W=raw[off+5:off+11];rid=len(targets);targets.append(v);seen={}
  for d in range(6):
   za=[x for x in Z if (x>>d&1)==(v>>d&1)];wa=[x for x in W if (x>>d&1)==(v>>d&1)]
   s=len(za)+1-len(wa)
   if s>=2:
    if not wa:continue
    pool=za;minor=[x for x in Z if x not in za];major=[x for x in W if x not in wa]
   elif s<=-2:
    s=-s;pool=[x for x in wa if x!=(1<<d)];minor=[x for x in W if x not in wa];major=[x for x in Z if x not in za]
   else:continue
   typ=TYPES.get((len(minor),len(major)+s,s))
   if typ is None:continue
   for S in combinations(pool,s):
    M=[project(x,d) for x in minor];U=[project(x,d) for x in S];J=[project(x,d) for x in major]+U
    assert len(set(M+J))==len(M)+len(J) and len(set(U))==s
    assert all((x^y).bit_count()!=1 for x in M for y in set(J)-set(U))
    anchor=min(M if M else U);key=masks([x^anchor for x in M],[x^anchor for x in J],[x^anchor for x in U])
    index=lookup.get(key)
    if index is None or index in seen:continue
    assert positive[index]['type']==typ
    seen[index]=(d,sum(1<<x for x in S),*masks(M,J,U))
  if seen:recordhits[rid]=seen
  for index,(d,S,M,J,U) in seen.items():
   orbitsets[index].add(rid)
   hitbytes.extend(struct.pack('<BIHBQIII',v,off//11,index,d,S,M,J,U))
 assert len(raw)%11==0
assert len(targets)==29370
(P/'TWELVE_EXTRA_TYPES_positive_hits.bin').write_bytes(hitbytes)
covered=set().union(*orbitsets.values()) if orbitsets else set();greedy=[];taken=set();todo=set(orbitsets)
while todo:
 index=max(todo,key=lambda j:(len(orbitsets[j]-taken),-j));new=orbitsets[index]-taken
 if not new:break
 greedy.append({'index':index,'newly_covered':len(new),'targets':dict(Counter(targets[rid] for rid in new))})
 taken|=new;todo.remove(index)
assert taken==covered
initial_greedy=[r['index'] for r in greedy]
frequencies=Counter(rid for index in initial_greedy for rid in orbitsets[index])
pruned=list(initial_greedy)
for index in reversed(initial_greedy):
 if all(frequencies[rid]>=2 for rid in orbitsets[index]):
  pruned.remove(index)
  for rid in orbitsets[index]:frequencies[rid]-=1
assert set().union(*(orbitsets[index] for index in pruned))==covered
chosen=pruned;selectedbytes=bytearray();reports=[]
for v in (1,7,31):
 raw=sources[v];kept=bytearray();new=0
 for i in range(len(raw)//11):
  rid=offsets[v]+i
  if rid not in covered:kept.extend(raw[11*i:11*i+11]);continue
  new+=1
  index=next(index for index in chosen if index in recordhits[rid]);d,S,M,J,U=recordhits[rid][index]
  selectedbytes.extend(struct.pack('<BIHBQIII',v,i,index,d,S,M,J,U))
 name=f'TWELVE_EXTRA_TYPES_positive_remaining_v{v}.bin';(P/name).write_bytes(kept)
 reports.append({'v':v,'input':len(raw)//11,'positive_covered':new,'remaining':len(kept)//11,'remaining_file':name,'remaining_sha256':hashlib.sha256(kept).hexdigest()})
(P/'TWELVE_EXTRA_TYPES_selected_witnesses.bin').write_bytes(selectedbytes)
out={'status':'PRODUCER_PENDING_LOCAL_RANK_AND_APPLICATION_REVIEW','input_count':29370,
 'producer_full_rank_indices':sorted(positive),'producer_nonfull_indices':sorted(set(geometries)-positive.keys()),
 'all_positive_covered':len(covered),'remaining':29370-len(covered),'actual_positive_orbits':len(orbitsets),
 'greedy_registry_indices':chosen,'greedy':greedy,'initial_greedy_indices':initial_greedy,'greedy_registry_size':len(chosen),'redundancy_pruned':len(initial_greedy)-len(chosen),
 'orbit_union_sizes':{i:len(orbitsets[i]) for i in sorted(orbitsets)},'all_positive_hit_records':len(hitbytes)//28,
 'hit_record_bytes':28,'selected_witness_records':len(selectedbytes)//28,'reports':reports,
 'input_hashes':input_hashes,'profile_sha256':hashlib.sha256((P/'TWELVE_EXTRA_TYPES_profile.json').read_bytes()).hexdigest(),
 'summary_sha256':hashlib.sha256((P/'TWELVE_EXTRA_TYPES_summary.json').read_bytes()).hexdigest(),
 'full_twelve_hole_proved':False,'full_P6_proved':False}
(P/'TWELVE_EXTRA_TYPES_coverage.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('greedy','orbit_union_sizes','input_hashes')},indent=2))
