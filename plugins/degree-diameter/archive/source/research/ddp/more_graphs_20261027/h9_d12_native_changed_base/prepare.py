"""Freeze a newactual-base scope without rerunning any distance checks."""
from pathlib import Path
import json
import time

OUT=Path(__file__).resolve().parent;BASE=OUT.parent;ROOT=OUT.parents[3]
start=time.process_time();load=lambda p:json.loads(p.read_text())
assert load(OUT/'PREDICTION.json')['frozen_before_native_checks']
pool=load(BASE/'h9_global_line_pool_d12/pool.json')['records']
ten=[(j,r) for j,r in enumerate(pool) if len(r['pins'])==10];assert len(ten)==596
history={};used={}
def add(pins,n,status,source,accepted=False):
 k=tuple(pins);history[k]=dict(source_n=n,status=status,source=source)
 if accepted:used[k]=used.get(k,0)+1
first=load(ROOT/'research/ddp/global_coverage_20261027/quadric_anchor_completion/first_success.json')
add(first['mandatory_pins'],42342,'ACCEPTED','quadric_anchor_completion/first_success.json',True)
for name in ['h9_d12_followups','h9_d12_global_extensions','h9_d12_global_remainder','h9_d12_changed_base_round2']:
 for r in load(BASE/name/'RESULT.json')['rows']:
  add(r['mandatory_pins'],r['source_n'],r['status'],name+'/RESULT.json',r.get('new_vertex') is not None)
source=BASE/'h9_d12_eightpin_constructive/graphs/graph_d12_D5_n42396.edges'
with source.open() as f:
 n,m=map(int,f.readline().split());degree=[0]*n
 for line in f:
  u,v=map(int,line.split());degree[u]+=1;degree[v]+=1
assert (n,m)==(42396,245865)
same=[];blocked=[];frozen=[]
for j,r in sorted(ten,key=lambda x:tuple(x[1]['pins'])):
 k=tuple(r['pins']);last=history[k]
 if last['source_n']>=n:same.append(j);continue
 bad=[v for v in k if degree[v]>=12]
 if bad:blocked.append(dict(pool_index=j,blocked_pins=bad));continue
 frozen.append(dict(pool_index=j,pins=list(k),last_evaluation=last,
                    prior_accepted_line_vertices=used.get(k,0),mandatory_current_degrees=[degree[v] for v in k]))
summary=dict(source_n=n,source_m=m,universe596=596,samebase_skipped=len(same),
             currentdegree_skipped_after_samebase=len(blocked),frozen_candidates=len(frozen),
             prior_accepted_line_copy_candidates=sum(r['prior_accepted_line_vertices']>0 for r in frozen),
             prepare_CPU_seconds=time.process_time()-start,coverage_checks=0)
(OUT/'frozen_items.json').write_text(json.dumps(frozen,indent=2)+'\n')
(OUT/'freeze_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'degree_skips.json').write_text(json.dumps(blocked,indent=2)+'\n')
print(json.dumps(summary,indent=2))
