"""Producer actual root-safe projections for new single/multi-cherry inputs."""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter
import json,hashlib,struct
R=Path(__file__).resolve().parent
summary=json.loads((R/'FOURTEEN_NEW_TYPES_summary.json').read_text())
maps=[tuple(sum(((x>>p[d])&1)<<d for d in range(5)) for x in range(32)) for p in permutations(range(5))]
def mask(xs):return sum(1<<x for x in set(xs))
def normpairs(pairs,tr,anchor):return tuple(sorted(tuple(sorted((tr[a^anchor],tr[b^anchor]))) for a,b in pairs))
classes=[];lookup={}
for row in summary['reports']:
 g=row['geometry'];H=set(g['minority']+g['majority']);U=set(g['omitted']);K=set(range(32))-H;ch=[]
 for h in sorted(H-U):
  ns=sorted({h^(1<<d) for d in range(5)}-U)
  if len(ns)==2 and set(ns)<=K:ch.append((h,*ns))
 pairs=[(p,q) for h,p,q in ch]
 if not pairs and not row['full_rank']:continue
 if len({x for e in pairs for x in e})!=2*len(pairs):continue
 target=1<<((len(K)-2*len(pairs))//2-1)
 if row['rank']!=target:continue
 classes.append({'index':row['index'],'geometry':g,'forced_cherries':ch,'forced_pairs':pairs,'covered_endpoints':len(K),'reduced_endpoints':len(K)-2*len(pairs),'target_rank':target,'source_prefix':row['prefix']})
 for anchor in g['minority']:
  for tr in maps:
   key=tuple(mask(tr[x^anchor] for x in g[k]) for k in ['minority','majority','omitted']);value=(row['index'],normpairs(pairs,tr,anchor))
   assert key not in lookup or lookup[key]==value;lookup[key]=value
(R/'EIGHTEEN_POST12_FORCED_candidate_classes.json').write_text(json.dumps({'status':'PRODUCER_CANDIDATE_LOCAL_CLASSIFICATIONS_NOT_YET_ACCEPTED','classes':classes},indent=2)+'\n')
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
reports=[];witness=bytearray();hist=Counter();mult=Counter();inputhash={};forcedset=set();plainset=set()
for v in [1,7,31]:
 name=f'EIGHTEEN_POST12_HALL_remaining_v{v}_covered.bin';raw=(R/name).read_bytes();assert len(raw)%17==0;inputhash[name]=hashlib.sha256(raw).hexdigest();rem=bytearray();safe=0;proj=0;hitsets=Counter()
 for off in range(0,len(raw),17):
  rec=raw[off:off+17];Z,W=rec[:8],rec[8:];assert v not in W;found=None;allids=set()
  for d in range(6):
   A=lambda x:(x>>d&1)==(v>>d&1)
   za=[x for x in Z if A(x)];wa=[x for x in W if A(x)];s=len(za)+1-len(wa)
   if s>=3:
    if not wa:continue
    pool=za;minor=[x for x in Z if not A(x)];major=[x for x in W if not A(x)]
   elif s<=-3:
    s=-s;pool=[x for x in wa if x!=(1<<d)];minor=[x for x in W if not A(x)];major=[x for x in Z if not A(x)]
   else:continue
   if (len(minor),len(major)+s,s) not in [(3,9,3),(2,10,4),(1,11,5)]:continue
   for S in combinations(pool,s):
    proj+=1;M=[project(x,d) for x in minor];O=[project(x^(1<<d),d) for x in S];J=[project(x,d) for x in major]+O;anchor=min(M)
    key=tuple(mask(x^anchor for x in xs) for xs in [M,J,O]);candidate=lookup.get(key)
    if candidate is None:continue
    row,npairs=candidate;pairs=tuple(tuple(sorted((a^anchor,b^anchor))) for a,b in npairs)
    assert not {x for e in pairs for x in e}&(set(M)|set(J))
    if v>>d&1 and 0 in {x for e in pairs for x in e}:continue
    allids.add(row)
    if found is None:found=(row,d,mask(S),mask(M),mask(J),mask(O),pairs)
  for i in allids:hitsets[i]+=1
  if 54 in allids:plainset.add((v,off//17))
  if allids-{54}:forcedset.add((v,off//17))
  if found:
   row,d,S,M,J,O,pairs=found;ends=[x for e in pairs for x in e]+[255]*(4-2*len(pairs));witness.extend(struct.pack('<BIHBQIIIB4B7x',v,off//17,row,d,S,M,J,O,len(pairs),*ends));hist[row]+=1;mult[len(pairs)]+=1;safe+=1
  else:rem.extend(rec)
 out=f'EIGHTEEN_POST12_FORCED_remaining_v{v}_covered.bin';(R/out).write_bytes(rem);reports.append({'v':v,'input':len(raw)//17,'safe':safe,'remaining':len(rem)//17,'legal_source_projections':proj,'per_local_hit_records':dict(hitsets),'remaining_file':out,'remaining_sha256':hashlib.sha256(rem).hexdigest()})
(R/'EIGHTEEN_POST12_FORCED_witnesses.bin').write_bytes(witness)
out={'status':'PRODUCER_CONDITIONAL_ON_LOCAL_CERTIFICATES_AND_SOURCE_ACCEPTANCE','candidate_indices':[c['index'] for c in classes],'lookup_size':len(lookup),'input':sum(r['input'] for r in reports),'safe':sum(r['safe'] for r in reports),'remaining':sum(r['remaining'] for r in reports),'forced8_subset':len(forcedset),'unconditional54_subset':len(plainset),'intersection':len(forcedset&plainset),'union':len(forcedset|plainset),'chosen_local_counts':dict(hist),'chosen_cherry_count_histogram':dict(mult),'reports':reports,'input_hashes':inputhash,'witness_bytes':40,'full_eighteen_hole_proved':False,'full_P6_proved':False}
(R/'EIGHTEEN_POST12_FORCED_coverage.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
