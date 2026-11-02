import resource
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
import json,time
from pathlib import Path
out=Path(__file__).resolve().parent;started=time.process_time()
steps=[1,22,12,85,92,71,81,8];inv=[4,5,6,7,0,1,2,3]
assert all((steps[k]+steps[inv[k]])%93==0 for k in range(8))
dp=[[0]*9 for _ in range(93)];dp[0][8]=1
raw=[0]*93;raw[0]=1;depthcounts=[1];endpoints_by_depth=[[1]+[0]*92]
for depth in range(1,10):
 nxt=[[0]*9 for _ in range(93)]
 for phase,row in enumerate(dp):
  for last,number in enumerate(row):
   if not number:continue
   for d,step in enumerate(steps):
    if last!=8 and d==inv[last]:continue
    nxt[(phase+step)%93][d]+=number
 dp=nxt;counts=[sum(row) for row in dp]
 assert sum(counts)==8*7**(depth-1)
 depthcounts.append(sum(counts));endpoints_by_depth.append(counts);raw=[a+b for a,b in zip(raw,counts)]
exact=1+8*sum(7**i for i in range(9));assert exact==53804809 and sum(raw)==exact
mn=min(raw);hist={}
for count in raw:hist[str(count)]=hist.get(str(count),0)+1
r={'status':'RAW_PHASE_CAPACITY_PASSES' if mn>=49663 else 'RAW_PHASE_CAPACITY_OBSTRUCTION','minimum_raw_count':mn,'maximum_raw_count':max(raw),'first_minimum_phase':raw.index(mn),'all_minimum_phases':[i for i,n in enumerate(raw) if n==mn],'phase_raw_counts':raw,'raw_count_histogram':dict(sorted(hist.items(),key=lambda z:int(z[0]))),'counts_by_word_length':depthcounts,'endpoint_counts_by_word_length':endpoints_by_depth,'last_state_counts_at_depth9':dp,'last_state_definition':{'positive_dart_indices':[0,1,2,3],'inverse_dart_indices':[4,5,6,7],'dart_phases':steps,'inverse_indices':inv,'none_index':8,'none_state':'Only empty word at phase0.'},'prefix_count':exact,'target_prime':49663,'prediction_supported':mn>=49663,'field_coverage_proved':False,'worker_CPU_seconds_before_serialization':time.process_time()-started,'worker_CPU_hard_limit_seconds':3,'field_endpoint_evaluations':0,'parameter_embeddings_tested':0,'word_lists':0,'graphs':0,'BFS':0,'actual_D':None,'ordinary_bad_unordered_pairs':None,'scope':'One phase-only rawword diagnostic on the boundM93 source; notfieldcoverage and notanextra per-BFSapproval procedure.'}
(out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['status','minimum_raw_count','first_minimum_phase','maximum_raw_count','prefix_count']}),flush=True)
