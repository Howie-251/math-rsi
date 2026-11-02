import collections,json,os,resource,time
from pathlib import Path
D=Path(__file__).resolve().parent;ROOT=D.parents[3];start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(4,5))
cases=json.load(open(D/'CASES.json'))
s=ROOT/'research/ddp/breadth_20261027_wave4/mizuno_d3_source'
st=json.load(open(s/'controller_structure.json'));C=json.load(open(s/'construction.json'))['controller']
oldNB=st['NB3_counts'];cycleof={v:i for i,c in enumerate(st['external_2factor_cycles']) for v in c}
records=[];counterexamples=[];hist=collections.Counter()
for rec in cases:
 adj=[set() for _ in range(33)]
 for u,v in rec['controller_edges']:adj[u].add(v);adj[v].add(u)
 for i,(v,r) in enumerate(zip(rec['old_triangle'],rec['chosen_external_neighbors'])):
  w=30+i
  two=[[v,x,r] for x in sorted(adj[v]&adj[r])]
  three=[[v,x,y,r] for x in sorted(adj[v]) for y in sorted(adj[x]&adj[r])]
  assert r not in adj[v] and r in C[v] and oldNB[v][r]==0
  item={'candidate_index':rec['candidate_index'],'source_triangle_index':rec['source_triangle_index'],'choice_bits':rec['choice_bits'],'cut_old_pair':[v,r],'designated_new_vertex':w,'source_C5':cycleof[v],'source_external_edge_no_NB3':True,'actual_new_length2_paths':two,'actual_new_length3_paths':three,'length2_count':len(two),'length3_count':len(three),'prediction_match':two==[[v,w,r]] and not three}
  records.append(item);hist[(len(two),len(three))]+=1
  if not item['prediction_match']:counterexamples.append(item)
result={'status':'ALL_240_CUT_PAIR_PREDICTIONS_SUPPORTED' if not counterexamples else 'PREDICTION_REFUTED_BY_COUNTEREXAMPLE','saved_controllers_read':len(cases),'saved_cut_pairs_checked':len(records),'length2_length3_histogram':{f'{a},{b}':n for (a,b),n in hist.items()},'counterexamples':counterexamples,'new_controller_generation':0,'graph_BFS':0,'source_BFS':0,'solver_calls':0,'field_graphs':0,'cpu_seconds':time.process_time()-start,'pid':os.getpid(),'uniform_q_cube_lift_exclusion':not counterexamples}
(D/'CUT_PAIR_COUNTS.json').write_text(json.dumps(records,indent=2)+'\n')
(D/'CUT_PAIR_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
