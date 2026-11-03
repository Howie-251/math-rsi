import time
START=time.process_time()
from pathlib import Path
from itertools import product
import json,resource
resource.setrlimit(resource.RLIMIT_CPU,(8,8))
HERE=Path(__file__).resolve().parent
BAR=[1,0,3,2];PRIOR=2.412243086
if(HERE/'ATTEMPT.json').exists():raise RuntimeError('one shot')
(HERE/'ATTEMPT.json').write_text(json.dumps({'status':'STARTED','prior':PRIOR})+'\n')
C=json.loads((HERE.parent/'EXISTING_C30_BINARY_CHART_INPUT.json').read_text())['typed_controller']['controller']
A=[2,1,4];V=[1,2,4,7]
charts={'ORIGINAL_ARC':[A,A,[1,2,7],[1,2,7]],'REPAIRED_ARC':[A,A,[2,1,7],[2,1,7]]}
def apply(cols,x):
 return (cols[0]if x&1 else 0)^(cols[1]if x&2 else 0)^(cols[2]if x&4 else 0)
def end(w):
 u=0
 for p in w:u=C[u][p]
 return u
pairs={t:[list(w)for l in range(4)for w in product(range(4),repeat=l)if end(w)==t]for t in [5,18]}
res={}
for name,M in charts.items():
 for p in range(4):
  assert apply(M[BAR[p]],V[p])==V[BAR[p]]
  assert all(apply(M[BAR[p]],apply(M[p],x))==x for x in range(8))
 def image(w,x):
  out={x}
  for p in w:out={apply(M[p],y)^(V[p]if lam else 0)for y in out for lam in [0,1]}
  return out
 ranks={','.join(map(str,w)):len(image(w,0)).bit_length()-1 for w in product(range(4),repeat=3)if all(w[i+1]!=BAR[w[i]]for i in range(2))}
 res[name]={'matrix_columns':M,'v':V,'inverse_pass':True,'ranks36':ranks,'rank3_count':sum(v==3 for v in ranks.values()),'pair_counts':{str(t):[len(set().union(*(image(w,x)for w in words)))for x in range(8)]for t,words in pairs.items()}}
pred={'unique_pair_word':pairs[5]==[[0,2,1]],'far4_to8':res['ORIGINAL_ARC']['pair_counts']['5']==[4]*8 and res['REPAIRED_ARC']['pair_counts']['5']==[8]*8,'adj_preserved8':all(c['pair_counts']['18']==[8]*8 for c in res.values()),'rank_count24_to28':res['ORIGINAL_ARC']['rank3_count']==24 and res['REPAIRED_ARC']['rank3_count']==28}
improved=[w for w,r in res['ORIGINAL_ARC']['ranks36'].items()if r<res['REPAIRED_ARC']['ranks36'][w]]
broken=[w for w,r in res['ORIGINAL_ARC']['ranks36'].items()if r>res['REPAIRED_ARC']['ranks36'][w]]
result={'status':'COMPLETE_TWO_FIXED_CHART_CONJUGATE_REPAIR_TEST','actual_pair_words':pairs,'charts':res,'predictions':pred,'improved_words':improved,'broken_words':broken,'native_CPU':time.process_time()-START,'prior_CPU':PRIOR,'case_CPU':PRIOR+time.process_time()-START,'case_cap':10,'new_graph_parameter_Lean':[0,0,0],'chartsearch_controllergeneration_BFS_Lean_ARIS':0,'next':'STOP_TWO_CHART_TEST; repairedchart isliteral input for one typedC30to32 insertion mechanism, not a record','terminal':True}
for fn in ['RESULT.json','TERMINAL.json']:(HERE/fn).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'predictions':pred,'improved':improved,'broken':broken,'case_CPU':result['case_CPU']},ensure_ascii=False),flush=True)
