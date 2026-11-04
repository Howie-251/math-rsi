"""Producer conditional fixed-required-edge actual projections, with leaf certificates."""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter,defaultdict
import json,hashlib,struct
R=Path(__file__).resolve().parent
summary=json.loads((R/'FOURTEEN_NEW_TYPES_summary.json').read_text());rows={x['index']:x for x in summary['reports']}
maps=[tuple(sum(((x>>p[d])&1)<<d for d in range(5)) for x in range(32)) for p in permutations(range(5))]
inverse=[tuple(tr.index(x) for x in range(32)) for tr in maps]
def mask(xs):return sum(1<<x for x in set(xs))
probes=[];positive={}
for line in (R/'FOURTEEN_FIXED_EDGE_probe.tsv').read_text().splitlines():
 a=list(map(int,line.split()));i,x,y,rank=a[:4]
 if rank==256:
  item={'candidate':len(probes),'local_index':i,'required_edge':[x,y],'rank':rank,'source_rows':a[4:]};probes.append(item);positive[(i,x,y)]=item
lookup={}
for p in probes:
 g=rows[p['local_index']]['geometry'];edge=p['required_edge']
 for anchor in g['minority'] or g['omitted']:
  for tr in maps:
   key=tuple(mask(tr[x^anchor] for x in g[k]) for k in ['minority','majority','omitted'])+(tuple(sorted(tr[x^anchor] for x in edge)),)
   lookup.setdefault(key,p['candidate'])
# Full geometric normalizations, used only to collect ACTUAL two-fixed-edge tasks.
geolookup=defaultdict(list)
for i,row in rows.items():
 if row['rank']<128:continue
 g=row['geometry']
 for anchor in g['minority'] or g['omitted']:
  for pi,tr in enumerate(maps):
   key=tuple(mask(tr[x^anchor] for x in g[k]) for k in ['minority','majority','omitted']);geolookup[key].append((i,anchor,pi))
main=set()
data=(R/'FOURTEEN_FORCED_witnesses.bin').read_bytes()
for rec in struct.iter_unpack('<BIHBQIIIB4B7x',data):main.add(rec[:2])
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
def peel(rec):
 alive=set(range(64))-{0,*rec};steps=[]
 while True:
  found=None
  for x in sorted(alive):
   ns=[x^(1<<d) for d in range(6) if x^(1<<d) in alive]
   if len(ns)==1:found=(x,ns[0]);break
  if found is None:return steps
  steps.append(found);alive-=set(found)
results=[];selected=[];peelings=[];hist=Counter();hits=Counter();tasks=defaultdict(set);fixedhit=set();extra=set();taskhit=defaultdict(set);single_actual=defaultdict(set);survivor_projections=0
for v in (1,7,31):
 raw=(R/f'FOURTEEN_HALL_remaining_v{v}_covered.bin').read_bytes();safe=0;new=0;double_records=0
 for off in range(0,len(raw),13):
  rec=raw[off:off+13];Z,W=rec[:6],rec[6:];chain=peel(rec);hist[len(chain)]+=1;forced=[tuple(sorted(e)) for e in chain];found=None;recordtasks=set()
  for d in range(6):
   A=lambda x:(x>>d&1)==(v>>d&1)
   za=[x for x in Z if A(x)];wa=[x for x in W if A(x)];s=len(za)+1-len(wa)
   if s>=3:
    if not wa:continue
    pool=za;minor=[x for x in Z if not A(x)];major=[x for x in W if not A(x)]
   elif s<=-3:
    s=-s;pool=[x for x in wa if x!=(1<<d)];minor=[x for x in W if not A(x)];major=[x for x in Z if not A(x)]
   else:continue
   if (len(minor),len(major)+s,s) not in [(3,9,3),(2,10,4),(1,11,5),(0,12,6)]:continue
   for S in combinations(pool,s):
    Y={x^(1<<d) for x in S};surviving=[(step,e) for step,e in enumerate(forced) if all(not A(x) for x in e) and not set(e)&Y]
    if not surviving:continue
    survivor_projections+=len(surviving)
    M=[project(x,d) for x in minor];J=[project(x,d) for x in set(major)|Y];O=[project(x,d) for x in Y];anchor=min(M or O);norm=tuple(mask(x^anchor for x in xs) for xs in [M,J,O])
    for step,e in surviving:
     actual=tuple(sorted(project(x,d) for x in e));key=norm+(tuple(sorted(x^anchor for x in actual)),);pid=lookup.get(key)
     if pid is not None and found is None:found={'v':v,'input_index':off//13,'probe_candidate':pid,'cut':d,'sources':list(S),'actual_M':M,'actual_J':J,'actual_U':O,'actual_required_edge':list(actual),'original_forced_edge':list(e),'leaf_chain_step':step}
     if (v,off//13) not in main:
      for i,ca,pi in geolookup.get(norm,[]):
       if rows[i]['rank']<256 or i==54:continue
       inv=inverse[pi];ee=tuple(sorted(inv[x^anchor]^ca for x in actual));single_actual[(i,*ee)].add((v,off//13))
    if len(surviving)>=2 and (v,off//13) not in main:
     for selected_edges in combinations(surviving,2):
      edges=[tuple(project(x,d)^anchor for x in e) for step,e in selected_edges]
      for i,ca,pi in geolookup.get(norm,[]):
       inv=inverse[pi];canonical=tuple(sorted(tuple(sorted((inv[a]^ca,inv[b]^ca))) for a,b in edges));task=(i,canonical)
       recordtasks.add(task)
  if found:
   selected.append(found);peelings.append({'v':v,'input_index':off//13,'chain':chain});fixedhit.add((v,off//13));hits[found['probe_candidate']]+=1;safe+=1
   if (v,off//13) not in main:extra.add((v,off//13));new+=1
  elif recordtasks:
   double_records+=1
   for task in recordtasks:tasks[task].add((v,off//13))
  results.append(None) if False else None
 results.append({'v':v,'fixed_positive_subset':safe,'net_new_after_forced9':new,'not_single_covered_records_with_double_tasks':double_records})
for task,records in tasks.items():taskhit[task[0]].add(task)
ordered=sorted(tasks)
(R/'FOURTEEN_FIXED_ACTUAL_multi_tasks.txt').write_text(''.join(str(i)+' 2 '+' '.join(str(x) for e in es for x in e)+'\n' for i,es in ordered))
(R/'FOURTEEN_FIXED_ACTUAL_multi_task_profile.json').write_text(json.dumps([{'local_index':i,'edges':es,'records':len(tasks[(i,es)])} for i,es in ordered],indent=2)+'\n')
allprobe={tuple(map(int,l.split()[:3])):int(l.split()[3]) for l in (R/'FOURTEEN_FIXED_EDGE_probe.tsv').read_text().splitlines()}
(R/'FOURTEEN_FIXED_ACTUAL_single_task_profile.json').write_text(json.dumps([{'local_index':i,'edge':[a,b],'actual_records_after_forced9':len(rs),'existing_source_basis_probe_rank':allprobe.get((i,a,b))} for (i,a,b),rs in sorted(single_actual.items())],indent=2)+'\n')
out={'status':'PRODUCER_ACTUAL_SCAN_PENDING_LOCAL_AND_APPLICATION_REVIEW','single_probe_positive_candidates':len(probes),'actual_surviving_B_edge_source_projections':survivor_projections,'actual_non54_single_probe_tasks_after_forced9':len(single_actual),'fixed_required_edge_subset':len(fixedhit),'main_forced9_intersection':len(fixedhit&main),'net_new_after_forced9':len(extra),'remaining_after_forced9_and_single_fixed':3923-len(main|fixedhit),'chosen_probe_counts':dict(hits),'reports':results,'forced_leaf_chain_length_histogram':dict(hist),'double_actual_task_count':len(tasks),'double_task_local_counts':{i:len(x) for i,x in taskhit.items()},'triple_original_forced_edges_found':0,'selected_witnesses':selected,'leaf_chains_for_selected_witnesses':peelings,'probe_candidates':probes,'full_fourteen_hole_proved':False,'full_P6_proved':False}
(R/'FOURTEEN_FIXED_ACTUAL_profile.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['selected_witnesses','leaf_chains_for_selected_witnesses','probe_candidates']},indent=2))
