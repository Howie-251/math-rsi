from collections import deque
import json
from pathlib import Path
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
assert (HERE/'P9_PREDICTION.md').exists()
start=time.process_time()
pool=json.loads((HERE.parent/'h9_quadric_line_extension_pool/pool.json').read_text())
source=ROOT/'research/ddp/breadth_20261027_wave4/pencil_source/deg12_diam5_n42342.txt'
adj=[[] for _ in range(42342)]
for line in source.read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):continue
    v,*neighbors=map(int,line.split());adj[v]=neighbors
rows=[]
for i,r in enumerate(pool['records']):
    pins=r['pins']
    assert len(pins)<=12 and len(set(pins))==len(pins)
    assert all(len(adj[a])<12 for a in pins)
    seen=set(pins);q=deque((a,0) for a in pins)
    while q:
        a,d=q.popleft()
        if d==4:continue
        for b in adj[a]:
            if b not in seen:seen.add(b);q.append((b,d+1))
    missing=sorted(set(range(len(adj)))-seen)
    rows.append(dict(candidate=i,pins=pins,missing_vertices=missing,
                     missing_count=len(missing),all_missing_are_extras=all(v>=41356 for v in missing),
                     complete_current_graph_R4=not missing))
result=dict(prediction='P9_SEVEN_DEGREE_FEASIBLE_Q_LINES',
            status='SUPPORTED' if any(r['complete_current_graph_R4'] for r in rows) else 'REFUTED',
            rows=rows,new_multisource_R4_checks=len(rows),new_graphs_generated=0,
            pin_or_anchor_changes=0,full_all_source_BFS=False,
            count_type='new-vertex-to-existing-vertex distance>5; not all-source bad pairs',
            CPU_seconds=time.process_time()-start)
(HERE/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},ensure_ascii=False))
print(json.dumps([dict(candidate=r['candidate'],missing_count=r['missing_count'],all_missing_are_extras=r['all_missing_are_extras']) for r in rows]))
