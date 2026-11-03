import json,time
from pathlib import Path
start=time.process_time()
p=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math/research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/petersen_c14_140_route_gate')
d=json.loads((p/'ALL_NB_WORDS_AND_INTEGER_FORMS.json').read_text())
ws=[w for w in d['words'] if w['root']==0 and w['target']==2]
assert len(ws)==17

def rank(mat, prime):
 a=[[x%prime for x in row] for row in mat]; r=0; piv=[]
 for c in range(6):
  j=next((j for j in range(r,len(a)) if a[j][c]),None)
  if j is None: continue
  a[r],a[j]=a[j],a[r]
  inv=pow(a[r][c],-1,prime);a[r]=[x*inv%prime for x in a[r]]
  for j in range(len(a)):
   if j!=r and a[j][c]:
    q=a[j][c];a[j]=[(x-q*y)%prime for x,y in zip(a[j],a[r])]
  piv.append(c);r+=1
 return r,piv

cases=[]
for omit in range(17):
 rem=[w for i,w in enumerate(ws) if i!=omit];ref=rem[0]
 mat=[[x-y for x,y in zip(w['integer_coefficients'],ref['integer_coefficients'])] for w in rem[1:]]
 ranks={str(q):rank(mat,q)[0] for q in (3,5)}
 cases.append({'omitted_word_id':ws[omit]['word_id'],'reference_word_id':ref['word_id'],'matrix':mat,'ranks':ranks})
supported=all(c['ranks']=={'3':6,'5':6} for c in cases)
result={'status':'ALL_SCALAR_AFFINE_F16_PETERSEN_COVERS_DIAMETER6_IMPOSSIBLE' if supported else 'RANK_PREDICTION_UNSUPPORTED_REQUIRES_ANALYSIS','prediction':'Each of17 possible outlier removals forces six cotree multipliers trivial modulo3 and5','prediction_supported':supported,'base_pair':[0,2],'NB_word_count':len(ws),'NB_word_ids':[w['word_id'] for w in ws],'words_generated_again':0,'fields_constructed':0,'voltage_assignments':0,'graph_BFS_Lean':0,'cases':cases,'new_graph_parameter_Lean_increment':[0,0,0]}
result['actual_process_CPU_seconds']=time.process_time()-start
(p/'AFFINE_F16_RANK_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print({k:v for k,v in result.items() if k!='cases'})
print('rank_cases',[(c['omitted_word_id'],c['ranks']) for c in cases])
