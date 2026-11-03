#!/usr/bin/env python3
import time
START=time.process_time()
import collections,json,resource
from pathlib import Path
HERE=Path(__file__).resolve().parent
PRIOR=37.767076346;PREP=.1;N=16416;OLD=15552;WIDTH=2052
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
interfaces=json.loads((HERE/'ALL_VISITED_CENTER_HELPER_INTERFACES.json').read_text())
schema=json.loads((HERE/'HELPER_BALL_SCHEMA.json').read_text())
assert len(interfaces)==schema['cases_saved']==342 and schema['bytes_per_ball']==WIDTH
counts=collections.Counter({'EVEN_K5_BASE_FAIL':0,'K5_BASE_PASS_BUT_ALL_DEGREE_LEGAL_H_FAIL':0});results=[];examples={}
with(HERE/'ALL_VISITED_CASE_HELPER_B0_B3.bits').open('rb')as f:
 for ci,case in enumerate(interfaces):
  assert case['case_index']==ci and case['helper_ball_byte_offset']==f.tell()
  B=[]
  for h in range(5):
   row=[]
   for r in range(4):
    raw=f.read(WIDTH);assert len(raw)==WIDTH;row.append(int.from_bytes(raw,'little'))
   B.append(row)
  base=((1<<N)-1)^int(case['base_donor_exclusion_mask_hex'],16)
  fail=None;coverage_counts=[]
  for h in range(5):
   cover=B[h][3]
   for g in range(5):
    if g!=h:cover|=B[g][2]
   assert cover&~base==0
   coverage_counts.append(cover.bit_count());missing=base&~cover
   if missing and fail is None:
    target=(missing&-missing).bit_length()-1;legs=[]
    for g in range(5):
     budget=3 if g==h else 2
     oldr=next((r for r in range(4)if B[g][r]>>target&1),None)
     legs.append(dict(last_helper=case['helper_labels'][g],true_K5_helper_cost=0 if g==h else 1,
      allowed_old_leg_radius=budget,old_leg_min_in_B0toB3=oldr,
      total_length_if_known=(0 if g==h else 1)+1+oldr if oldr is not None else None,
      reaches_within4=bool(B[g][budget]>>target&1)))
    fail=dict(first_helper_index=h,first_helper=case['helper_labels'][h],first_target=target,
     target_class='original15552'if target<OLD else'retained_clone',oldleg_route_decomposition=legs)
  category='EVEN_K5_BASE_FAIL'if fail else'K5_BASE_PASS_BUT_ALL_DEGREE_LEGAL_H_FAIL'
  record=dict(case_index=ci,source_center_v=case['source_center_v'],category=category,
   clique_base_pass=fail is None,helperpair_distance_in_K5=1,helper_labels=case['helper_labels'],
   legal_helper_caps=case['helper_capacity'],base_targets=16412,
   allfive_K5_base_cover_sizes=coverage_counts,first_failure=fail)
  counts[category]+=1;results.append(record);examples.setdefault(category,record)
 assert not f.read(1)
first=results[0]
supported=(first['source_center_v']==15 and first['first_failure']is not None and
 first['first_failure']['first_helper']==15560 and first['first_failure']['first_target']==1)
actual=time.process_time()-START
FAILURE_CHARGE=.05
out=dict(status='COMPLETE_SAVED_HELPER_BALL_K5_RELAXATION_POSTPROCESS',case_count=342,
 category_counts=dict(counts),examples=examples,case_results=results,
 first_v15_helper15560_target1_prediction_supported=supported,
 degree_relaxed_complete_K5_not_claimed_legal=True,
 saved_helper_ball_rows_read=342*5*4,source_parses=0,ball_recomputations=0,H_searches=0,
 new_BFS_field_solver_Lean_ARIS_graph_runs=0,
 prior_case_CPU_seconds=PRIOR,new_preparation_CPU_seconds=PREP,actual_postprocess_CPU_seconds=actual,
 failed_preexecution_conservative_CPU_charge_seconds=FAILURE_CHARGE,
 wholecase_CPU_seconds=PRIOR+PREP+FAILURE_CHARGE+actual,wholecase_CPU_cap_seconds=120,postprocess_CPU_cap_seconds=1,
 terminal=True,active_processes=0,next='STOP no sourceguided/split/S5/newsolver')
(HERE/'K5_RELAXATION_POSTPROCESS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in ['case_results','examples']}))
