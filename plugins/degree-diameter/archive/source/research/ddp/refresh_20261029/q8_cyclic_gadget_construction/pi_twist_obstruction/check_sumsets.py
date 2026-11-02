#!/usr/bin/env python3
import itertools,json,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
start=time.process_time()
sets=[(0,)+p for p in itertools.combinations(range(1,8),2)]
def ap_types(A):
 out=[]
 for d in [1,3]:
  if any({s,(s+d)%8,(s+2*d)%8}==set(A) for s in range(8)):out.append(d)
 return out
rows=[];full=[]
for A in sets:
 for B in sets:
  sums=sorted({(a+b)%8 for a in A for b in B})
  row=dict(A=A,B=B,sumset=sums,size=len(sums),full=len(sums)==8,A_AP_step_types=ap_types(A),B_AP_step_types=ap_types(B))
  predicted=(ap_types(A)==[1] and ap_types(B)==[3]) or (ap_types(A)==[3] and ap_types(B)==[1])
  assert row['full']==predicted
  if row['full']:
   assert all((x-y)%8!=4 for S in [A,B] for x in S for y in S)
   full.append(row)
  rows.append(row)
with (HERE/'SUMSET_TABLE.jsonl').open('w') as out:
 for row in rows:out.write(json.dumps(row)+'\n')
result=dict(status='PREDICTED_SUMSET_LEMMA_SUPPORTED_EXACTLY',sets_containing_zero=len(sets),ordered_pairs_checked=len(rows),full_pairs=len(full),odd_step1_sets=[A for A in sets if ap_types(A)==[1]],odd_step3_sets=[A for A in sets if ap_types(A)==[3]],all_full_pairs=full,any_full_set_has_halfturn_difference=False,graphs_generated=0,BFS_runs=0,delta_assignments_enumerated=0,CPU_seconds=time.process_time()-start)
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='all_full_pairs'},indent=2))
