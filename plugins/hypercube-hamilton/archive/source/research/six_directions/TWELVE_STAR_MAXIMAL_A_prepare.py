"""Actual case00/03 options with explicit shared coordinate maps; no proof acceptance."""
from pathlib import Path
from itertools import permutations
import struct,json,hashlib
P=Path(__file__).resolve().parent
alloptions=json.loads((P/'TWELVE_ROOT_STAR_NONADJACENT_OPTIONS.json').read_text())
maps=[tuple(sum(((x>>q[d])&1)<<d for d in range(5)) for x in range(32)) for q in permutations(range(5))]
seeds={0:(3,4,7),3:(15,1,7)}
for n in ['TWELVE_STAR_B_REVIEW.json','Q5_T17_RANK_BATCH_REVIEW.json','TWELVE_EXTRA_FORCED_REVIEW.json']:
 assert json.loads((P/n).read_text())['verdict']=='PASS'
rows=[]
for orbit,rep in enumerate(alloptions['representatives']):
 raw=bytearray();options=[];T={x^32 for x in rep['Z']}
 for option in rep['options']:
  case=option['case']
  if case not in (0,3):continue
  q,b,t=option['q'],option['b'],option['t'];w=option['w']
  assert t in T-{31} and (q^t).bit_count()==1 and q.bit_count()%2==0 and w!=b
  assert w in (1,2,4,8,16) and b in (1,2,4,8,16)
  seed=seeds[case];perm=next(i for i,tr in enumerate(maps) if tuple(tr[x] for x in seed)==(q,b,t))
  raw.extend(bytes((q,t,w,b,case,perm)))
  options.append({**option,'permutation_index':perm,'vertex_map':maps[perm]})
 name=f'TWELVE_STAR_MAXIMAL_A_options_{orbit}.bin';(P/name).write_bytes(raw)
 rows.append({'orbit':orbit,'Z':rep['Z'],'T':sorted(T),'options':options,'binary':name})
out={'status':'PRODUCER_OPTIONS_PREPARED','option_record_bytes':6,'coordinate_permutation_output_reads_input':True,'rows':rows,'opening_forests_are_positive_witnesses_not_universal_rank':True,'star_Q6_closed':False}
(P/'TWELVE_STAR_MAXIMAL_A_options.json').write_text(json.dumps(out,indent=2)+'\n')
print('Prepared options:',[len(r['options']) for r in rows])
