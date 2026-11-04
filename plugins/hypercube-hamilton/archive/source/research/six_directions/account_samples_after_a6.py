"""Classify old samples under the A6/eight-free proofs; not a global census."""
import collections,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def main():
 source=ROOT/'remaining_samples_after_eight_adjacent.json'
 data=json.loads(source.read_text(encoding='utf-8-sig'))
 approved=json.loads((ROOT/'A6_CLOSURE_REVIEW.json').read_text(encoding='utf-8-sig'))
 assert approved.get('verdict',approved.get('status'))=='PASS'
 counts=collections.Counter();closed=[];remaining=[]
 goodrows={(0,1),(0,2),(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3)}
 for r in data['remaining']:
  u=r['u'];v=r['v']^u;M=[(a^u,b^u) for a,b in r['matching']]
  assert len(M)==28 and len({a for e in M for a in e})==56
  assert all((a^b).bit_count()==1 for a,b in M)
  holes=set(range(64))-{a for e in M for a in e}
  assert 0 in holes and v.bit_count()%2==1
  Z=[a for a in holes if a and a.bit_count()%2==0];W=[a for a in holes if a.bit_count()%2]
  if v in holes:reason='eight_free';cuts=[]
  else:
   cuts=[]
   for i in range(6):
    a=sum((z>>i&1)==(v>>i&1) for z in Z);b=sum((z>>i&1)==(v>>i&1) for z in W)
    if (a,b) in goodrows:cuts.append({'coordinate':i,'a':a,'b':b})
   reason='covered_good_cut' if cuts else 'R8-covered'
  counts[reason]+=1
  row=dict(r,closure_reason=reason,good_cuts=cuts)
  (remaining if reason=='R8-covered' else closed).append(row)
 result={'scope':'Old sample accounting only; zero remaining samples is NOT full eight-hole P6',
         'source':source.name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'counts':dict(counts),'newly_closed_count':len(closed),'remaining_count':len(remaining),
         'closed':closed,'remaining':remaining,'full_eight_hole_proved':False,'full_p6_proved':False}
 (ROOT/'remaining_samples_after_a6.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:result[k] for k in ('counts','newly_closed_count','remaining_count')}))
if __name__=='__main__':main()
