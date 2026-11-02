import resource
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
import json,time
from pathlib import Path
out=Path(__file__).resolve().parent
started=time.process_time()
phases=[1,36,45,48,13,4];inv=[3,4,5,0,1,2]
dp=[[0]*7 for _ in range(49)];dp[0][6]=1
raw=[0]*49;raw[0]=1
counts_by_length=[1]
endpoint_counts_by_length=[[1]+[0]*48]
for depth in range(1,10):
 nxt=[[0]*7 for _ in range(49)]
 for phase,row in enumerate(dp):
  for last,number in enumerate(row):
   if not number:continue
   for dart,step in enumerate(phases):
    if last!=6 and dart==inv[last]:continue
    nxt[(phase+step)%49][dart]+=number
 dp=nxt
 at_depth=[sum(row) for row in dp]
 total=sum(at_depth)
 assert total==6*5**(depth-1)
 counts_by_length.append(total);endpoint_counts_by_length.append(at_depth)
 raw=[a+b for a,b in zip(raw,at_depth)]
exact=1+6*sum(5**i for i in range(9))
assert exact==2929687 and sum(raw)==exact
mn=min(raw);mx=max(raw)
result={'status':'RAW_CAPACITY_PASSES' if mn>=6959 else 'RAW_CAPACITY_OBSTRUCTION','minimum_raw_count':mn,'maximum_raw_count':mx,'first_minimum_phase':raw.index(mn),'all_minimum_phases':[i for i,n in enumerate(raw) if n==mn],'target_fiber_size':6959,'prediction_supported':mn>=6959,'raw_counts_by_phase':raw,'counts_by_length':counts_by_length,'endpoint_counts_by_length':endpoint_counts_by_length,'last_state_counts_at_depth9':dp,'last_state_definition':{'dart_indices':list(range(6)),'dart_phases':phases,'inverse_indices':inv,'none_index':6,'none_state':'Only depth0 at phase0 has count1; no none state after a step'},'empty_prefix_included':True,'exact_prefix_count':exact,'official_count_without_empty':2929686,'arithmetic':'unbounded Python integer counts','CPU_seconds_inside_worker_before_serialization':time.process_time()-started,'worker_CPU_hard_limit_seconds':3,'field_endpoint_evaluations':0,'word_lists':0,'graphs':0,'BFS':0,'parameter_search':0,'actual_D':None,'ordinary_bad_unordered_pairs':None,'scope':'Fixed49phase projection raw named-word capacity. Passing this gate is necessary and not sufficient for complete field coverage.'}
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','minimum_raw_count','first_minimum_phase','maximum_raw_count','exact_prefix_count','counts_by_length','CPU_seconds_inside_worker_before_serialization']}),flush=True)
