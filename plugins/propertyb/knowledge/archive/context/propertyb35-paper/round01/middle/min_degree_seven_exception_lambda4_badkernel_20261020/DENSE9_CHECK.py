"""Tiny refinement of dense-kernel18 to9 (and0/6/6/9 by tau), then24 saved keys. No new probability/layout table."""
from pathlib import Path
from itertools import product
from math import comb
import json,time
P=Path(__file__).resolve().parent;st=time.process_time();parts=((0,5),(1,4),(2,3))
triples=[(ls,sum(comb(l-1,2) for l in ls)) for ls in product(range(1,5),repeat=3)]
def F(t,a):
 ls=(t[0],t[1],a[0],t[2],a[1],a[2]);L=sum(ls);return sum(min(ls[i],ls[j]) for i,j in parts if L-ls[i]-ls[j]>=13)
one={T:0 for T in (8,9,10)};two={T:0 for T in (8,9,10)};three={T:0 for T in (8,9,10)};witness={};count=0;classmax={}
for t,c in triples:
 cand=[]
 for a,d in triples:
  val=F(t,a)
  if c+d<=10:
   for T in one:
    if c+d<=T:one[T]=max(one[T],val)
  if c+d>=8 and c+d<=10 and val:cand.append((a,d,val))
 for a,d,fa in cand:
  for b,e,fb in cand:
   if c+d+e>10:continue
   count+=1;classmax[c]=max(classmax.get(c,0),fa+fb)
   for T in two:
    if c+d+e<=T:
     if fa+fb>two[T]:two[T]=fa+fb;witness[str(T)]={'triangle':t,'triangle_cost':c,'first_attach':a,'first_cost':d,'first_matching':fa,'second_attach':b,'second_cost':e,'second_matching':fb}
# In the3-kernel case the established family lemma forces tau10,cS7 and3 attachcost1.
per=max(F(t,a) for t,c in triples if c==7 for a,d in triples if d==1);assert per==2;three[10]=3*per
assert one=={8:6,9:6,10:9} and two=={8:0,9:4,10:7} and three=={8:0,9:0,10:6};assert count==288
B={t:(0 if t<=7 else max(one[t],two[t],three[t])) for t in range(11)}
old=json.loads((P/'RESULT.json').read_text());ind=json.loads((P/'FINAL_VERIFY_RESULT.json').read_text());assert ind['status']=='PASS_COMPLETE_447_WITH_FULL_DOMAIN_AND_CONTEXTS';keys=[]
for z in old['key_refinement']:
 k=z['key'];caps=k['caps'].copy();applied=k['tau']<=10
 if applied:
  assert z['cost_ge8_caller_complete_in_pilot'];caps[3]=min(caps[3],12*k['n'][3]+B[k['tau']])
 v=6864*k['n'][1]+sum(dw*min(k['newP'],sum(caps[i:])) for i,dw in enumerate((36,84,210,462,924)))
 keys.append({'spectrum_id':z['spectrum_id'],'n':k['n'],'tau':k['tau'],'newP':k['newP'],'new_caps':caps,'dense_pointwise_B':B.get(k['tau']),'twice_L':v,'strict':v<5445440,'lambda4_subbranch_only':True,'coupled_P_candidate_not_used':z['coupled_P_candidate_not_used']})
ids=sorted({k['spectrum_id'] for k in keys});out={'status':'PASS_DENSE9_TINY_AND_SAVED24_KEY_REFINEMENT','scope':__doc__,'one_kernel_matching_max':one,'two_kernel_matching_max':two,'three_kernel_matching_max':three,'two_kernel_feasible_cases':count,'two_kernel_by_triangle_cost':classmax,'two_kernel_witnesses':witness,'bad_outer_bound_tau0_through10':B,'strict_keys':sum(k['strict'] for k in keys),'remaining_key_count':sum(not k['strict'] for k in keys),'newly_strict_lambda4_subbranch_ids':[sid for sid in ids if all(k['strict'] for k in keys if k['spectrum_id']==sid)],'remaining_spectrum_ids':[sid for sid in ids if any(not k['strict'] for k in keys if k['spectrum_id']==sid)],'all_keys':keys,'remaining_keys':[k for k in keys if not k['strict']],'cpu_seconds':time.process_time()-st};(P/'DENSE9_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('all_keys','remaining_keys')}));print('REMAIN',out['remaining_keys'])
