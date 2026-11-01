"""Independent exactpair lowcost domains plus all447 new fixed certificates expanded to35 original indices. Reuse226 already audited certificates."""
from pathlib import Path
from itertools import product,permutations
from fractions import Fraction
from math import comb
import json,time,sys
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'));from independent_structure_bounds import independent_rows
st=time.process_time();r=json.loads((P/'RESULT.json').read_text());cross=(5,6,9,10);pairs=(3,5,6,9,10,12)
# LowK6cost<=7 forces no triples and exactcross13. Independently check cross inclusive cost at sums14/15.
assert min(sum(comb(x-1,2) for x in ls) for ls in product(range(1,5),repeat=4) if sum(ls)>=14)==8
assert min(sum(comb(x-1,2) for x in ls) for ls in product(range(1,5),repeat=4) if sum(ls)>=15)==10
patterns=[]
for cv in product(range(1,5),repeat=4):
 if sum(cv)!=13:continue
 for A,B in product(range(1,5),repeat=2):
  base=[0]*16;base[3]=A;base[12]=B
  for m,v in zip(cross,cv):base[m]=v
  if sum(comb(base[m]-1,2) for m in pairs)<=7:patterns.append(base)
perms=[]
for a,b,c in product((0,1),repeat=3):
 left=(1,0) if a else (0,1);right=(3,2) if b else (2,3);perms.append(right+left if c else left+right)
old=json.loads((P.parent/'min_degree_seven_residual_cap12_pilot_20261020/RESULT.json').read_text());oldcases={tuple(z['counts']):z for z in old['checked_cases'] if not z['legacy']};oldind=json.loads((P.parent/'min_degree_seven_residual_cap12_pilot_20261020/independent/RESULT.json').read_text());assert oldind['status']=='PASS_COMPLETE_SCOPED_INDEPENDENT_VERIFICATION'
checked_labels=0;checked_reps=0
for q in r['complete_missing_quad_lowcost_domains']:
 need=tuple(q['quad']);keys=set()
 for ds in set(permutations(need)):
  for base in patterns:
   ns=base.copy()
   for i,d in enumerate(ds):ns[1<<i]=d-sum(n for m,n in enumerate(base) if m>>i&1)
   ns[0]=35-sum(ns)
   if min(ns)>=0:keys.add(tuple(ns))
 assert keys==set(map(tuple,q['low_cost_labeled_keys']))
 reps=set()
 for ns in keys:
  ims=[]
  for p in perms:
   out=[0]*16
   for m,n in enumerate(ns):out[sum(1<<p[i] for i in range(4) if m>>i&1)]=n
   ims.append(tuple(out))
  reps.add(min(ims))
 assert reps=={tuple(x['counts']) for x in q['entries']};checked_labels+=len(keys);checked_reps+=len(reps)
# Recompute active taucontexts using direct inclusive incidence and exact h17 formula.
contexts={};new=[]
for q in r['complete_missing_quad_lowcost_domains']:
 for z in q['entries']:
  mu=z['counts'];ds=[sum(n for m,n in enumerate(mu) if m>>i&1) for i in range(4)];inc={m:sum(n for T,n in enumerate(mu) if T&m==m) for m in pairs};cost=sum(comb(l-1,2) for l in inc.values());extra=0
  for i,d in enumerate(ds):
   S=4*d-sum(v for m,v in inc.items() if m>>i&1);assert 17<=S<=68;extra+=max(0,S-34,2*S-85)
  active=[]
  for j in r['source24_keys_in6_spectra']:
   if q['quad'] not in next(x for x in r['actual_quad_projection'] if x['spectrum_id']==j['spectrum_id'])['missing_quads']:continue
   whole=j['degrees'];D=max(whole);outsideD=whole.count(D)>ds.count(D);need=cost+max(extra,max(0,4*D-40) if outsideD else 0)
   if j['key']['tau']>=need:active.append((j['spectrum_id'],j['source_key_index'],j['key']['tau'],need))
  assert sorted(active)==sorted((x['spectrum_id'],x['source_key_index'],x['tau'],x['required_tau']) for x in z['active_contexts'])
for z in r['all_checked_cases']:
 if z['reused_verified_previous_case']:
  assert tuple(z['counts']) in oldcases and oldcases[tuple(z['counts'])]['best']==z['best'] and z['best']['strict']
 else:new.append(z)
assert len(new)==447
stream=(P/'VERIFY_ROWS.jsonl').open('w');n=0;maximum=Fraction();partial=False
for z in new:
 masks=[m for m,num in enumerate(z['counts']) for _ in range(num)];assert len(masks)==35
 types=[frozenset(i+1 for i in range(4) if m>>i&1) for m in masks];rr=independent_rows(21,tuple(z['best']['positions']),types);v=sum((min(x['A'],x['B'],x['C']) for x in rr),Fraction());assert v==Fraction(z['best']['bound'])<1;n+=1;maximum=max(maximum,v)
 stream.write(json.dumps({'counts':z['counts'],'quad':z['quad'],'expanded35_masks':masks,'positions':z['best']['positions'],'bound':str(v),'rows':[{k:str(v) if isinstance(v,Fraction) else v for k,v in x.items()} for x in rr]})+'\n')
 if time.process_time()-st>4.2:partial=True;break
stream.close()
out={'status':'CPU_BOUNDED_PARTIAL' if partial else 'PASS_COMPLETE_LOW_COST_DOMAIN_CONTEXTS_AND447_CERTIFICATES','scope':__doc__,'explicit_lambda4_subbranches_only':True,'lowcost_quad_domains':len(r['complete_missing_quad_lowcost_domains']),'lowcost_labeled_keys':checked_labels,'lowcost_D8_representatives':checked_reps,'all24_taucontexts_equal':True,'reused_verified_certificates':226,'new_certificates_expected':447,'new_original35_certificates_replayed':n,'position_rows':21*n,'maximum_strict_bound':str(maximum),'new_nonstrict':[],'cpu_seconds':time.process_time()-st};(P/'VERIFY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
