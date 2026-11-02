from pathlib import Path
import json
import time

started=time.process_time()
here=Path(__file__).resolve().parent
project=here.parents[3]
source=project/'research/ddp/breadth_20261027_wave2/triangle_factor33_controller/best.edges'
rows=[list(map(int,s.split())) for s in source.read_text().splitlines() if s.strip() and not s.startswith('#')]
assert rows[0]==[33,66]
adj=[set() for _ in range(33)]
for u,v in rows[1:]:adj[u].add(v);adj[v].add(u)
assert len(rows[1:])==66 and all(len(a)==4 for a in adj)
missing=[];walks=0;required=0
for u in range(33):
    reachable=set()
    for a in adj[u]:
        for b in adj[a]:
            if b==u:continue
            for c in adj[b]:
                if c==a:continue
                reachable.add(c);walks+=1
    for v in range(33):
        if v==u or v in adj[u]:continue
        required+=1
        if v not in reachable:missing.append([u,v])
result={'status':'PASS_CURRENT_F5_CONTROLLER_GATE' if not missing else 'FAIL_CURRENT_F5_CONTROLLER_GATE',
        'source':str(source.relative_to(project)),'n':33,'m':66,
        'required_nonadjacent_ordered_pairs':required,'nb3_walks_enumerated':walks,
        'missing_nonadjacent_ordered_pairs':len(missing),
        'missing_unordered_pairs':len({tuple(sorted(p)) for p in missing}),
        'missing_pairs':missing,'cpu_seconds':time.process_time()-started,
        'existing_objects_checked':1,'bfs_runs':0,'solver_calls':0,'fiber_graphs_generated':0}
(here/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,separators=(',',':')))
