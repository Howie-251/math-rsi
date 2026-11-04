"""Producer actual witness and exact-complement self-check, not independent review."""
from pathlib import Path
from itertools import permutations
from collections import Counter
import struct,json,hashlib
R=Path(__file__).resolve().parent
classes={r['index']:r for r in json.loads((R/'FOURTEEN_FORCED_summary.json').read_text())['reports']}
maps=[tuple(sum(((x>>p[d])&1)<<d for d in range(5)) for x in range(32)) for p in permutations(range(5))]
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
def vertices(m):return {x for x in range(32) if m>>x&1}
def pairset(es):return {frozenset(e) for e in es}
raws={v:(R/f'FOURTEEN_HALL_remaining_v{v}_covered.bin').read_bytes() for v in (1,7,31)};seen={v:set() for v in raws};hist=Counter()
data=(R/'FOURTEEN_FORCED_witnesses.bin').read_bytes();assert len(data)%40==0
for v,i,row,d,S,M,J,O,nr,*ends in struct.iter_unpack('<BIHBQIIIB4B7x',data):
 assert v in raws and i not in seen[v] and 13*i+13<=len(raws[v]);seen[v].add(i)
 rec=raws[v][13*i:13*i+13];Z,W=rec[:6],rec[6:];assert v not in W and len({0,*rec})==14
 A=lambda x:(x>>d&1)==(v>>d&1)
 za=[x for x in Z if A(x)];wa=[x for x in W if A(x)];gap=len(za)+1-len(wa);even=gap>=0;s=abs(gap)
 selected={x for x in range(64) if S>>x&1};assert len(selected)==s and s in (3,4,5)
 if even:assert len(wa)>=1 and selected<=set(za);minor=[x for x in Z if not A(x)];major=[x for x in W if not A(x)]
 else:assert selected<=set(wa) and 1<<d not in selected;minor=[x for x in W if not A(x)];major=[x for x in Z if not A(x)]
 Y={x^(1<<d) for x in selected};assert not Y&{0,*rec}
 assert vertices(M)=={project(x,d) for x in minor} and vertices(O)=={project(x,d) for x in Y} and vertices(J)=={project(x,d) for x in set(major)|Y}
 assert nr==len(classes[row]['forced_pairs']) and all(x==255 for x in ends[2*nr:]);actualpairs=tuple(zip(ends[:2*nr:2],ends[1:2*nr:2]))
 assert not {x for e in actualpairs for x in e}&(vertices(M)|vertices(J));assert not(v>>d&1 and 0 in {x for e in actualpairs for x in e})
 g=classes[row]['geometry'];found=False
 for anchor in vertices(M):
  for tr in maps:
   if {tr[x^anchor] for x in vertices(M)}!=set(g['minority']):continue
   if {tr[x^anchor] for x in vertices(J)}!=set(g['majority']):continue
   if {tr[x^anchor] for x in vertices(O)}!=set(g['omitted']):continue
   if pairset((tr[a^anchor],tr[b^anchor]) for a,b in actualpairs)!=pairset(classes[row]['forced_pairs']):continue
   found=True;break
  if found:break
 assert found;hist[row]+=1
for v,raw in raws.items():
 remaining=b''.join(raw[i:i+13] for i in range(0,len(raw),13) if i//13 not in seen[v]);assert remaining==(R/f'FOURTEEN_FORCED_remaining_v{v}_covered.bin').read_bytes()
out={'status':'PRODUCER_AUTHOR_CHECK_SUCCESS_NOT_INDEPENDENT_ACCEPTANCE','actual_witnesses_fully_replayed':len(data)//40,'chosen_classes':dict(hist),'exact_three_source_order_complements':True,'independent_local_and_actual_application_review_required':True,'full_fourteen_hole_proved':False,'full_P6_proved':False}
(R/'FOURTEEN_FORCED_application_author_check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
