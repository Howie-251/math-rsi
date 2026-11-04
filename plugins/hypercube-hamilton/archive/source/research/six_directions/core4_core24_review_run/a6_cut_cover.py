"""Complete residual A6 hole geometry census (no enumeration of matchings)."""
import itertools,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def main():
 odd=[x for x in range(32) if x.bit_count()%2]
 rows=[];counts=Counter();normalizations={}
 for z in (3,15):
  allowed=[x for x in odd if x.bit_count()!=1 and (x^z).bit_count()!=1]
  count=0
  for triple in itertools.combinations(allowed,3):
   for v in odd:
    if v in triple:continue
    majority=(*triple,v);minority=(0,z)
    deltas=[sum((x>>i&1)==(v>>i&1) for x in majority)-sum((x>>i&1)==(v>>i&1) for x in minority) for i in range(5)]
    # Prefer the cuts with the least transfer machinery, then 3,4,1.
    choice=next(((i,t) for t in (2,3,4,1) for i,d in enumerate(deltas) if d==t),None)
    if choice is None:
     assert (z,triple,v) in ((3,(13,21,25),2),(3,(14,22,26),1)) and deltas==[0]*5
     i,t=None,0;k=None
    else:
     i,t=choice;k=sum((x>>i&1)==(v>>i&1) for x in minority)
    if t==1:assert k in (1,2)
    if t==2:assert k in (0,1)
    if t==3:assert k in (0,1)
    if t==4:assert k==0
    counts[t]+=1;count+=1
    rows.append({'minority':[0,z],'majority':list(majority),'forbidden':v,'deltas':deltas,'cut':i,'delta':t,'minority_in_target_side':k})
  normalizations[z]=count
 assert normalizations=={3:728,15:260} and len(rows)==988
 result={'status':'PASS','scope':'complete normalized residual A6 hole geometry only','normalizations':normalizations,'counts_by_selected_delta':dict(counts),'rows':rows,'a6_proved':False,'full_p6_proved':False}
 (ROOT/'a6_cut_cover.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
if __name__=='__main__':main()
