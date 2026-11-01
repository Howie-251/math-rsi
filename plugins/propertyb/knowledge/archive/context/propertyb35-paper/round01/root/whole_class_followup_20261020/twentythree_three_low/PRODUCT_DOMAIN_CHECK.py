from pathlib import Path
from itertools import product
from collections import Counter
from time import process_time
import json
P=Path(__file__).resolve().parent
start=process_time();answer=[]
for U in (7,8,9):
 slots=[]
 for z in range(3):slots.append([[],[(z,3)],[(z,4)],[(z,3),(z,3)],[(z,3),(z,4)],[(z,4),(z,4)],[(z,3,4)]])
 result=set();candidates=0
 for choices in product(*slots):
  flat=sum(choices,[])
  for m in range(U):
   candidates+=1;tr=tuple(sorted(flat+[(3,4)]*m));inc=Counter(z for e in tr for z in e)
   if inc[3]>U-1 or sum(len(e)-1 for e in tr if 3 in e)>4*U-22:continue
   K=21-U+sum(len(e)-1 for e in tr);w4=sum(len(e)-1 for e in tr if 4 in e)
   low=max(7,1+inc[4],(22+w4+3)//4)
   if low<=K:result.add((tr,low,K))
 name='DOMAIN.json' if U==7 else 'DOMAIN_U'+str(U)+'_R13.json'
 old=json.loads((P/name).read_text());actual={(tuple(tuple(e) for e in t),lo,hi) for t,lo,hi,r13 in old if r13}
 assert result==actual
 answer.append({'U':U,'cartesian_candidates':candidates,'inventories':len(result),'degree_keys':sum(hi-lo+1 for _,lo,hi in result),'equals_growth_domain':True})
out={'status':'PASS','rows':answer,'cpu_seconds':process_time()-start}
(P/'PRODUCT_DOMAIN_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
