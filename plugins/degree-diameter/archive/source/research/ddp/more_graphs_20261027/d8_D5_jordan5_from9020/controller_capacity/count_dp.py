import resource
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
import json,time
from pathlib import Path
out=Path(__file__).resolve().parent;started=time.process_time()
pos=[(1,1),(8,6),(2,7),(8,9)]
darts=pos+[((-pow(2,-j,11)*n)%11,(-j)%20) for n,j in pos]
inv=[4,5,6,7,0,1,2,3]
assert darts[4:]==[(5,19),(4,14),(6,13),(6,11)]
for k,(n,j) in enumerate(darts):
 m,l=darts[inv[k]]
 assert (j+l)%20==0 and (n+pow(2,j,11)*m)%11==0 and (m+pow(2,l,11)*n)%11==0
moves=[]
for state in range(220):
 phase,n=divmod(state,11)
 moves.append([11*((phase+j)%20)+(n+pow(2,phase,11)*m)%11 for m,j in darts])
dp=[[0]*9 for _ in range(220)];dp[0][8]=1
raw=[0]*220;raw[0]=1;bydepth=[[1]+[0]*219];totals=[1]
for depth in range(1,6):
 nxt=[[0]*9 for _ in range(220)]
 for state,row in enumerate(dp):
  for last,number in enumerate(row):
   if not number:continue
   for d in range(8):
    if last!=8 and d==inv[last]:continue
    nxt[moves[state][d]][d]+=number
 dp=nxt;at=[sum(row) for row in dp]
 assert sum(at)==8*7**(depth-1)
 totals.append(sum(at));bydepth.append(at);raw=[a+b for a,b in zip(raw,at)]
assert sum(raw)==1+8*sum(7**i for i in range(5))==22409
mn=min(raw);first=raw.index(mn);hist={}
for count in raw:hist[str(count)]=hist.get(str(count),0)+1
r={'status':'RAW_CAPACITY_PASSES' if mn>=25 else 'RAW_CAPACITY_OBSTRUCTION','minimum_raw_count':mn,'maximum_raw_count':max(raw),'first_minimum_slot':first,'first_minimum_phase':first//11,'first_minimum_normal11':first%11,'all_minimum_slots':[i for i,n in enumerate(raw) if n==mn],'target_module_size':25,'prediction_supported':mn>=25,'raw_counts_phase_slow':raw,'raw_count_histogram':dict(sorted(hist.items(),key=lambda z:int(z[0]))),'counts_by_word_length':totals,'endpoint_counts_by_word_length':bydepth,'last_state_counts_at_depth5':dp,'state_encoding':'11*phase+normal11','last_state_definition':{'dart_indices':list(range(8)),'darts_normal_phase':darts,'inverse_indices':inv,'none_index':8,'none_state':'Only empty prefix at identity.'},'prefix_count':sum(raw),'worker_CPU_seconds_before_serialization':time.process_time()-started,'worker_CPU_hard_limit_seconds':3,'module_endpoint_evaluations':0,'parameter_vectors_tested':0,'word_lists':0,'graphs':0,'BFS':0,'actual_D':None,'ordinary_bad_unordered_pairs':None,'scope':'Only raw words on the fixed eight-dart220projection. Pass is necessary, not a module/fullgraphcoverage certificate.'}
(out/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['status','minimum_raw_count','first_minimum_slot','first_minimum_phase','first_minimum_normal11','prefix_count']}),flush=True)
