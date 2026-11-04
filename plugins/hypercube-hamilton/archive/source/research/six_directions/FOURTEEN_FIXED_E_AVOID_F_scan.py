"""Producer actual sufficient gate; no acceptance or main ledger edits."""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter,defaultdict
import json
P=Path(__file__).resolve().parent
local=json.loads((P/'FOURTEEN_FIXED_E_AVOID_F_local.json').read_text());g=local['geometry']
H=set(g['majority']);U=set(g['omitted']);e=(19,23);f=(8,24)
def mask(s):return sum(1<<v for v in s)
maps=[tuple(sum(((v>>p[k])&1)<<k for k in range(5)) for v in range(32)) for p in permutations(range(5))]
lookup=defaultdict(list)
for anchor in U:
 for pi,tr in enumerate(maps):
  lookup[mask(tr[x^anchor] for x in H),mask(tr[x^anchor] for x in U)].append((anchor,pi))
def proj(x,d):return (x&((1<<d)-1))|((x>>(d+1))<<d)
def lift(x,d,side):return (x&((1<<d)-1))|((x>>d)<<(d+1))|(side<<d)
def peel(alive):
 alive=set(alive);out=[]
 while True:
  edge=next(((x,ns[0]) for x in sorted(alive) if len(ns:=[x^(1<<d) for d in range(6) if x^(1<<d) in alive])==1),None)
  if edge is None:return out
  out.append(edge);alive-=set(edge)
def forbidden_certificate(alive,pair):
 # If no perfect matching remains after fixing pair, return exact Hall witness.
 rem=alive-set(pair);E=sorted(x for x in rem if x.bit_count()%2==0)
 adj={x:[x^(1<<d) for d in range(6) if x^(1<<d) in rem] for x in E};mate={}
 def augment(x,seen):
  for y in adj[x]:
   if y in seen:continue
   seen.add(y)
   if y not in mate or augment(mate[y],seen):mate[y]=x;return True
  return False
 for x in E:augment(x,set())
 if len(mate)==len(E):return None
 reached=set(E)-set(mate.values());changed=True
 while changed:
  N={y for x in reached for y in adj[x]};new={mate[y] for y in N if y in mate}-reached
  changed=bool(new);reached|=new
 N={y for x in reached for y in adj[x]};assert len(N)<len(reached)
 return dict(even_subset=sorted(reached),neighbors=sorted(N),deleted_pair=sorted(pair))
selected=[];profile=Counter();total=Counter();records=[];examples=[];optionhist=Counter();conditional=[]
for v in (1,7,31):
 raw=(P/f'FOURTEEN_RESIDUAL_STRUCTURE_maxA_remaining_v{v}_covered.bin').read_bytes();positive=[];remain=[]
 for index,off in enumerate(range(0,len(raw),13)):
  rec=tuple(raw[off:off+13]);Z=set(rec[:6]);W=set(rec[6:]);alive=set(range(64))-{0}-Z-W
  chain=peel(alive);forces={tuple(sorted(x)) for x in chain};found=None;possible_pairs=set()
  for d in range(6):
   aside=v>>d&1;A=lambda x:(x>>d&1)==aside
   za=Z&{x for x in range(64) if A(x)};wa={x for x in W if A(x)};s=len(za)+1-len(wa)
   if s>=3:
    if not wa:continue
    pool=za;minor={x for x in Z if not A(x)};major={x for x in W if not A(x)}
   elif s<=-3:
    s=-s;pool=wa-{1<<d};minor={x for x in W if not A(x)};major={x for x in Z if not A(x)}
   else:continue
   if minor or len(major)+s!=12 or s!=6:continue
   for S in combinations(sorted(pool),s):
    Y={x^(1<<d) for x in S};actualH={proj(x,d) for x in major|Y};actualU={proj(x,d) for x in Y};anchor=min(actualU)
    key=(mask(x^anchor for x in actualH),mask(x^anchor for x in actualU))
    for ca,pi in lookup.get(key,[]):
     tr=maps[pi];glob=lambda x:lift(tr[x^ca]^anchor,d,1-aside)
     ee=tuple(sorted(map(glob,e)));ff=tuple(sorted(map(glob,f)))
     if ee not in forces or set(ee)&Y:continue
     total['fixed_e_projections']+=1
     possible_pairs.add(ff)
     general_hall=forbidden_certificate(alive,ff)
     if general_hall is not None:
      total['general_Hall_impossible_f']+=1
      if found is None:
       found=dict(v=v,input_index=index,record=list(rec),cut=d,sources=list(S),canonical_anchor=ca,
        permutation_index=pi,actual_anchor=anchor,actual_required_edge=list(ee),actual_forbidden_edge=list(ff),
        leaf_chain=chain,forbidden_original_edge_Hall=general_hall,
        route='mixed_parity_completion_avoidance_given_no_original_f')
     total['canonical_root_'+str(next((x for x in range(32) if glob(x)==0),-1))]+=1
     if len(examples)<8:examples.append(dict(v=v,record=rec,cut=d,sources=S,e=ee,f=ff,chain=chain,canonical_root=next((x for x in range(32) if glob(x)==0),-1)))
     # Safe obstruction exclusion via one unchanged original edge. Prefer
     # an already forced surviving edge at either endpoint of f.
     guard=next((edge for edge in forces if set(edge)&set(ff) and edge!=ff and all(not A(x) for x in edge) and not set(edge)&Y),None)
     hall=None;protected=None
     if guard is None:
      # canonical24 has same parity as Y; its original mate cannot be in Y.
      protected=glob(24)
      if protected not in alive or protected^(1<<d) not in Z|W:continue
      assert all(protected.bit_count()%2==y.bit_count()%2 for y in Y)
      total['protected24_projections']+=1
      hall=forbidden_certificate(alive,ff)
      if hall is None:continue
     total['sufficient_projections']+=1
     if found is None:
      found=dict(v=v,input_index=index,record=list(rec),cut=d,sources=list(S),canonical_anchor=ca,
       permutation_index=pi,actual_anchor=anchor,actual_required_edge=list(ee),actual_forbidden_edge=list(ff),
       leaf_chain=chain,surviving_guard_edge=guard,protected24=protected,forbidden_original_edge_Hall=hall)
  if possible_pairs:
   optionhist[len(possible_pairs)]+=1
   conditional.append(dict(v=v,input_index=index,record=rec,forbidden_pairs=sorted(possible_pairs)))
  if found:selected.append(found);positive.append(rec);profile[v]+=1
  else:remain.append(rec)
 for name,rr in [('positive',positive),('remaining',remain)]:
  (P/f'FOURTEEN_FIXED_E_AVOID_F_{name}_v{v}_covered.bin').write_bytes(b''.join(map(bytes,rr)))
 records.append(dict(v=v,input=len(raw)//13,positive=len(positive),remaining=len(remain)))
out=dict(status='PRODUCER_SUFFICIENT_APPLICATION_PENDING_FRESH_LOCAL_AND_TRANSFER_REVIEW',
 totals=dict(total),reports=records,examples=examples,conditional_records=conditional,
 distinct_forbidden_pair_choices=dict(optionhist),selected=selected,new_positive=sum(profile.values()),
 remaining=2527-sum(profile.values()),full_fourteen_hole_proved=False,full_P6_proved=False)
(P/'FOURTEEN_FIXED_E_AVOID_F_application.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('selected','conditional_records','examples')},indent=2))
