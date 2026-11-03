#!/usr/bin/env python3
"""One read of saved center profiles; no source/degree/load/packing work."""
import time
START=time.process_time()
import csv,json,resource
from collections import Counter,defaultdict
from pathlib import Path
HERE=Path(__file__).resolve().parent
PRIOR=2.783706889;PREP=.1
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
text=(HERE/'ALL15552_CENTER_BLOCKING_PROFILES.tsv').read_text()
schema='actual_tab'if'\t'in text.splitlines()[0]else'literal_backslash_t'
if schema=='literal_backslash_t':text=text.replace('\\t','\t')
rows=list(csv.DictReader(text.splitlines(),delimiter='\t'))
groups=defaultdict(list);old_role_centers={};unselected_hist=Counter()
for row in rows:
 c=int(row['source_center']);selected=int(row['selected_role_or_minus1'])
 if selected>=0:old_role_centers[selected]=c;continue
 count=int(row['distinct_blocking_clone_owners']);unselected_hist[count]+=1
 if count!=4:continue
 roles=tuple(map(int,row['blocking_old_roles'].split(',')))
 assert len(roles)==len(set(roles))==4 and roles==tuple(sorted(roles))
 groups[roles].append(c)
assert len(rows)==15552 and len(old_role_centers)==864
assert sum(unselected_hist.values())==14688 and min(unselected_hist)==4
assert unselected_hist[4]==342
records=[dict(blocking_old_roles=list(roles),blocking_old_centers=[old_role_centers[r]for r in roles],
 source_centers=sorted(centers),group_size=len(centers))for roles,centers in sorted(groups.items())]
hist=Counter(r['group_size']for r in records);maximum=max(hist)
supported=maximum>=5
actual=time.process_time()-START
result=dict(status='COMPLETE_SAVED_BLOCKER4_GROUP_POSTPROCESS',profile_rows_read_once=len(rows),
 profile_delimiter=schema,source_parses=0,degree_load_recomputations=0,packing_pair_or_candidate_evaluations=0,
 original_unselected_centers=14688,minimum_blocking_owners=4,exactly_four_blocker_centers=342,
 groups=len(records),group_size_histogram=dict(sorted(hist.items())),maximum_group_size=maximum,
 prediction_exists_at_least_five_centers_with_same_four_blockers_supported=supported,
 groups_with_at_least_five_centers=sum(r['group_size']>=5 for r in records),group_records=records,
 paper_k_at_most3_out_kplus1_in='COMPLETE_NO_FROM_MINIMUM_FOUR_DISTINCT_BLOCKERS',
 four_out_five_in=('NECESSARY_GROUP_OPPORTUNITY_ONLY_NOT_TESTED'if supported else'COMPLETE_NO_FROM_GROUP_MAX_BELOW_FIVE'),
 scope='sameaccepted864incumbent,binaryonecloneperoriginalcenter,frozenoriginalN;notglobalmaximumorallnonorbitNO',
 new_source_BFS_field_degree_load_solver_Lean_review_or_graph_runs=0,
 prior_case_CPU_seconds=PRIOR,new_preparation_CPU_seconds=PREP,actual_postprocess_CPU_seconds=actual,
 wholecase_CPU_seconds=PRIOR+PREP+actual,postprocess_CPU_cap_seconds=1,wholecase_CPU_cap_seconds=20,
 terminal=True,active_processes=0,next='STOP no4out5incandidate/pair/local ladder')
(HERE/'BLOCKER4_GROUP_POSTPROCESS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()if k!='group_records'}))
