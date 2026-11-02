from pathlib import Path
import json,random,time,resource,subprocess
P=Path(__file__).resolve().parent;S=P.parent/'mizuno_d4_source';started=time.process_time();wall=time.monotonic()
D=json.loads((S/'construction.json').read_text());F=json.loads((S/'wide_C10_functions.json').read_text());cal=json.loads((S/'wide_C10_capacity.json').read_text());free=F['free_edges'];seed=20261027510
assert free==[1,5,8,10,11,12,13,14,15] and cal['C10_integer_transplant_missing_representative_targets']==44
rng=random.Random(seed);starts=[cal['C10_integer_transplant_free_voltages']]+[[rng.randrange(1,10) if j<2 else rng.randrange(10) for j in range(9)] for _ in range(7)]
with (P/'input.txt').open('w') as f:
 print(64,file=f)
 for row in F['functions']:
  for slot in row:
   print(len(slot),file=f)
   for c in slot:print(*c,file=f)
 print(8,file=f)
 for st in starts:print(*st,file=f)
(P/'starts.json').write_text(json.dumps(dict(seed=seed,starts=starts,proposals_per_start=25000,free_edge_ids=free,criterion='identity OR12 reduced2 OR100 source rank-good reduced4',first_score_reused=44,source_C9_small_calibration_reused=True),indent=2)+'\n')
r0=resource.getrusage(resource.RUSAGE_CHILDREN);subprocess.run(['g++','-O3','-std=c++17',str(P/'search.cpp'),'-o',str(P/'search')],check=True);r1=resource.getrusage(resource.RUSAGE_CHILDREN)
def limits():resource.setrlimit(resource.RLIMIT_CPU,(55,55))
with (P/'search_result.json').open('w') as out:subprocess.run([str(P/'search')],stdin=(P/'input.txt').open(),stdout=out,check=True,preexec_fn=limits)
r2=resource.getrusage(resource.RUSAGE_CHILDREN);result=json.loads((P/'search_result.json').read_text());assert result['first_score']==44
gamma=[0]*16
for e,v in zip(free,result['best']):gamma[e]=v
assert gamma[1] and gamma[5]
inv=D['inverse_labels'];C=[[-1]*4 for _ in range(80)]
for e,r in enumerate(D['base_edges']):
 u,v,t=r['tail'],r['head'],r['label'];z=gamma[e]
 for h in range(10):C[10*u+h][t]=10*v+(h+z)%10;C[10*v+(h+z)%10][inv[t]]=10*u+h
assert all(len(set(row))==4 and u not in row for u,row in enumerate(C))
assert all(C[v][inv[t]]==u for u,row in enumerate(C) for t,v in enumerate(row))
edges=[(u,v) for u,row in enumerate(C) for v in row if u<v];assert len(edges)==160 and len(set(edges))==160
(P/'best80.edges').write_text('80 160\n'+''.join(f'{u} {v}\n' for u,v in edges))
(P/'best80.labels.json').write_text(json.dumps(dict(n=80,inverse=inv,out=C,vertex_encoding='10*base+cyclic_state',full_voltage=gamma,free_edge_ids=free,base_edges=D['base_edges']),separators=(',',':'))+'\n')
if result['best_score']==0:
 words=[[]]+F['reduced2_words']+F['good4_words'];witness=[]
 for root in range(8):
  targets={}
  for word in words:
   u=10*root
   for t in word:u=C[u][t]
   targets.setdefault(u,word)
  assert len(targets)==80
  for u,word in sorted(targets.items()):witness.append(dict(source=10*root,target=u,word=word,kind='identity_balanced_cover' if not word else 'reduced2_pencil' if len(word)==2 else 'rank_good4'))
 assert len(witness)==640
 (P/'route_witnesses640.json').write_text(json.dumps(dict(orbit_representative_pairs=640,all_ordered_pairs_after_translation=6400,translation_rule='Add k modulo10 to both controller cyclic states, preserving base and all labels.',witnesses=witness),separators=(',',':'))+'\n')
result.update(method='Unrestricted nine-free-voltage source8-base C10 first finite profile',seed=seed,workers=1,controller_vertices=80,controller_edges=160,controller_degree=4,criterion='identity OR reduced2 OR100 source rank-good reduced4',free_edge_ids=free,best_full_voltage=gamma,missing_representative_targets=result['best_score'],missing_ordered_controller_pairs=10*result['best_score'],saved_record_order=5832,would_be_lift_order_if_hit=6480,would_be_degree=12,search_process_CPU_hard_limit_seconds=55,search_internal_stop_seconds=54,compile_CPU_seconds=r1.ru_utime+r1.ru_stime-r0.ru_utime-r0.ru_stime,search_process_CPU_seconds=r2.ru_utime+r2.ru_stime-r1.ru_utime-r1.ru_stime,python_CPU_seconds=time.process_time()-started,wall_seconds=time.monotonic()-wall,root_unique_final_check_pending=True,controller_BFS_performed=False,large6480_graph_generated=False,extra_seeds_filters_sheets_bases=False)
result['total_CPU_seconds']=result['compile_CPU_seconds']+result['search_process_CPU_seconds']+result['python_CPU_seconds'];(P/'terminal.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='best_masks'},indent=2))
