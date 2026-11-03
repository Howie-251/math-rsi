"""Exact rowweight certificate check on cached balls; one actual-source R2 binding."""
from pathlib import Path
import json,time
P=Path(__file__).parent;start=time.process_time()
mat=json.loads((P/'radius2_sets.json').read_text());cert=json.loads((P/'INTEGER_ROW_WEIGHTS.json').read_text());profile=json.loads((P.parent/'SOURCE_PROFILE.json').read_text())
n=mat['source_n'];eligible=mat['eligible'];balls=mat['closed_R2'];w=cert['row_weights']
assert n==972 and len(eligible)==len(balls)==108 and len(w)==972
assert eligible==profile['free_vertices'] and len(set(eligible))==108
assert all(type(x)==int and x>=0 for x in w)
assert all(len(b)==len(set(b)) and all(0<=t<n for t in b) for b in balls)
W=sum(w);colweights=[sum(w[t] for t in b) for b in balls];C=max(colweights)
assert W==cert['W_total_target_weight'] and C==cert['C_max_single_ball_weight']
assert colweights==cert['all_108_ball_weights']
assert W>14*C and W>13*C
# Parse the independent header-edge format, not the producer's adjacency-list loader.
lines=(P.parent/'source972.edges').read_text().splitlines();header=tuple(map(int,lines[0].split()));assert header==(972,6264)
adj=[set() for _ in range(n)]
for line in lines[1:]:
 if not line.strip() or line.startswith('#'):continue
 u,v=map(int,line.split());adj[u].add(v);adj[v].add(u)
pin=eligible[0];actual={pin}|adj[pin]
for v in adj[pin]:actual.update(adj[v])
assert pin==5 and len(adj[pin])==12 and sorted(actual)==balls[0]
lower=(W+C-1)//C
r={'status':'EXACT_INTEGER_MATRIX_OBSTRUCTION_CONFIRMED','source_n':n,'target_Delta':13,'target_D':3,'eligible_pins':108,'W':W,'C':C,'W_minus_13C':W-13*C,'W_minus_14C':W-14*C,'ratio_exact':f'{W}/{C}','minimum_pins_strict_lower_bound':lower,'positive_weight_rows':sum(x>0 for x in w),'all_108_column_sums_match':True,'binding_check':{'source':'../source972.edges','pin':pin,'old_degree':len(adj[pin]),'closed_R2_size':len(actual),'matches_cached_column':True},'model_binding':'All eligible labels match actual SOURCE_PROFILE free108. Only first cached sphere independently rebuilt; other spheres reuse producer computation.','source_D3_BFS':0,'new_BFS':0,'cached_balls_recomputed':1,'LP_runs':0,'MIP_runs':0,'new_graphs':0,'ordinary_bad_unordered_pairs':None,'CPU_seconds':time.process_time()-start,'prediction':'SUPPORTED','scope':'Any append of only one new vertex with at most13 neighbors among the108 free source vertices, with source induced graph unchanged; not arbitrary helpers or old-edge additions/deletions.'}
(P/'ANALYSIS_CHECK.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
