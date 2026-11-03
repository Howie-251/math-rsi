from pathlib import Path
import json,time
OUT=Path(__file__).resolve().parent;BASE=OUT.parent
START=time.process_time();load=lambda p:json.loads(p.read_text())
assert load(OUT/'PREDICTION.json')['frozen_before_checks']
pool=load(BASE/'h9_global_line_pool_d12/pool.json')['records']
source=BASE/'h9_d12_ninepin_saturated_deletion/graphs/graph_d12_D5_n42397.edges'
with source.open() as f:
 n,m=map(int,f.readline().split());degree=[0]*n
 for line in f:
  u,v=map(int,line.split());degree[u]+=1;degree[v]+=1
assert (n,m)==(42397,245877)
raw=[];dedup={}
for j,r in enumerate(pool):
 if len(r['pins'])!=10:continue
 deleted=[v for v in r['pins'] if degree[v]>=12]
 if len(deleted)!=2:continue
 pins=[v for v in r['pins'] if v not in deleted]
 row=dict(pool_index=j,original_tenpins=r['pins'],deleted_saturated_pins=deleted,mandatory_pins=pins)
 raw.append(row);dedup.setdefault(tuple(pins),row)
allitems=[dedup[k] for k in sorted(dedup)];selected=allitems[:32]
(OUT/'frozen_items.json').write_text(json.dumps(selected,indent=2)+'\n')
summary=dict(source_n=n,source_m=m,original_tenpin_universe=596,exactlytwo_saturated_raw=len(raw),
 distinct_eightpin_sets=len(allitems),duplicate_variants=len(raw)-len(allitems),frozen_items=len(selected),
 outside_frozen_unattempted=len(allitems)-len(selected),prepare_CPU_seconds=time.process_time()-START)
(OUT/'freeze_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
