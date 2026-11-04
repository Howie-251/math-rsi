"""Separate actual T37-positive and safe forced-T17 subsets of the frozen348283 domain."""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter
import json,struct,hashlib
P=Path(__file__).resolve().parent
BAD={0,1,2,3,6,12,13,14,15};POS=set(range(64))-BAD
summary=json.loads((P/'Q5_T37_INDEPENDENT_summary.json').read_text())
assert {r['index'] for r in summary['reports'] if r['full_rank']}==POS
assert len(POS)==55
assert json.loads((P/'Q5_T37_INDEPENDENT_REVIEW.json').read_text())['verdict']=='PASS'
t37={}
raw=(P/'HIGHER_Q5_FULL_T37_projection_witnesses.bin').read_bytes()
for v,f,i,orb,d,S in struct.iter_unpack('<BBIBBQ',raw):
 if orb in POS:t37.setdefault((v,f,i),(orb,d,S))
assert len(t37)==106052
forced_rows={5:[1,2,4,7,11,28,31],6:[1,2,4,11,13,22,31],9:[1,2,4,7,11,21,31],11:[1,2,4,11,19,25,26],12:[1,2,4,7,11,13,31],13:[1,2,4,11,13,14,31],17:[1,2,4,7,11,13,14]}
lookup={}
for perm in permutations(range(5)):
 tr=lambda x:sum(((x>>perm[i])&1)<<i for i in range(5))
 for row,J in forced_rows.items():
  key=(tuple(sorted(tr(x) for x in J)),tuple(sorted(tr(x) for x in (1,2,4))))
  assert key not in lookup or lookup[key]==row;lookup[key]=row
assert json.loads((P/'HIGHER_FORCED_CHERRY_REVIEW.json').read_text())['verdict']=='PASS'
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
def mask(xs):return sum(1<<x for x in xs)
forced={};forced_binary=bytearray();t37_binary=bytearray();reports=[];inputs={}
for v in (1,7,31):
 for f in (0,1):
  tag=f"h12_v{v}_{'free' if f else 'covered'}";name=f'HIGHER_Q5_FULL_reuse_remaining_{tag}.bin';data=(P/name).read_bytes();inputs[name]=hashlib.sha256(data).hexdigest()
  for off in range(0,len(data),11):
   i=off//11;rid=(v,f,i);Z=data[off:off+5];W=data[off+5:off+11];found=None
   if rid in t37:
    orb,d,S=t37[rid];t37_binary.extend(struct.pack('<BBIBBQ',v,f,i,orb,d,S))
   for d in range(6):
    za=[x for x in Z if (x>>d&1)==(v>>d&1)];wa=[x for x in W if (x>>d&1)==(v>>d&1)]
    if (len(za),len(wa))==(4,2):pool=za;minor=[x for x in Z if x not in za];major=[x for x in W if x not in wa]
    elif (len(za),len(wa))==(1,5):pool=[x for x in wa if x!=(1<<d) and (not f or x!=v)];minor=[x for x in W if x not in wa];major=[x for x in Z if x not in za]
    else:continue
    assert len(minor)==1
    for S in combinations(pool,3):
     m=project(minor[0],d);O=tuple(sorted(project(x,d) for x in S));J=tuple(sorted([project(x,d) for x in major]+list(O)))
     key=(tuple(sorted(x^m for x in J)),tuple(sorted(x^m for x in O)))
     if key not in lookup:continue
     normalR={1,2,4,8,16}-set(key[1]);assert len(normalR)==2
     R={x^m for x in normalR};assert not R&({m}|set(J))
     # u belongs to B exactly when v's cut bit is one; root's projected label is zero.
     if (v>>d&1) and 0 in R:continue
     found=(lookup[key],d,mask(S),1<<m,mask(J),mask(O),mask(R));break
    if found:break
   if found:
    forced[rid]=found;row,d,S,M,J,O,R=found
    forced_binary.extend(struct.pack('<BBIBBQIIII',v,f,i,row,d,S,M,J,O,R))
  counts={'v':v,'free_target':bool(f),'input':len(data)//11}
  ids={(v,f,i) for i in range(len(data)//11)};A=ids&t37.keys();B=ids&forced.keys()
  counts.update(T37_positive=len(A),forced_T17_safe=len(B),intersection=len(A&B),union=len(A|B),remaining_after_T37=len(ids-A),remaining_after_forced=len(ids-B),remaining_after_union=len(ids-A-B))
  for label,covered in [('T37',A),('FORCED17',B),('T37_FORCED_union',A|B)]:
   remaining=b''.join(data[i*11:i*11+11] for i in range(len(data)//11) if (v,f,i) not in covered)
   target=f'HIGHER_Q5_FULL_{label}_remaining_{tag}.bin';(P/target).write_bytes(remaining)
   counts[label+'_remaining_file']=target;counts[label+'_remaining_sha256']=hashlib.sha256(remaining).hexdigest()
  reports.append(counts);print(json.dumps(counts),flush=True)
(P/'HIGHER_Q5_FULL_T37_positive_witnesses.bin').write_bytes(t37_binary)
(P/'HIGHER_Q5_FULL_FORCED17_safe_witnesses.bin').write_bytes(forced_binary)
out={'status':'PRODUCER_ACTUAL_APPLICATION_PENDING_INDEPENDENT_REVIEW','input':348283,'T37_positive_indices':sorted(POS),'T37_open_indices':sorted(BAD),
 'T37_positive_covered':len(t37),'forced_T17_safe_covered':len(forced),'intersection':len(t37.keys()&forced.keys()),
 'union':len(t37.keys()|forced.keys()),'remaining_after_union':348283-len(t37.keys()|forced.keys()),
 'T37_local_candidates_not_yet_accepted':False,'T37_local_review_PASS':True,'forced_general_transfer_import_PASS':True,
 'T37_witness_bytes':16,'forced_witness_bytes':32,'input_hashes':inputs,'reports':reports,
 'full_twelve_hole_proved':False,'full_P6_proved':False}
(P/'HIGHER_Q5_FULL_T37_FORCED_union_coverage.json').write_text(json.dumps(out,indent=2)+'\n')
for family in ('T37','FORCED17'):
 result={**out,'scope':family+' subset of the common frozen348283 domain'}
 (P/f'HIGHER_Q5_FULL_{family}_coverage.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('reports','input_hashes')},indent=2))
