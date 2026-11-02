"""Frozen410 Baer13-neighborhood production; oldsource validation is inherited."""
import time,resource
initial_child=resource.getrusage(resource.RUSAGE_CHILDREN)
from pathlib import Path
import json,subprocess
from collections import Counter

OUT=Path(__file__).resolve().parent;BASE=OUT.parent;ROOT=OUT.parents[3]
resource.setrlimit(resource.RLIMIT_CPU,(40,40))
load=lambda p:json.loads(p.read_text())
assert load(OUT/'PREDICTION.json')['frozen_before_producer_checks']
pool=load(BASE/'h9_baer_plane_pool/pool12.json');assert (pool['source_n'],pool['source_m'])==(42397,245877)
items=sorted(enumerate(pool['records']),key=lambda x:(len(x[1]['pins']),tuple(x[1]['pins']),x[0]))
assert len(items)==410 and Counter(len(r['pins']) for i,r in items)==Counter({10:12,11:105,12:293})
frozen=[dict(ordinal=j,oldindex=i,pool_index=r['pool_index'],pins=r['pins'],anchor_cap=r['anchor_cap'],raw_point_count=13) for j,(i,r) in enumerate(items)]
(OUT/'frozen_items.json').write_text(json.dumps(frozen,indent=2)+'\n')
NATIVE=BASE/'h9_d12_eightpin_extensions/cover'
source=BASE/'h9_d12_ninepin_saturated_deletion/graphs/graph_d12_D5_n42397.edges'
with source.open() as f:
 initial_n,initial_m=map(int,f.readline().split());adj=[[] for _ in range(initial_n)]
 for line in f:
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
assert (initial_n,initial_m)==(42397,245877)
current_file=source;current_m=initial_m;rows=[];accepted=[];prepare_calls=0;verify_calls=0;selected_calls=0
rootcal=BASE/'h9_baer_plane_pool/first_core_calibration';inherited=load(rootcal/'mandatory.json')
assert items[0][1]['pool_index']==31 and inherited['pins']==items[0][1]['pins']
assert inherited['source_n']==initial_n and not any(v<41356 for v in inherited['missing'])
assert inherited['exact_two_complete'] and not inherited['exact_one_or_two_found']
(OUT/'items').mkdir(exist_ok=True);(OUT/'graphs').mkdir(exist_ok=True)
def cpu():
 c=resource.getrusage(resource.RUSAGE_CHILDREN)
 return time.process_time()+c.ru_utime+c.ru_stime-initial_child.ru_utime-initial_child.ru_stime
def save_sequence():
 (OUT/'accepted_extensions.json').write_text(json.dumps(dict(initial_n=initial_n,initial_m=initial_m,
   final_n=len(adj),final_m=current_m,records=accepted,new_neighbor_type='Baer13 foldedblocking set plus allowedanchors',
   delivery_waits_for_root_first_newmechanism_acceptance=True),indent=2)+'\n')
print('FROZEN '+json.dumps(dict(items=410,pin_counts={'10':12,'11':105,'12':293},first31_root_exactfail_inherited=True,CPU_total=cpu())),flush=True)
status='ALL410_FROZEN_ITEMS_TERMINAL';core_counterexample=None
for ordinal,(oldindex,item) in enumerate(items):
 pins=item['pins'];cap=12-len(pins);assert cap==item['anchor_cap']
 row=dict(ordinal=ordinal,oldindex=oldindex,pool_index=item['pool_index'],source_n=len(adj),source_m=current_m,
          mandatory_pins=pins,anchor_cap=cap,raw_point_count=13,neighbor_type='foldedBaer13blocking set',
          prior_accepted_pool_indices=[r['pool_index'] for r in accepted])
 blocked=[p for p in pins if len(adj[p])>=12]
 if blocked:row.update(status='CURRENT_DEGREE_BLOCKED',blocked_pins=blocked);rows.append(row);continue
 if ordinal==0:
  row.update(status='INHERITED_ROOT_EXACT_CAP2_FAIL',mandatory_R4_missing=inherited['missing_count'],
             core_R4_missing_count=0,extra_R4_missing_count=inherited['missing_count'],
             inherited_root_file=str((rootcal/'mandatory.json').relative_to(ROOT)),root_calibration_CPU_seconds=inherited['CPU_seconds'])
  rows.append(row);continue
 reserve=7.6 if cap else 1.2
 if 40-cpu()<reserve:status='TOTAL_CPU_RESERVE_STOP';break
 prefix=OUT/'items'/f'ord{ordinal:03d}_pool{item["pool_index"]}_n{len(adj)}';pf=Path(str(prefix)+'.pins.txt')
 pf.write_text(' '.join(map(str,pins))+'\n');mode='prepare' if cap else 'verify'
 with Path(str(prefix)+'.log').open('w') as log:
  ret=subprocess.run([str(NATIVE),mode,str(current_file),str(pf),str(prefix)],stdout=log,stderr=log)
 if cap:prepare_calls+=1
 else:verify_calls+=1
 if ret.returncode:
  row.update(status='UNKNOWN_NATIVE_PROCESS_LIMIT',returncode=ret.returncode);rows.append(row);continue
 check=load(Path(str(prefix)+'.json'))
 row.update(mandatory_R4_file=str(Path(str(prefix)+'.json').relative_to(ROOT)),native_CPU_seconds=check['CPU_seconds'])
 if check['status']=='DEGREE_INFEASIBLE':row['status']='CURRENT_DEGREE_BLOCKED_NATIVE';rows.append(row);continue
 missing=check['missing'];coremiss=[v for v in missing if v<41356]
 row.update(mandatory_R4_missing=len(missing),core_R4_missing_count=len(coremiss),extra_R4_missing_count=len(missing)-len(coremiss))
 if coremiss:
  core_counterexample=dict(**row,missing_core_vertices=coremiss,Baer_witness=item['witness'],source_graph=str(current_file.relative_to(ROOT)))
  (OUT/'Pcore_counterexample.json').write_text(json.dumps(core_counterexample,indent=2)+'\n')
  row['status']='PCORE_COUNTEREXAMPLE_STOP';rows.append(row);status='PCORE_COUNTEREXAMPLE_STOP'
  print('PCORE_FAILURE '+json.dumps(dict(pool_index=item['pool_index'],source_n=len(adj),first_core_missing=coremiss[0])),flush=True);break
 anchors=None
 if not missing:anchors=[]
 elif cap==0:row['status']='EXACT_CAP0_EXTRAS_MISSING'
 elif cap==1:
  a=check.get('exact_anchors',[])
  if check.get('exact_one_or_two_found') and len(a)==1:anchors=a
  else:row['status']='EXACT_NO_ONE_ANCHOR'
 else:
  if check.get('exact_one_or_two_found'):anchors=check['exact_anchors']
  else:row['status']='EXACT_NO_AT_MOST_TWO_ANCHORS' if check.get('exact_two_complete') else 'UNKNOWN_NATIVE_EXACT_TWO_LIMIT'
 if anchors is None:rows.append(row);continue
 neighbors=sorted(pins+anchors);assert len(neighbors)==len(set(neighbors))<=12 and all(len(adj[v])<12 for v in neighbors)
 if anchors:
  pf.write_text(' '.join(map(str,neighbors))+'\n');selected=Path(str(prefix)+'_selected')
  ret=subprocess.run([str(NATIVE),'verify',str(current_file),str(pf),str(selected)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
  verify_calls+=1;selected_calls+=1;assert ret.returncode==0
  good=load(Path(str(selected)+'.json'));assert good['missing_count']==0
  selected_file=Path(str(selected)+'.json')
 else:good=check;selected_file=Path(str(prefix)+'.json')
 assert good['covered_count']==len(adj) and max(good['pin_current_degrees'])<12
 row.update(status='ACCEPTED_BAER13_COMPLETE_CURRENT_R4',new_vertex=len(adj),full_neighbor_set=neighbors,
            anchors=anchors,neighbors_old_degrees=good['pin_current_degrees'],new_vertex_degree=len(neighbors),
            new_n=len(adj)+1,new_m=current_m+len(neighbors),actual_current_R4_covered=len(adj),actual_current_R4_missing=0,
            native_selected_R4_file=str(selected_file.relative_to(ROOT)),mandatory_check_reused_for_noanchors=not bool(anchors),
            Baer_witness=item['witness'],witness_multiplicity=item['witness_multiplicity'])
 adj.append(neighbors.copy())
 for v in neighbors:adj[v].append(len(adj)-1)
 current_m+=len(neighbors);current_file=OUT/'graphs'/f'graph_d12_D5_n{len(adj)}.edges'
 with current_file.open('w') as f:
  f.write(f'{len(adj)} {current_m}\n')
  for u,ns in enumerate(adj):
   for v in ns:
    if u<v:f.write(f'{u} {v}\n')
 row['graph_file']=str(current_file.relative_to(ROOT));rows.append(row);accepted.append(row);save_sequence()
 (OUT/f'accepted_{len(accepted):02d}.json').write_text(json.dumps(row,indent=2)+'\n')
 if len(accepted)==1:(OUT/'first_hit.json').write_text(json.dumps(row,indent=2)+'\n')
 print('HIT '+json.dumps(dict(accepted=len(accepted),pool_index=item['pool_index'],n=len(adj),m=current_m,neighbors=neighbors,anchors=anchors,CPU_total=cpu())),flush=True)
 if len(accepted)==32:status='ACCEPTED32_REVIEW_POINT';break
save_sequence()
result=dict(status=status,initial_n=initial_n,initial_m=initial_m,final_n=len(adj),final_m=current_m,
 scope_items=410,rows_visited=len(rows),items_unattempted=410-len(rows),rows=rows,records=accepted,
 accepted_extensions=len(accepted),final_graph=str(current_file.relative_to(ROOT)),
 Pcore_actual_mandatory_checks=sum('core_R4_missing_count' in r for r in rows),
 Pcore_counterexample=core_counterexample is not None,
 inherited_root_firstcase=True,root_firstcase_CPU_seconds_separately=inherited['CPU_seconds'],
 native_prepare_calls=prepare_calls,native_verify_calls=verify_calls,native_extra_selected_checks=selected_calls,
 noanchor_positive_repeated_check=False,CPU_parent_plus_all_children_seconds=cpu(),
 allsource_BFS=0,externalreview=0,Lean=0,MIP=0,
 row_status_counts=dict(Counter(r['status'] for r in rows)),
 mandatory_geometric_scope='Baer13 F3-subgeometries in364 F3-centerflatplanes only',
 pending=['Root firstnewmechanism newroot acceptance beforedelivery append'] if accepted else [],delivery_modified=False)
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k not in ['rows','records']}),flush=True)
