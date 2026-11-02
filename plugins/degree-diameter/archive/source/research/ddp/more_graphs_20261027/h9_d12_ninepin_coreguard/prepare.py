from pathlib import Path
import json,time
OUT=Path(__file__).resolve().parent;BASE=OUT.parent
start=time.process_time();load=lambda p:json.loads(p.read_text())
assert load(OUT/'PREDICTION.json')['frozen_before_checks']
original=load(BASE/'h9_d12_ninepin_saturated_deletion/PREDICTION.json')['rows'];assert len(original)==126
previous={r['pool_index']:r for r in load(BASE/'h9_d12_ninepin_saturated_deletion/RESULT.json')['rows']}
source=BASE/'h9_d12_ninepin_saturated_deletion/graphs/graph_d12_D5_n42397.edges'
with source.open() as f:
 n,m=map(int,f.readline().split());degree=[0]*n
 for line in f:
  u,v=map(int,line.split());degree[u]+=1;degree[v]+=1
assert (n,m)==(42397,245877)
frozen=[];blocked=[];accepted_skip=[]
for item in sorted(original,key=lambda r:(tuple(r['mandatory_pins']),r['pool_index'])):
 if item['pool_index']==43:accepted_skip.append(item['pool_index']);continue
 bad=[v for v in item['mandatory_pins'] if degree[v]>=12]
 if bad:blocked.append(dict(pool_index=item['pool_index'],blocked_pins=bad));continue
 frozen.append(dict(**item,previous_evaluation=previous.get(item['pool_index'])))
summary=dict(source_n=n,source_m=m,original_items=126,accepted_pool_skipped=accepted_skip,
 currentdegree_blocked=len(blocked),frozen_items=len(frozen),
 earlier_limited_items_included=sum(r['previous_evaluation'] is not None for r in frozen),
 prepare_CPU_seconds=time.process_time()-start)
(OUT/'frozen_items.json').write_text(json.dumps(frozen,indent=2)+'\n')
(OUT/'freeze_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'degree_skips.json').write_text(json.dumps(blocked,indent=2)+'\n')
print(json.dumps(summary,indent=2))
