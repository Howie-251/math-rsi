"""Independent Krow-first lift domain and correctedC35-index fixed certificate replay. Only z-pivot pure2, no overlapping quota."""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction
import json,time,sys
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'));from independent_structure_bounds import independent_rows
st=time.process_time();d=json.loads((P/'RESULT.json').read_text());assert d['complete'] and d['strict_count']==470;PP=(3,5,6,9,10,12);base=d['base_counts'];expected=set()
for row in product(range(1,5),repeat=4):
 for a,b,c in product(range(4),range(4),range(5)):
  cc=(a,b,c,row[0]-a-b,row[1]-a-c,row[2]-b-c)
  if min(cc)<0 or sum(cc)>7 or cc[3]+cc[4]+cc[5]!=row[3]:continue
  if any(x>base[m] for m,x in zip(PP,cc)):continue
  c0=7-sum(cc)
  if c0>base[0]:continue
  expected.add((cc,c0,tuple(row)))
assert expected=={(tuple(z['pair_lifts']),z['c0'],tuple(z['Krow'])) for z in d['inputs']} and len(expected)==470
# At least2 actual bad unordered pairs among5 distinct4-links on16 free points:
# 20-|union|>=4, each intersecting unordered pair contributes at most3.
assert (20-16+2)//3==2

def falling(n,r):
 if n<r:return 0
 out=1
 for k in range(r):out*=n-k
 return out
profiles={}
for posz in (1,10,11,12):
 pos=(posz,8,9,20,21);a=posz-1-sum(k<posz for k in pos[1:]);b=21-posz-sum(k>posz for k in pos[1:]);assert a+b==16
 profiles[posz]={'a':a,'b':b,'W':str(Fraction(falling(a,4)*falling(b,4),falling(16,8)))}
assert profiles[10]['W']==profiles[12]['W']=='7/1430' and profiles[11]['W']=='7/1287'
rowsout=[];values=[];purecases=0;newlystrict=0
for z in d['cases']:
 cc=z['pair_lifts'];c0=z['c0'];picked={0:c0,**dict(zip(PP,cc))};masks=[]
 for m,n in enumerate(base):
  pick=picked.get(m,0)
  assert 0<=pick<=n
  masks.extend([2*m+1]*pick+[2*m]*(n-pick))
 assert len(masks)==35 and Counter(masks)==Counter({int(k):v for k,v in z['counts'].items()})
 assert sum(bool(m&1) for m in masks)==7 and all(sum(bool(m>>i&1) for m in masks)==v for i,v in enumerate((7,9,10,10,10)))
 pos=tuple(z['best']['positions']);q=2 if c0==5 else 0;assert q==z['pure_quota'];purecases+=bool(q)
 stubs=[frozenset(i+1 for i in range(5) if m>>i&1) for m in masks];rr=independent_rows(21,pos,stubs);W=Fraction(profiles[pos[0]]['W']);value=zero=Fraction();rows=[]
 for r in rr:
  loss=2*q*W if r['k']==pos[0] else Fraction();assert r['C']>=loss
  old=min(r['A'],r['B'],r['C']);new=min(r['A'],r['B'],r['C']-loss);zero+=old;value+=new
  src=z['best']['rows'][r['k']-1];assert old==Fraction(src['old_min']) and loss==Fraction(src['loss']) and new==Fraction(src['corrected_min'])
  rows.append({**{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()},'pure_loss':str(loss),'corrected_min':str(new)})
 assert value==Fraction(z['best']['bound'])<1 and zero==Fraction(z['best']['zero_bound'])
 newlystrict+=zero>=1;values.append(value);rowsout.append({'pair_lifts':cc,'c0':c0,'Krow':z['Krow'],'selected_degrees':[7,9,10,10,10],'expanded35_masks':masks,'positions':pos,'pure_quota':q,'W_at_z':str(W),'bound':str(value),'zero_bound_same_positions':str(zero),'rows':rows})
 assert time.process_time()-st<13
(P/'VERIFY_ROWS.json').write_text(json.dumps({'cases':rowsout},indent=2)+'\n')
out={'status':'PASS_COMPLETE470_ACTUAL_DOMAIN_AND_ALL_STRICT_CORRECTED_CERTIFICATES','scope':__doc__,'domain':470,'row_first_keys_equal':True,'strict':len(values),'maximum_bound':str(max(values)),'cases_with_c0five':purecases,'selected_corrected_certificate_zero_bound_nonstrict':newlystrict,'pure_weight_profiles':profiles,'only_one_unordered_pure_quota':2,'only_z_pivot_loss':'4W when c0=5; otherwise0','no_other_quota':True,'N':21,'locks':5,'free_vertices':16,'original_edge_indices':35,'ordered_distinct_pairs':1190,'rows':470*21,'cpu_seconds':time.process_time()-st}
(P/'VERIFY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
