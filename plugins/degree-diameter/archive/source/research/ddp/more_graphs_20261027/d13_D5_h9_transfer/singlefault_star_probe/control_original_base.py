"""Exactlyoneoriginal-base R4 control; no construction or othercaseretest."""
from pathlib import Path
from collections import Counter,deque
import json,time,resource

OUT=Path(__file__).resolve().parent
GROUP=OUT.parent
ROOT=OUT.parents[4]
start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
load=lambda p:json.loads(p.read_text())
assert load(OUT/'CONTROL_PREDICTION.json')['frozen_before_originalbase_control']
seq=load(OUT/'continuation/accepted_sequence.json')
case=next(r for r in seq['records'] if not r['guards'])
assert (case['ordinal'],case['prototype'],case['deleted_saturated_pin'])==(38,3962,6216)
assert case['source_n']==51418 and len(case['mandatory_pins'])==10
current=load(ROOT/case['mandatory_R4_file'])
assert current['source_n']==51418 and current['missing_count']==0
pins=case['mandatory_pins'];adj=[]
raw=GROUP/'source51417.adjlist.txt'
with raw.open() as f:
    for line in f:
        if not line.strip() or line.startswith('#'):continue
        row=list(map(int,line.split()));assert row[0]==len(adj);adj.append(row[1:])
assert len(adj)==51417
dist=[-1]*51417;q=deque()
for p in pins:dist[p]=0;q.append(p)
while q:
    u=q.popleft()
    if dist[u]==4:continue
    for v in adj[u]:
        if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
missing=[v for v,d in enumerate(dist) if d<0]
deleted=case['deleted_saturated_pin']
deleted_core_neighbors={x for x in adj[deleted] if x<50554}
proxy=[p for p in pins if {x for x in adj[p] if x<50554}==deleted_core_neighbors]
previous=load(OUT/'MECHANISM.json')['CPU_seconds']
result=dict(status='ONE_ORIGINALBASE_CONTROL_COMPLETE',ordinal=38,prototype=3962,deleted_pin=6216,
    original_source_n=51417,original_source_file=str(raw.relative_to(ROOT)),
    mandatory_pins=pins,original_pin_degrees=[len(adj[p]) for p in pins],
    original_degrees_legal=all(len(adj[p])<13 for p in pins),
    original_R4_missing_count=len(missing),original_R4_missing=missing,
    original_R4_covered=51417-len(missing),
    original_R4_distance_histogram=dict(sorted(Counter(d for d in dist if d>=0).items())),
    current_production_source_n=51418,current_R4_missing_count=0,
    current_R4_evidence=case['mandatory_R4_file'],
    prediction_supported=not missing and all(len(adj[p])<13 for p in pins),
    firstseed_needed_for_this_oldtarget_coverage=bool(missing),
    retained_pins_with_same_core_neighborhood_as_deleted=proxy,
    deleted_core_neighbors=sorted(deleted_core_neighbors),
    local_proxy_neighbors={str(p):adj[p] for p in proxy},
    control_scope_cases=1,other39_originalbase_cases_retested=0,
    old_source_allroot_BFS=0,newgraph_BFS=0,newgraphs=0,
    previous_targeted_analysis_CPU=previous,control_CPU_seconds=time.process_time()-start)
result['combined_mechanism_CPU_seconds']=previous+result['control_CPU_seconds']
assert result['combined_mechanism_CPU_seconds']<1
(OUT/'ORIGINALBASE_CONTROL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
