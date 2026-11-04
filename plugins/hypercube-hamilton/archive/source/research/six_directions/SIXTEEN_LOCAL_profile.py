"""Conditional producer: new ordinary and root-safe forced local inputs."""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter
import json,hashlib,struct
R=Path(__file__).resolve().parent
summary=json.loads((R/'SIXTEEN_NEW_TYPES_summary.json').read_text())
maps=[tuple(sum(((x>>p[d])&1)<<d for d in range(5)) for x in range(32)) for p in permutations(range(5))]
def mask(xs):return sum(1<<x for x in set(xs))
classes=[];lookup={};shapes=set()
for row in summary['reports']:
 g=row['geometry'];H=set(g['minority']+g['majority']);U=set(g['omitted']);K=set(range(32))-H;ch=[]
 for h in sorted(H-U):
  ns=sorted({h^(1<<d) for d in range(5)}-U)
  if len(ns)==2 and set(ns)<=K:ch.append((h,*ns))
 pairs=[(p,q) for h,p,q in ch]
 if not pairs and not row['full_rank']:continue
 if len({x for e in pairs for x in e})!=2*len(pairs):continue
 if pairs and len({x.bit_count()%2 for x in U|{x for e in pairs for x in e}})!=1:continue
 target=1<<((len(K)-2*len(pairs))//2-1)
 if row['rank']!=target:continue
 cls={'index':row['index'],'geometry':g,'forced_cherries':ch,'forced_pairs':pairs,'covered_endpoints':len(K),'reduced_endpoints':len(K)-2*len(pairs),'target_rank':target,'source_prefix':row['prefix']};classes.append(cls)
 shapes.add((len(g['minority']),len(g['majority']),len(U)))
 for anchor in g['minority'] or g['omitted']:
  for tr in maps:
   key=tuple(mask(tr[x^anchor] for x in g[k]) for k in ('minority','majority','omitted'))
   val=(row['index'],tuple(sorted(tuple(sorted((tr[a^anchor],tr[b^anchor]))) for a,b in pairs)))
   assert key not in lookup or lookup[key]==val;lookup[key]=val
(R/'SIXTEEN_LOCAL_candidate_classes.json').write_text(json.dumps({'status':'CONDITIONAL_PRODUCER_ONLY','classes':classes},indent=2)+'\n')
def project(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
reports=[];hashes={};witness=bytearray();hist=Counter();allhits=[]
for v in (1,7,31):
 name=f'SIXTEEN_POST12_FORCED_remaining_v{v}_covered.bin';raw=(R/name).read_bytes();assert len(raw)%15==0;hashes[name]=hashlib.sha256(raw).hexdigest();keep=bytearray();safe=0;proj=0
 for idx in range(len(raw)//15):
  rec=raw[15*idx:15*(idx+1)];Z,W=rec[:7],rec[7:];found=None;allids=set()
  for d in range(6):
   A=lambda x:(x>>d&1)==(v>>d&1)
   za=[x for x in Z if A(x)];wa=[x for x in W if A(x)];s=len(za)+1-len(wa)
   if s>=2:
    if not wa:continue
    pool=za;minor=[x for x in Z if not A(x)];major=[x for x in W if not A(x)]
   elif s<=-2:s=-s;pool=[x for x in wa if x!=(1<<d)];minor=[x for x in W if not A(x)];major=[x for x in Z if not A(x)]
   else:continue
   if (len(minor),len(major)+s,s) not in shapes:continue
   for S in combinations(pool,s):
    proj+=1;M=[project(x,d) for x in minor];O=[project(x,d) for x in S];J=[project(x,d) for x in major]+O;anchor=min(M or O)
    candidate=lookup.get(tuple(mask(x^anchor for x in xs) for xs in (M,J,O)))
    if candidate is None:continue
    row,npairs=candidate;pairs=tuple(tuple(sorted((a^anchor,b^anchor))) for a,b in npairs)
    if pairs:
     assert s>=3
     if v>>d&1 and 0 in {x for e in pairs for x in e}:continue
    allids.add(row)
    if found is None:found=(row,d,mask(S),mask(M),mask(J),mask(O),pairs)
  allhits.append({'v':v,'index':idx,'local_indices':sorted(allids)})
  if found:
   row,d,S,M,J,O,pairs=found;assert len(pairs)<=2
   ends=[x for e in pairs for x in e]+[255]*(4-2*len(pairs));witness.extend(struct.pack('<BIHBQIIIB4B7x',v,idx,row,d,S,M,J,O,len(pairs),*ends));safe+=1;hist[row]+=1
  else:keep.extend(rec)
 out=f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin';(R/out).write_bytes(keep)
 reports.append({'v':v,'input':len(raw)//15,'safe':safe,'remaining':len(keep)//15,'projections':proj})
(R/'SIXTEEN_LOCAL_witnesses.bin').write_bytes(witness)
(R/'SIXTEEN_LOCAL_all_hit_sets.json').write_text(json.dumps(allhits)+'\n')
out={'status':'CONDITIONAL_PRODUCER_ONLY','classes':len(classes),'input_hashes':hashes,'reports':reports,'chosen_histogram':dict(hist),'remaining':sum(x['remaining'] for x in reports),'full_P6_proved':False}
(R/'SIXTEEN_LOCAL_coverage.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
