from pathlib import Path
import json,time
OUT=Path(__file__).resolve().parent;BASE=OUT.parent;START=time.process_time()
load=lambda p:json.loads(p.read_text())
assert load(OUT/'PREDICTION.json')['frozen_before_checks']
history=load(BASE/'h9_baer_plane_extensions/RESULT.json')['rows']
pool=load(BASE/'h9_baer_plane_pool/pool12.json')['records']
source=BASE/'h9_baer_plane_extensions/graphs/graph_d12_D5_n42398.edges'
with source.open() as f:
 n,m=map(int,f.readline().split());degree=[0]*n
 for line in f:
  u,v=map(int,line.split());degree[u]+=1;degree[v]+=1
assert (n,m)==(42398,245889)
early=[r for r in history if r['source_n']<42398]
failures=[r for r in early if r.get('new_vertex') is None]
accepted=[r for r in early if r.get('new_vertex') is not None]
assert len(failures)==52 and len(accepted)==1
frozen=[];blocked=[]
for r in failures+accepted:
 pins=r['mandatory_pins'];bad=[v for v in pins if degree[v]>=12]
 if bad:blocked.append(dict(pool_index=r['pool_index'],blocked_pins=bad,previously_accepted=r.get('new_vertex') is not None));continue
 item=pool[r['oldindex']]
 assert item['pins']==pins
 frozen.append(dict(pool_index=r['pool_index'],oldindex=r['oldindex'],pins=pins,anchor_cap=12-len(pins),
   prior_source_n=r['source_n'],prior_status=r['status'],copy_of_previously_accepted=r.get('new_vertex') is not None))
frozen.sort(key=lambda r:(len(r['pins']),tuple(r['pins']),r['oldindex']))
summary=dict(source_n=n,source_m=m,early_failures=52,early_accepted=1,
 currentdegree_blocked=len(blocked),frozen_items=len(frozen),legal_copy_candidates=sum(r['copy_of_previously_accepted'] for r in frozen),
 same42398_failures_not_retested=True,nonflat34_not_retested=True,nonstable2_not_retested=True,
 prepare_CPU_seconds=time.process_time()-START)
(OUT/'frozen_items.json').write_text(json.dumps(frozen,indent=2)+'\n')
(OUT/'freeze_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'degree_skips.json').write_text(json.dumps(blocked,indent=2)+'\n')
print(json.dumps(summary,indent=2))
