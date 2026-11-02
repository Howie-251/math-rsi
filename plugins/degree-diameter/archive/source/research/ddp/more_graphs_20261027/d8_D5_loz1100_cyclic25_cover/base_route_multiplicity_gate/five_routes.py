from pathlib import Path
import json,time,resource,collections
resource.setrlimit(resource.RLIMIT_CPU,(3,3));p=Path(__file__).resolve().parent;t0=time.process_time()
p.joinpath('FIVE_ROUTE_PREDICTION.json').write_text(json.dumps({'prediction':'In every one of the125 already fixed metacyclic lifts, at least two of the five reduced source routes to g3=(phase11,normal55=1) coincide in the lifted5fibre, preventing fullD5.','frozen_before_this_specific_fibre_endpoint_evaluation':True,'inherited':'All125fullcandidate failures and source routecount5 are known, but the g3 fibre images were not consulted or saved in those result summaries.'},indent=2)+'\n')
phase=[1,12,11,16,19,8,9,4];inverse=[4,5,6,7,0,1,2,3];normal=[0,33,1,19,0,22,38,26];factors=[pow(2,k,55) for k in phase];words=[]
def walk(j,n,word,last):
 if j==11 and n==1:words.append(word)
 if len(word)==5:return
 for k in range(8):
  if last>=0 and k==inverse[last]:continue
  walk((j+phase[k])%20,(n*factors[k]+normal[k])%55,word+[k],k)
walk(0,0,[],-1);assert len(words)==5
cases=[]
for r in [2,57,112,167,222]:
 for s in range(5):
  for t in range(5):
   norms=[0,33+55*s,1,19+55*t]
   norms += [(-n*pow(r,(-j)%20,275))%275 for j,n in zip(phase[:4],norms[:4])]
   endpoints=[]
   for word in words:
    j=n=0
    for k in word:j,n=(j+phase[k])%20,(n*pow(r,phase[k],275)+norms[k])%275
    assert j==11 and n%55==1
    endpoints.append(n)
   cases.append({'r':r,'s':s,'t':t,'endpoint_normals':endpoints,'deck_ids':[(n-1)//55 for n in endpoints],'distinct_lifts':len(set(endpoints))})
hist=dict(sorted(collections.Counter(c['distinct_lifts'] for c in cases).items()))
result={'status':'COMPLETE_TARGETED_FIVE_ROUTE_COMPARISON','prediction':'SUPPORTED' if all(c['distinct_lifts']<5 for c in cases) else 'REFUTED','source_target':[11,1],'darts':list(zip(phase,normal)),'inverse_darts':inverse,'five_words':words,'word_lengths':[len(w) for w in words],'image_histogram':hist,'fully_covered_cases':[c for c in cases if c['distinct_lifts']==5],'cases':cases,'source_BFS':0,'new_graphs':0,'old_target_BFS_reruns':0,'CPU_seconds':time.process_time()-t0}
p.joinpath('FIVE_ROUTE_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['cases','fully_covered_cases']}));print('fullcoverage_count',len(result['fully_covered_cases']));print('firstcase',cases[0])
