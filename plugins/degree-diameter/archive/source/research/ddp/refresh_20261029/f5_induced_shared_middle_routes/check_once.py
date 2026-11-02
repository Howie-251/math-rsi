#!/usr/bin/env python3
from array import array
from pathlib import Path
import json
import time

HERE=Path(__file__).resolve().parent
start=time.process_time()
raw=array('H')
with (HERE.parent/'f5_induced_hyperplane3000/source_adjacency.u16.bin').open('rb') as f:
    raw.fromfile(f,3750*20)
adj=[set(raw[20*v:20*v+20]) for v in range(3750)]
w=0
L=[1,2,3,4]
Y=sorted(v for v in adj[w] if v//125==20)
Z=sorted(v for v in adj[w] if v//125==18)
records=[]
for x in L:
    for y in Y:
        direct=y in adj[x]
        paths2=[[x,z,y] for z in sorted(adj[x]&adj[y])]
        paths3=sorted([x,a,b,y] for a in adj[x] for b in adj[y] if b in adj[a])
        expected=sorted([x,z,w,y] for z in Z)
        common=set(paths3[0][1:3]) if paths3 else set()
        for path in paths3:common.intersection_update(path[1:3])
        records.append({'x':x,'y':y,'adjacent':direct,'two_walks':paths2,
            'three_walks':paths3,'three_walk_count':len(paths3),
            'common_internal_vertices':sorted(common),
            'exact_expected_five_routes':not direct and not paths2 and paths3==expected})
result={'status':'COMPLETE_LOCAL_LITERAL_GATE',
    'w':w,'L':L,'Y':Y,'Z':Z,
    'Y_matches_prediction':Y==list(range(2500,2505)),
    'Z_matches_prediction':Z==[2250+5*t for t in range(5)],
    'pairs_checked':len(records),'pairs_with_exact_expected_routes':sum(r['exact_expected_five_routes'] for r in records),
    'all_twenty_predictions_supported':len(records)==20 and all(r['exact_expected_five_routes'] for r in records),
    'old_unique_control_distance3_closure_applies_to_this_control_pair':False,
    'reason_old_closure_does_not_force_w_for_two_point_seed':'controller 0 and20 are adjacent; no retained endpoints in two control fibers at distance3',
    'new_exact_endpoint_condition':'keep(x) AND keep(y) => keep(0) AND OR_{z in Z} keep(z)',
    'cache_reads':1,'BFS_runs':0,'source_edge_text_reads':0,'new_graphs':0,'solver_calls':0,
    'CPU_seconds':time.process_time()-start,'pending':[]}
(HERE/'PAIR_RESULTS.json').write_text(json.dumps(records,indent=2)+'\n')
(HERE/'PATHS_1_2500.json').write_text(json.dumps(next(r for r in records if r['x']==1 and r['y']==2500),indent=2)+'\n')
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
