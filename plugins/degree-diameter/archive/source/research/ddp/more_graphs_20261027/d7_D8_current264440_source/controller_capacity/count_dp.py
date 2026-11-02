import resource
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
import json,time
from pathlib import Path
out=Path(__file__).resolve().parent;started=time.process_time()
positive=[(1,4),(3,9),(9,6)]
darts=positive+[((-pow(6,-j,11)*n)%11,(-j)%40) for n,j in positive]+[(0,20)]
inv=[3,4,5,0,1,2,6]
for i,(n,j) in enumerate(darts):
 m,k=darts[inv[i]]
 assert (j+k)%40==0 and (n+pow(6,j,11)*m)%11==0 and (m+pow(6,k,11)*n)%11==0
moves=[]
for state in range(440):
 phase,n=divmod(state,11)
 moves.append([11*((phase+j)%40)+(n+pow(6,phase,11)*m)%11 for m,j in darts])
dp=[[0]*8 for _ in range(440)];dp[0][7]=1
raw=[0]*440;raw[0]=1
depthcounts=[1];bydepth=[[1]+[0]*439]
for depth in range(1,9):
 nxt=[[0]*8 for _ in range(440)]
 for state,row in enumerate(dp):
  for last,number in enumerate(row):
   if not number:continue
   for dart in range(7):
    if last!=7 and dart==inv[last]:continue
    nxt[moves[state][dart]][dart]+=number
 dp=nxt;counts=[sum(row) for row in dp]
 assert sum(counts)==7*6**(depth-1)
 depthcounts.append(sum(counts));bydepth.append(counts)
 raw=[a+b for a,b in zip(raw,counts)]
assert sum(raw)==1+7*sum(6**i for i in range(8))==2351462
mn=min(raw);first=raw.index(mn)
hist={}
for count in raw:hist[str(count)]=hist.get(str(count),0)+1
r={'status':'RAW_CAPACITY_PASSES' if mn>=641 else 'RAW_CAPACITY_OBSTRUCTION','minimum_raw_count':mn,'maximum_raw_count':max(raw),'first_minimum_slot':first,'first_minimum_phase':first//11,'first_minimum_normal11':first%11,'all_minimum_slots':[i for i,n in enumerate(raw) if n==mn],'raw_counts_phase_slow':raw,'raw_count_histogram':dict(sorted(hist.items(),key=lambda x:int(x[0]))),'counts_by_word_length':depthcounts,'endpoint_counts_by_word_length':bydepth,'last_state_counts_at_depth8':dp,'state_encoding':'11*phase+normal11','last_state_definition':{'dart_indices':list(range(7)),'darts_normal_phase':darts,'inverse_indices':inv,'none_index':7,'none_state':'Only empty prefix at controller identity usesnone.'},'prefix_count':sum(raw),'target_fiber_size':641,'prediction_supported':mn>=641,'capacity_is_sufficient':False,'worker_CPU_seconds_before_serialization':time.process_time()-started,'worker_CPU_hard_limit_seconds':3,'field_endpoint_evaluations':0,'word_lists':0,'graphs':0,'BFS':0,'actual_D':None,'ordinary_bad_unordered_pairs':None,'scope':'Only raw count on the fixed440state source projection; no field endpoint coverage assertion.'}
(out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['status','minimum_raw_count','first_minimum_slot','first_minimum_phase','first_minimum_normal11','prefix_count']}),flush=True)
