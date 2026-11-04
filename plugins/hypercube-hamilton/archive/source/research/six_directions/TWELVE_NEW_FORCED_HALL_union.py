"""Separate exact union of conditional safe-forced cases and explicit Hall exclusions."""
from pathlib import Path
import json,struct,hashlib
P=Path(__file__).resolve().parent
forced=set();hall=set();sources={v:(P/f'TWELVE_NEW_TYPES_positive_remaining_v{v}.bin').read_bytes() for v in (1,7,31)}
for v,i,*rest in struct.iter_unpack('<BIHBQIIII',(P/'TWELVE_NEW_FORCED_safe_witnesses.bin').read_bytes()):
 assert (v,i) not in forced;forced.add((v,i))
odd=sum(1<<x for x in range(64) if x.bit_count()%2);even=((1<<64)-1)^odd
neighbors=[sum(1<<(x^(1<<d)) for d in range(6)) for x in range(64)]
for v,i,S,T in struct.iter_unpack('<BIQQ',(P/'TWELVE_HALL_witnesses.bin').read_bytes()):
 assert (v,i) not in hall;hall.add((v,i));rec=sources[v][11*i:11*i+11];assert len(rec)==11
 Z=set(rec[:5]);W=set(rec[5:]);coveredE=even&~(1|sum(1<<x for x in Z));coveredO=odd&~sum(1<<x for x in W)
 assert S and not S&~coveredE
 actual=0;todo=S
 while todo:
  low=todo&-todo;actual|=neighbors[low.bit_length()-1];todo^=low
 actual&=coveredO
 assert actual==T and T.bit_count()<S.bit_count()
assert len(forced)==552 and len(hall)==7483
union=forced|hall;reports=[]
for v,raw in sources.items():
 indices={(v,i) for i in range(len(raw)//11)};kept=b''.join(raw[11*i:11*i+11] for i in range(len(raw)//11) if (v,i) not in union)
 name=f'TWELVE_NEW_FORCED_HALL_union_remaining_v{v}.bin';(P/name).write_bytes(kept)
 reports.append({'v':v,'input':len(raw)//11,'safe_forced':len(indices&forced),'Hall_impossible':len(indices&hall),'intersection':len(indices&forced&hall),'union_removed':len(indices&union),'remaining':len(kept)//11,'remaining_file':name,'remaining_sha256':hashlib.sha256(kept).hexdigest()})
out={'status':'PRODUCER_EXACT_UNION_PENDING_FORCED_LOCAL_APPLICATION_AND_HALL_REVIEWS','common_input':37405,'conditional_safe_forced':len(forced),'Hall_impossible':len(hall),'intersection':len(forced&hall),'union_removed':len(union),'remaining':37405-len(union),'every_Hall_S_and_exact_covered_neighbor_T_verified':True,'reports':reports,'original_forced_and_Hall_files_unchanged':True,'full_twelve_hole_proved':False,'full_P6_proved':False}
(P/'TWELVE_NEW_FORCED_HALL_union.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
