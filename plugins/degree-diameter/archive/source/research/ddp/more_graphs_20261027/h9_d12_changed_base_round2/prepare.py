"""Freeze actual last-evaluation/currentdegree scope, then parameterize the producer."""
from pathlib import Path
import json

OUT=Path(__file__).resolve().parent
BASE=OUT.parent
ROOT=OUT.parents[3]
load=lambda p:json.loads(p.read_text())
plan=load(OUT/'PREDICTION.json');assert plan['frozen_before_extension_batch']
allpool=load(BASE/'h9_global_line_pool_d12/pool.json')['records']
ten=[(i,r) for i,r in enumerate(allpool) if len(r['pins'])==10]
assert len(ten)==596
history={};used={}
def add(pins,source_n,status,where,accepted=False):
 key=tuple(pins)
 history.setdefault(key,[]).append(dict(source_n=source_n,status=status,source=where))
 if accepted:used[key]=used.get(key,0)+1
old=ROOT/'research/ddp/global_coverage_20261027'
first=load(old/'quadric_anchor_completion/first_success.json')
add(first['mandatory_pins'],42342,'ACCEPTED','quadric_anchor_completion/first_success.json',True)
for r in load(BASE/'h9_d12_followups/RESULT.json')['rows']:
 add(r['mandatory_pins'],r['source_n'],r['status'],'h9_d12_followups/RESULT.json',bool(r.get('new_vertex') is not None))
for name in ['h9_d12_global_extensions','h9_d12_global_remainder']:
 for r in load(BASE/name/'RESULT.json')['rows']:
  add(r['mandatory_pins'],r['source_n'],r['status'],name+'/RESULT.json',bool(r.get('new_vertex') is not None))
source=BASE/'h9_d12_global_remainder/graphs/graph_d12_D5_n42391.edges'
with source.open() as stream:
 n,m=map(int,stream.readline().split());degree=[0]*n
 for line in stream:
  u,v=map(int,line.split());degree[u]+=1;degree[v]+=1
assert (n,m)==(42391,245805)
same=[];blocked=[];frozen=[]
for i,r in sorted(ten,key=lambda x:tuple(x[1]['pins'])):
 key=tuple(r['pins']);assert key in history
 last=history[key][-1]
 if last['source_n']>=n:same.append(i);continue
 bad=[v for v in key if degree[v]>=12]
 if bad:blocked.append(dict(pool_index=i,blocked_pins=bad,last_evaluation=last));continue
 frozen.append(dict(pool_index=i,pins=list(key),mandatory_current_degrees=[degree[v] for v in key],
                    last_evaluation=last,prior_accepted_line_vertices=used.get(key,0),
                    multiple_line_vertex_candidate=used.get(key,0)>0))
summary=dict(source_n=n,source_m=m,universe=596,samebase_skipped=len(same),samebase_indices=same,
             olderbase_currentdegree_skipped=len(blocked),frozen_candidates=len(frozen),
             multiple_line_vertex_candidates=sum(r['multiple_line_vertex_candidate'] for r in frozen),
             frozen_pool_indices=[r['pool_index'] for r in frozen],
             coverage_checks_performed=0)
(OUT/'frozen_items.json').write_text(json.dumps(frozen,indent=2)+'\n')
(OUT/'freeze_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
(OUT/'degree_skips.json').write_text(json.dumps(blocked,indent=2)+'\n')

text=(BASE/'h9_d12_global_remainder/batch.py').read_text()
def replace(a,b):
 global text
 assert a in text,a
 text=text.replace(a,b)
replace("source=OUT.parent/'h9_d12_global_extensions/graphs/graph_d12_D5_n42377.edges'",
        "source=OUT.parent/'h9_d12_global_remainder/graphs/graph_d12_D5_n42391.edges'")
replace('assert initial_n==42377 and initial_m==245637','assert initial_n==42391 and initial_m==245805')
start=text.index('allpool=json.loads(');end=text.index('rows=[];accepted=[];',start)
text=text[:start]+'''allpool=json.loads((OUT.parent/'h9_global_line_pool_d12/pool.json').read_text())['records']
frozen=json.loads((OUT/'frozen_items.json').read_text())
items=[(r['pool_index'],allpool[r['pool_index']]) for r in frozen]
frozen_by_index={r['pool_index']:r for r in frozen}
assert all(item['pins']==frozen_by_index[i]['pins'] for i,item in items)
'''+text[end:]
replace('enumerate(items,start=367):','enumerate(items):')
replace("blocked=[v for v in pins if len(adj[v])>=12]",
"row['last_evaluation']=frozen_by_index[pool_index]['last_evaluation']\n row['prior_accepted_line_vertices']=frozen_by_index[pool_index]['prior_accepted_line_vertices']\n row['multiple_line_vertex']=frozen_by_index[pool_index]['multiple_line_vertex_candidate']\n blocked=[v for v in pins if len(adj[v])>=12]")
replace("'N12_REMAINING225_ON_VERIFIED42377'","'N12_CHANGED_BASE_ROUND2_ON_42391'")
replace("'ALL225_ITEMS_TERMINAL'","'ALL_FROZEN_ITEMS_TERMINAL'")
replace('scope_items=225','scope_items=len(items)')
replace('items_unattempted=225-len(rows)','items_unattempted=len(items)-len(rows)')
text=text.replace('root_final_independent_acceptance_pending=True','root_final_independent_acceptance_pending=False')
text=text.replace("'COMPLETE_EXTENSION_FOUND_PENDING_ROOT_FINAL'","'ACCEPTED_ACTUAL_DEGREE_COMPLETE_R4'")
(OUT/'batch.py').write_text(text)
print(json.dumps(summary,indent=2))
