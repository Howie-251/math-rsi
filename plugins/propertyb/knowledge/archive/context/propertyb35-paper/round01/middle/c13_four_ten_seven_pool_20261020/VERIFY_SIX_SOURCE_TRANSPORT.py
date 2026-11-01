"""All six actual K inventories, exact S4 transport of counts and fixed positions."""
from pathlib import Path
from itertools import permutations
from collections import Counter
from fractions import Fraction
import json,sys,time
P=Path(__file__).resolve().parent;ROOT=P.parents[4];st=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows,injection_probability
tails=[z['counts'] for z in json.loads((P.parent/'generic_c3_thirteen_pilot_20261020/RESULT.json').read_text())['cases'] if not z['strict']]
proofs={0:json.loads((P/'shared_views/VERIFY_DUAL.json').read_text()),2:json.loads((P/'shared_views_orbit2/VERIFY_DUAL.json').read_text())}
assert all(p['status']=='PASS_COMPLETE_ACTUAL_DOMAIN_AND_EXACT_CHARGING_CLOSURE' for p in proofs.values())
def mask_image(m,p):return sum(1<<p[i] for i in range(4) if m>>i&1)
def image(mu,p):
 a=[0]*16
 for m,n in enumerate(mu):a[mask_image(m,p)]=n
 return a
records=[];total=0
for sid,mu in enumerate(tails):
 found=[(rid,p) for rid in (0,2) for p in permutations(range(4)) if image(mu,p)==tails[rid]]
 assert found
 rid,p=min(found);proof=proofs[rid]
 repcoef={m:w for m,w in zip((m for m,n in enumerate(tails[rid]) if n),proof['charging_coefficients'])}
 originalcoef={m:repcoef.get(mask_image(m,p),0) for m,n in enumerate(mu) if n}
 charge=sum(originalcoef[m]*n*(5-m.bit_count()) for m,n in enumerate(mu) if n)
 assert charge==192<204
 inverse=[0]*4
 for i,j in enumerate(p):inverse[j]=i
 def original_mask(m):return (m&1)|(mask_image(m>>1,inverse)<<1)
 sample=None
 for cert in proof['cases']:
  masks=[original_mask(m) for m in cert['expanded35_masks']]
  assert len(masks)==35 and Counter(m>>1 for m in masks)==Counter({m:n for m,n in enumerate(mu) if n})
  pos=[cert['positions'][0]]+[cert['positions'][1+p[i]] for i in range(4)]
  assert len(set(pos))==5
  dd=[sum(bool(m>>i&1) for m in masks) for i in range(5)]
  assert dd==[cert['r'],10,10,10,10]
  c=Counter(m>>1 for m in masks if m&1)
  score=sum(originalcoef[m]*n for m,n in c.items());assert score==cert['score']<12
  assert sum(m==1 for m in masks)==cert['expanded35_masks'].count(1)
  if sample is None:sample=(masks,pos,cert)
  total+=1
 masks,pos,cert=sample;types=[frozenset(i+1 for i in range(5) if m>>i&1) for m in masks]
 ir=independent_rows(21,tuple(pos),types);U=Fraction()
 for rr in ir:
  W=injection_probability(16,rr['a'],rr['b'],4,4,False) if rr['k']==pos[0] else Fraction()
  U+=min(rr['A'],rr['B'],rr['C']-2*cert['pure_unordered_quota']*W)
 assert U==Fraction(cert['bound'])<1
 records.append(dict(source=sid,representative=rid,original_K_to_representative=list(p),source_counts=mu,charging_coefficients_by_original_mask=originalcoef,actual_total_charge=charge,transported_certificate_count=len(proof['cases']),all_actual35_projection_degrees_positions_and_score_checked=True,sample_transported_positions=pos,sample_exact_bound=str(U),sample_original35_replay=True))
assert [r['source'] for r in records if r['representative']==0]==[0,1,3,5]
assert [r['source'] for r in records if r['representative']==2]==[2,4]
out=dict(status='PASS_ALL_SIX_ACTUAL_SOURCE_TRANSPORTS',scope=__doc__,not_old_marked_D8=True,not_H_automorphism=True,groups=[[0,1,3,5],[2,4]],total_transported_certificates=total,sources=records,cpu_seconds=time.process_time()-st)
(P/'SIX_SOURCE_TRANSPORT.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k!='sources'})
